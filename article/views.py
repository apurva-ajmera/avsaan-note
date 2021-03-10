from django.shortcuts import render,redirect
from .models import Note
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .forms import NoteCreateForm
from django.contrib import messages

# Create your views here.

def make(request):
    return render(request, 'article/choose.html',{'title':'Choose Template'})

def home(request):
    messages.success(request, f'Some examples are given below. Click on name to see more detail')
    context = {
      'notes' : Note.objects.all(),
      'title': 'Home'
    }
    return render(request, 'article/home.html', context)

def detail(request, slug):
    messages.success(request, f'Scroll down to find sharing options!!')
    notes = Note.objects.filter(slug=slug)
    return render(request, 'article/detail.html', {'notes': notes,'title': 'Detail'})

def create(request, category):
    if request.method == 'POST':
        form = NoteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.instance.category = category
            form.save()
            slug = form.instance.slug
            return redirect('note-detail', slug=slug)

    else:
        form = NoteCreateForm()

    return render(request, 'article/form.html', {'form': form, 'title':'Create'})

class NoteDetailView(DetailView):
    model = Note

class NoteUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['image', 'name', 'date', 'extra_information']

    def form_valid(self, form):
        value = ''
        def test(self):
            article = self.get_object
            value = article.slug

        form.instance.creator = self.request.user
        form.instance.slug = value
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False

class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.creator:
            return True
        return False

def uploads(request):
    messages.success(request, f'Click on name to see more detail')
    notes = Note.objects.filter(creator=request.user)
    context = {
      'notes' : notes,
      'length' : len(notes),
      'title': 'Your uploads'
    }
    return render(request, 'article/user_uploads.html', context)
