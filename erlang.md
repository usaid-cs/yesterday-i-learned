[Erlang has no strings](http://learnyousomeerlang.com/starting-out-for-real)

- Erlang has [guards](http://learnyousomeerlang.com/syntax-in-functions#guards-guards) like `old_enough(0) -> false;`, or `old_enough(X) when X >= 16 -> true;`.
- Erlang is a "stricter" functional programming language. That means functions are one-to-one mappings, except where you break that referential transparency somewhere.
- The [Actor model](https://en.wikipedia.org/wiki/Actor_model)... an actor can receive messages, create other actors, and send messages to other actors/tell other actors what to do with these messages. And it is [assumed](http://www.brianstorti.com/the-actor-model/) at this point that each actor can do a function, non-blocking action.
- A Supervisor manages crashing actors (now called "processes"). The supervisor happens to also be an actor, because in Erlang, everything is an actor.
- There is a cost to sending messages. This makes Erlang is limited in performance by the overhead of parallelism.
- Expressions in `erl` (the shell) will be evaluated only if they are terminated with `.` (the space can be substituted with a linebreak)
- **Variables must be capitalised.**
- Variables can be set multiple times, but only if the values are the same as what they already have. The reason the shell gives is `no match of right hand side value`. So maybe you can `assert` things with this property.
- Like python, [use `_` to store results of an expression if you don't care about it.](http://learnyousomeerlang.com/starting-out-for-real) Unlike python, however, it is impossible to _read from_ `_.`
- Atoms are like ruby symbols, with the same names as values. **Atoms must not be capitalised.**
- `=:=` appears to be the exact comparison operator. `5 =:= 5.0.` is false, but `5 == 5.` is true.
- It is impossible (verify?) to add together two different types, but possible (verify?) to compare two different types. ~~It is just going to be false.~~
- [All numbers are "less than" atoms if compared.](http://learnyousomeerlang.com/starting-out-for-real) The full list is as such: `number < atom < reference < fun < port < pid < tuple < list < bit string`
- Tuples are written with `{curly, braces}`. Unpacking is also done like so: `{A, B} = {1, 2}.` You can also assert various things by partially unpacking, like `{1, B} = Sometuple.` would raise some sort of error if the first element in `Sometuple` is not 1.
- [There is no _good_ string type.](http://erlang.org/doc/reference_manual/typespec.html) Strings are just lists. `[97, 98, 99].` will automatically become the string `"abc"`, and ~~it appears to do so only if all numbers in the list are between 32 and 126~~no it does some crazy things.
- `%%` is [how you start comments](https://github.com/rabbitmq/rabbitmq-server/blob/master/src/rabbit_alarm.erl).
- File extension is `.erl`.
- Most operators are as expected, except `=:=` (compare exactly equal), `/=` (compare not equivalent), and `=<`, which should have been `<=`.
- `++` returns two lists concatenated: `[1] ++ [2] = [1,2].` (this actually assigns the RHS to the LHS), `[1] ++ [2] == [1,2].` (true), `[1] ++ [2] =:= [1,2].` (also true)
- `--` returns whatever left from cancelling two lists out, from left to right of each list: `[2,4,2] -- [2,4] =:= [2].` It is possible to try and subtract from the first list more elements than what it holds; `[2,4,2] -- [2,4,2,4].` just gives you an empty list.
- The `[A|B]` syntax breaks a list up to head and rest, where the head is the first element, and _the rest is the rest of the list_. Docs may call the rest, the "tail".
- If you accidentally type in `erb` instead of `erl`, that gives you "ruby templating".
- The A in `[A|B]` can also be any number of CSVs, and B can be any list, e.g. `[1, 2, 3, 4 | [5, 6 | [7, 8]]] =:= [1,2,3,4,5,6,7,8].`
- List comprehension is done in the form `[ X || X <- list ]`, read the same way as `[X for X in list]`. For example, `[ 2*N || N <- [1,2,3,4] ].` returns a list with everything multiplied by 2.
- Conditions can be attached to list comprehensions as well, e.g. `[ X || X <- list, cond ]`, read the same way as `[X for X in list if cond]`. For example, `[2*N || N <- [1,2,3,4], N < 4].` returns `[2,4,6]`.
- Multiple lists and conditions can be used in the same list comprehension... `[ 2*N || M <- [1,2,3,4], N <- [1,2], M < 3, N < 2].` reads `[2*n for n in [1,2] if n < 2 for m in [1,2,3,4] if m < 3]`, and would return `[2,2]`.
- If you need to work with bits and bytes, then read [this](http://learnyousomeerlang.com/starting-out-for-real#bit-syntax). Otherwise don't worry about it.
- [BEAM](http://erlang.org/faq/implementations.html) ("Bogdan/Björn's Erlang Abstract Machine") is Erlang's reference VM. Elixir uses the same VM, along with [many others](https://github.com/llaisdy/beam_languages), almost all of which are unpopular.
- The `erlang` module (think of it as "namespace") is automatic. `element()`, `hd()`, and `tl()` are all in the `erlang` module. You can call functions in a module with `module:function(...)`.
- [There is no direct way to get the type of something](https://stackoverflow.com/a/28377262/1558430).
- To create a module, a file called `name.erl` must have `-module(name).` at the top. The `name` inside is an atom, so it must be in lower case.
- To export a function in a module, write your function, say `add(A,B) -> A + B.`, then add `-export([add/2, anotherfunction/n, ...]).` to the file, where `2` is the number of arguments that the function takes.
- To import a function in a module, add `-import(name, [add/2, anotherfunction/n, ...]).` to the file, where `2` is the number of arguments that the function takes. You don't need to import a function to use it though, so maybe [don't do that](http://www.erlang.se/doc/programming_rules.shtml#HDR26).
- Everyone separates lines with `;`; this language uses `,`. Because reasons.
- You [**MUST**](https://www.thegeekstuff.com/2010/05/erlang-hello-world-example/) export your entry point before `erlc` can compile your program with it. Do so with `-export([main/0]).` (or something like that)
- You need to compile every single file with `erlc` (turning them into `.beam`s) before you can run your main program. If you don't like that, use [`erl -make`](https://stackoverflow.com/a/2549026/1558430) or [write your own makefile.](https://stackoverflow.com/a/2549228/1558430)
- The erlang kids still contribute to the [OTP](http://learnyousomeerlang.com/what-is-otp) (open telecom platform). It implements libraries, modules, and standards that every erlang application should follow.

---

    Checkpoint: http://learnyousomeerlang.com/syntax-in-functions
