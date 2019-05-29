from django.urls import path
from . import views


urlpatterns = [
path('test/<int:test_id>/question/<int:pk>', views.question_detail, name = 'question_detail'),
path('<int:question_id>/', views.vote, name = 'vote'),
path('results/', views.results, name = 'results'),
path('', views.TestList.as_view(), name = 'test_list'),
path('test/<int:pk>/', views.test_detail, name = 'test_detail')
]