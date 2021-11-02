from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Post, Vote
from api.serializers import PostSerializer, PostCommentSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        else:
            return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        slr = PostCommentSerializer(post, context={'request': request})
        return Response(slr.data)


class AddVote(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        try:
            vote = Vote.objects.get(article_id=post, user_id=self.request.user)
            vote.delete()
            post.vote_count -= 1
            post.save()
            return Response({'error': 'Unvote'}, status=200)
        except:
            Vote.objects.create(article=post, user_id=self.request.user)
            post.vote_count += 1
            post.save()
            return Response({'message': 'Vote'}, status=200)
