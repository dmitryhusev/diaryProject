from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import AssignForm

def main(request):

    user_list = User.objects.all()
    form =AssignForm
    context = {'users': user_list, 'form': form}
    return render(request, 'tracker.html', context)

def issue(request):

    pass