from django.db import models
from django.urls import reverse
from django.conf import settings
import os
from .validators import (
    validate_image_size, 
    validate_image_extension,
    validate_schematic_size,
    validate_schematic_extension
)

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Имя автора")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

class Schematic(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название схемы")
    description = models.TextField(blank=True, verbose_name="Описание")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='schematics', verbose_name="Автор")
    image = models.ImageField(
        upload_to='schematics/', 
        blank=True, 
        null=True, 
        verbose_name="Картинка схемы",
        validators=[validate_image_size, validate_image_extension]
    )
    file_litematica = models.FileField(
        upload_to='litematica_files/', 
        blank=True, 
        null=True, 
        verbose_name="Файл схемы",
        validators=[validate_schematic_size, validate_schematic_extension]
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def save(self, *args, **kwargs):
        """Если картинка не загружена, устанавливаем дефолтную"""
        if not self.image:
            default_image_path = 'default_images/default_schematic.png'
            full_default_path = os.path.join(settings.MEDIA_ROOT, default_image_path)
            
            if os.path.exists(full_default_path):
                self.image = default_image_path
            else:
                pass
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        if self.image and self.image.name != 'default_images/default_schematic.png':
            self.image.delete(save=False)
        if self.file_litematica:
            self.file_litematica.delete(save=False)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schematic_detail', args=[str(self.id)])

    class Meta:
        verbose_name = "Схема"
        verbose_name_plural = "Схемы"
        ordering = ['-created_at']