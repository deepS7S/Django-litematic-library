import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_image_size(value):
    """Проверка размера изображения (не более 1MB)"""
    filesize = value.size
    limit_mb = 1
    if filesize > limit_mb * 1024 * 1024:
        raise ValidationError(
            _('Максимальный размер изображения %(limit_mb)s MB. Текущий размер: %(size).2f MB'),
            params={'limit_mb': limit_mb, 'size': filesize / (1024 * 1024)},
        )

def validate_schematic_size(value):
    """Проверка размера файла схемы (не более 20MB)"""
    filesize = value.size
    limit_mb = 20
    if filesize > limit_mb * 1024 * 1024:
        raise ValidationError(
            _('Максимальный размер файла схемы %(limit_mb)s MB. Текущий размер: %(size).2f MB'),
            params={'limit_mb': limit_mb, 'size': filesize / (1024 * 1024)},
        )

def validate_image_extension(value):
    """Проверка расширения изображения"""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp']
    if not ext in valid_extensions:
        raise ValidationError(
            _('Неподдерживаемый формат изображения. Поддерживаются: %(extensions)s'),
            params={'extensions': ', '.join(valid_extensions)},
        )

def validate_schematic_extension(value):
    """Проверка расширения файла схемы"""
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.litematic']
    if not ext in valid_extensions:
        raise ValidationError(
            _('Неподдерживаемый формат файла схемы. Поддерживаются: %(extensions)s'),
            params={'extensions': ', '.join(valid_extensions)},
        )