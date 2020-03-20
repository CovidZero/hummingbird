import json

from datetime import datetime

import requests

from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware

from api.report.models import *

url = "http://plataforma.saude.gov.br/novocoronavirus/resources/scripts/database.js"


def cron(*args, **options):
    if 6 <= datetime.now().hour <= 20:

        print(f"Cron job is running. The time is {datetime.now()}")
        request = requests.get(url)

        content = request.content.decode('utf8').replace('var database=', '')
        data = json.loads(content)

        for record in data['brazil']:
            date_time = datetime.strptime(f"{record['date']} {record['time']}",
                                          '%d/%m/%Y %H:%M')

            report, report_created = Report.objects.get_or_create(
                updated_at=make_aware(date_time)
            )

            if report_created:
                for value in record['values']:
                    state = int(value['uid'])

                    suspects = value.get('suspects', 0)
                    refuses = value.get('refuses', 0)
                    cases = value.get('cases', 0)
                    deaths = value.get('deaths', 0)
                    recovered = value.get('recovered', 0)

                    Case.objects.get_or_create(
                        suspects=suspects, refuses=refuses, cases=cases, deaths=deaths, recovered=recovered,
                        defaults={
                            'state': state,
                            'report': report
                        })

    print(f"Done! The time is: {datetime.now()}")


class Command(BaseCommand):
    help = 'Update kaggle dataset with the last cases of COVID-19 in Brazil.'

    def handle(self, *args, **options):
        print('Cron started! Wait the job starts!')

        scheduler = BlockingScheduler()
        scheduler.add_job(cron, 'cron', minute=20, timezone='America/Maceio')

        scheduler.start()
