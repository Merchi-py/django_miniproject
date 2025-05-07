from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',  views.HomePageView.as_view(), name="home_page"),
    path('order_create/',  views.OrderCreationView.as_view(), name="order_create"),
    path('review_create/',  views.ReviewCreate.as_view(), name="review_create"),
]
