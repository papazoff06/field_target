from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.http import Http404
from django.views import View
from django.views.generic import  DeleteView
from field_target.accounts.forms import UserRegisterForm, ProfileForm, UserEditForm
from field_target.accounts.models import UserProfile
from django.shortcuts import render, redirect
from django.urls import reverse_lazy



class UserRegisterView(View):
    def get(self, request):
        user_form = UserRegisterForm()
        profile_form = ProfileForm()
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'accounts/register.html', context)

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')

        return render(request, 'accounts/register.html', context)

class CustomLogoutView(LogoutView):
    success_url = reverse_lazy('home')

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('home')

class ProfileDetailsView(LoginRequiredMixin, View):
    model = UserProfile
    template_name = 'accounts/profile-details.html'


    def get(self, request):
        try:
            profile = request.user.userprofile
        except UserProfile.DoesNotExist:
            raise Http404("No UserProfile found for this user.")

        context = {
            'profile': profile
        }
        return render(request, self.template_name, context)

    def get_object(self, queryset=None):
        try:
            return self.request.user.userprofile
        except UserProfile.DoesNotExist:
            raise Http404("No UserProfile found for this user.")


class ProfileEditView(LoginRequiredMixin, View):
    template_name = 'accounts/profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(self.success_url)

        context = {
            'user_form': user_form,
            'profile_form': profile_form,
        }
        return render(request, self.template_name, context)

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = UserProfile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    def post(self, request, *args, **kwargs):
        user = request.user
        logout(request)

        user.userprofile.delete()
        user.delete()

        return redirect(self.success_url)





