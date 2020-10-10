#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# By HarJIT in 2020. MIT/Expat licence.

import os, shutil

preexisting = (0x261e, 0x261f, 0x1f6b5, 0x1f6b6, 0x1f6c0, 0x1f918, 0x1f919, 0x1f91a, 0x1f385, 0x1f3c3, 0x1f3c4, 0x1f3c7, 0x1f3ca, 0x1f3cb, 0x1f449, 0x1f44a, 0x1f44b, 0x1f44c, 0x1f44d, 0x1f44e, 0x1f44f, 0x1f450, 0x1f466, 0x1f467, 0x1f468, 0x1f469, 0x1f472, 0x1f473, 0x1f474, 0x1f475, 0x1f476, 0x1f477, 0x1f478, 0x1f47c, 0x1f481, 0x1f482, 0x1f483, 0x1f485, 0x1f486, 0x1f487, 0x1f4aa, 0x1f46e, 0x1f470, 0x1f6b4, 0x261c, 0x261d, 0x270a, 0x270b, 0x270c, 0x1f91b, 0x1f91c, 0x1f91d, 0x1f91e, 0x1f471, 0x1f6a3, 0x270d, 0x1f575, 0x1f58e, 0x1f590, 0x1f595, 0x1f596, 0x1f597, 0x1f645, 0x1f646, 0x1f647, 0x1f64b, 0x1f64c, 0x1f64d, 0x1f64e, 0x1f64f, 0x1f57a, 0x26f9, 0x1f442, 0x1f443, 0x1f446, 0x1f447, 0x1f448, 0x1f934, 0x1f935, 0x1f936, 0x1f938, 0x1f939, 0x1f93b, 0x1f93c, 0x1f93d, 0x1f926, 0x1f930, 0x1f933, 0x1f93e, 0x1f937)

# Note: yellow for ligtning and other uses is #ffce31, while the default skin tone is #ffdd67.
modifiers = (None, 0x1F3FB, 0x1F3FC, 0x1F3FD, 0x1F3FE, 0x1F3FF)
skin   = ("#ffdd67", "#ffe1bd", "#fed0ac", "#d6a57c", "#b47d56", "#8a6859")
shadow = ("#eba352", "#e6b796", "#e0a372", "#b58360", "#935e3e", "#705041")
hair   = ("#ffb300", "#594640", "#dbb471", "#594640", "#231f20", "#231f20")
lips   = ("#f09985", "#e08672", "#e08672", "#b58360", "#935e3e", "#7d5442")
lshad  = ("#d47f6c", "#b86e5d", "#b86e5d", "#805c44", "#734c31", "#5c3f34")

cra, cga, cba = (0xFF, 0x05, 0x97) # i.e. avgs with s to get c
cheeks = []
for n, i in enumerate(skin):
    sr, sg, sb = int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)
    cr, cg, cb = (sr + cra) // 2, (sg + cga) // 2, (sb + cba) // 2
    cheeks.append(f"#{cr:02x}{cg:02x}{cb:02x}")
csra, csga, csba = (0xD9, 0x0F, 0x86) # i.e. avgs with ss to get cs
cshad = []
for n, i in enumerate(shadow):
    ssr, ssg, ssb = int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)
    csr, csg, csb = (ssr + csra) // 2, (ssg + csga) // 2, (ssb + csba) // 2
    cshad.append(f"#{csr:02x}{csg:02x}{csb:02x}")
bra, bga, bba = (0x23, 0x0D, -0x1F) # i.e. avgs with s to get b
brow = []
for n, i in enumerate(skin):
    sr, sg, sb = int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)
    br, bg, bb = (sr + bra) // 2, (sg + bga) // 2, (sb + bba) // 2
    brow.append(f"#{br:02x}{bg:02x}{bb:02x}")
kra, kga, kba = (-0x1F, -0x07, -0x04) # i.e. avgs with ss to get k
keycol = []
for n, i in enumerate(shadow):
    ssr, ssg, ssb = int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)
    kr, kg, kb = (ssr + kra) // 2, (ssg + kga) // 2, (ssb + kba) // 2
    keycol.append(f"#{kr:02x}{kg:02x}{kb:02x}")
ara, aga, aba = (0xB1, 0x75, 0x1B) # i.e. avgs with s to get a
accent = []
for n, i in enumerate(skin):
    sr, sg, sb = int(i[1:3], 16), int(i[3:5], 16), int(i[5:7], 16)
    ar, ag, ab = (sr + ara) // 2, (sg + aga) // 2, (sb + aba) // 2
    accent.append(f"#{ar:02x}{ag:02x}{ab:02x}")

for i in os.listdir("svg"):
    if "draft" in i:
        continue
    if int(i.split("-", 1)[0].split(".", 1)[0], 16) in list(range(0x1F1E6, 0x1F200)) + [0x1F3F3, 0x1F3F4]:
        continue # Don't mess around with flags
    if int(i.split("-", 1)[0].split(".", 1)[0], 16) in preexisting:
        continue # Already dealt with prior to this script's creation
    with open(os.path.join("svg", i), "r") as f:
        b = f.read()
    if "#ffdd67" in b and "-" not in i:
        for mno, modifier in list(enumerate(modifiers))[1:]:
            mod = b.replace(skin[0], skin[mno])
            mod = mod.replace(shadow[0], shadow[mno])
            mod = mod.replace(hair[0], hair[mno])
            mod = mod.replace(lips[0], lips[mno])
            mod = mod.replace(lshad[0], lshad[mno])
            mod = mod.replace(cheeks[0], cheeks[mno])
            mod = mod.replace(cshad[0], cshad[mno])
            mod = mod.replace(brow[0], brow[mno])
            mod = mod.replace(keycol[0], keycol[mno])
            mod = mod.replace(accent[0], accent[mno])
            ofn = os.path.join("svg", i).replace(".svg", f"-{modifier:04x}.svg")
            print("Writing", ofn)
            with open(ofn, "w") as f:
                f.write(mod)



