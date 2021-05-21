from django.db import models


class DataSchema(models.Model):
    title = models.CharField(max_length=128)
    preferences = models.ForeignKey(
        to='DataSchemaPreferences',
        related_name='schema',
        on_delete=models.CASCADE,
    )
    updated_at = models.DateTimeField(auto_now=True)


class DataSchemaPreferences(models.Model):
    class ColumnSeparator(models.TextChoices):
        COMMA = ','
        SEMICOLON = ';'

    class StringCharacter(models.TextChoices):
        SINGLE_QUOTE = "'"
        DOUBLE_QUOTE = '"'

    column_separator = models.CharField(max_length=128, choices=ColumnSeparator.choices)
    string_character = models.CharField(max_length=128, choices=StringCharacter.choices)


class DataSchemaColumn(models.Model):
    class Types(models.TextChoices):
        FULL_NAME = 'name'
        EMAIL = 'email'
        PHONE_NUMBER = 'phone_number'
        DATE = 'date'
        COMPANY_NAME = 'company'

    title = models.CharField(max_length=128)
    type = models.CharField(max_length=128, choices=Types.choices)
    order = models.IntegerField()
    schema = models.ForeignKey(
        to=DataSchema,
        related_name='columns',
        on_delete=models.CASCADE,
    )


class DataSet(models.Model):
    class Statuses(models.TextChoices):
        READY = 'Ready'
        PROCESSING = 'Processing'
        NOT_READY = 'Not Ready'

    file = models.FileField(upload_to='schema/sets/', null=True)
    schema = models.ForeignKey(
        to=DataSchema,
        related_name='sets',
        on_delete=models.CASCADE,
    )
    rows = models.IntegerField()
    status = models.CharField(
        max_length=64,
        choices=Statuses.choices,
        default=Statuses.NOT_READY,
    )
    created_at = models.DateTimeField(auto_now_add=True)
