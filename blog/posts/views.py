from django.shortcuts import render
from django.http import Http404, HttpResponse
import datetime
from .models import Topic, Category, Post

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def topic_list(request):
    # pobieramy wszystkie obiekty Topic z bazy poprzez QuerySet

    topics = Topic.objects.all()
    return render(request,
                  "posts/topic/list.html",
                  {'topics': topics})

def topic_detail(request, id):
    # pobieramy konkretny obiekt Topic
    topic = Topic.objects.get(id=id)

    try:
        topic = Topic.objects.get(id=id)
    except Topic.DoesNotExist:
        raise Http404("Obiekt Topic o podanym id nie istnieje")

    return render(request,
                  "posts/topic/detail.html",
                  {'topic': topic})

def category_detail(request, id):
    Category = Category.objects.all()

    try:
        category = category.objects.get(id=id)
    except category.DoesNotExist:
        raise Http404("Obiekt Category o podanym id nie istnieje")
    return render(request,
                  "posts/category/detail.html",
                  {'category': category})
