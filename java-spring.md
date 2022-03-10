![It's Springtime!](https://i.imgur.com/n93DTMM.png)

## How to Basic

* To run the project: [`./gradlew bootRun` or `./mvnw spring-boot:run`](https://spring.io/guides/gs/spring-boot/)
* To run the project with auto-reload, run [`./gradlew build --continuous`](https://stackoverflow.com/a/52389314/1558430) in another terminal.
* If you see [`Devtools is not supported yet, please remove the related dependency for now.`](https://stackoverflow.com/questions/70206109/org-springframework-aot-codegenerationexception-could-not-generate-spring-facto), uh, you can either remove it from `build.gradle`/`pom.xml`, or [disable Spring Native / AOT](https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/). [Devtools enables hot swapping / reloading](https://stackoverflow.com/questions/43129647/intellij-idea-spring-boot-hot-reload-on-manual-save), and AOT takes a long time to compile.
* You can supposedly [make IntelliJ auto-reload](https://stackoverflow.com/questions/43129647/intellij-idea-spring-boot-hot-reload-on-manual-save), too.
* [`@RequestMapping`](https://www.baeldung.com/spring-requestmapping) can be put on a class or method. Or maybe a field too, because that's what Copilot says, but who knows.
* `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, and `@PatchMapping` are just shorthands for `@RequestMapping(method = RequestMethod.VERB)`.

## Dependency Injection and the Spring Context

* In Spring's context, inversion of control means you get the thing you want, directly, without worrying about its dependencies, because they will be injected for you. "This is the beauty of IoC and DI. Components are only responsible for their own dependencies. They don't need to know any instantiation details. This avoids refactoring when dependencies change. It also avoids creating leaky abstractions while creating a very pleasant separation of concerns." - Internal quote
* [`@Autowired private FooFormatter fooFormatter;`](https://www.baeldung.com/spring-autowire) means a copy of `FooFormatter` (a registered component) is created for you, for your class to use. Arguments? Not sure. The `"fooFormatter"` in `@Component("fooFormatter")` is actually a qualifier; if you have multiple classes that implement the autowired interface (`FooFormatter`), you can use the qualifier (i.e. `@Qualifier("fooFormatter")`) to specify which one to inject.
* ["Constructor injection (...) is actually recommended over field injection"](https://stackoverflow.com/a/40620318/1558430): [An `@Inject` annotation over a constructor ensures you cannot create a class in a way that bypasses injection](https://odrotbohm.de/2013/11/why-field-injection-is-evil/). As an added advantage, your dependencies can be marked final, which is thread-safe. [Spring lets you do this by marking a `@Component`'s constructor with `@Autowired`](https://www.baeldung.com/constructor-injection-in-spring), and "As of Spring 4.3, classes with a single constructor can omit the `@Autowired` annotation".
* [Eager initialisation, which is default, helps spot problems with beans early on](https://howtodoinjava.com/spring5/core/spring-bean-eager-vs-lazy-init/). With [`@Lazy` initialisation](https://howtodoinjava.com/spring5/core/spring-bean-eager-vs-lazy-init/), beans are created when you `.getBean()` them, which may be faster if you have a large application.
* In Spring, the BeanFactory is the container that manages all the dependencies (Beans) in the application.

## Project Configuration

* `pom.xml` is for Maven. `build.gradle` is for Gradle.
* You use start.spring.io because it unifies the versions of dependencies that you use across multiple microservices.
* Some guy [says](https://www.youtube.com/watch?v=bB-xAYpeVL8) that [autoconfiguration](https://www.baeldung.com/spring-boot-custom-auto-configuration) is better than manually injecting or intercepting requests (?). The two links say different things, so there's more to look into.

## Actuators

* [Actuator](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#actuator) is a spring module for production-ready features. It contains endpoints that let you manage the health of the application, e.g. `/actuator/health` and `/actuator/prometheus`.

## Persistence and Data Access

* DTOs (Data Transfer Objects) *are* Entities.
* DTOs can have [field-level validation annotations](https://www.javaguides.net/2021/04/spring-boot-dto-validation-example.html), like `@NotEmpty`, `@Max`, or `@Email`. If you need more validation, write custom validation code.

## Spring MVC

## Templating engines

## REST APIs with Spring

* [Serialisers](https://www.baeldung.com/spring-boot-jsoncomponent) do exist in Spring. But if you want to both serialise and deserialise something, you need to make yourself a `@JsonComponent` class that contains a `public static class Serializer<T>`, and a `public static class Deserializer<T>`.
* [Use](https://www.youtube.com/watch?v=bB-xAYpeVL8) the OpenAPI specification when you create a new API.

## Events and Listeners

## Reactive Spring (Spring 5+)

* [Reactive calls don't wait for I/O](https://www.youtube.com/watch?v=bB-xAYpeVL8)? And therefore reduces idle time?
