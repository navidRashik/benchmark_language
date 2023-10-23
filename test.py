from locust import HttpUser, task, between


# python -m locust -f test.py
class WebsiteUser(HttpUser):
    # wait_time = between(1, 2.5)

    @task(1)
    def fastapi(self):
        self.client.get("http://localhost:8001/fastapi")

    @task(0)
    def flask(self):
        self.client.get("http://localhost:5001/flask")

    @task(1)
    def chi(self):
        self.client.get("http://localhost:3001/chi")

    @task(0)
    def actix(self):
        self.client.get("http://localhost:8002/actix")
