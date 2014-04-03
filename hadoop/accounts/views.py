# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, RequestContext
from forms import SignInForm
from django.contrib.auth.decorators import login_required


# def register(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password1')
#         form = UserCreationForm(request.POST)
#         errors = []
#         if not form.is_valid():
#             errors.extend(UserCreationForm.error_messages)
#             return HttpResponseRedirect('/accounts/register', {'errors': errors, })
#         user = form.save()
#         user.save()
#         profile = UserProfile(user=user)
#         profile.save()
#         new_user = auth.authenticate(username=username, password=password)
#         if new_user is not None:
#             auth.login(request, new_user)
#             return HttpResponseRedirect('/accounts/profile')
#         else:
#             return HttpResponseRedirect('/accounts/login')

#     form = UserCreationForm()
#     return render_to_response("accounts/register.html", {
#         'form': form,
#     }, context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print request.POST.get('next')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                next = request.POST.get('next')
                if next is not None:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect('/hello')
    return render_to_response('signin.html', {
        'next': request.GET.get('next'),
        }, context_instance=RequestContext(request))


# @login_required
# def user_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user.profile)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('accounts/profile.html')
#     else:
#         form = UserProfileForm(instance=request.user.profile)
#     return render_to_response('accounts/profile.html', {
#         'form': form,
#         'user': request.user,
#         }, context_instance=RequestContext(request))
