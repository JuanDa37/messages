from django.urls import path
from . import views

urlpatterns = [
    path("messages/", view = views.getMessages, name = "get-messages"),
    path("messages/created/", view = views.createMessages, name = "create-messages"),
    path("authors/<int:author_id>/", views.update_profile_picture, name="update-profile-picture"),
    path("authors/<str:username>/", views.get_author_by_username, name="get_author_by_username"),
]