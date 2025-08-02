

from django.contrib.auth import login, get_user, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, DeleteView

from field_target.accounts.forms import UserRegisterForm, ProfileForm, UserEditForm
from field_target.accounts.models import UserProfile


# Create your views here.
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
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')  # or wherever you'd like to go

        return render(request, 'accounts/register.html', context)

class ProfileDetailsView(View):
    model = UserProfile
    template_name = 'accounts/profile-details.html'


    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        return render(request, 'accounts/profile-details.html', {'profile': profile})



from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import ProfileForm, UserEditForm

class ProfileEditView(View):
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

class ProfileDeleteView(DeleteView):
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





