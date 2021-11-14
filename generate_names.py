#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# By HarJIT in 2020. MIT/Expat licence.

import os, xml.dom.minidom, unicodedata, shutil, glob

cldrnames = {}
_document = xml.dom.minidom.parse("CLDR/annotations/en.xml")
for _i in _document.getElementsByTagName("annotation"):
    if _i.hasAttribute("type") and _i.getAttribute("type") == "tts":
        cldrnames[_i.getAttribute("cp")] = _i.firstChild.wholeText
_document = xml.dom.minidom.parse("CLDR/annotationsDerived/en.xml")
for _i in _document.getElementsByTagName("annotation"):
    if _i.hasAttribute("type") and _i.getAttribute("type") == "tts":
        cldrnames[_i.getAttribute("cp")] = _i.firstChild.wholeText
rcldrnames = dict(zip(cldrnames.values(), (i.casefold() for i in cldrnames.keys())))
for i in list(cldrnames.keys())[:]:
    cldrnames[i.replace("\u200D", "")] = cldrnames[i]

def get_cldrname(ucs):
    if ucs in cldrnames:
        return cldrnames[ucs]
    if len(ucs) == 1:
        altname = unicodedata.name(ucs, None)
        if altname:
            altname = altname.title()
            if altname.casefold() in rcldrnames:
                altname = "Unicode " + altname
            return altname
    if len(ucs) > 1:
        n = [get_cldrname(i) for i in ucs]
        if None not in n:
            ret = ", ".join(n)
            if ret.endswith("skin tone"):
                ret = ":".join(ret.rsplit(",", 1))
            return ret
    return None

print("Sorting out names")
for pn in glob.glob("**/*.svg", recursive=True):
    if "node_modules" in pn or "other" in pn or "sprites" in pn:
        continue
    i = os.path.basename(pn)
    if "draft" in i.casefold():
        continue
    ucs = "".join(chr(int(j, 16)) for j in os.path.splitext(i)[0].replace("-BW", "").split("-"))
    document = xml.dom.minidom.parse(pn)
    cldrname = get_cldrname(ucs)
    if cldrname:
        if not document.getElementsByTagName("title"):
            title = document.createElement("title")
            title.appendChild(document.createTextNode(cldrname))
            document.documentElement.insertBefore(title, document.documentElement.firstChild)
            document.documentElement.insertBefore(document.createTextNode("\n    "), title)
            #print("Adding name to", i)
        else:
            title = document.getElementsByTagName("title")[0]
            if "," not in cldrname and title.firstChild.wholeText.strip().casefold() != cldrname.casefold():
                for j in title.childNodes:
                    title.removeChild(j)
                title.appendChild(document.createTextNode(cldrname))
                #print("Updating name of", i)
        if cldrname.startswith("Unicode "):
            cfn = cldrname[8:].casefold()
            collision = rcldrnames[cfn]
            collision = "-".join("{:04x}".format(ord(j)) for j in collision)
            comment = "CLDR {!r} is {}".format(cfn, collision)
            print(comment)
            if title.lastChild.nodeName != "#comment": # i.e. if not already added.
                title.appendChild(document.createComment(comment))
        shutil.move(pn, pn + "~")
        with open(pn, "w") as f:
            x = document.toxml().replace("<?xml version=\"1.0\" ?>", "")
            f.write(x)
            os.unlink(pn + "~")







