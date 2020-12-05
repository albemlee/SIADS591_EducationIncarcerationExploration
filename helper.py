import requests
import json
import pandas as pd

class EducationData_API:
    def __init__(self, topic, source, endpoint, year):
        self.topic = topic
        self.source = source
        self.endpoint = endpoint
        self.year = year
        self.base_url = 'https://educationdata.urban.org/api/v1/{}/{}/{}/{}/'.format(
            self.topic,
            self.source,
            self.endpoint,
            self.year
        )

    def get_request(self):
        results = []
        api_response = requests.get(url = self.base_url)
        results.extend(api_response.json()['results'])
        next_page = api_response.json()['next']
        while next_page:
            api_response = requests.get(url = next_page)
            results.extend(api_response.json()['results'])
            next_page = api_response.json()['next']

        self.results_df = pd.DataFrame(results)
