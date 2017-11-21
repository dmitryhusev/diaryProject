from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import AssignForm
from .models import Tracker
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def main(request):

    user_list = User.objects.all()
    form =AssignForm
    context = {'users': user_list, 'form': form}
    return render(request, 'tracker.html', context)

def issues(request):

    issues = Tracker.objects.all()
    context = {'issues': issues}
    return render(request, 'issues.html', context)

@login_required
def add_issue(request):

    user_list = User.objects.all()
    if request.method != 'POST':
        form = AssignForm()
    else:
        form = AssignForm(data=request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('description') 
            send_to = form.cleaned_data.get('assignee')
            from_logged = User.username
            form.save()
            send_mail(title, message, settings.EMAIL_HOST_USER, [send_to], fail_silently=False)
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
            title = 'DO NOT REPLY'
            ticket_name = form.cleaned_data.get('title').upper()
            send_to = form.cleaned_data.get('assignee')
            form.save()
            current_user = request.user
            message = '%s %s' %('Changed by:', current_user)
            send_mail(title, ticket_name + '\n' + '\n' + message, settings.EMAIL_HOST_USER, [send_to], fail_silently=False)
            return HttpResponseRedirect(reverse('tracker:edit_issue', args=[issue_id]))
    context = {'form': form, 'users': user_list, 'issue_id': issue_id}
    return render(request, 'edit_issue.html', context)

