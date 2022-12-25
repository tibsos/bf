import os

from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4


def upload_image(instance, filename):
        
    e = filename.split('.')[-1]
    s = f"{u4}.{e}"

    return os.path.join('uploads/app/note/images', s)

class Image(m.Model):

    uid = m.UUIDField(default = u4)
    user = m.ForeignKey(User, on_delete = m.CASCADE)

    note = m.ForeignKey('Note', on_delete = m.CASCADE)

    file = m.ImageField(upload_to = upload_image)

    uploaded_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return f"{self.user.username} Image"
    
    class Meta:

        ordering = ['-uploaded_at']

class Folder(m.Model):

    uid = m.UUIDField(default = u4)
    user = m.ForeignKey(User, on_delete = m.CASCADE)

    title = m.TextField()

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['-updated_at']

class Note(m.Model):

    uid = m.UUIDField(default = u4)
    user = m.ForeignKey(User, on_delete = m.CASCADE)

    title = m.TextField(blank = True)
    content = m.TextField(blank = True)
    
    images = m.ManyToManyField(Image, blank = True, related_name = 'ni')
    folders = m.ManyToManyField(Folder, blank = True)

    archived = m.BooleanField(default = False)
    p = m.BooleanField(default = False)
    loved = m.BooleanField(default = False)
    
    deleted = m.BooleanField(default = False)
    deleted_at = m.DateTimeField(blank = True, null = True)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        if self.title:

            return f"{self.user.username} | {self.title}"
        
        else:

            return f"{self.user.username} Note"

    class Meta:

        ordering = ['-updated_at']