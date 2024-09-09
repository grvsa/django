from django.urls import path
##from women.views import index, categories
from . import views ## удобнее так

urlpatterns = [
    path('cats/', views.categories),
    path('', views.index),
]