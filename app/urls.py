from django.urls import path
from . import views
from .views import about_view

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about_view, name='about'),
    path('activities/', views.activities_view, name='activities'),
    path('book-now/', views.book_now, name='book_now'),
    path('contact/', views.contact, name='contact'),
    path('luxury-camp/', views.luxury_camp, name='luxury_camp'),
    path('luxury-camp/<slug:slug>/', views.luxury_camp, name='luxury_camp_detail'),
    path('tour/', views.tour, name='tour'),
    path('tour/<slug:slug>/', views.tour_detail, name='tour_detail'),
    path('events/', views.events, name='events'),
    path('daytrip/<slug:slug>/', views.daytrip_detail, name='daytrip_detail'),
    path('cities/', views.city_list, name='city_list'),
    path('cities/<slug:slug>/', views.city_detail, name='city_detail'),
    path('photography/', views.photography, name='photography'),
    path('contact/submit/', views.contact_email, name='contact_email'),
    path('contact/submit2/', views.contact_email2, name='contact_email2'),
    path('book-now/submit/', views.booking_email, name='booking_email'),
    path('sitemap.xml', views.manual_sitemap, name='manual_sitemap'),
] 