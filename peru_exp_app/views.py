
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.contrib import messages

from django.http import HttpResponse
from .models import PlacesList, Comment

from .forms import CommentForm, AddPlacesForm, UpdatePlacesForm

# Create your views here.


def landing_page(request):
    return render(request, 'index.html')


class Coast(ListView):

    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Coast')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Andes(ListView):
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='The Andes')
        template = "region_places.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Jungle(ListView):
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
        comment_form = CommentForm()
        context = {
            'context': place_data,
            'comments': comments,
            'commented': False,
            'comment_form': comment_form
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        place = PlacesList.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all().order_by('-date_created')
        template = 'place_information.html'

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.place = place_data
            comment.save()
        else:
            print(comment_form.errors)

        return render(request, template, {
            'context': place_data,
            'comments': comments,
            'commented': True,
            'comment_form': comment_form
        })


def comment_update_view(request, slug, pk):

    if request.method == 'POST':
        body = request.POST.get('body')
        # get the review to update
        comment = Comment.objects.get(id=pk)
        comment.body = body
        comment.save()

        place = comment.place_id
        place_info = PlacesList.objects.all()
        place_slug = get_object_or_404(place_info, pk=int(place))
        slug = place_slug.slug
    return redirect('place_information', slug=slug)


def comment_delete_view(request, slug, pk):

    if request.method == 'GET':
        comment = Comment.objects.get(id=pk)

        # get the review to update
        comment.delete()

        place = comment.place_id
        place_info = PlacesList.objects.all()
        place_slug = get_object_or_404(place_info, pk=int(place))
        slug = place_slug.slug
    return redirect('place_information', slug=slug)


def profile(request, *args, **kwargs):
    user = request.user
    template = 'user_profile.html'
    return render(request, template)


#class favourites(ListView):
#    def add_favourites(UserProfile, PlacesList, slug):
#        user = get_object_or_404(User, user=request.User)
#        if user.favourites.exists():
#            user.favourites.remove(request.user)
#        else:
#            user.favourites.add(request.user)

#    def favourites(request, user, slug):
#        user_modal = UserProfile
#        user = user_modal.objects.filter(user=request.user)
#        favs = user.favourites

#        place = PlacesList
#        place_items = place.objects.all()


# class AddPlace(View):
#    def AddPlace(self, request, *args, **kwargs):
#        place = PlacesList.objects.all()
#        template = 'add_place.html'
#        context = {
#            'add_place_form': AddPlacesForm()
#        }

#        return render(request, template, context)

#    def post(self, request, *args, **kwargs):
#        data = PlacesList.objects.all()

#        template = 'add_place.html'
#        add_place_form = AddPlacesForm()
#        if add_place_form.is_valid():
#            if not self.slug in data:
#                self.slug = slugify(self.place)
#            add_place_form.instance.place = request.place
#            new_place = add_place_form.save()
#            new_place.place = place
#            new_place.save()

#        return render(request, 'add_place.html', {'form': add_place_form})

def AddPlace(request):
    if request.method == 'POST':
        form = AddPlacesForm(request.POST)
        places = PlacesList.objects.all()
        if form.is_valid():
            form.save()
            message = messages.success(request, "Posted.")
            return redirect('/')
        else:
            message = messages.error(request, "It exist.")
            return redirect('/')

    elif request.method == 'GET':
        form = AddPlacesForm(request.GET)
    return render(request, 'add_place.html', {'form': form})


#def place_update_view(request, slug):

#    if request.method == 'POST':
#        place_data = request.POST.get('__all__')
#        # get the review to update
#        place = PlacesList.objects.all()
#        place_slug = get_object_or_404(place, slug=slug)
#        slug = place_slug.slug

#        place.info = info
#        place.save()

#    return redirect('place_information', slug)
