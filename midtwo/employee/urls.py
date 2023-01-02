from django.urls import path
from . import views

urlpatterns = [
    path('emplist',views.emplist.as_view()),
    path('empdel/<int:pk>',views.empdel.as_view())
]
