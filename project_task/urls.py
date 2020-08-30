from django.urls import path
from project_task.views import ProductList, ProductFilterByCategory

app_name = 'project_task'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('category/product/<int:pk>/', ProductFilterByCategory.as_view(),
         name='product_filter_category'),
    path('brand/product/<int:pk>/', ProductFilterByCategory.as_view(),
         name='product_filter_brand')
]
