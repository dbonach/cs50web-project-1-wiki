from django.shortcuts import render
import re
import markdown2
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util


def index(request):
    '''
    Check if request has a query parameter, if the parameter
    is an empty string the page is redirected to "index" path
    with no query parameters and then tha page is reloaded, if
    it's a non-empty string the request is redirected to "entry"
    path with the parameter as argument.
    '''
    if(request.GET):
        query = request.GET['q']
        if(query):
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': query}))
        else:
            return HttpResponseRedirect(reverse("encyclo:index"))

    # If there's no query parameters index is rendered
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):

    '''
    Requests with a query occurs when there's a search query from
    index or wiki pages.
    When there's a non-empty query the request will be redirected to "entry"
    path with the query as "entry" argument, resulting in "wiki/query/".
    If there's an empty string in the query it'll be redirect to "entry"
    path with entry as a parameter, resulting in a page reload.
    '''
    if(request.GET):
        query = request.GET['q']
        if(query):
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': query}))
        else:
            return HttpResponseRedirect(reverse("encyclo:entry", kwargs={'entry': entry}))

    # Get the content for a given entry
    content = util.get_entry(entry)

    # If there's no matching entry, notFound is called to handle it
    if (content == None):
        return notFound(request, entry)

    # Else, render the page with its entry content
    else:
        return render(request, "encyclopedia/wiki.html", {
            "title": entry + " - Wiki",
            "content": markdown2.markdown(content)
    })

def notFound(request, entry):

        # Get all saved entries
        items = util.list_entries()

        '''
        If an item from util.list_entries() has entry as
        a sub string, that item is append to entries.
        '''
        entries = []

        for item in items:
            if re.search(entry, item, re.IGNORECASE):
                entries.append(item)

        '''
        Render a search result page with all matching entries or
        with a message informing that there's no similar page.
        '''
        return render(request, "encyclopedia/notfound.html", {
            "title": entry + " - Wiki",
            "query": entry,
            "entries": entries
        })