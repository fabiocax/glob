from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post



class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'index.html'
	paginate_by = 3
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dados'] = Post.objects.filter(detach=True).order_by('-created_on')
		return context

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dados'] = Post.objects.filter(detach=True).order_by('-created_on')
		return context



