class Context:
    """
    全局上下文
    用来在接口之间传递数据，比如 org_id、vlan_id、scene_name 等
    """

    # 类变量，用来存唯一的实例
    _instance = None

    def __new__(cls):
        # 如果还没有实例，就创建一个
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._data = {}   # 用来存数据的字典
        return cls._instance

    def set(self, key, value):
        """
        存数据
        用法：Context().set("org_id", 123)
        """
        self._data[key] = value

    def get(self, key):
        """
        取数据
        用法：org_id = Context().get("org_id")
        如果 key 不存在，返回 None
        """
        return self._data.get(key)

    def clear(self):
        """清空所有数据"""
        self._data.clear()

    def show(self):
        """打印当前所有数据（调试用）"""
        print(f"当前 Context 内容：{self._data}")