from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.
# post_list = ListView.as_view(model=Post)

# class PostView(ListView):
#     model = Post

# post_list = PostView.as_view()

# def post_list(request):
#     qs = Post.objects.all()
#
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'q': q
#     })

post_list = ListView.as_view(model=Post, paginate_by=10)


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     response = HttpResponse()
#     response.write("Hellow World " * pk)
#     return response


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)
#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     return render(request, 'instagram/post_detail.html', {'post': post})


# post_detail = DetailView.as_view(model=Post,
#                                  queryset=Post.objects.filter(is_public=True))

class PostDetailView(DetailView):
    model = Post

    def get_queryset(self):
        '''
        self.request.user.is_authenticated
        로그인이 안 되어 있으면 공개된 것만 보고 되어 있으면 모두 봐라
        '''
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        return qs


post_detail = PostDetailView.as_view()


def archives_years(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f"{year}, Archives")
