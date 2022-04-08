from django.urls import path

from mainapp.views import MainCreateView, MainDetailView, MainUpdateView, MainDeleteView, MainListView, PidListView

app_name = "mainapp"

urlpatterns = [
    path('list/', MainListView.as_view(), name='list'),
    path('pid/', PidListView.as_view(), name='pid'),

    path('create/', MainCreateView.as_view(), name='create'),
    path('detail/<int:pk>', MainDetailView.as_view(), name='detail'),
    path('update/<int:pk>', MainUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', MainDeleteView.as_view(), name='delete'),
    ]