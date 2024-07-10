import pytest
from src.models.repository.events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="Novo registro no banco de dados")
def test_insert_event():
    events_info = {
        "uuid": "123456",
        "title": "Test Event 2",
        "details": "Teste Event Details 2",
        "slug": "teste_slug_2",
        "maximum_attendees": 20
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(events_info)
    print(response)


def test_get_event_by_id():
    event_id = "123456"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
