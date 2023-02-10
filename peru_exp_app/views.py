from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from django.http import HttpResponseRedirect

from django.contrib import messages

from django.http import HttpResponse
from .models import Place, Comment, User

from .forms import CommentForm, AddPlacesForm, UpdatePlacesForm
from profiles_app.views import MyProfile

# Create your views here.


def landing_page(request):
    """ VIEW FOR LANDING PAGE - HOME """
    return render(request, 'index.html')


def admin(request):
    return render(request, 'admin')


def profile(request):
    return MyProfile(request)


class Coast(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: COAST """

    model = Place
    queryset = Place.objects.filter(region='Coast')
    paginate_by = 4
    template_name = "region_coast.html"


""" LOCATIONS AT COAST FILTERS """


class ArqueologicCoast(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Coast', type_location='Arqueologic')
        template = "region_coast.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class BeachCoast(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: BEACH """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Coast', type_location='Beach')
        template = "region_coast.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class NatureCoast(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: NATURE """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Coast', type_location='Nature')
        template = "region_coast.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class CulturalCoast(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Coast', type_location='Cultural')
        template = "region_coast.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Andes(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: THE ANDES """
 
    model = Place
    queryset = Place.objects.filter(region='The Andes')
    paginate_by = 4
    template_name = "region_the_andes.html"


""" LOCATIONS AT THE ANDES FILTERS """


class ArqueologicAndes(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='The Andes', type_location='Arqueologic')
        template = "region_the_andes.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class NatureAndes(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: NATURE """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='The Andes', type_location='Nature')
        template = "region_the_andes.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class CulturalAndes(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='The Andes', type_location='Cultural')
        template = "region_the_andes.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class Jungle(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: JUNGLE """
    model = Place
    queryset = Place.objects.filter(region='Jungle')
    paginate_by = 4
    template_name = "region_jungle.html"


""" LOCATIONS AT JUNGLE FILTERS """


class ArqueologicJungle(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Jungle', type_location='Arqueologic')
        template = "region_jungle.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class NatureJungle(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: NATURE """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Jungle', type_location='Nature')
        template = "region_jungle.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class CulturalJungle(ListView):
    """ VIEW FOR LIST OF COAST PLACES FILTER: ARQUEOLOGIC """

    def get(self, request, *args, **kwargs):
        model = Place
        data_filtered = Place.objects.filter(region='Jungle', type_location='Cultural')
        template = "region_jungle.html"
        paginate_by = 6
        context = {
            'context': data_filtered
        }

        return render(request, template, context)


class PlaceInformation(View):
    """ VIEW FOR DETAILED INFORMATION OF THE SELECTED PLACE """
    """ FROM THE HTML FOR THIS VIEW A PLACE-POST CAN BE COMMENTED BY REGULAR REGISTERED USERS """
    """ FROM THE HTML FOR THIS VIEW A PLACE-POST CAN BE EDIT OR DELETE, REDIRECTING YOU TO THE LANDING - HOME PAGE """
    def get(self, request, slug, *args, **kwargs):
        place = Place.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all().order_by('date_created')
        template = 'place_information.html'
        comment_form = CommentForm()
        updateform = UpdatePlacesForm(instance=place_data)
        interested = False
        if place_data.interests.filter(id=self.request.user.id).exists():
            interested = True
        context = {
            'context': place_data,
            'comments': comments,
            'commented': False,
            'interested': interested,
            'comment_form': comment_form,
            'update_form': updateform
        }
        return render(request, template, context)

    def post(self, request, slug, *args, **kwargs):
        """ VIEW FOR POST A COMMENT """
        place = Place.objects.all()
        place_data = get_object_or_404(place, slug=slug)
        comments = place_data.comments.all().order_by('-date_created')
        template = 'place_information.html'
        comment_form = CommentForm(data=request.POST)
        interested = False
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.place = place_data
            comment.save()
            commented = True

            if commented == True:
                messages.success(request, 'Your comment had been add successfully!')
        else:
            comment_form()

        if place_data.interests.filter(id=self.request.user.id).exists():
            interested = True

        return redirect(request.META.get('HTTP_REFERER'))


def comment_update_view(request, slug, pk):
    """ VIEW FOR EDIT A COMMENT IF AUTHOR OF IT """
    if request.method == 'POST':
        body = request.POST.get('body')
        # get the review to update
        comment = Comment.objects.get(id=pk)
        comment.body = body
        comment.save()
        updated = True
        place = comment.place_id
        place_info = Place.objects.all()
        place_slug = get_object_or_404(place_info, pk=int(place))
        slug = place_slug.slug
        if updated == True:
            messages.info(request, 'Your commented had been updated successfully!')
    return redirect(request.META.get('HTTP_REFERER'))


def comment_delete_view(request, slug, pk):
    """ VIEW FOR DELETE A COMMENT IF AUTHOR OF IT OR ADMIN """
    if request.method == 'GET':
        comment = Comment.objects.get(id=pk)

        # get the review to update
        comment.delete()
        deleted = True
        place = comment.place_id
        place_info = Place.objects.all()
        place_slug = get_object_or_404(place_info, pk=int(place))
        slug = place_slug.slug
        if deleted == True:
            messages.warning(request, 'Your comment had been deleted successfully!')      
    return redirect(request.META.get('HTTP_REFERER'))


""" VIEWS FOR ADMIN FUNCTIONALITY IN THE HTML """


class AdminPage(CreateView):
    """ VIEW FOR ADD A NEW PLACE-POST """
    template_name = 'admin_page.html'
    model = Place
    form_class = AddPlacesForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        added = True
        if added == True:
            messages.success(self.request, 'The new post has been add successfully!')
        return redirect('/adminpage/')


def SearchResults(request):
    """ VIEW FOR SEARCH A PLACE POST """
    if request.method == 'POST':
        search = request.POST.get('search')
        search_result = Place.objects.all().filter(name__icontains=search)
        template = 'search.html'
        context = {
            'searched': search,
            'search_result': search_result
        }
        return render(request, template, context)


#THIS IS WORKING TO SAVE BUT DOESNT SHOW IN THE FORM THE DATA AND HTML NEEDS TO BE CALL BY FIELD
# class place_update_view(LoginRequiredMixin, UserPassesTestMixin, UpdateView):


def place_update_view(request, slug):
    """ VIEW FOR EDIT PLACES INFORMATION """
    form = UpdatePlacesForm()

    if request.method == 'POST':
        lugar = Place.objects.get(slug=slug)
        form = UpdatePlacesForm(request.POST, request.FILES, instance=lugar)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            updated = True
            if updated == True:
                messages.success(request, 'The post had been updated successfully!')

    return redirect(request.META.get('HTTP_REFERER'))


def place_delete_view(request, slug):
    """ VIEW FOR DELETE A POST, JUST ADMIN HAS ACCESS TO """
    if request.method == 'GET':
        place = Place.objects.get(slug=slug)

        # get the review to update
        place.delete()
        deleted = True
        if deleted == True:
            messages.success(request, 'The post has been deleted successfully!')

    return redirect('/adminpage/')


""" USER PROFILE SECTION """


def interests(request, *args, **kwargs):
    """ VIEW FOR USER PROFILE """
    user = request.user
    template = 'interests.html'
    interests = Place.objects.filter(interests=request.user.id)
    paginate_by = 6
    context = {
        'interests': interests,
    }
    return render(request, template, context)


def add_interest(request, slug):
    interested = False
    if request.method == 'POST':
        place = get_object_or_404(Place, slug=slug)
        if place.interests.filter(id=request.user.id).exists():
            place.interests.remove(request.user)
            messages.success(request, 'Place removed from interests')
        else:
            place.interests.add(request.user)
            interested = True
            messages.success(request, 'Place added to interests')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
