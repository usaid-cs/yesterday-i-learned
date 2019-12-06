# Being a developer

A senior anything developer needs to know more than just a specific language.
I would go so far as to argue there's no such thing as a senior php developer or a senior javascript developer. There's only a _senior_ developer.
Basically, if you were handed a project and needed to do it from start to finish on your own, could you?

## Tools & Scoping

- If I gave you a client spec, could you find enough of the holes in it to inform management that their $40,000 bid should really be $120,000?
- Given a client spec, would you be able to select the appropriate tool for the job? That is, should be it Wordpress? Should it be Drupal? Should it be Joomla? (trick question, it should never be Joomla). Should it be Symfony, or Laravel? Should it be 100% custom?

## System Administration & Dev Ops

- Could you spool up an appropriate Amazon server? Could you set up a working environment in Vagrant that is easy for another developer to spin up if you needed their help?
- Could you obtain an SSL cert and get it hooked up?
- ~~Could you untangle some nasty push into a git repo?~~

## Full Stack

- Could you create a responsive, semantically clear HTML front-end? What about javascript? Clean javascript, not some jQuery jungle.
- Can you manage a MySQL or Postgres DB without help? Going back to tools & scoping, is a relational database even the right solution for project? Should you use a mix of both?
- Can you cleanly integrate & optimize both (SQL/NoSQL)?
- Do you know how to scale relational and non-relational databases?
- Do you know how to utilize transactions in PHP and set up foreign key constraints and cascades to ensure data integrity?
- What about apache/ngnix and other server-related things?

## Leadership & Teamwork

- If you didn't have the time to do anything yourself, could you effectively manage a team of developers to hit milestones and sprint targets? (effectively becoming a low-level PM) How would you do it?
- How would you best allocate resources to overcome blockers?
- Can you lead a code review?
- Would you know how to assign tasks to the right people such that they become better developers as a result of working on this project - that is, pushing them ever so slightly out of their comfort zone, but not so far that it jeopardizes the product or timelines?

# Algorithms

> _[Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy.](http://users.ece.utexas.edu/~adnan/pike.html)_

## [Bubble sort](http://www.ideserve.co.in/learn/bubble-sort)

Iterating through the list, swap item n with item n+1 if item n+1 is smaller than item n. Repeat until no items are swapped in an entire run.

Bubble sort gets its name because larger items bubble up to the end of the list (or smaller items bubble up to the front of the list).

## [Selection sort](http://www.ideserve.co.in/learn/selection-sort)

Find the smallest item in the array and take it out (or swap with the first item if you want).
Find the next smallest item in the array and take it out (or swap with the second item if you want).
Repeat until there are no items.

## [Insertion sort](http://www.ideserve.co.in/learn/insertion-sort)

Get yourself a new blank list.
Take the first item from the array and place it in the list, sorted.
Take the second item from the array and place it in the list, sorted.
Repeat until there are no items in the array.

This is different from selection sort only from where the next item is taken. Selection sort looks for the smallest item. Insertion sort gets the first item and figures where to put it.

## [Bloom filter](http://en.wikipedia.org/wiki/Bloom_filter)

Heuristically determine if something is in a set, being correct most of the time.

- Uses less space than full search

## Clustering

### K-means

```
for data in datas:
    for mean in means:
        if data is closest to this mean:  # "closest" is the euclidean distance
            mean.add data
    return means
```

## "Space-time tradeoff"

[Space-time tradeoff](https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff) is usually "trade space for speed", rather than "trade speed for space". You frequently see things like caches (space for speed) and hashes (space for speed). There are occasions where space is limited (like in firmware), but they are comparatively rare.

# Patterns

The [SOLID pattern](https://en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29): "one class does one simple thing, and the subclasses of this class also does the same thing."

## Creational patterns

### Builder

### Abstract Factory

### Factory Method

### Prototype

### Singleton

## Structural patterns

### Adapter

### Bridge

### Composite

### Decorator

### Facade

### Flyweight

### Proxy

## Behavioural patterns

### Chain of Responsibility

### Command

### Interpreter

### Mediator

### Memento

### Observer

### State

### Strategy

### Template Method

### Visitor

# Data structures

## Linked lists

## stacks

Stacks can be used to implement [depth-first search](https://www.youtube.com/watch?v=iaBEKo5sM7w).

1. Given a tree/graph and its root, push it onto the stack.
2. Grab any of its children at random. Push it onto the stack. _Mark the node as visited._
3. If there are unvisited nodes, continue 2.
4. If there are no unvisited nodes, pop the node out of the stack.

The stack being empty signals the end of the algorithm run.

## queues

## Priority Queues

[Priority queues are typically implemented as heaps](https://stackoverflow.com/a/11093725/1558430). **Heaps**, in particular binary heaps, are binary trees whose topmost element is the smallest (in this case, highest priority). **Binary trees**, in turn, are typically implemented with arrays. We have come full circle.

## dicts

## trees

"Leaves" refer exclusively to the nodes at the bottom level, not just any node with no children.
A "full" tree is one that has the maximum number of leaf nodes.
A "complete" binary tree is one that is full, except maybe for the last level.

### binary search trees

### [B-trees](https://en.wikipedia.org/wiki/B-tree)

No one knows what the B stands for.

## Hashes

## Monads

- [Monads](https://en.wikipedia.org/wiki/Monad_(functional_programming\)) are "functional expressions" like `== null`.
- Monads aren't useful alone; they require composition to do real work. _Binding_ two monads means `(monad1 ∘ monad2)(x) -> monad1(monad2(x))`.
- When monads are composed, they can short-circuit evaluations, making programs run faster.
- Game theory: sometimes the intuitive option isn't the one you should pick -- nor is the unintuitive option, because that's also what the other guy is thinking. [Here are a few examples](http://wjspaniel.wordpress.com/2014/05/25/game-theory-is-really-counterintuitive/).

# Challenges

- [ ] Erlang (concurrent programming)
- [ ] [Operating Systems](http://pages.cs.wisc.edu/~remzi/OSTEP/)
- [ ] TCP/IP
- [ ] Machine learning (stocks)
- [ ] Image (logo) recognition
- [ ] Haskell (functional static programming)
- [ ] Fabric (deployment)
- [ ] Hadoop (mapreduce / parallelism)
- [ ] Julia (science)
- [ ] ETag tracking

# Misc

- **Tail call optimisation** refers to the behaviour in recursive functions for when a true function (one that has no side effects) calls itself again as the only operation in the last statement, allowing the computer to run that function while preserving the function's address space.
- **Class P Problems** (or just P) are problems that an algorithm can solve in polynomial time. P is also known as _quickly solvable_.
- **Class NP Problems** (or just NP) are problems that can be solved quickly, provided that the answer is given. NP is also known as _quickly checkable/verifiable_.
- **NP-Complete** problems are problems that are both NP and NP hard.
- The [null object pattern](https://en.wikipedia.org/wiki/Null_Object_pattern) involves overloading a function with one that specifically handles the base case of "null".
- A [bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) has nothing to do with blooming; it was just named after a guy called Burton Bloom. It is a space-efficient set that can give you false positives (something is in the list), but never false negatives (something is not in the list).
- The [Big O Cheat Sheet](http://bigocheatsheet.com/) ranks everything except O(1), O(n), and O(log n) as "bad" or worse.
- "Covariance" is just a fancy way of saying "if parent method returns `Number` then surely a subclass method can return `float`"
- In [Dijkstra's shortest path algorithm](https://www.youtube.com/watch?v=gdmfOwyQlcI) (requires weighted edges), all but the root node has an initial weight of infinity. Every single run of the algorithm involves travelling from the lowest unvisited vertex to its neighbours.
- [Decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) appears to have come from python, which was in turn inspired by [Java annotations](https://en.wikipedia.org/wiki/Java_annotation); the generic term for a function-modifying function is called an [advice](https://en.wikipedia.org/wiki/Advice_%28programming%29). Depending on compiler setup, Java annotations don't necessarily have to do anything.
- "25519" in ed25519 is 2^(255) - 19. A 256-bit elliptic curve key (which is what Curve 25519 is) is [weaker](https://wiki.openssl.org/index.php/Elliptic_Curve_Cryptography) than a 4096-bit asymmetric key, like RSA.
- Unlike "Big O", which is the upper bound, there is also a "Big Theta" which includes both the lower and upper bounds, called the "tight bound". You can't have a "best case of `O(n)`" because the best case is Omega, or `Ω(n)`.
- The Y combinator is [said](https://deniskyashif.com/on-recursive-functions/) to allow recursion without recursing, or in languages that do not support recursion. The JS implementation is `const Y = f => { const g = x => f(x(x)); return g(g); };`.
- A superclass is called a superclass, despite it always having fewer methods than its subclasses, because [a superclass always has more instances, the thing we are counting.](https://www.youtube.com/watch?v=mVVNJKv9esE)
- A [higher-order function](https://github.com/hemanth/functional-programming-jargon#higher-order-functions-hof) (more jargons inside link) is a function that accepts a function and returns a function. A decorator is a higher-order function.
- [Dynamic arrays](https://stackoverflow.com/questions/3917574/how-is-pythons-list-implemented) start off larger than the size that the program requested. Then it fills up. When it does get filled up, the array is _copied_ to a new place with a larger size. Apart from that, there is no speed penalty compared to normal arrays.
- If a question asks you to ["add up two numbers without using + or -"](https://leetcode.com/problems/sum-of-two-integers/), [don't use `sum()`](https://leetcode.com/problems/sum-of-two-integers/discuss/84279/Python-solution)... instead, invest your time in learning [the bit operations](https://leetcode.com/problems/sum-of-two-integers/discuss/84410/Python-Solution).
- Binary search [is](http://stackoverflow.com/questions/3581528/how-is-the-square-root-function-implemented) the most simple way to implement `sqrt` without a library function. Given `n`, start from `n/2`, and return when results converge.
- [Two's complement](https://en.wikipedia.org/wiki/Two%27s_complement). Assuming your numbers don't overflow, you can represent negative numbers with **inverted bits, and add 1**. For example, to represent `-4`, you figure out what `4` is (hint: it's `00000100`), flip all the bits (hint: it's `11111011`), and then add 1 (hint: it's `11111100`). Then, for some reason, if you add and subtract that number (again, assuming it doesn't overflow), the result is still what you would expect. For example, if you add 13 (`00001101`) to -4 (`11111100`), you end up with `100001001` (ignore carryover, or leftmost 1), which is 9.
- **An abstract data type (ADT) is just a contract**. The user of the ADT doesn't need to know how it's implemented; the provider of the ADT doesn't need to know how it's used.
- [Metaclasses](https://en.wikipedia.org/wiki/Metaclass) are classes whose instances are classes.
- You use [recursion](https://stackoverflow.com/a/7186607/1558430) to do variable-depth for loops.
- [JIT compilers might actually be faster than AOT compilers](https://softwareengineering.stackexchange.com/questions/274640/why-is-android-runtimes-aot-compilation-more-performant-than-dalviks-jit) given the amount of information that is available to them when the program is running. The advantage of AOT, however, is it can take as much time as it wants, and compile only once.