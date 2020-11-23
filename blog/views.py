from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post,Image



class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1,detach=False,sidebar=False,footer=False).order_by('-created_on')
	template_name = 'index.html'
	paginate_by = 3
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dados'] = Post.objects.filter(detach=True,status=1,footer=False).order_by('-created_on')
		context['sidebar'] = Post.objects.filter(sidebar=True,status=1,footer=False).order_by('-created_on')
		context['footer'] = Post.objects.get(footer=True,status=1).content
		context['logo'] = Image.objects.get(slug='logo').image
		return context

class PostDetail(generic.DetailView):
	model = Post
	template_name = 'post_detail.html'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dados'] = Post.objects.filter(detach=True,status=1,footer=False).order_by('-created_on')
		context['sidebar'] = Post.objects.filter(sidebar=True,status=1,footer=False).order_by('-created_on')
		context['footer'] = Post.objects.get(footer=True,status=1).content
		context['logo'] = Image.objects.get(slug='logo').image
		return context



