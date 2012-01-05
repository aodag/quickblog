from quickblog import models
import logging

log = logging.getLogger(__name__)


def includeme(config):
    settings = config.registry.settings.get('quickblog.fa_settings}}', {})

    # Example to add a specific model
    #config.formalchemy_model("/my_model", package='quickblog',
    #                         model='quickblog.models.MyModel')
    #                         **settings)

    log.info('quickblog.faroutes loaded')
