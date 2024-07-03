from django.db import models


class ObjectsManager(models.Manager):
    def get_queryset(self):
        return super(ObjectsManager, self).get_queryset()


class ActiveObjectsManager(models.Manager):
    """ Active objects manager """

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)