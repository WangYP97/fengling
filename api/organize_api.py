from common.client import ApiClient


#新增组织
def add_organize_api(client):
    path='/api/v1/organize/'
    params={
        "name":"name001",
        "code":"code001",
        "type":"type001",

        "parent":"parent001",
        "description": "description001"
    }

    res=client.post(path,params)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if res.json().get('success')!= 'true':
        raise Exception(f"业务失败：{res.json().get('message')}")

    print(res)

    """预留提取ID"""

#编辑组织
def update_organize_api(client,org_id,**fields):
    res=client.patch(f'/api/v1/organize/{org_id}/',json=fields)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if res.json().get('success')!= 'true':
        raise Exception(f"业务失败：{res.json().get('message')}")


#删除组织
def delete_organize_api(client,org_id):
    res=client.delete(f'/api/v1/organize/{org_id}/')

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if res.json().get('success')!= 'true':
        raise Exception(f"业务失败：{res.json().get('message')}")


#获取组织列表
def list_organize_api(client,org_id):
    res=client.get('/api/v1/organize/tree/')

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if res.json().get('success')!= 'true':
        raise Exception(f"业务失败：{res.json().get('message')}")



