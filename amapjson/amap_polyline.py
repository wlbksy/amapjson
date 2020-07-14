class Polyline:
    def __init__(self):
        self.path = None
        # Number, 层叠顺序, 默认zIndex:10
        self.zIndex = None
        # Bool, 是否将覆盖物的鼠标或touch等事件冒泡到地图上, 默认 false
        self.bubble = None
        # String, 指定鼠标悬停时的鼠标样式
        self.cursor = None
        # Boolean, 是否绘制成大地线，默认false
        self.geodesic = None
        # Boolean, 线条是否带描边，默认false
        self.isOutline = None
        # Number, 描边的宽度，默认为1
        self.borderWeight = None
        # String, 线条描边颜色，此项仅在isOutline为true时有效，默认：#000000
        self.outlineColor = None
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
        # Boolean, 设置折线是否可拖拽移动，默认为false
        self.draggable = None
        # String, 折线拐点的绘制样式，默认值为'miter'尖角，其他可选值：'round'圆角、'bevel'斜角
        self.lineJoin = None
        # String, 折线两端线帽的绘制样式，默认值为'butt'无头，其他可选值：'round'圆头、'square'方头
        self.lineCap = None
        # Boolean	是否延路径显示白色方向箭头, 默认false。
        # Canvas绘制时有效，建议折线宽度大于6时使用；在3D视图下不支持显示方向箭头
        self.showDir = None
        # Any, 用户自定义属性，支持JavaScript API任意数据类型
        self.extData = None

        self.has_path = False

    def set_path(self, path):
        self.path = path
        self.has_path = True

    def toGeojson(self):
        assert self.has_path, 'polyline need path'

        geojson_dict = {
            'type': 'Feature',
            'properties': {},
            'geometry': {
                'type': 'LineString',
                'coordinates': self.path
            }
        }

        properties = {
            'zIndex': self.zIndex,
            'bubble': self.bubble,
            'cursor': self.cursor,
            'geodesic': self.geodesic,
            'isOutline': self.isOutline,
            'borderWeight': self.borderWeight,
            'outlineColor': self.outlineColor,
            'strokeColor': self.strokeColor,
            'strokeOpacity': self.strokeOpacity,
            'strokeWeight': self.strokeWeight,
            'strokeStyle': self.strokeStyle,
            'strokeDasharray': self.strokeDasharray,
            'draggable': self.draggable,
            'lineJoin': self.lineJoin,
            'lineCap': self.lineCap,
            'showDir': self.showDir,
            'extData': self.extData
        }

        for k, v in properties.items():
            if v is not None:
                geojson_dict['properties'][k] = v
        if 'strokeWeight' not in geojson_dict['properties']:
            geojson_dict['properties']['strokeWeight'] = 3
        return geojson_dict
