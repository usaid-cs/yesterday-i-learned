![It's Springtime!](https://i.imgur.com/n93DTMM.png)

## How to Basic

* To run the project: [`./gradlew bootRun` or `./mvnw spring-boot:run`](https://spring.io/guides/gs/spring-boot/). I use [`mvn spring-boot:run`](https://docs.spring.io/spring-boot/docs/1.5.16.RELEASE/reference/html/using-boot-running-your-application.html).
* To run the project with auto-reload, run [`./gradlew build --continuous`](https://stackoverflow.com/a/52389314/1558430) in another terminal.
* If you see [`Devtools is not supported yet, please remove the related dependency for now.`](https://stackoverflow.com/questions/70206109/org-springframework-aot-codegenerationexception-could-not-generate-spring-facto), uh, you can either remove it from `build.gradle`/`pom.xml`, or [disable Spring Native / AOT](https://docs.spring.io/spring-native/docs/current/reference/htmlsingle/). [Devtools enables hot swapping / reloading](https://stackoverflow.com/questions/43129647/intellij-idea-spring-boot-hot-reload-on-manual-save), and AOT takes a long time to compile.
* You can supposedly [make IntelliJ auto-reload](https://stackoverflow.com/questions/43129647/intellij-idea-spring-boot-hot-reload-on-manual-save), too.
* [`@RequestMapping`](https://www.baeldung.com/spring-requestmapping) can be put on a class or method. Or maybe a field too, because that's what Copilot says, but who knows.
* `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`, and `@PatchMapping` are just shorthands for `@RequestMapping(method = RequestMethod.VERB)`.
* The `@Slf4j` ("Simple Logging Facade 4 Java") annotation instantly gives you a [`private static final org.slf4j.Logger log`](https://stackoverflow.com/a/68964629/1558430) that you can use to log things.

### Spring Application Lifecycle

* "Initialisation" phase
    * Application context is created
    * Bean factory is initialised
        * Bean definitions are loaded
            * This can come from Java or XML (not preferred) configuration, or component scanning (auto-configuration)
            * The factory gets references to the loaded beans, but no objects have been instantiated at this point
        * Bean factory post-processing (BFPP)
            * We can still change the beans here, e.g. [`PropertySourcesPlaceholderConfigurer`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/context/support/PropertySourcesPlaceholderConfigurer.html), which resolves `${...}` placeholders within bean definition property values before the beans are created.
            * It is not common to write your own components to impact this behaviour, but you can do so here.
    * Beans are instantiated, from those having no dependencies, to those having the most dependencies (dep graph)
        * Beans are created eagerly by default, and even if you mark it as `@Lazy`, it'll be created if other eager beans need it
        * We call the setters on the bean
            * For the `@Autowired` fields (i.e. not constructors), Spring sets those beans now
            * Beans still aren't ready for use at this point
        * `BeanPostProcessor` Pre-init / Init / Post-init
            * We can configure the beans here if they still need to be configured
            * `@PostConstruct` methods called here
            * Beans are ready to use
* "Use" phase
* "Destruction" phase
    * The application context starts to close
    * `@PreDestroy` methods are called

### "Aspects"

* `@Aspect`s are reusable (DRY + separation of concerns) pieces of code that is injected into certain parts of the application at runtime. [A `@Pointcut` decides where the code is added, and `@Before` / `@Around` / `@After` decide what gets run](https://dev.to/jarjanazy/intro-to-spring-s-aspects-4pee).
* Spring provides an aspect called `@Transactional`, as well as aspects related to caching and logging.
* Basically, due to the lack of powerful decorators in Java, the Spring team made their own.

## Dependency Injection and the Spring Context

* In Spring's context, inversion of control means you get the thing you want, directly, without worrying about its dependencies, because they will be injected for you. "This is the beauty of IoC and DI. Components are only responsible for their own dependencies. They don't need to know any instantiation details. This avoids refactoring when dependencies change. It also avoids creating leaky abstractions while creating a very pleasant separation of concerns." - Internal quote
* [`@Autowired private FooFormatter fooFormatter;`](https://www.baeldung.com/spring-autowire) means a copy of `FooFormatter` (a registered component) is created for you, for your class to use. Arguments? Not sure. The `"fooFormatter"` in `@Component("fooFormatter")` is actually a qualifier; if you have multiple classes that implement the autowired interface (`FooFormatter`), you can use the qualifier (i.e. `@Qualifier("fooFormatter")`) to specify which one to inject.
* ["Constructor injection (...) is actually recommended over field injection"](https://stackoverflow.com/a/40620318/1558430): [An `@Inject` annotation over a constructor ensures you cannot create a class in a way that bypasses injection](https://odrotbohm.de/2013/11/why-field-injection-is-evil/). As an added advantage, your dependencies can be marked final, which is thread-safe. [Spring lets you do this by marking a `@Component`'s constructor with `@Autowired`](https://www.baeldung.com/constructor-injection-in-spring), and "As of Spring 4.3, classes with a single constructor can omit the `@Autowired` annotation".
* [Eager initialisation, which is default, helps spot problems with beans early on](https://howtodoinjava.com/spring5/core/spring-bean-eager-vs-lazy-init/). With [`@Lazy` initialisation](https://howtodoinjava.com/spring5/core/spring-bean-eager-vs-lazy-init/), beans are created when you `.getBean()` them, which may be faster if you have a large application.
* In Spring, the BeanFactory is the container that manages all the dependencies (Beans) in the application.
* `@Bean`-ing a method called `public Foo foo()` calls `foo()` every time you have an `@Autowired` thing somewhere that looks for a `Foo`.
* All beans are singletons by default. If you don't want that, e.g. you want a per-request bean, or a per-session bean: [configure your bean scope](https://docs.spring.io/spring-framework/docs/6.0.x/reference/html/core.html#beans-factory-scopes) using annotations like `@RequestScope` and `@SessionScope`. In particular, the `@PrototypeScope` gives you a new instance of the bean every time.
* If a `@Component` has only one constructor, and that constructor doesn't have the `@Autowired` annotation on it, Spring Boot will autowire those dependencies for you anyway, because you can't use that class otherwise. It is still best practice (probably) to put `@Autowired` there anyway.

### [Proxies](https://medium.com/javarevisited/spring-dependency-injection-demystified-part-1-proxying-7be4fa52bb6c)

[Proxies](https://medium.com/trabe/understanding-aop-in-spring-from-magic-to-proxies-6f5911e5e5a8) wrap all classes starting Spring 4.0. Behaviours will only be added to public methods; internal calls and private methods will not have proxying.

* Proxies supposedly [aren't that bad in performance](https://spring.io/blog/2007/07/19/debunking-myths-proxies-impact-performance/).

### Component Scanning

* Use `@Component` to indicate that the class should be loaded into the bean factory.
* `@Controller`, `@Service`, and `@Repository` are [stereotypes](https://www.baeldung.com/spring-component-annotation) of `@Component`: they behave the exact same way, just with different names for humans to look at.
* Spring Boot handles starting component scanning for you with the `@SpringBootApplication` annotation. Outside of Spring Boot, you can wrap your own thing manually with `@ComponentScan`.

## Project Configuration

* `pom.xml` is for Maven. `build.gradle` is for Gradle.
* You use start.spring.io because it unifies the versions of dependencies that you use across multiple microservices.
* Some guy [says](https://www.youtube.com/watch?v=bB-xAYpeVL8) that [autoconfiguration](https://www.baeldung.com/spring-boot-custom-auto-configuration) is better than manually injecting or intercepting requests (?). The two links say different things, so there's more to look into.
* The [`application.properties` file](https://www.javatpoint.com/spring-boot-properties) goes in `src/main/resources`. This folder is also where every other settings file goes.
* To [show SQL statements that Hibernate runs](https://stackoverflow.com/a/47441828/1558430), add `logging.level.org.hibernate.SQL=debug` and `logging.level.org.hibernate.type.descriptor.sql=trace` to `application.properties`. Or maybe [try this here](https://stackoverflow.com/questions/2536829/hibernate-show-real-sql).
* If a `@Configuration` class's `@Value(...)` field is not explicitly labelled `public`, it is not going to be accessible outside of the module's package. To allow that, make it public like it suggested.
* The `"${some.string}"` in `@Value("${some.string}")` is interpolated ("property references"), which means anything outside the `${}` is not interpolated. For example, `@Value("Foo")` really gives you the string `"Foo"`, nothing more.
* Adding `@Profile("!dev")` to a `@Bean` makes it not available when the profile name is `dev`. You can change the profile manually with `-Dspring.profiles.active=dev`. Remember there can be only one bean of each type at any given context (well, you can with `@Qualifier`, but close enough...), so `@Bean @Profile("dev") Foo foo1() {...}` combined with `@Bean @Profile("!dev") Foo foo2() {...}` allows you to swap which bean your app gets, depending on the environment variable.
* You can also use `#{ ... }` in interpolation. This is syntax for [spring expression language](https://www.baeldung.com/spring-expression-language)--yet another thing to remember because it's java--and you can do a bunch of stuff with it.

## Actuators

* [Actuator](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#actuator) is a spring module for production-ready features. It contains endpoints that let you manage the health of the application, e.g. `/actuator/health` and `/actuator/prometheus`.
* `POST`ing to `/actuator/loggers/(some logger)` with `{"configuredLevel": "TRACE", "effectiveLevel": "TRACE"}` will enable verbose logging for that logger, even if the default was not that. Updating the special [`/actuator/loggers/ROOT`](https://www.baeldung.com/spring-boot-changing-log-level-at-runtime) will turn logging to 11 globally.

## Persistence and Data Access

* The J in [JPA](https://en.wikipedia.org/wiki/Jakarta_Persistence) stands for [Jakarta](https://en.wikipedia.org/wiki/Jakarta_EE) (which itself is a renaming of "Java EE"), and the A stands for API.
* DTOs (Data Transfer Objects) *are* Entities.
* DTOs can have [field-level validation annotations](https://www.javaguides.net/2021/04/spring-boot-dto-validation-example.html), like `@NotEmpty`, `@Max`, or `@Email`. If you need more validation, write custom validation code.
* A `@Query()` (raw query) is SELECT-only by default. To run `INSERT`, `UPDATE` or `DELETE` statements, add [`@Modifying`](https://www.baeldung.com/spring-data-jpa-modifying-annotation#annotation) on top of it.
* The query inside `@Query` (e.g. `@Query("DELETE FROM TableName WHERE ...")`) uses the table's class name `TableName` instead of the name you define in `@Table(name = "table_name")`, because all of that is actually [JPQL](https://www.baeldung.com/spring-data-jpa-query#1-jpql) (Java Persistence Query language), instead of raw SQL. If you want to actually SQL, add `nativeQuery = true`.
* `deleteAll(entities)` literally runs [a `DELETE` query for each item](https://www.netsurfingzone.com/jpa/spring-data-jpa-deleteall-vs-deleteallinbatch/) you pass in.
* [`cascade = CascadeType.REMOVE`](https://www.objectdb.com/java/jpa/persistence/delete) acts like `models.CASCADE` in Django, where if you delete the current entity, the referenced entities are deleted as well.
* [OpenJPA suggests using `CascadeType.PERSIST` liberally](https://stackoverflow.com/a/13027330/1558430), i.e. if you save something, it will also try to save the related entity.
* [`CascadeType.REFRESH`](https://stackoverflow.com/questions/1403681/what-does-cascadetype-refresh-actually-do) is used when you load/reload an entity from the DB. Except for performance-critical circumstances, you will probably want its related entities to be refreshed, too.
* Model-level (`@Entity`) interaction is handled by [Hibernate](https://docs.jboss.org/hibernate/core/4.0/hem/en-US/html/listeners.html), not Spring itself.
* By default, [the table name in `@Column(name = "...")` will be converted to lower case](https://stackoverflow.com/questions/25283198/spring-boot-jpa-column-name-annotation-ignored) using the `SpringNamingStrategy`.

## Spring MVC

* To [return a JSON object in your Spring response](https://stackoverflow.com/questions/44839753/returning-json-object-as-response-in-spring-boot), *all you need to do* is constructing any kind of `Map` (probably `HashMap`), [`.put`ting values into it](https://stackoverflow.com/a/48063891/1558430), and then returning the map (if you claim to be returning `Map<K, V>`, that is).
* You might want to return `ResponseEntity<T>` in your controller methods because [it lets you control the status code and headers](https://www.baeldung.com/spring-response-entity) in addition to the body. To do so, you `return ResponseEntity.status(...).header(...).body(POJO)` (`.body` is always the last call that converts `BodyBuilder` to `ResponseEntity`).

## Templating engines

## REST APIs with Spring

* [Serialisers](https://www.baeldung.com/spring-boot-jsoncomponent) do exist in Spring. But if you want to both serialise and deserialise something, you need to make yourself a `@JsonComponent` class that contains a `public static class Serializer<T>`, and a `public static class Deserializer<T>`.
* [Use](https://www.youtube.com/watch?v=bB-xAYpeVL8) the OpenAPI specification when you create a new API.
* If you [put `spring.data.rest.base-path=api`](https://stackoverflow.com/questions/22024716/spring-data-rest-base-path), then the Spring-data-rest API you set up is exposed at `/api/` instead of `/`. [doc](https://docs.spring.io/spring-data/rest/docs/current/reference/html/#getting-started.boot)

## Events and Listeners

## Reactive Spring (Spring 5+)

* [Reactive calls don't wait for I/O](https://www.youtube.com/watch?v=bB-xAYpeVL8)? And therefore reduces idle time?

## Testing

* Your tests will fail with message "No qualifying bean of type `com.Foo` available" if you forget the `@MockBean Foo foo` inside it.
