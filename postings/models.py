from django.db import models
from users.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Postings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='postings/static/', 
        blank=True, 
        default='postings/statics/default.png', 
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],
        )
    

    def __str__(self):
        return self.title
    
class Likes(models.Model):
    post_id = models.ForeignKey(Postings, related_name="", on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name="", on_delete=models.CASCADE)
    
