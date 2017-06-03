## How to contribute to the Emoji Two library

### Help wanted!
1. If you want to contribute your creative skills, but have no idea which emoji you should be drawing, check the issues for missing characters to complete milestones, e.g. [Unicode 10.0](/EmojiTwo/emojitwo/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Unicode+10.0%22) or [Emoji 5.0](/EmojiTwo/emojitwo/issues?q=is%3Aopen+is%3Aissue+milestone%3A%22Emoji+5.0%22).
2. Assign yourself to any emoji you are planning to create.
3. Fork the project.
4. Create the SVG graphics in the respective branch (e.g. `unicode10` or `emoji5`) or a dedicated local branch (e.g. `u1f9ff`).
5. When you are finished or want feedback, open a pull request. Please select the correct remote branch and mention the issue number(s) of the emoji(s) affected.
6. Get praised. 🎉 💛

### Bugs
* Check the [current issues](/EmojiTwo/emojitwo/issues/) to be sure the bug has not already been reported.
* If you have written a patch for the bug submit a [pull request](/EmojiTwo/emojitwo/pulls) including your patch.
* Include a brief description of the issue and how your patch will solve it.

### Emoji artwork
* Unlike [Emojione](/Ranks/emojione-assets/), Emojitwo very much welcomes additions and changes to the artwork! 
  This is covered by the original and unrevokable [CC-BY](https://creativecommons.org/licenses/by/4.0/) license chosen for Emojione 2.x artwork by Ranks.com.
* Design suggestions are welcome. 
  They will be considered by the community. 
  There is no guarantee they will be adopted. 
* Notes on visual errors are also very much accepted, see [Bugs](#Bugs).
* Both can be submitted as issues or pull requests at Github. 
  Pull requests *must* contain the edited SVGs and *may* contain the respective PNGs generated from that.
* Keep in mind that although the main license is CC-BY 4.0, non-commercial and private use does not require attribution. 
  When submitting artwork, you allow non-commercial and private use without attribution.
* Do not backport designs from Emojione 3+ or other sets with more restrictive or unknown licenses! 
  Twemoji and Noto may have compatible licenses, but their design style is usually too different to be a good fit.
* We intend to provide graphics for all new emojis from upcoming releases of the [Unicode Standard](http://unicode.org/alloc/Pipeline.html) (i.e. codepoints) and of [Unicode Emoji](http://unicode.org/reports/tr51/proposed.html) (sequences). 
  Contributions are *highly* welcome!
  Pull requests should use the respective branch as a base, e.g. `Unicode10`, instead of `master`.
* We actively support the addition of graphics for new sequences even if they are not supported by any other vendor.

### SVG code style
* Most existing SVG files are minified. This *will* change. 
  New contributions *should* indent code to make it more readable.
* We support manual editing of SVG source code and therefore prefer semantic elements like `<ellipse>` and `<rect>` over more concise `path` notation.
* For legacy reasons, we currently prefer SVG attributes over CSS styles, e.g. `fill="#F00BA7"` instead of `style="fill: #F00BA7"`. This *may* change in the future.
* Contributions should reuse colors already used within the project. Documentation of the Emojitwo palette shall follow.
* All `<g>` elements *should* have a self-documenting `id` attribute, e.g. `mouth` instead of `g12`.
* Every file *should* be self-documenting with proper elements.
  - `<title>`[English CLDR short name](http://www.unicode.org/repos/cldr/tags/latest/common/annotations/en.xml) if available`</title>`
  - `<desc>`Codepoint(s), additional info`</desc>`
  - We currently do not embed meta data like Dublin Core, but this *may* change.

Thank you for your interest in contributing to this library.

Regards,

the Emojitwo maintainers
