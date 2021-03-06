# 读写数据库数据

## 数据库数据读取

pandas库提供了读取和存储**关系型数据库**数据的函数和方法。

但除了pandas库外，还**需要使用SQLAlchemy库建立对应的数据库连接**

+ SQLAlchemy配合相应数据库的Python连接工具
    + 比如，MySQL数据库需要安装mysqlclient或者pymysql库
    + 使用create_engine()建立一个数据库连接
        + 参数是一个连接字符串
        + 比如`数据库产品名+连接工具名：//用户名:密码@数据库IP地址:数据库端口号/数据库名称?charset=数据库数据编码`
        + engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8")
    + read_sql_table()，**只能够读取数据库的某一个表格**， 不能实现查询的操作。
        + pandas.read_sql_table(table_name, con, schema=None, index_col=None,
            coerce_float=True, columns=None)
    + read_sql_query()，**则只能实现查询操作**，不能直接读取数据库中的某个表。
        + pandas.read_sql_query(sql, con, index_col=None, coerce_float=True)
    + read_sql()，是两者的综合，**既能够读取数据库中的某一个表， 也能够实现查询操作**。
        + pandas.read_sql(sql, con, index_col=None, coerce_float=True, columns=None)



## 数据库数据存储

只有一个to_sql()方法

+ DataFrame.to_sql(mame, con, schema=None, if_exists='fail', index=True, index_label=None, dtype=None)
    + name：接收string。代表数据库表名。无默认。
    + con：接收数据库连接。无默认。
    + index：接收boolean。表示是否将行索引作为数据传入数据库。默认True。
    + index_label：接收string或者sequence。代表是否引用索引名称，如果index参数为True此参数
        为None则使用默认名称。如果为多重索引必须使用sequence形式。默认为None 
    + dtype：接收dict。代表写入的数据类型(列名为key, 数据格式为values)。默认为None.

+ data = pd.read_sql("select * from meal_order_detail1", con=engine)
    data.to_sql("tmp", con=engine, if_exists="replace")



# 读写文本文件

## 文本文件读取

文本文件是一种由若干行字符构成的计算机文件，它是一种典型的顺序文件。
csv是一种逗号分隔的文件格式，因为其分隔符不一定是逗号，又被称为字符分隔
文件，文件以纯文本形式存储表格数据(数字和文本)

+ 使用read_table来读取文本文件。
    + pandas.read_table(filepath_or_ buffer, **sep= '\t'**，header= 'infer ，names=None, index_col=None,dtype=None, engine =None, nrows=None)
+ 使用read_csv函数来读取csv文件。
    + pandas.read_csv(filepath_or_buffer, **seq=','**, header= 'infer ,names = None, index_col = None,dtype=None, engine=None, nrows=None)


read_table和read_csv常用参数及其说明。

+ filepath：接收string。代表文件路径。无默认。
+ sep：接收string。代表分隔符。read_csv 默认为','，read_table默认为制表符"[Tab]"
+ header：接收int或sequence.表示将某行数据作为列名。默认为infer, 表示自动识别。
+ names：接收array。表示列名。默认为None.
+ index_col：接收int、sequence或False。 表示索引列的位置，取值为sequence则代表多重索
    引。默认为None。
+ dtype：接收dict.代表写入的数据类型(列名为key,数据格式为values)。默认为None.
+ engine：接收c或者python。代表数据解析引擎。默认为C。



## 文本文件存储

文本文件的存储和读取类似，结构化数据可以通过pandas中的to_ csv函数实现以csv文件格式存储文件。
DataFrame.to_csv(path_or_buf=Nond, sep=','，na_rep=”, columns=None, header=True,index=True, index_label=None, mode='w' ,encoding=None)

+ path_or_buf：接收string。代表文件路径。无默认。
+ index：接收boolean,代表是否将行名(索引)写出。默认为True。
+ index_label：接收sequence。表示索引名。默认为None
+ sep：接收string。代表分隔符。默认为","。
+ na_ rep：接收string。代表缺失值。默认为""
+ mode：接收特定string。代表数据写入模式。默认为w。
+ columns：接收list。 代表写出的列名。默认为None。
+ encoding：接收特定string。代表存储文件的编码格式。默认为None。
+ header：接收boolean,代表是否将列名写出。默认为True。



# 读写Excel文件

## Excel文件读取

pandas提供了read_excel函数来读取"xIs" "xIsx" 两种Excel文件。
pandas.read_excel(io, sheetname=0, header=0, index_col=None,


+ io：接收string。表示文件路径。无默认。
+ sheetname：接收string、int。 代表excel表内数据的分表位置。默认为0。
+ header：接收int或sequence。表示将某行数据作为列名。默认为infer, 表示自动识别。
+ names：接收int、sequence或者False。 表示索引列的位置，取值为sequence则代表多重索引。默认为None。
+ index_col：接收int、sequence或者False。 表示索引列的位置，取值为sequence则代表多重索引。默认为None。
+ dtype：接收dict.代表写入的数据类型(列名为key,数据格式为values)。默认为None。



## Excel文件储存

+ 将文件存储为Excel文件，可以使用to excel方法。其语法格式如下。
    DataFrame.to_excel(excel_writer= None, sheetname=None', na_rep=”",header=True, index=True, index_label_None, mode= 'w’,encoding=None)
+ to_ csv方法的常用参数基本一 致，区别之处在于指定存储文件的文件路径参数名称为excel writer,并且没有sep参数，增加了一个sheetnames参数用来指定存储的Excel sheet的名称，默认为sheet1.



# DataFrame

## 基础属性

+ values：元素
+ index：索引
+ columns：列名
+ dtypes：类型
+ size：元素个数
+ ndim：维度数
+ shape：数据形状（行列数目）



## 增删改查DataFrame数据

### 查看访问DataFrame中的数据数据基本查看方式

+ **对单列数据的访问**: 
    + DataFrame的**单列数据为一一个Series**
    + 根据DataFrame的定义可以知晓DataFrame是一个带有标签的二维数组，**每个标签相当每一列的列名**。
        有以下两种方式来实现对单列数据的访问。
    + **以字典访问某一个key的值的方式使用对应的列名**，实现单列数据的访问。
    + **以属性的方式**访问，实现单列数据的访问。(不建议使用， 易引起混淆)

+ **对某一列的某几行访问**:
    + 访问DataFrame中某一 列的某几行时，单独一列的DataFrame可以视为一个Series (另一种pandas提供的类， 可以看作是只有一列的DataFrame)，而**访问一个Series基本和访问一个一维的ndarray相同**。
+ **对多列数据访问**: 
    + 访问DataFrame多列数据可以**将多个列索引名称视为一个列表**，同时访问DataFrame多列数据中的多行数据和访问单列数据的多行数据方法基本相同。

+ **对某几行访问**:
    + 如果只是需要访问DataFrame某几行数据的实现方式则和上述的访问多列多行相似，**选择所有列，使用"."代替**即可。
    + **head和tail也可以得到多行数据**，但是用这两种方法得到的数据都是从**开始**或者**末尾**获取的连续数据。默认参数为访问5行，只要在方法后方的“()" 中填入访问行数即可实现目标行数的查看。



### 查看访问DataFrame中的数据loc, iloc访问方式

+ **loc方法**是针对DataFrame**索引名称的切片方法**，如果传入的不是索引名称，那么切片操作将无法执行。利用loc方法，**能够实现所有单层索引切片操作**。loc方法使用方法如下。
    + DataFrame.loc[行索引名称或条件, 列索引名称]
+ iloc和loc区别是**iloc接收的必须是行索引和列索引的位置**。iloc方法的使用方法如下。
    + DataFrame.iloc[行索引位置, 列索引位置]
    + 索引位置都可以是一个列表，而不是只单单是一个列，可以是其中的几列

+ 若使用detail.iloc[**detail['order_ id"]=='458'**,[1,5]]读取数据，则会报错，原因在于此处条件**返回的为一个布尔值Series**, 而iloc可以接收的数据类型并不包括Series。根据Series的构成只要取出该Series的values就可以了。 需改为detail.iloc[**(detail['order id']=='458').values**,[1,5]])。 
+ loc更加灵活多变，代码的可读性更高，iloc的代码简洁，但可读性不高。具体在数据分析工作中使用哪一种方法，根据情况而定，大多数时候建议使用loc方法。
    + 使用loc方法和iloc实现多列切片，其**原理**的通俗解释就是**将多列的列名或者位置作为一个列表或者数据传入**。
    + 使用loc, iloc方法可以取出DataFrame中的任意数据。
    + 在**loc**使用的时候内部传入的行索引名称如果为一个区间，则**前后均为闭区间**;
    + **iloc**方法使用时内部传入的行索引位置或列索引位置为区间时，则为**前闭后开区间**。
    + **loc内部还可以传入表达式，结果会返回满足表达式的所有值**。



### 查看访问DataFrame中的数据——切片方法之ix 

+ ix方法更像是loc和iloc两种切片方法的融合。ix方法在使用时**既可以接收索引名称也可以接收索引位置**。其使用方法如下。
    + DataFrame.ix[行索引的名称或位置或者条件, 列索引名称或位置]
+ 使用ix方法时有个注意事项
    + 第一条，**当索引名称和位置存在部分重叠时，ix默认优先识别名称**。
    + 第二条，用索引时，会比iloc方法要慢，因此建议使用iloc和loc，而不是使用ix



### 更新修改DataFrame中的数据

+ 更改DataFrame中的数据， 原理是**将这部分数据提取出来，重新赋值为新的数据**。
+ 需要注意的是，**数据更改直接针对DataFrame原数据更改**，操作无法撤销，如果做出更改，需要对更改条件做确认或对数据进行备份。



### 为DataFrame增添数据

+ DataFrame添加一列的方法非常简单，只需要新建一个列索引。 并对该索引下的数据进行赋值操作即可。
+ 新增的一列值是相同的则直接赋值一个常量即可。



### 删除某列或某行数据

删除某列或某行数据需要用到pandas提供的方法drop, drop方法的用法如下。

+ axis为0时表示删除行，axis为1时表示删除列。
    drop(labels, axis=0, level=None, inplace=False, errors='raise')
+ 常用参数如下所示。
    + labels：接收string或array。代表删除的行或列的标签。无默认。
    + axis：接收0或1.代表操作的轴向。默认为0.
    + levels：接收int或者索引名。代表标签所在级别。默认为None。
    + inplace：接收boolean。代表操作是否对原数据生效。默认为False.



# pandas描述统计方法

pandas是基于numpy库的，因此可以使用numpy的统计方法

+ pandas提供了更加便利的方法来计算均值,如detail[' amounts ].mean()。
+ pandas还提供了一个方法叫作**describe**,**能够一次性得出数据框所有数值型特征的非空值数目、均值、四分位数、标准差。**
+ 方法名称和说明
    + min，最小值
    + max，最大值
    + mean，均值
    + ptp，极差
    + median，中位数
    + std，标准差
    + var，方差
    + cov，协方差
    + sem，标准误差
    + mode，众数
    + skew，样本偏度
    + kurt，样本峰度
    + quantile，四分位数
    + count，非空值数目
    + describe，描述统计
    + mad，平均绝对离差



## 类别型特征的描述性统计

+ 描述类别型特征的分布状况， 可以使用频数统计表。pandas库中实现频数统计的方法为value_ counts.
+ pandas提供了categories类，可以使用astype方法将 目标特征的数据类型转换为category类别。
+ describe方法除 了支持传统数值型以外，还能够支持对category类型的数据进行描述性统计，四个统计量分别为列非空元素的数目，类别的数目，数目最多的类别，数目最多类别的数目。



# 转换与处理时间序列数据

## pandas时间相关的类

在多数情况下， 对时间类型数据进行分析的前提就是将原本为字符串的时间转换为标准时间类型。
**pandas继承了NumPy库和datetime库的时间相关模块**，提供了6种时间相关的类。

+ Timestamp：最基础的时间类。表示某个时间点。在绝大多数的场景中的时间数据都是Timestamp形式的时间。
    + 其中Timestamp作为时间类中最基础的，也是最为常用的。在多数情况下，**时间相关的字符串都会转换成为Timestamp**。pandas提供了**to_datetime**函数， 能够实现这一目标。
    + 值得注意的是，Timestamp类型时间是有限制的。
    + 在多数涉及时间相关的数据处理，统计分析的过程中，需要提取时间中的年份，月份等数据。使用对应的
        Timestamp类属性就能够实现这一目的。
+ Period：表示单个时间跨度，或者某个时间段，例如某一天，某一小时等。
+ Timedelta：表示不同单位的时间，例如1天，1.5小时， 3分钟，4秒等，而非具体的某个时间段。
    + Timedelta类
        Timedelta是时间相关的类中的一个异类，不仅能够使用正数，还能够使用负数表示单位时间，例如1秒，2分钟，3小时等。**使用Timedelta类， 配合常规的时间相关类能够轻松实现时间的算术运算**。目前Timedelta函数中时间周期中没有年和月。所有周期名称，对应单位及其说明如下表所示。
    + 使用Timedelta ，可以很轻松地实现在某个时间上加减一段时间 。
    + 除了使用Timedelta实现时间的平移外，还能够直接对两个时间序列进行相减，从而得出一个Timedelta.
        + data['lock_time'] + pd.Timedelta(days=1) # 每个数据加1天
        + 周期名称——单位——说明
            + weeks，无，星期
            + seconds，S，秒
            + days，D，天
            + milliseconds，ms，毫秒
            + hours，h，小时
            + microseconds，us，微妙
            + minutes，m，分
            + nanoseconds，ns，纳秒
+ Datetimelndex：一组Timestamp构成的Index, 可以用来作为Series或者DataFrame的索引
+ Periodtimelndex：一组Period构成的Index, 可以用来作为Series或者DataFrame的索引|。
    + 除了将数据字原始DataFrame中直接转换为Timestamp格式外，还可以将数据单独提取出来将其转换为Datetimelndex或者PeriodIndex。
    + 转换为PeriodIndex的时候需要注意，需要通过freq参数指定时间间隔，常用的时间间隔有Y为年，M为月，D为日，H为小时，T为分钟，S为秒。两个函数可以用来转换数据还可以用来创建时间序列数据，其参数非常类似。
+ Timedeltalndex：一组Timedelta构成的Index,可以用来作为Series或者DataFrame的索引





# 使用分组聚合进行组内计算

### groupby方法的参数及其说明

该方法提供的是分组聚合步骤中的拆分功能，能根据索引或字段对数据进行分组。其常用参数与使用格式如下。

+ DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True,squeeze=False, **kwargs)
    + by：接收list, string, mapping或generator。 用于确定进行分组的依据，无默认。
    + axis：接收int。表示操作的轴向，默认对列进行操作。默认为0。
    + level：接收int或者索引名。代表标签所在级别。默认为None。
    + as_index：接收boolearn。表示聚合后的聚合标签是否以DataFrame索引形式输出。默认为True。
    + sort：接收boolearn。表示是否对分组依据分组标签进行排序。默认为True,
    + group_keys：接收boolearn。表示是否显示分组标签的名称。默认为True。
    + squeeze：接收boolearn。表示是否在允许的情况下对返回数据进行降维。默认为False。

+ **by参数的特别说明**
    + 如果传入的是一个函数则对索引进行计算并分组。
    + 如果传入的是一个字典或者Series则字典或者Series的值用来做分组依据。
    + 如果传入一个NumPy数组则数据的元素作为分组依据。
    + 如果传入的是字符串或者字符串列表则使用这些字符串所代表的字段作为分组依据。



### GroupBy对象常用的描述性统计方法

用groupby方法分组后的结果并不能直接查看，而是被存在内存中，输出的是内存地址。实际上分组后的数据对象GroupBy类似Series与DataFrame，是pandas提供的一种对象。GroupBy对象常用的描述性统计方法如下。

+ 方法名称——说明
    + count：计算分组的数目,包括缺失值。
    + cumcount：对每个分组中组员的进行标记，0至n-1。
    + head：返回每组的前n个值。
    + size：返回每组的大小。
    + max：返回每组最大值。
    + min：返回每组最小值。
    + mean：返回每组的均值。
    + std：返回每组的标准差。
    + median：返回每组的中位数。
    + sum：返回每组的和。



### 使用agg方法聚合数据

#### agg和aggregate函数参数及其说明

+ agg，aggregate方法都支持对每个分组应用某函数，包括Python内置函数或自定义函数。同时这两个方法能够也能够直接对DataFrame进行函数应用操作。

+ 在正常使用过程中，agg函数和aggregate函数对DataFrame对象操作时功能几乎完全相同，因此只需要掌握其中一个函数即可。它们的参数说明如下表。
    + *DataFrame.***agg**(**func**, axis=0, *args**, **kwargs)
    + *DataFrame.***aggregate**(**func**, axis=0, *args**, **kwargs)
        + func：接收list、dict、function。表示应用于每行/每列的函数
        + axis：接收0或1。代表操作的轴向。默认为0

#### agg方法求统计量

+ 可以使用agg方法一次求出当前数据中所有菜品销量和售价的总和与均值，如detail[['counts','amounts']].agg([np.sum,np.mean]))。

+ 对于某个字段希望只做求均值操作，而对另一个字段则希望只做求和操作，可以使用字典的方式，将两个字段名分别作为key，然后将NumPy库的求和与求均值的函数分别作为value，如detail.agg({'counts':np.sum,'amounts':np.mean}))。

+ 在某些时候还希望求出某个字段的多个统计量，某些字段则只需要求一个统计量，此时只需要将字典对应key的value变为列表，列表元素为多个目标的统计量即可，如detail.agg({'counts':np.sum,'amounts':[np.mean,np.sum]}))

#### agg方法与自定义的函数

+ 在agg方法可传入读者自定义的函数。

+ 使用自定义函数需要注意的是NumPy库中的函数np.mean，np.median，np.prod，np.sum，np.std，np.var能够在agg中直接使用，但是在自定义函数中使用NumPy库中的这些函数，如果计算的时候是单个序列则会无法得出想要的结果，如果是多列数据同时计算则不会出现这种问题。

+ 使用agg方法能够实现对每一个字段每一组使用相同的函数。

+ 如果需要对不同的字段应用不同的函数，则可以和Dataframe中使用agg方法相同。



### 使用apply方法聚合数据

+ apply方法类似agg方法能够将函数应用于每一列。不同之处在于**apply方法相比agg方法传入的函数只能够作用于整个DataFrame或者Series**，而**无法像agg一样能够对不同字段，应用不同函数获取不同结果**。

+ 使用apply方法对GroupBy对象进行聚合操作其方法和agg方法也相同，只是使用agg方法能够实现对不同的字段进行应用不同的函数，而apply则不行。
+ *DataFrame.***apply**(**func**, axis=0, broadcast=False, raw=False, reduce=None,*args=(), **kwds)
    + 参数名称——说明
    + func：接收functions。表示应用于每行/列的函数。无默认。
    + axis：接收0或1。代表操作的轴向。默认为0。
    + broadcast：接收boolearn。表示是否进行广播。默认为False.
    + raw：接收boolearn。表示是否直接将ndarray对象传递给函数。默认为False。
    + reduce:接收boolearn或者None。表示返回值的格式。默认None.



### 使用transform方法聚合数据

+ transform方法能够**对整个DataFrame的所有元素进行操作**。且transform方法只有一个参数“func”，表示对DataFrame操作的函数。

+ 同时transform方法还能够对DataFrame分组后的对象GroupBy进行操作，可以实现组内离差标准化等操作。

+ 若在计算离差标准化的时候结果中有NaN，这是由于根据离差标准化公式，最大值和最小值相同的情况下分母是0。而**分母为0的数在Python中表示为NaN**。



# 创建透视表与交叉表

## 使用povit_table函数创建透视表

### pivot_table函数常用参数及其说明

+ 利用pivot_table函数可以实现透视表，pivot_table()函数的常用参数及其使用格式如下。

+ *pandas.***pivot_table**(data, values=None, index=None, columns=None,aggfunc='mean', fill_value=None, margins=False,dropna=True,margins_name='All')
    + 参数名称——说明
    + data接收：DataFrame。表示创建表的数据。无默认。
    + values：接收字符串。用于指定想要聚合的数据字段名，默认使用全部数据。默认为None.
    + index：接收string或list。表示行分组键。默认为None.
    + columns：接收string或list。表示列分组键。默认为None。
    + aggfunc：接收functions。表示聚合函数。默认为mean。
    + margins：接收boolearn.表示汇总(Total) 功能的开关，设为True后结果集中会出现名为"ALL" 的行和列。默认为False。
    + dropna：接收boolearn.表示是否删掉全为NaN的列。默认为True。



### pivot_table函数主要的参数调节

+ 在不特殊指定聚合函数aggfunc时，会默认使用numpy.mean进行聚合运算，numpy.mean会自动过滤掉非数值类型数据。可以通过指定aggfunc参数修改聚合函数。

+ 和groupby方法分组的时候相同，pivot_table函数在创建透视表的时候分组键index可以有多个。

+ 通过设置columns参数可以指定列分组。

+ 当全部数据列数很多时，若只想要显示某列，可以通过指定values参数来实现。

+ 当某些数据不存在时，会自动填充NaN，因此可以指定fill_value参数，表示当存在缺失值时，以指定数值进行填充。

+ 可以更改margins参数，查看汇总数据。



## 使用crosstab函数创建交叉表

+ 交叉表是一种特殊的透视表，主要用于计算分组频率。利用pandas提供的crosstab函数可以制作交叉表，crosstab函数的常用参数和使用格式如下。
+ 由于交叉表是透视表的一种，其参数基本保持一致，不同之处在于crosstab函数中的index，columns，values填入的都是对应的从Dataframe中取出的某一列。
+ pandas.**crosstab**(index, columns, values=None,rownames=None, colnames=None,aggfunc=None, margins=False,dropna=True, normalize=False)
    + 参数名称——说明
    + index：接收string或list。表示行索引键。无默认。
    + columns：接收string或list。表示列索引键。无默认。
    + values：接收array。表示聚合数据。默认为None。
    + aggfunc：接收function。表示聚合函数。默认为None。
    + rownames：表示行分组键名。无默认。
    + colnames：表示列分组键名。无默认。
    + dropna：接收boolearn.表示是否删掉全为NaN的。默认为False.
    + margins：接收boolearn.默认为True。汇总(Total) 功能的开关，设为True后结果集中会出现名为"ALL" 的行和列。
    + normalize接收boolearn.表示是否对值进行标准化。默认为False.

