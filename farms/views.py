from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Farm
# Create your views here.

farms = [
    {
        'row' : 12,
        'col' : 10,
        'lat' : 35.23123,
        'lng' : 35.2341
    },
    {
        'row' : 23,
        'col' : 14,
        'lat' : 50.23123,
        'lng' : 38.2341
    },

]



class PostListView(ListView):
    model = Farm
    template_name = 'farms/index.html'
    context_object_name = 'farms'

class PostDetailView(DetailView):
    model = Farm

class PostDetailView(DetailView):
    model = Farm

class PostCreateView(CreateView):
    model = Farm
    fields = ['row', 'col', 'lat', 'lng']
    success_url = '/post'

    def form_valid(self, form):
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        ctx = super(PostCreateView, self).get_context_data(**kwargs)
        ctx['farms'] = Farm.objects.all()
        return ctx


class PostUpdateView(UpdateView):
    model = Farm
    fields = ['row', 'col', 'lat', 'lng']

    def form_valid(self, form):
        return super().form_valid(form)



class PostDeleteView(DeleteView):
    model = Farm
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False