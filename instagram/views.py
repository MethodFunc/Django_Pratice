from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
# from django.core.checks import messages
from django.contrib import messages
from .models import Post
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView, CreateView, UpdateView, \
    DeleteView
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.urls import reverse, reverse_lazy

from pprint import pprint


# 외래키를 할당하려면 @login_required 데코레이터로 꾸밀 것
# @login_required
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # commit의 기본 값은 True, False 시 데이터베이스에 데이터가 생성이 안됨.
#             # 사용하는 이유가 인스턴스를 지연 하고자 사용함
#             post = form.save(commit=False)
#             post.author = request.user
#             # commit False 시 다음 코드를 호출해야함
#             post.save()
#             messages.success(request, '포스트를 저장했습니다.')
#             return redirect(post)
#     else:
#         form = PostForm()
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': None
#
#     })


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        messages.success(self.request, '포스트를 저장했습니다.')

        return super().form_valid(form)


post_new = PostCreateView.as_view()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        return super().form_valid(form)


post_edit = PostUpdateView.as_view()


# 수정할 때는 이미 작성자 명이 들어가 있기 때문에 commit=False할 피룡 없음.
# @login_required
# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if post.author != request.user:
#         messages.error(request, "작성자만 수정 가능합니다.")
#         return redirect(post)
#
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             post = form.save()
#             messages.success(request, '포스트를 수정했습니다.')
#
#             return redirect(post)
#     else:
#         form = PostForm(instance=post)
#
#     return render(request, 'instagram/post_form.html', {
#         'form': form,
#         'post': post
#
#     })


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    # 실제로 이렇게 해도 됨
    # success_url = "/instagram"
    #
    # def get_success_url(self):
    #     return reverse("instagram:post_list")

    # 같이 사용될 때 사용 할 수 있음
    success_url = reverse_lazy("instagram:post_list")


post_delete = PostDeleteView.as_view()


# @login_required
# def post_delete(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "Post is Deleted")
#         return redirect('instagram:post_list')
#
#     return render(request, 'instagram/post_confirm_delete.html', {
#         "post": post,
#     })


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

# post_list = ListView.as_view(model=Post, paginate_by=10)


# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# @method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '')

        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)
        if q:
            qs = qs.filter(message__icontains=q)

        return qs


post_list = PostListView.as_view()


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


post_archive = ArchiveIndexView.as_view(model=Post, date_field="create_at")

post_archive_year = YearArchiveView.as_view(model=Post, date_field="create_at", make_object_list="message")
