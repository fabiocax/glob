from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
from django.views import generic
from .models import Post,Image,Menu



class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1,detach=False,sidebar=False,footer=False).order_by('-created_on')
	template_name = 'index.html'
	paginate_by = 3
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['dados'] = Post.objects.filter(detach=True,status=1,footer=False).order_by('-created_on')
		context['menu'] = Menu.objects.filter(active=True)
		context['submenu'] = Post.objects.filter(status__gt=0).order_by('-created_on')
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
		context['menu'] = Menu.objects.filter(active=True)
		context['submenu'] = Post.objects.filter(status__gt=0).order_by('-created_on')
		context['sidebar'] = Post.objects.filter(sidebar=True,status=1,footer=False).order_by('-created_on')
		context['footer'] = Post.objects.get(footer=True,status=1).content
		context['logo'] = Image.objects.get(slug='logo').image
		return context



class PostSearch(generic.ListView):
	queryset = Post.objects.filter(status=1,detach=False,sidebar=False,footer=False).order_by('-created_on')
	template_name = 'search.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			search=self.request.GET.get('search' )
			if not search == '':
				context['pesquisa'] = Post.objects.filter(status=1,detach=False,sidebar=False,footer=False,content__contains=search)[:3]
		except:
			search="null"
		
		
		context['dados'] = Post.objects.filter(detach=True,status=1,footer=False).order_by('-created_on')
		context['sidebar'] = Post.objects.filter(sidebar=True,status=1,footer=False).order_by('-created_on')
		context['menu'] = Menu.objects.filter(active=True)
		context['submenu'] = Post.objects.filter(status__gt=0).order_by('-created_on')
		context['footer'] = Post.objects.get(footer=True,status=1).content
		context['logo'] = Image.objects.get(slug='logo').image
		return context
