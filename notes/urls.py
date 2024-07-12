from django.urls import path
from .views import UserCreateView, NoteListCreateView, NoteDetailView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user_create'),
    path('notes/', NoteListCreateView.as_view(), name='note_list_create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
]

