import json
import jsonschema
from jsonschema import validate
from locust import FastHttpUser, task, events


def get_schema():
    with open('./schemas/webcams_schema.json', 'r') as file:
        schema = json.load(file)
    return schema


schema = get_schema()


class DriveBcUser(FastHttpUser):
    @task
    def backend(self):
        with self.client.get("/api/test/webcams", catch_response=True) as response:
            json = response.json()

            try:
                validate(instance=json, schema=schema)
            except jsonschema.exceptions.ValidationError as err:
                err = "JSON response does not match"
                response.failure(err)
                return False, err
