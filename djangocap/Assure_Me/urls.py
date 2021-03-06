from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Assure_Me"
urlpatterns = [
    url(r'^$', views.initial, name='initial'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.user_logout, name='logout'),
    url(r'^home$', views.home_view, name='home'),
    url(r'^account$', views.account_view, name='account'),
    url(r'^account_edit$', views.account_edit_view, name='account_edit'),
    url(r'^affirmations$', views.affirmations_view, name='affirmations'),
    url(r'^affirmation_new$', views.new_affirmation_view, name='new_affirmation'),
    url(r'^affirmation_delete/(?P<Affirmation_Id>\d+)$', views.delete_affirmation_view, name='delete_affirmation'),
    url(r'^affirmation_edit/(?P<Affirmation_Id>\d+)$', views.edit_affirmation_view, name='edit_affirmation'),
    url(r'^phone$', views.sms_response, name='text'),
]
