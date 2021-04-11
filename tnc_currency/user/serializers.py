from .models import User
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    """Serializer for User class"""
    
    retype_password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'retype_password', 'policies_agree', 'conditions_agree')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password',
                'min_length': 8
                }
            }
        }
    
    def create(self, validated_data):
        """overrides the create function to call the custom user manager"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """overrides the update fn to hash the password"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

    def validate(self, attrs):
        """validates and authenticates user"""
        email = attrs.get('email')
        password = attrs.get('password')
        retype_password = attrs.pop('retype_password')
        name = attrs.get('name')
        policies_agree = attrs.get('policies_agree')
        conditions_agree = attrs.get('conditions_agree')

        if password != retype_password:
            raise ValidationError('Passwords do not match')
        
        if policies_agree != True or conditions_agree != True:
            raise ValidationError('You must agree to policies and conditions')

        return attrs
