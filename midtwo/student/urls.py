from django.urls import path
from . import views

urlpatterns = [
    path('stulist',views.stulist.as_view()),
    path('studel/<int:pk>',views.studel.as_view())
]