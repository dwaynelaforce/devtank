from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('about', views.about),
    path('message/<int:user_id>/inbox', views.inbox),
    path('add_project', views.add_project),
    path('create_project', views.create_project),
    # path('upload_proj_img/<int:project_id>', views.upload_proj_img),
    # path('add_project_img/<int:project_id>', views.add_project_img),
    path('delete_project/<int:project_id>', views.delete_project),
    path('projects/<int:project_id>', views.show_project),
    path('devs/<int:dev_id>', views.show_dev),
    path('edit_project/<int:project_id>', views.edit_project),
    path('add_to_watchlist/<int:project_id>', views.add_to_watchlist),
    path('remove_from_watchlist/<int:project_id>', views.remove_from_watchlist),
    path('category_search_button/<str:category>', views.category_search_button),
    path('new', views.new_chat),
    path('new_reply/<int:message_id>', views.new_reply),
    # path('search_db', views.SearchBar.as_view()),
    path('edit_profile_page/<int:user_id>', views.edit_profile_page),
    path('edit_profile/<int:user_id>', views.edit_profile),
    path('search_categories', views.search_categories),
    #path('get_categorys', views.get_categorys),
    path('logout', views.logout),
]