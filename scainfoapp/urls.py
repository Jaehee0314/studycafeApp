from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.test_view, name='test_view'),
    path('hashtag/', views.hashtag_view, name='hashtag'),
    path('sort_star/', views.sortstar_view, name='sort_star'),
    path('sort_review/', views.sortreview_view, name='sort_star'),
]