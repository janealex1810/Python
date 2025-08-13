import pytest


@pytest.mark.negative
class TestProjectsNegative:
    def test_create_project_without_name(self, api_client):
        project_data = {"description": "Project without name"}
        response = api_client.create_project(project_data)
        assert response.status_code == 400

    def test_get_nonexistent_project(self, api_client):
        nonexistent_id = "00000000-0000-0000-0000-000000000000"
        response = api_client.get_project(nonexistent_id)
        assert response.status_code == 404

    def test_update_project_with_invalid_data(self, api_client, cleanup_project):

        project_data = {"name": "Project for Invalid Update"}
        create_response = api_client.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Пытаемся обновить с невалидными данными
        update_data = {"name": ""}  # Пустое имя недопустимо
        response = api_client.update_project(project_id, update_data)
        assert response.status_code == 400
