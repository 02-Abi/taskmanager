from celery import shared_task
from django.utils import timezone
from django.core.mail import send_mail
from .models import Task

@shared_task
def send_due_task_reminders():
    now = timezone.now()
    due_tasks = Task.objects.filter(remind_at__lte=now)

    for task in due_tasks:
        send_mail(
            subject=f"Reminder: {task.title}",
            message=f"Your task is due now.\n\n{task.description}",
            from_email=None,
            recipient_list=[task.user.email],
            fail_silently=True,
        )
        task.delete()
