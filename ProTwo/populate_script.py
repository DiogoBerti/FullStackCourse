import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# Fake Script

import random
from AppTwo.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()

topics = ['search','social','marketplace','news','games']

def add_topic():
    # Retorna uma Tupla
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Usa o random da funçao anterior para adicionar um topic
        topic = add_topic()

        # Usa o Faker para criar os dados dos campos
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=topic,
                                                url=fake_url,
                                                name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,
                                                        date=fake_date)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(10)
    print('Done!')
