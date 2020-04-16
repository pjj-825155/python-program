from pyecharts.charts import Map
from pyecharts import options as opts
 
data=[("湖北",1058),
      ("浙江",104),
      ("广东",98),
      ("河南",83),
      ("重庆",75),
      ("湖南",69),
      ("安徽",60),
      ("北京",54),
      ("山东",46),
      ("四川",44),
      ("上海",40),
      ("江西",36),
      ("广西",33),
      ("江苏",33),
      ("福建",29),
      ("海南",22),
      ("陕西",22),
      ("辽宁",19),
      ("黑龙江",15),
      ("河北",13),
      ("天津",13),
      ("云南",11),
      ("山西",9),
      ("甘肃",7),
      ("内蒙古",7),
      ("澳门",5),
      ("香港",5),
      ("贵州",5),
      ("宁夏",4),
      ("吉林",4),
      ("新疆",4),
      ("青海",4),
      ("台湾",3),]
c= (
    Map()
    .add("",data,"china")
    #不显示地名
    #.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="地图"),
        #显示颜色
        visualmap_opts=opts.VisualMapOpts(max_=200),
        #颜色分段
        #visualmap_opts=opts.VisualMapOpts(max_=1200, is_piecewise=True),
        )
    )
c.render('map.html')
