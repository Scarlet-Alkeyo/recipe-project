from rest_framework import serializers
from categories.models import Categories
from reminder.models import Reminder
from sharing.models import Sharing
from users.models import Users
from shopping_list.models import Shopping_list
from food_items.models import Food_items
from ingredients.models import Ingredients
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharing
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class   IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class   Food_itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_items
        fields = '__all__'


class   Shopping_listSerializer(serializers.ModelSerializer):
    class Meta:
        model =Shopping_list
        fields = '__all__'