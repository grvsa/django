from django.urls import path, re_path, register_converter
##from women.views import index, categories
from . import views ## удобнее так
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
##    path('cats/', views.categories),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('', views.index, name='home'),
#    re_path(r'^archive/(?P<year>[0-9]{4})/',views.archive),
    path('archive/<year4:year>/', views.archive, name='archive')
]