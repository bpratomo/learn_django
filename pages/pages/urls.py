from django.urls import path
from . import views
from django.views.generic import RedirectView


urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('about', views.AboutPageView.as_view(), name = 'about')
    # path('test',RedirectView.as_view(url='http://google.com')),

]