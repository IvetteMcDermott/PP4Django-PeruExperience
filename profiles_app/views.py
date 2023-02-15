from django.shortcuts import render
from .models import UserProfile
from django.views import generic, View
from .forms import ProfileForm
from django.contrib import messages


# Create your views here.

# def my_profile(request):

#     template_name = 'profiles/user_profile.html'
#     model = UserProfile
#     form_class = ProfileForm()

#     if request.method == 'POST':
#         user_obj = UserProfile.objects.get(user=request.user)

#         if form.is_valid(self, form):
#             form.instance.user = user_obj
#             form.save()
#             added = True
#             if added == True:
#                 messages.success(self.request, 'The new post has been add successfully!')
    
#         return render(request, 'profiles/user_profile.html', {'form': form_class, 'user': user_obj, })

def my_profile(request):
    """ VIEW FOR PROFILE PAGE """
    form = ProfileForm()
    user_obj = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_obj)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            updated = True
            if updated == True:
                messages.success(request, 'The profile had been updated successfully!')
    return render(request, 'profiles/user_profile.html', {'form': ProfileForm(), 'user': user_obj,})

