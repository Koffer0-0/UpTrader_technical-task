from django.urls import path

from mytask import views

urlpatterns = [
    path("", views.index, name='index'),
    path('<str:parent_or_child>/<int:pk>/', views.base, name='items'),
]
