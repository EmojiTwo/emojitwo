#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# By HarJIT in 2020. MIT/Expat licence.

import os, shutil, glob

preexisting = (0x261e, 0x261f, 0x1f6b5, 0x1f6b6, 0x1f6c0, 0x1f918, 0x1f919, 0x1f91a, 0x1f385, 0x1f3c3, 0x1f3c4, 0x1f3c7, 0x1f3ca, 0x1f3cb, 0x1f449, 0x1f44a, 0x1f44b, 0x1f44c, 0x1f44d, 0x1f44e, 0x1f44f, 0x1f450, 0x1f466, 0x1f467, 0x1f468, 0x1f469, 0x1f472, 0x1f473, 0x1f474, 0x1f475, 0x1f476, 0x1f477, 0x1f478, 0x1f47c, 0x1f481, 0x1f482, 0x1f483, 0x1f485, 0x1f486, 0x1f487, 0x1f4aa, 0x1f46e, 0x1f470, 0x1f6b4, 0x261c, 0x261d, 0x270a, 0x270b, 0x270c, 0x1f91b, 0x1f91c, 0x1f91d, 0x1f91e, 0x1f471, 0x1f6a3, 0x270d, 0x1f575, 0x1f58e, 0x1f590, 0x1f595, 0x1f596, 0x1f597, 0x1f645, 0x1f646, 0x1f647, 0x1f64b, 0x1f64c, 0x1f64d, 0x1f64e, 0x1f64f, 0x1f57a, 0x26f9, 0x1f442, 0x1f443, 0x1f446, 0x1f447, 0x1f448, 0x1f934, 0x1f935, 0x1f936, 0x1f938, 0x1f939, 0x1f93b, 0x1f93c, 0x1f93d, 0x1f926, 0x1f930, 0x1f933, 0x1f93e, 0x1f937)

# Note: yellow for lightning and other uses is #ffce31, while the default skin tone is #ffdd67.
modifiers = (None, 0x1F3FB, 0x1F3FC, 0x1F3FD, 0x1F3FE, 0x1F3FF)
skin   = ("#ffdd67", "#ffe1bd", "#fed0ac", "#d6a57c", "#b47d56", "#8a6859")
shadow = ("#eba352", "#e6b796", "#e0a372", "#b58360", "#935e3e", "#705041")
hair   = (("#ffb300",
         "#ffbc00"), "#594640", "#dbb471", "#594640", "#231f20", "#231f20")
lips   = ("#f09985", "#e08672", "#e08672", "#b58360", "#935e3e", "#7d5442")
lshad  = (("#d47f6c",
         "#e2596c"), "#b86e5d", "#b86e5d", "#805c44", "#734c31", "#5c3f34")
cheeks = ("#ff717f", "#ff73aa", "#fe6aa1", "#ea5589", "#d94176", "#c43678")
cshad  = ("#ea5589", "#df638e", "#dc597c", "#c74973", "#b63662", "#a42f63")
brow   = ("#917524", "#91774f", "#906e46", "#7c592e", "#6b451b", "#563a1d")
keycol = ("#664e27", "#635849", "#604e37", "#4b3e2e", "#3a2b1d", "#28241e")
keycl2 = ("#937237", "#91774f", "#947151", "#7c592e", "#664e27", "#594640")
accent = (("#d6a57c",
         "#d8a941"), "#e0a372", "#e0a372", "#b58360", "#8a6859", "#947151")

def simulreplace(b, *args):
    if not args:
        return b
    frm, to = args[0]
    if isinstance(frm, tuple):
        if len(frm) == 1:
            frm, = frm
        else:
            return to.join(simulreplace(i, (frm[1:], to), *args[1:]) for i in b.split(frm[0]))
    return to.join(simulreplace(i, *args[1:]) for i in b.split(frm))

for pn in glob.glob("**/*.svg", recursive=True):
    if "node_modules" in pn or "other" in pn or "sprites" in pn:
        continue
    i = os.path.basename(pn)
    if "draft" in i.casefold():
        continue
    if int(i.split("-", 1)[0].split(".", 1)[0], 16) in list(range(0x1F1E6, 0x1F200)) + [0x1F3F3, 0x1F3F4]:
        continue # Don't mess around with flags
    if int(i.split("-", 1)[0].split(".", 1)[0], 16) in preexisting:
        continue # Already dealt with prior to this script's creation
    with open(pn, "r") as f:
        b = f.read()
    if "#ffdd67" in b and "-" not in i:
        for mno, modifier in list(enumerate(modifiers))[1:]:
            mod = simulreplace(b, (skin[0], skin[mno]),
                                  (shadow[0], shadow[mno]),
                                  (hair[0], hair[mno]),
                                  (lips[0], lips[mno]),
                                  (lshad[0], lshad[mno]),
                                  (cheeks[0], cheeks[mno]),
                                  (cshad[0], cshad[mno]),
                                  (brow[0], brow[mno]),
                                  (keycol[0], keycol[mno]),
                                  (keycl2[0], keycl2[mno]),
                                  (accent[0], accent[mno]))
            ofn = pn.replace(".svg", f"-{modifier:04x}.svg")
            print("Writing", ofn)
            with open(ofn, "w") as f:
                f.write(mod)



