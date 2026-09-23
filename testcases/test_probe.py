from api.probe_api import add_probe_api,update_probe_api,find_probe_id_by_ip,delete_probe_api

"""探针crud流程"""
def test_probe_crud(api_client):
    #添加探针
    add_probe_api(api_client)

    #根据ip查找探针id
    probe_id=find_probe_id_by_ip(api_client,"99.99.7.19").get("id")
    assert probe_id is not None
    print(f"创建探针成功，id为{probe_id}")

    #编辑探针
    new_probe=update_probe_api(api_client,probe_id,scheme=2)
    assert '成功' in new_probe.get('message')
    print("编辑成功！")

    #删除探针
    delete_probe_api(api_client,probe_id)
    assert find_probe_id_by_ip(api_client,probe_id) is None
    print(f"id：{probe_id}的探针删除成功！")