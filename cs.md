# Computer Science

## [Grades](https://www.levels.fyi/2019/) of Developers

### Entry-level (0~2 years)

New-grads or little to no industry experience.
Develop and maintain low to moderately complex components working on a team.
Typically receives guidance and support from more experienced team members.

### Intermediate engineers (2~5 years)

Develop and own moderate to complex components.
Possibly lead a small team or project.
Ability to mentor engineers, provide technical guidance, code reviews, design and deliver on small projects end-to-end.
Impact is typically at the immediate team scope.
At many companies, this is considered a 'career-level', as in you can spend the rest of your career operating at this level without being pushed out for not being promoted.

### Senior engineers (5+ years)

* Typically less than 30% of employees in a company are at this level.
* **Expected to lead and own complex technical initiatives.**
* Expected to solve a problem / finish a project in the best way possible, not just in ways they already know about.
* Begin setting the vision and future direction of team.
* Impact across multiple related teams within an org.
* Role shifts more towards design rather than implementation depending on size and expectations at company.
- Learn to push back. You aren't hired to be a code monkey. You are hired to make high quality contributions.

### Staff engineers (10+ years)

This level is much more coveted than the previous ones. Typically less than 10% of employees in a company are at this level.

* Impact spans across organizations.
* Entrusted with business-critical projects in highly-ambiguous problem spaces, from start to finish, while balancing various technical trade offs including speed to delivery, maintainability, and system performance, and for setting technical vision for an org or multiple orgs.
* Responsible for reviewing and providing feedback on technical designs across an org.
* Responsible for mentoring new hires and other engineers to help them become more proficient by example, tech talks, paired programming, and other avenues to increase technical efficiency across the organization.
* **Little to no day-to-day coding.**
* Role depends highly on organizational and company needs and becomes loosely defined.
* **Expected to operate fully autonomously.**

### Principal engineers (15+ years):

* Usually less than 3% of employees in a company are at this level.
* Smaller companies may not have any individuals at this level.
* Impact spans across the company and sometimes industry.
* Expected to operate fully autonomously.

## Data Structures

### Linked lists

There are singly-linked lists, and then there are doubly-linked lists.

Learn about the two-pointer method for linked list manipulation.

### Stacks

Stacks can be used to implement [depth-first search](https://www.youtube.com/watch?v=iaBEKo5sM7w). If you use recursion, you use a (call) stack already.

1. Given a tree/graph and its root, push it onto the stack.
2. Grab any of its children at random. Push it onto the stack. _Mark the node as visited._
3. If there are unvisited nodes, continue 2.
4. If there are no unvisited nodes, pop the node out of the stack.

The stack being empty signals the end of the algorithm run.

### Queues

Queues can be used for BFS.

### Priority Queues

[Priority queues are typically implemented as heaps](https://stackoverflow.com/a/11093725/1558430) (i.e. a priority queue is an abstract data type, and a heap is a data structure). **Heaps**, in particular binary heaps, are binary trees whose topmost element is the smallest (in this case, highest priority). **Binary trees**, in turn, are typically implemented with arrays. We have come full circle.

### Trees

"Leaves" refer exclusively to the nodes at the bottom level, not just any node with no children.
A "full" tree is one that has the maximum number of leaf nodes.
A "complete" binary tree is one that is full, except maybe for the last level.

#### Binary search trees

* In-order traversal is important because if you traverse a BST in order, then it just so happens that [you'll get all elements in ascending order](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/).

#### [B-trees](https://en.wikipedia.org/wiki/B-tree)

No one knows what the B stands for.

#### Post-order traversal

Post-order traversal is a fancy name for "first visit the left, then visit the right, finally visit the current node".

### Heaps

Heaps are ordered binary trees (not binary *search* trees). Max heaps are heaps where the parent is always greater than the child.

Properties of a min heap:

* It is a complete binary tree. (A complete binary tree is a binary tree that has all nodes filled in, except for maybe the bottom right portion at the bottommost layer.)
  * And since it is not a BST, the left hand side is not necessarily less than the right hand side.
* The value of a node is smaller *or equal* to its children. (i.e. as opposed to a BST, a value can be in the heap more than once.)

#### [How to implement a heap](https://leetcode.com/explore/learn/card/heap/643/heap/4017/)

You can implement a heap using an array...?

* The first index of the array stores the number of elements in the tree.
* Given a node's array index, `i`: the left child is at `i * 2`, and the right child is at `i * 2 + 1`, and its parent is `i // 2`.
* To determine if a node in a heap is a leaf node (with no children): If the node index is greater than `n / 2`, then it is a leaf.

#### [How to insert into a min heap](https://leetcode.com/explore/learn/card/heap/643/heap/4019/)

1. Remember that a complete binary tree is one that is completely full, except for maybe the right hand side of the bottom layer. Therefore, we place a new node at either the first slot available on the bottom right layer, or make a new level with the new node at the bottom left.
2. The new node is probably not where it should be. Bubble up the value until the min heap property is satisfied.

#### [How to delete from a min heap](https://leetcode.com/explore/learn/card/heap/643/heap/4020/)

1. Swap the value of the last node in the complete binary tree, with the top node. The property of the min/max heap is not satisfied at this point.
2. Delete the last node in the complete binary tree.
3. If the top node has a value that violates the heap property, then swap with its smallest child node (in case of min heap), or largest child node (in case of max heap).
4. Keep doing that until the heap property is satisfied.

### Hashes

There are hash maps (dicts) and hash sets (sets). Both provide accessing an element in O(1) time (in a set's case, looking up an item itself).

In some languages, there are ways to override an object's `getHashCode` or equivalent, such that you can prevent yourself from adding something into a hashmap/set more than once (for whatever reason).

## Algorithms

> _[Fancy algorithms are slow when n is small, and n is usually small. Fancy algorithms have big constants. Until you know that n is frequently going to be big, don't get fancy.](http://users.ece.utexas.edu/~adnan/pike.html)_

### [Bubble sort](http://www.ideserve.co.in/learn/bubble-sort)

Iterating through the list, swap item n with item n+1 if item n+1 is smaller than item n. Repeat until no items are swapped in an entire run.

Bubble sort gets its name because larger items bubble up to the end of the list (or smaller items bubble up to the front of the list).

### [Selection sort](http://www.ideserve.co.in/learn/selection-sort)

Find the smallest item in the array and take it out (or swap with the first item if you want).
Find the next smallest item in the array and take it out (or swap with the second item if you want).
Repeat until there are no items.

### [Insertion sort](http://www.ideserve.co.in/learn/insertion-sort)

Get yourself a new blank list.
Take the first item from the array and place it in the list, sorted.
Take the second item from the array and place it in the list, sorted.
Repeat until there are no items in the array.

This is different from selection sort only from where the next item is taken. Selection sort looks for the smallest item. Insertion sort gets the first item and figures where to put it.

### [Bloom filter](http://en.wikipedia.org/wiki/Bloom_filter)

Heuristically determine if something is in a set, being correct most of the time.

- Uses less space than full search

### Greedy approach

> A greedy algorithm follows [the] problem solving approach of making the locally optimal choice at each stage, with the hope of finding a global optimum.

In each iteration, the algorithm makes a choice that maximises the result.

It doesn't always solve your problem, but that's what greedy is.

## Clustering

### K-means

```
for data in datas:
    for mean in means:
        if data is closest to this mean:  # "closest" is the euclidean distance
            mean.add data
    return means
```

## One-pass random selection

If you need to, say, "get one random line from a file", and you don't want to keep every line in memory, then [replace the current line with the next line at a decreasing probability](https://www.wikiwand.com/en/Reservoir_sampling#/An_optimal_algorithm) of 1/(number of lines read). It is equivalent to picking the nth line at random.

### "Space-time tradeoff"

[Space-time tradeoff](https://en.wikipedia.org/wiki/Space%E2%80%93time_tradeoff) is usually "trade space for speed", rather than "trade speed for space". You frequently see things like caches (space for speed) and hashes (space for speed). There are occasions where space is limited (like in firmware), but they are comparatively rare.

## Patterns

The [SOLID pattern](https://en.wikipedia.org/wiki/SOLID_%28object-oriented_design%29): "one class does one simple thing, and the subclasses of this class also does the same thing."

### Creational patterns

#### [Builder](https://refactoring.guru/design-patterns/builder)

Lets you construct a complex object step by step. Useful for constructing different objects with the same setup code.

```
new Car()
    .setWheels(4)
    .setTransmission(manual)
    .getProduct()

new Car()
    .setWheels(2)
    .setTransmission(CVT)
    .getProduct()
```

#### [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)

The abstract factory interface has methods that claim to return an abstract object.

The concrete factories that subclass from the abstract factory can decide for themselves what kind of concrete objects they will produce.

#### [Factory Method](https://refactoring.guru/design-patterns/factory-method)

A concrete factory decides, for you, what kind of object you would like.

For example, the `Dialog.create` method will decide whether to return `WinDialog` or `MacDialog` depending on the OS context.

#### Prototype

Subclasses all support a method called `clone()`, and you delegate the cloning method to the object itself (since some parts of the object can be private).

#### Singleton

The class contains a `getInstance()` method, which keeps track of the first object that it creates, and returns a reference to that object every time.

### Structural patterns

#### Adapter

#### Bridge

#### Composite

#### Decorator

#### Facade

#### Flyweight

#### Proxy

### Behavioural patterns

#### Chain of Responsibility

#### Command

#### Interpreter

#### Mediator

#### Memento

#### Observer

#### State

#### Strategy

#### Template Method

#### Visitor

## Misc

- **Tail call optimisation** refers to the behaviour in recursive functions for when a true function (one that has no side effects) calls itself again as the only operation in the last statement, allowing the computer to run that function while preserving the function's address space.
- **P Problems** (or just P) are problems that an algorithm can solve in polynomial time. P is also known as _quickly solvable_.
- **NP Problems** (or just NP) are problems that can be solved quickly (checked in polynomial time), provided that the answer is given. NP is also known as _quickly checkable/verifiable_.
- **NP-Hard** problems are ["at least as hard" as NP problems, but don't need to be an NP problem, or even a decision problem](https://stackoverflow.com/questions/1857244/what-are-the-differences-between-np-np-complete-and-np-hard).
- **NP-Complete** problems are problems that are both NP and NP hard.
- The [null object pattern](https://en.wikipedia.org/wiki/Null_Object_pattern) involves overloading a function with one that specifically handles the base case of "null".
- A [bloom filter](https://en.wikipedia.org/wiki/Bloom_filter) has nothing to do with blooming; it was just named after a guy called Burton Bloom. It is a space-efficient set that can give you false positives (something is in the list), but never false negatives (something is not in the list).
- The [Big O Cheat Sheet](http://bigocheatsheet.com/) ranks everything except O(1), O(n), and O(log n) as "bad" or worse.
- "Covariance" is just a fancy way of saying "if parent method returns `Number` then surely a subclass method can return `float`"
- In [Dijkstra's shortest path algorithm](https://www.youtube.com/watch?v=gdmfOwyQlcI) (requires weighted edges), all but the root node has an initial weight of infinity. Every single run of the algorithm involves travelling from the lowest unvisited vertex to its neighbours.
- [Decorators](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators) appears to have come from python, which was in turn inspired by [Java annotations](https://en.wikipedia.org/wiki/Java_annotation); the generic term for a function-modifying function is called an [advice](https://en.wikipedia.org/wiki/Advice_%28programming%29). Depending on compiler setup, Java annotations don't necessarily have to do anything.
- "25519" in ed25519 is 2^(255) - 19. A 256-bit elliptic curve key (which is what Curve 25519 is) is [weaker](https://wiki.openssl.org/index.php/Elliptic_Curve_Cryptography) than a 4096-bit asymmetric key, like RSA.
- Unlike "Big O", which is the upper bound, there is also a "Big Theta" which includes both the lower and upper bounds, called the "tight bound". You can't have a "best case of `O(n)`" because the best case is Omega, or `Ω(n)`. A tight bound is found when an algorithm's best case *and* worst case differ by no more than a constant factor.
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
- The supposed [advantage of little-endian](https://softwareengineering.stackexchange.com/a/95573/116811) is that if you have a 16-bit value stored in a 32-bit long integer, you can read the first 16 bits of the little-endian long (i.e. "short") and still get that value at exactly that address.
- The [rule of 3](https://news.ycombinator.com/item?id=22022466) is real. Don't refactor something in the name of deduplication until it happens three times (and, even then, think about whether deduplication is the right abstraction). It doesn't mean you have to copy code for the second time, it just means you need to think for yourself whether the code there is worth copying if the total lifetime number of occurrences is 3 or fewer.
- [If you find yourself passing parameters and adding conditional paths through shared code, the abstraction is incorrect.](https://www.sandimetz.com/blog/2016/1/20/the-wrong-abstraction)
- The [make change](https://www.youtube.com/watch?v=DJ4a7cmjZY0) question is a dynamic programming question. Apparently the number of unique ways to make change is (the number of unique ways to change the amount - 1) + (the number of unique ways to change the amount, if you had one fewer type of coin, assuming the subtraction of it yields 0 or more). Or something like that.
- [Declarative programming](https://en.wikipedia.org/wiki/Declarative_programming) is an umbrella term that describes any kind of programming that is not imperative. SQL ("get me this without me telling you how") is declarative programming. Languages without a side effect (like regex) are declarative programming. *Functional programming is declarative programming*.
- The term [fifth-generation programming language](https://en.wikipedia.org/wiki/Fifth-generation_programming_language) was misused by software vendors so much that the term now means nothing on top of what SQL does.
- Async [backpressure](https://medium.com/@jayphelps/backpressure-explained-the-flow-of-data-through-software-2350b3e77ce7) refers to anything that slows down your async slow from progressing. Reasons can be: CPU, IO, waiting for the user to confirm a thing. You can reduce backpressure mostly by reducing the amount of data that goes into the flow, buffering (sometimes by re-queuing) or batching intermediate steps, or dropping whatever you can't handle as a last resort.
- [Embarrassingly parallel](https://en.wikipedia.org/wiki/Embarrassingly_parallel) means "embarrassing in riches", i.e. an overbundance of places where your code can run in parallel.
- Microservices don't help scale the service... they only help scale development. ["If you don't have the organization structured for "independent services", then microservices will likely fail."](https://old.reddit.com/r/programming/comments/jznvbz/the_macro_problem_with_microservices/gddh7lh/)
- When they say ["write code ... mostly functions"](https://www.brandonsmith.ninja/blog/write-code-not-too-much-mostly-functions), they mean *pure* functions, with no side effects.
- Array access is O(1) because the address for any item is (address + index)---which takes O(1) to compute---and then we specifically ignore the cost of memory access, which may be [close to O(log n)](https://stackoverflow.com/a/20961951/1558430) in hardware, but we don't talk about that.
- "Marshalling" is the almost same thing as serialising.
- [On data ensapsulation in OO](https://stackoverflow.com/questions/2747721/getters-and-setters-are-bad-oo-design): "don't ask for the information you need to do the work; ask the object that has the information to do the work for you."
- The word "trie" has the same pronunciation as "try".
- Software can't tell you the big-O complexity of an algorithm [because of the halting problem](https://stackoverflow.com/questions/38420564/is-there-a-programmatic-way-or-eclipse-plugin-to-calculate-big-o-notation-for-ja). There may be plugins that tell you an approximate runtime, though.
- [Continuous integration](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment) just means your feature code is quickly merged into master. Automated tools help with the whole testing thing in the process.
- A "[data race](https://en.wikipedia.org/wiki/Race_condition#Data_race) condition" occurs when two or more threads access the same memory concurrently.
- [How to tell if a FLOSS project is doomed to FAIL](http://www.theopensourceway.org/book/The_Open_Source_Way-How_to_tell_if_a_FLOSS_project_is_doomed_to_FAIL.html)
- The whole point of devops was to make devs own their infrastructure. [There shouldn't be a "devops team"](https://wolfoliver.medium.com/the-big-devops-misunderstanding-8435a910a5fd), because that's just, an ops team.
