from pyecharts import options as opts
from pyecharts.charts import Liquid,Page
from pyecharts.globals import SymbolType

c=Liquid(init_opts=opts.InitOpts(page_title="球形图"))# 设置html页面标题  
c.add("lq",[0.6,0.7])#前一个为最低页面和显示百分数，后一个为最高页面
c.set_global_opts(title_opts=opts.TitleOpts(title="Liquid-基本示例"))
c.render("球形图.html")
