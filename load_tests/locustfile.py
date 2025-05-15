from locust import HttpUser, task

class EcommerceUser(HttpUser):
    @task
    def load_home(self):
        self.client.get('/')