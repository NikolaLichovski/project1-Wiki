# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django import forms

from . import util
import markdown2

from random import choice

class NewPageForm(forms.Form):
    title = forms.CharField
    content = forms.CharField(widget=forms.Textarea)


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


# def wiki(request, entry_name):
#     if util.get_entry(entry_name) is not None:
#         html = util.convert_md(entry_name)
#         return render(request, "encyclopedia/pages.html", {
#             "title": entry_name, "body": html
#         })
#     else:
#         return render(request, "encyclopedia/pages.html", {
#             "title": "ERROR", "body": "THIS PAGE IS NOT AVAILABLE."
#         })

def wiki(request, entry_name):
    md = util.get_entry(entry_name)
    if md is not None:
        html = markdown2.markdown(md)
        return render(request, "encyclopedia/pages.html", {
            "title": entry_name, "body": html
        })
    else:
        return render(request, "encyclopedia/pages.html", {
            "title": "ERROR", "body": "Requested page was not Found."
        })


def search(request):
    entries_list = util.list_entries()
    query = request.GET.get("q", "")
    if query in entries_list:
        return redirect(wiki, query)
    else:
        results = [entry for entry in entries_list if query.lower() in entry.lower()]
        return render(request, "encyclopedia/index.html", {
            "entries": results
        })


def random_page(request):
    return wiki(request, choice(util.list_entries()))


# def new_page(request):
#     if request.method == "POST":
#         form = NewPageForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = "# " + title + "\n" + form.cleaned_data['content']
#             if title not in util.list_entries():
#                 util.save_entry(title, content)
#                 return HttpResponseRedirect("/wiki/" + title)
#             else:
#                 return render(request, "encyclopedia/new_page.html", {
#                     "entry": "Entry for " + title + " already exists!",
#                     "title": "Error"
#                 })
#     else:
#         return render(request, "encyclopedia/new_page.html", {
#             "form": NewPageForm(),
#             "title": "Create New Page"
#         })

