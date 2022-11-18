from django.urls import path
from .views import indexPageView
from .views import createPageView
from .views import updatePageView
from .views import readPageView
from .views import deleteRecipePageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("create/", createPageView, name="create"),
    path("update/", updatePageView, name="updateRecipe"),
    path("read/", readPageView, name="readRecipe"),
    path('deleteRecipe/<int:rec_id>/', deleteRecipePageView, name='deleteRecipe'), # Delete
]