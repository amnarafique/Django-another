from django.db import models

class NotCompletedTaskManger(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(done=False)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    dead_line = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    done = models.BooleanField(default=False)
    objects = models.Manager()
    not_completed = NotCompletedTaskManger()

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title


def test():
    pass



