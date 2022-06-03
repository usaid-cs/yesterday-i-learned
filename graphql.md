* In addition to features like smart caching, **federated graphs** (graphs that work with each other, somehow, and expose a single graphql endpoint) help reduce the number of API endpoints that your client needs to contact to get the data it needs. In effect, your client needs to contact just one API to use dozens of services. This makes client-side development easier, but deprecation of backend services harder.
* ["Connections"](https://www.apollographql.com/blog/graphql/explaining-graphql-connections/) are GraphQL's equivalent of connections.
* The entire thing you give the graphql server is called a *document*.
* `query` (read-only fetch) and `mutation` (write + fetch) are called [operations](https://spec.graphql.org/draft/#sec-Language.Operations). There is also a `subscription` (read from events).
* [*Fragments*](https://spec.graphql.org/draft/#sec-Language.Fragments) (`{ ...Fragment }`) lets you expand `Fragment` into that block, which looks like `fragment Fragment on Foo { fields }`.
* In Java fashion, [a `Vote` declaration allows both a `Vote` and `null`](https://stackoverflow.com/a/46771890/1558430). To force a `Vote`, use `Vote!`.
* `[Vote!]` means a 0~n list of `Vote`s, [*or `null`*](https://stackoverflow.com/a/46771890/1558430). If you want literally a list of `Vote`s, use `[Vote!]!`.
* There is [no way to validate the length of a list](https://stackoverflow.com/a/62192275/1558430), i.e. you can't write something that forces a 1-element list. Write that validation in your resolver instead.
* Every GraphQL document--query and mutation--ends up being a `POST` request, because [GET requests have a length limit](https://old.reddit.com/r/graphql/comments/ekzn86/why_does_graphql_only_take_http_post_for_requests/fdeo84g/), and `POST` doesn't have the same limitation.
* `foo: Boolean = true` [defaults](https://stackoverflow.com/a/51567429/1558430) that field to true if omitted.
