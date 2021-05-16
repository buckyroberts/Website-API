import uuid

from django.db import models
from thenewboston.models.created_modified import CreatedModified


class Playlist(CreatedModified):
    PLAYLIST_TYPE = [
        ('youtube', 'youtube'),
        ('vimeo', 'vimeo')
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    published_at = models.DateTimeField()
    instructor = models.ForeignKey('videos.Instructor', on_delete=models.CASCADE, null=True)
    thumbnail = models.CharField(max_length=250)
    categories = models.ManyToManyField('videos.PlaylistCategory')
    playlist_type = models.CharField(max_length=15, choices=PLAYLIST_TYPE)

    class Meta:
        ordering = ('published_at',)

    def __str__(self):
        return f'#{self.pk}: {self.title}'
