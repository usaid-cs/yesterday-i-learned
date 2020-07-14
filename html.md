- You can send an entire email with just a link: `<a href="mailto:user@example.com?subject=Email%20title&amp;body=Wow%20you%20clicked%20it">Send</a>` and if that's in one of your gmail emails, you start composing immediately.
- If you already declared your HTML file to be UTF-8 (with `<meta charset="UTF-8">`), you can [and should](https://github.com/hail2u/html-best-practices#dont-use-character-references-as-much-as-possible) write UTF-8 characters as UTF-8 rather than entities.
- The `<iframe>` was introduced by Internet Explorer. ["It has been speculated that the tag name stands for ... [Scott] Isaacs Frame, although Scott has denied this."](https://schepp.dev/posts/today-the-trident-era-ends/) [Scott Isaacs](https://en.wikipedia.org/wiki/Scott_Isaacs) made Ajax. He works for Amazon now.
- There is [a very small number of void tags](https://html.spec.whatwg.org/multipage/syntax.html#elements-2), and the ones you will actually use are: `br`, `hr`, `img`, `input`, `meta`.
- The `<small>` HTML tag is reserved for defining "smallprint" or legal text.
- A semantic tag called `<time>` allows you to enter it in ISO 8601 format and a human-readable one at the same time, [like this](https://zachholman.com/talk/utc-is-enough-for-everyone-right): `<time title="May 28, 2018, 3:47 PM PST" datetime="2018-05-28T15:47:57-08:00">six minutes ago</time>`
- W3C [might](https://www.w3.org/TR/html51/syntax.html#sec-comments) have removed the requirement that comments must have a space between `<!--` and the actual comment, so `<!--comment-->` is valid now.
- [Multiple `<tbody>` elements can exist in the same table.](https://stackoverflow.com/questions/3076708/can-we-have-multiple-tbody-in-same-table) Suspect the only reason for this is styling.
- In HTML5, `<style>` tags must have the `scoped` attribute if they are in the `<body>` tag. Styles will be applied to its parent and siblings.
- Google uses [a chain of iframes](www.googletagmanager.com/ns.html?id=GTM-NQTT) inside `<noscript` tags, to track users in case the browser has javascript disabled.
- `<meta property="og:image" content="(the facebook share thumbnail)">`
- There is a [`time`](http://www.w3schools.com/tags/tag_time.asp) tag in HTML5, and [it does something](http://jsfiddle.net/trevoro/T4wRq/) if you [tell it to](http://trevoro.net/2013/whats-your-timezone/).
- `&blacktriangledown;` is a thing. [Those bastards](http://www.w3.org/TR/2013/WD-components-intro-20130606/#decorator-section)...
- I hear [it's okay for html comments to be outside the <html> tag](http://stackoverflow.com/questions/365805/is-it-ok-to-put-html-comments-outside-the-html-tags), but [not if it comes before <!DOCTYPE>](http://stackoverflow.com/questions/941100/can-comments-appear-before-the-doctype-declaration). The only two browsers I suspect trouble are firefox and opera.
- HTML5 [allows `a` to contain `div`](http://stackoverflow.com/a/1828032/1558430).
- HTML5 element IDs can begin with a number. `$('#5')`, for example, works.
- HTML5 element IDs can contain multiple dots: [`<div id="a.b.c"></div>`](http://stackoverflow.com/a/9930611/1558430). It can also contain hyphens, underscores, and colons. [HTML5 loosened it up](https://mathiasbynens.be/notes/html5-id-class), so now the only thing it *cannot* contain are spaces.
- Adding `width=device-width` or `user-scalable=no` on [some versions of mobile browsers](https://github.com/ftlabs/fastclick#when-it-isnt-needed) apparently introduces the side benefit of not introducing a hover-click delay.
- [HTML5 tainted canvas](https://developer.mozilla.org/en-US/docs/HTML/CORS_Enabled_Image) is a `(new Image).crossOrigin = ...` change that allows a limited selection of browsers to serve images from any remote origin. This was implemented to allow canvases to reading images to be requested using cookies.
- `crossOrigin` defaults to anonymous. There is no need to specify `anonymous`.
- Serving an anonymous image inside a canvas removes a canvas' ability to be read.
- Hashes can actually go to an ID as well as a name (`#foo` -> `<div id="foo"/>`).
- In HTML5, `a` tags can have a [`download` attribute](http://www.w3schools.com/tags/att_a_download.asp) that forces the link to be downloaded.
- Websites can restrict content sources by appending a header to the response. Here is the one github uses.
- [The `address` element was not created for postal addresses (...) unless those addresses are in fact the relevant contact information for a document or section of a document](http://html5doctor.com/the-address-element/)
- [Nested `span`s are okay.](http://stackoverflow.com/questions/1078127/are-nested-span-tags-ok-in-xhtml) The same probably speaks for other inline elements, too.
- A `<button>` with undeclared `type` apparently defaults to a submit button.
- [You can define your own tags](http://stackoverflow.com/questions/9845011/are-custom-elements-valid-html5/9845124#9845124). They just need at least one dash in the tag name, e.g. `<x-hello>`, `<md-tag>`, `com-foo`.
  The key function here is [`var XFoo = document.registerElement('x-foo');`](http://www.html5rocks.com/en/tutorials/webcomponents/customelements/)
- In Chrome, `<img>` tags with no `src` have a [grey border](http://stackoverflow.com/questions/10848722/google-chrome-images-have-border) that does not go away with any amount of CSS.
- [Void tags are `<foo>`](https://github.com/w3c/webcomponents/issues/624#issuecomment-385304654), and self-closing tags are `<foo />`.
- HTML5 allows closing tags to be omitted where the semantics are obvious, for example, `li` in `ul`, or `option` in `optgroup`. Then again, your colleagues will kill you, so it is not a usable part of the spec.
- However, [custom tags can never be self-closing in HTML5](http://stackoverflow.com/questions/23961178/do-custom-elements-require-a-close-tag).
- `disabled` prevents focus on the element, whereas `readonly` lets you focus on it, but not edit it. `readonly` elements also get `submit`ted.
- You can [change an `<input>`'s placeholder style](http://stackoverflow.com/a/2610741) using pseudoselectors `::-webkit-input-placeholder, :-moz-placeholder, ::-moz-placeholder, :-ms-input-placeholder`, if the field's `appearance: textfield`. With that said, these styles are platform-dependent (as you may expect with prefixed styles), and currently the placeholder cannot be inspected.
- Well, you cannot specify [offline file wildcards](http://stackoverflow.com/questions/8001196/how-do-i-specify-a-wildcard-in-the-html5-cache-manifest-to-load-all-images-in-a).
- Saving too much in localStorage gives you a `DOM Exception 22: QuotaExceededError`.
- In `<head>`, when you expect a script to have access to nothing: [`document.head` is actually available.](https://eager.io/blog/everything-I-know-about-the-script-tag/)
- "Use of the Application Cache is deprecated on insecure origins", which is great. [AppCache sucks blue balls](http://alistapart.com/article/application-cache-is-a-douchebag), anyway.
- [An empty href](http://stackoverflow.com/questions/5637969/is-an-empty-href-valid) points to the same document.
- ["Properties"](https://stackoverflow.com/a/6004028/1558430) are likely something where `prop in node` is true. "Attributes" are likely what you write directly in HTML. So if an `input` element has `value="foo"`, but user types in `bar`, then that element has attribute `foo`, but value `bar`.
- Adding `sandbox` to [`<iframe sandbox>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) magically makes iframes safer. You can allow some things to escape, like `sandbox="allow-forms allow-scripts"`.
- The point of [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is to protect the client from leaking information to another origin.
- The point of [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) is to protect the client from random stuff that might get injected into their webpages.
- The point of [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) is to protect the client from getting fake resources from something like a compromised CDN.
- The point of [CORB](https://fetch.spec.whatwg.org/#corb) is to ensure what the client requested is what the client wanted; requesting a `text/plain` to be displayed in an `<img>` tag would be blocked because it is impossible.
- On `defer` vs `async`: `defer` [downloads scripts in parallel, and then waits for HTML parsing to finish, _and then_ executes the script when HTML is done](https://developers.google.com/web/fundamentals/primers/modules). `async` downloads scripts in parallel, but executes the script as soon as it is downloaded, blocking HTML parsing.
- Progressive Web Apps must be served over HTTPS.
- `<input type="email">` allows empty strings because that's just how it is without `required="required"`.
- One advantage of [HAML](https://en.wikipedia.org/wiki/Haml) over HTML is the lack of closing tags. The disadvantage that came with that: long lines, because indentations are now used for nesting.
- An HTML element is everything between (and including) the start/end tags.

## [Writing jank-free webpages](http://aerotwist.com/blog/pixels-are-expensive/)

60fps = limiting each frame to 16ms.

- **USE PAGESPEED** to analyse your _render tree_.
- Three stages of rendering: _Layout_ (calculating geometry of where everything ought to be), _Paint_ (filling in the page), and _Compositing_ (picking a layer to minimise repaints).
- Use the `will-change: wat` CSS directive to let the browser know what will be changed

### Eliminating expensive animations

Expensive animations include:

- Scrolling
- Transition based on variables
