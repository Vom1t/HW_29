from django.urls import path

from ads.views.category import *


urlpatterns = [
    path('', CategoryListView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view())
]
