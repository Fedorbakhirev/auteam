import re
from datetime import timedelta, date

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import Group

from .models import *
from .forms import *
from .admin import *

from .decorators import *


def home(request):
    tariffs = Tariff.objects.all().order_by('-id')[:3]
    return render(request, 'main/index.html', {'tariffs': tariffs})


def tariffs(request):
    tariffs = Tariff.objects.all().order_by('-id')
    return render(request, 'main/cards.html', {'tariffs': tariffs})


class Contacts(CreateView):
    form_class = ContactForm
    template_name = 'main/contacts.html'
    success_url = reverse_lazy('main:contact_success')


def contact_success(request):
    return render(request, 'main/contact-success.html')


@login_required
def get_tariff(request, id):
    response = request.user.usertariff
    if response.tariff:
        return render(request, 'main/tariff-error.html')
    else:
        response.tariff_id = id
        response.is_active = False
        response.is_paid = None
        response.save()
        return render(request, 'main/tariff-success.html')


@login_required
def remove_tariff(request):
    response = request.user.usertariff
    if response.tariff and response.is_active:
        history = TariffHistory(user=request.user, tariff_id=response.tariff_id)
        history.save()
        response.tariff_id = None
        response.is_active = False
        response.save()
        return redirect('main:profile')
    else:
        return redirect('main:profile')


@login_required
def get_tariffs_history(request):
    history = TariffHistory.objects.all().order_by('-id').filter(user=request.user.pk)
    return render(request, 'main/user/history/history_cards.html', {'history': history})


@login_required()
def view_decline(request, id):
    tariff = TariffHistory.objects.get(pk=id)
    return render(request, 'main/user/history/view_decline.html', {'tariff': tariff})


@login_required
def get_complaints_history(request):
    history = Complaint.objects.all().order_by('-id').filter(user=request.user.pk)
    return render(request, 'main/user/history/history_complaints.html', {'history': history})


class AddComplaint(CreateView):
    form_class = ComplaintForm
    template_name = 'main/user/create_complaint.html'
    success_url = reverse_lazy('main:complaints_history')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddComplaint, self).form_valid(form)


@login_required()
def view_profile(request):
    if User.objects.filter(pk=request.user.pk, groups__name='Инженер').exists():
        return redirect('main:engineer_lk')
    else:
        profile = UserTariff.objects.get(user=request.user)
        return render(request, 'main/user/lk.html', {'profile': profile})


@login_required()
def pay_tariff(request):
    tariff = UserTariff.objects.get(user=request.user)
    if tariff.is_paid == None:
        tariff.is_paid = date.today()
    tariff.is_paid = tariff.is_paid + timedelta(days=30)
    tariff.save()
    return redirect('main:profile')


@login_required()
def view_requisites(request):
    tariff = UserTariff.objects.get(user=request.user)
    return render(request, 'main/user/requisites.html', {'tariff': tariff})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('main:auth')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def post(self, request, *args, **kwargs):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.save()

            u = User.objects.get(username=request.POST['username'])
            if not UserTariff.objects.filter(user=u).exists():
                adduser = UserTariff(user=u, tariff_id=None, is_active=False, phone_number=request.POST['phone'])
                adduser.save()

            return redirect('main:auth')
        else:
            return render(request, self.template_name, {'form': form})


class LoginUser(LoginView):
    authentication_form = LoginUserForm
    template_name = 'main/auth.html'
    success_url = reverse_lazy('main:home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        if not UserTariff.objects.filter(user=self.request.user.pk).exists():
            adduser = UserTariff(user=self.request.user, tariff_id=None, is_active=False)
            adduser.save()
        return reverse_lazy('main:home')


def logout_view(request):
    logout(request)
    return redirect('main:home')


@group_required('Инженер')
def engineer_profile(request):
    profile = User.objects.get(pk=request.user.pk)
    return render(request, 'main/engineer/engineer.html', {'profile': profile})


@group_required('Инженер')
def connection_requests(request):
    cards = UserTariff.objects.all().order_by('-id').filter(is_active=False).filter(tariff__isnull=False)
    return render(request, 'main/engineer/requests/connectionrequests.html', {'cards': cards})


@group_required('Инженер')
def request_detail(request, id):
    card = UserTariff.objects.get(pk=id)
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            history = TariffHistory(user=card.user, tariff_id=card.tariff_id, desc=request.POST['desc'],
                                    is_declined=True, engineer=request.user)
            history.save()
            card.tariff_id = None
            card.is_active = False
            card.engineer = None
            card.save()
            return redirect('main:connetion_requests')
        else:
            return render(request, 'main/engineer/requests/requestdetail.html', {'card': card, 'form': form})
    else:
        form = RequestForm()
    return render(request, 'main/engineer/requests/requestdetail.html', {'card': card, 'form': form})


@group_required('Инженер')
def accept_request(request, id):
    card = UserTariff.objects.get(pk=id)
    card.is_active = True
    card.engineer = request.user
    card.save()
    return redirect('main:connetion_requests')


@group_required('Инженер')
def complaints_list(request):
    if request.user.is_superuser:
        complaints = Complaint.objects.all().order_by('-id').filter(status=False)
    else:
        complaints = Complaint.objects.all().order_by('-id').filter(engineer=request.user).filter(status=False)
    return render(request, 'main/engineer/complaints/complaintlist.html', {'complaints': complaints})


@group_required('Инженер')
def complaint_reply(request, id):
    complaint = Complaint.objects.get(pk=id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            complaint.answer = request.POST['answer']
            complaint.status = True
            complaint.save()
            return redirect('main:complaints_list')
        else:
            return render(request, 'main/engineer/complaints/complaint_reply.html',
                          {'complaint': complaint, 'form': form})
    else:
        form = ReplyForm()
    return render(request, 'main/engineer/complaints/complaint_reply.html', {'complaint': complaint, 'form': form})
