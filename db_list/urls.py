from django.urls import path, include
from . import views



urlpatterns = [
    path('list/', views.testJsonView.as_view(), name='listdb'),
    path('test/', views.testHTMLrenderContextView.as_view(), name='test'),
]