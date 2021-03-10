from django.urls import path
from . import views
from .views import NoteDetailView,NoteUpdateView,NoteDeleteView

urlpatterns = [
    path('make/', views.make, name='make'),
    path('', views.home, name='home'),
    path('my-uploads/', views.uploads, name='upload'),
    path('<str:slug>/', views.detail, name='note-detail'),
    path('new/<str:category>/', views.create, name='note-create'),
    path('<slug:slug>/update/', NoteUpdateView.as_view(), name='note-update'),
    path('<slug:slug>/delete/', NoteDeleteView.as_view(), name='note-delete'),
]
