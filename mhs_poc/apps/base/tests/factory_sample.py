# flake8: noqa

"""
Sample from: 
https://github.com/pydanny/cookiecutter-django/blob/master/%7B%7Bcookiecutter.project_slug%7D%7D/%7B%7Bcookiecutter.project_slug%7D%7D/users/tests/factories.py
More reference: https://djangostars.com/blog/django-pytest-testing

Faker docs: https://faker.readthedocs.io/en/master/
"""

# from django.contrib.auth import get_user_model
# from factory import Faker, post_generation
# from factory.django import DjangoModelFactory


# class UserFactory(DjangoModelFactory):

#     username = Faker("user_name")
#     email = Faker("email")
#     name = Faker("name")

#     @post_generation
#     def password(self, create: bool, extracted: Sequence[Any], **kwargs):
#         password = (
#             extracted
#             if extracted
#             else Faker(
#                 "password",
#                 length=42,
#                 special_chars=True,
#                 digits=True,
#                 upper_case=True,
#                 lower_case=True,
#             ).generate(params={"locale": None})
#         )
#         self.set_password(password)

#     class Meta:
#         model = get_user_model()
#         django_get_or_create = ["username"]
