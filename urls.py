from django.contrib import admin
from django.urls import path, include
from homepage import views

urlpatterns = [
    path('login',views.enter, name="login"),
    path("register",views.register, name="register"),
    path("about",views.about, name="about"),
    path("menu",views.menu, name="menu"),
    path("service",views.service, name="service"),
    path("welcome",views.land, name="welcome"),
    path("team",views.team, name="team"),
    path("testimonial",views.testimonial, name="testimonial"),
    path("booking",views.booking, name="booking"),
    path("",views.start, name="start"),
    path("order",views.order, name="order"),
    path("contact",views.contact, name="contact"),
    path("checkoutpage",views.checkoutpage, name="checkoutpage"),
    path("activate/<uidb64>/<token>",views.activate, name="activate"),
    
]
