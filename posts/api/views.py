from rest_framework import viewsets, routers
from posts.api.serializers import PostSerializer
from posts.models import Post

router = routers.DefaultRouter()

class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

router.register(r'posts', PostViewSet, base_name='post')
