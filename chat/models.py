import uuid

from django.db import models

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class ExampleModel(DjangoCassandraModel):
    example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    user = models.BigIntegerField()
    recipient = models.BigIntegerField()
    body = columns.Text()
