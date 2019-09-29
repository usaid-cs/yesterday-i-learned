![](http://i.imgur.com/V7Fr14e.jpg)

- Ordering of python lists is persistent. [src](http://stackoverflow.com/a/13694053)
- Pycharm hinting:

```
"""
Exploit the workers by hanging on to outdated imperialist dogma which
perpetuates the economic and social differences in our society.

@type peasant: Person
@param peasant: Person to oppress.
                http://grammarist.com/usage/oppress-repress-suppress/
"""
```

- [PEP 3107](http://legacy.python.org/dev/peps/pep-3107/) / PEP 484 hinting:

```
def foo(a: 'what is a', b: 5 + 6, c: list) -> max(2, 9):
    # foo accepts a (commented), b (11), c (any kind of list), and returns 9
```

- Under normal circumstances, `register.simple_tag` is all you need for your django templating needs.
- To pretty-format a JSON file, do `cat ugly.json | python -mjson.tool > pretty.json`.
- `re.VERBOSE`, aka `re.X`, will ignore all whitespaces in a regex. Will Also ignore everything after a `#`.
- Python does not raise a rounding exception when a large number is used. The typical check is `n + 1 == n`.
- To speed up a read-only query, try adding `.values_list(fields...)` to a QuerySet, which returns simple tuples.
- It is absolutely possible that django `loaddata` is a douchebag.
  Therefore, to import all objects without referential errors, use `python manage.py loaddata init_dev.json`,
  which provides all references before inserting.
- Multiple args: calling a `function(a, b, **kwargs)` where kwargs contains `a=4` or `b=[]` will raise an Exception.
- `dict(a=4,b=5)` === `{'a': 4, 'b': 5}`
- There is such thing as a [for-else](http://stackoverflow.com/questions/19061990/python-dividing-integers-in-a-list-by-another-list-until-the-result-is-zero/19062037?noredirect=1#comment28174201_19062037) condition, where the `else` part doesn't execute only if the for loop is `break`ed from within.
- `for-else` also runs `else` if the loop is never run (e.g. has 0 items).
- There is also a [while-else loop](http://www.tutorialspoint.com/python/python_while_loop.htm) that runs when the variable changes to `False`.
- [Django creates the project for you.](https://docs.djangoproject.com/en/dev/intro/tutorial01/#creating-a-project)
- Variables can be _accessed_ from an inner scope, but the outer value of the same variable will not be changed. Use [`nonlocal`](http://stackoverflow.com/a/1261961/1558430) to change the outer value.
- `*args` is of type tuple, not list.
- Use the `for-else` loop to avoid setting "flag variables", e.g. `found = False ...`. Faster than flags in Python.
- `dict(a dict)` clones the dict (for one level).
- `list(a list)` clones the list (for one level). `list(a) is not a`.
- These three are successively better than the former.

```
for k in d:
    print k, d[k]

for k, v in d.items():
    print k, v

for k, v in d.iteritems():  # Not python3
    print k, v

for k, v in six.iteritems(d):
    print k, v
```

- `dict`s have a `setdefault` method: avoids `KeyError`s.
- Instead of updating dictionaries with another dictionary, there is a `ChainMap` in Python 3 that handles the common "defaults" use case.
- [Use full kwargs everywhere, except in loops](http://youtu.be/OSGv2VnC0go?t=31m39s)
- `NamedTuple` is a subclass of `Tuple` that lets you express what the tuple values actually are.
- Built-in tuple unpacking (`a, b = (1, 2)`) is faster than loading them with indices.
- Always concatenate strings with `.join`.
- Python 3.4 can ignore all but some exceptions using `with ignored(TypeError, ValueError, ...):`. Actually, [it might been renamed to `contextlib.suppress`](https://bugs.python.org/issue19266).
- Generator expressions, e.g. `sum(i for i in list)` is faster than `sum([i for i in list])`.
- Django or nosetests runs any `TestCase` subclass in files with their names beginning with `test` when you run `manage.py test`.
- `django.http` contains http error classes that handle the nitty gritty (e.g. allowed methods in 405)
- [You cannot make a `dict`, `json.loads`, `json.dumps`, or otherwise, with integer keys in python](http://stackoverflow.com/questions/1450957/pythons-json-module-converts-int-dictionary-keys-to-strings).
- If you are a jackass, you [can](http://stackoverflow.com/a/481755/1558430) write recursive lambdas.
- Decorators can return functions that are already wrapped with decorators, by virtue that decorators can be wrapped in anything.
- Every module is imported only once, but every `import` call will invoke a check to make sure the module is imported.
- `@functools.wraps(fn)` is used to wrap a the wrapper function inside a decorator that helps preserve the original function's docstrings.
- [`apply`](http://docs.python.org/2/library/functions.html#apply) is a keyword. It is a bit like `map`.
- "Almost every time you use `reduce` means you are doing something wrong", so `reduce()` was moved into `functools.reduce()` in Python3.
- [`__contains__`](http://stackoverflow.com/questions/1964934/what-is-contains-do-which-one-can-call-contains-function) controls the behaviour of `a in obj`.
- [Django `smart_str`](https://docs.djangoproject.com/en/1.4/ref/unicode/) along with `smart_unicode` probably solves all of Python 2's problems.
- [Python `Enum`](http://stackoverflow.com/a/1695250/1558430) Spoiler: 3.4+
- The `buffer` type is used to create [multiple "varied" reference to some parts of a large object in memory](http://stackoverflow.com/a/3422740/1558430).
- `for` creates a new scope. `for foo in foo` if `foo` is `"bar"` then it prints b, a, then r.
- Keys can be pretty much anything, and they are not stringified: `{None: 'b', 1: 5, <function __main__.<lambda>>: 4, '1': 6}`
- Taking that right back, [lists cannot be dictionary keys](https://wiki.python.org/moin/DictionaryKeys).
- "You don't mock out any part of our system, you mock out other people's code"
- [`assertEquals` is deprecated](http://docs.python.org/2/library/unittest.html#deprecated-aliases)
- If `assertEqual` receives two `dict`s, it automatically calls `assertDictEqual`.
- [`itertools.cycle`](http://docs.python.org/2/library/itertools.html#itertools.cycle): for when you want to loop over something, over and over
- Django's `QueryDict` can be converted to a dict by calling `.dict()`.
- [`StringIO.StringIO`](http://docs.python.org/2/library/stringio.html) is **not** used for performance reasons. It is used to [convert a string into a memory-bound file](http://stackoverflow.com/questions/7996479/what-is-stringio-in-python-used-for-in-reality) so functions that expect a file can work without writing the string to a file first.
- There is a `3to2`!
- You can [decorate functions with classes](https://bitbucket.org/jsbueno/lelo/src/ab9837ef82001329c421afbfe7e0759c6ec0f16d/lelo/_lelo.py?at=master) that have `__call__`!
- Instance variables (`class.foo == 'far'`) are class variables (`class.foo == Class.foo`) as long as [the instance doesn't change its instance variable's value](http://stackoverflow.com/a/69067/1558430).
- `[:]` (aka `[None:None]`) [copies a list](http://stackoverflow.com/a/2612815/1558430) (Fast copy; Thanks Ford)
- `enumerate()`: returns tuples with index as the first value
- `re.sub(pattern, repl, string)` is technically `re.sub(pattern, lambda repl: repl, string)`, which allows [text munging](https://docs.python.org/2/library/re.html#text-munging).
- `yield`s are formally referred to as [coroutines](http://en.wikipedia.org/wiki/Coroutine) -- function with multiple entry/resume points.
- The `signal` package has an `alarm` method that can [timeout a long-running function](https://wiki.python.org/moin/PythonDecoratorLibrary#Function_Timeout).
- [Python3 exceptions are only accessible within the `except` block, for GC reasons](http://www.toptal.com/python/top-10-mistakes-that-python-programmers-make). Interestingly, even if the same name existed outside the `except` block, [Python3 will remove the variable of the same name from the outer scope](http://www.wefearchange.org/2013/04/python-3-language-gotcha-and-short.html).
- Set generators are [already available in python2.7](http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Dictionary_and_set_comprehensions).
- The `set`'s `discard` method makes stupid things like `new_set = {x for x in old_set if x != 'foo'}` a little bit redundant.
- Lambda expressions can have parameter defaults, positional and keyword arguments!
- Django Foreign keys default to `None`.
- `__future__` imports can only be done at the top of a file.
- Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
- [You can and should use monads in your code in almost any programming language](http://www.valuedlessons.com/2008/01/monads-in-python-with-nice-syntax.html)
- `a >> b` can be overridden using the magic method `__rshift__`.
- I don't know what the author was talking about, but python has something called the [bidirectional generator](https://www.google.ca/search?q=python+bidirectional+generator&oq=python+bidirectional+generator&aqs=chrome..69i57.4705j0j7&client=ubuntu-browser&sourceid=chrome&es_sm=0&ie=UTF-8) which no one explained.
- Override `parse_start_url` to diagnose Scrapy errors that occur on start urls.
- In Django, `admin.site.register(Model)` doesn't need an admin (e.g. `admin.site.register(Model, ModelAdmin)`) if all you want is an automatic form.
- `\d` [isn't](http://stackoverflow.com/a/6479605/1558430) `0-9` -- it also contains digits from other locales.
- Contrary to popular opinion, `requirements.txt` simply came from `pip freeze > requirements.txt`.
- `pip freeze` also removes duplicate package requirements, so it helps you clean up the file in a way.
- Generate random test urls using `itertools.product`: http://stackoverflow.com/questions/2535924/simple-way-to-create-possible-case/2535934#2535934
- ~~It is not necessary to `urlunparse` a url before generating a new url with parts changed. `urlparse(url, scheme='http')` changes the schema of that url to http.~~ I lied. It only works for `scheme`.
- `unicode`'s `translate` is different from `str`'s `translate`; their translation tables are [not interchangeable](http://stackoverflow.com/questions/10385419/python-typeerror-expected-a-character-buffer-object-personal-misunderstanding) (`unicode` strings require `unicode` tables)
- Every single [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/#basic-usage) directory (`venv`) has a `bin/activate` which you can `.`.
- And, get this, your repository does not need to be cloned into the virtual environment directory.
- Trick from the Internet: "To automatically unpack a list containing a single item, append a trailing comma to the variable name on the left of the assignment operation."
- Tastypie allows only GET by default. `authorization = Authorization()` is required in the `Meta` class to allow insecure PATCHes.
- An instance's class [can be changed](http://stackoverflow.com/a/8062313/1558430) dynamically, restricted to user-defined classes only; it's unadvisable to do so regardless.
- `if` statements do NOT have an `else` equivalent of `for-else`, i.e. if [none of the branches are completely run](http://stackoverflow.com/q/21612910/1558430), because `if` statements don't have `break`s.
- `if` statements do NOT have any kind of `for-else`-type block that is run whenever any one or more conditions above are run.
- Python does not optimise tail calls.
- `def foo(a, (b, c), d)` destructures the second tuple. (Thanks @sboparen) This is _only_ a thing in python2.
- Django `TestCase` has a `@skip` decorator that, if added to any `def test_` methods, will disable the test. (`from django.utils.unittest.case import skip`)
- [Certain evidence](http://programmers.stackexchange.com/a/187471) points to recommend importing just a module (`import module` instead of `from module import func1, func2`) if a lot of things are used from that module. (Then again, how you can live with writing `module.func1` and `module.func2` all the time is beyond me.)
- `()` is a thing, and `(this,)` is a thing. A trailing comma is required only if the tuple contains exactly one item.
- `setattr(a_django_object, ...)` will silently update the object's `__dict__`. Doing the same `setattr` to an object will cause an `AttributeError` if the attribute was not defined in the class.
- `python -m webbrowser <url>` opens... that url in your browser.
- Python 3.0 ~ 3.2 don't have the `u'unicode string literal'` syntax, which would crash any python2 script that are otherwise the same as its python3 counterpart.
- Apparently [you can get `easy_install` from `python-setuptools`](http://www.mediawiki.org/wiki/Gerrit/git-review).
- Apparently [you can get `pip` from `easy_install`](http://www.mediawiki.org/wiki/Gerrit/git-review), too.
- Python 2.7+ is the only python2 version that comes with the set notation (`{1, 2, 3}`).
- [PyLint expects all global variables to be constants, and be named in ALL_UPPERCASE](http://docs.pylint.org/tutorial.html)
- Want a monad for absolutely no work? Get [PyMonad](https://pypi.python.org/pypi/PyMonad/)!
- [Marisa-trie](https://github.com/kmike/marisa-trie) consumes less memory than if you decide to build your own trie in python.
- `bytes(...)`: turn strings into sequences of anything from 0 to 255.
- [`simplejson` is subjectively better than `json`](http://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules) -- to use either, `import simplejson as json`.
- It is [an insanely stupid idea](http://stackoverflow.com/questions/6031584/python-importing-from-builtin-library-when-module-with-same-name-exists) to have a folder that has the same name as one of the built-in libraries.
- It wasn't possible to `import (many things with brackets)` [until python 2.7](http://legacy.python.org/dev/peps/pep-0328/).
- `range()` can actually be faster in some cases - eg. if iterating over the same sequence multiple times. `xrange()` has to reconstruct the integer object every time, but `range()` will have real integer objects. (It will always perform worse in terms of memory however, and there is no such thing as Python2's `range()` in Python3.)
- If you aren't being code reviewed or anything, you can subclass `namedtuple` like this:

```
class Foo(namedtuple('lol', 'a b c')): pass
```

- `namedtuple` accepts pretty much anything for its second argument. These all work.

```
namedtuple('a', ['b', 'c'])
namedtuple('a', 'b, c')
namedtuple('a', 'b c')
namedtuple('a', """
b
c
""")
```

- If a function is decorated with `contextlib.contextmanager`, then [it can be used as a `with` statement](https://docs.python.org/2/library/contextlib.html). The function must contain exactly one `yield`, where things that happen before the `yield` works like `__enter__`, and what happens after the `yield` is treated like `__exit__`.
- Eloborating on `contextmanager`, the `yield` must be _run_ only once; the statement cannot be in a loop.
- [`contextlib.suppress(BaseException)`](https://docs.python.org/3/library/contextlib.html#contextlib.suppress) is basically the `never_fail` decorator. And oops, it is only for Python 3.
- `random.seed()` is better than `random.seed(0)`, because [the parameter default is the system time](https://docs.python.org/2/library/random.html#random.seed).
- `hash(-2)` is the same as `hash(-1)`.
- Objects that have an overridden **eq** cannot be hashed, unless their **hash** are also defined.
- Python2 does [float multiplications](https://github.com/python/cpython/blob/10d5f4d9b6279945ba8062fd04c0314e5ead0a53/Objects/intobject.c#L533) internally to compute results of integer multiplications, presumably to find out of two numbers multiplying each other will cause an overflow.
- It is possible to [`__import__('python-module-with-dashes-in-the-filename'`](http://stackoverflow.com/questions/761519/is-it-ok-to-use-dashes-in-python-files-when-trying-to-import-them), but if you create a file such as this, you deserve to be shot.
- `os.getenv('HOME')` works, only because `$HOME` is populated by the shell.
- [You can compare tuples](http://stackoverflow.com/a/5292332/1558430)! `(1,2)` is less than `(3, 4)`.
- You can assign to spliced arrays: `arr[:4] = [9,9]` replaces the first 4 items of the array with `[9,9]`.
- `round()` doesn't work on `Decimal`s. To round a `Decimal` to certain digits, do: `Decimal(123.456789).quantize(Decimal("0.001")) # 3 decimal points`
- `Decimal.quantize` is called that because it also makes up more decimal points if you ask it to: `Decimal(1234.56789).quantize(Decimal("0.000000000000000001")) # Decimal('1234.567890000000033979')`
- You _can_ `def foo(bar=NamedTupleAsDefaultValue())`, but would you...?
- `arrow.replace()` accepts singluar nouns like `hour` that replaces the component, or plural forms like `hours` that shifts the value relatively, instead.
- [Guido](https://mail.python.org/pipermail/python-dev/2010-April/099459.html) doesn't like `merged_dict = dict(some_dict, **another_dict)`, and nor do you. (it only handles string keys)
- In Python3, arguments can be [forced named](http://stackoverflow.com/a/14298976/1558430): with `def foo(a, * must_use_kwargs_for_this_arg)`.
- One-liner `if` clauses are executed before the assignment, so `b = a.foo if a else 2` will not raise `AttributeError` even if `a = None`.
- ["Never (create, change, or delete models) directly"](http://www.dabapps.com/blog/django-models-and-encapsulation/) - Tom Christie
- `bool` is a subclass of `int`, and cannot be subclassed further.
- "Either or" is `bool(a) != bool(b)`, or just `operator.xor`. This is different from `nand`, which is false when both are false, and not `nor`, which is true when both are true.
- As much as tuples are immutable, its contents are:

```
>>> a = ([], [])
>>> a[0].append(1)
>>> a
([1], [])
```

- `logging.debug("{}".format(123))` builds strings unnecessarily when logging level is set to above debug. To combat this, use `logging.debug(u"%s", 123)` instead, where the arguments must be positional. For internal reference, the Gerrit ID is 626.
- Strings can also be formatted traditionally with a keywords: `'Today is %(month)s %(day)s.') % {'month': m, 'day': d}`
- [`python -W all`](http://stackoverflow.com/a/18996013/1558430) prints all `PendingDeprecationWarning`s, and is the preferred way to run python locally.
- [`j` is the only notation for complex numbers.](http://stackoverflow.com/a/8370696/1558430)

```python
>>> abs(1+12i)
  File "<stdin>", line 1
    abs(1+12i)
            ^
SyntaxError: invalid syntax
>>> abs(1+12j)
12.041594578792296
```

- The `abs()` of a complex number is the dot product of its real-imaginary plane. If this is not intended, use `math.fabs()` instead, which raises on imaginary numbers.
- Unit test `self.assert*`s take a last parameter that is the failure message: `self.assertIn(0, [1,2,3], "0 not found in list")`
- `(str).casefold()` is meant to normalise all variants of the same string, such as `['False', 'false', 'FALSE']` into something you can put into a switch-case block. Then again, there isn't switch-case in Python, only dict keys.
- The [try-finally block](https://wiki.python.org/moin/HandlingExceptions) has no `except`, so it runs the finally block (which typically rolls back something), then raises the exception.
- Although there are no docstring type-hinting standards, [this one by PyCharm](https://www.jetbrains.com/pycharm/help/type-hinting-in-pycharm.html) will do: `:param parameter_name: x.y.ParameterClass | None`
- [`sum()` takes a second parameter](https://docs.python.org/2/library/functions.html#sum), `start`. It really means `sum() + start`.
- `history` is always a variable in ipython.
- Booleans are inherited from `int`, so you can add them together.
- "Tim Peters also snuck some subtle jokes into the Zen itself (notice the dashes on the TOOWTDI line do it two different ways?"
- Multiple assignments (e.g. `a = b = []`) assigns the same reference to each variable, even if the value is primitive (e.g. `5`).
- [When called with three arguments, type acts like a constructor, so you can create new types in an inline fashion.](http://ivansmirnov.io/python-metaclasses/)
- There's [a whole package](https://pypi.python.org/pypi/lockfile) for the `process.pid` thing.
- Sending gzip requests through the `requests` library is [completely manual](http://stackoverflow.com/questions/28656068/compressing-request-body-with-python-requests). You really have to construct a gzip stream and modify the headers.
- As an asider, [`Transfer-Encoding: gzip` is a better header than `Content-Encoding: gzip`](http://stackapps.com/questions/916/why-content-encoding-gzip-rather-than-transfer-encoding-gzip) because the latter does not imply the final content type of `.gz`.
- In Python 3, unbound methods don't exist. There is `unbound_method()` in six that achieves a similar goal.
- [django-rest-swagger](https://github.com/marcgibbons/django-rest-swagger/) documents the API.
- `max(None, 0)` is 0. `max(0, None)` is also 0. `min(None, 0)` is `None`. Therefore, `None < 0`. In fact, `None < float('-inf')`.
- `UnicodeEncodeError` and `UnicodeDecodeError` in a nutshell:

```
>>> "{}".format('Café')                  # str to str
'Caf\xc3\xa9'                            # ok
>>> u"{}".format(u'Café')                # utf8 to utf8
u'Caf\xe9'                               # ok
>>> u"{}".format('Café'.decode('utf8'))  # utf8 to utf8
u'Caf\xe9'                               # ok
>>> "{}".format(u'Café')                 # utf8 to str
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe9' in position 3: ordinal not in range(128)
>>> u"{}".format('Café')                 # str to utf8
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)
```

- [**There's no formal guarantee about the stability of sets (or dicts, for that matter.)**](http://stackoverflow.com/a/3812600) However, in the CPython implementation, as long as nothing changes the set, the items will be produced in the same order.
- [Assigning attributes to a function doesn't raise `AttributeError`s](https://mail.python.org/pipermail/python-dev/2000-April/003364.html). PEP 232 [tries to justify it](https://www.python.org/dev/peps/pep-0232/)--the gist being, "it doesn't hurt."
- `isinstance()` accepts a tuple worth of types.
- Installing `python-examples` apparently [gives access to `reindent.py`](http://stackoverflow.com/a/1024489/1558430), which obviously reindents python scripts.
- Splicing a `range` (which is `xrange`) in python3 gives you another `range`. The equivalent `xrange` cannot be spliced in python2.
- By overriding the behaviour of `__lt__`, `__gt__`, `__eq__`, etc., things that often do comparisons (and therefore return bools) now return SQL "Expression" objects, like so:

```
>>> str(db.Column('a') > db.Column('b'))
'a > b'  # look ma, not a bool
```

- [An `Enum`'s class attributes have itself as its own class](https://docs.python.org/3/library/enum.html). `isinstance(Color.green, Color) is True`.
- But with every `Enum` having every attribute in its own class, they don't have access to other attributes: `Color.red.blue # AttributeError`
- Depending on version, [Python2 and 3 raise different errors](http://stackoverflow.com/a/23703899/1558430) when an `object()` is asked if it is equal to another `object()`.
- Exploiting the tuple syntax can make multidimentional "arrays" very easy to work with:

```
>>> a = {(1,2): 4}  # This can be a subclass of `dict` with list indexing
>>> a[1,2]
4
```

- If you use `python2` to run a script with a `#!/... python3` shebang in it, it runs with python2, man. Duh.
- `UnicodeError` is the superclass of `UnicodeDecodeError`, `UnicodeEncodeError`, and the lesser-known `UnicodeTranslateError`.
- The `exceptions` library contains all built-in exceptions. All files have an implicit `from exceptions import *`.
- `mock.patch` [needs](http://alexmarandon.com/articles/python_mock_gotchas/) a direct reference to the function where it is called. To patch `from a import b` running in module `c`, patch `c.b`, not `a.b`.
- Whatever you think `-0.0` is, it exists... and it is equal to `0.0`.
- [`pwd.getpwall()`](https://docs.python.org/2.7/library/pwd.html), misleadingly, does not return a list of all passwords. They are usually `*` or `x`, due to the use of a shadow password system, explained in the link.
- The implementation of [`keyword.iskeyword()`](https://hg.python.org/cpython/file/2.7/Lib/keyword.py#l17) is a real misfortune.
- Python2 has [`WeakReference`](https://docs.python.org/2/library/weakref.html)s too!
- `basestring` is just `str` in python3.
- Python3's type hinting [enforces nothing](https://www.python.org/dev/peps/pep-0484/#the-meaning-of-annotations). For the same reason, they called it annotations. For really enforcing these rules, consider [mypy](http://mypy.readthedocs.org/en/latest/duck_type_compatibility.html).
- `set().update(...)` can handle lists as well, not just sets.
- Splicing indices don't have to be integers... at least not now. `[1,2,3][:None]` returns a copy of `[1,2,3]`, just as `[1,2,3][:]` would.
- Python's `foo = set()` has an `update(bar)`, too. It just adds what's in `bar` into `foo`.
- Comparing any integer outside [-5, 256] with `is` is [incorrect](http://stackoverflow.com/a/306353/1558430): "The current implementation keeps an array of integer objects for all integers between -5 and 256, when you create an int in that range you actually just get back a reference to the existing object."
- However, `500 is 500` is always true. `a = 500; b = 500; a is b` is usually false.
- Returning inside a `try` _or_ an `except` block will still run the `finally` block, if one exists.

```
>>> def foo():
    try:
        print 'foo'
        raise Exception(4)
        return 5
    except:
        print 'baz'
        return 6
    finally:
        print 'bar'

>>> print foo()
foo
baz
bar
6
```

- As far as SQLAlchemy is concerned, [there is no difference between `== true()` and `.is_(True)`](https://groups.google.com/forum/#!msg/sqlalchemy/T2bKLjzO6KA/1EwA6spA9QsJ). Howveer, pep8 and co. will complain about the former, so you should use the latter.
- `__all__` only concerns `import *` statements. It carries no weight anywhere else.
- `{}` is [definitely](https://www.reddit.com/r/learnpython/comments/42ymhl/returning_is_faster_than_returning_dict_even/) faster than `dict()`. This is also why you should always use literals where possible.
- Django's [`TransactionTestCase`](https://docs.djangoproject.com/en/1.9/topics/testing/tools/#django.test.TransactionTestCase) is different from its `TestCase` in that while `TestCase` uses a transaction to roll back the database after each test, and--get this--`TransactionTestCase` does _not_ use transactions. It just truncates all the tables.
- `list` is a type.
- You can test if a function was called with anything using [`mock.assert_called_once_with('foo', bar=ANY)`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.ANY)
- [Welcome to unicode](https://eev.ee/blog/2015/09/12/dark-corners-of-unicode/), where `e < f < é`:

```
>>> words = ['cafeteria', 'caffeine', 'café']
>>> words.sort()
>>> words
['cafeteria', 'caffeine', 'café']
```

- There is no `.none()` in SQLAlchemy; only [`.filter(sqlalchemy.sql.false())`](http://stackoverflow.com/questions/10345327/sqlalchemy-create-an-intentionally-empty-query). The latter still incurs one query.
- `ModelA.query.join(ModelB)` does a JOIN on whichever `db.relationship(ModelB)` ModelA defines. Don't ask what happens if there are multiple relationships right now.
- The `entry_points` thing in setup.py installs scripts inside your `(venv path)/bin/` directory.
- SQLAlchemy's equivalent of `.values_list('id', flat=True)` is `.options(load_only('id'))`. I have not tested this.
- [Putting code in the `try-else` block](http://stackoverflow.com/a/855764/1558430) is meant to _avoid_ catching the same exception in the `else` block, while still running a `finally` if the `else` block fails; basically, syntactic sugar for two try blocks.
- `sys.modules` contains an import, e.g. `datetime`, only after you import it.
- You can `''.join([u'a', u'\u3000', 'bunch', 'of', u'unicode', 'strings'])`, but not `'{}'.format(u'a unicode \u3000 string')`, because reasons. (python2)
- `dict()` unzips iterables of iterables. `dict( (('a', 'b'), ('c', 'd')) ) == {'a': 'b', 'c': 'd'}` (and if there are key conflicts, keys with a higher list index prevails)
- Providing the same kwargs to a `partial()`ed function overrides the default:

```
>>> import functools
>>> def foo(**kwargs):
...     print kwargs
...
>>> foo2 = functools.partial(foo, a=2)
>>> foo2()
{'a': 2}
>>> foo2(a=4)
{'a': 4}
```

- Regex flags can be [directly put inside the match string](http://stackoverflow.com/a/38250089/1558430): like `re.findall("/foo/s", "foo")`.
- [PEP 318](https://www.python.org/dev/peps/pep-0318/) rejected the `def foo @decorator (bar, baz):` syntax on the basis that it no longer allows `def foo(` to be grepped. THANK YOU.
- [`PuDB`](https://pypi.python.org/pypi/pudb) exists as a concept; it is a graphical pdb.
- `os.tmpnam()` makes a temp path up for you, but the thing is vulnerable for some reason related to symlinks, so now you need to use `os.tmpfile()`, which opens the file for you as well.
- `textwrap.dedent` is a standard library function.
- When generating reports/exports of any sort, remember to [also generate a metadata file](https://www.airpair.com/python/posts) that records how the data was generated at the time, so you can check the validity of the data later on.
- pip has the `ncu` equivalent built in: `pip list -o`
- Values in `Enum` cannot be compared with those in `IntEnum`, even when both values are exactly integer `1`s.
- [PEP 440](https://www.python.org/dev/peps/pep-0440/), which rings a bell because of CHEM 440, describes python's SemVer. The `rc` in `X.Y.ZrcN` is Release Candidate, not "RideCo", the vapourware company.
- Of all the spacing requirements in python, the space between the `n` and `[` in `for i in[1,2,3,4] :` is not necessary. Nor does the redundant space between `]` and `:` matter. Your life is a lie.
- numpy's `array` is not an instance of `list`.
- numpy's odd way of [telling if an array contains only 1 or 0](http://stackoverflow.com/a/40596003/1558430) is `((arr == 0) | (arr == 1)).all()`, or `~((arr != 0) & (arr != 1)).any()`.
- ["Celery"](http://stackoverflow.com/questions/13440875/pros-and-cons-to-use-celery-vs-rq) is python's way of saying "I will make a small mistake of choosing Celery now, to avoid a bigger mistake later on".
- You can specify [requirements for each platform and python version](http://stackoverflow.com/questions/29222269/is-there-a-way-to-have-a-conditional-requirements-txt-file-for-my-python-applica/35614580#35614580) in requirements, like this: `atomac==1.1.0; sys_platform == 'darwin'`
- Backticking a variable `x` is equivalent to `repr(x)`, but since it is only for python2, it is better if you never learned it.
- Doing [`from builtins import dict`](http://python-future.org/compatible_idioms.html#dictionaries) (provided by the [future](http://askubuntu.com/a/728339) package) in a file automatically makes any `dict()`'s `.values()` an iterable, saving memory in python2 and 3 without `.itervalues()`. This does not apply to dict literals.
- `**kwargs` do not need to contain variable name-only keys. You can call `foo(**{' ': None})` if you want.
- `nosetests` (Python?) accepts a `-a foo` parameter, that only runs tests decorated with `@attr('foo')`.
- `ast.literal_eval('123 # comments')` actually returns 123. It still throws ValueError for things like function calls, however.
- [Simon Pirschel](https://aboutsimon.com/), creator of [udatetime](https://github.com/freach/udatetime), says that we should use udatetime because [it is faster](https://aboutsimon.com/blog/2016/08/04/datetime-vs-Arrow-vs-Pendulum-vs-Delorean-vs-udatetime.html).
- [`.format()` can do many things.](https://pyformat.info/) Useful examples include `{:d}` (as an integer), `{:>10}` (leftpad a string), `{!r}` (repr an object), and `{foo.bar}` (getattr).
- [`numpy.split(array, 3)` splits into 3 arrays. `numpy.array_split(array, 3)` splits into arrays of length 3.](http://stackoverflow.com/questions/9922395/python-numpy-split-array-into-unequal-subarrays)
- [Click](https://pypi.python.org/pypi/click) is a far more intuitive version of optparse/argparse/whatever.
- If you say (in python2 anyway) `[b for b in c]`, but `c` happens to have no elements, then `b` is never defined.
- The `cPickle` module in PyPy is written in pure python.
- `a_string.replace('foo', '')` can obviously still contain `foo`, if `'ffoooo'.replace('foo', '')`
- _Thus spake the Lord: Thou shalt indent with four spaces. No more, no less. Four shall be the number of spaces thou shalt indent, and the number of thy indenting shall be four. Eight shalt thou not indent, nor either indent thou two, excepting that thou then proceed to four. Tabs are right out._ -- Georg Brandl
- The imports you write assume you run these scripts from the [top level of the project](http://stackoverflow.com/questions/43498467/python-importerror-of-my-own-module). Imports don't magically work simply because there is an `__init__.py` in the directory.
- [The backspace character](https://en.wikipedia.org/wiki/Backspace) (`chr(8)`) is a caret shifting mechanism. One backspace moves the caret one character to the left, and the next character replaces the character that is already in that position. For example, `print 'A' + chr(8) + 'B'` prints just `B` (because the B replaced the A), and `'A' + chr(8)` prints just `A` (because nothing replaced the A yet). `print 'A' + 'B' + chr(8) + chr(8) + 'C'` prints `CB`, because the caret is moved two characters back, and the C replaces the A.
- The `a, *_, b = [...]` unpacking thing raises a ValueError if the list is fewer than two elements long. `a, b = foo[0], foo[-1]` does not do that.
- [`type('', (), {})()` will create an object that can have arbitrary attributes.](http://stackoverflow.com/a/24448351/1558430)
  1, Up until python 3.7, [it was impossible](https://docs.python.org/3.7/whatsnew/3.7.html) to have a function with more than 255 parameters, but a function name of more than 255 parameters is ok (you tested 100,000 characters).
- A statement is a complete line of code that performs some action, while an expression is any section of the code that evaluates to a value. [Expressions can be combined “horizontally” into larger expressions using operators, while statements can only be combined “vertically” by writing one after another, or with block constructs.](https://www.quora.com/Whats-the-difference-between-a-statement-and-an-expression-in-Python)
- [`sets.Set`](http://stackoverflow.com/a/32108276/1558430) is deprecated (removed in 3, even); `set` is not.
- `json.dumps(float('inf'))` should fail because `Infinity` is not valid JSON. Yet, using `simplejson`, it succeeds. So if your python code generates any JSON that contains an `Infinity` in it, your JS will get rekt.
- Too many items in your celery 3 queue? [`celery worker -Q queuename --purge`](https://stackoverflow.com/a/33531638/1558430)
- [Avoiding attribute access in loops](https://wiki.python.org/moin/PythonSpeed/PerformanceTips#Loops) can have a measurable improvement in loop speed, and not only when the attributes are magic.
- [`python -m`](https://docs.python.org/2/using/cmdline.html) runs that module as if the module's contents were `__main__`. There is [little](https://stackoverflow.com/a/22241810/1558430) difference between `python that.py` and `python -m 'that'`.
- [You cannot monkey patch python's `list`](https://stackoverflow.com/a/38257902/1558430). Well, [you can](https://stackoverflow.com/a/4025310/1558430), but literals won't use your subclass, and outside of a PoC, that won't be a smart thing to do.
- The `call` object is supposed to be used by [unpacking](https://stackoverflow.com/a/39669722/1558430): `args, kwargs = mock_func.call_args`
- `simplejson.loads()` has a `for_json=False` argument that can be turned True if you want any object with a `for_json(self)` method to return their own representation instead.
- You can have `exit(0)` anywhere, in globals, in a function or in a list comprehension, and the script will exit with 0. In a generator, `exit(0)` takes effect whenever that generator outputs its first item.
- Python3 has the `raise from` syntax, where given an exception (e.g. `except ValueError as e`), you can [re-raise a different exception](https://stackoverflow.com/questions/24752395/python-raise-from-usage) while noting what the original cause was, i.e. `raise TypeError(...) from e`. Default is to show the previous errors anyway. To supress it, `raise ... from None` (no context).
- [Sometimes `%.0f` rounds up. Sometimes `%.0f` rounds down.](https://stackoverflow.com/a/24121342/1558430) Try 10.5 (becomes 10) and 1.5 (becomes 2).
- The `set` literal happily accepts repeated items, like `{1,1,1}`. It just comes out as `{1}`.
- Given `[1,2,3,4,5,6,7]`, `bisect.bisect_left(that array, 4)` will give you the index of 4, to the left of `4`, and `bisect.bisect_right(that array, 4)` will give you the index of 5, to the right of `4`.
- Destructured additions cannot be done. That is, `(a, b) += 1` ("add 1 to each of a and b") and `(a, b) += (3, 4)` ("add 3 to a and add 4 to b") will not work. You can still do `a, b = a + 3, b + 4`, though.
- `inspect.getfile(obj)` works only on a class, so `inspect.getfile(obj.__class__)`.
- _Almost_ everything in python has a `__module__` attribute that tells you which module it came from. Primitives don't have it. Literals don't have it (because only primitives have literals). If you make a function or class in a REPL, then the module is `__main__`. The module for `type` is `__builtin__`, as is the case for other builtins, like `min` and even `function`. The module for built-in exceptions are `exceptions`, though, because that is where they are located. And, of course, if you attempt to inspect the builtin stuff, like `inspect.getfile(type(None))`, then you get a big fat `TypeError: <module '__builtin__' (built-in)> is a built-in class`.
- Assuming because python wants only one (obvious) way to do something, John Roth [once](https://www.python.org/dev/peps/pep-0327/#why-floating-point) recommanded removing the `/` operator altogether, presumably replaced with the multiplying inverse. The community didn't like that.
- [Gunicorn is a WSGI server.](http://docs.gunicorn.org/en/stable/deploy.html) You will still need Nginx.
- If you [don't pickle anything or parse any XML](http://igordavydenko.com/talks/by-pycon-2017/#slide-19), python 3.6 isn't that slow compared to python 2.7.
- You can multiply `timedelta` by a scalar.
- You can conditionally define methods in a class by wrapping it in an if statement.
- Lambda bodies are executed every run, even if they are one line, like `a = lambda: datetime.now()` would always give you a new time.
- [That one time the creator of Rest Framework said, hey, you should make your project compatible with the Rest Framework](https://github.com/clarkduvall/serpy/issues/7)
- SQLAlchemy lets you [choose between different kinds of lazy loading](http://docs.sqlalchemy.org/en/latest/orm/loading_relationships.html) for foreign key relations.
- [`__new__(cls, ...)`](https://docs.python.org/2/reference/datamodel.html#object.__new__) is a special method that takes the class as the first argument, but is not a `@staticmethod` or `@classmethod` ("special-cased so you need not declare it as such").
- Even in python2.7, if you prefix any class attribute with `__` (i.e. `self.__foo = 1`), [trying to read that attribute from anything except `self` will raise an `AttributeError`.](https://stackoverflow.com/a/38864561/1558430) Instead, [the interpreter does a little obfuscation](https://stackoverflow.com/a/4555970/1558430) such that the attribute is under a different key, usually (but not if subclassed) in the form of `_ClassName__foo`. Use `dir(the instance)` to view.
- Keras specifically implements neural networks. It does not implement other kinds of machine learning.
- It is completely possible for `pip` and `pip3` to install something into `.local/pip` and have absolutely no effect, other than to make it impossible to install the package as root. First `pip uninstall the-thing`, and then reinstall it with `sudo`.
- Just use [`sys.version_info >= (3, 0)`](http://sweetme.at/2013/10/21/how-to-detect-python-2-vs-3-in-your-python-script/) to check if you are running python3, but some `basestring NameError` business.
- Unlike JS, python does not have "dict unpacking", i.e. `{foo, bar} = {'foo': 1, 'bar': 2}`. You _can_ write `foo, bar = {'foo': 1, 'bar': 2}`, but the result is random from an unsorted dict.
- [Running synchronous tasks in celery is not recommended](http://docs.celeryproject.org/en/latest/userguide/tasks.html#task-synchronous-subtasks) (i.e. `.get()` in a `@task`)
- Alembic uses the `env.py` that you generated with `init` to detect models. This file must import all the models that you want to manage.
- Django ORM is considered "active record" (i.e. each row is an object), whereas SQLAlchemy is a "data mapper" (i.e. objects and rows don't necessarily map one to one). This forces many things to be manually configured in SQLAlchemy, for better or for worse.
- In a declaration like [`parent = relationship("Parent", back_populates="child")`](http://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#one-to-one), there needs to be a matching class `Parent` and an attribute called `child`. ["When the `backref` keyword is used on a single relationship, it’s exactly the same as if the above two relationships were created individually using `back_populates` on each."](http://docs.sqlalchemy.org/en/latest/orm/backref.html)
- In a SQLAlchemy column definition, [there is no difference between an `Integer` and an `Integer()` instance.](http://docs.sqlalchemy.org/en/latest/core/type_basics.html)
- Every return value of `float(a: float)` is just `a`, the same float object.
- [You cannot `partial` a class'es method from inside the class.](https://stackoverflow.com/questions/16626789/functools-partial-on-class-method) At least you cannot do that [without a stub](https://gist.github.com/carymrobbins/8940382), or until python 3.4's `partialmethod()` is introduced.
- [Number range filters like `df[10 < df.column < 20]` does not work in pandas.](https://stackoverflow.com/questions/31617845/how-to-select-rows-in-a-dataframe-between-two-values-in-python-pandas#31617974) You _need_ to do a double condition like `df[(10 < df.column) & (df.column < 20)]`.
- To pick multiple columns off a dataframe, you can't do `df['a', 'b', 'c']` because that's intuitive and pythonic. You [need](https://stackoverflow.com/a/48584948/1558430) to do `df[['a', 'b', 'c']]` instead...
- Importing `matplotlib.pyplot` as `plt` is [a standard convention](https://pandas.pydata.org/pandas-docs/stable/visualization.html).
- [Celery beat is a process that just puts tasks into queues in regular intervals](http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html). You still need a separate worker to listen to that queue.
- Alembic [`stamp`](http://alembic.zzzcomputing.com/en/latest/api/commands.html#alembic.command.stamp) is the SQLAlchemy equivalent of faking a migration. Example: `stamp fc34a1fc6e7d`. You might need to get dirty anyway, as there is no unstamping.
- [`.get(something)` is just `.filter(primary key == something).first()`](https://stackoverflow.com/questions/34299704/when-to-use-sqlalchemy-get-vs-filterfoo-id-primary-key-id-first).
- [On celery workers](https://www.distributedpython.com/2018/10/26/celery-execution-pool/): "pre-fork for CPU instensive, eventlet/gevent for IO bound work ya prefork would block the workers while making long HTTP requests, preventing other work from being done. Async lets IO things happen more concurrently" - a guy who types "ya" instead of "yeah"
- Alembic is worse than Django migrations in [various ways](http://alembic.zzzcomputing.com/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect). First, it does not auto detect table OR column renames. Second, it does not detect changes in contraints. Third, I'll make something up later.
- [`mailbox`](https://docs.python.org/2/library/mailbox.html) is a standard library. It manipulates mailbox files (like `.mbox`).
- Comparing with `None` using `<` or `>` in python3 raises a `TypeError`. `None` was previously just "less than everything".
- You give Arrow an absurd date, like `arrow.get(year=0, month=0, day=0)`, and it will give you the current time. Sure. But you do something completely reasonable, like [`arrow.get(year=1918, month=11, day=11)`](https://en.wikipedia.org/wiki/Armistice_of_11_November_1918), it will still give you the current time. "Yeah but that's before the epoch," you say? **Nope**. You're just calling it wrong. `arrow.get()` doesn't take year/month/day as arguments.
- Requests' [sessions](https://laike9m.com/blog/requests-secret-pool_connections-and-pool_maxsize,89/) are not just for making code cleaner; it also allows the library to share `urllib3` connection pools, so the code makes fewer unnecessary connections to the target server.
- For simple queries, if you don't like `SQLAlchemyModel.query.filter(SQLAlchemyModel.field == thing)`, [maybe](https://stackoverflow.com/questions/2128505/whats-the-difference-between-filter-and-filter-by-in-sqlalchemy) you can use `filter_by` instead: `SQLAlchemyModel.query.filter_by(field=thing)`.
- You can implement [custom states in celery](http://docs.celeryproject.org/en/latest/reference/celery.states.html), if for some reason you want to do that, by subclassing `celery.states.state`, which is a subclass of `str`.
- [Celery's revoked tasks will stay in memory until automatically discarded.](https://stackoverflow.com/questions/46019528/remove-a-revoked-celery-task) There is no manual option. Apart from shutting the broker down and purging the queue there (`sudo rabbitmqctl purge_queue 'queue_name'`), there is no good way to purge revoked tasks from celery.
- `//` is the floor division operator, which for `3.0 // 6` gives you `0.0` in either version, and still returns a float if either number is not an integer. It doesn't turn every result into integers.
- Since tuples are immutable, defaulting a parameter to a tuple is uncommon, but fine.
- A dict's ~~`.keys()`, `.values()`, and `.items()`~~ `.viewkeys()`, `.viewvalues()`, and `.viewitems()` have an official name called [dictionary views](https://docs.python.org/3/glossary.html). If the dict changes, so do the views.
- [Python3's `super()` need not specify the class and instance.](https://stackoverflow.com/a/19609168/1558430) In the event that the class has multiple parents, and you do something like `super().foo()`, it decides for you whichever class has the method `foo` first, which is the same behaviour as if you specify `super(this class, this instance).foo()`.
- You can't [name a file with a period and import it](https://stackoverflow.com/questions/1828127/how-to-reference-python-package-when-filename-contains-a-period#1828249) normally.
- A (function or compatible object)'s `__dict__` (if you do stupid things like that) becomes populated with `{'foo': 'bar'}` if you choose to assign, say, [`a_function.foo = 'bar'`](http://www.diveintopython3.net/special-method-names.html#esoterica).
- [You can override `__instancecheck__(i)` and `__subclasscheck__(c)`](https://www.python.org/dev/peps/pep-3119/#overloading-isinstance-and-issubclass) for a free pink slip.
- `a << b` is ["`a` shifted left by `b` zeros"](https://wiki.python.org/moin/BitwiseOperators).
- `re.match` will look for your pattern at the beginning of your string. `re.search` looks for your pattern anywhere in the string.
- `if not ():` is a valid statement because `()` is a falsy tuple.
- Python3 [`Exception`s do not have `.message`](https://github.com/charlesthk/python-mailchimp/issues/61) anymore.
- The [`range()` is not a generator](https://stackoverflow.com/a/13092317/1558430) because you can't call `next()` on it. And you can't call `next()` on it because you want some nice properties like `1 in range(5)`, which generators cannot offer, and index access `range(5)[1]`, which generators also cannot offer.
- Perhaps contradictory to the previous point, [all generators are iterators](https://stackoverflow.com/a/2776865/1558430) so you should be able to iterate through any generator.
- If you give a function a `__call__`, it does nothing with it.
- Django's `django.utils.six` is [said](https://stackoverflow.com/a/32578107/1558430) to be a bit different from the real `six`, under the section [`### Additional customizations for Django ###`](https://github.com/django/django/blob/d6eaf7c0183cd04b78f2a55e1d60bb7e59598310/django/utils/six.py#L869).
- The built-in `cmp()` was [left in python 3.0.0 by mistake](http://python3porting.com/differences.html#comparisons).
- Function defaults are just in `func.__defaults__`.
- ["`str.encode()` always returns `bytes`, and `bytes.decode()` always returns `str`."](https://docs.djangoproject.com/en/1.10/topics/python3/)
- jupyter notebooks are a thing because people want to inline markdown with code. I am guessing you can do a lot of creative things from there.
- [`ctypes`](https://docs.python.org/2/library/ctypes.html) does not just offer C types; it also allows external library functions to be called.
- `2` is an available PyPI package name because you can't `import 2`. Still, [`1`](https://pypi.org/project/1/) is taken for no reason.
- [`EnvironmentError`, `IOError`, and `WindowsError`](https://docs.python.org/3/library/exceptions.html#EnvironmentError) are all aliases for `OSError` in python3.
- The only free version of python supported on Google App Engine is 2.7.
- [`isoweekday`](https://docs.python.org/2/library/datetime.html#datetime.date.isoweekday) is 1-indexed, with 7 being Sunday, because, I don't know.
- `time.time` is a function. `datetime.time` is a data type.
- [PEP 3109](https://www.python.org/dev/peps/pep-3109/) explicitly says that "[the `EXCEPTION`] in `raise EXCEPTION` ... may be an exception class or an instance of an exception class".
- Unlike what [this page](https://medium.com/@wpcarro/tuples-in-javascript-57ede9b1c9d2) suggests, there are no `namedtuple` literals like `color = (red=255, green=0, blue=0)`. Not in 2, not in 3.
- VS code (when used for python) lacks "find usages" and "import this thing", but [people like it](https://www.slant.co/versus/1240/5982/~pycharm_vs_visual-studio-code).
- `async` can go with the `with` statement as well (i.e. `async with`). See [here](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python) for other concurrency-related examples.
- There is a handy [`contextlib.closing`](https://docs.python.org/2/library/contextlib.html#contextlib.closing)`(some_connection()) as connection` thing that you can use to make sure a thing closes when the block exits.
- A return statement in the `finally` block will return before a return statement in your `try` block returns.
- PEP 515 describes underscores in numerals. `1_000_000` is really a million.
- PEP 526 introduces the first syntax that is _not_ an expression. Variable type annotation `variable: int`, bearing in mind that doesn't assign anything to the variable, is not an expression.
- Guido and friend actually tried to distance their project from actual snakes, because the entire thing was supposed to be a Monty Python joke instead of a zoo, but finally [gave up when O'Reilly printed a snake in front of their first python book](https://www.youtube.com/watch?v=gJ4duC-V6Xw).
- A `finally` clause could not contain a `continue` [until python3.8](https://docs.python.org/3.8/whatsnew/3.8.html#other-language-changes).
- To get your query string from an SQLAlchemy expression, do [`str(the_expression.statement.compile())`](https://stackoverflow.com/a/25563491/1558430).
- There is no non-literal one-liner (i.e. `list(1, 2, 3)`) for making a list. But there is for a dict: `dict(a=1, b=2)`.
- Through the act `baz = foo + bar`, where all of these are `list`s, will create an entirely new list for `baz`. If `foo` were `[1,2,3]` and you modify `baz[0] = 'haha'`, `foo` will remain `[1,2,3]`.
- `license()` (with an S) is a built-in function. It shows python's story and history in addition to the actual licence. Making a function called `license()` is usually harmless, except if you use pylint: `Redefining built-in 'license'`
- [`ngxtop`](https://github.com/lebinh/ngxtop) is a pip package.
- Comparing tuples with tuples, like `(1, 0) < (3, 0)` works how you think it would, but comparing tuples with lists that _look about the same_ will not: `(1, 0) < [3, 0]` is false because the two types cannot be compared together.
- You can `os.path.join` a `PosixPath`, you can `Path('/') / 'home' / 'bob'`, but you can't `Path('/') + 'home/bob'`, because that'd be "unintuitive".
- Re machine learning: [you should probably just go with tensorflow](https://deepsense.ai/keras-or-pytorch/), if it installs.
- The exception message for doing `max(0, None)` is different for python 3.5 (`TypeError: unorderable types: NoneType() > int()`) and 3.6 (`TypeError: '>' not supported between instances of 'NoneType' and 'int'`).
- Saying `raise`, without an exception to reraise in the context, will get you a `RuntimeError`.
- A python3 class method annotation that needs to specify itself (e.g. a `Time` class whose method returns a `Time`) needs to be [annotated with a string](https://stackoverflow.com/a/33533514/1558430) (e.g. `'Time'`). This is because of the evaluation order... `Time` is not defined until the class is entirely parsed (or something). This is resolved in Python 3.7 (with a future import) and 4.0 (just works).
- [Function annotations](https://www.bernat.tech/the-state-of-type-hints-in-python/) (PEP-3107) is Python 3.0+, and does not specify what the annotations needs to do. Type hints (PEP-483, PEP-484) define [how these annotations can be used for type checking](https://www.caktusgroup.com/blog/2017/02/22/python-type-annotations/). Variable annotations (PEP-526, e.g. `foo: int = 1`) is Python 3.6+.
- While `Dict` is preferred over `dict` when writing type hints, [`typing.Boolean` is not a thing](https://docs.python.org/3/library/typing.html), as are [other "primitives"](https://mypy.readthedocs.io/en/latest/cheat_sheet_py3.html) such as `int`.
- [`typing.Tuple[float, float]`](https://stackoverflow.com/questions/39458193/using-list-tuple-etc-from-typing-vs-directly-referring-type-as-list-tuple-etc) means a tuple _exactly_ 2 elements long, both of which being floats.
- [`.pyi` files](https://www.python.org/dev/peps/pep-0484/) are syntactically valid python files that are type _stubs_. By having a different extension, you cannot run pyi files directly (or import them?), and you can put the type stubs right beside your actuaal python file.
- `__slots__` might lower memory usage by 40% to 50%.
- GVR had already mentioned that [PEPs are not laws](https://github.com/PyCQA/pycodestyle/issues/466). PEPs are not intended to be laws. PEPs are "merely intended to guide humans, not to require them to follow it every time."
- `()` does not equal `(,)` because the latter is a syntax error.
- Raymond's twitter pro tip: [Generally, lists are for looping; tuples for structs. Lists are homogeneous; tuples heterogeneous. Lists for variable length.](https://stackoverflow.com/a/16941245/1558430)
- If you want your coworker to kill you, use the ["Additional Unpacking Generalizations"](https://www.python.org/dev/peps/pep-0448/) (PEP 448) to write your tuple: `*(x for x in range(10)),`. In the same PEP: you can now unpack multiple things, multiple times, in the same function call. You can also first unpack some `*args`, and then add more after it to overwrite the stuff in `args`. _Guido_ accepted this PEP.
- A `/` inside documentation like `sin(x, /)` means "all arguments are positional-only", and to be fair, [not that many people like it, or know what it is](https://twitter.com/raymondh/status/1103047432164696064).
- Child test classes that are tagged with `@attr(...)` also inherit that tag.
- [`BaseException` still exists in python 3.](https://docs.python.org/3/library/exceptions.html#BaseException) All things `raise`d must be a subclass of `BaseException`.
- pydocstyle contains mutually exclusive rules, [D212](https://github.com/PyCQA/pydocstyle/blob/5add163ee56084b333c1071d19055a3780ba74e2/src/pydocstyle/violations.py#L204) ("Multi-line docstring summary should start at the first line") and [D213](https://github.com/PyCQA/pydocstyle/blob/5add163ee56084b333c1071d19055a3780ba74e2/src/pydocstyle/violations.py#L206) ("Multi-line docstring summary should start at the second line"). [You don't enable both at the same time](https://stackoverflow.com/a/45990465/1558430)
- [Tox](https://docs.python-guide.org/writing/tests/#tox) is a meta test runner that manipulates the virtualenv. If you have a project that never changes virtualenv (read: supports only one python version), Tox is not the tool of choice.
- In a [list comprehension](https://www.python.org/dev/peps/pep-0202/#rationale) (formally PEP 202) in the form `[... for x... for y...]`, the last index varies fastest, just like nested for loops.
- If you need a reason not to use list comprehensions for looping, [here](https://github.com/PyCQA/pylint/issues/2380#issuecomment-411660809) it is, from Claudiu Popa, a member of the [Python Code Quality Authority](https://github.com/PyCQA): _"(...) you are creating a transient list that just gets thrown away after you're done with the iteration. It's more efficient to just use the for loop here, and it goes without saying that it helps with the readability of the code as well."_
- "Returns anything with superclass T" can supposedly be written as [`-> Type[T]`](https://docs.python.org/3/library/typing.html#typing.Type).
- Using [`super(self.__class__, self)`](https://stackoverflow.com/a/18208725/1558430) in subclass of the class that contains that line will not call the correct superclass method. To prevent that happening in your project, use [flake8-super-call](https://pypi.org/project/flake8-super-call/).
- NumPy has its own PEP-like things, called [NEPs](https://www.numpy.org/neps/) ("NumPy Enhancement Proposals").
- Disable a named logger: `logging.getLogger('some name').propagate = False`
- If a function `yield`s, the function returns a `generator`, and any function that returns the return of that function also returns the same generator.
- [`Optional` is NOT used](https://docs.python.org/3/library/typing.html#typing.Optional) when the argument is optional. `Optional` is used when `None` is an allowed value, whether or not the `None` may be omitted.
- A [naive datetime object](https://docs.python.org/2/library/datetime.html) does not care about its time zone. An "aware" datetime object, however, does.
- The 1.0 release of [html5lib](https://pypi.org/project/html5lib/) (you know, the first one after 0.9999999...) was a botched release.
- Raymond, your role model, got burned [at least once](https://lwn.net/Articles/730962/) by a Dropbox employee.
- Alembic is called Alembic (a distillation apparatus) because it works with SQL[Alchemy](https://en.wikipedia.org/wiki/Alembic).
- Imports are done at most once per module. If you put a print statement inside a module, it is going to print just once, no matter how you `import` or `from... import` it again.
- [`typing.NoReturn`](https://docs.python.org/3/library/typing.html#typing.NoReturn) (a function that never returns, i.e. always raises) was new in python 3.5.4. Ubuntu ships python 3.5.2 though, because you're a joke. As an aside, `NoReturn` is not used when a function returns `None`.
- According to some kind of type theory, it is [preferred](https://docs.python.org/3/library/typing.html#typing.List) to annotate arguments with a abstract type, e.g. `Sequence`, `Iterable`, but annotate return values with a concrete type, e.g. `List`.
- Each item in a mock function's `call_args_list` is a list of [`call`s](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.call). Each `call` can be unpacked with `args, kwargs = call`. Then, as expected, `args` is a tuple and `kwargs` is a dict.
- `glob.glob()` is not sorted. You have to sort it yourself.
- To specify a version of python that pyenv will use for a project, put `2.5.0` inside a [`.python-version`](https://github.com/pyenv/pyenv#choosing-the-python-version) file at the project root. Then, `python` will map to whichever one pyenv thinks you want.
- [`raise AnError() from None`](https://stackoverflow.com/a/33822606/1558430) disables the "During handling of the above exception, another exception occurred" traceback.
- [This here](https://gist.github.com/sloria/7001839) tells you to: name something `audio.Controller` rather than `audio.AudioController`. It also tells you to `import a.module` rather than `from a.module import something` to prevent circular imports (no valid citation).
- `NotImplemented` (not `NotImplementedError`) is _returned_ exclusively by magic methods like [ `__eq__()`, `__lt__()`, `__add__()`, and `__rsub__()`](https://stackoverflow.com/questions/878943/why-return-notimplemented-instead-of-raising-notimplementederror) to indicate that the operation is not implemented for the other type.
- `dict` is a "subclass" of `MutableMapping`.
- Runtime complexity for dicts/lists/deque are [published](https://wiki.python.org/moin/TimeComplexity). Notably, lists are surprisingly faster than dicts in getting an item by index/key (O(1) vs O(n)) in the worst case.
- [`TestCase.addCleanup`](https://docs.python.org/3.5/library/unittest.html#unittest.TestCase.addCleanup) (noting the `up` is lower case, unlike that in `setUp`, because [peps sucked 20 years ago](https://www.reddit.com/r/Python/comments/p03k0/why_does_no_one_seem_to_care_that_unittest/c3lfxnf/) amirite) is an instance-only method. Class-level exceptions cannot be cleaned up like this.
- A method in a class can be called by a line inside the class without receiving `self`. See [example](sources/0003.py). It's not going to pass PEP8, but it sure runs.
- There is an `assertIs` in addition to `assertEqual`, but [using `is` for numbers can potentially be incorrect](https://codeyarns.com/2012/05/01/integer-caching-in-python/) when the number is outside [-5, 256]... among other [strange situations](https://stackoverflow.com/a/15172182/1558430) where the compiler could not optimise the code ahead of time.
- Like [they said](https://docs.python.org/3/library/functions.html#breakpoint), `breakpoint()` is purely a convenience function.
- [PEP 420](https://www.python.org/dev/peps/pep-0420/#specification): It is no longer necessarily the case that a folder needs an `__init__.py` (making it a package) for files to be imported, but the rules are still confusing enough that you will want to continue having these files.
- According to [this guy](https://stackoverflow.com/questions/2903827/why-are-python-exceptions-named-error), exception classes should not end with `Exception` because we don't write normal classes ending with `Class` or variables ending with `_variable` either. As for _what_ exceptions are not errors, examples include `SystemExit`, `KeyboardInterrupt`, and exceptions that are called `Warning`s instead of `Error`s.
- You have never used F strings because they are python 3.6 and up, but you're stuck on 3.5.
- [If a class declares `__slots__`, all of its subclasses need to declare `__slots__` individually](https://stackoverflow.com/a/28059785/1558430), but only attributes introduced by that particular subclass.
- Only python3 classes with `__slots__` defined will raise `AttributeError` when something not inside `__slots__` is assigned to it. It does not do that in python2. See also: [source](sources/0005.py)
- `set1.isdisjoint(set2)` is a very verbose way to check if the two sets have no common items, aka `not (set1 & set2)`. The only difference is [short-circuiting](https://stackoverflow.com/questions/45112928/python-isdisjoint-runtime). And yes, [a set is disjoint with an empty set](https://python-reference.readthedocs.io/en/latest/docs/sets/isdisjoint.html).
- In python 2, `range()` a function. In python3, it is a class. Its instance type is `range`.
- An [iterable](https://docs.python.org/3/glossary.html) is an object that can return its members one at a time. A "sequence" is an iterable that supports indexing. If you need to remember one thing, remember: **the `list` is the built-in sequence**. `dict`s are iterables but not sequences.
- A generator that outputs nothing can be truthy. [There is no good way to tell if a generator is empty](https://stackoverflow.com/questions/661603/how-do-i-know-if-a-generator-is-empty-from-the-start).
- `random.choice` cannot choose from an empty list.
- Docstrings cannot be assigned literally. If you have a `foo = """string"""`, and a `class Bar:\nfoo`, the class does not have a docstring. You can assign it to `__doc__` though.
- `Arrow` is not an instance of `datetime`.
- [pydocstyle](https://github.com/PyCQA/pydocstyle) has a rule, [D401](http://www.pydocstyle.org/en/stable/error_codes.html), that says examples from [PEP 257](https://www.python.org/dev/peps/pep-0257/) are invalid. All docstrings need to start with a verb in imperative mood, even for functions that return a boolean.
- To run a script in a virtualenv, you just need to run it with _that_ python (usually `~/virtualenvs/blah/bin/python`). You can even put it in the script's shebang if it doesn't need to be portable.
- [Adding `Counter()` to another `Counter()`](https://docs.python.org/2/library/collections.html#collections.Counter) removes all zeros and negative counts.
- [`json` raises `ValueError` but `simplejson` raises `JSONDecodeError`](https://stackoverflow.com/questions/712791/what-are-the-differences-between-json-and-simplejson-python-modules#comment20589523_712799), which is a subclass of `ValueError`. To be compatible with both (if that's your goal) you can only catch `ValueError`.
- To make an ordered counter (a blend of `Counter()` and `OrderedDict()`), you [really](https://stackoverflow.com/a/35448557/1558430) make `class OrderedCounter(Counter, OrderedDict)`.
- The G in Gunicorn stands for Green. It uses a pre-fork worker model. ["pre-fork" means the worker is forked before a request comes in](https://stackoverflow.com/a/25894770/1558430), and ["worker" means the master process spins up workers, but doesn't know what the workers are doing](http://docs.gunicorn.org/en/stable/design.html).
- `max([])` would complain about being an empty sequence, but `max([], default=5)` will not.
- In 2018, a PEP that [allows an expression to also assign shit](https://www.python.org/dev/peps/pep-0572/) (i.e. `y0 = (y1 := f(x))`) was accepted. [GVR _rage quit_.](https://www.python.org/dev/peps/pep-0401/) He left because [people hated him for the decision he makes in _his_ language](https://mail.python.org/pipermail/python-committers/2018-July/005664.html). He left because he's tired [of having to fight to have his project the way to wants it].
- [The contents of a lambda is never called on initialisation](sources/0006.py), even if it looks like it will, like `a = lambda: foo()`. In this case, `foo` is not called until the lambda is.
- Yes, you can redefine the `print()` function in python3.
- `"abcd".split()` will only split it to `["abcd"]`, which is useless. `"abcd".split('')` will complain about "empty separator" instead, which is also useless. To get `['a', 'b', 'c', 'd']`, do `list("abcd")`.
- [IronPython (python on Mono) doesn't have an global interpreter lock (GIL)](https://rohanvarma.me/GIL/).
- `pip install --user` is usable only if you include `~/.local/bin` in your path.
- Python's `float` is actually [usually C's `double`](https://docs.python.org/2/library/stdtypes.html#numeric-types-int-float-long-complex).
- [Perhaps the main flaw of Python's async implementation is the fact that you can accidentally call synchronous functions from asynchronous contexts - and they'll happily work fine and block the entire event loop until they're finished.](https://www.aeracode.org/2018/06/04/django-async-roadmap/)
- Variable scoping is full of shit. [Nested functions can access variables outside it, but not if it is redefined _anywhere in the function, including behind the line of access_](https://stackoverflow.com/a/13277359).
- XML parsing can lead to files automatically fetched from the internet. [etree, DOM, and xmlrpc are all wide open to these types of attacks](https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03). The official response is [yes that's right](https://docs.python.org/3/library/xml.html#xml-vulnerabilities).
- Celery's `.delay()` is just `.apply_async()` with fewer options. [Always prefer `.apply_async`.](https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/)
- If you have a celery task that depends on input from another task, [chain them up](https://pawelzny.com/python/celery/2017/08/14/celery-4-tasks-best-practices/). That way you wait for one task instead of two.
- If you define a celery config's `task_queues`, you also need to define its `task_routes` (which tasks go to which queue). Use `'*'` to say all tasks go to one queue.
- Unless you have an old project that goes by some convention, [gevent is typically better than eventlet](https://blog.gevent.org/2010/02/27/why-gevent/) for reliability and ease of use.
- If you use Django _just_ for the ORM, then [Peewee](http://docs.peewee-orm.com/en/latest/) might be a better choice. It does have [a migration extension](https://github.com/klen/peewee_migrate), but you will slowly realise you will need to write your own raw DDL anyway.
- Notice `ayncio`'s name: [it's for waiting for IO](https://realpython.com/async-io-python/). It is not for you to write parallel code. It is not multiprocessing. It is not multithreading. It is how you write coroutines (`async def`). It is a way you (a)wait on stuff. _Use `asyncio` when you can. Use threading if you must._
- `__len__` must return an int, even if you override it to return 1.5 or something.
- `int()` takes a base, i.e. `int('0b10000', 2)`.
- You [cannot](scripts/py3.5-await-outside-async.py) await anything inside a non-async function.
- "A lot of things are implicit in python. Like variable declarations. Referring to PEP20 isn't an argument, and blindly making everything explicit would be stupid." - [Rawing7](https://www.reddit.com/r/Python/comments/9u3kop/why_does_pythons_async_execution_model_so/e91fkwl/)
- In SQLAlchemy, to define a column with a python-side "default", use the keyword `default`. To define a column that the database server knows is the default, use [`database_default`](https://docs.sqlalchemy.org/en/13/core/defaults.html).
- It looks like you shouldn't do `str(some_bytes)` and `str(some_bytearray)`. [`python3 -b`](https://docs.djangoproject.com/en/2.2/releases/2.0/#removed-support-for-bytestrings-in-some-places) tells you that's not a good thing.
- Use [pipdeptree](https://pypi.org/project/pipdeptree/) to a. find out your dependencies as a tree, and find out why you have a package installed (as which packages' dependency).
- The trailing comma in `def foo(a,b,)` is valid in python3.5, but in [`def foo(*,a,b,)`, it is not](https://bugs.python.org/issue9232#msg110089)... at least not until 3.6.
- The difference between `str(a)` and `a.__str__()` is [the former calls `type(a).__str__(a)`](https://stackoverflow.com/a/41168971/1558430)... in case you deliberately monkey patch `a`'s `__str__`.
- [`py.test` is the old `pytest`](https://stackoverflow.com/questions/39495429/py-test-vs-pytest-command). You should not use it anywhere.
- If your function says it takes in an `Enum`, then (according to mypy) [no matter what the value is, you need to supply it from an Enum](scripts/enum_test.py).
- Strings' `.zfill(pad)`, which pads your strings with zeros on the left until you get a length of (pad), is basically a coding contest method for when you need to generate a fixed-length binary string from `bin()`.
- You can inline `try` and `except`, i.e. `try: print(1); print(1/0)`, but there is no C-style syntax to turn that into a multi-line statemnet, e.g. `try: (print(1); \n print(1/0))` (considered a semicolon-separated tuple), `try: {print(1); \n print(1/0)}` (considered a semicolon-separated set), `try: (print(1), \n print(1/0))` (it's a valid tuple, but you can't ever have a statement in it).
- Custom class attributes prefixed with `__` are private. It is not possible to read it. *However*, [you can still assign something to it from the outside](scripts/dunder_private.py), and any `__attributes` that was not declared in the class are actually public. The instance cannot read the value you assigned though (because it has its own hashed key for that attribute). What does it mean for you? Nothing. Use it how you like.
- `set_a or set_b` gives you the first set that is not empty. Use `set_a | set_b` (OR) or `set_a ^ set_b` (XOR).
- [Gareth Dwyer](https://github.com/sixhobbits), author of the book Flask by Example, [said](https://www.codementor.io/garethdwyer/flask-vs-django-why-flask-might-be-better-4xs7mdf8v) that Flask might be better than Django. In that post, he wrote two hello-world examples.
- Because `'%s' % 1 + 2` raises `TypeError` instead of giving you `3`, you can see `%` has higher precedence than `+`.
- [Stackoverflow](https://stackoverflow.com/questions/14083111/should-i-use-encoding-declaration-in-python-3) says [PEP 263 `# coding=utf-8` lines](https://www.python.org/dev/peps/pep-0263/) are not necessary in [python3](https://www.python.org/dev/peps/pep-3120/) if all the files in the same project are in UTF-8, and your editor knows how to deal with it.