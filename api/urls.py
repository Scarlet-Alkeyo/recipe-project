
from .views import CategoriesListView,UsersListView,Shopping_listListView,ReminderListView,Food_itemsListView,IngredientsListView,SharingListView
from django.contrib import admin
from .views import CategoriesView
from .views import UsersDetailView
from .views import Shopping_listDetailView
from .views import ReminderDetailView
from .views import Food_itemsDetailView
from .views import IngredientsDetailView
from .views import SharingDetailView


urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('shopping_list/', Shopping_listListView.as_view(), name='shopping_list-list'),
    path('food_items/', Food_itemsListView.as_view(), name='food_items-list'),
    path('ingredients/', IngredientsListView.as_view(), name='ingredients-list'),
    path('sharing/', SharingListView.as_view(), name='sharing-list'),
    
    path('categories/', CategoriesListView.as_view(), name='category-list'),
    path("users/<int:id>/", UsersListView.as_view(), name = "user_list_view"),
    path("shopping_list/<int:id>/", Shopping_listDetailView.as_view(), name = "shopping_list_view"),
    path("food_items/<int:id>/",Food_itemsDetailView.as_view(), name = "food_item_list_view"),
    path("reminder/<int:id>/", ReminderDetailView.as_view(), name = "reminder_list_view"),
    path("sharing/<int:id>/", SharingDetailView.as_view(), name = "course_list_view"),
]