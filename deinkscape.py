#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# By HarJIT in 2020. MIT/Expat licence.

import os, xml.dom.minidom, shutil, re, glob

svgpresattrs = ("alignment-baseline", "baseline-shift", "clip", "clip-path", "clip-rule", "color", 
"color-interpolation", "color-interpolation-filters", "color-profile", "color-rendering", "cursor", 
"direction", "display", "dominant-baseline", "enable-background", "fill", "fill-opacity", 
"fill-rule", "filter", "flood-color", "flood-opacity", "font-family", "font-size", 
"font-size-adjust", "font-stretch", "font-style", "font-variant", "font-weight", 
"glyph-orientation-horizontal", "glyph-orientation-vertical", "image-rendering", "kerning", 
"letter-spacing", "lighting-color", "marker-end", "marker-mid", "marker-start", "mask", "opacity", 
"overflow", "pointer-events", "shape-rendering", "solid-color", "solid-opacity", "stop-color", 
"stop-opacity", "stroke", "stroke-dasharray", "stroke-dashoffset", "stroke-linecap", 
"stroke-linejoin", "stroke-miterlimit", "stroke-opacity", "stroke-width", "text-anchor", 
"text-decoration", "text-rendering", "transform", "unicode-bidi", "vector-effect", 
"visibility", "word-spacing", "writing-mode")

needlessline = re.compile("(?m)^\s*\n")

def has_real_dc(document):
    if document.getElementsByTagName("cc:license"):
        return True
    elif document.getElementsByTagName("cc:License"):
        return True
    elif document.getElementsByTagName("dc:contributor"):
        return True
    elif document.getElementsByTagName("cc:Agent"):
        return True
    elif document.getElementsByTagName("cc:permits"):
        return True
    elif document.getElementsByTagName("cc:requires"):
        return True
    return False

for pn in glob.glob("**/*.svg", recursive=True):
    i = os.path.basename(pn)
    if "draft" in i.casefold():
        continue
    document = xml.dom.minidom.parse(pn)
    changed = False
    keep_metadata = has_real_dc(document)
    retain_ns = ["xmlns:xlink"]
    if keep_metadata:
        retain_ns.extend(["xmlns:rdf", "xmlns:cc", "xmlns:dc"])
    for element in document.getElementsByTagName("*"):
        if element.nodeName == "metadata" and not keep_metadata:
            print(i, "removing", element.nodeName)
            changed = True
            element.parentNode.removeChild(element)
        elif element.nodeName == "defs":
            if (not element.childNodes) or (len(element.childNodes) == 1 and
                    element.firstChild.nodeName == "#text" and
                    not element.firstChild.wholeText.strip()):
                print(i, "removing", element.nodeName)
                changed = True
                element.parentNode.removeChild(element)
        elif element.nodeName.startswith(("inkscape:", "sodipodi:")):
            print(i, "removing", element.nodeName)
            changed = True
            element.parentNode.removeChild(element)
        #
        if element.hasAttribute("style"):
            # Rip SVG pres. attributes out of inline CSS, replacing any overridden attributes
            # Note: this will bork on quoted ; in values, which I don't expect to occur.
            stylelist = element.getAttribute("style").strip(";").split(";")
            styleout = ""
            for style in stylelist:
                if ":" not in style:
                    continue # nvm
                name, val = style.split(":", 1)
                if name in svgpresattrs:
                    print(i, "attributising", name)
                    changed = True
                    element.setAttribute(name.strip(), val.strip())
                elif "inkscape" in name:
                    print(i, "removing", name)
                    changed = True
                    pass
                else:
                    print(i, "retaining", name)
                    changed = True
                    styleout += style + ";"
            if not styleout:
                element.removeAttribute("style")
            else:
                element.setAttribute("style", styleout)
        for attr in list(element.attributes.keys())[:]:
            if attr.startswith("stroke-") and not element.hasAttribute("stroke") and not (element.nodeName == "g"):
                print(i, "removing", attr)
                changed = True
                element.removeAttribute(attr)
            elif attr.startswith("inkscape:") or attr.startswith("sodipodi:"):
                print(i, "removing", attr)
                changed = True
                element.removeAttribute(attr)
            elif attr.startswith("xmlns:") and attr not in retain_ns:
                print(i, "removing", attr)
                changed = True
                element.removeAttribute(attr)
            elif (element.nodeName == "svg") and (attr == "version"):
                print(i, "removing", attr)
                changed = True
                element.removeAttribute("version")
            elif attr == "fill-opacity" and element.getAttribute("fill-opacity") == "1":
                print(i, "removing", attr)
                changed = True
                element.removeAttribute("fill-opacity")
        if element.hasAttribute("stroke"):
            print(i, "has stroke")
        if element.hasAttribute("id") and ((not element.parentNode) or
                element.parentNode.nodeName != "defs"):
            # Autogenerated ID rubbish
            if re.compile(r"^{}\d+$".format(element.nodeName)).match(element.getAttribute("id")):
                print(i, "removing ID", element.getAttribute("id"))
                changed = True
                element.removeAttribute("id")
    if changed:
        shutil.move(pn, pn + "~")
        with open(pn, "w") as f:
            x = document.toxml().replace("<?xml version=\"1.0\" ?>", "")
            f.write("".join(needlessline.split(x)))
            os.unlink(pn + "~")







