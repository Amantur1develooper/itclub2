from rest_framework import serializers
from .models import User, Documentation, Topics_Documentation, Test, Comment, Topics_Test, AboutUs
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Этот email уже занят.")
        return value
    
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'firstname', 'lastname', 'password', 'phone', 'image',)

    def validate(self, attrs):
        copied = attrs.copy()
        copied.pop('image')
        for item in copied:
            if not item[1]:
                raise ValidationError({
                    item[0]: [
                        f'{item[0]} не может быть пустым'
                    ]
                })
                
        return attrs
    
    
class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(validators=[validate_password])

    class Meta:
        model = User
        fields = (
            'email',
            'firstname',
            'lastname',
            'image',
            'phone',
            'password',
        )
        extra_kwargs = {
            'lastname':{'required':True},
            'firstname':{'required':True},
            'phone':{'required':True}
        }
    
    def validate(self, attrs):
        copied = attrs.copy()
        copied.pop('image')
        for item in copied:
            if not item[1]:
                raise ValidationError({
                    item[0]: [
                        f'{item[0]} не может быть пустым'
                    ]
                })
                
        return attrs
    
    
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class DocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documentation
        fields = '__all__'

    def validate(self, data):
        if not data.get('description'):
            raise serializers.ValidationError("Поле 'description' не может быть пустым.")
        return data


class TopicsDocumentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics_Documentation
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TopicsTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics_Test
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'
