import pytest

from common.client import ApiClient

@pytest.fixture(scope="session")
def api_client():
    client=ApiClient()
    TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg5Njk5ODQyLCJqdGkiOiIxZmY5OGQ2MDMwZjA0NWMxOGE4OTU5N2U2ODJjYjU2MiIsInVzZXJfaWQiOjUsInZhbGlkaXR5X3R5cGUiOiJwZXJtYW5lbnQiLCJ2YWxpZGl0eV9leHBpcmUiOm51bGx9.hXFFfavK1vcBQ9DKLehCPqLzWNHj1-TEQJsS6QXZ7ME"
    client.set_token(TOKEN)
    print("token OK")
    return client