- There is a `ch` length unit that can be used in modern browsers (i.e. except IE).
- A stylus [`@media` query](http://stylus-lang.com/docs/media.html) can be included inside an element whose styles you want to change contextually.
- [BEM](http://getbem.com/) (block-element-modifier) is a naming convention, not a tool. [For example](https://css-tricks.com/bem-101/), a block (e.g. `.btn`) might come with elements (e.g. `.btn__price`, `.btn__text`) and modifiers that change the block (e.g. `.btn--big`, `.btn--orange`). You may notice that SASS solves these problems, but sometimes you don't have SASS.
- The original "web colours" came from [X11](https://news.ycombinator.com/item?id=20137446). Netscape literally gave the colour codes to X11, which then renders the colours. Netscape got colour support for free. "Because X11 shipped with a suite of pre-defined colour names, Netscape supported those pre-defined colour names. Because X11 supported custom colours in #RGB, #RRGGBB and #RRRRGGGGBBBB syntax, Netscape supported those too."
- [Attributes beginning with `--`](https://stackoverflow.com/a/40055702), for example `--main-color: #000`, are custom properties used elsewhere, for example a computation. [Ionic components use custom properties](https://ionicframework.com/docs/api/menu#css-custom-properties).
- Class names are `dash-separated` because [it allows for a selector like `[class^="foo-"]`](https://stackoverflow.com/a/20811902/1558430) to target `foo-bar`, which starts with `foo`, but not target `fooBar`, which also starts with `foo`.
- Styling for the iPhone X basically means messing with the platform-specific [`safe-area-inset-top`](https://www.quirksmode.org/blog/archives/2017/10/safeareainset_v.html) value right after your normal rules, which will not be overridden by your `inset-` thing because it is invalid on any other platform, and is 0 on any iOS device that is not the iPhone X.
- [`normalize.css`](https://github.com/necolas/normalize.css/blob/master/normalize.css) is a ~350 line CSS file, more than half of which are comments.
- CSS3 has `background-size`, whose most useful values are `cover` (scaled and cropped) and `contain` (scaled to fit).
- `text-overflow` allows [custom truncation characters][mozilla]. It is CSS3. For everything else, there's [mastercard](http://dotdotdot.frebsite.nl/).
- Chrome doesn't support two-valued text-overflows, e.g. `clip ellipsis`.
- Relative paths in an external CSS file is [relative to the file][stackoverflow].
- A `:before` selector with `content: "|";` solves many problems, including stupid site menu separators.
- Web components ([decorators][w3]): basically, js templating without the js. Dayum.
- All you need to make an oval subtraction is `border-radius: 50%;`.
- CSS pseudo elements [do not exist in the DOM][stackoverflow 2].
- For the geeky: `ul { list-style-type: binary; }`
- `calc` (`calc(100% - 40px);`) works in [IE9+, prefix-free][tutorialzine].
- [You can already][tutorialzine] use expressions like `content:attr(data-title)` for `:before` selectors that have a `data-title`.
- Everyone except IE8 supports [multiple background images](http://caniuse.com/#feat=multibackgrounds), in the format `background:url('abc.png') repeat x y, url('def.png') repeat x y`.
- It was apparently agreed upon that webapp buttons be used in conjunction with [a normal cursor][stackoverflow 3] instead of a hand.
- Can't set a container's width and height based on the ratio of its background image? [Have an invisible image tag inside the container][stackoverflow 4] so the container displays its background image according to the shrunk ratio of its invisible children.
- There is something called the [`rem` size unit][snook] in CSS3, which stands for "root em". It is the em size multiplied by its parents' size values (e.g. 10rem in a 80% parent is effective 8em)
- [CSS triangles -- a tragedy in five acts][stackoverflow 5] (essentially, three sides of borders combined with something with neither width nor height)
- Can you use scoped css (`<style scoped>`)? [No](http://caniuse.com/style-scoped), you cannot use scoped CSS.
- [`:visited`][mozilla 2] can only change `color`, `background-color`, and [other forms of colour](https://www.w3schools.com/cssref/sel_visited.asp).
- [`:visited`][mozilla 2] cannot be read by JavaScript.
- `transform: translate/scale/rotate/skew/matrix npx npx` and `opacity` apparently [do not trigger repaints](http://aerotwist.com/blog/pixels-are-expensive/) and are thus CPU-friendly. (This does not apply to non-px animations)
- iOS 6/7 support `position: sticky`, which is like `fixed` except dependent on where the element is relative to the viewport.
- IE8 and under have a 4095-CSS-selector limit in any given page.
- There is a [`text-rendering: optimizeLegibility`](http://aestheticallyloyal.com/public/optimize-legibility/) flag that makes kerning look "normal" according to what the browser. However, page rendering is (slightly) slower, text will sometimes disappear if combined with `text-transform: small-caps`, and disappear completely in WebOS.
- Transforms and translates [_will_ mess with z-indices](http://dabblet.com/gist/2463684) by [creating a different stacking context](http://stackoverflow.com/a/10814448), so use these optimisations only when necessary.
- `backface-visibility: hidden` means that, if you flip an object by the z-axis (revealing its back, or _backface_), the object will be hidden instead of inverted.
- `local('☺')` means ["never use the local font"](http://stackoverflow.com/q/3698319/1558430).
- [Uncommon selectors](http://code.tutsplus.com/tutorials/the-30-css-selectors-you-must-memorize--net-16048):
  - `a:link` (never clicked) and `a:visited` (clicked)
  - `div + p`: only `p`s immediately after a div
  - `div ~ p`: only `p`s immediately before a div
  - `a[href]`: `a`s with any `href`. See also: `a[href^="foo"]` (starts with), `a[href$="foo"]` (ends with), `a[href*="foo"]` (anywhere), and `a[href~="foo"]` (if `href`, a space-separated value, contains `foo`).
- [Pull and exact amount left and right opposite to each other](http://stackoverflow.com/questions/20979062/bootstrap-right-column-on-top-on-mobile-view) to have a bootstrap left column to appear at the bottom in mobile view.
- Specificity are defined in sets; `(0,0,999,0)` (999 classes) is never greater than `(0,1,0,0)` (one id).
- [Flexbox](http://caniuse.com/#feat=flexbox) is in fact already usable in all reasonable browsers (that is, not IE).
- Flexbox isn't the end-all, either. It has a [known list of Flexbox bugs](https://github.com/philipwalton/flexbugs) across supported browsers that you should know about.
- Set a dummy whose top margin is "100%" to have an element [whose height is the same as its width](http://jsfiddle.net/ansciath/B8FU8/).
- Such a font as [OpenDyslexic](http://opendyslexic.org/) exists.
- A [tracking](http://www.presslabs.com/blog/web-typography-for-non-designers/) of 100 is [0.1em](http://stackoverflow.com/a/10376142/1558430). Also, 1em is simply 1000.
- Gradient generators are [discouraged](http://codepen.io/thebabydino/full/pjxVWp) because they generate `-ms-` attributes that never worked in the first place.
- [`@font-face`](https://www.reddit.com/r/netsec/comments/3py3f2/css_based_attack_abusing_unicoderange_of_fontface/) can be used to leak characters in a secure text field. The workaround is specifying a [content security policy](http://www.html5rocks.com/en/tutorials/security/content-security-policy/) whitelist.
- [Enforce HTML semantics](http://www.ebaytechblog.com/2015/11/04/how-our-css-framework-helps-enforce-accessibility/) by only using semantic selectors.
- A `::selection` pseudoselector may be effective against text selection on your website:

```
*::selection {
    display: none !important;  /* annoy all your users */
}
```

- `content: ...` (or any attribute, really) can be set to the [content of some other attribute](https://github.com/chinchang/hint.css/blob/master/hint.css#L65), using something like `content: attr(data-some-other-attribute);`.
- `font-weight: strong` is not a thing. The correct alias is `font-weight: bold`.
- Style a `<path>` with `stroke-dasharray: 5` to make it a dashed line (5px step). `5,10` would have dashes that are 10px spaced out.
- [w3schools](http://www.w3fools.com/) says that [`pt` (in/72), `px` (in/96), and `pc` (in/6) should not be used on screen](https://www.w3schools.com/cssref/css_units.asp) because their absolute sizing means different-sized screens show them differently, and "the em and rem units are practical in creating perfectly scalable layout!"
- You can select an element in the shadow DOM with [`::part(foo)`](https://developer.mozilla.org/en-US/docs/Web/CSS/::part) only if the element has `part="foo"` in it. It cannot be chained. `::part(foo) #bar` will match exactly nothing. Ionic framework gets around this by exposing [custom properties on each component](https://ionicframework.com/docs/api/item#css-custom-properties), where specifying a variable (prefixed with `--`) will let it be used within the shadow DOM.

## XPath

- `//` is _root_ if used at the start, or _any descendant_ if used anywhere else.
- `/` is _from anywhere_ if used at the start, or _direct descendant_ if used anywhere else.
- `img[@src="wat"]` filters `img` tags by `src`. The same works for data attributes.

## [Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

- Containers all have `display: flex`.
- If you want the items to wrap around, add `flex-wrap: wrap` to the container.
- Vertical-align items inside the container with `align-items: flex-start (top), center (middle), flex-end (bottom), stretch (every item is full height)`.

## Design

- "This redesign incorporates two of the worst design trends today: _very low contrast text_ and _gratuitously, obnoxiously large fixed headers._"

Takeaway: _Use high-contrast text_. **Don't use fixed headers**.

[mozilla]: https://developer.mozilla.org/en-US/docs/Web/CSS/text-overflow
[mozilla 2]: https://blog.mozilla.org/security/2010/03/31/plugging-the-css-history-leak/
[snook]: http://snook.ca/archives/html_and_css/font-size-with-rem
[stackoverflow]: http://stackoverflow.com/questions/940451/using-relative-url-in-css-file-what-location-is-it-relative-to
[stackoverflow 2]: http://stackoverflow.com/questions/9395858/event-listener-on-a-css-pseudo-element-such-as-before-or-after
[stackoverflow 3]: http://stackoverflow.com/questions/4121854/is-it-wrong-to-use-the-hand-cursor-for-clickable-items-such-as-buttons
[stackoverflow 4]: http://stackoverflow.com/a/12098334/1558430
[stackoverflow 5]: http://stackoverflow.com/a/7073558/1558430
[tutorialzine]: http://tutorialzine.com/2013/10/12-awesome-css3-features-you-can-finally-use/
[w3]: http://www.w3.org/TR/2013/WD-components-intro-20130606/#decorator-section
