from django.db import models
from django.utils.timezone import now


class BaseWebDavModel(models.Model):
    """
    Abstract Base WebDav Model that other models will inherit from

    Contains the basic items:
    - name
    - create timestamp
    - last modified timestamp
    """
    name = models.CharField(max_length=255)
    created = models.DateTimeField(default=now)
    modified = models.DateTimeField(default=now)

    class Meta:
        abstract = True


class CollectionModel(BaseWebDavModel):
    """
    Collection Model - represents a directory in WebDav
    """
    parent = models.ForeignKey('self', blank=True, null=True)
    size = 0

    class Meta:
        unique_together = (('parent', 'name'),)

    def __str__(self):
        return "Collection {}".format(self.name)


class ObjectModel(BaseWebDavModel):
    """
    Object Model - represents a file in a directory in WebDav
    """

    parent = models.ForeignKey(CollectionModel, blank=True, null=True)

    # the actual file
    path = models.FileField(max_length=255)

    # size of the file
    size = models.IntegerField(default=0)

    # md5 hash of the file (ToDo: check if we can do sha256 or so)
    md5 = models.CharField(max_length=255)

    class Meta:
        unique_together = (('parent', 'name'),)

    def __str__(self):
        return "Object {}".format(self.name)
