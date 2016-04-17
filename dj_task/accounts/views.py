import csv
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import CustomUser
from accounts.forms import AddUserForm
from accounts.common.access import access
from accounts.common.bizzfuzz import bizzfuzz


def list_all_user(request):
    # Displays all users from database
    users = CustomUser.objects.all()

    return render(request, "accounts/all_users.html", {'users': users})


def view_user(request, user_id):
    # Displays single user in database
    user = CustomUser.objects.get(id=user_id)

    return render(request, "accounts/view_user.html", {'user': user})


def add_user(request):
    # Adding new user in database
    if request.method == "POST":
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddUserForm()
    return render(request, 'accounts/add_user.html', {'form': form})


def edit_user(request, user_id):
    # Editing user in database
    user = get_object_or_404(CustomUser, id=user_id)

    if request.method == "POST":
        form = AddUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AddUserForm(instance=user)
    return render(request, 'accounts/edit_user.html', {'form': form})


def delete_user(request, user_id):
    # Remove user from db
    user = get_object_or_404(CustomUser, id=user_id)
    user.delete()

    return redirect('/')


def csv_list(request):
    # Generates a report in a CSV-format.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=list_users.csv'

    writer = csv.writer(response, dialect=csv.excel)
    writer.writerow(['Username', 'Date of birth', 'Access', 'Random number', 'BizzFuzz'])

    users = CustomUser.objects.all()
    for user in users:
        check_access = access(user.birthday)
        check_bizzfuzz = bizzfuzz(user.random_number)

        writer.writerow([user.username, user.birthday,
                        check_access, user.random_number,
                        check_bizzfuzz])
    return response