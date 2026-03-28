from django import forms
from .models import Schematic, Author

class SchematicForm(forms.ModelForm):
    
    clear_image = forms.BooleanField(
        required=False,
        label="Удалить текущее изображение (установить дефолтное)",
        help_text="Отметьте, чтобы удалить загруженное изображение и установить дефолтное"
    )
    clear_file = forms.BooleanField(
        required=False,
        label="Удалить текущий файл схемы",
        help_text="Отметьте, чтобы удалить загруженный файл схемы"
    )
    
    class Meta:
        model = Schematic
        fields = ['name', 'description', 'author', 'image', 'file_litematica']
        labels = {
            'name': 'Название схемы',
            'description': 'Описание',
            'author': 'Автор',
            'image': 'Изображение',
            'file_litematica': 'Файл схемы (.litematic)',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        
        if instance:
            if instance.image and instance.image.name != 'default_images/default_schematic.png':
                self.fields['image'].help_text = f'Текущее изображение: {instance.image.name} (размер: {self._get_file_size(instance.image)})'
            elif instance.image and instance.image.name == 'default_images/default_schematic.png':
                self.fields['image'].help_text = 'Установлено дефолтное изображение'
            if instance.file_litematica:
                self.fields['file_litematica'].help_text = f'Текущий файл: {instance.file_litematica.name} (размер: {self._get_file_size(instance.file_litematica)})'
    
    def _get_file_size(self, file_field):
        """Получить размер файла в читаемом формате"""
        if file_field and hasattr(file_field, 'size'):
            size = file_field.size
            if size < 1024:
                return f"{size} B"
            elif size < 1024 * 1024:
                return f"{size / 1024:.2f} KB"
            else:
                return f"{size / (1024 * 1024):.2f} MB"
        return "неизвестно"
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        if self.cleaned_data.get('clear_image'):
            if instance.image and instance.image.name != 'default_images/default_schematic.png':
                instance.image.delete(save=False)
            instance.image = 'default_images/default_schematic.png'
        
        if self.cleaned_data.get('clear_file'):
            if instance.file_litematica:
                instance.file_litematica.delete(save=False)
                instance.file_litematica = None
        
        if commit:
            instance.save()
            self.save_m2m()
        
        return instance

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {
            'name': 'Имя автора',
        }