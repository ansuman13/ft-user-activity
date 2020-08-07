import random

import pytz
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker
# for showing loader
from tqdm import tqdm

from core.models import ActivityPeriod

fake = Faker()


class Command(BaseCommand):
    """Django command to create sample data"""

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int)

    def handle(self, *args, **options):
        """Handle the command"""
        total_users = options['number_of_users']

        TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

        # for generate sample user, tqdm for showing loader
        for _ in tqdm(range(total_users), desc='Creating user and their '
                                               'Activity'):
            user = get_user_model().objects.create_user(
                real_name=fake.name(),
                tz=random.choice(TIMEZONES)[0],
                email=fake.email(),
                password=fake.password())

            no_of_activities = random.randint(2, 5)

            # TODO: update this to make sense 🤣. later.
            # since activity is one day event, change this from this year
            # to this day maybe.
            end_datetime = fake.date_time_this_year()
            start_datetime = end_datetime - fake.time_delta(end_datetime)

            for count in range(no_of_activities):
                ActivityPeriod.objects.create(
                    user=user,
                    start_time=end_datetime,
                    end_time=start_datetime
                )
