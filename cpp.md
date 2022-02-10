# C++

- [Neither C nor C++ are type-safe](https://en.wikipedia.org/wiki/Type_safety#Strong_and_weak_typing). One `memcpy` call and you can put anything in memory meant for some other type.
- [_References_ (e.g. `int& something`)](https://stackoverflow.com/questions/4305673/does-c-have-references) are C++ only. They are effectively constant final pointers. `int& c = a;` means "C points to whatever A is already pointing to", which is safer, and simpler to understand.
- Creating a reference to something uninitialised may accidentally give it value. `int a; int& b = a;` will suddenly make `a` nonzero. Use `-Wuninitialized` (part of `-Wall`) to detect this error.
- It is impossible to write `int& something;`. You must assign it something on initialisation.
- ["Member-access with pointers uses `->`; member-access with references uses `.`](https://stackoverflow.com/a/57780/1558430)
- The [`~ClassName`](http://stackoverflow.com/a/1395509/1558430) definition in a class denotes a destructor, because `ClassName` initially is a constructor, but negated by `~` to give the semantic meaning of a destructor.
- `public:` followed by an indented block of methods, means that anything inside the block is public (same applies to `private`)

```
class Rectangle {
    int width, height;
    public:
        void set_values (int,int);
        int area() {
            return width*height;
        }
};  // semicolon?
```

- [Trigraphs](http://stackoverflow.com/questions/7825055/what-does-the-c-operator-do) are character mappings that map three characters to a single one, not found on older keyboards. For example, "??!" maps to "|".
- You are supposed to use [Smart pointers](http://en.wikipedia.org/wiki/Smart_pointer) now (C++11), which manages memory allocation for you. You should never (supposedly) create references to objects like in C# and Java either; just create objects and C++ will manage the memory for you.
- Operators can be overloaded; for example, to overload `+` for adding two `Class`es together, use `Class operator+(const Class&, const Class&);`
- [Function overloading](https://www.reddit.com/r/programming/comments/3en2px/til_you_can_use_function_overloading_in_c/) is not a standard feature in C, but you can do it in C11 in an ugly way.
- [Ugly (yet valid) C syntax](http://blog.robertelder.org/weird-c-syntax/):
  - Inline return type definitions are possible: `struct foo {...} function () { return foo(...) }`
  - Returning pointers to functions, where `foo` takes in nothing, and returns a function `bar` that takes an int and returns an int: `int ( *foo(void) ) (int i) { return bar }`
  - [`"Hello"[5] == 5["Hello"]`.](http://stackoverflow.com/a/381549/1558430)
- You can still specify the namespace, `foo::some_func()`, in a file/method `using namespace foo`.
- `std::cout` is [more proper](http://stackoverflow.com/a/4781861/1558430) than `printf` in C++.
- If your header files are C++ only, [name them `.hpp`](http://stackoverflow.com/questions/152555/h-or-hpp-for-your-class-definitions). Otherwise, header files that can be used for both C and C++ should use `.h`.
- C++ struct values can have defaults:

```
struct Foo {
    int no_default;
    int yes_default = 0;
};
```

- There is [struct inheritance](http://stackoverflow.com/questions/979211/struct-inheritance-in-c). Use the colon to denote structs with all fields in the parent struct:

```
struct A { };
struct B : A { };  // Has all A's fields
```

- > [In C++, a struct can have methods, inheritance, etc. just like a C++ class.](http://stackoverflow.com/a/979241/1558430)
- It is possible--get this--to redefine a class/instance method. Instead of using [interfaces](http://www.tutorialspoint.com/cplusplus/cpp_interfaces.htm) like normal humans would (hint: they don't exist), you may define a class in the header, then change the definition of the class.
- According to your colleagues, `new Something()` gives you a pointer to something, whereas `Something()` gives you the exact thing. For the case of `std::string`, [this helpful post](http://stackoverflow.com/questions/8069092/c-string-declaration) explains **four** variants:

```
1. `std::string s = std::string("foo");  // creates a temporary std::string object containing "foo", then assigns it to s`
2. `std::string s = "foo";`  // equivalent to 1. Internally, this runs one of the constructors in std::string that accepts const char*.
3. `std::string s = new std::string("foo"); // compiler error while trying to assign a pointer to a variable of type std::string`
4. `std::string s("foo");`
```

> "One of the main benefits of using std::string is that it manages the underlying string buffer for you automatically, so new-ing it kind of defeats that purpose."

- Function/method names are [`UpperCamelCase`](https://google.github.io/styleguide/cppguide.html#Function_Names), unless they are cheap, (e.g.) "so cheap that you normally wouldn't bother caching its return value when calling it in a loop", in which case they are `underscored_things`; such a function normally consists of only one comparison.
- [`do {...} while (0)`](http://www.pixelstech.net/article/1390482950-do-%7B-%7D-while-%280%29-in-macros) is the de facto way of writing a macro that expands correctly, whether in a one-liner if statement, or in an if-else.
- Macros are not substituted in macros. (Otherwise `#ifdef`s will get complicated)
- Headers can contain other headers, but should not.
- Rule: When addressing compile errors in your programs, always resolve the first error produced first.
- Vectors are just dynamic arrays. A vector comes with convenient functions like [`push_back()`](http://www.cplusplus.com/reference/vector/vector/push_back/) and `pop_back()` to use a vector as a queue or a stack.
- Compared to arrays, **vectors** consume more memory in exchange for the ability to manage storage and [grow dynamically](http://stackoverflow.com/a/6632991/1558430) in an efficient way. Use vector unless you have a very, very small array, and know what you are doing.
- If both a `<foo>` and `<foo.h>` exists, then the `.h` version is deprecated. Use the non-h version.
- When used to get strings, [`cin >> a_string` will only get the input up to a space](http://www.cplusplus.com/doc/tutorial/basic_io/). To get the whole line, use `getline(cin, a_string)` instead.
- [Anything created with `new` and not `delete`d is automatically leaked.](http://stackoverflow.com/questions/7242493/how-to-create-a-memory-leak-in-c) [Anything manually allocated with `malloc` and not `free`d is also automatically leaked.](http://www.geeksforgeeks.org/what-is-memory-leak-how-can-we-avoid/)
- [Use `delete` by itself to free a single object. Use `delete []` with square brackets to free a heap array.](http://stackoverflow.com/a/8417851/1558430)
- Unless you do systems programming, [there is almost no reason to pick C over C++](https://softwareengineering.stackexchange.com/a/113316/116811). Simply [not using the C++ features you don't use](https://softwareengineering.stackexchange.com/a/113398/116811) is also an option.
- You can't `cout` a string unless you [`#include <string>`](https://stackoverflow.com/a/6321005/1558430).
- Pointers and references are complicated. As such, C++11 provides an additional way to declare yet another kind of reference, called [rvalue referneces](http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2004/n1690.html), using the double-ampersand syntax: `A&&`.
- Header files exist so [you don't need to recompile a class if the definition didn't change](http://www.math.uaa.alaska.edu/~afkjm/csce211/handouts/SeparateCompilation.pdf) (PDF).
- In a move that could possibly backfire, the C++20 lambda syntax [uses square brackets](https://www.bfilipek.com/2020/08/lambda-syntax.html), like `[](auto x, auto y) { /*...*/ };`.
- A `struct`'s members are public by default. A `class`'s members are private by default.
- [`and`](https://stackoverflow.com/questions/44381428/and-keyword-in-c) is the exact same as `&&`.
- [`const`](https://quuxplusone.github.io/blog/2022/01/23/dont-const-all-the-things/) is used when you want to pass in an expensive variable by reference (instead of by value, which makes copies; this happens a lot with strings), but you want to ensure the variable is not modified once passed in. Function parameters that do such a thing should be marked with `const`.
