from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import	HttpResponse, Http404, HttpResponseRedirect
from django.template import	Context, loader, RequestContext
from blogs.models import Blogspost
from django.views import generic
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# def	listing(request):
#     content_list = Blogspost.objects.all()
#     paginator =	Paginator(content_list,	5)
#     page = request.GET.get('page')
#     try:
#         contents = paginator.page(page)
#     except PageNotAnInteger:
#         contents = paginator.page(1)
#     except EmptyPage:
#         contents = paginator.page(paginator.num_pages)
#     return render_to_response('blogs/list.html', {"contents": contents})

def index(request):
    blogs_list = Blogspost.objects.order_by('-pub_date').all()
    paginator = Paginator(blogs_list, 8)
    page = request.GET.get('page')
    try:
        latest_blogs_list =  paginator.page(page)
    except PageNotAnInteger:
        latest_blogs_list = paginator.page(1)
    except EmptyPage:
        latest_blogs_list = paginator.page(paginator.num_pages)
    return render_to_response('blogs/index.html',{"latest_blogs_list":latest_blogs_list})





# def	index(request):
#     latest_blogs_list = Blogspost.objects.order_by('-pub_date')[:10]
#     context = {'latest_blogs_list': latest_blogs_list,}
#     return render(request, 'blogs/index.html', context)
#
def	detail(request,	blogs_id):
    blog = get_object_or_404(Blogspost, pk=blogs_id)
    return render(request, 'blogs/detail.html', {'blog': blog})
