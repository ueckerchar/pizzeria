from django.urls import path

from . import views

app_name = 'MainApp'

urlpatterns = [
    path('',views.index,name='index'),
    path('pizzas',views.pizzas,name='pizzas'),
    path('pizzas/<int:pizza_id>/',views.pizza,name='pizza'),
    path('comment/<int:pizza_id>/',views.comment,name='comment'),
]