
#新增组织
def add_organize_api(client):
    path='/api/v1/organize/'
    params={
        "name":"name001",
        "code":"23232",
        "type":"type001",
        "parent":"1",
        "description": "description001"
    }

    res=client.post(path,json=params)

    # print("完整返回：",res.json())

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    # print(res)

    """预留提取ID"""
    org_id=res.json().get('data',{}).get('id')
    return org_id

#编辑组织
def update_organize_api(client,org_id,**fields):

    res=client.patch(f'/api/v1/organize/{org_id}/',json=fields)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json().get('data')


#删除组织
def delete_organize_api(client,org_id):
    res=client.delete(f'/api/v1/organize/{org_id}/')

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

#查询id
def find_organize_by_id(organize_list,org_id):
    """
    递归遍历组织树，找到匹配id
    """
    for item in organize_list:
        #先在父节点匹配
        if item.get('id') == org_id:
            return item

        # 如果有子节点，进子节点匹配
        children=item.get('children',[])
        if children:
            result=find_organize_by_id(children,org_id)
            if result:
                return result

    return None

#获取组织列表
def list_organize_api(client,org_id):
    res=client.get('/api/v1/organize/tree/')

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    organize_list=res.json().get('data',[])
    result=find_organize_by_id(organize_list,org_id)
    return result





