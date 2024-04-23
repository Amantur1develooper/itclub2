from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import User, Documentation, Comment, Topics_Documentation, Test, Topics_Test, AboutUs
from .serializers import CommentSerializer, UserSerializer, DocumentationSerializer, TopicsDocumentationSerializer, TestSerializer, \
    TopicsTestSerializer, AboutUsSerializer, LoginSerializer, RegisterUserSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .mixins import UltraModelViewSet




class LoginGenericAPIView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0]
            user_serializer = UserSerializer(instance=user, context={'request': request})
            return Response({
                **user_serializer.data,
                'token_key': token.key
            })
        return Response({'massage': 'The user is not found or the password is invalid'},
                        status=status.HTTP_400_BAD_REQUEST)


class RegisterGenericApiView(GenericAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.get_or_create(user=user)[0]
        user_serializer = UserSerializer(instance=user, context={'request': request})
        return Response({
            **user_serializer.data,
            'token': token.key,
        })


class ProfileViewSet(UltraModelViewSet):
    queryset = User.objects.all()
    # pagination_class = SimpleResultPagination
    serializer_class = ProfileSerializer
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    

# class UserListCreateAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


class DocumentationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DocumentationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Documentation.objects.all()
    serializer_class = DocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsDocumentationListCreateAPIView(generics.ListCreateAPIView):
    queryset = Topics_Documentation.objects.all()
    serializer_class = TopicsDocumentationSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class TopicsDocumentationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics_Documentation.objects.all()
    serializer_class = TopicsDocumentationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsTestListCreateAPIView(generics.ListCreateAPIView):
    queryset = Topics_Test.objects.all()
    serializer_class = TopicsTestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TopicsTestRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Topics_Test.objects.all()
    serializer_class = TopicsTestSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]


class AboutUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AboutUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class CommentListAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]