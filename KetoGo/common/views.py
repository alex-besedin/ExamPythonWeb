from django.contrib.auth import mixins, get_user_model
from django.shortcuts import render, redirect

UserModel = get_user_model()


def index(request):
    return render(request, 'common/home-page.html')

# def get_profile():
#     try:
#         profile = Profile.objects.get()
#         return profile
#     except Profile.DoesNotExist as ex:
#         return None


# def index(request):
# profile = get_profile()
# print(profile)
# if profile is None:
#     return redirect('accounts/profile-edit-page', pk=request.user.pk)

# context = {
#     'profile': profile,
# }

# return render(request, 'common/home-page.html')


# class UsersListView(generic.ListView):
#     model = UserModel
#     template_name = 'common/home-page.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#
#         context['user'] = self.request.user
#         # context['has_email'] = UserModel.has_email(self.request.user)
#
#         return context


# def index(request):
# when still no users:
# search_form = SearchPhotoForm(request.GET)
# search_string = None
# if search_form.is_valid():
#     search_string = search_form.cleaned_data['pet_name']

# photos = Photo.objects.all()
# if search_string:
#     photos = photos.filter(tagged_pets__name__icontains=search_string)
# photos = [apply_likes_count(photo) for photo in photos]
# photos = [apply_user_liked_photos(photo) for photo in photos]

# context = {
#     'photos': photos,
#     # 'comment_form': PhotoCommentForm(),
#     'search_form': search_form,
# }

# return render(
#     request,
#     'common/home-page.html',
#     # context,
# )
