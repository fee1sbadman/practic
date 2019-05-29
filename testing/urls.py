from django.urls import path
from . import views


urlpatterns = [
path('test/<int:test_id>/question/<int:pk>', views.question_detail, name = 'question_detail'),
path('<int:question_id>/', views.vote, name = 'vote'),
path('test/<int:pk>/results/', views.results, name = 'results'),
path('results/<int:test_id>/', views.zero, name = 'zero'),
path('', views.test_list, name = 'test_list'),
path('test/<int:pk>/', views.test_detail, name = 'test_detail')
]