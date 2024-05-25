from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import HttpResponse 
from .models import Post 
from django.views.generic import (ListView , DetailView , CreateView , DeleteView , UpdateView)


posts= [
    {
        'author':'Dipanshi Dey',
        'title': 'sample1',
        'content':'content1',
        'date':'May 18,2024'
    },
    
    {
        'author':'Naman Verma',
        'title': 'sample2',
        'content':'content2',
        'date':'May 28,2018'
    },
    
    {
        'author':'Scarlet Buttler',
        'title': 'sample3',
        'content':'content3',
        'date':'May 18,2024'
    },
]

def home(request):
    context={
        'posts': Post.objects.all()
    }
    
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model=Post 
    template_name='blog/home.html'
    context_object_name= 'posts'
    ordering=['-date']
class PostDetailView(DetailView):
    model=Post
class PostCreateView(LoginRequiredMixin ,CreateView):
    model=Post
    fields = ['title','content']
    def form_valid(self , form ):
        form.instance.author = self.request.user
        return super().form_valid(form) 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model=Post
    fields = ['title','content']
    def form_valid(self , form ):
        form.instance.author = self.request.user
        return super().form_valid(form)  
    def test_func(self):
        post= self.get_object()
        if self.request.user==post.author:
            return  True
        return False 
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
    model=Post    
    success_url = "/"
    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return  True
        return False    
    
   
    

#def about(request):
    #return HttpResponse("<h1>Blog About</h1>") how it looked before 
    
def about(request):
   return render(request,'blog/about.html',{'title':'About'})    
    
 

# Create your views here.
