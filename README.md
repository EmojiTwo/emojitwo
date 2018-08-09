# Emojione

Version 2.x of Emojione is no longer supported by [Ranks.com](https://emojione.com). 
Versions 3 and 4 have slightly different desigsn and new, more restrictive licensing terms.
Some people prefer the flat cartoon design and the FOSS license with actual access to the SVG sources.

# Emojitwo 

The artwork of the second generation of the web's first complete open source emoji set. It is and will stay 100% free and open source.

**We need help** from graphic designers to make more glyphs! 
See the [milestones](https://github.com/EmojiTwo/emojitwo/milestones), [projects](https://github.com/EmojiTwo/emojitwo/projects) and especially the issues tagged [`character artwork`](https://github.com/EmojiTwo/emojitwo/labels/character%20artwork) for details. 
Do not be afraid to ask for assistance, also boldly send pull requests. 
Every year Uniucode aims to release a couple dozen new emojis. 
Some of them come with gender and skin tone variants, but at least the latter can be generated automatically.

## Differences between Emojitwo and Emojione 2.x

Emojitwo is restricted to the artwork, i.e. image files.
SVG is its native format. Everything else is derived from that.

### Additions

+ Unicode 9 beta emojis Rifle and Modern Pentathlon have been resurrected: [U+1F946 &#x1f946;](https://github.com/EmojiTwo/emojitwo/blob/master/svg/1f946.svg), [U+1F93B &#x1f93b;](https://github.com/EmojiTwo/emojitwo/blob/master/svg/1f93b.svg).
+ Flag for deprecated region code `SU`: [U+1F1F8+1F1FA &#x1f1f8;&#x1f1fa](https://github.com/EmojiTwo/emojitwo/blob/master/svg/1f1f8-1f1fa.svg).
+ More ist listed in the [full changelog](CHANGELOG.md).

### Changes

* Documentation has been updated to
  1. encourage contributions to the artwork,
  2. use _Emojitwo_ or _Emoji Two_ instead of _Emojione_ or _Emoji One_ where appropriate.
* Some minor color optimizations.
* SVG source code prettified.

See the documentation for a more [detailed change log](doc/changes).

### Removals

- All programming libraries have been removed. Reusable meta data files will remain.

### Plans

Emojitwo shall eventually include graphics for new emojis:
https://github.com/EmojiTwo/emojitwo/milestones
  - Emoji characters defined in the [Unicode Standard 10.0]() (June 2017),  [Unicode Standard 11.0]() (June 2018) and later.
  - Sequences documented in [Unicode Emoji 4.0](http://www.unicode.org/reports/tr51/tr51-9.html) (November 2016), [5.0](http://www.unicode.org/reports/tr51/tr51-11.html) (March 2017) and later (UTR#51), e.g. flags.
  - Characters extended in [Unicode Emoji 11.0](http://www.unicode.org/reports/tr51/proposed.html) and later (UTS#51).
  - Existing Unicode characters without the `Emoji` property, especially to match other vendors (like Microsoft and Samsung).
  - Custom sequences and alternatives, especially those supported by other vendors.

Emojitwo shall adopt a more restricted color palette. Actual changes will be subtle and barely noticable. This will affect flags.

## Emojione 2.x Artwork License

*  Applies to all PNG and SVG files as well as any adaptations made.
    *  [License](LICENSE.md): Creative Commons Attribution 4.0 International
    *  Human Readable License: http://creativecommons.org/licenses/by/4.0/
    *  Complete Legal Terms: http://creativecommons.org/licenses/by/4.0/legalcode
  
### Emojione Artwork Attribution

With the release of version 3.0, the Emojione project also made changes to 2.2.7’s licensing. 
[Previously](https://web-beta.archive.org/web/20170327003706/http://emojione.com/licensing/#attribution), Emojione did not require attribution for non-commercial and personal use. Considering that the Emojione project only changed the documentation in that branch to mandate attribution in any case, Emojitwo forked a state before those changes for greater flexibility.

For **non-commercial** and **personal use**, you *should* credit the creators. 
For **commercial use**, proper attribution *must* be given on every web page, app, or video description where our emojis are displayed. 

### Creative Commons Requirements

In section 3(a)(1) of the CC-BY 4.0 legal terms, it lists the following as the guidelines needed to fulfill the attribution requirements:

> If You Share the Licensed Material (including in modified form), You must:
> - retain the following if it is supplied by the Licensor with the Licensed Material:
>     - identification of the creator(s) of the Licensed Material and any others designated to receive attribution, in any reasonable manner requested by the Licensor (including by pseudonym if designated);
>     - a copyright notice;
>     - a notice that refers to this Public License;
>     - a notice that refers to the disclaimer of warranties;
>     - a URI or hyperlink to the Licensed Material to the extent reasonably practicable;
> - indicate if You modified the Licensed Material and retain an indication of any previous modifications; and
> - indicate the Licensed Material is licensed under this Public License, and include the text of, or the URI or hyperlink to, this Public License."

### Proper Attribution Examples

Must contain:
- The original name _Emojione_ (or _Emoji One_) and the forked name _Emojitwo_ (or _Emoji Two_).
- Links to the repository and Ranks.com's website
    - https://github.com/EmojiTwo/emojitwo/ or https://emojitwo.github.io/emojitwo/
    - https://www.emojione.com
- The title and a link to the Creative Commons license
    - Creative Commons Attribution International 4.0 (CC-BY 4.0)
    - https://creativecommons.org/licenses/by/4.0/legalcode

Also helpful:
- Make sure it does not look like Ranks.com or the Emojitwo community created or endorsed your product.
- List all modifications you've made to the artwork. (Also consider to submit them for inclusion.)
- A reference to Ranks.com as original creators of Emojione.

### Ideal Attribution

> Emoji artwork is provided by [Emojitwo](https://emojitwo.github.io/), 
> originally released as [Emojione 2.2](https://www.emojione.com) by [Ranks.com](http://www.ranks.com)
> with contributions from the Emojitwo community
> and is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/legalcode).

### Attribution Location

#### Apps
- A note with link in the *app store description* is required.
- Other links and praise are much appreciated:
    - app settings
    - official app website
    - social media
    
#### Websites
- A note with link on *every web page* where our emojis are displayed is required.
- Other links and praise are much appreciated:
    - main homepage
    - social media
    
#### Web Videos
- A note with link in the *video description* is required.
- Other links and praise are much appreciated:
    - on-screen when emojis are displayed
    - on-screen in credits
    - social media

## Information

### Generating New Sprites

The sprites are not automatically updated and should be refreshed locally if you plan to use them. To do this, you must have [NPM](https://www.npmjs.com/),  [Grunt](https://gruntjs.com/), and [ImageOptim](https://imageoptim.com/mac) installed on your machine. 

From the root of the project, first install Node modules:
```$ npm install```

Then generate new sprites and css by executing:
```grunt```
*Note:* the ImageOptim process takes a few minutes to optimize the PNG sprite.

### Bug reports

If you discover any bugs, feel free to create an issue on GitHub. We also welcome the open-source community to contribute to the project by forking it and issuing pull requests.

 *  https://github.com/EmojiTwo/emojitwo/issues
 *  https://github.com/emojione/emojione-assets/issues
 *  https://github.com/emojione/emojione/issues

### Contact

If you have any questions, comments, or concerns you are also welcome to contact the maintainers and major contributors directly.

* https://twitter.com/informoji

### Alternatives
We sincerely hope that you choose to use Emojitwo and support our project, but if you feel like it's not for you, please have a look at these possible alternatives:

* [Emojione 1.5.2 (SVG/PNG)](https://github.com/emojione/emojione-legacy/) (CC-BY-4.0)
* [Emojione 3.0 (PNG)](https://github.com/emojione/emojione-legacy/) (CC-BY-4.0)
* [Twitter Twemoji (SVG/PNG)](https://github.com/twitter/twemoji/) (CC-BY-4.0)
* [Google Noto Emoji (SVG/PNG)](https://github.com/googlei18n/noto-emoji/) (Apache License 2.0)
  * [Blobmoji (SVG/PNG)](https://github.com/c1710/blobmoji) (Apache License 2.0), a maintained fork of the pre-2017 Noto style
* [Emojidex (SVG)](https://github.com/emojidex/emojidex-vectors)/[(PNG)](https://github.com/emojidex/emojidex-rasters) (custom license)
