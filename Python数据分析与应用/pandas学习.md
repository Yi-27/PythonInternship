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