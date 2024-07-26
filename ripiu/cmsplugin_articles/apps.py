from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ArticlesConfig(AppConfig):
    name = 'ripiu.cmsplugin_articles'
    verbose_name = _('Articles and sections')
