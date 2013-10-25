import math
# from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse

from blog.models import Post
from blog.forms import ContactForm
from django.contrib.comments.models import Comment

recent_posts_count = 7
recent_comments_count = 7
posts_per_page = 4

def basic_context():
    ordered_posts = Post.objects.order_by('-pub_date')
    recent_posts = ordered_posts[:recent_posts_count]
    ordered_comments = Comment.objects.order_by('-submit_date')
    recent_comments = ordered_comments[:recent_comments_count]
    return {'ordered_posts': ordered_posts,
            'recent_posts': recent_posts,
            'recent_comments': recent_comments}

def index(request):
    return page(request, 1)

def page(request, page_num):
    page_num = int(page_num)
    beg, end = posts_per_page * page_num - posts_per_page, \
               posts_per_page * page_num
    context = basic_context()
    ordered_posts = context['ordered_posts']
    pages_count = int(math.ceil(ordered_posts.count()*1.0/posts_per_page))
    context.update(selected_posts=ordered_posts[beg:end],
                   pages_range=range(1, pages_count+1),
                   page_num=page_num)
    return render(request, 'blog/index.html', context)

def archives(request):
    return render(request, 'blog/archives.html', basic_context())

def about(request):
    return render(request, 'blog/about.html', basic_context())

def detail(request, year, month, day, title):
    post = get_object_or_404(Post, 
                             pub_date__year=int(year), 
                             pub_date__month=int(month), 
                             pub_date__day=int(day), 
                             title=title)
    context = basic_context()
    context.update(post=post)
    return render(request, 'blog/detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipients = ['yangwenhaogdut@163.com']
            if cc_myself:
                recipients.append(sender)
            send_mail(sender+':'+subject, message, 'yangwenhaogdut@163.com', recipients)
            return HttpResponseRedirect(reverse('blog:thanks'))
    else:
        form = ContactForm()
    context = basic_context()
    context.update(form=form)
    return render(request, 'blog/contact.html', context) 

def thanks(request):
    return render(request, 'blog/thanks.html', basic_context())

# def IndexView(generic.ListView):
#     template_name = 'blog/index.html'
#     context_object_name = 'latest_posts'
#     queryset = Post.objects.order_by('-pub_date')[:5]

# def DetailView(generic.DetailView):
#     slug_field = 'title'
#     slug_url_kwarg = 'title'
#     template_name = 'blog/detail.html'
#     context_object_name = 'post'

#     def get_queryset(self):
#         return Post.objects.filter(pub_date__year=self.kwargs['year'],
#                                    pub_date__month=self.kwargs['month'],
#                                    pub_date__day=self.kwargs['day'])
