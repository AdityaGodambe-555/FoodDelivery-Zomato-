from django.urls import path
from productsapp import views

urlpatterns = [
    path('',views.home_page),
    path('dashboard/',views.dashboard),
    path('filter/',views.filter_by_typ),
    path('sort/',views.sort_by_price),
    path('range/', views.filterbyrange),
    path('category/', views.Category_food),
    path('search/', views.search),
]