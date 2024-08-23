from ast import Delete
from audioop import reverse
from re import template
from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin #requires login for features
from django import forms

#local
from . import models


# Create your views here.

def home(request):
    meals = models.Meal.objects.all()
    context = {
        'meals': meals
    }
    return render(request, 'logApp/home.html', context)
    

def about(request):
    return render(request, "logApp/about.html", {'title' : 'about page'})


class MealListView(LoginRequiredMixin, ListView):
    model = models.Meal
    template_name = 'logApp/home.html'
    context_object_name = "meals"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['meals'] = context['meals'].filter(author = self.request.user)
    def get_queryset(self):
            queryset = super(MealListView, self).get_queryset()
            return queryset.filter(author=self.request.user)
    

class MealDetailView(DetailView):
    model = models.Meal


class MealCreateView(LoginRequiredMixin, CreateView):
    model = models.Meal
    fields = ['title', 'description', 'created_at']

    def get_form(self, *args, **kwargs):
        form = super(MealCreateView, self).get_form(*args, **kwargs)
        form.fields['created_at'].widget = forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        })
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)






class MealUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Meal
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Meal
    success_url = reverse_lazy('home')
