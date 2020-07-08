+ Python有很多数据可视化的package，主要分为探索性分析方向的（Matplotlib，Seaborn）和交互性信息可视化（Bokeh，Plotly）,后者主要用于与业务结合过程中展现总体分析结果的。

+ Python有很多非常优秀易用的数据可视化的库，作为入门在这里使用Python的matplotlib，事实上Python中很多可视化库都是基于matplotlib开发的，例如Seaborn等。



# pyplot基础语法

## 基本绘图流程

+ 创建画布
    + 判断可要创建子图
+ （选定子图）
+ 添加标题、轴名称、轴刻度
+ 绘制图形
+ 添加图例
+ （绘制其他子图）
+ 保存图形
+ 显示图形



## 创建画布与创建子图

+ plt.figure()
    + 创建一个空白画布，可以指定画布的大小和像素
+ figure.add_subplot()
    + 创建并选中子图，可以指定子图的行数，列数，与选中图片编号



## 添加画布内容

+ plt.title，添加标题，可以指定标题名称、位置、颜色、字体大小等参数

+ plt.xlabel，添加x轴名称，可以指定位置、颜色、字体大小等参数
+ plt.ylabel，添加y轴名称
+ plt.xlim，指定当前图形x轴的范围，只能确定一个数值区间，无法使用字符串标识
+ plt.ylim，指定y轴的范围
+ plt.xticks，指定x轴刻度的数目与取值
+ plt.yticks
+ plt.legend，指定当前图形的图例，可以指定大小、位置、标签



## 保存与展示图形

+ plt.savefig()，保存绘制的图片，可以指定图片的分辨率、边缘的颜色等参数
+ plt.show()，在本机显示图形





# 绘制散点图

+ 利用散点的分布形态反映特征间的统计关系

+ 值由点在图表中的位置标示，类别由图表中的不同标记表示，通常用于比较跨类别的数据

+ `matplotlib.pyplot.scatter(x, y, s=None, c=None,marker=None,alpha=None, **kwargs)`
    + x，y：接收array，表示x轴和y轴对应的数据
    + s：接收数值或者一维的array，指定点的大小，若传入一维array则表示每个点的大小，默认为None
    + c：接收颜色或者一维的array，指定点的颜色
    + marker：接收特定的string，表示绘制的点的类型，默认为None
    + alpha：接收0-1的小数，表示点的透明度，默认为None



# 绘制折线图

+ 将数据点按顺序连接起来

+ 用于查看因变量y随着自变量x改变的趋势

+ 适合用于显示随时间而变化的连续数据

+ 还能看出数量的差异和增长趋势的变化

+ `matplotlib.pyplot.plot(*args, **kwargs)`
    + plot()，官方文档的语法中只要求填入不定长参数
    + 实际可以填入的主要参数为
        + x,y：array，表示x轴和y轴对应的数据
        + color：string，指定线条的颜色，默认为None
            + 常用颜色
            + b，蓝色；g，绿色；r，红色
            + c，青色；y，黄色；m，品红
            + k，黑色；w，白色
        + linestyle：string，指定线条类型，默认为 "-"
        + marker：string，表示绘制定的类型，默认为None
        + alpha：接收0-1的小数，表示点的透明度，默认为None

+ 如果为plot()命令提供单个列表或数组 ，matplotlib假定它是一系列y值，并自动为您生成x值。由于python范围以0开头，因此默认的x向量与y的长度相同，但以0开头。因此x数据为 [0,1,2,3]。



# 绘制直方图（Histogram）

+ 横轴表示数据所属类别，纵轴表示数量或者占比

+ 直观查看数据的分布状态
+ 可以看出分布表中无法发现的数据模式、样本的频率分布和总体的分布

+ `matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, hold=None, data=None, **kwargs)`
    + x，表示条形在x轴的坐标
    + height：array，表示x轴所代表数据的数量
    + width：0-1直接的float，指定直方图的宽度，默认为0.8
    + color：接收特定string或者包含颜色字符串的array，表示直方图的颜色，默认为None



**注：条形图横轴表示类别或具体的数据，直方图横轴表示数据范围**



# 绘制饼图（Pie Graph）

+ 反映部分与部分，部分与整体之间的比例关系

+ 易于显示每组数据相对于总数的大小
+ `matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=None, radius=1, ...)`
    + x：array，用于绘制的数据
    + explode：array，表示指定项离饼图圆心为n个半径，默认None
    + labels：array，指定每一项的名称，默认为None
    + colors：接收特定string或者包含颜色字符串的array，表示饼图的颜色，默认为None
    + autopct：string，指定数值的显示方式，默认为None
    + pctdistance：float，指定每一项的比例和距离饼图圆心n个半径，默认为0.6
    + labeldistance：float，指定每一项的名称和距离饼图圆心n个半径，默认为1.1
    + radis：float，表示饼图的半径，默认为1



# 绘制箱线图（boxplot）

+ 能提供有关数据位置和分散情况的关键信息
+ 尤其在比较不同特征时，更能表现其分散程度差异
+ **箱线图利用数据中五个统计量（最小值、下四分位数、中位数、上四分位数和最大值）来描述数据**
+ 可以粗略看出数据是否具有对称性、分布的分散程度等信息，特别可以用于几个样本的比较

+ `matplotlib.pyplot.boxplot(x, notch=None, sym=None, vert=None, whis=None, position=None, widths=None, patch_artist=None, meanline=None, labels=None,...)`
    + x：array，表示用于绘制的数据
    + notch：boolean，表示中间箱体是否有缺口，默认None
    + sym：string，指定异常点形状，默认None
    + vert：boolean，表示图形是横向或者纵向，默认为None
    + position：array，表示图形位置，默认None
    + widths：scalar或者array，表示每个箱体的宽度，默认为None
    + labels：array，指定每一个箱线图的标签
    + menline：boolean，表示是否显示均值线，默认为False



# 中文乱码和符号乱码修正

rcParams可以用于设置图的分辨率、大小，文字字体等信息

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.rcParams['axes.unicode_minus'] = False



# 其他

+ matplotlib在任何文本表达式中接受TeX方程表达式（数学公式）。编写一个**由美元符号包围**的TeX表达式。

+ plt.title(r'$\sigma_i=15$')

