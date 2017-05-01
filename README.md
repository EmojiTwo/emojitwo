# Emojione

Version 2.x of Emojione is no longer supported by [Ranks.com](https://emojione.com). 
Version 3 has a slightly different design and new, more restrictive licensing terms.
Some people prefer the flat cartoon design and the FOSS license with actual access to the SVG sources.

# EmojiTwo 

The artwork of the second generation of the web's first complete open source emoji set. It is and will stay 100% free.

## Differences between Emojitwo and Emojione 2.x

Emojitwo is restricted to the artwork, i.e. image files.
SVG is its native format. Everything else is derived from that.

As of its initial release in April 2017, Emojitwo did not contain any additional artwork.

### Additions

+ Unicode 9 beta emojis Rifle and Modern Penthatlon have been resurrected.

### Changes

* Documentation has been updated to
  1. encourage contributions to the artwork,
  2. use _Emoji Two_ instead of _Emoji One_ where appropriate.

### Removals

- All programming libraries have been removed. Reusable meta data files will remain.

### Plans

Emojitwo shall eventually include graphics for new emojis:

  - Characters defined in the [Unicode Standard 10.0]() (June 2017) and later.
  - Sequences documented in [Unicode Emoji 5.0](http://www.unicode.org/reports/tr51/tr51-11.html) (March 2017) and later (UTR#51), e.g. flags.
  - Characters extended in [Unicode Emoji 6.0](http://www.unicode.org/reports/tr51/proposed.html) and later (UTS#51).
  - Existing Unicode characters without the `Emoji` property, especially to match other vendors (especially Microsoft and Samsung).
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

### Bug reports

If you discover any bugs, feel free to create an issue on GitHub. We also welcome the open-source community to contribute to the project by forking it and issuing pull requests.

 *  https://github.com/EmojiTwo/emojitwo/issues
 *  https://github.com/Ranks/emojione-assets/issues
 *  https://github.com/Ranks/emojione/issues

### Contact

If you have any questions, comments, or concerns you are welcome to contact the major contributors directly.

* https://twitter.com/informoji
* [![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/Ranks/emojione?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

### Alternatives
We sincerely hope that you choose to use Emojitwo and support our project, but if you feel like it's not for you, please have a look at these possible alternatives:

* [Emojione 1.5.2 (SVG/PNG)](/Ranks/emojione-legacy/) (CC-BY-4.0)
* [Emojione 3.0 (PNG)](/Ranks/emojione-legacy/) (CC-BY-4.0)
* [Twitter Twemoji (SVG/PNG)](/twitter/twemoji/) (CC-BY-4.0)
* [Google Noto Emoji (SVG/PNG)](/googlei18n/noto-emoji/) (Apache License 2.0)
* [Emojidex (SVG)](/emojidex/emojidex-vectors)/[(PNG)](https://github.com/emojidex/emojidex-rasters) (custom license)
