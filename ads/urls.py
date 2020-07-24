from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='list'),
    path('<uuid:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('create/', views.AdCreateView.as_view(), name='create'),
    # path('create/', views.ad_create_form_name, name='create'),
    path('update/<uuid:pk>/', views.AdUpdateView.as_view(), name='update'),
    path('search/', views.AdSearchResultsView.as_view(), name='search_results'),
    path('search/<uuid:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('userad/', views.userprofile, name='user_ad'),
    path('userad/<uuid:pk>/', views.AdDetailView.as_view(), name='user_ad_detail'),
    path('userad/update/<uuid:pk>/', views.AdUpdateView.as_view(), name='user_ad_update'),
    path('userad/delete/<uuid:pk>/', views.AdDeleteView.as_view(), name='user_ad_delete'),
]