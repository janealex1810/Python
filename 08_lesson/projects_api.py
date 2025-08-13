import requests


class ProjectsAPI:
    def init(self, base_url, auth_token):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Content-Type": "application/json"
        }

    def create_project(self, project_data):
        url = f"{self.base_url}/api-v2/projects"
        response = requests.post(url, json=project_data, headers=self.headers)
        return response

    def get_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, update_data):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.put(url, json=update_data, headers=self.headers)
        return response

    def delete_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.delete(url, headers=self.headers)
        return response
