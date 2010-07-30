"""Setup the pylonsApp application"""
import logging

from pylonsapp.config.environment import load_environment
from pylonsapp.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup pylonsapp here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    meta.metadata.bind = meta.engine

    meta.metadata.create_all(checkfirst=True)

    log.info("Adding homepage...")

    # TODO 唯一性判断
    from pylonsapp.model import Page
    page = Page()
    page.title=u'Home Page'
    page.content = u'Welcome to the SimpleSite home page.'
    meta.Session.add(page)
    meta.Session.commit()
    log.info("Successfully set up.")

