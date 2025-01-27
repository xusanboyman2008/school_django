from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from Logins.models import Logins_model


# Create your views here.

def all(request):
    logins_list = Logins_model.objects.all().order_by('status')
    page_number = request.GET.get('page', 1)  # Get the current page number from the request
    paginator = Paginator(logins_list, 10)  # Paginate with 10 records per page
    page_obj = paginator.get_page(page_number)
    return render(request, 'Logins/home.html', context={'page_obj': page_obj,'user':'user'})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        password = request.POST.get('email').lower()
        username = request.POST.get('name')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('all_logins')
        else:
            messages.error(request, 'Username OR password does not exit')

    return render(request, 'Logins/login.html')

# Create a new login
def create_login(request):
    if request.method == "POST":
        login = request.POST.get("login")
        password = request.POST.get("password")

        if Logins_model.objects.filter(login=login).exists():
            return JsonResponse({"success": False, "message": "Login already exists!"})

        Logins_model.objects.create(login=login, password=password)
        return redirect(reverse('all_logins') + f'?page={request.GET.get("page", 1)}')


def update_login(request, pk):
    if request.method == "POST":
        login_instance = get_object_or_404(Logins_model, id=pk)
        login_instance.login = request.POST.get("login")
        login_instance.password = request.POST.get("password")
        login_instance.status = request.POST.get("status")
        login_instance.save()
        return redirect(reverse('all_logins') + f'?page={request.GET.get("page", 1)}')


# Update or delete a login
def delete_login(request, pk):
    login_instance = get_object_or_404(Logins_model, id=pk)

    if request.method == "PUT":
        login_instance.login = request.POST.get("login", login_instance.login)
        login_instance.password = request.POST.get("password", login_instance.password)
        login_instance.save()
        return JsonResponse({"success": True, "message": "Login updated successfully!"})

    if request.method == "DELETE":
        login_instance.delete()
        return JsonResponse({"success": True, "message": "Login deleted successfully!"})

    if request.method == "DELETE":
        login_instance = Logins_model.objects.get(id=pk)
        login_instance.delete()


def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('all_logins')
    logout(request)