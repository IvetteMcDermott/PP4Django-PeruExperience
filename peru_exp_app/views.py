from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from .models import PlacesList, Comment

from .forms import CommentForm

# Create your views here.


def landing_page(request):
    return render(request, 'index.html')


class Coast(View):

    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Coast')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Andes(View):
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='The Andes')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Jungle(View):
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Jungle')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class PlaceInformation(View):

    def get(self, request, slug, *args, **kwargs):
        place = PlacesList.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all().order_by('date_created')
        template = 'place_information.html'
        context = {
            'context': place_data,
            'comments': comments,
            'commented': False,
            'comment_form': CommentForm()
        }

        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        place = PlacesList.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all()
        template = 'place_information.html'

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.author = request.user.username
            comment = comment_form.save(commit=False)
            comment.place_data = place_data
            comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template, {
            'context': place_data,
            'comments': comments,
            'commented': True,
            'comment_form': comment_form
        })
