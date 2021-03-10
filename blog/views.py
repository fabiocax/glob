from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.
from django.views import generic
from .models import Post,Image,Menu
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

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

def post_detail(request, slug):
	template_name = 'post_detail.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(active=True)
	new_comment = None
	dados = Post.objects.filter(detach=True,status=1,footer=False).order_by('-created_on')
	menu = Menu.objects.filter(active=True)
	submenu = Post.objects.filter(status__gt=0).order_by('-created_on')
	sidebar = Post.objects.filter(sidebar=True,status=1,footer=False).order_by('-created_on')
	footer = Post.objects.get(footer=True,status=1).content
	logo = Image.objects.get(slug='logo').image
	# Comment posted
	if request.method == 'POST':
	    comment_form = CommentForm(data=request.POST)
	    if comment_form.is_valid():

	        # Create Comment object but don't save to database yet
	        new_comment = comment_form.save(commit=False)
	        # Assign the current post to the comment
	        new_comment.post = post
	        # Save the comment to the database
	        new_comment.save()
	else:
	    comment_form = CommentForm()

	return render(request, template_name, {
		'post': post,
		'comments': comments,
		'new_comment': new_comment,
		'comment_form': comment_form,
		'dados':dados,
		'menu':menu,
		'submenu':submenu,
		'sidebar':sidebar,
		'footer':footer,
		'logo':logo,
		})



