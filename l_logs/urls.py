from django.urls import path
from . import views
app_name = 'l_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic
    path('topics/<topic_id>/', views.topic, name='topic'),
    # Page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<topic_id>/', views.new_entry, name='new_entry'),
    # Page for editing an entry
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]