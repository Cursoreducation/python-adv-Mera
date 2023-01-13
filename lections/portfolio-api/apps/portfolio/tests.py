import tempfile
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.reverse import reverse

MEDIA_ROOT = tempfile.mkdtemp()

User = get_user_model()


class UserMixin(object):
    @staticmethod
    def _create_user(number: int):
        user = User.objects.create(
            username=f"test_{number}",
            email=f"test_{number}@example.com",
        )
        user.set_password("testPassword")
        user.save()
        return user


class ImageTestCase(TestCase, UserMixin):
    def setUp(self) -> None:
        self.user = self._create_user(1)

        self.login_url = reverse("accounts:login")
        self.image_list_url = reverse("portfolio:image-list")
        self.image_detail_url = reverse("portfolio:image-detail", kwargs={"pk": 1})
