from django.urls import path
from api import views 

#fbv
#urlpatterns = [
#   path('products/', views.products_list), 
#    path('products/<int:product_id>/', views.product_detail),
#]

#cbv, mixins
urlpatterns = [
 
   path('products/', views.ProductListAPIView.as_view()),
   path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
]

#generics
#urlpatterns = [
#   path('products/', views.ProductListAPIView.as_view()),
#   path('products/<int:product_id>/', views.ProductDetailAPIView.as_view()),
#    
#    path('categories/', views.CategoryListAPIView.as_view()),
#    path('categories/<int:category_id>/', views.CategoryDetailAPIView.as_view()),
    
    
#    path('categories/<int:category_id>/products/', views.CategoryProductsAPIView.as_view()),
#]
