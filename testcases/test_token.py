from common.client import ApiClient

def test_token(api_client):
    re=api_client.get('/api/v1/white_list/')
    print(re.text)
    print(re.status_code)

    assert re.status_code == 200

