from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('poemas/crear/', views.register_poema, name='notes'),
    path('poemas/', views.get_notes, name='poems'),
    path('poemas/<int:poem_id>/', views.note_detail, name='notedetail'),
    path('notes/<int:note_id>/delete/', views.note_delete, name='note_delete'),
]