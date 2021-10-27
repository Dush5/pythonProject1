from locust import HttpUser, task, constant, TaskSet


class WebsiteTest(TaskSet):

    @task
    def engine6_webpage(self):
        count = 0
        with open("file.txt") as fp:
            for line in fp:
                self.client.get(line.strip())


class MyLoadTest(HttpUser):
    host = "http://bmwvwtopeka-com.website.tp9249.df-tp.com"
    wait_time = constant(1)

    def on_start(self):
        print("Load test has started")
        pass

    def on_stop(self):
        print("Load testing has been finished")
        pass

    tasks = [WebsiteTest]
