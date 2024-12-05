from django.db import models

# Create your models here.

# {
#     id: number,
#     username: string,
#     title: string,
#     content: string
#     created_datatime: datetime,
    
# }

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)