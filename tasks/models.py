from django.db import models

# Create your models here.
from django.db import models

from users.models import User
from projects.models import Project
# -------------------------------------------------------------------------------------------------
class TaskPriority(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority = models.CharField(max_length=50)
    priority_ar = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format
    class Meta:
        verbose_name        = "Task Priority"
        verbose_name_plural = "Task Priority"

    def __str__(self):
        return self.priority
# -------------------------------------------------------------------------------------------------
class TaskStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=50)
    status_ar = models.CharField(max_length=50, blank=True, null=True)
    color = models.CharField(max_length=7)  # Assuming color code in hexadecimal format
    class Meta:
        verbose_name        = "Task Status"
        verbose_name_plural = "Task Status"

    def __str__(self):
        return self.status
# -------------------------------------------------------------------------------------------------
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, blank=True, null=True)
    
    title = models.CharField(max_length=255, blank=True, null=True)
    title_ar = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    dependency = models.ManyToManyField('self', symmetrical=False, related_name='dependent_tasks', blank=True)
    color = models.CharField(max_length=7) # Assuming color code in hexadecimal format
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, blank=True, null=True)
    priority = models.ForeignKey(TaskPriority, on_delete=models.PROTECT, blank=True, null=True)
    
    due_date = models.DateTimeField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    actual_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    
    tags = models.ManyToManyField('Tag', blank=True)

    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # for tasks you want to neglect in official records - or self-assigned
    is_hidden = models.BooleanField(null=False, default = False)

    class Meta:
        verbose_name        = "Task"
        verbose_name_plural = "Task"

    def __str__(self):
        return self.title
# -------------------------------------------------------------------------------------------------
class TaskAssignment(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    class Meta:
        unique_together = (("task", "user"),)
# -------------------------------------------------------------------------------------------------
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
# -------------------------------------------------------------------------------------------------
class AttachementOfComment(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments_commnets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
# -------------------------------------------------------------------------------------------------
class AttachmentOfTask(models.Model):
    id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='attachments_tasks/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
# -------------------------------------------------------------------------------------------------
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
# -------------------------------------------------------------------------------------------------