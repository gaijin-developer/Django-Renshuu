from django.urls import path
from . import views

urlpatterns = [
   path("<str:topic>/", views.news_view),
   path("<int:num1>/<int:num2>",views.add_view)
   # path("sports/",views.news_view),
    #path("finance/",views.finance_view)
]
