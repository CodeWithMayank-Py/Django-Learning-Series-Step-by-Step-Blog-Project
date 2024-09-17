from django.urls import path
from . import views
from .views import BlogListView

urlpatterns = [
    path("", views.index, name="index"),
    path("class/", BlogListView.as_view(), name="blogs"),
]
