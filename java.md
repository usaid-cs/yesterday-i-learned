![](http://i.imgur.com/6Lf1OXl.jpg)

## [Introduction to Java](https://dev.java/learn/)

- Java is *younger* than Python, by 4 years.
- For a language that [puts so much emphasis on OOP (like Ruby)](https://en.wikipedia.org/wiki/Java_%28programming_language%29#Principles), Java sure is looking for criticism for keeping the [eight primitives](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html) in the language that aren't objects.
- [SDK man](https://sdkman.io/sdks) supports only Java-related SDKs. It's the nvm of Java.
- There isn't a `===` comparison operator. Which is good. But [`==` does the wrong thing with boxed primitives](https://stackoverflow.com/a/30454789/1558430), which is not good.
- [All primitive type names are reserved keywords](https://www.w3schools.com/java/java_ref_keywords.asp). Object type names, including `Object`, are not. In fact, there is not a single reserved keyword that starts with an upper case letter.
- `_` is a reserved keyword.
- There are no [generators](https://stackoverflow.com/questions/11570132/generator-functions-equivalent-in-java). Or proper coroutines. Kotlin made coroutines in the JVM by transforming code.
- It took Java until version 15 to get docstrings ("string blocks").
- [Variable names are case-sensitive](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html).
- [Everything is passed by value](http://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html); object references do not change outside the function.
- [`|=` is an assignment](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html), which means `foo = foo | that thing`.
- `;` is required after any non-block statement, including `return`.
- The "com" is [the company website's TLD](http://stackoverflow.com/questions/2125293/java-packages-com-and-org) by convention.
- [JLS = Java Language Specification](http://docs.oracle.com/javase/specs/)
- Prior to Java 7, it was impossible to [`switch/case` with a string condition](https://www.geeksforgeeks.org/string-in-switch-case-in-java/). Something about ["because it's slow"](https://stackoverflow.com/a/338230/1558430).
- JavaFX is a UI library.
- Despite Java's verbosity, [recommended line length is still under 80 characters](https://www.oracle.com/technetwork/java/javase/documentation/codeconventions-136091.html#313)... unless you read the Google style guide, which recommends 100.
- Google's style guide also recommends [2-space indents](https://google.github.io/styleguide/javaguide.html#s4.2-block-indentation). The main point is to make working with other teams easier, but if you work alone... be careful what you wish for.
- The Java mascot is [Duke](https://www.oracle.com/java/duke.html). What kind of animal is Duke? No one knows. Why's it called Duke? [No one knows](https://jaxenter.com/duke-the-java-mascot-explained-118397.html).
- Features new in Java 7: [anonymous interface implementation](http://tutorials.jenkov.com/java/lambda-expressions.html)
- Features new in Java 8: [Lambdas](http://tutorials.jenkov.com/java/lambda-expressions.html) (replacing stateless anonymous interface implementation), `Method::references` (where `references` is a static method...), interfaces that can have code in them, and `Optional` (see above).
- [Features new in Java 9](https://www.javatpoint.com/java-9-features): try-with resources, a [`@SafeVarargs` annotation](https://www.baeldung.com/java-safevarargs) that tells the compiler not to check for heap pollution, and anonymous classes.
- `if`, `else if`, `else`, `switch`, `do`, and `while` all work familiarly, except `switch`, which apparently didn't accept Strings until SE 7.
- `for ( ; ; )` is an infinite loop.
- `==` compares the two sides by address. `.equals()` compares the two objects by however the hell they decide to, in the implementation of `.equals()`, usually being an equivalence check.
- Where you have multiple `switch` `case`s, a variable can be initialized in another `case` block, and it will still work. Again, just because you can, it doesn't mean you should.
- [`Map` is an interface](http://stackoverflow.com/a/1348246); `HashMap` is the implementation.
- Concatenating an `Integer` to a `String` to have it automatically become a string is apparently [bad form](http://stackoverflow.com/a/18648773).
- `.clone()` can potentially return any subclass of the object you think you are holding. You can go `person.clone()` and it might give you an `Employee` or a `Thief`. (page 233)
- So many things are stuck on Java 8 because Java 9 is not backward-compatible.
- Where the memory is used to store primitives [depends on the JDK implementation](http://stackoverflow.com/questions/31608220/where-are-string-objects-when-created-using-tostring-methods-stored-in-memory-in) (and which types). In other words, it is best for you to ignore all this.
- ["To get a new feature into Java, it must get consensus from a consortium of large vendors such as Oracle, IBM, HP, Fujitsu & Red Hat."](https://softwareengineering.stackexchange.com/a/359420/116811) So next time a feature doesn't exist, blame the [Java Community Process Executive Committee](https://en.wikipedia.org/wiki/JCP_Executive_Committee).
- Glassdoor [says](https://www.marketwatch.com/story/the-best-job-in-america-pays-up-to-125-000-a-year-and-has-10-000-job-openings-11641384094) "Java developer" is the "best job in America". It turns out that way because companies that force you to write Java typically have good work-life balance.
- `println` prints the line, but `printf` lets you format the line with stuff inside (use `%n` to add a new line).
- [`Objects.hash(Object... values)`](https://docs.oracle.com/javase/8/docs/api/java/util/Objects.html#hash-java.lang.Object...-) takes any number of arguments, and generates a `hashCode` based on them. You can implement your own `hashCode()` method this way.
- I have been told that [JSP and Servlets are old stuff](https://www.quora.com/Do-Java-Web-Application-developers-still-need-to-know-JSP-and-Servlets-in-2019). And yet... [go learn both in 2022](https://www.upgrad.com/blog/top-java-web-application-technologies/)?
- `Scanner in = new Scanner` needs to be closed, apparently. Use try-with-resources to do it, which... is just [putting that line in a `try` with no `catch`](https://docs.oracle.com/javase/tutorial/essential/exceptions/tryResourceClose.html).
- Did you know that Java*Script* is often faster than Java because they both use a VM?
- "POJO" stands for [Plain Old Java Object](https://en.wikipedia.org/wiki/Plain_Old_Java_Object). What's *not* a POJO is a class that either extends a class, implements an interface, or is annotated. Beans are POJOs.

## Conventions

- Camel case conventions: `ClassName`, [`verbMethodName`](http://docs.oracle.com/javase/tutorial/java/javaOO/methods.html), `attributeName`
- [Google's style guide](https://google.github.io/styleguide/javaguide.html#s6.3-static-members) allows static methods to be called only through the class, not `anInstance.aStaticMethod()`. The same guide also says [`XmlHttpRequest` is correct and `XMLHTTPRequest` is not](https://google.github.io/styleguide/javaguide.html#s5.3-camel-case), for which [python's PEP8](https://www.python.org/dev/peps/pep-0008/#descriptive-naming-styles) argues for the exact opposite.
- Consider [google-java-format](https://github.com/google/google-java-format) for your formatting needs. Or [spotless](https://github.com/diffplug/spotless).
- [You can name your variables after a class, like `Integer Integer = new Integer(1)`](https://stackoverflow.com/questions/27877897/in-java-the-variable-name-can-be-same-with-the-classname). Well, just because you can, it doesn't mean you should.
- `//@formatter:off` and `//@formatter:on` control ranges between which Eclipse does not highlight your code. This had no effect on IDEA.
- The first line in the docstring is extracted as the summary of the method. Now that's normally no problem, but they chose `. ` as the delimiter, so you can't have stuff like `Mr. Bean` in the summary unless you [hack it out](https://stackoverflow.com/a/18282355/1558430).
- For docstrings, they want to start them with a third-person verb. Both Python and git want first-person verbs in imperative mood.
- As a strong adherent to the SOLID principles, [even if you want an object to print itself out, there should be another object for that](https://www.baeldung.com/solid-principles). Example in page: `Book`, and `BookPrinter`.

## Types

- A [raw type](https://stackoverflow.com/a/2770631/1558430) is using a generic type without specifying the type parameter. When they say ["you shouldn't use raw types"](https://rules.sonarsource.com/java/RSPEC-3740), they meant use `List<String>` instead of `List`, not that every type must be parameterised, because not all types can be parameterised.
- `float`s are half the size of `double`s.
- `float`s (e.g. `3.2f`) and `double`s (e.g. 3.2) [should never be compared directly](http://stackoverflow.com/a/16627869/1558430).
- ["Type inference"](https://softwareengineering.stackexchange.com/a/184183) in Java means `public <T> T foo(T t) { return t; }` returns whatever type you throw at it. It doesn't do more than that because Java devs really really like typing things out: ["...the redundant type serves as valuable documentation..."](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=4459053)
- Less draconian than Haskell: `new Integer`s can be added to `int`s and `float`s.
- Apparently, empty character literals (`''`) are not allowed. It makes no sense anyhow. Empty string is `""`.
- [Autoboxing](http://docs.oracle.com/javase/tutorial/java/data/autoboxing.html): something new since 1.5, automatically treating `1` and `new Integer(1)` as the same thing, instead of a primitive and a class, respectively. "Boxing" turns a primitive into an object. "Unboxing" turns an object back into a primitive.
- It is impossible to write `(5).toString()`, because fuck you, and fuck literals. To get a `"5"`, you need `new Integer(5).toString()`, or `Integer.toString(5)`. Update: [there are actually a thousand ways to convert an int to a string](http://javadevnotes.com/java-integer-to-string-examples), but `.toString()` isn't one.
- You can't `string.reverse()` to reverse a string, because it's Java. Instead, you need to use [`(new StringBuffer(string)).reverse().toString()`](https://www.geeksforgeeks.org/reverse-a-string-in-java/), because it's Java.
- Accessing a string's characters? `s[i]`? No no no. [`s.charAt(i)`](https://www.techiedelight.com/iterate-over-characters-string-java/).
- Accessing a string's characters, one by one? `for c in s`? No no no. There's `for (char c: s.toCharArray())`, where `toCharArray` copies your fucking string into a new array, or [looping through indexes like a pleb](https://stackoverflow.com/a/196975/1558430), i.e. `for ( ... s.length() ) { ... s.charAt(i) ... }`. Apparently doing this both nicely and quickly requires [*a third party library from Google*](https://guava.dev/releases/21.0/api/docs/com/google/common/collect/Lists.html#charactersOf-java.lang.CharSequence-): `for (Character c: Lists.charactersOf(s))`.
- You can assign any number (e.g. `int a = 1`) to any type that has a larger range than it (e.g. `long b = a`) without casting.
- ...However, you [cannot cast a `bool` to/from anything](https://stackoverflow.com/questions/3793650/convert-boolean-to-int-in-java), including an int.
- You can put underscores in between number literals, e.g. `123_456_789`.
- You can't return `{0, 1, 2, 3}` and expect to return an array. No no no too simple. You need to [`return new int[] {0, 1, 2, 3}`](https://stackoverflow.com/a/9331864/1558430). Because `new` applies to primitives too. Or something.
- You can't have "an array of Lists", i.e. `new List<E>[]`. Because it's not typesafe. That's just what the book says in item 28. I don't exactly get it.
- There used to be a time where [calling `method(long foo)` with `method(0)` will throw an error](https://tech.jonathangardner.net/wiki/Why_Java_Sucks#Won.27t_cast_an_int_to_a_long) because it wants `0L`. Thankfully, this is no longer the case.
- There is no difference between Long's notation, [`l` and `L`](http://stackoverflow.com/a/770017/1558430).
- Strong references are your normal `ObjectClass object = new ObjectClass()`. [Weak references](https://weblogs.java.net/blog/2006/05/04/understanding-weak-references) are references that can be garbage-collected at their own pace, so can sometimes become null. Use WeakReferences by wrapping them: `WeakReference<ObjectClass> = new WeakReference<ObjectClass>(object)`
- `PhantomReference`s are a special type of `WeakReference`, which is always null.
- [Making `List`s](http://stackoverflow.com/a/858590/1558430)
- [`Void` is not `void`](http://stackoverflow.com/a/10839064), because, again, fuck you. `void` is the type, and `Void` is a thing that holds the type.
- [`java.util.Date` is actually `Timestamp`, with an underlying implementation of a long.](https://news.ycombinator.com/item?id=14179783) Use something else instead, like jodatime.
- There is no `someArray[-1]`. Do it with `someArray[someArray.length - 1]`. Note how strings would ask you to use `.length()` (a method).
- The [array literal](https://stackoverflow.com/questions/1200621/how-do-i-declare-and-initialize-an-array-in-java) is done with curly brackets. Example: `int[] array = {1, 2, 3, 4, 5};`. C does the same thing. Blame C.
- `Array` is fixed size; you _must_ specify its size when creating it. `ArrayList` is variable size. `ArrayList` can also support generic types.
- If you add a number to a string (e.g. `"hello " + 5`), [you get the string](https://codegym.cc/groups/posts/int-to-string-java) `hello 5`. You do that in python, and you get a TypeError. So python is more strongly-typed than java in at least one way.
- Instead of doing `NewType(somethingElse)` to get something of type `NewType`, Java goes [`Arrays.asList(anArray)`](https://www.geeksforgeeks.org/find-max-min-value-array-primitives-using-java/). The mental model is different: if you want to do something, ask yourself if you can do it, rather than asking that something for help.
- Since strings are immutable, [`StringBuilder` is designed to let you append to a string without creating a new instance every time](https://www.toptal.com/java/top-10-most-common-java-development-mistakes). Syntax: `stringBuilder.append(newString).toString()`.
- [You *cannot* modify a List while it is being iterated](https://www.baeldung.com/java-concurrentmodificationexception) (`ConcurrentModificationException`). Alternatives include: using another "to remove" list; iterating through the `aList.iterator()`, which is [different](https://techdifferences.com/difference-between-iterator-and-listiterator-in-java.html) from the `aList.listIterator()` method; the `.removeIf` method; and using `aList.stream().filter(...)...`, which keeps the elements you want, instead of removing the ones you don't.
- Just like in JS (since JS learns from Java), [`String.split(s)` treats `s` as a regular expression](http://anh.cs.luc.edu/170/html/Java4Python.html), not a simple delimiter.
- There is nothing wrong with [`"Concatenating " + "multiple " + "strings"` in a single statement](https://stackify.com/java-performance-tuning/). They are optimised to a single `String` anyway. But for more than maybe three statements, a `StringBuilder` is preferred.
- People don't want you to use `BigDecimal` because of how slow it is. But sometimes you need to use it. In that case, [don't create one with a `double`](https://blogs.oracle.com/javamagazine/post/four-common-pitfalls-of-the-bigdecimal-class-and-how-to-avoid-them) because that's clearly got a double's precision. Garbage in, garbage out.
- By definition, Java's version of `MAX_INT` (`Integer.MAX_VALUE`), is [2^31 - 1](https://stackoverflow.com/a/7847939/1558430), regardless of platform. Also note that [Java's `int` is actually a `long int` in C](https://stackoverflow.com/a/15005018/1558430), and a Java `long` is more closely related to C's [`long long`](https://en.wikipedia.org/wiki/C_data_types) @ 64 bits.
- You can't just use `int` on prod because 2^32 is not that big of a number, and it will overflow to negative just about anywhere.
- [Class-based variables are implicitly `null`](https://stackoverflow.com/a/2707325/1558430). `Foo foo;` doesn't make it anything; `Foo foo` makes it null. [Primitives start off as 0, false, or the like](https://stackoverflow.com/a/25434449/1558430).
- Don't create a boxed primitive if you can initialise one with a primitive value. It's a good idea to have the compiler box it for you.
- Remember static types: splitting a String (`foo.split(",")` or something) results in multiple Strings. That requires the type to be `String[]`.
- [`HashMap` is more time-efficient. A `TreeMap` is more space-efficient (insertion time at O(log n)).](https://stackoverflow.com/questions/2444359/what-is-the-difference-between-a-hashmap-and-a-treemap/2444370#comment2430837_2444370)
- [Both `List.of` and `Arrays.asList` produce lists of fixed size](https://stackoverflow.com/a/68390147/1558430) (i.e. you can't add more to the list later). `List.of` will not take `null` for an answer, while `Arrays.asList` [might](https://stackoverflow.com/a/46580435/1558430) be better for large, mutable datasets. And then there's `java.util.ArrayList`, which [supports lots more things](https://stackoverflow.com/a/58132442/1558430) with a performance hit.
- The [`var` type](https://openjdk.java.net/jeps/286) was [added](https://ondro.inginea.eu/index.php/new-features-in-java-versions-since-java-8/) in Java 10. Michael recommends [only using `var` with `new` something](https://stackoverflow.com/questions/57376875/use-cases-when-lombok-or-java-var-is-useful#comment101238996_57377128) to not overdo inference.
- [A reifiable type is a type whose type information is fully available at runtime](https://docs.oracle.com/javase/tutorial/java/generics/nonReifiableVarargsType.html): primitives, non-generic types, raw types, and "invocations of unbound wildcards". Non-reifiable types are types where information has been removed at compile-time by type erasure.
- [`Array` is an implementation. `List` and `MutableList extends List` are interfaces](https://stackoverflow.com/a/36263748/1558430), with notable implementations being `ArrayList` and `LinkedList`. It is good practice to [prefer `List` et al. over `Array`](http://www.javapractices.com/topic/TopicAction.do?Id=39) unless performance is critical... like, _critical_. [Both `Array` and `ArrayList` have an amortised get and insertion time of O(1)](https://www.youtube.com/watch?v=ZVJ7kpEMc7U).
- There are [differences between `HashMap` and `HashTable`](https://beginnersbook.com/2014/06/difference-between-hashmap-and-hashtable/). Generally, a HashMap is better solution because it sounds like it is threadsafe.
- So `Arrays.sort()` sorts arrays, and `Collections.sort()` sorts collections (which `List`s are).
- `Character.toString(c)` is the same as `String.valueOf(c)` because the latter calls the former, but you might want to call the latter more often because that one cares less about your original type.
- Try to implement Iterable for anything that can be looped over, so you can use the foreach (`for ... : `) loop style.
- When two strings are concatenated, both are copied.
- `<` unboxes a boxed primitive; `==` does not. This can ~~fuck~~trip you right up when you write a comparator (example from the book): `Comparator<Integer> naturalOrder = (i, j) -> (i < j) ? -1 : (i == j ? 0 : 1);`. `i == j` will never be true even if they have identical values.
- If a null boxed primitive is unboxed, it will raise NPE even before any method is called on it.
- If your `Stack` `.isEmpty()` and you do so much as to `.peek()` at it, you will get a `java.util.EmptyStackException`, even though `.pop()` exists, and it is completely reasonable for `.pop()` to throw something. So you see guards like `s.isEmpty() || s.pop()` everywhere.
- There is [no way](https://stackoverflow.com/questions/2914695/how-can-you-write-a-function-that-accepts-multiple-types) to write a function that accepts multiple types, like `void foo(<A, B, C> bar)`. You also don't need to. You can overload the function that accepts one type each.
- [`int[][] a` is a 2-dimensional array. `int[] a[]` is a 2-dimensional array. `int a[][]` is a 2-dimensional array.](https://blog.jooq.org/10-things-you-didnt-know-about-java/). You can even stick annotations anywhere in between.
- You cannot compare booleans with integers (or null). You can't even `if (1)`. There is no java truth table because [nothing is convertible from/to boolean](https://stackoverflow.com/questions/24363080/can-i-convert-boolean-into-another-data-type-in-java) (and that's at least one thing Java got right relative to JS).
- You can't remove anything from an array.
- To make a shallow clone of a list, do `new ArrayList<>(aList)`. This is equivalent to `list(a_list)` in python. You can also try [`aList.clone()`](https://www.geeksforgeeks.org/arraylist-clone-method-in-java-with-examples/) if you have an ArrayList. There are [warnings about threads and thread safety](https://stackoverflow.com/questions/14319732/how-to-copy-a-java-util-list-into-another-java-util-list), so try not to fuck with concurrency.
- `anotherList = aList.subList(0, aList.size())` produces a [view](https://stackoverflow.com/questions/3962766/how-to-get-a-reversed-list-view-on-a-list-in-java#comment76811001_3963075) of the original list, not a copy of the list. Consequently, if you do anything to `anotherList`, it will affect the contents of `alist`. If you `Collections.reverse()` a subset of the list, for example, then the original list will have that subset reversed, as well.
- `aList.equals(anotherList)` really checks if the two lists are the same! Wow!

### `null`

- Need to check for `null` everywhere, because Java is a very safe language, obviously.
- The default "nothing" constant is `null`. Now you can return `null` from any method that claims to return an object---which is *terrible*---but at least you can't return `null` in a method that claims to return a primitive, i.e. `int foo() { return null }` won't ever compile.
- It is always possible to `return null` in any function, even if the return type is specified not to be null.
- `String foo = null` is [perfectly fine](https://www.youtube.com/watch?v=-r5cebGAIZc) in this language. You can even compile something like this and get no warnings, and then get `NullPointerException` when you run it. Perfection.

#### [`Optional`](https://dzone.com/articles/using-optional-correctly-is-not-optional)

> [`Optional` is intended to provide a *limited* mechanism for library method return types, where there needed to be a clear way to represent "no result", and using null for such was overwhelmingly likely to cause errors.](https://dzone.com/articles/using-optional-correctly-is-not-optional) - [Stuart Marks](https://blog.jooq.org/the-java-ecosystems-obsession-with-nonnull-annotations/), quoting someone else

- Null checks can be replaced with [`Optional<Type> optionalVal = Optional.ofNullable(somethingThatCanBeNull); if(optionalVal.isPresent()) { optionalVal.get(); }`](https://www.toptal.com/java/top-10-most-common-java-development-mistakes). When used as such, it is not any better than the `== null` check for [not allowing `null` semantically](https://stackoverflow.com/a/28746693/1558430); ["the real power comes from being able to defer the error handling (no value) to a later time and chaining map/flatMap/filter etc. methods without if/else blocks."](https://stackoverflow.com/questions/28746482/optional-vs-null-what-is-the-purpose-of-optional-in-java-8#comment70270554_28746693)
- Java has an [`Optional` container type](http://rcardin.github.io/functional/programming/types/2019/10/06/optional-is-the-new-mandatory.html) that lets you do your null checks with a different set of methods instead of `!= null`. Although [an `Optional` type can never return null](https://stackoverflow.com/questions/28746482/optional-vs-null-what-is-the-purpose-of-optional-in-java-8), you will still need to check if the thing you returned "is empty", i.e. whether the underlying value is null. [Could be mistaken though](https://dzone.com/articles/using-optional-correctly-is-not-optional).
- Don't return an `Optional` if you can return an "empty" container instead. For example, if you are normally returning a list of something, an empty list is a perfectly valid return value.
- Prefer null checks to `Optional` if all you do is create an Optional for the sole purpose of chaining methods on it: [item 12](https://dzone.com/articles/using-optional-correctly-is-not-optional). If your optional is created and destroyed in the same scope, think twice.
- Prefer alternatives to `Optional.isPresent()` and `Optional.get()` if there are any. `anOptional.orElse(defaultValue)` is a good one (equivalent to `thingy || defaultValue` in JS).
- `orElse(null)` is some stupid thing that lets you adapt your code to old code that allows nullable references.
- `Optional.ifPresent(someLambda)` simply does nothing if the Optional is empty.
- `Optional.steam()` retains anything that is present. `.flatMap(Optional::stream)` is equivalent to `.filter(Optional::isPresent).map(Optional::get)`.
- You can [`Optional.map(aFunction).oeElse(defaultValue)`](https://dzone.com/articles/using-optional-correctly-is-not-optional) to apply a function to an `Optional` if it's present, or return a default value if it's not. The map happens after the Optional checks itself for presence.
- The `.get()` in `Optional.get()` is one of the few places in Java where a `.get()` throws an exception. Brian Goetz expresses deep remorse for having designed it that way.
- Don't use Optionals in function parameters. Callers should never need to pass you an Optional (e.g. `myMethod(Optional.of("some value"))`).
- [Use `Optional.of()` when you know the thing can't be `null`](https://stackoverflow.com/a/31696584/1558430), and `Optional.ofNullable()` when it can be `null`. Because of the nature of `Optional` (it helps you handle `null`), using a `Optional.of()` that raises `NullPointerException` is really just in terms of contract (i.e. you need to return an `Optional`, but quite often you know for sure that you should be returning something).
- [`Objects.nonNull`](https://www.developer.com/java/java-7-feature-asserting-non-null-objects/) is an assertion-like call that throws `NullPointerException` wherever you want to make sure something is definitely not null at some point, i.e. `variable!!`, except less elegant.
- This whole "null " thing happens to allow you to write linked list iteration without worrying if `node.next` is a node (because it may be null).

## Generics

- [Generics](https://en.wikipedia.org/wiki/Generics_in_Java): `<T>` means "of type T".
- [Bounded generics](https://stackoverflow.com/questions/30292959/understanding-bounded-generics-in-java-what-is-the-point), e.g. `<T extends Number>` is generally useful only if you have two or more bounds, i.e. `<T extends Number & Comparable<T>>`, because `<T extends number>`, "T must be a subclass of Number", could have just been declared as `Number`.
- Generic parameters (the `T` in `<T>`) cannot be a primitive because primitives, for whatever reason, aren't considered types. [They are working on it](https://openjdk.java.net/jeps/218), but honestly? Still? Anyway.
- Adding a method inside an interface will instantly (with a lack of a better term) fuck everyone over because none of the implementations have that new method. To combat this, Java 8 adds [`default type funcName() {...}`](https://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html) to interface definitions. Of course you'll start to wonder the purpose of interfaces if you can have code in it, but I digress.
- Anyway, not using generics in your code may prevent you from using type inference with lambdas (because it won't know how to infer types).
- In methods with more than one generic type, you use [`U`, `V`, etc](https://stackoverflow.com/a/2900933/1558430). There are other letters reserved for things like Elements (E) and Numbers (N).
- ["Generics are implemented by erasure"](https://stackoverflow.com/a/339720/1558430), allowing them to interoperate with code that didn't use generics (such as code from Java 4).
- You need to [declare your generics in your method *declarations*](https://stackoverflow.com/questions/52259571/why-type-parameter-required-before-return-type-for-static-generic-methods), e.g. `public static <T> int foo(T t)`. Otherwise, for some reason, the compiler isn't smart enough to know what `T` is, even though you just declared it in the class `public class Foo<T, U, V>`.
- You cannot write two methods with generic parameters (e.g. `List<Integer>`, and `List<Long>`) that [boil down to the same thing](https://tech.jonathangardner.net/wiki/Why_Java_Sucks#name_clash:_X_and_Y_have_the_same_erasure), because they are essentially the same method after type erasure, and your code won't know which to call.
- When instantiating a typed Map (`Map<String String> foo = new HashMap<String, String>();`), the second `String, String` can be omitted because it is obvious (diamond operator). Then again, most things are obvious in Java, but they cannot be omitted.
- The [diamond operator](https://stackoverflow.com/questions/4166966/what-is-the-point-of-the-diamond-operator-in-java) (`<>`) allows you to omit the type of a concrete instance when you have already declared the type of the variable. The compiler then infers one type from the other. Somewhat related: if you don't have the `<>`, then you get an "unchecked conversion warning" (right hand side is a raw type).
- Parameterise your type declarations whenever possible. `List ofNumbers` (bad) allows you to `add` anything into the list, while `List<Integer> ofNumbers` (good) will break compilation when you add any non-integer to it.
- In between `public` and `void`, you can specify [bounded parameters](https://docs.oracle.com/javase/tutorial/java/generics/bounded.html) that specifies ... superclasses of that type that can be passed in, I guess. Today I have not learned.
- `@SuppressWarnings("unchecked")` in the code means that you confirm [the generic method/function is doing legal things](http://stackoverflow.com/a/1129812/1558430).
- You can't make an `Optional<T>` of a primitive, because a primitive is not a `T`. There are however classes like [`OptionalInt`](https://www.dariawan.com/tutorials/java/optionaldouble-optionalint-and-optionallong/), which allow you to use streams with primitives, for example.
- Ever noticed how `Optional<T>` is `Optional < T >`? Pretty sure multiple comparisons aren't coming to Java.

## Classes, Interfaces, and things to that effect

- If your class is not designed to be subclassed, mark it as `final`.
- The "readable yet obscure" way to initialise an object is through [double brace initialisation](https://www.baeldung.com/java-double-brace-initialization), where you can add an anonymous class to the end of an instantiation (i.e. `new Foo() { ... }`), but you can also [add a constructor](https://wiki.c2.com/?DoubleBraceInitialization) to that anonymous class using another pair of braces (i.e. `new Foo() {{ ... }}`), hence the name.
- A class constructor is named after the class, and a subclass instantiation calls constructor methods from the ancestor to the terminal class, *on the terminal class*. Therefore, if `class Sub extends Super`, and both of these classes have a constructor, then `Super()` is first called, and `Sub()` is then called. To beware in this case: if both `Super()` and `Sub()` call `overrideMe()` and `Sub` overrides `overrideMe`, then `Sub.overrideMe` will be called twice and `Super.overrideMe` will be called zero times.
- People [prefer interfaces over abstract classes](https://stackoverflow.com/questions/639592/why-are-interfaces-preferred-to-abstract-classes) because abstract classes must be the bottom of the inheritance chain. Once you inherit it, you can't inherit something else.
- [Both abstract classes and interfaces can contain methods](https://www.baeldung.com/java-interface-default-method-vs-abstract-class). In an interface, you have to add `default`, though. Default methods are for when you want to add a method to an interface, but are not interested in breaking every single class that *has now not implemented the new method*.
- Adding default methods to existing interfaces don't guarantee the methods will do the right thing when called from a subclass. You can add default methods to a *new* interface all you want, but it should be done to an existing interface only after determining that fixing existing implementations is not possible.
- [**Do not define constants with an interface**.](https://softwareengineering.stackexchange.com/questions/49572/is-it-a-bad-practice-to-have-an-interface-to-define-constants) Use a normal class instead.
- When accessing class variables, `this` appears to be optional, i.e. `this.foo` works just as well as `foo`.
- Avoid typing `this.foo` when inside a context that already gives you `foo`. ["As a general rule you should avoid redundant syntax wherever it may arise"](https://stackoverflow.com/a/14932717/1558430) - coming from a Java developer
- A class can have no public constructors to avoid being created. This is useful for utility classes, as well as forcing instantiation through static factory methods (like `List.of`, incidentally).
- [Class within a class](https://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) is allowed... apparently it encourages encapsulation, logical code grouping, and maintainable code.
- ... but inner classes cannot have static members, if they are not themselves static.
- [*Constructors can't call each other.*](https://tech.jonathangardner.net/wiki/Why_Java_Sucks#Constructors_can.27t_call_each_other) Or [can they](https://stackoverflow.com/a/285184/1558430)? Anyway, you will really want to limit the number of constructors you have, to limit the amount of duplicate / boilerplate code you write.
- Non-static classes cannot be instantiated inside a static function.
- Subclasses are possible, of course, but [`this` and `super` must be called as the constructor's first statement](http://stackoverflow.com/questions/1168345/why-does-this-and-super-have-to-be-the-first-statement-in-a-constructor)
- Subclassing syntax: `public SubClass extends SuperClass`
- [Static inner classes are exactly like external classes except that they have access to all members of the outer class, regardless of access qualifier](http://stackoverflow.com/a/4848071/1558430).
- `static {}` in a class [acts as the class constructor](http://stackoverflow.com/questions/2943556/static-block-in-java). This is called once when the class is loaded in memory, i.e. making two instances will not run static blocks twice. [A static block can only reference static variables](https://beginnersbook.com/2013/04/java-static-class-block-methods-variables/); it is a good place to initialise them.
- ... in contrast, a `{}` block without the `static` keyword is an instance initializer.
- ... in further contrast, variable declarations in the class, but outside any method, are called [declaration statements](https://stackoverflow.com/a/12062963/1558430).
- [Interfaces](http://docs.oracle.com/javase/tutorial/java/javaOO/classdecl.html): `implements YourInterface1, YourInterface2, ...`
- [Access modifiers](http://docs.oracle.com/javase/tutorial/java/javaOO/variables.html): `public`, `private`, [and more](http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
- "You don't have to provide any constructors for your class, but you must be careful when doing this. **The compiler automatically provides a no-argument, default constructor for any class without constructors.**"
- The `this` keyword always means the current object, even if the current method is not visibly bound to anything. This is like Python's `self`, except `self` is not specified.
- [`this`](http://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html) is used to remove ambiguity when the scope has a variable that has the same name as its outer class attribute.
- [Outer classes can only be declared public or package private.](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html) That is to say, it is either seen, or not seen, by other packages. Package-private is the default access modifier; there is no need to do anything.
- [Static vs non-static inner classes](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html): non-static inner classes have access to other outer class members.
- Instantiating an inner class: `OuterClass.InnerClass innerObject = outerObject.new InnerClass();`, noting that the `new` keyword goes _after_ the outer class name.
- The [`@Override`](http://stackoverflow.com/a/94447/1558430) denotes "I override a parent method"; whether or not it does anything is up to the compiler.
- `@Override` "came from" `java.lang` automatically for every file, just like the implied `from exceptions import *` in Python.
- Interfaces can be private. There are virtual no uses for this case.
- Classes that extends `Serializable` all require a unique `private static final long serialVersionUID;` value that allows a deserialized object to know which class along the class tree to deserialize back into.
- All interfaces are static. `static` is redundant.
- All interface methods are public. `public` is redundant.
- Because inner classes are visible only within the outer class, [an interface method inside a class like that must be public](http://stackoverflow.com/questions/11639741/java-attempting-to-assign-weaker-access-privilege-error) (or at least better than the base class, I am guessing).
- Notice a constructor syntax is `public Foo()`. It never asks for the return type. If you type `public Foo Foo()`, that's a method called `Foo` on your instances of `Foo`. Because fuck you.
- **Overloading is so prone to abuse**, Item 52 recommends not to overload a method in a way where any two versions share the same number of parameters. The solution? "Give them different names, lol"
- [`static final type UPPERCASE_UNDERSCORED`](http://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) defines constants. It can still be `private`, accessible to only instances of this class.
- `final` methods cannot be overridden.
- [Shadowing is discouraged](http://stackoverflow.com/questions/1092099/what-is-variable-shadowing-used-for-in-a-java-class)
- In Java, when you make a new instance of an interface (say `MyList(List)`), you can say ["I depend on any class that does this stuff"](https://stackoverflow.com/questions/1992384/program-to-an-interface-what-does-it-mean) and write stuff like `List foo = new MyList()`. This is more apparent when you write a function that takes in "collections of anything, as long as it is a collection."
- Class docstrings apply to all methods in the class. So you can put `@throws NullPointerException ...` in the class method if lots of (most) methods in the class throw `NullPointerException`.
- Without `this.`, `foo` can either refer to the instance variable `foo`, or the static variable `foo`.
- Rather than assigning `self = this` or something like that, the outer class can be referenced with [`OuterClass.this`](http://stackoverflow.com/questions/2808501/calling-outer-class-function-from-inner-class) instead.
- It is apparently okay to have a type starting with an `@`, such as [`@Interface`](http://stackoverflow.com/questions/918393). `public @interface Foo { ... }` allows you to use the annotation `@Foo` in other files.
- There's an ["effectively final"](https://stackoverflow.com/questions/20938095/difference-between-final-and-effectively-final) state: A variable or parameter whose value is never changed after it is initialized is effectively final, i.e. [a variable that is assigned to only once](https://www.baeldung.com/java-8-lambda-expressions-tips#variables). References to objects are also effectively final, even if the objects themselves change. Effectively final variables do not give compiler errors if they were really declared with `final`.
- [Defender methods](https://www.tutorialspoint.com/what-are-defender-methods-or-virtual-methods-in-java) and default methods (in an interface) are the same thing.
- ["Good news: private methods in interfaces look like they will make Java 9."](https://stackoverflow.com/questions/27368432/why-does-java-8-not-allow-non-public-default-methods#comment45484226_27369217) - Brian Goetz, one of the guys who's in charge of it in the first place. Anyway, with this small addition, it finally makes sense to build classes with mixins, rather than inheritance (see point about multiple inheritance).
- Refer to objects (`I<> foo = new C<>()`) by their interfaces ("what they do"), not the class ("what they are"). It's ok if you can't find a good interface to do it with; base class is fine too. In general, limit the method scope if possible.

## Functions and methods

- [`varargs`](http://docs.oracle.com/javase/1.5.0/docs/guide/language/varargs.html) are denoted with [`...`](http://stackoverflow.com/questions/5224252/what-are-these-three-dots-in-parameter-types), and can be used _only_ in the final argument position.
- Example `varargs`: `public int foo(int ... params) { }`
- In a particular case where `varargs` is declared with type `Object`: `public int foo(Object ... params) { }`, `foo` accepts anything.
- A lambda cannot be serialized, and (for a different reason) really shouldn't exceed three lines.
- [Don't write your own lambda if there's already a built-in method for it](https://twitter.com/stuartmarks/status/1151589003721756672), e.g. `Integer::parseInt` (static), `Instant.now()::isAfter` (bound), `String::toLowerCase` (unbound), `TreeMap<K, V>::new` (class constructor), `int[]::new` (array constructor). Note that all of these methods use the same syntax `::` for referencing.
- If the element type of the `varargs` array is not reifiable, you get [a warning](https://stackoverflow.com/questions/28914088/java-warning-varargs-method-could-cause-heap-pollution-from-non-reifiable-varar). If you know for sure that you are doing it right (the `varargs` array is not modified in any way, and if the the reference to the array is not leaked), then use `@SafeVarargs` to shut it up.
- Convenience is often not worth it. When in doubt, leave (convenience methods) out.
- Methods should accept no more than four parameters each.
- [No optional parameters](http://stackoverflow.com/a/7428077/1558430).
- [Type inference is bad](https://news.ycombinator.com/item?id=20296123), but fucking [lambdas with inferred types](https://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html) are not? Fuck off.
- [Anonymous classes implement interfaces](https://docs.oracle.com/javase/tutorial/java/javaOO/anonymousclasses.html#declaring-anonymous-classes).
- Writing a method that accepts an object (e.g. `int foo(Integer bar)`) *implies that you accept null* in its place. Null can come and go, so [mark things with `@NonNull`](https://www.baeldung.com/java-avoid-null-check) whenever you don't check (so the IDE tells you where it could be null), and `@Nullable` when you aren't sure if it could be null / are sure that you handle null.
- Counterpoint: [`@NonNull` is just noise and should be avoided in your own codebase](https://blog.jooq.org/the-java-ecosystems-obsession-with-nonnull-annotations/): "let go of your null fear. null is not a problem in well-designed software."
- There are no optional parameters. There are no keyword parameters. There is barely varargs, and even that got fucked up by implementation detail.
- Functions are not first-class: "The Java programming language doesn't let you pass methods into methods. But you can pass an object into a method and then invoke the object's methods."
- A function that accepts `foo(int[] bar)` really accepts an array of ints, which is created using `new int[n]`.
- [Covariant return type](http://en.wikipedia.org/wiki/Covariant_return_type): _a subclassed method can return a subtype of the superclass method's return type_.
- [Contravariant argument](<https://en.wikipedia.org/wiki/Covariance_and_contravariance_(computer_science)#Contravariant_method_argument_type>): an (unsupported) overloading of a function that accepts a more general argument than its overridden counterpart.
- A class method that returns an instance of itself is used for chaining. Not memory-efficient; just chaining.
- A method `public void foo(String...bar)` means that [it accepts an arbitrary number of arguments of type `String`](http://stackoverflow.com/a/3158767/1558430). If used in conjunction with other parameters, this must be placed last.
- A method name is too long if it's 65536 characters or longer.
- A lambda does not compile if it tries to access a non-final variable... but it will still work if it is "effectively final" (i.e. not modified, see above). Something about thread safety.

## Exceptions

- It is common knowledge for java developers that "NPE" stands for `NullPointerException`.
- `try { } catch (Exception e) {}` does not catch undefined variable and attribute accesses, aka [`cannot find symbol`](http://www.roseindia.net/java/java-get-example/cannot-find-symbol.shtml).
- The syntax for catching multiple exceptions is `SomeExceptionClass|AnotherExceptionClass`.
- A method can choose not to catch an exception only if it says it `throws` the same exceptions in its own signature.
- Finalizers have been deprecated since Java 9 because it tends to break code. It is replaced by Cleaners, which are also unnecessary in most cases. They don't have execution guarantees, so avoid both of them when doing anything time-critical. (Look into implementing `AutoClosable` instead)
- "Try with resources" has the syntax `try (BufferedReader br = new BufferedReader(new FileReader(path))) { ... }`. Compared to "try-finally", it shows the correct exception message when closing a file fails in the finally block.
- Every time you put [`@SuppressWarnings("unchecked")`](https://stackoverflow.com/questions/1129795/what-is-suppresswarnings-unchecked-in-java), make sure you do it at the smallest scope, and make sure you explain why.
- [Checked exceptions](https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/) are called that because they are checked at compile time. You need to declare those in methods that throw them. Or you can handle them.
- Checked exceptions (anything with the syntax `type methodName throws SomeExceptionClass`) must be caught immediately above its execution stack.
- Don't ever throw *or* catch `AssertionError`. You can use `assert`, obviously.
- Runtime exceptions (i.e. unchecked ones) shouldn't be caught.
- Methods with checked exceptions can't be used directly in streams, so avoid unnecessary use of checked exceptions. Maybe Optional and unchecked exceptions can help in either case.

## Enums

- **Enums**: `public enum EnumName { OPTION1, OPTION2, OPTION3, ... }` allows you to use the enum like `EnumName.OPTION1`. Enums do not have instances.
- All Enum values can be accessed via `EnumName.values()`.
- [Enums can contain code, variables, and even the void main.](http://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
- [Enums should be used where speed is not an issue](http://trevore.com/post/should-I-use-enums-in-Android)
- Each enum value can take constructor parameters. See the [`Planet` example](https://docs.oracle.com/javase/tutorial/java/javaOO/enum.html) `MERCURY (3.303e+23, 2.4397e6),`. *These arguments can also be lambdas*, so you can tell each enum how it works (strategy pattern), if need be.
- Don't ever use `enum.ordinal()`. An enum's value is never supposed to change when you add/remove/reorder them.
- Enums cannot be extended. It makes no sense to extend enums. But if you need to do that for some reason, emulate it with an interface.
- **Two-element enums are almost always better than booleans**, unless the meaning of the boolean is clear from the method name.

## Annotations and reflection

- Annotations can be put in function arguments, like `public void foo(@NonNull int[] bar)`. In this case, `NonNull` is from `android.support.annotation`, but [there are *a lot* of `NonNull` and `NotNull` classes out there](https://stackoverflow.com/questions/4963300/which-notnull-java-annotation-should-i-use), and [the checker framework checks them all](https://checkerframework.org/manual/#nullness-related-work).
- "Reflection" from Java's point of view is just [the ability to inspect and dynamically call classes, methods, attributes, etc. at runtime.](https://stackoverflow.com/a/37638/1558430) Simple things like calling a method by name counts as reflection.
- `Class.forName`, like PHP's `get_class`, returns the class object called that string. The string needs to be the class' full qualifier.
- Reflections are cool, but you lose type checking. They are also [slow](https://stackoverflow.com/questions/42425906/is-java-reflection-bad-practice).
- The [`@FunctionalInterface` annotation](https://www.baeldung.com/java-8-lambda-expressions-tips) tells the compiler to fail if you try to add more than one method to a [functional interface](https://www.baeldung.com/java-8-functional-interfaces#Functional). A functional interface is an interface that contains a single abstract method.

## Streams, threads, and parallel programming

- How to do `map(func, list)`? [`List<...> ... = list.stream().map(func).collect(Collectors.toList());`](https://stackoverflow.com/a/20999230/1558430) (🥲)
- [Immutable objects are inherently thread-safe](https://stackoverflow.com/questions/9303532/immutable-objects-are-thread-safe-but-why) because there is nothing about read-only objects that needs synchronising.
- Just because you can use [streams](https://www.geeksforgeeks.org/stream-in-java/) ("half-assed pipes") to do everything, doesn't mean you should; do the more readable thing.
- Stream processors should really just use pure functions. There is no benefit to using streams if you put iterative code inside it.
- Try to avoid returning a stream unless you know it will be used as a stream. If not then return a collection.
- [Reading a file with input streams](https://www.overops.com/blog/improve-your-application-performance-with-garbage-collection-optimization/) (and never holding the entire file in memory) is better than storing a file in a byte array, for both memory reasons, and the garbage collection that follows: [`FileInputStream fis = new FileInputStream(fileName); MyProtoBufMessage msg = MyProtoBufMessage.parseFrom(fis);`](https://gist.github.com/TaliSoroker/37df26e570a6d45093c2cc3633e4dd94#file-gctip2)
- Streams are easy to parallelise using `.parallel()`, but it may do the wrong thing (if your stream processors aren't pure functions, for example). The rough rule of thumb given by Josh suggests using `.parallel()` on something if you know (number of elements * lines of code per element) exceeds 100k.

## How Java gets around having no features™

- What's multiple inheritance, anyway? Java doesn't know. "Composition" is relaying a child object's methods in a "has-a" relationship. For example, if a `Person` "has-a" `Job`, then [you implement `Person.getSalary` as a forwarding method that just calls and returns `this.job.getSalary`](https://www.journaldev.com/1325/composition-in-java-example). Java developers prefer composition over inheritance, even though the language construct heavily prefers inheritance over composition. There [isn't an easy way](https://stackoverflow.com/a/17987980/1558430) to write a mixin (an interface but not really), for example.
- [Telescoping constructors](https://www.vojtechruzicka.com/avoid-telescoping-constructor-pattern/) don't scale. Use the builder pattern instead.
- Setters that `return this;` are of the [builder pattern](http://en.wikipedia.org/wiki/Builder_pattern). According to a colleague of yours, doing so instead of `return void;` has no real performance differences. [Android's `AlertDialog.Builder`](https://developer.android.com/guide/topics/ui/dialogs) is one of those.
- Speaking of the builder pattern: it is Java's way of offering keyword arguments, without having keyword arguments. You can also go with [double brace initialisation](https://stackoverflow.com/a/1988268/1558430) (explained below) at a performance cost.
- The javabeans `setThis`, `setThat` pattern doesn't allow an object to be checked for consistency before it is created. It also removes the possibility of having the object be immutable after creation (because you don't know when creation ends).
- If you want a singleton, maybe you can use the single element enum pattern (again, as a crutch for having no good options). Singletons are hard to test.
- On operator overloading (i.e. using `<`, `>`, `<=`, etc. for your own classes) is [not a thing](https://stackoverflow.com/questions/29179194/compare-two-objects-with-or-operators-in-java). You really need to define your own `isGreaterThan`, `isLessThan` methods for that. Or you can implement some [`Comparable` interface, or `Comparator` interface](https://stackoverflow.com/questions/420223/what-is-the-difference-between-compare-and-compareto). So, basically madness.
- The de-facto method of freeing something from memory is `something = null`. That is not to say you should. Null an object reference when you no longer need it *only where sensible*. It's just code noise so you want to avoid doing this unless you need to. You can avoid it by declaring variables in the smallest scope, so they get garbage collected naturally.
- Consider using static factory methods instead of a constructor: can have a name, can have more than one of those per class, not required to give you a new instance every time, can return a subtype as well as its own type, and can add your own logic. Also there doesn't need to be one for a class.
- Make defensive copies of arguments so no one can modify them again, through the references they leave outside. (Item 50)
- When you make defensive copies of something, you first copy the object, then you validate the copied object, not other other way around. Viega01 says doing otherwise results in a [time-of-check/time-of-use attack](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use)... by letting malicious code run in between your validation and copy code... somehow.
- An "abstract builder" is a build that is yet to be concrete (heh). So since a builder builds something (let's call it `T`), how do you write reusable code in the builder that references `T`? Apparently you do the [simulated self type](https://www.sitepoint.com/self-types-with-javas-generics/) trick, because java doesn't even have a self type?
- On defensive copies... if you have a method that returns a reference to your internal variable, you need to *return* a defensive copy too.
- When writing methods, prefer interface parameters over class parameters (i.e. `foo(Map bar)` is better than `foo(HashMap bar)`). This locks your method onto a behaviour (basically duck typing), rather than a implementation.
- `@Override` alerts you whenever you aren't overriding anything. It catches a potential error, where a developer writes a similar method that isn't overridden, but overloaded instead.
- [Item 41](https://dev.to/kylec32/effective-java-use-marker-interfaces-to-define-types-45ob) says that marker interfaces are superior to annotations. [Lots of people disagree](https://beetechnical.com/tech-tutorial/marker-interfaces-vs-annotations-in-java-quick-comparison/).
- Instead of `"string ${interpolation}"`, you get [`String.format("string %s", "substitution")`](https://stackoverflow.com/a/6389845/1558430). Kotlin has it.
- Instead of `foo?.bar`, you get `foo == null ? null : foo.bar` (it's better that way™)
- "(A) common problem that junior to intermediate developers tend to face at some point: they either don't know or don't trust the contracts they are participating in and defensively overcheck for nulls. Additionally, when writing their own code, they tend to rely on returning nulls to indicate something thus requiring the caller to check for nulls." - An answer on [how to deal with nulls everywhere](https://stackoverflow.com/a/271874/1558430), with solutions including the [null object pattern](https://en.wikipedia.org/wiki/Null_object_pattern#Java), which throws away places where you would use `null` for "no object applicable", instead providing a stubbed subclass of what's required.
- So, one day, Java 12 overhears other programming languages talking about ["arrow functions"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) and ["yield keyword"](https://realpython.com/introduction-to-python-generators/), and being the [enterprising](https://en.wikipedia.org/wiki/Jakarta_EE) language that it is, it goes and creates its own arrows and yields. [Switch expressions: we have those features at home](https://howtodoinjava.com/java14/switch-expressions/).
- You can't return multiple values, so you just make a brand new class that has the fields you want, and then return that.
- `array.contains(item)`? No! Too easy. You need to choose between [`Arrays.asList(array).contains(item)`, `Arrays.stream(array).anyMatch(item::equals)`, `IntStream.of(array).anyMatch(x -> x == item)`, and `Set.of(array).contains(item)`](https://stackoverflow.com/a/1128728/1558430), depending on what type of array it is, and [whether your thing is hashable](https://stackoverflow.com/a/1128899/1558430).
- There is no [tail call optimisation](https://stackoverflow.com/questions/20826786/does-java-support-and-optimize-away-tail-recursive-calls). A solution proposed by JOOQ is [avoid recursion](https://blog.jooq.org/top-10-easy-performance-optimisations-in-java/).

## Testing, mocking, and stuff

- The java repl is called `jshell`. If you have a JDK installed, you already have it.
- Java-style assertions use the colon, i.e. `assert a == 0: "a is not 0.";`
- Since Java allows you to have memory leaks, you'll hopefully [profile your application](https://stackoverflow.com/questions/10108942/how-to-memory-profile-in-java) every time you push it.
- You cannot [down-compile new Java features into an older VM](https://discuss.gradle.org/t/why-cant-i-use-different-sourcecompatibility-targetcompatibility-with-hello-world/11958) by setting `targetCompatibility` lower than `sourceCompatibility`. That would be too easy.
- `Objects.requireNonNull` apparently supersedes `== null` checks. In nonpublic methods, you can also use `assert` (because you control the code).
- ["Mocking a final class is just as easy as mocking any other class"](https://www.baeldung.com/mockito-final). If you can't, you can still [write a `@Delegate` class that wraps every method of the final class](https://stackoverflow.com/a/14292975/1558430), and then test the final class there. It's just subclassing [with extra steps](https://awwmemes.com/t/extension-ladder).

## Packages, imports, and ecosystem

- `from a import b as c` [is impossible](http://stackoverflow.com/q/2447880/1558430). Classes must be imported with their own names.
- There is no such thing as a [nested package](https://stackoverflow.com/questions/26509219/nested-packages-in-java), but there is such a thing as a subpackage (`foo.bar`). The package name can also be [anything you like, regardless of where you place the file itself](https://stackoverflow.com/a/8395934/1558430), so you can throw files wherever you like :) (and get fired)
- If maven is used, `pom.xml` decides what is compiled along as dependencies.
- `sourceCompatibility` is which version of Java you wrote your code in. `targetCompatibility` is the VM version that your app should run in. For some reason, you can set your source code's Java version to be different from the version of bytecode that it generates, to be different from the JDK compiling it. For example [here](https://stackoverflow.com/a/22326989/1558430), you can write Java 1.5 code, compile with JDK 1.6, but it won't run in a Java 1.5 VM. Make sure your source version and JDK versions match at least.
- Spring is a dependency injection framework.
- [Spring Boot is an extension on top of Spring](https://www.baeldung.com/spring-vs-spring-boot). That's why it's got that space in the name.
- With [Lombok](https://projectlombok.org/features/all), you can make a Builder by simply [marking something with `@Builder`](https://stackoverflow.com/a/51637774/1558430).
- You can use a class in Java without importing it **if**: a) `java/c` know where to find the class, and b) you know the full name of the class. In the case of class name conflict, you [don't import it](https://stackoverflow.com/a/7547268/1558430), opting to use it through its fully qualified package path instead.
- `.java` files compile to `.class` files, which are then packaged into `.jar` (Java ARchive) files.
- [`.jar` files can also contain media](http://en.wikipedia.org/wiki/JAR_%28file_format%28)
- A `.war` file is [a bundle of `JSP` files, as well as the assets required to run a web application](https://pediaa.com/what-is-the-difference-between-jar-and-war-files/), like HTML, CSS, and JS files. [`.jar` files can also be used to start a web server](https://stackoverflow.com/questions/5871053/difference-between-jar-and-war-in-java#comment52876035_5871096), supposedly.
- You can import `blah.blah.blah` without having the actual source code -- as long as you have their `class`es.
- Maven and Gradle [are](https://blog.idrsolutions.com/2018/07/what-is-a-package-manager-and-why-should-you-use-one/) Java's equivalent of npm. It just so happens that those tools also help you build the project, because Java projects need to be built.

## Garbage

- There are [different garbage collectors](https://stackoverflow.com/questions/54615916/when-to-choose-serialgc-parallelgc-over-cms-g1-in-java) to choose from, including [`-XX:+UseG1GC`, the old but gold serial GC, and `-XX:+UseParallelGC`, which was improved in Java 17](https://www.optaplanner.org/blog/2021/09/15/HowMuchFasterIsJava17.html). The parallel one has higher pause times if run on single-core machines.
- There is a [don't garbage collect](https://blogs.oracle.com/javamagazine/epsilon-the-jdks-do-nothing-garbage-collector) compiler mode that shows you where the memory is likely to run out in your program. The epsilon compiler mode can also be used when a program exits quickly (where there's no point to GC at all), and if you write latency-critical code in java for some reason.
- [Immutable objects are easier to garbage collect](https://www.overops.com/blog/improve-your-application-performance-with-garbage-collection-optimization/) because since they are frozen on instantiation, *they cannot possibly contain a reference to anything that is created later*.
- Run Java applications in real time by [disabling GC](https://news.ycombinator.com/item?id=24897540). High frequency traders (who don't know how to write in anything else) do that.

## Things that don't fit other categories

- [Beans](http://en.wikipedia.org/wiki/JavaBean) are plain objects that contain many other objects, with their properties all encapsulated in getters and setters. Beans cannot have constructors with arguments.
- Beans are used for cross-network class transfers.
- [Enterprise JavaBeans](https://www.infoworld.com/article/2076777/a-beginner-s-guide-to-enterprise-javabeans.html) seem to be an architecture for running encapsulated code on a client-server setup. Client runs a bean wrapper of some sort. The server contains beans that run the code. This makes EJBs quite similar to a one-server microservice model, [with some low-level differences](https://stackoverflow.com/questions/30237292/is-the-microservices-architectural-pattern-similar-to-ejb-1-0).
- [`getBoolean(thing, prop)`](http://with-example.blogspot.ca/2013/07/booleangetboolean-vs-booleanparseboolean.html) checks if thing.prop is `"true"`; `parseBoolean(thing)` check if `thing` is `"true"` regardless of case.
- `Integer.getInteger(string nm)` gets you the integer value of the system property `nm`... not parsing `nm`. Use [`Integer.parseInt`](https://stackoverflow.com/a/4397363/1558430) instead.
- HTML is allowed in javadoc because someone decided it would be a good idea to allow raw tags in there, so maybe it will look better when the doc is generated.
- Liquibase is used to run migrations, [so you can avoid writing raw SQL](https://reflectoring.io/database-migration-spring-boot-liquibase/). You declare these potentially in YAML format, so I don't know how data migrations work, and the internet is not sure if Liquibase is the tool for data migrations at all.
- [`a += b` is not the same as `a = a + b`](https://stackoverflow.com/questions/8710619/why-dont-javas-compound-assignment-operators-require-casting/8710747#8710747), because fucking Java loves leaking implementation detail. `a += b` is the same as `a = (typeof a) (a + b)`, where `(a + b)` will be recast. `a = a + b`, on the other hand, clearly does not do typecasting (and thus gives you "Incompatible type exceptions").
