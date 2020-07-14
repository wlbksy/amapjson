class Marker:
    def __init__(self):
        self.center = None
        # Number, 圆半径，单位: 米
        self.radius = None
        # Number, 层叠顺序, 默认zIndex:10
        self.zIndex = None
        # Bool, 是否将覆盖物的鼠标或touch等事件冒泡到地图上, 默认 false
        self.bubble = None
        # String, 指定鼠标悬停时的鼠标样式
        self.cursor = None
        # String, 线条颜色，使用16进制颜色代码赋值。默认值为#006600
        self.strokeColor = None
        # Float, 轮廓线透明度，取值范围[0,1]，0表示完全透明，1表示不透明。默认为0.9
        self.strokeOpacity = None
        # Number, 轮廓线宽度
        self.strokeWeight = None
        # String, 轮廓线样式，实线:solid，虚线:dashed
        self.strokeStyle = None
        # Array, 勾勒形状轮廓的虚线和间隙的样式，此属性在strokeStyle 为dashed 时有效
        # 取值： 实线：[0, 0, 0]
        #       虚线：[10, 10] 表示 10 个像素的实线和 10 个像素的空白（如此反复）组成的虚线
        #      点画线：[10, 2, 10] 表示 10 个像素的实线和 2 个像素的空 + 10 个像素的实线和
        #             10 个像素的空白（如此反复） 组成的虚线
        self.strokeDasharray = None
        # String, 圆形填充颜色,使用16进制颜色代码赋值。默认值为#006600
        self.fillColor = None
        # Float, 圆形填充透明度，取值范围[0,1]，0表示完全透明，1表示不透明。默认为0.9
        self.fillOpacity = None
        # Any, 用户自定义属性，支持JavaScript API任意数据类型
        self.extData = None

        self.has_center_and_radius = False

    def set_center_radius(self, center, radius):
        self.center = center
        self.radius = radius
        self.has_center_and_radius = True

    def toGeojson(self):
        assert self.has_center_and_radius, 'marker need center and radius'

        geojson_dict = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'Point',
                'coordinates': self.center
            }
        }

        properties = {
            'radius': self.radius,
            'zIndex': self.zIndex,
            'bubble': self.bubble,
            'cursor': self.cursor,
            'strokeColor': self.strokeColor,
            'strokeOpacity': self.strokeOpacity,
            'strokeWeight': self.strokeWeight,
            'strokeStyle': self.strokeStyle,
            'strokeDasharray': self.strokeDasharray,
            'fillColor': self.fillColor,
            'fillOpacity': self.fillOpacity,
            'extData': self.extData
        }

        for k, v in properties.items():
            if v is not None:
                geojson_dict['properties'][k] = v
        return geojson_dict
