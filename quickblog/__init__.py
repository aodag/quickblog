from pyramid.config import Configurator
import sqlahelper
from sqlalchemy import engine_from_config

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings)
    sqlahelper.add_engine(engine)
    config = Configurator(settings=settings)
    config.include('.fainit')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
