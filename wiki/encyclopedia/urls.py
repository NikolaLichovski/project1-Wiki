from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("search", views.search, name="search"),
    path("wiki/<entry_name>", views.wiki, name="wiki"),
    # path("newPage", views.new_page, name="new_page"),
    path("randomPage", views.random_page, name="random_page")
]
