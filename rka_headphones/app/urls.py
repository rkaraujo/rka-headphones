from django.urls import path
from .views import HeadphoneListView, CableListView, EartipListView, HeadphoneCombinationListView

urlpatterns = [
    path('headphones/', HeadphoneListView.as_view(), name='headphones-list'),
    path('cables/', CableListView.as_view(), name='cables-list'),
    path('eartips/', EartipListView.as_view(), name='eartips-list'),
    path('headphone-combinations/', HeadphoneCombinationListView.as_view(), name='headphones-combinations-list'),
]
