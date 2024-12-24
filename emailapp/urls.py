from django.urls import path
from . import views
from emailapp.views import mainviews


urlpatterns = [
    path('', mainviews.index, name='index'),
    path('email_page', mainviews.email_page, name='email_page'),
    path('send-email/', mainviews.email_form_view, name='send_email'),
]