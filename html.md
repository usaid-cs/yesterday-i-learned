1. A semantic tag called `<time>` allows you to enter it in ISO 8601 format and a human-readable one at the same time, [like this](https://zachholman.com/talk/utc-is-enough-for-everyone-right): `<time title="May 28, 2018, 3:47 PM PST" datetime="2018-05-28T15:47:57-08:00">six minutes ago</time>`
1. W3C [might](https://www.w3.org/TR/html51/syntax.html#sec-comments) have removed the requirement that comments must have a space between `<!--` and the actual comment, so `<!--comment-->` is valid now.
1. [Multiple `<tbody>` elements can exist in the same table.](https://stackoverflow.com/questions/3076708/can-we-have-multiple-tbody-in-same-table) Suspect the only reason for this is styling.
1. In HTML5, `<style>` tags must have the `scoped` attribute if they are in the `<body>` tag. Styles will be applied to its parent and siblings.
1. Google uses [a chain of iframes](www.googletagmanager.com/ns.html?id=GTM-NQTT) inside `<noscript` tags, to track users in case the browser has javascript disabled.
1. `<meta property="og:image" content="(the facebook share thumbnail)">`
1. There is a [`time`](http://www.w3schools.com/tags/tag_time.asp) tag in HTML5, and [it does something](http://jsfiddle.net/trevoro/T4wRq/) if you [tell it to](http://trevoro.net/2013/whats-your-timezone/).
1. `&blacktriangledown;` is a thing. [Those bastards](http://www.w3.org/TR/2013/WD-components-intro-20130606/#decorator-section)...
1. I hear [it's okay for html comments to be outside the <html> tag](http://stackoverflow.com/questions/365805/is-it-ok-to-put-html-comments-outside-the-html-tags), but [not if it comes before <!DOCTYPE>](http://stackoverflow.com/questions/941100/can-comments-appear-before-the-doctype-declaration). The only two browsers I suspect trouble are firefox and opera.
1. HTML5 [allows `a` to contain `div`](http://stackoverflow.com/a/1828032/1558430).
1. HTML5 element IDs can begin with a number. `$('#5')`, for example, works.
1. HTML5 element IDs can contain multiple dots: [`<div id="a.b.c"></div>`](http://stackoverflow.com/a/9930611/1558430).
1. Adding `width=device-width` or `user-scalable=no` on [some versions of mobile browsers](https://github.com/ftlabs/fastclick#when-it-isnt-needed) apparently introduces the side benefit of not introducing a hover-click delay.
1. [HTML5 tainted canvas](https://developer.mozilla.org/en-US/docs/HTML/CORS_Enabled_Image) is a `(new Image).crossOrigin = ...` change that allows a limited selection of browsers to serve images from any remote origin. This was implemented to allow canvases to reading images to be requested using cookies.
1. `crossOrigin` defaults to anonymous. There is no need to specify `anonymous`.
1. Serving an anonymous image inside a canvas removes a canvas' ability to be read.
1. Hashes can actually go to an ID as well as a name (`#foo` -> `<div id="foo"/>`).
1. In HTML5, `a` tags can have a [`download` attribute](http://www.w3schools.com/tags/att_a_download.asp) that forces the link to be downloaded.
1. Websites can restrict content sources by appending a header to the response. Here is the one github uses.
1. [The `address` element was not created for postal addresses (...) unless those addresses are in fact the relevant contact information for a document or section of a document](http://html5doctor.com/the-address-element/)
1. [Nested `span`s are okay.](http://stackoverflow.com/questions/1078127/are-nested-span-tags-ok-in-xhtml) The same probably speaks for other inline elements, too.
1. A `<button>` with undeclared `type` apparently defaults to a submit button.
1. [You can define your own tags](http://stackoverflow.com/questions/9845011/are-custom-elements-valid-html5/9845124#9845124). They just need at least one dash in the tag name, e.g. `<x-hello>`, `<md-tag>`, `com-foo`.
  The key function here is [`var XFoo = document.registerElement('x-foo');`](http://www.html5rocks.com/en/tutorials/webcomponents/customelements/)

```
Content-Security-Policy: default-src *; script-src assets-cdn.github.com www.google-analytics.com collector-cdn.github.com; object-src assets-cdn.github.com; style-src 'self' 'unsafe-inline' 'unsafe-eval' assets-cdn.github.com; img-src 'self' data: assets-cdn.github.com identicons.github.com www.google-analytics.com collector.githubapp.com *.githubusercontent.com *.gravatar.com *.wp.com; media-src 'none'; frame-src 'self' render.githubusercontent.com gist.github.com www.youtube.com player.vimeo.com checkout.paypal.com; font-src assets-cdn.github.com; connect-src 'self' ghconduit.com:25035 live.github.com uploads.github.com s3.amazonaws.com
```

1. In Chrome, `<img>` tags with no `src` have a [grey border](http://stackoverflow.com/questions/10848722/google-chrome-images-have-border) that does not go away with any amount of CSS.
1. HTML5 allows closing tags to be omitted where the semantics are obvious, for example, `li` in `ul`, or `option` in `optgroup`. Then again, your colleagues will kill you, so it is not a usable part of the spec.
1. However, [custom tags can never be self-closing in HTML5](http://stackoverflow.com/questions/23961178/do-custom-elements-require-a-close-tag).
1. `disabled` prevents focus on the element, whereas `readonly` lets you focus on it, but not edit it. `readonly` elements also get `submit`ted.
1. You can [change an `<input>`'s placeholder style](http://stackoverflow.com/a/2610741) using pseudoselectors `::-webkit-input-placeholder, :-moz-placeholder, ::-moz-placeholder, :-ms-input-placeholder`, if the field's `appearance: textfield`. With that said, these styles are platform-dependent (as you may expect with prefixed styles), and currently the placeholder cannot be inspected.
1. Well, you cannot specify [offline file wildcards](http://stackoverflow.com/questions/8001196/how-do-i-specify-a-wildcard-in-the-html5-cache-manifest-to-load-all-images-in-a).
1. Saving too much in localStorage gives you a `DOM Exception 22: QuotaExceededError`.
1. In `<head>`, when you expect a script to have access to nothing: [`document.head` is actually available.](https://eager.io/blog/everything-I-know-about-the-script-tag/)
1. "Use of the Application Cache is deprecated on insecure origins", which is great. [AppCache sucks blue balls](http://alistapart.com/article/application-cache-is-a-douchebag), anyway.
1. [An empty href](http://stackoverflow.com/questions/5637969/is-an-empty-href-valid) points to the same document.
1. ["Properties"](https://stackoverflow.com/a/6004028/1558430) are likely something where `prop in node` is true. "Attributes" are likely what you write directly in HTML. So if an `input` element has `value="foo"`, but user types in `bar`, then that element has attribute `foo`, but value `bar`.
1. Adding `sandbox` to [`<iframe sandbox>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) magically makes iframes safer. You can allow some things to escape, like `sandbox="allow-forms allow-scripts"`.
1. The point of [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) is to protect the client from leaking information to another origin.
1. The point of [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) is to protect the client from random stuff that might get injected into their webpages.
1. The point of [SRI](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) is to protect the client from getting fake resources from something like a compromised CDN.
1. The point of [CORB](https://fetch.spec.whatwg.org/#corb) is to ensure what the client requested is what the client wanted; requesting a `text/plain` to be displayed in an `<img>` tag would be blocked because it is impossible.
1. On `defer` vs `async`: `defer` [downloads scripts in parallel, and then waits for HTML parsing to finish, *and then* executes the script when HTML is done](https://developers.google.com/web/fundamentals/primers/modules). `async` downloads scripts in parallel, but executes the script as soon as it is downloaded, blocking HTML parsing.
1. Progressive Web Apps must be served over HTTPS.

## [Writing jank-free webpages](http://aerotwist.com/blog/pixels-are-expensive/)

60fps = limiting each frame to 16ms.

1. **USE PAGESPEED** to analyse your *render tree*.
1. Three stages of rendering: *Layout* (calculating geometry of where everything ought to be), *Paint* (filling in the page), and *Compositing* (picking a layer to minimise repaints).
1. Use the `will-change: wat` CSS directive to let the browser know what will be changed

### Eliminating expensive animations

Expensive animations include:

1. Scrolling
1. Transition based on variables
