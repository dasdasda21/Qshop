from rest_framework import  serializers
from LoginUser.models import *
class GoodsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:  #元类
        model = Goods   #遍历的对象
        fields =[
            "goods_number",
            "goods_name",
            "goods_price",
            "goods_count",
            "goods_location",
            "goods_safe_date",
            "goods_pro_time",
        ]   #接口返回的字段