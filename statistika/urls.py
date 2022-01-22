from django.urls import path
from .views import StatsView, StatsEdit

urlpatterns = [
    path('', StatsView.as_view(), name='stats'),
    path('update/<int:son>', StatsEdit.as_view(), name='stats-update'),
]