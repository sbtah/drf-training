from django.urls import path
from search import views


app_name = "search"


urlpatterns = [
    path("", views.SearchListView.as_view(), name="search-list"),
]
