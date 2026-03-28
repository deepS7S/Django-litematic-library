from django.urls import path
from . import views

urlpatterns = [
    # Схемы
    path('', views.SchematicListView.as_view(), name='schematic_list'),
    path('add/', views.SchematicCreateView.as_view(), name='schematic_add'),
    path('<int:pk>/edit/', views.SchematicUpdateView.as_view(), name='schematic_edit'),
    path('<int:pk>/delete/', views.SchematicDeleteView.as_view(), name='schematic_delete'),
    path('<int:pk>/', views.schematic_detail, name='schematic_detail'),
    
    # Авторы
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='author_add'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]