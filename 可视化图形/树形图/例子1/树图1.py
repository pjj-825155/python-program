import json
import os

from pyecharts import options as opts
from pyecharts.charts import Page, Tree

data =[
    {
        "name": "Peter",
        "children": [
            {
                "name": "Tom",
                "children": [[[]]]
            },
            {
                "name": "John",
                "children": [[[]]]
            },
        ]
    }
]

tree=(
     Tree()
        .add("", data)
        .set_global_opts(title_opts=opts.TitleOpts(title="Tree-基本示例"))
    )

tree.render("例子1.html")
