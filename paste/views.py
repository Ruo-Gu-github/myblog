from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import	HttpResponse, Http404, HttpResponseRedirect
from django.template import	Context, loader, RequestContext
from django.views import generic
from paste.models import Paste
from paste.forms import PasteForm
from django.core.urlresolvers import reverse

class IndexView(generic.ListView):
    model = Paste
    template_name = 'paste/paste_list.html'

class DetailView(generic.DetailView):
    model = Paste
    template_name = 'paste/paste_detail.html'

def create_info(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            success_url = reverse('paste:display_info')
            return HttpResponseRedirect(success_url)
        else:
            print (form.errors)
    else:
        form = PasteForm()

    return render_to_response('paste/paste_form.html', {'form': form}, context)
