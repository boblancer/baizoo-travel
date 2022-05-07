from locust import HttpUser, task, between
import random

def gen_coor():
    r1 = random.randrange(1, 60, 2)	
    r2 = random.randrange(1, 60, 2)	

    return (13.1 + r1/1000, 100.2 + r2/1000)
class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)
    
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def test_search(self):
        x,y = gen_coor()
        self.client.get("/travel/spots?lat={}&long={}".format(x,y))
