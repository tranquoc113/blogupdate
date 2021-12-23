from django.contrib.auth.models import AbstractUser
from django.db.models import CharField


class Users(AbstractUser):
    """Default user for myupdate.vn."""

    #: First and last name do not cover name patterns around the globe
    name = CharField(blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

