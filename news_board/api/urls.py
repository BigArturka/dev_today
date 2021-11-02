from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views.comment_views import CommentViewSet
from api.views.post_views import PostViewSet, AddVote


app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('post/<int:pk>/vote/', AddVote.as_view(), name='add_vote'),
]
