from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.contrib import messages

from django.http import HttpResponse
from .models import PlacesList, Comment

from .forms import CommentForm, AddPlacesForm, UpdatePlacesForm

# Create your views here.


def landing_page(request):
    """ VIEW FOR LANDING PAGE - HOME """
    return render(request, 'index.html')


class Coast(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: COAST """

    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Coast')
        template = "region_places.html"
        paginate_by = 3
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Andes(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: THE ANDES """
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='The Andes')
        template = "region_places.html"
        paginate_by = 3
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Jungle(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: JUNGLE """
    def get(self, request, *args, **kwargs):
        model = PlacesList
        data_filtered = PlacesList.objects.filter(region='Jungle')
        template = "region_places.html"
        paginate_by = 3
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class PlaceInformation(View):
    """ VIEW FOR DETAILED INFORMATION OF THE SELECTED PLACE """
    """ FROM THE HTML FOR THIS VIEW A PLACE-POST CAN BE COMMENTED BY REGULAR REGISTED USERS """
    """ FROM THE HTML FOR THIS VIEW A PLACE-POST CAN BE EDIT OR DELETE, REDIRECTING YOU TO THE LANDING - HOME PAGE """
    def get(self, request, slug, *args, **kwargs):
        place = PlacesList.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all().order_by('date_created')
        template = 'place_information.html'
        comment_form = CommentForm()
        updateform = UpdatePlacesForm(instance=place_data)
        context = {
            'context': place_data,
            'comments': comments,
            'commented': False,
            'comment_form': comment_form,
            'update_form': updateform
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        """ VIEW FOR POST A COMMENT """
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
    """ VIEW FOR EDIT A COMMENT IF AUTHOR OF IT """
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
    """ VIEW FOR DELETE A COMMENT IF AUTHOR OF IT OR ADMIN """
    if request.method == 'GET':
        comment = Comment.objects.get(id=pk)

        # get the review to update
        comment.delete()

        place = comment.place_id
        place_info = PlacesList.objects.all()
        place_slug = get_object_or_404(place_info, pk=int(place))
        slug = place_slug.slug
    return redirect('place_information', slug=slug)


""" VIEWS FOR ADMIN FUNCTIONALITY IN THE HTML """


class AddPlace(LoginRequiredMixin, CreateView):
    """ VIEW FOR ADD A NEW PLACE-POST """
    template_name = 'add_place.html'
    model = PlacesList
    form_class = AddPlacesForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddPlace, self).form_valid(form)


#THIS IS WORKING TO SAVE BUT DOESNT SHOW IN THE FORM THE DATA AND HTML NEEDS TO BE CALL BY FIELD
# class place_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

def place_update_view(request, slug):
    """ VIEW FOR EDIT PLACES INFORMATION """
    form = UpdatePlacesForm()

    if request.method == 'POST':
        information = request.POST.get('info')
        # get the review to update
        place = PlacesList.objects.get(slug=slug)
        place.info = information
        place.save()

    return redirect("/")


def place_delete_view(request, slug):
    """ VIEW FOR DELETE A POST, JUST ADMIN HAS ACCESS TO """
    if request.method == 'GET':
        place = PlacesList.objects.get(slug=slug)

        # get the review to update
        place.delete()

    return redirect('/')


""" USER PROFILE SECTION """


def profile(request, *args, **kwargs):
    """ VIEW FOR USER PROFILE """
    user = request.user
    template = 'user_profile.html'
    return render(request, template)


