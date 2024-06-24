from . import views
from django.urls import path

urlpatterns = [
    path('findDealers/',views.findDealer,name = 'findDealer'),
    path('becomeDealer/', views.becomeDealer, name='becomeDealer')
]