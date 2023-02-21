from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.views import generic, View
from django.views.generic import UpdateView, ListView, CreateView

from .forms import UpProfileForm
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.


def my_profile(request):
    """ RENDER THE PROFILE FUNCTION AND GIVE ACCESS TO THE FORM WHERE CAN ENTER/UPDATE IT """
    """ THE PROFILE IS CREATED BY SIGNAL, SO DOESNT HAVE ANYOTHER INFORMATION THAN THE USER """
    user_obj = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UpProfileForm(request.POST, request.FILES, instance=user_obj)

        if form.is_valid():
            form.save()
            messages.success(request, 'The profile had been updated successfully!')
    else:
        form = UpProfileForm(instance=user_obj)
    return render(request, 'profiles_app/user_profile.html', {'form': form, 'user': user_obj, })


class Community(ListView):
    """ DISPLAYS ALL THE PROFILES IN THE MODAL FOR REGISTER USERS """

    model = UserProfile
    queryset = model.objects.exclude(user_name__exact="")
    paginate_by = 4
    template_name = "profiles_app/community.html"
