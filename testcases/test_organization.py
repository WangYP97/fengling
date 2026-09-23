from api.organize_api import add_organize_api,list_organize_api,update_organize_api,delete_organize_api

import time

def test_org_crud(api_client):
    #创建组织
    org_id=add_organize_api(api_client)
    assert org_id is not None
    print(f"组织新增成功！，id:{org_id}")

    time.sleep(1)

    #查询组织
    list=list_organize_api(api_client,org_id)
    assert list is not None,f"列表里没有找到 org_id={org_id}"
    assert list["name"] == 'name001'
    print(f"查询到id为{org_id}的组织名称为{list['name']}")

    time.sleep(1)
    #编辑组织
    update_organize_api(api_client,org_id,name="newname001",parent="2")
    new_list=list_organize_api(api_client,org_id)
    assert new_list.get("name") == 'newname001'
    assert new_list.get("parent") == 2
    print("编辑成功！")

    #删除组织
    delete_organize_api(api_client,org_id)
    time.sleep(1)

    del_data=list_organize_api(api_client,org_id)
    assert del_data is None
    print("删除成功！")







