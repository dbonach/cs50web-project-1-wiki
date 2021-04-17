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
    # print("###", end=" ")
    # print(request.path)
    # entry = re.sub("/wiki/", "", request.path)
    # print(entry)
    content = util.get_entry(entry)
    # print(entry + "- wiki")
    if (content == None):
        return render(request, "encyclopedia/notfound.html", {
            "entry": entry + " - wiki"
        })
    # print(markdown2.markdown(text))
    return render(request, "encyclopedia/wiki.html", {
        "entry": entry + " - wiki",
        "content": markdown2.markdown(content)
    })