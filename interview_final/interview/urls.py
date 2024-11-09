from django.urls import path
from . import views

app_name = 'interview'

urlpatterns = [
    path('', views.InterviewRoundListView.as_view(), name='round-list'),
    path('round/add/', views.InterviewRoundCreateView.as_view(), name='round-create'),
    path('round/<int:round_id>/send-email/', views.send_email_view, name='send-email'),
]
