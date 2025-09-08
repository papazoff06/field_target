from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import modelformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone, duration
from django.utils.timezone import now
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from field_target.accounts.models import UserProfile
from field_target.competitions.forms import CompetitionCreationForm, CompetitionEditForm, ScoreUpdateForm
from field_target.competitions.models import Competition, Registration
from django.db.models import F

# Create your views here.
class CompetitionCreateView(LoginRequiredMixin, CreateView):
    model = Competition
    form_class = CompetitionCreationForm
    template_name = 'competitions/competition-create.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to create competitions.")

        return super().dispatch(request, *args, **kwargs)


class ShowAllCompetitionsView(ListView):
    model = Competition
    template_name = 'competitions/all-competitions.html'
    context_object_name = 'competitions'
    ordering = ['start_date']

    def get_queryset(self):
        today = timezone.now().date()
        return Competition.objects.filter(end_date__gte=today).order_by('start_date')


class CompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition-details.html'
    context_object_name = 'competition'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        competition = self.get_object()
        user = self.request.user
        competitors = Registration.objects.filter(competition=competition).annotate(
            annotated_total_score=F('first_day_score') + F('second_day_score') + F('tird_day_score')
        ).order_by('-annotated_total_score')
        context['competitors'] = competitors
        context['today'] = now().date()
        context['is_past'] = competition.end_date < context['today']
        context['competition_days'] = competition.end_date - competition.start_date

        if user.is_authenticated:
            context['is_registered'] = Registration.objects.filter(
                competition=competition,
                shooter=user.userprofile
            ).exists()
        else:
            context['is_registered'] = False

        return context


class CompetitionRegisterView(LoginRequiredMixin, CreateView):
    model = Registration
    fields = ['accommodation']
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


class CompetitionEditView(LoginRequiredMixin, UpdateView):
    model = Competition
    template_name = 'competitions/competition-edit.html'
    form_class = CompetitionEditForm
    success_url = reverse_lazy('all-competitions')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser and not request.user.has_perm('competitions.change_competition'):
            return HttpResponseForbidden("You are not authorized to edit competitions.")

        return super().dispatch(request, *args, **kwargs)


class CompetitionDeleteView(LoginRequiredMixin, DeleteView):
    model = Competition
    template_name = 'competitions/competition-delete.html'
    success_url = reverse_lazy('all-competitions')

class ShowPastCompetitionsView(ListView):
    model = Competition
    template_name = 'competitions/past-competitions.html'
    context_object_name = 'competitions'
    ordering = ['start_date']
    def get_queryset(self):
        today = timezone.now().date()
        return Competition.objects.filter(end_date__lte=today).order_by('start_date')

class PastCompetitionDetailView(DetailView):
    model = Competition
    template_name = 'competitions/competition-details.html'  # SAME template
    context_object_name = 'competition'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        competition = self.get_object()
        context['competitors'] = Registration.objects.filter(competition=competition)
        context['today'] = now().date()
        context['is_past'] = True  # Always past for this view
        return context

class UpdateScoresView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'competitions/update-score.html'
    form_class = ScoreUpdateForm

    def test_func(self):
        # Only staff users can access
        return self.request.user.is_staff

    def get_competition(self, competition_id):
        return get_object_or_404(Competition, pk=competition_id)

    def get(self, request, competition_id):
        competition = self.get_competition(competition_id)
        registrations = Registration.objects.filter(competition=competition).select_related('shooter__user')
        ScoreFormSet = modelformset_factory(Registration, form=self.form_class, extra=0)
        formset = ScoreFormSet(queryset=registrations)
        competition_days = competition.end_date - competition.start_date
        return render(request, self.template_name, {
            'formset': formset,
            'competition': competition,
            'competition_days': competition_days,
        })

    def post(self, request, competition_id):
        competition = self.get_competition(competition_id)
        registrations = Registration.objects.filter(competition=competition)
        ScoreFormSet = modelformset_factory(Registration, form=self.form_class, extra=0)
        formset = ScoreFormSet(request.POST, queryset=registrations)


        if formset.is_valid():
            formset.save()
            return redirect('competition-details', pk=competition_id)

        competition_days = competition.end_date - competition.start_date
        print(competition_days)
        return render(request, self.template_name, {
            'formset': formset,
            'competition': competition,
            'competition_days': competition_days
        })