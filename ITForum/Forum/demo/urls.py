from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryListCreateAPIView,
    CategoryRetrieveUpdateDestroyAPIView,
    TopicListCreateAPIView,
    TopicRetrieveUpdateDestroyAPIView,
    MessageListCreateAPIView,
    MessageRetrieveUpdateDestroyAPIView,
    CommentListCreateAPIView,
    CommentRetrieveUpdateDestroyAPIView,
    LikeCreateAPIView,
)
router = routers.DefaultRouter()
router.register("category", CategoryListCreateAPIView, "categories")
router.register("topic", TopicListCreateAPIView, "topics")
router.register("message", MessageListCreateAPIView, "messages")
router.register("comment", CommentListCreateAPIView, "comments")
router.register("like", LikeCreateAPIView, "likes")


urlpatterns = [
    path('', include(router.urls)),
]

'''
urlpatterns = [
    path('categories/', CategoryListCreateAPIView.as_view(), name='category-list'),
    path('categories/<int:pk>/',
         CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-detail'),
    path('topics/', TopicListCreateAPIView.as_view(), name='topic-list'),
    path('topics/<int:pk>/', TopicRetrieveUpdateDestroyAPIView.as_view(),
         name='topic-detail'),
    path('messages/', MessageListCreateAPIView.as_view(), name='message-list'),
    path('messages/<int:pk>/',
         MessageRetrieveUpdateDestroyAPIView.as_view(), name='message-detail'),
    path('comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/',
         CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
    path('likes/', LikeCreateAPIView.as_view(), name='like-create'),
]
'''
