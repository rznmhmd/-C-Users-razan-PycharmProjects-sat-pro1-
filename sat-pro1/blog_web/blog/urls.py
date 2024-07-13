from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    # other paths as needed
    path('categories/', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
]