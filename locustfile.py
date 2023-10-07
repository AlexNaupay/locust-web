from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)

    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })

    @task
    def index(self):
        self.client.get("/")
        # self.client.get("/static/assets.js")

# pip list --format=freeze | grep -E '^\S' > requirements.txt

# run: locust -f locustfile.py
