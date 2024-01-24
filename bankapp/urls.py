from django.urls import path, include

from bankapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<slug:distname>/', views.details, name='details'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('newpage/', views.newpage, name='newpage'),
    path('form/', views.form, name='form'),
    # path('my_def_in_view/', views.my_def_in_view, name='my_def_in_view'),
    path('confirmationpage/', views.confirmationpage, name='confirmationpage'),
    path('get-topics-ajax/', views.get_topics_ajax, name="get_topics_ajax"),


]
