from example.commons import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar

def bar_base():
    bar = Bar(init_opts=opts.InitOpts(page_title="bar页面"))  # 设置html页面标题
    #bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])  # 设置x轴的参数
    bar.add_xaxis(Faker.choose())#随机生成
    bar.add_yaxis("A", Faker.values())
    bar.add_yaxis("B", Faker.values())

    # 设置全局配置项，可选
    bar.set_global_opts(opts.TitleOpts(title="主标题", subtitle="副标题"))
    # render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
    bar.render("柱状图例子.html")  # 也可以自己指定文件名

if __name__ == "__main__":
    bar_base()
