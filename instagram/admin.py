from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


# Register your models here.
# 1st.
# admin.site.register(Post)

# 2nd
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'message_length', 'create_at', 'update_at', 'is_public']
    list_display_links = ["message"]
    search_fields = ["message", 'is_public']
    list_filter = ["create_at", 'is_public']

    def message_length(self, post):
        return len(post.message)

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style="width: 72px;height: 72px"/>')

        return None


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
