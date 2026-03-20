import requests

class Endpoint:
    status = None

    def check_response_status_code_ok(self):
        assert self.status in [200, 201]