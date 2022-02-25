from rest_framework import serializers
from .models import *


class Books_Section_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books_Section
        fields = ['parent_id', 'heading', 'paragraph']

