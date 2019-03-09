import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'newProj.settings')

import django
django.setup()

from faker import Faker
from appone.models import User 

fakegen = Faker()

def populate(N=5):

	for newuser in range(N):

		fake_name = fakegen.name().split()
		fake_first_name = fake_name[0]
		fake_last_name = fake_name[1]
		fake_email = fakegen.email()

		newUser = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
	print("Populating Users")
	populate(20)
	print("Done populating!")
