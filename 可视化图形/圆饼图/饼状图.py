from example.commons import Faker
from pyecharts.charts import Pie
from pyecharts import options as opts

pie = Pie(init_opts=opts.InitOpts(page_title="pie页面"))  # 设置html页面标题
pie.add("天气类型",[list(z) for z in zip(Faker.choose(),Faker.values())])
#设置标题
pie.set_global_opts(opts.TitleOpts(title="饼状图", subtitle="副标题"))
#pie.show_config()
#保存图表
pie.render("饼状图.html")
