from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_app, name='all_app'),
    path('<int:chai_id>/', views.chai_detail, name='chai_detail'),
    path('chai_store/', views.chai_store_view, name='chai_stores'),
]
