from django.contrib.auth.models import User, Group
from rest_framework import serializers
from services.models import services


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class servicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = services
        fields = ('service_id','service_name','service_version','service_port','service_port','remark')