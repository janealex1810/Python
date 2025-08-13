import pytest
from projects_api import ProjectsAPI


@pytest.fixture
def api_client():

    base_url = "https://yougile.com"
    auth_token = "your_auth_token_here"
    return ProjectsAPI(base_url, auth_token)


@pytest.fixture
def cleanup_project(api_client):
    project_ids = []
    yield project_ids
    # Удаляем созданные проекты после тестов
    for project_id in project_ids:
        api_client.delete_project(project_id)
