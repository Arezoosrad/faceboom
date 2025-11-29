from django.contrib import admin

# Register your models here.
from .models import MyUser,Message,FriendRequest,Post,Comments,Like

admin.site.register(MyUser)
admin.site.register(Like)
admin.site.register(Comments)
admin.site.register(FriendRequest)
admin.site.register(Post)
admin.site.register(Message)

