from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('henrry',views.henrry,name='henrry'),
    path('kiara',views.kiara,name='kiara'),
    path('<str:name>',views.greet,name='greet')

    

]