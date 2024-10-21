from django.db import models
from .manager import ActiveObjectsManager, ObjectsManager
from .createupdateuser import get_current_user


class CreatedUpdatedAt(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class BaseModel(CreatedUpdatedAt, models.Model):
    """
    An abstract base class model to add basic db fields
    """

    objects = ObjectsManager()
    active_objects = ActiveObjectsManager()
    is_deleted = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        "app_auth.UserModel",
        related_name="%(class)s_created_by",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        "app_auth.UserModel",
        related_name="%(class)s_updated_by",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user:
            if not self.pk:  # New instance
                self.created_by = user
            self.updated_by = user
        super().save(*args, **kwargs)