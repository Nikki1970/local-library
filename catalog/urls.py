from django.urls import path, include
from . import views

urlpatterns = [

]
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns = [
    path('', views.index, name='index'),
]