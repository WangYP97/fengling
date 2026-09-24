from api.threat_scene_api import add_threat_scene_api,query_threat_scene_api,delete_threat_scene_api,update_threat_scene_api
from common.context import Context

"""威胁场景管理crud流程"""
def test_add_threat_scene(api_client):

    #新增威胁场景
    scene_id=add_threat_scene_api(api_client)
    assert scene_id is not None
    print(f"威胁场景创建成功，id为{scene_id}")

    #编辑威胁场景
    new_scene=update_threat_scene_api(api_client,scene_id,description="测试描述")
    scene_name=Context().get("name")
    new_query=query_threat_scene_api(api_client,name=scene_name)[0]
    # print(new_scene)
    # print(new_query)
    assert "成功" in new_scene.get("message")
    assert new_query.get("description") == '测试描述'
    print("编辑成功！")

    #删除威胁场景
    delete_threat_scene_api(api_client,scene_id)
    delete_data=query_threat_scene_api(api_client,name=scene_name)
    # print(delete_data)
    assert len(delete_data) == 0,f"删除后仍能查到：{delete_data}"
    print("删除成功！")





