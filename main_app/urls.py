from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('about', views.about),
    # path('inbox/<int:user_id>', views.inbox),
    path('add_project', views.add_project),
    path('create_project', views.create_project),
    path('upload_proj_img', views.upload_proj_img),
    path('add_project_img/<int:project_id>', views.add_project_img),
    path('delete_project/<int:project_id>', views.delete_proj),
    path('projects/<int:project_id>', views.show_project),
    path('edit_project/<int:project_id>', views.edit_proj),
    # path('new_chat', views.new_chat),
    # path('new_reply', views.new_reply),
    path('logout', views.logout),
]