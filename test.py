from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    host = 'http://ignite2.tp9249.df-tp.com'
    wait_time = constant(1)

    @task
    def get_users(self):
        response = self.client.get("/")
