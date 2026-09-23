
#新增vlan
def add_vlan_api(client):
    params ={
        "area":25,
        "physical_network":"enp10s0",
        "vlan_id":12,
        "network_segment":"1.1.1.0/24",
        "gateway":"1.1.1.1",
        "mask":"255.255.255.0",

        "notes":"beizhu111111111"
    }
    res=client.post('/api/v1/vlan_info/',data=params)


    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json().get('data',{}).get('id')

#编辑vlan
def update_vlan_api(client,vlan_id):
    params = {
        "area": 25,
        "physical_network": "enp10s0",
        "vlan_id": 12,
        "network_segment": "1.1.1.0/24",
        "gateway": "1.1.1.1",
        "mask": "255.255.255.0",

        "notes": "bwwwwwww1111"
    }
    res=client.put(f'/api/v1/vlan_info/{vlan_id}/',data=params)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()

#查询vlan
def query_vlan_api(client,vlan_id):

    res=client.get('/api/v1/vlan_info/?page=1&pageSize=20&area=25&include_descendants=false&organize=1')
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    for item in res.json().get('data'):
        if item.get('id')==vlan_id:
            return item

    return None

#删除vlan
def delete_vlan_api(client,vlan_id):
    res=client.delete(f'/api/v1/vlan_info/{vlan_id}/')

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")