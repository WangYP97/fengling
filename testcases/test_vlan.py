from api.vlan_api import add_vlan_api,query_vlan_api,delete_vlan_api,update_vlan_api

"""VLAN区域的crud流程"""
def test_vlan_crud(api_client):
    #新增vlan区域
    vlan_id=add_vlan_api(api_client)
    assert vlan_id is not None

    #查询新增vlan
    vlan_detail=query_vlan_api(api_client,vlan_id)
    assert vlan_detail is not None,f"网络区域创建失败"
    assert vlan_detail.get("network_segment") == '1.1.1.0/24'
    print(f"成功创建id为：{vlan_id}的vlan区域：{vlan_detail.get('network_segment')}")

    #编辑vlan区域
    new_vlan=update_vlan_api(api_client,vlan_id)
    vlan_detail=query_vlan_api(api_client,vlan_id)
    assert new_vlan.get("message") == "编辑成功"
    assert vlan_detail.get("notes") == 'bwwwwwww1111'
    print('vlan编辑成功！')

    #删除vlan
    delete_vlan_api(api_client,vlan_id)
    vlan_detail=query_vlan_api(api_client,vlan_id)
    assert vlan_detail is None
    print(f"id为{vlan_id}的vlan区域已经被删除！")


