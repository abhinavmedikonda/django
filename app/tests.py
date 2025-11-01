# Create your tests here.
import os
import shutil
import tempfile
from django.test import TestCase, RequestFactory, override_settings
from app import views


class ViewsAndAuthTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_renders_index_template(self):
        # create a temporary templates dir with index.html so render() succeeds
        tmpdir = tempfile.mkdtemp()
        try:
            with open(os.path.join(tmpdir, "index.html"), "w") as f:
                f.write("<html><body>index</body></html>")

            tmpl_settings = [
                {
                    "BACKEND": "django.template.backends.django.DjangoTemplates",
                    "DIRS": [tmpdir],
                    "APP_DIRS": True,
                    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
                }
            ]

            with override_settings(TEMPLATES=tmpl_settings):
                request = self.factory.get("/")
                response = views.index(request)
                self.assertEqual(response.status_code, 200)
                self.assertIn("index", response.content.decode())
        finally:
            shutil.rmtree(tmpdir)

    def test_authenticate_success_with_correct_credentials(self):
        self.assertTrue(views.authenticate("admin", views.PASSWORD))

    def test_authenticate_fails_with_wrong_username(self):
        self.assertFalse(views.authenticate("notadmin", views.PASSWORD))

    def test_authenticate_fails_with_wrong_password(self):
        self.assertFalse(views.authenticate("admin", "wrongpassword"))

    def test_authenticate_handles_nonstring_values(self):
        # ensure non-string / None inputs don't crash and return False
        self.assertFalse(views.authenticate(None, None))
        self.assertFalse(views.authenticate("admin", None))
        self.assertFalse(views.authenticate(None, views.PASSWORD))