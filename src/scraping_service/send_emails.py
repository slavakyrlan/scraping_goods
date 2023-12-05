import os, sys
import django
from django.core.mail import EmailMultiAlternatives
import datetime
from django.contrib.auth import get_user_model

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"

django.setup()

from scraping.models import Information, Error
from scraping_service.settings import (
    EMAIL_HOST_USER,
    EMAIL_HOST, EMAIL_HOST_PASSWORD
)

ADMIN_USER = EMAIL_HOST_USER

today = datetime.date.today()
subject = f"Рассылка доступных оборудований за {today}"
text_content = f"Рассылка доступных оборудований {today}"
from_email = EMAIL_HOST_USER
empty = '<h2>К сожалению на сегодня по Вашим предпочтениям данных нет. </h2>'

User = get_user_model()
qs = User.objects.filter(send_email=True).values('warehouse', 'device', 'email')
users_dct = {}
for i in qs:
    users_dct.setdefault((i['warehouse'], i['device']), [])
    users_dct[(i['warehouse'], i['device'])].append(i['email'])

if users_dct:
    params = {'warehouse_id__in': [], 'device_id__in': []}
    for pair in users_dct.keys():
        params['warehouse_id__in'].append(pair[0])
        params['device_id__in'].append(pair[1])
    qs = Information.objects.filter(**params, timestamp=today).values()[:10]
    informations = {}
    for i in qs:
        informations.setdefault((i['warehouse_id'], i['device_id']), [])
        informations[(i['warehouse_id'], i['device_id'])].append(i)
    for keys, emails in users_dct.items():
        rows = informations.get(keys, [])
        html = ''
        for row in rows:
            html += f'<h3"><a href="{row["url"]}">{row["title"]}</a></h3>'
            html += f'<p>{row["description"]} </p>'
            html += f'<p>{row["company"]} </p><br><hr>'
        _html = html if html else empty
        for email in emails:
            to = email
            msg = EmailMultiAlternatives(
                subject, text_content, from_email, [to]
            )
            msg.attach_alternative(_html, "text/html")
            msg.send()

#if subject:
       # msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
       # msg.attach_alternative(_html, "text/html")
       # msg.send()