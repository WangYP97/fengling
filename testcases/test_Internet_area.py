import time

from api.Internet_area_api import add_area_api,update_area_api,delete_area_api,query_area_api

"""网络区域的crud流程"""
def test_internet_area(api_client):
    #新增网络区域
    area_id=add_area_api(api_client)
    assert area_id is not None
    print(f"新增id为：{area_id}的网络区域成功！")
    
    time.sleep(2)

    #查询网络区域
    area_detail=query_area_api(api_client,area_id)
    assert area_detail is not None,f"未找到id：{area_id}的网络区域数据"
    assert area_detail['name'] =='区域名称111'
    print(f"找到id：{area_id}的网络区域名称为{area_detail['name']}")

    #编辑网络区域
    update_area=update_area_api(api_client,area_id,name='new网络区域111')
    assert update_area.get('name')== 'new网络区域111'
    print("网络区域编辑成功！")

    #删除网络区域
    delete_area_api(api_client,area_id)
    area_detail=query_area_api(api_client,area_id)
    assert area_detail is None
    print("网络区域删除成功！")


