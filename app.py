from dependency_injector import containers, providers

from services.microsoft_todo_service import MicrosoftTodoService

print("test")


class Container(containers.DeclarativeContainer):
    microsoft_todo_service = providers.Singleton(MicrosoftTodoService)
