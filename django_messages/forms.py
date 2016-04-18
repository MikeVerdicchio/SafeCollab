from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from auth.models import UserProfile
from Crypto.PublicKey import RSA
from base64 import b64decode


if "notification" in settings.INSTALLED_APPS and getattr(settings, 'DJANGO_MESSAGES_NOTIFY', True):
    from notification import models as notification
else:
    notification = None

from django_messages.models import Message
from django_messages.fields import CommaSeparatedUserField
from django.core.exceptions import ValidationError

class ComposeForm(forms.Form):
    """
    A simple default form for private messages.
    """
    recipient = CommaSeparatedUserField(label=_(u"Recipient"))
    subject = forms.CharField(label=_(u"Subject"), max_length=120)
    body = forms.CharField(label=_(u"Body"),
        widget=forms.Textarea(attrs={'rows': '12', 'cols':'55'}))
    encrypt = forms.BooleanField(label=_(u"Encrypt"))
        
    def __init__(self, *args, **kwargs):
        recipient_filter = kwargs.pop('recipient_filter', None)
        super(ComposeForm, self).__init__(*args, **kwargs)
        if recipient_filter is not None:
            self.fields['recipient']._recipient_filter = recipient_filter
    
                
    def save(self, sender, parent_msg=None):
        if sender is None:
            raise ValidationError(self.error_messages['empty_sender'], code='empty_sender')
        recipients = self.cleaned_data['recipient']
        subject = self.cleaned_data['subject']
        body = self.cleaned_data['body']
        encrypt = self.cleaned_data['encrypt']
        message_list = []
        for r in recipients:
            if encrypt == True:
                # key = UserProfile.objects.get(username__exact=r).public_key
                # key = key.replace('-----BEGIN PUBLIC KEY----- ', '')
                # key = key.replace(' -----END PUBLIC KEY-----', '')

                key = b'MIGJAoGBAJNrHWRFgWLqgzSmLBq2G89exgi/Jk1NWhbFB9gHc9MLORmP3BOCJS9konzT/+Dk1hdZf00JGgZeuJGoXK9PX3CIKQKRQRHpi5e1vmOCrmHN5VMOxGO4d+znJDEbNHODZR4HzsSdpQ9SGMSx7raJJedEIbr0IP6DgnWgiA7R1mUdAgMBAAE='

                keyDER = b64decode(key)
                key = RSA.importKey(keyDER)
                body = key.encrypt(body.encode('utf-8'), 32)
            msg = Message(
                sender = sender,
                recipient = r,
                subject = subject,
                body = body,
            )
            if parent_msg is not None:
                msg.parent_msg = parent_msg
                parent_msg.replied_at = timezone.now()
                parent_msg.save()
            msg.save()
            message_list.append(msg)
            if notification:
                if parent_msg is not None:
                    notification.send([sender], "messages_replied", {'message': msg,})
                    notification.send([r], "messages_reply_received", {'message': msg,})
                else:
                    notification.send([sender], "messages_sent", {'message': msg,})
                    notification.send([r], "messages_received", {'message': msg,})
        return message_list
