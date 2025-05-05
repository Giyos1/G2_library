from django.contrib.auth.models import Group

from accounts.models import User

# 1- adminkada admin group yaratim
admin, _ = Group.objects.get_or_create(name='admin')

# 2- permessions biriktirdim
# permis

# 2- user bilan groupni biriktirish
user = User.objects.get(id=1)
user.groups.add(admin)
