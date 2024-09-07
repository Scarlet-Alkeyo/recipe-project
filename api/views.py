# from  rest_framework.response import Response
# from rest_framework.views import APIView
# from categories.models import Categories
# from reminder.models import Reminder
# from food_items.models import Food_items
# from ingredients.models import Ingredients
# from sharing.models import Sharing
# from shopping_list.models import Shopping_list
# from users.models import Users
# from rest_framework.response import Response
# from .serializer import CategorySerializer
# from .serializer import UsersSerializer
# from .serializer import ReminderSerializer
# from .serializer import IngredientsSerializer  
# from .serializer import Shopping_listSerializer
# from .serializer import Food_item_listSerializer
# from .serializer import  Sharing_listSerializer


# class CategoriesListView(APIView):
#     def post(self, request):
#         serializer = CategoriesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         categories = Categories.objects.all()
#         serializer = CategoriesSerializer(categories, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         category = get_object_or_404(Categories, id=id)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    




# class Food_itemsListView(APIView):
#     def post(self, request):
#         serializer = Food_itemsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         food_items = Food_items.objects.all()
#         serializer = Food_itemsSerializer(reminder, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         food_items = get_object_or_404(food_items, id=id)
#         food_items.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



# class ReminderListView(APIView):
#     def post(self, request):
#         serializer = ReminderSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         reminder = Reminder.objects.all()
#         serializer = ReminderSerializer(reminder, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         reminder = get_object_or_404(reminder, id=id)
#         reminder.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    




# class SharingListView(APIView):
#     def post(self, request):
#         serializer = SharingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         sharing = Sharing.objects.all()
#         serializer = SharingSerializer(sharing, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         sharing = get_object_or_404(reminder, id=id)
#         sharing.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# class Shopping_listListView(APIView):
#     def post(self, request):
#         serializer = Shopping_listSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         Shopping_list = Shopping_list.objects.all()
#         serializer = Shopping_listSerializer(Shopping_list, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         shopping_list = get_object_or_404(reminder, id=id)
#         shopping_list.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# class IngredientsListView(APIView):
#     def post(self, request):
#         serializer = IngredientsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         ingredients = Ingredients.objects.all()
#         serializer = IngredientsSerializer(ingredients, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         ingredients = get_object_or_404(ingredients, id=id)
#         ingredients.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    



# class UsersListView(APIView):
#     def post(self, request):
#         serializer = UsersSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def get(self, request):
#         users = Users.objects.all()
#         serializer = UsersSerializer(users, many=True)
#         return Response(serializer.data)
#     def delete(self, request, id):
#         usersListView = get_object_or_404(users, id=id)
#         users.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    





from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from categories.models import Categories
from reminder.models import Reminder
from food_items.models import Food_items
from ingredients.models import Ingredients
from sharing.models import Sharing
from shopping_list.models import Shopping_list
from users.models import Users
from .serializer import (
    CategoriesSerializer,
    UsersSerializer,
    ReminderSerializer,
    IngredientsSerializer,
    Shopping_listSerializer,
    Food_itemsSerializer,
    SharingSerializer
)


class CategoriesListView(APIView):
    def post(self, request):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        category = get_object_or_404(Categories, id=id)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FoodItemsListView(APIView):
    def post(self, request):
        serializer = Food_itemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        food_items = Food_items.objects.all()
        serializer = Food_itemsSerializer(food_items, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        food_item = get_object_or_404(Food_items, id=id)
        food_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReminderListView(APIView):
    def post(self, request):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        reminder = get_object_or_404(Reminder, id=id)
        reminder.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SharingListView(APIView):
    def post(self, request):
        serializer = SharingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        sharing = Sharing.objects.all()
        serializer = SharingSerializer(sharing, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        sharing_item = get_object_or_404(Sharing, id=id)
        sharing_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShoppingListView(APIView):
    def post(self, request):
        serializer = Shopping_listSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        shopping_list = Shopping_list.objects.all()
        serializer = Shopping_listSerializer(shopping_list, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        shopping_item = get_object_or_404(Shopping_list, id=id)
        shopping_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IngredientsListView(APIView):
    def post(self, request):
        serializer = IngredientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        ingredients = Ingredients.objects.all()
        serializer = IngredientsSerializer(ingredients, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        ingredient = get_object_or_404(Ingredients, id=id)
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UsersListView(APIView):
    def post(self, request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        user = get_object_or_404(Users, id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
