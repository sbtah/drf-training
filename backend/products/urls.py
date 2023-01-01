from django.urls import path
from products import views


app_name = "products"


urlpatterns = [
    path("", views.product_list_view, name="product-list"),
    path("<int:pk>/", views.product_detail_view, name="product-detail"),
    path("<int:pk>/update/", views.product_update_view, name="product-update"),
    path("<int:pk>/delete/", views.product_delete_view, name="product-delete"),
    path("create/", views.product_create_view, name="product-create"),
]
