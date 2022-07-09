import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import os  # noqa: E402
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_One.settings')

import django  # noqa: E402
django.setup()

from app_one.models import Topic, Webpage, AccessRecord  # noqa: E402
import random  # noqa: E402
from faker import Faker  # noqa: E402

fake_gen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Sports']


def add_topic():

    topic = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    topic.save()

    return topic


def populate(N=5):

    for entry in range(N):

        fake_name = fake_gen.company()
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()

        topic = add_topic()

        webpg = Webpage.objects.get_or_create(
            topic=topic, name=fake_name, url=fake_url)[0]

        AccessRecord.objects.get_or_create(
            webpage=webpg, date=fake_date)


if __name__ == '__main__':

    print("Populating Script")
    populate(10)
    print("Populating Complete")
