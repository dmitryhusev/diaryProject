from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import AssignForm
from .models import Tracker

def main(request):

    user_list = User.objects.all()
    form =AssignForm
    context = {'users': user_list, 'form': form}
    return render(request, 'tracker.html', context)

def issues(request):

    issues = Tracker.objects.all()
    context = {'issues': issues}
    return render(request, 'issues.html', context)


def add_issue(request):

    user_list = User.objects.all()
    if request.method != 'POST':
        form = AssignForm()
    else:
        form = AssignForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:issues'))
    context = {'form': form, 'users': user_list, }
    return render(request, 'add_issue.html', context)

def edit_issue(request, issue_id):

    user_list = User.objects.all()
    issue = Tracker.objects.get(id=issue_id)
    if request.method != 'POST':
        form = AssignForm(instance = issue)
    else:
        form = AssignForm(instance = issue, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tracker:edit_issue', args=[issue_id]))
    context = {'form': form, 'users': user_list, 'issue_id': issue_id}
    return render(request, 'edit_issue.html', context)
