

from django.db import models


# Create your models here.


# class Post(models.Model) :  # ORM 정의 하나의 게시글을 위한 클래스. model을 상속받아서 클래스를 적용할 준비가된 클래스가 된다.
#         title = models.CharField(max_length=32) #2의 거듭제곱 꼴로 선언하는것이 좋다.
#         content = models.TextField (default=0, max_length=2048, blank= True, null=True) 
#         head_image = models.ImageField(
#                 upload_to = "landing/images/%Y/%m/%d/%H/",
#                 blank= True
                
#         )
#         created_at =models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
        
        



class Blog(models.Model) :
        blog_name =models.CharField(max_length=64)
        blog_banner =models.ImageField(
                upload_to = "blog/images/banner",
                blank =True,
                null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now =True)

                
class TempUser(models.Model) :
        user_name = models.CharField(max_length=32)
        user_email = models.CharField(max_length=64)

class Post(models.Model) :
        writer = models.ForeignKey(TempUser, on_delete=models.CASCADE, null= True)
        title = models.CharField(max_length=64) #2의 거듭제곱 꼴로 선언하는것이 좋다.
        content = models.TextField (default=0, max_length=2048, blank= True, null=True) 
        head_image = models.ImageField(
                upload_to = "landing/images/%Y/%m/%d/%H/",
                blank= True
        )
        liked_users =  models.ManyToManyField(TempUser, related_name = "user_likses")
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now =True)


