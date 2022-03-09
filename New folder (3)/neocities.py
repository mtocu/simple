import requests, io

class Neocities:
    def __init__(self, apiKey: str):
        self.requests = requests.Session()
        self.requests.headers["Authorization"] = f"Bearer {apiKey}"
    
    def upload(self, filename: str, content: str):
        return self.requests.post("https://neocities.org/api/upload",files={filename: content})