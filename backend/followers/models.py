from django.db import models
from core.models import Account

class UserFollowing(models.Model):

    # profil obserwowany
    profile_id = models.ForeignKey(Account, related_name="profile_id", on_delete=models.CASCADE)

    # profil który kliknął "obserwuj"
    following_profile_id = models.ForeignKey(Account, related_name="following_profile_id", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.following_profile_id.username + "->" + self.profile_id.username

    class Meta:
        ordering = ['created']
