from blog.models import Post


def get_posts():
    return Post.objects.select_related("post_author").prefetch_related("tag").order_by("-id")

def get_post(post_id):
    pass

def get_posts_by_tag(post_id):
    pass

def get_comments_by_post(post_id):
    pass

def get_tag(tag_id):
    pass