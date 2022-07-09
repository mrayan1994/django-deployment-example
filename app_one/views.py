from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from app_one.models import AccessRecord
from app_one.forms import UserForm, UserProfileInfoFrom

# Create your views here.


def index(request):

    return HttpResponse("Hello World")


def home_view(request):

    return render(request, 'app_one/home.html')


def user_login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)

                return HttpResponseRedirect('home')

            else:

                return HttpResponse('<h1>Account Not Active!</h1>')

        else:

            print('Login attempt failed!!')
            print('Username: {u} and password: {p}'.format(
                u=username, p=password))

            return HttpResponse('<h1>Invalid Credentials!</h1>')

    else:

        return render(request, 'app_one/user_login.html', context={})


@login_required
def user_logout_view(request):

    logout(request)

    return HttpResponseRedirect('user_login')


def user_registration_view(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        user_profile_form = UserProfileInfoFrom(data=request.POST)

        if user_form.is_valid() and user_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            if 'picture' in request.FILES:

                user_profile.profile = request.FILES['picture']

            user_profile.save()

            registered = True

        else:

            print(user_form.errors, user_profile_form.errors)

    else:

        user_form = UserForm()
        user_profile_form = UserProfileInfoFrom()

    return render(request, 'app_one/user_registration.html',
                  context={'user_form': user_form, 'user_profile_form': user_profile_form, 'registered': registered})


@login_required
def records_page_view(request):

    acc_rec_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': acc_rec_list}

    return render(request, 'app_one/access_records_page.html', context=date_dict)  # noqa E501


# def form_page_view(request):
#
#     form = TestForm()
#
#     if request.method == 'POST':
#
#         form = TestForm(request.POST)
#
#         if form.is_valid():
#
#             print("Validation Successful")
#             print("Name: " + form.cleaned_data['name'])
#             print("Email: " + form.cleaned_data['email'])
#             print("Text: " + form.cleaned_data['text'])
#
#     return render(request, 'app_one/form_page.html', context={'form': form})
