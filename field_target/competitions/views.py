from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from field_target.accounts.models import UserProfile
from field_target.competitions.forms import CompetitionForm, CompetitionRegistrationForm
from field_target.competitions.models import Competition, Registration


# Create your views here.
class CompetitionCreateView(CreateView):
    model = Competition
    form_class = CompetitionForm
    template_name = 'competitions/competition-create.html'
    success_url = reverse_lazy('home')

class ShowAllCompetitionsView(ListView):
    model = Competition
    template_name = 'competitions/all-competitions.html'
    context_object_name = 'competitions'
    ordering = ['start_date']


class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition-details.html'
    context_object_name = 'competition'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        competition = self.get_object()
        user = self.request.user
        context['competitors'] = Registration.objects.filter(competition=competition)

        if user.is_authenticated:
            context['is_registered'] = Registration.objects.filter(
                competition=competition,
                shooter=user.userprofile
            ).exists()
        else:
            context['is_registered'] = False
        return context

class CompetitionRegisterView(CreateView):
    model = Registration
    fields = ['accommodation']  # Only ask the user for accommodation if needed
    template_name = 'competitions/competition-register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['competition'] = self.competition
        return context

    def dispatch(self, request, *args, **kwargs):
        self.competition = get_object_or_404(Competition, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user_profile = get_object_or_404(UserProfile, user=self.request.user)
        form.instance.shooter = user_profile
        form.instance.competition = self.competition
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('competition-details', kwargs={'pk': self.competition.pk})


