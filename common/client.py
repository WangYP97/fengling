import requests
from config.setting import BASE_URL,TIMEOUT

class ApiClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.token = None


    def set_token(self, token):
        """设置token，后续所有请求自动带上token"""
        self.token = token
        header={'Authorization': 'JWT ' + self.token}
        self.session.headers.update(header)

    def get(self,path,**kwargs):
        """
        发送get请求，path：接口请求地址；**kwargs：其他参数，例如：params headers

        """
        url = self.base_url + path
        if "timeout" not in kwargs:
            kwargs["timeout"] = TIMEOUT
        response = self.session.get(url, **kwargs)
        return response

    def post(self,path,**kwargs):
        """post请求"""
        url = self.base_url + path
        if "timeout" not in kwargs:
            kwargs["timeout"] = TIMEOUT

        response = self.session.post(url, **kwargs)
        return response

    def patch(self,path,**kwargs):
        url = self.base_url + path
        if "timeout" not in kwargs:
            kwargs["timeout"] = TIMEOUT

        response = self.session.patch(url, **kwargs)
        return response

    def delete(self,path,**kwargs):
        """post请求"""
        url = self.base_url + path
        if "timeout" not in kwargs:
            kwargs["timeout"] = TIMEOUT

        response = self.session.delete(url, **kwargs)
        return response

