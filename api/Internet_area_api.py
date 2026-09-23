
#新增区域
def add_area_api(client):
    params={
        "name":"区域名称111",
        "type":"type111",
        "owner_organize":1,
        "security_level":1,

        "description":"描述文字11111111"
    }
    res=client.post('/api/v1/internet_area/',data=params)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    area_id=res.json().get('data',{}).get('id')
    return area_id


#编辑区域
def update_area_api(client,area_id,**kwargs):
    res=client.patch(f'/api/v1/internet_area/{area_id}/',data=kwargs)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json().get('data')


#查询区域
def query_area_api(client,area_id):
    res=client.get('/api/v1/internet_area/asset_space/?organize=1')
    # print(res.json().get('data'))

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    area_list=res.json().get('data')
    for item in area_list:
        if item.get('id') ==area_id:
            return item

    return None

#删除区域
def delete_area_api(client,area_id):
    res=client.delete(f'/api/v1/internet_area/{area_id}/')
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")
