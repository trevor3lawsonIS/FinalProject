from django.urls import path
from .views import indexPageView
from .views import createPageView
from .views import updatePageView
from .views import readPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("create", createPageView, name="create"),
    path("update", updatePageView, name="update"),
    path("read", readPageView, name="read"),
]