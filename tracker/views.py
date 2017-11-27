from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import AssignForm
from .models import Tracker
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def issues(request):

    if 'q' in request.GET:
        q = request.GET['q']
        data = Tracker.objects.filter(title__icontains=q )
    else:
        data = Tracker.objects.all()
    paginator = Paginator(data, 10)
    page = request.GET.get('page')

    try:
        issue = paginator.page(page)

    except PageNotAnInteger:
        issue = paginator.page(1)

    except EmptyPage:
        issue = paginator.page(paginator.num_pages)

    context = {'issues': issue}
    return render(request, 'issues.html', context)


@login_required
def add_issue(request):

    user_list = User.objects.all()
    if request.method != 'POST':
        form = AssignForm()
    else:
        form = AssignForm(data=request.POST)
        if form.is_valid():
            title = 'DO NOT REPLY'
            ticket_name = form.cleaned_data.get('title').upper()
            send_to = form.cleaned_data.get('assignee')
            form.save()
            current_user = request.user
            message = '%s %s' %('Changed by:', current_user)
            send_mail(title, ticket_name + '\n' + '\n' + message, settings.EMAIL_HOST_USER, [send_to], fail_silently=False)
            return HttpResponseRedirect(reverse('tracker:issues'))
    context = {'form': form, 'users': user_list, }
    return render(request, 'add_issue.html', context)


def edit_issue(request, issue_id):

    user_list = User.objects.all()
    issue = Tracker.objects.get(id=issue_id)
    if request.method != 'POST':
        form = AssignForm(instance=issue)
    else:
        form = AssignForm(instance=issue, data=request.POST)
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

