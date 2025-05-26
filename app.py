import urllib.parse as urlparse
from datetime import datetime, UTC
from logging import getLogger
from o3 import Config
from peewee import (DateTimeField,
                    Model,
                    CharField,
                    DatabaseProxy,
                    SqliteDatabase,
                    PostgresqlDatabase
                    )

from pypette import PyPette, redirect
from pypette import static_file


app = PyPette()

logger = getLogger(__name__)

config = Config()

database_proxy = DatabaseProxy()


def parse_connection_url(url):  # pragma: no cover
    logger.info("Connection: %s", url)
    parsed = urlparse.urlparse(url, scheme='sqlite')
    connect_kwargs = {'database': parsed.path[1:]}
    if parsed.username:
        connect_kwargs['user'] = parsed.username
    if parsed.password:
        connect_kwargs['password'] = parsed.password
    if parsed.hostname:
        connect_kwargs['host'] = parsed.hostname
    if parsed.port:
        connect_kwargs['port'] = parsed.port

    return parsed.scheme, connect_kwargs


def create_database():
    engine, kwargs = parse_connection_url(config.database_connection_url)
    if 'sqlite' in engine:
        database = SqliteDatabase(pragmas={'journal_mode': 'wal',
                                           'foreign_keys': 1},
                                  **kwargs)
    if 'postgres' in engine:  # pragma: no cover
        kwargs['user'] = config.postgres_user
        kwargs['password'] = config.postgres_password
        database = PostgresqlDatabase(**kwargs)

    return database


class BaseModel(Model):
    class Meta:
        database = database_proxy


class Cats(BaseModel):
    id = CharField(primary_key=True, max_length=36, null=False)
    answer = CharField(max_length=10, null=False)
    creation_time = DateTimeField(default=datetime.now(UTC), null=False, formats=["%Y-%m-%d %H:%M:%S.%f%z"])

    def __repr__(self):  # pragma: no cover
        return f"<Captcha {self.id}>"


@app.route("/static/:filename", method='GET')
def static(request, filename):
    rv = static_file(request, filename, 'static')
    return rv


@app.route('/')
def home(request):
    return redirect(request, '/image/1')


@app.route('/image/:image_id')
def show_image(request, image_id):

    image_id = int(image_id)
    if image_id < 1 or image_id > 5:
        return redirect(request, '/image/1')

    prev_id = image_id - 1 if image_id > 1 else 5
    next_id = image_id + 1 if image_id < 5 else 1
    numbers = range(1,6)
    return app.templates.load('base.tpl').render(locals())


def wsgi():
    """
    Return a wsgi app for usage with another framwork
    """
    database = create_database()
    database.connect()
    database_proxy.initialize(database)

    database.create_tables([Cats], safe=True)
    return app


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('', 8000, app)
    print("Serving on port 8000...")
    httpd.serve_forever()
