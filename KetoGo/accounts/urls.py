from django.urls import path, include
from KetoGo.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, DetailsUserView, EditUserView, \
    DeleteUserView, GetAllUsersCreateUser, GetUpdateDeleteSingleUser

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),

    path('profile/<int:pk>/', include([
        path('', DetailsUserView.as_view(), name='details user'),
        path('edit/', EditUserView.as_view(), name='edit user'),
        path('delete/', DeleteUserView.as_view(), name='delete user'),
    ])),
    path('api/', include([
        path('', GetAllUsersCreateUser.as_view(), name='get or create user'),
        path('<int:pk>/', GetUpdateDeleteSingleUser.as_view(), name='get put del user'),
    ])),
)

# handler500 = my_handler500
