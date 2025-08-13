import pytest


@pytest.mark.positive
class TestProjectsPositive:
    def test_create_project(self, api_client, cleanup_project):
        project_data = {
            "name": "Test Project",
            "description": "This is a test project"
        }
        response = api_client.create_project(project_data)
        assert response.status_code == 201
        assert "id" in response.json()
        cleanup_project.append(response.json()["id"])

    def test_get_project(self, api_client, cleanup_project):
        # Сначала создаем проект
        project_data = {"name": "Project to Get"}
        create_response = api_client.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Затем получаем его
        response = api_client.get_project(project_id)
        assert response.status_code == 200
        assert response.json()["id"] == project_id
        assert response.json()["name"] == "Project to Get"

    def test_update_project(self, api_client, cleanup_project):
        # Сначала создаем проект
        project_data = {"name": "Project to Update"}
        create_response = api_client.create_project(project_data)
        project_id = create_response.json()["id"]
        cleanup_project.append(project_id)

        # Обновляем проект
        update_data = {"name": "Updated Project Name"}
        response = api_client.update_project(project_id, update_data)
        assert response.status_code == 200

        # Проверяем обновление
        get_response = api_client.get_project(project_id)
        assert get_response.json()["name"] == "Updated Project Name"
