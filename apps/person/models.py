from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError


def validator_file_size_limit(value):
        """Validación de limite de tamaño del archivo

        Parameters
        ----------
        value : value
            Archivo

        Raises
        ------
        ValidationError
            _description_
        """
        limit = 2 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File too large. Size should not exceed 2 MiB.')

class Person(models.Model):
    """
    Represents a person in the system.

    This model stores basic information about individuals including their name,
    email, age, and timestamps for record creation and updates.
    """

    # Personal Information Fields
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.PositiveIntegerField()
    document = models.FileField(
        default="",
        upload_to="files/",
        validators=[
            FileExtensionValidator(
                ['pdf', 'docx', 'odt']
            ),
            validator_file_size_limit
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        String representation of the Person model.

        Returns:
            str: The person's name for easy identification in admin and queries.
        """
        return self.name