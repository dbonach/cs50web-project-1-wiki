from django.shortcuts import render
import re
import markdown2
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wiki(request, entry):
    content = util.get_entry(entry)
    if (content == None):
        return render(request, "encyclopedia/notfound.html", {
            "entry": entry + " - Wiki"
        })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "entry": entry + " - Wiki",
            "content": markdown2.markdown(content)
    })