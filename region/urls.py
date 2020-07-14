from django.urls import path
from region import views

urlpatterns = [
    path('', views.index, name='index'),
    path('states', views.states, name='states'),
    path('countries', views.countries, name='countries'),
    path('country_selected/<int:country_id>/', views.show_by_country_page, name='classroom_selected')
]