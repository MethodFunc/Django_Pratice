from django.shortcuts import render
from .models import  Post

# Create your views here.


def post_list(request):
    qs = Post.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(message__icontains=q)

    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'q': q
    })


# def item_list(request):
#     qs = Item.objects.all()
#
#     q = request.GET.get('q', '')
#
#     if q:
#         qs = qs.filter(name__icontains=q)
#
#         return render(request, 'shop/item_list.html', {
#             'item_list': qs,
#             'q': q
#         })
