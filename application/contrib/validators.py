from secrets import token_urlsafe
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class TextValidator(validators.RegexValidator):
    """
    Validator for usernames.

    Ensures that the username contains only
    letters, numbers, and the following special characters:
    - . (dot)
    - _ (underscore)
    - - (hyphen)
    """

    regex = r"^[\w.-]+$"
    message = _(
        "Enter a valid username. "
        "This value may contain only "
        "letters, numbers, and the following special characters: "
        "- . (dot), _ (underscore), and - (hyphen)."
    )
    flags = 0


@deconstructible
class FileUpload:
    def __call__(self, instance, filename):
        """
        Generates the new filename using a random string and file extension.
        """

        ext = filename.split(".")[-1]  # File extension
        mark = token_urlsafe(16).lower()  # Generates a random string
        return f"file.{mark}.{ext}"  # Returns the new file name

