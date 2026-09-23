import json


#新增探针
def add_probe_api(client):
    params={
        # "area":1,
        # "vlan":64,#前端回显网段地址、网关地址、子网掩码、物理网卡
        # "ip":"99.99.7.99",
        # "icmp_probe_awareness":True,
        # "port_probe_awareness":True,
        # "scheme":"random"

        "scheme": "random",
        "vlan": 64,
        "icmp_probe_awareness": True,
        "port_probe_awareness": True,
        "area": 1,
        "ip": "99.99.7.19"

    }

    # print(json.dumps(params))

    res=client.post('/api/v1/probe_info/',json=params)
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()

#查询探针
def query_area_api(client):
    res=client.get('/api/v1/probe_info/?page=1&pageSize=10&vlan=64')
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    probe_list=res.json().get('data',[])
    return probe_list

"""
    根据IP，从列表查询接口返回数据，找到对应id
"""
def find_probe_id_by_ip(client,probe_ip):
    probe_list=query_area_api(client)
    for item in probe_list:
        if item.get('ip') == probe_ip:
            return item

    return None


#编辑探针
def update_probe_api(client,probe_id,**fields):
    """
    参数只包含：
    icmp_probe_awareness
    port_probe_awareness
    scheme
    """
    res=client.patch(f'/api/v1/probe_info/{probe_id}/',data=fields)
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()



#删除探针
def delete_probe_api(client,probe_id):
    param={
        "ids":[probe_id]
    }
    res=client.delete('/api/v1/probe_info/multi_delete/',data=param)
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()