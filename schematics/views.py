from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.views import View
from .models import Schematic, Author
from .forms import SchematicForm, AuthorForm

# Grid-вывод всех схем
class SchematicListView(ListView):
    model = Schematic
    template_name = 'schematics/schematic_list.html'
    context_object_name = 'schematics'
    paginate_by = 12

# Добавление схемы
class SchematicCreateView(CreateView):
    model = Schematic
    form_class = SchematicForm
    template_name = 'schematics/schematic_form.html'
    success_url = reverse_lazy('schematic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить схему'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Схема успешно добавлена!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{error}')
        return super().form_invalid(form)

# Изменение схемы
class SchematicUpdateView(UpdateView):
    model = Schematic
    form_class = SchematicForm
    template_name = 'schematics/schematic_form.html'
    success_url = reverse_lazy('schematic_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать схему'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Схема успешно обновлена!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f'{error}')
        return super().form_invalid(form)

# Удаление схемы
class SchematicDeleteView(DeleteView):
    model = Schematic
    template_name = 'schematics/schematic_confirm_delete.html'
    success_url = reverse_lazy('schematic_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Схема успешно удалена!')
        return super().delete(request, *args, **kwargs)

# Детальный просмотр
def schematic_detail(request, pk):
    schematic = get_object_or_404(Schematic, pk=pk)
    return render(request, 'schematics/schematic_detail.html', {'schematic': schematic})

# Список авторов
class AuthorListView(ListView):
    model = Author
    template_name = 'schematics/author_list.html'
    context_object_name = 'authors'
    paginate_by = 20

# Создание автора
class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'schematics/author_form.html'
    success_url = reverse_lazy('author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить автора'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Автор успешно добавлен!')
        return super().form_valid(form)

# Редактирование автора
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'schematics/author_form.html'
    success_url = reverse_lazy('author_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать автора'
        return context
    
    def form_valid(self, form):
        messages.success(self.request, 'Автор успешно обновлен!')
        return super().form_valid(form)

# Удаление автора
class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'schematics/author_confirm_delete.html'
    success_url = reverse_lazy('author_list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Автор успешно удален!')
        return super().delete(request, *args, **kwargs)