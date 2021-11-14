#!/usr/bin/env python3
# -*- mode: python; coding: utf-8 -*-
# By HarJIT in 2020. MIT/Expat licence.

import ast, os, glob

dat = ast.literal_eval(open("BlendedEmojiData.txt").read())

for (kind, aff) in (("Colour", ""), ("B/W", "-BW")):
    exists = [os.path.basename(pn) for pn in glob.glob("**/*.svg", recursive=True)]
    sumps = {
        # Properties: ([presents…], [absents…])
        "ID.DoCoMo": ([], []),
        "ID.au": ([], []),
        "ID.SoftBank": ([], []),
        "SBCS.Webdings": ([], []),
        "SBCS.Wingdings_1": ([], []),
        "SBCS.Wingdings_2": ([], []),
        "SBCS.Wingdings_3": ([], []),
        "SBCS.ZapfDingbats": ([], []),
        "JIS.ARIB": ([], []),
        "JIS.2004": ([], []),
        "MBCS_EUC.Wansung": ([], []),
        "MBCS_EUC.KPS": ([], []),
    }
    # May be lower than the sum due to overlap between sets
    total_present = []
    total_wanted = []
    for i in dat:
        for key in ("UCS.Standard", "UCS.PUA.SoftBank", "UCS.PUA.Google",
                    "UCS.PUA.au.web", "UCS.PUA.DoCoMo"):
            if key in dat[i]:
                j = dat[i][key].replace("\u200d", "").replace("\ufe0f", "")
                k = "{}{}.svg".format("-".join("{:04x}".format(ord(m)) for m in j), aff)
                if k in exists:
                    for m in sumps:
                        if m in dat[i]:
                            sumps[m][0].append(dat[i]) # present
                    total_present.append(dat[i])
                    break
        else: # i.e. didn't encounter break
            j = i.replace("\u200d", "").replace("\ufe0f", "")
            k = "{}{}.svg".format("-".join("{:04x}".format(ord(m)) for m in j), aff)
            print(k, i)
            for m in sumps:
                if m in dat[i]:
                    sumps[m][1].append(dat[i]) # absent
            total_wanted.append(dat[i])
    print()
    for i in sumps:
        print("{} {}: {:d} present, {:d} wanted: ".format(i, kind, len(sumps[i][0]), len(sumps[i][1])),
                *(j["UCS.Standard"] for j in sumps[i][1] if "UCS.Standard" in j))
    print("Overall {}: {:d} present, {:d} wanted".format(kind, len(total_present), len(total_wanted)))







