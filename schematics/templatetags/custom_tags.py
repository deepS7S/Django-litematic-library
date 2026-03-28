from django import template
from django.conf import settings
import os

register = template.Library()

@register.simple_tag
def default_image():
    """Возвращает путь к дефолтному изображению"""
    return os.path.join(settings.STATIC_URL, 'default_images/default_schematic.png')