from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('profile', ProfileViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Name",
        default_version='v1',
        description="API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('login/', LoginGenericAPIView.as_view()),
    path('register/', RegisterGenericApiView.as_view()),
    path('comment/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # path('users/', UserListCreateAPIView.as_view(), name='user-list'),
    #  path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),

    path('documentation/', DocumentationListCreateAPIView.as_view(), name='documentation-list'),
    path('documentation/<int:pk>/', DocumentationRetrieveUpdateDestroyAPIView.as_view(), name='documentation-detail'),

    path('topics-documentation/', TopicsDocumentationListCreateAPIView.as_view(), name='topics-documentation-list'),
    path('topics-documentation/<int:pk>/', TopicsDocumentationRetrieveUpdateDestroyAPIView.as_view(),
         name='topics-documentation-detail'),

    path('test/', TestListCreateAPIView.as_view(), name='test-list'),
    path('test/<int:pk>/', TestRetrieveUpdateDestroyAPIView.as_view(), name='test-detail'),

    path('topics-test/', TopicsTestListCreateAPIView.as_view(), name='topics-test-list'),
    path('topics-test/<int:pk>/', TopicsTestRetrieveUpdateDestroyAPIView.as_view(), name='topics-test-detail'),

    path('about-us/', AboutUsListCreateAPIView.as_view(), name='about-us-list'),
    path('about-us/<int:pk>/', AboutUsRetrieveUpdateDestroyAPIView.as_view(), name='about-us-detail'),
    path('', include(router.urls))
    
    
]
