from django.shortcuts import render
import re
import markdown2
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util


def index(request):

    if(request.GET):
        query = request.GET['q']
        if(query):
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': query}))
        else:
            return HttpResponseRedirect(reverse("encyclo:index"))
        
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):

    if(request.GET):
        query = request.GET['q']
        if(query):
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': query}))
        else:
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': entry}))

    content = util.get_entry(entry)

    if (content == None):
        return render(request, "encyclopedia/notfound.html", {
            "title": entry + " - Wiki",
            "query": entry
        })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "title": entry + " - Wiki",
            "content": markdown2.markdown(content)
    })
