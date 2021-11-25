from django.urls import path

from . import views

app_name = 'kouka2'
urlpatterns = [
    path('',views.Kouka2View.as_view(),name='kouka2'),
]