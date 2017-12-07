# -*- coding: utf-8 -*-
from django.conf import settings  # NOQA
from appconf import AppConf


class CmspluginFilerImageAppConf(AppConf):
    IMAGE_WIDTH = 1500
    IMAGE_HEIGHT = 1500
    IMAGE_CROP = True
    IMAGE_UPSCALE = True

    class Meta:
        prefix = 'ripiu_articles'
