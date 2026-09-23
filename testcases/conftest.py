import pytest
import time
from common.client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    client=ApiClient()
    TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkwNDY5OTY5LCJqdGkiOiI1MzI3OTQ3Y2M3NGM0ZWFhYmNkYTVkYzIwZjIzOWE5MSIsInVzZXJfaWQiOjUsInZhbGlkaXR5X3R5cGUiOiJwZXJtYW5lbnQiLCJ2YWxpZGl0eV9leHBpcmUiOm51bGx9.LCF0ptNUKayS1Mtnx4CytmpYYzOq93_NN794BIa2dIs"
    client.set_token(TOKEN)
    print("token OK")
    return client