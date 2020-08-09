from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from iflame.models import StudentInformation


@receiver(post_save, sender=StudentInformation)
def post_save_signal_call(sender, instance, created, **kwargs):
    print('postsave')
    return


def pre_save_signal_call(sender, instance, **kwargs):
    print('Presave')
    return


pre_save.connect(pre_save_signal_call, sender=StudentInformation)

# post_save.connect(post_save_signal_call, sender=StudentInformation)
