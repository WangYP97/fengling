import time

from common.context import Context


#新增威胁场景
def add_threat_scene_api(client):
    unique_name= f"测试_{int(time.time())}"
    params={
        "name":unique_name,
        "threat_level":1,
        "time_window":1,
        "is_enable":True,
        "trigger_rules": {
            "rules": [
                {
                    "protocol": "HTTP",
                    "dimension": "probe",
                    "limit": 1
                }
            ]
        },

        "description":"ceshi1321312312"
    }
    res=client.post("/api/v1/menace_scene/",json=params)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    scene_id=query_threat_scene_api(client,name=unique_name)[0].get('id')
    ctx=Context()
    ctx.set("scene_id",scene_id)
    ctx.set("name",unique_name)
    return scene_id
    return scene_id

#编辑威胁场景
def update_threat_scene_api(client,scene_id,**kwargs):

    res=client.patch(f"/api/v1/menace_scene/{scene_id}/",json=kwargs)

    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()

#查询威胁场景
def query_threat_scene_api(client,**filters):
    res=client.get("/api/v1/menace_scene/?page=1&page_size=10",params=filters)
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json().get('data')

#删除威胁场景
def delete_threat_scene_api(client,scene_id):
    res=client.delete(f"/api/v1/menace_scene/{scene_id}/")
    if res.status_code != 200:
        raise Exception(f"HTTP请求异常：{res.status_code},{res.text}")

    if not res.json().get('success'):
        raise Exception(f"业务失败：{res.json().get('message')}")

    return res.json()