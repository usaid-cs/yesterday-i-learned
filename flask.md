1. To properly get messages from a flask app running on gunicorn, the command needs to be as such: `gunicorn project.file:app --log-file=- --log-level debug`
1. PyCharm understands gunicorn only after ["gevent compatible debugging"](http://stackoverflow.com/a/20738996/1558430) is enabled.
1. The view's function `__name__` *is* the view's name. This means a name cannot contain things like colons.
1. `url_for('foo.bar')` gives you the url for a view named `bar` in a [blueprint](http://flask.pocoo.org/docs/0.10/blueprints/) called `foo`.
1. Views can return just a string as the response.
1. [There are no nested blueprints](http://stackoverflow.com/questions/33003178/nested-blueprints-in-flask) (yet)
1. Flask SQLAlchemy creates only one `db.session`  that you can commit at any time.
1. Understand flask ["blueprints"](http://flask.pocoo.org/docs/0.12/blueprints/) as traits that are common across some of your views, like templates or url prefixes.