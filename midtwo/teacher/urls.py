from django.urls import path
from . import views

urlpatterns = [
    path('telist',views.telist.as_view()),
    path('tedel/<int:pk>',views.tedel.as_view())
]