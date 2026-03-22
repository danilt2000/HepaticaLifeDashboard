from app import Container
from services.microsoft_todo_service import MicrosoftTodoService
container = Container()


def test_get_recent_activities():
    service = container.microsoft_todo_service()

    assert isinstance(service, MicrosoftTodoService)
    service.get_recent_activities()
