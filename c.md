# C

1. C is statically and weakly typed. In the compromise between productivity and verbosity, this is the worst possible combination.
1. The variable convention seems to be `underscored_things`.
1. *Pointers* (e.g. `int* something`) are something you declare. It *points* to something of the declared type. It should only be assigned addresses (`&something`).
1. "Accessing" what a pointer is pointing to uses something like Python's unpacking syntax: if `int* foo` points to something that's `14`, `*foo` gives you `14`.
1. A pointer can also be used as if it were a variable. For example, if `*foo` were pointing at something that's 14, you can just `*foo = 50` to change it to 50.
1. Trying to assign something to your pointer's address, when you haven't initialised it (i.e. `int& foo; &foo = 1;`) will give you a segfault.
1. Declare an array of things: `type var_name[size];`, not `type [size]var_name;`.
1. `sizeof` is a thing, and gives you the size of the type, not the object. This means to know how long an array is, you need to do some maths.
1. `cin >> any_variable` assigns the variable (including array items) with whatever the user typed in standard in.
1. [`O=(int)&O`](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#int-_2048ointo______): setting a variable equal to the int cast of its memory address is a very short way of generating a random integer.
1. [`yada = - ~yada` is equivalent to `++yada` because of 2's complement.](https://github.com/duckythescientist/obfuscatedLife/blob/master/remarks.md#while__-__2048___oo0x41c64e6d123450x7fffffff1024150)
1. "Pro tip: when you develop with gcc, don't settle for anything less than `gcc -ansi -pedantic -Wall`" -- [TeMPOraL](https://news.ycombinator.com/item?id=7156405) (`-ansi` being [`c89`](http://stackoverflow.com/questions/10300114/should-i-use-ansi-or-explicit-std-as-compiler-flags))
1. "You can go further and specify a particular standard, plus extra warnings not included in -Wall: `gcc -std=gnu99 -pedantic -Wall -Wextra -Werror`" - [nitrogen](https://news.ycombinator.com/item?id=7156405)
1. "gcc is 'Gnu Compiler Collection'. ~~If you pass it a C++ file, it will invoke the C++ compiler ('g++') behind the scenes."~~ No it bloody won't.
1. Undeclared variables are implicitly `int`s. This was deprecated after C99, however.
1. Writing cross-platform C code: [start from the beginning](http://www.ski-epic.com/source_code_essays/ten_rules_for_writing_cross_platform_c_source_code.html)
1. There is such a thing as a [C interpreter](http://www.reddit.com/r/programming/comments/2latu2/c4_c_in_4_functions/clt70uk) and C Scripting... but you probably don't want to do that with `gcc`. `tcc` is a faster choice (`#!/usr/local/bin/tcc -run`)
1. `make` can compile a source file directly, like `make file` directly. If the file is called `file.c`, the argument must have its `.c` omitted.
1. `Makefile` [tells make what to do in the same directory](http://c.learncodethehardway.org/book/ex2.html). Inside you can specify `CFLAGS`.
1. Makefiles must be [indented with tabs](http://stackoverflow.com/questions/2131213/can-you-make-valid-makefiles-without-tab-characters).
1. [`CFLAGS="-Wall -Wextra -Werror -std=c99 -pedantic -g3" splint $1 && make $1 ...`](http://stackoverflow.com/a/2574456/1558430).
1. [C99](https://en.wikipedia.org/wiki/C99) is stricter than C89; C11 (aka C1X) does not appear to be any stricter.
1. [`#include "files"`, and `#include <headers>`.](http://stackoverflow.com/a/50266/1558430)
1. [`splint`](http://splint.org/) lints C.
1. Splint *really* wants any function calls with unused results to have `(void)` in front of them.
1. ~~`puts` is a *nix command.~~
1. The only way to write a function that accepts no arguments is to have a `void` in it, i.e. [`rtype func_name(void) { ... }`](http://stackoverflow.com/a/3156437/1558430)
1. `main` must [either](http://stackoverflow.com/questions/3156423/why-dont-we-use-void-in-main#comment3246503_3156423) take nothing (`void`), or exactly these two parameters: `int argc, char* argv[]`, and return an `int`.
1. `$()` in Makefile is [more portable](http://stackoverflow.com/questions/2214575/passing-arguments-to-make-run#comment2167270_2214593) than `${}`.
1. Valgrind the debugger does various checks after compilation. It needs the `-g` flag for CC above to be set.
1. `//` commenting must not be used.
1. `printf` and co. expect `%f` to actually be `double`, not `float`.
1. [`float` requires a trailing `f`](http://stackoverflow.com/a/5026592/1558430); `double` does not. This means all number literals with decimal points are doubles. However, it is possible, for some reason, to assign `float to_a_doule = 10.0`, or `double from_a_float = 10.0f`.
1. `long` requires a trailing capital `L`, and its formatting string is `%ld` ('long number').
1. `%e` (scientific notation) should only be used on `double`s.
1. For whatever reason, `[]` is used to denote arrays; `{}` is used to express an array literal.
1. [If you omit the size of the array, an array just big enough to hold the initialization is created.](http://www.tutorialspoint.com/cprogramming/c_arrays.htm)
1. Splint disallows `an_array[10]` to be initialised with an array that is not 10 items long. If Splint isn't there, then the array default is 0.
1. There is no point writing different code for array access. [Compilers know.](http://stackoverflow.com/questions/4939834/in-c-accessing-my-array-index-is-faster-or-accessing-by-pointer-is-faster)
1. [`sizeof an_array`](http://stackoverflow.com/a/204232/1558430) tells you the size of the array, *or* the size of its pointer, [depending on where you got it](http://stackoverflow.com/a/10349610/1558430). ["the usual solution is to pass the length along with the array as a separate argument."](http://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c#comment28408105_10349610) (which `argc` is)
1. [A bug in Splint](http://stackoverflow.com/questions/10257470/splint-parse-error-in-for-loop) causes variable initialisation inside a for loop to be impossible.
1. Strings are `char[]`s or `*char`s. They **must** be manually terminated with [a null byte (`\0`)](http://stackoverflow.com/questions/18688971/c-char-array-initialization#comment27531014_18688992), or Valgrind will complain.
1. Arrays of strings are `char[][]`, `*char[]`, or ... `**char` (?), where `char[number of strings][size of each string]`
1. [`auto`](http://stackoverflow.com/questions/2192547/where-is-the-c-auto-keyword-used) makes a variable have a function-local lifetime, which is the default. `static` cannot be used.
1. The `*` in `int *foo` is attached to the variable. [`int* foo` is invalid syntax.](http://stackoverflow.com/a/4203080/1558430)
1. It is [not possible](http://stackoverflow.com/a/4203948/1558430) to declare multiple variables on the same line, because Code Complete says so.
1. [Include guards](https://en.wikipedia.org/wiki/Include_guard) prevent the same header from being included more than once. [`#pragma once`](https://en.wikipedia.org/wiki/Pragma_once) works better [in every way](http://stackoverflow.com/a/6793411/1558430). Unfortuntely, since Oracle doesn't support pragma once, we are [stuck](http://stackoverflow.com/a/1144110/1558430) with include guards.
1. There are [only three error codes](https://en.wikipedia.org/wiki/Errno.h) you can use.
1. > ["The `.PHONY` rule keeps make from doing something with a file named `clean`."](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/) By not looking for files called `clean`, it improves performance.
1. [`main` must be a function.](http://stackoverflow.com/questions/33305574/why-does-const-int-main-195-result-in-a-working-program-but-without-the-const) Don't let anyone tell you different.
1. When creating an array of a given type, a continuous chunk of memory is assigned, exactly (the size of the type) * (the number of things).
1. [Given the way arrays are created](http://stackoverflow.com/questions/381542/with-c-arrays-why-is-it-the-case-that-a5-5a), `foo[4]` is really `*(foo + 4)` or `*(4 + foo)`, which makes `4[foo]` equivalent.
1. `thing_t` is supposed to mean "a type called 'thing'". C programmers are against the Hungarian notation.
1. [C pointers are not integers](http://nullprogram.com/blog/2016/05/30/); Any pointer type may be converted to an integer type, but the result depends on implementation. (If the pointer is a large negative number, for example, then the behaviour is undefined.)
1. [`foo->bar` is equivalent to `(*foo).bar`, i.e. it gets the member called `bar` from the struct that `foo` points to.](http://stackoverflow.com/a/2575050/1558430) It serves as syntactic sugar, to make code look nicer if all you have is a pointer.
