from django.urls import path

from . import views

app_name = "message"
urlpatterns = [
    path('', views.MessageListView.as_view(), name='message_list'),
    path('create/', views.MessageCreateView.as_view(), name='message_create'),
    path('update/<pk>', views.MessageUpdateView.as_view(), name='message_delete'),
    path('delete/<pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('<pk>/', views.MessageDetailView.as_view(), name='message_detail'),
]