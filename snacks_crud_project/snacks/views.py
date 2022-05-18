from django.shortcuts import render
from .models import Snack
from django.views.generic import(
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,
                                            )

class SnackListView(ListView):
    template_name = 'snack-list.html'
    model=Snack 

class SnackDetailView(DetailView):
    template_name = 'snack-detail.html'
    model=Snack 

class SnackCreateView(CreateView):
    template_name = 'snack-create.html'
    model=Snack
    fields = ['title' , 'purchaser' , 'description']

class SnackUpdateView(UpdateView):
    template_name = 'snack-update.html'
    model=Snack 
    fields = ['title' , 'description']

class SnackDeleteView(DeleteView):
    template_name = 'snack-delete.html'
    model=Snack 
    success_url ='/'