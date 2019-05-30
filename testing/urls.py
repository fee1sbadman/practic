from django.urls import path, include
from . import views



urlpatterns = [
path('test/<int:test_id>/question/<int:pk>', views.question_detail, name = 'question_detail'),
path('<int:question_id>/', views.vote, name = 'vote'),
path('test/<int:pk>/results/', views.results, name = 'results'),
path('results/<int:test_id>/<int:user_id>/', views.zero, name = 'zero'),
path('results/<int:test_id>/', views.bal, name = 'bal'),
path('', views.test_list, name = 'test_list'),
path('test/<int:pk>/', views.test_detail, name = 'test_detail'),
path('accounts/', include('django.contrib.auth.urls')),
path('contact/', views.contact, name = 'contact'),
]