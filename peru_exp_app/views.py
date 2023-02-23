from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView
from django.http import HttpResponseRedirect

from django.contrib import messages

from django.http import HttpResponse
from .models import Place, Comment, User

from .forms import CommentForm, AddPlacesForm, UpdatePlacesForm, UpdateCommentForm
from profiles_app.views import my_profile

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator


# Create your views here.


def landing_page(request):
    """ VIEW FOR LANDING PAGE - HOME """
    return render(request, 'index.html')


def admin(request):
    return render(request, 'admin')


def profile(request):
    return my_profile(request)


class Coast(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: COAST """
    model = Place
    queryset = Place.objects.filter(region='Coast')
    paginate_by = 4
    template_name = "region_coast.html"


class Andes(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: THE ANDES """
    model = Place
    queryset = Place.objects.filter(region='The Andes')
    paginate_by = 4
    template_name = "region_the_andes.html"


class Jungle(ListView):
    """ VIEW FOR LIST OF PLACES FILTER: JUNGLE """
    model = Place
    queryset = Place.objects.filter(region='Jungle')
    paginate_by = 4
    template_name = "region_jungle.html"


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
        updatecommentform = UpdateCommentForm()
        interested = False
        if place_data.interests.filter(id=self.request.user.id).exists():
            interested = True
        context = {
            'context': place_data,
            'comments': comments,
            'commented': False,
            'interested': interested,
            'comment_form': comment_form,
            'update_form': updateform,
            'update_comment': updatecommentform
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
    comment = Comment.objects.get(id=pk)
    updatecomment = UpdateCommentForm(instance=comment)
    if updatecomment.is_valid():
        updatedcommment = updatecomment.save(commit=False)
        # get the review to update
        updatedcommment.body = updatedcomment.instance.body
        updatedcommment.save()    
        messages.info(request, 'Your commented had been updated successfully!')
    context = { 'form': updatecomment}
    return redirect(request.META.get('HTTP_REFERER'), context)


def comment_delete_view(request, slug, pk):
    """ VIEW FOR DELETE A COMMENT IF AUTHOR OF IT OR ADMIN """
    if request.method == 'GET':
        comment = Comment.objects.get(id=pk)
        # get the review to update
        comment.delete()
        messages.warning(request, 'Your comment had been deleted successfully!')      
    return redirect(request.META.get('HTTP_REFERER'))


""" VIEWS FOR ADMIN FUNCTIONALITY IN THE HTML """


@method_decorator(staff_member_required, name='dispatch')
class AdminPage(CreateView):
    """ VIEW FOR ADD A NEW PLACE-POST """
    template_name = 'admin_page.html'
    model = Place
    form_class = AddPlacesForm

    def form_valid(self, request, form):
        form.save(commit=False)
        form.instance.user = self.request.user
        form.save()
        added = True
        if added == True:
            messages.success(self.request, 'The new post has been add successfully!')
        return render(request, 'admin_page', {'form': AddPlacesForm()})


def search_locations(request, page=1):
    """ VIEW FOR SEARCH A PLACE POST """
    if request.method == 'POST':
        region = request.POST.get('searchregion')
        search = Place.objects.all().filter(region=region)
        location = request.POST.get('searchlocation')
        search_result = search.filter(type_location=location).order_by('-date_created')
        template = 'search.html'
        context = {
                'searched': region,
                'search_result': search_result,
                'location': location,
            }
        return render(request, template, context)


def search_place(request):
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


@staff_member_required
def place_update_view(request, slug):
    """ VIEW FOR EDIT PLACES INFORMATION """
    form = UpdatePlacesForm()

    if request.method == 'POST':
        place = Place.objects.get(slug=slug)
        form = UpdatePlacesForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            updated = True
            if updated == True:
                messages.success(request, 'The post had been updated successfully!')

    return redirect(request.META.get('HTTP_REFERER'))


@staff_member_required
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


def search(request):
    """ VIEW FOR LANDING PAGE - HOME """
    return render(request, 'search.html')


""" USER PROFILE SECTION """


def interests(request, *args, **kwargs):
    """ VIEW FOR USER PROFILE """
    user = request.user
    template = 'interests.html'
    interests = Place.objects.filter(interests=request.user.id)
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


def handler404(request, exception):
    """ Custom 404 page """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Custom 500 page """
    return render(request, "errors/500.html", status=500)


def handler403(request, exception):
    """ Custom 403 page """
    return render(request, "errors/403.html", status=403)


def handler405(request, exception):
    """ Custom 405 page """
    return render(request, "errors/405.html", status=405)
