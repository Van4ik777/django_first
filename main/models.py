from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Max
from profanityfilter import ProfanityFilter

profanity_filter = ProfanityFilter()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    stars = models.IntegerField(
        default=0,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)
    liked = models.BooleanField(default=False)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def save(self, *args, **kwargs):
        self.content = profanity_filter.censor(self.content)
        super().save(*args, **kwargs)



class CartItem(models.Model):
    '''
    Model for cart items
    '''
    pizza_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)


