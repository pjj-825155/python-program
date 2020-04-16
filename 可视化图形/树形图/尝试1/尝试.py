import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

data=[{"children":[{"name":"B"},
                   {"children":[{"name":"E"},
                                {"children":[{"name":"J"},
                                             {"name":"K"},
                                             {"name":"L"}],
                                 "name":"F"}],
                    "name":"C",},
                   {"children":[{"children":[{"name":"M"}],
                                 "name":"G"},
                                {"children":[{"name":"N"},
                                             {"name":"O"}],
                                 "name":"H"},
                                {"children":[{"name":"P"},
                                             {"name":"Q"},
                                             {"name":"R"}],
                                 "name":"I"}],
                    "name":"D",}],
       "name":"A",}]

tree=(
     Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )

tree.render("例子1.html")
