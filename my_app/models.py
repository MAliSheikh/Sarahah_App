from django.db import models
from django.contrib.auth.models import User


class Comment_Reply(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:13] + "..." + " by " + self.user.username

    
class Reply(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    cs_no = models.AutoField(primary_key=True)
    comment_no = models.IntegerField() # Comment_Reply k table se sno le rha frontend me print krwa kr
    reply_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Link(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uuid = models.TextField() 

    def __str__(self):
        return self.uuid[0:13] + "..." + " by " + self.user.username