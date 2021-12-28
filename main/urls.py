from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),

    path('tariffs/', tariffs, name='tariffs'),
    path('get_tariff/<id>', get_tariff, name='get_tariff'),
    path('remove_tariff/', remove_tariff, name='remove_tariff'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('contacts/success', contact_success, name='contact_success'),


    path('lk/', view_profile, name='profile'),
    path('lk/requisites/', view_requisites, name='view_requisites'),
    path('lk/requisites/pay/', pay_tariff, name='pay'),
    path('lk/tariffs_history/', get_tariffs_history, name='tariffs_history'),
    path('lk/tariffs_history/id=<id>', view_decline, name='view_decline'),
    path('lk/complaints_history/', get_complaints_history, name='complaints_history'),
    path('lk/addcomplaint', login_required(AddComplaint.as_view()), name='addcomplaint'),

    path('engineer/', engineer_profile, name='engineer_lk'),
    path('engineer/requests/', connection_requests, name='connetion_requests'),
    path('engineer/requests/id=<id>/', request_detail, name='request_detail'),
    path('engineer/requests/id=<id>/accept/', accept_request, name='request_accept'),
    path('engineer/complaints/', complaints_list, name='complaints_list'),
    path('engineer/complaints/id=<id>/', complaint_reply, name='complaints_reply'),

    path('login/', LoginUser.as_view(), name='auth'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]
