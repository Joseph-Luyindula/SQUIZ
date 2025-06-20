from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	total_game = models.IntegerField(default=0)
	slug = models.SlugField()
	image = models.ImageField(null=True,blank=True,upload_to="image_category")
	def __str__(self):
		return str(self.name)
	
	class Meta:
		verbose_name = "catégorie"
		verbose_name_plural = "catégories"

		
class Questionnaire(models.Model):
	Question = models.TextField()
	good_answer = models.CharField(max_length=200)
	response_list = models.JSONField(default=dict)
	categories= models.ManyToManyField(Category,default="")
	image = models.ImageField(blank=True, null=True)
	create_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return str(self.Question)
	
	class Meta:
		verbose_name = "Questionnaire"
		verbose_name_plural = "Questionnaires"
	

class Level(models.Model):
	name = models.CharField(max_length=10)
	pseudo = models.CharField(max_length=50)
	color = models.CharField(max_length=10)
	max = models.IntegerField()
	description = models.TextField(blank=True,null=True)
	
	def __str__(self):
		return f"{self.name}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    level = models.ForeignKey(Level, models.RESTRICT, blank=True,null=True)
    xp = models.IntegerField(default=0)
    total_games = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    win_rate = models.IntegerField(default=0)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,null=True)
    friends = models.ManyToManyField('self', blank=True, symmetrical=True)
    data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user}"


class FriendRequest(models.Model):
    from_user = models.ForeignKey(Profile, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Profile, related_name='received_requests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"


class Badge(models.Model):
	name = models.CharField(max_length=350)
	description = models.TextField()
	target = models.CharField(max_length=350)
	position = models.IntegerField()
	value = models.IntegerField()
	image = models.ImageField(upload_to='badges/', blank=True, null=True)
	
	def __str__(self):
		return str(self.name)


class UserBadge(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.badge.name}"
        
        
        
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)

#@receiver(post_save, sender=User)
#def save_user_profile(sender, instance, **kwargs):
#    instance.profile.save()
