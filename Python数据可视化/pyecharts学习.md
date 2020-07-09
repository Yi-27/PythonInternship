+ Echarts 是一个由百度开源的数据可视化，凭借着良好的交互性，精巧的图表设计，得到了众多开发者的认可。而 Python 是一门富有表达力的语言，很适合用于数据处理。当数据分析遇上数据可视化时，pyecharts 诞生了。

+ pyecharts 分为 v0.5.X 和 v1 两个大版本，v0.5.X 和 v1 间不兼容，v1 是一个全新的版本。（使用版本为v1）

+ 官网：https://www.echartsjs.com/index.html

+ Pyecharts官网：https://pyecharts.org/#/zh-cn/intro

+ 安装：pip install pyecharts



# 绘图逻辑

+ 选择图表类型

+ 添加数据

+ 设置全局变量

+ 显示及保存图表



+ 图表类型: from pyecharts.charts import *
+ 函数——说明
    + Scatter：散点图
    + Funnel：漏斗图
    + Bar：柱状图
    + Gauge：仪表盘
    + Pie：饼图
    + Graph：关系图
    + Line：折线/面积图
    + Liquid：水球图
    + Radar：雷达图
    + Parallel：平行坐标系
    + Sankey：桑基图
    + Polar：极坐标系
    + WordCloud：词云图
    + HeatMap：热力图



# 添加数据

+ 散点图、折线图等二维数据图形可通过 .add_xaxis(xaxis_data=x)和.add_yaxis(series_name='', y_axis=y)方法设置

+ 饼图等一维图形可通过.add(series_name=‘’, data_pair=[(i, j)for i, j in zip(lab, num)])方法设置参数

+ pyecharts 所有方法均支持链式调用。



# 显示、保存图表

+ .get_options() # 该行只为了查看配置项，方便调试时使用

+ .render()：默认将会在当前目录下生成一个 render.html 的文件，支持 path 参数，设置文件保存位置，如 render(r"e:\my_first_chart.html")，文件用浏览器打开。

+ .Jupyter Notebook() 直接调用 render_notebook ()随时随地渲染图表



# 全局配置组件：定制图表

+ 使用 options 配置项，在 pyecharts 中，一切皆 Options。

+ 全局配置项可通过 set_global_options 方法设置
+ 比如，添加标题：
    + .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))



# pyecharts地理图表

+ 有时我们会很希望把数据展示在地图上，来做数据可视化，使数据更加清晰明了。

+ 比如：微信好友全国分布，显示票房省份数据，全国评分显示



**具体代码示例看ipynb文件**