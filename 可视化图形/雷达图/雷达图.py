from pyecharts import options as opts
from pyecharts.charts import Radar

v1=[[4300,10000,28000,35000,50000,19000,40000]]
v2=[[5000,14000,28000,31000,42000,21000,46000]]

ra=Radar(init_opts=opts.InitOpts(page_title="雷达图"))
ra.add_schema(
    schema=[
        opts.RadarIndicatorItem(name="销售",max_=6500),
        opts.RadarIndicatorItem(name="管理",max_=16000),
        opts.RadarIndicatorItem(name="技术",max_=30000),
        opts.RadarIndicatorItem(name="客服",max_=38000),
        opts.RadarIndicatorItem(name="研发",max_=52000),
        opts.RadarIndicatorItem(name="市场",max_=25000),
        opts.RadarIndicatorItem(name="利润",max_=50000),
        ]
    )
ra.add("预算",v1)#前面为名称，后面为数值
ra.add("实际",v2)
ra.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
ra.set_global_opts(title_opts=opts.TitleOpts(title="雷达图示例"))
ra.render("雷达图.html")
