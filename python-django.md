# Django tips

## Models

- Once you set a primary key on something, it can't really be changed if a foreign key references it (and it applies to any constrained FK field in RDBMS in general, not just Django): `update or delete on table "foo_foo" violates foreign key constraint "bar_bar_foo_id_b6840f2a_fk_foo_foo_id" on table "bar_bar" ... DETAIL:  Key (id)=(1) is still referenced from table "bar_bar".`
- MongoDB [officially](https://code.djangoproject.com/wiki/NoSqlSupport) recommends [Djongo](https://github.com/nesdis/djongo) as the Mongo(NoSQL) adapter.
- `Model(id)` is NOT the same as `Model.objects.get(id=id)`. You can save the object from `Model.objects.get(id=id)`, but not `Model(id)`: `ValidationError: {u'id': [u'Model with this ID already exists.']}`. [`Model(id)` is undocumented](https://docs.djangoproject.com/en/2.1/ref/models/instances/#django.db.models.Model) and should never be used.
- Every `<Model>.objects` is just a [subclass of] `models.Manager()`. And you can extend `models.Manager`. Make your own `objects` by subclassing it.
- [Django never stores timezones in the database.](https://docs.djangoproject.com/en/1.8/topics/i18n/timezones/) The `USE_TZ` setting is only good for converting these UTC times to the site user's local time.
- To filter by any django model field, use the [`DjangoFilterBackend`](http://stackoverflow.com/a/2137652)
- All unsaved models (`pk=None`) of the same type hash to the same thing, because it is technically correct. Do not store them in a `set` -- they will just go away.
- When you change a DB field to a computed field (`@property`), you can specify `db_field` to keep it pointing to the original column name: http://stackoverflow.com/a/12358707/1558430
- Model field defaults can be a callable (function), but the function takes in nothing, so it is really only good for dates and times.
- Instead of making another Query just to fetch the same object again, there already is an [`obj.refresh_from_db()`](https://docs.djangoproject.com/en/1.9/ref/models/instances/#django.db.models.Model.refresh_from_db) available.
- Queries can accept [`Variable` instances](https://lincolnloop.com/blog/faster-django-sites-pypy/) where values normally go, so that these queries can be precompiled (and later inserted using `.bind()`). You know, for rare cases when a query takes longer to generate than it takes to run.
- "Repeatedly getting a certain index in a queryset" is not cached. Unless you evaluate the entire queryset, in which case, it is.
- [`blank=True` is required if you don't want a `ManyToManyField` to be required?](https://stackoverflow.com/a/2529875/1558430)
- If you are smart enough to use `.save(update_fields=['foo'])`, [be smart enough to know](https://code.djangoproject.com/ticket/22981) that `auto_now[_add]` fields will be updated only if they are specified in `update_fields`.
- Can't have `__getattr__` in django models.
- The difference between `get_user_model()` and `settings.AUTH_USER_MODEL` is, well, the latter is a string. (Being a string is still useful in situations where the actual model is not needed, like a foreign key reference, or type hinting.)
- You cannot write a `unique_together` based on foreign key values, because [`unique_together` maps directly to columns](https://stackoverflow.com/a/4440189/1558430).
- `manage.py sqlmigrate` lets you see what queries a (schema) migration will run.
- [Signals are synchronous and blocking](http://www.slideshare.net/flywindy/two-scoops-ofdjangologgingandsignals).
- First you migrate, then you load fixtures. It is not strictly enforced, but in order to have a database set up, you must first run `migrate` to get your tables, so you should just stick to it.
- Django does not support [ENUM](https://www.postgresql.org/docs/9.1/datatype-enum.html) types.
- [Deconstruction](https://docs.djangoproject.com/en/2.2/howto/custom-model-fields/#field-deconstruction), as far as Django fields are concerned, is the _opposite of construction_, or: how to turn a field instance into arguments that, when used to call `SomeField.__init__`, to recreate the field instance with the same values. (The other word choice is "Destruction".)

### `ForeignKey`

- Simply making a [`ForeignKey('self')`](https://stackoverflow.com/questions/15285626/django-self-referential-foreign-key) will make a foreign key to self.
- If a class A has a `ForeignKey` to class B with `on_delete=CASCADE`, B does not get deleted when A is deleted, but if B is deleted, then A is.
- `PROTECT` in `FK(foo, on_delete=PROTECT)` is supposed to mean "if you want to delete that foo, you must first delete every object referencing it".
- `OneToOneField` is a subclass of `ForeignKey`, so the schema _should not_ change if you change between the two.
- There wasn't a real reason for handling cascade deletes in Django (code) rather than the DB (data) other than that [it happened](https://stackoverflow.com/a/32793838/1558430).
- [Abstract `related_name` can contain string substitutes](https://docs.djangoproject.com/en/dev/topics/db/models/#be-careful-with-related-name-and-related-query-name) like `%(class)s` (the class name of a subclassed model) and `%(app_label)s` (the app of the subclassed model).

### [`blank=True` or `null=True`](http://stackoverflow.com/a/8609425)?

Usually, both. `blank=True` makes Django allow None, while `null=True` makes the database tolerate `NULL`.

`null=True` is not required for `TEXT` or `CHAR` fields.

### [`SeparateDatabaseAndState`](https://docs.djangoproject.com/en/2.2/ref/migration-operations/#separatedatabaseandstate)

`SeparateDatabaseAndState` actually isn't that mysterious.

Inside a `SeparateDatabaseAndState`, `database_operations` are the SQL statements that the migration makes, while `state_operations` are the things that Django thinks changed before and after this migration.

So if you were to have an autodetected migration that looks like:

    class Migration(migrations.Migration):

        operations = [
            migrations.AddField(...),
        ]

and you want to run SQL _different from what Django would run to add that field_, you can do

    class Migration(migrations.Migration):

        database_operations = [
            migrations.RunSQL(sql='DROP TABLE...', reverse_sql='DROP TABLE ANYWAY...')
        ]

        state_operations = [
            migrations.AddField(...),
        ]

        operations = [
            migrations.SeparateDatabaseAndState(
                database_operations=database_operations,
                state_operations=state_operations),
        ]

Now, when this migration is run, it drops a table instead of creating a new column, all while thinking that the migration results in the desired schema.

### Querying models

- If you filter by `id__in=queryset`, Django might make it a subquery. But if you do `id__in=list(queryset)`, no matter the size of the queryset, the queryset must be evaluated first, and the two-query version might be faster than the subquery version.
- It is possible to filter by a date field's component, like `.filter(date__day=10) # Look for dates on the 10th`.
- Specifying multiple identical query conditions do not cancel previous ones out. `Car.objects.filter(price__gt=100).filter(price__gt=0)` will still build a query similar to `SELECT * FROM tblCar WHERE price > 100 AND price > 0`.
- [`.exclude()`](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#django.db.models.query.QuerySet.exclude) generates a `WHERE NOT (conditions)` query rather than flipping those conditions in the code (e.g. `gt` to `<=`).
- The `QuerySet` is a monad. You can call `prefetch_related` and `select_related` in either order and it won't care. (It does care about double splicing and double ordering, however.)
- [`count()` is faster](http://stackoverflow.com/questions/14327036/count-vs-len-on-a-django-queryset) if all you need is a length; `len()` is faster if you already have the whole queryset already evaluated (for instance, when you actually use the whole set in a loop). With that said, the SQL `COUNT()` is very slow when you reach millions of rows, so [find some other way to do it](https://medium.com/squad-engineering/estimated-counts-for-faster-django-admin-change-list-963cbf43683e).
- Django 1.8 apparently lets you aggregate by an expression now, e.g. `.aggregate(Min('price') + 1)`
- [`QuerySet.iterator()`](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#django.db.models.query.QuerySet.iterator) does exactly that: make a queryset that _does not cache_ to save memory. Every call to loop the `.iterator()` will cause it to execute queries.
- To [aggregate by a field whose `related_name` is `+`](http://stackoverflow.com/questions/38576912/django-aggregate-by-field-with-no-related-name), try something clever: `Reward.objects.values('user').annotate(rewards_count=Count('id')).order_by()`, or [override a model's definition using a mirror class](http://stackoverflow.com/a/38583862/1558430) whose `Meta.managed` is `False`.
- It is [completely possible](https://github.com/django/django/blob/428c0bbe1bcd303560d7e96d7d2721ff3fdc0e3f/django/db/models/expressions.py#L155) to filter by an `F('time_field') + timedelta(seconds=???)`. It is also possible to query by another numeric field, and then treating it as a number of seconds, in the form of `.filter(...__gt/lt=F('some_other_field') * timedelta(seconds=1))`.
- Annotating a query with an [`ExpressionWrapper` field](http://stackoverflow.com/a/40618185/1558430) allows queries to be built using a result of some multi-field computation, which you normally cannot.
- Django 1.9 now has a [`Now()`](https://docs.djangoproject.com/en/1.10/ref/models/database-functions/#now) you can use to `filter(field__lt=Now())`. If the two servers have the same timestamp at the same time, using this and whatever from `datetime` have no functional difference.
- You might have to use the related name of the actual thing you want to count, rather than the thing itself, like `Foo.objects.annotate(d=Count('related_key')).order_by('-d').values_list('d') # Usually the one you want`
- Prefetching with `get_object_or_404` is possible with something like `get_object_or_404(Thing.prefetch_related(), id=4)`.
- [Django-pandas](https://github.com/chrisdev/django-pandas/) does exactly what you think it'd do: convert a queryset into a dataframe. Basically, you are working with tables.
- It is [not possible](https://stackoverflow.com/questions/21439031/django-f-expressions-joined-field?lq=1) to write an update statement based on `F(a__nested__field)`.
- `shell_plus` has a [`shell_plus --print-sql`](https://stackoverflow.com/a/31450706/1558430) option, which allows you to steal the query from an update().
- You can't `.first().values_list(...)` (because `.first()` converts the thing into an instance), but you can `.values_list(...).first()`.
- Like the name almost suggests, `defer('a', 'b', 'c')` fetches all columns except a, b, and c. And like the name suggests, `only('a', 'b', 'c')` only fetches columns a, b, and c. The `related__name` syntax is also supported.
- If you `annotate(a='foo__bar__baz')` a queryset that evaluates to objects (i.e. the default kind of queryset), then each object gets an attribute `a`.
- It is possible to map-annotate a (one or many)-to-many relationship using `annotate(singular_relation=F('plurals_relation'))`; each object gets at most one plurals relation annotated.
- In an M2M field, it doesn't matter how many things you have there... if you do `print(foo.bars)` instead of `print(foo.bars.all())`, it's always going to print `Bar.None`.
- To order a queryset's related fields (like if you are querying users and their products, with products sorted by name), do a `Prefetch()` on those products, with `queryset=` being an ordered set of products.
- Filtering by `Q()` does nothing, *except* if `|`ed with another `Q()`... so `Q() | Q(foo=1)` is the exact same as `Q() & Q(foo=1)`, because ["the empty Q() should not have any effect at all, whether ORed or ANDed into the query"](https://code.djangoproject.com/ticket/24279).

#### Don't know what `select_related` and `prefetch_related` do

According to onymous internet sources,

`select_related`

For foreign key & one-to-one relationships

If your query only retrieves a `values()` or `values_list` from a relation or annotated value (e.g. `values_list('foo__bar__baz')`), there is no need to `select_related` that field.

`prefetch_related`

For many-to-many, many-to-one, and generic foreign keys (i.e. whenever it isn't easy to do an inner join).

#### Queries do crazy things when executed in parallel

Use `@transaction.atomic`.

##### Django dies when using `@transaction.atomic`

> **Avoid catching exceptions inside atomic!** This is mostly a concern for `DatabaseError` and its subclasses such as `IntegrityError`. The correct way [is to catch the exception outside the atomic block].

#### Queries do crazy things even when executed in atomic blocks

Use `QuerySet.select_for_update(nowait=bool).filter(...)` in conjunction with `@transaction.atomic`.

All tables read by that `filter()` will be locked and be exclusive to this queryset until the atomic block is done.

**WARNING** [`select_for_update()` row locks are very aggressive](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#select-for-update). The `@transaction.atomic` around the statement must terminate as early as possible.

#### `__in` queries don't preserve order

i.e. `Foo.objects.filter(id__in=[1,2,3])` doesn't necessarily give you `Foo(id=1)`, `Foo(id=2)`, `Foo(id=3)`, in that order.

Use [`in_bulk`](https://docs.djangoproject.com/en/1.8/ref/models/querysets/#in-bulk) instead, which is also unordered, but at least returns a `dict` so you can re-order it to your liking back to a `list`.

#### Filtering by how many other foreign keys an object has

Annotate with the count of the foreign key, then filter on the annotation.

```
from django.db.models import Count, Q
Content.objects.annotate(tp=Count('tagged_products')).filter(tp__gte=3)
```

#### Group by how many rows have a certain value in a column

```
>>> Product.objects.values('shop_id').annotate(products=Count('shop_id')).order_by()
<QuerySet [{'shop_id': 1, 'products': 1023870}, {'shop_id': 4, 'products': 130}]>
```

[`values()`, `annotate()`, and `order_by()` must go in that exact order.](https://stackoverflow.com/a/19102493/1558430)

#### Filtering by `foo__in([1, 2,3, None])` not working

[Apparently you can't?](https://stackoverflow.com/a/15366686/1558430) You need to filter the None separately.

```
.filter(Q(foo__isnull=True) | Q(foo__in=[1, 2, 3]))
```

#### Cleaning up your mess after an outer join

```
qs.distinct()
```

, bearing in mind that calling `prefetch_related` multiple times on the same queryset makes those prefetch calls multiple times.

### Migrations

#### I want to reset all my migrations by [deleting and recreating them](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html), but `makemigrations` isn't doing anything

You can't delete the `migrations/__init__.py`s in your apps. Keep those files, then run `makemigrations` again.

#### `ALTER TABLE`-type migrations kill my app

Any migration that needs some kind of lock on a table will kill django's connections to the database.

If you want to alter a table (like for real, not just `help_text` on a field), you need to find ways to do so without adding a lock. For postgres, consider strategies like [adding an index concurrently](https://stackoverflow.com/a/42704241/1558430).

Note that a `CREATE INDEX CONCURRENTLY` index will still block the migration itself. It is not asynchronous.

#### `AttributeError: module 're' has no attribute 'RegexFlag'`

Did you know? Creating a migration with `all(`in Django, with one of the fields using `RegexValidator`, which has at least one flag, while running python3.6`)` will result in a migration file that says

    validators=[RegexValidator('^ ... $', flags=2)]

rather than

    validators=[RegexValidator('^ ... $', flags=re.RegexFlag(2))]

But `re.RegexFlag` was added in python3.6, so you cannot run this migration in python3.5 anymore.

Just replace `re.RegexFlag(...)` with the number inside (in this case, `2`).

#### My project has too many migrations that touch other apps so they can't be squashed automatically

Well don't make so many apps in the project. You did it to yourself, mate.

[Don't put everything in a single app, either](https://hackernoon.com/0-100-in-django-starting-an-app-the-right-way-badd141ef439). If possible, assess whether you have hit the size limit for your project, i.e. make a new project.

## Views / Templating

- [Django does not force you to put code at some specific place](http://stackoverflow.com/a/8590943/1558430). With that said, since MVC requires a service abstraction layer between M and C, which hardly anyone ever has, Django tends to recommend logic in either V or [M](http://stackoverflow.com/a/8591009/1558430), depending on whether the logic concerns requests.
- the `django_js` tag cannot be compressed!
- To override a template that is defined in a package, configure your `TEMPLATE_DIRS` variable to let your own `templates` directory have a higher lookup priority.
- Adding `{{ block.super }}` inside a block retains whatever was in the block in the parent template.
- [assignment tags](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/#assignment-tags): `some_assignment_tag param1 param2 param3... as variable_you_can_use_below`
- Template rendering is apparently [multi-threaded](https://docs.djangoproject.com/en/1.7/howto/custom-template-tags/#thread-safety-considerations).
- The result of calling `build_absolute_uri()` on a fake Request gives you `http://testserver/(...)`.
- [Generic model serializer](http://ihackernews.com/comments/8971480)
- [`authenticate()`](https://docs.djangoproject.com/en/1.6/topics/auth/default/#django.contrib.auth.authenticate) checks the credentials; `login()` actually logs the user in.
- The act of initialising a `QueryDict` [already parses the query string](https://docs.djangoproject.com/en/1.7/ref/request-response/#django.http.QueryDict.__init__). There is no need to use urlparse.
- Expressions in `blocktrans {{ this thing }} endblocktrans` [must not have attribute/key access](http://stackoverflow.com/questions/11338098/why-in-i18n-blocktrans-django-a-object-dict-or-list-dont-work).
- Doing a format with `ugettext` works [if you `.format()` the proxy object](https://stackoverflow.com/a/11001193/1558430), i.e. `ugettext_lazy('{foo}').format(foo='bar')`, rather than `ugettext_lazy('{foo}'.format(foo='bar'))`. So you don't actually need to stick with the `_(...) % (...)` operator.
- You can do [`.values()` or `,values_list()` expressions](https://docs.djangoproject.com/en/1.11/ref/models/querysets/#values-list), e.g. `Entry.objects.values_list('id', Lower('headline'))`.
- Translated string substitutionss (e.g. `_('hello %(world)s')`) must be named because you don't necessarily want all languages to have those translations in the same order.
- The closest thing nodejs has to Django templates is [swig](https://github.com/paularmstrong/swig), but it is discontinued.
- There's a [`django.template.Template`](https://github.com/django/django/blob/97e637a87fb45c4de970cca6cb783d93473c9d15/django/template/base.py#L141), and then there's a [`django.template.backends.django.Template`](https://github.com/django/django/blob/b9cf764be62e77b4777b3a75ec256f6209a57671/django/template/backends/django.py#L48), with the latter being a backend for the former.
- Rest framework's `Response` has inheritance of `Response -> django.template.response.SimpleTemplateResponse -> django.http.HttpResponse`. Django's built-in `JsonResponse` has inheritance of `JsonResponse -> django.http.HttpResponse`.
- Django class-based views have a `as_view()` method that turns the class into a function (more or less). It is decorated by an in-house [`@classonlymethod` decorator](https://stackoverflow.com/questions/8133312/what-is-the-difference-between-django-classonlymethod-and-python-classmethod), which makes `as_view` callable only in a class, but not in any of its instances. As for what `as_view()` does to convert the class into a function: [it's just a dispatcher](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html) that diverts the request to the class's `get`, `post`, and whatever else methods, depending on the request's type.
- You always avoid translating variables (i.e. `_(variable)`) because [`makemessages` won't detect them](https://docs.djangoproject.com/en/2.2/topics/i18n/translation/#standard-translation).
- [`MIDDLEWARE_CLASSES` got deprecated in 1.10; it is `MIDDLEWARE` now](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-MIDDLEWARE). The major difference is: `MIDDLEWARE_CLASSES` short-circuits to a 500 if a middleware throws an exception, while for `MIDDLEWARE`, all subsequent middlewares see a 500 response.
- You `makemessages` only when you have a `locale` folder. If you don't have a locale folder, Django gives you junk, half-translated files everywhere.

### got only `30` from a URL like `?foo=10&foo=20&foo=30`

Conventional wisdom tells us `request.GET.get('foo')` would get us whatever `foo` is, which is, by default, the last `foo`.

To get all the values instead, use `request.GET.getlist('foo')`, which is `['10', '20', '30']`.

### `{{ form.as_table }}` Doesn't return table markup?

Sometimes (but not according to the docs), unless you wrap all that in `<table>` tags, the form will render as line-broken strings:

```
<table>
{{ form.as_table }}
</table>
```

## REST Framework

- A `Serializer` can validate `request.query_params` (especially query strings that have repeated keys), but once you convert the query params to a `dict`, it cannot do the same thing anymore.

## Testing

- Giving any `TestCase` a `fixtures` list attribute automatically loads these fixtures whenever the tests are run.

## Admin

- [`./manage.py runscript`](http://django-extensions.readthedocs.org/en/latest/runscript.html) is exactly what ought to be done in place of where you used to code your management commands.
- [`prop.boolean = True`](http://stackoverflow.com/questions/12842095/how-to-display-a-boolean-property-in-the-django-admin) in django admin turns the display of that method into a checkbox, rather than just saying 'True'.
- The Django admin lists fields in the order the fields themselves are declared in your models file. For example, `class Foo: bar = ..., baz = ...` actually shows `bar` before `baz` in the admin.
- [`list_filter` can contain `admin.(...)Filter`s](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/), not just field names.
- An admin page's `short_description` will show only for instance methods.

## WSGI

To run Django under something other than `runserver`, `uWSGI` is preferred. To get the library, run:

```
pip install uwsgi  # requires reboot
```

### urlconf: `urlconf_module, app_name, namespace = arg ... ValueError: need more than 1 value to unpack`

Only Django 1.7 and up accepts plain lists for `include()`. Lower versions of django must wrap their urls in a `patterns('', ...)` first.

# Django troubleshooting

### Migrating a migration that was previously faked

`MigrationHistory.objects.get(app_name="your_app_name", migration="0001_whatever_filename").delete()`

### Failed to migrate models in two apps in the same project that impose foreign key constraints

Try to mark (after the fact, unfortunately) the schema migration that has a schema migration dependency with the [`depends_on` keyword][readthedocs].

### Doing a data migration that needs access to the model class

It is possible that your model has changed (e.g. somebody added new field).
Instead of `from app.models import Foo`, you might need to use [`Foo = apps.get_model('app', 'Foo')`](https://realpython.com/blog/python/data-migrations/) to get the _historical_ model, which might avoid any issues that may arise.

## Base models storing common fields

Add a `class Meta` that contains `abstract = True`.

This has a downside of no longer allowing the class to be referenced (as foreign keys) directly.

### `RelatedObjectDoesNotExist` when you try to access an attribute by `related_name`

Well, here's where Django suddenly decides to conform to `hasattr()`.

```
>>> foo.ratings
RelatedObjectDoesNotExist: Foo has no ratings.
>>> getattr(foo, 'ratings')
RelatedObjectDoesNotExist: Foo has no ratings.
>>> hasattr(foo, 'ratings')
False  # foo has no ratings
```

## Misc

- [Adrian Holovaty](http://www.holovaty.com/) added the line ["Thanks for checking it out."](https://github.com/django/django/commit/226acf35c84b379aa2e3c3b4672c18c61e3a8114) to the django/django repo.
- [Bumping the cache version](https://docs.djangoproject.com/en/2.1/topics/cache/#cache-versioning) helps with situations where two Django deployments run side by side, but only one deployment understands a "new" version of the cache, for example: a python2 deployment cannot understand cached objects pickled by python3.
- A free security check is available at `manage.py check --deploy`.

### Django signals (e.g. `post_save`, `m2m_changed`, ...) not working

The file you have these hooks must be touched by python at least once... try importing these hooks from a file that you know django uses. (The imports don't need to be used)

### Fixtures won't load

[`contenttypes` and `permission` are the culprits](http://stackoverflow.com/questions/853796/problems-with-contenttypes-when-loading-a-fixture-in-django). Remove all of them from the fixture file (using a script or something), then re-run loaddata.

[readthedocs]: http://south.readthedocs.org/en/latest/dependencies.html

### Can't dump fixtures through `call_command`

You need to [change the stdout to a `StringIO()`](https://stackoverflow.com/a/20480323/1558430) first.

### `class Meta` has nothing in it

Say for a normal python class `Foo(object)` containing another class `Bar(object)`, in which an attribute `baz = 1`, you access that attribute with `Foo.Bar.baz`, no problem.
But if you have a Django `Foo(Model)` with a class `Meta(object)` and `index_together = [...]` inside, you will find [this POS](https://stackoverflow.com/a/10344218/1558430): `AttributeError: class Meta has no attribute 'index_together'`
No worries though, [you can still find what you want in `Foo._meta.index_together`](https://stackoverflow.com/a/15395241/1558430).
