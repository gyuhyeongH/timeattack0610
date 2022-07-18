from django.contrib import admin
from django.urls import path

from . import views


app_name ='product'
urlpatterns = [
    path('list', views.categorize_product, name='list'),
    path('list/<str:category_name>', views.categorize_product, name='list'),

    path('<int:id>/<str:product_name>', views.product_detail, name='product_detail'),

    # product_order
    path('order', views.product_order, name='product_order')

]