
from django.urls import path
from .views import posts_list,post_detail
urlpatterns = [
    path('posts/',posts_list),
    path('posts/<int:id>/',post_detail)
]
