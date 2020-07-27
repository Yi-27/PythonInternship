# 导入包
import pandas as pd
import requests
import json
import os
import time

# 国内数据存储路径
filepath_cn = "./疫情数据/国内数据"
if not os.path.exists(filepath_cn): # 先判断这个文件夹是否已存在，已存在说明数据时最新的
    os.mkdir(filepath_cn) # 创建用最后更新时间来创建文件夹
filepath_fg = "./疫情数据/外国数据"

# 定义一个存储DataFrame的函数，包装了to_csv()方法
def df_to_csv(df=None, filepath=None, filename=None, encoding='GBK', retain_index=False):
    """
    params:
        df：DataFrame数据
        filepath：文件存储路径
        filename：文件名
        encoding：文件存储编码格式
        retain_index：是否保留DataFrame的索引
    """
    if not os.path.exists(filepath): # 先判断这个文件夹是否已存在，已存在说明数据时最新的
        os.mkdir(filepath) # 创建时，文件夹名里有时间来区分数据是否为最新
    df.to_csv(filepath + '/' + filename, encoding=encoding, index=retain_index) # 保存到文件夹中


# 爬取国内数据
def get_china_data(url, headers)
    # url0 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5
    res0 = requests.get(url, headers=headers) # 请求数据，使用第一种请求头
    data0 = json.loads(res0.json()['data']) # 因为data对应的值还是json字符串，还要转成Python字典


    china_data = {'name': data0['areaTree'][0]['name']} # 新建一个字典，并地区名添加进去
    china_data.update(data0['areaTree'][0]['total']) # 合并地区的数据，字典合并字典
    provinces_data =  [china_data] # 先创建省份数据列表，后续数据直接追加尽量，列表中的数据都是字典，先把全国的数据添进去

    # 各省份的数据都在 data['areaTree'][0]['children']这里，这是个列表，34个省级行政区
    provinces = data0['areaTree'][0]['children']
    # 遍历这个列表取出每个省的数据和每个地区的数据
    for i in provinces:
        # i['total'] 就是每个省的数据，里面的 showRate 和 showHeal 字段是不需要的 等同于这样data['areaTree'][0]['children'][0]['total']
        one_procevice_data = {'name': i['name']} # 将省份的名字先添加进字典
        one_procevice_data.update(i['total']) # 合并具体数据 i['total']是字典型的数据
        provinces_data.append(one_procevice_data) # 向省份列表追加每个省的数据

        # 获取省内的各市的数据 省内的数据一次就保存到单独的csv文件中
        districts = i['children']
        districts_data = [one_procevice_data]
        for j in districts:
            one_district_data = {'name': j['name']}
            one_district_data.update(j['total'])
            districts_data.append(one_district_data)

        # 将字典构成的列表直接转为DataFrame
        districts_df = pd.DataFrame(districts_data)
        del districts_df['showRate'] # 删除这多余的两列
        del districts_df['showHeal']

        # 保存这个省内各市的数据
        # districts_df.rename(columns=field_name_cn, inplace=True) # 把列名改为中文
        df_to_csv(districts_df, filepath_cn+'/各省具体数据', f'{i["name"]}.csv') # 存储各省具体数据
        # districts_df.to_csv(f"{filepath}/{i['name']}.csv", encoding='GBK', retain_index=False) # 保存到文件夹中 


    # 将字典构成的列表直接转为DataFrame
    provinces_df = pd.DataFrame(provinces_data)                        
    del provinces_df['showRate'] # 删除这多余的两列
    del provinces_df['showHeal']

    # 保存每个省的数据
    # provinces_df.rename(columns=field_name_cn, inplace=True) # 把列名改为中文
    df_to_csv(provinces_df, filepath_cn, '中国疫情数据.csv')
    # provinces_df.to_csv(f"{field_name_cn}/中国.csv", encoding='GBK', retain_index=False) # 保存到文件夹中 


# 爬取国内数据随时间变化
def get_china_time_data(url, headers):
    # url1 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_other' # 国内数据（随时间变化）
    res1 = requests.get(url, headers=headers)
    data1 = json.loads(res1.json()['data']) # 因为data对应的值还是json字符串，还要转成Python字典
    
    # 该部分可以直接转DataFrame然后存储数据
    df_to_csv(pd.DataFrame(data1['chinaDayList']), filepath_cn, '国内历史每日数据.csv')
    df_to_csv(pd.DataFrame(data1['chinaDayAddList']), filepath_cn, '国内历史每日新增数据.csv')
    df_to_csv(pd.DataFrame(data1['dailyNewAddHistory']), filepath_cn, '历史每日新增数据（湖北、国家、和非湖北）.csv')
    
    prov_compare = pd.DataFrame(data1['provinceCompare']) # 各省数据比较（现存确诊，新增确诊，死亡，治愈，连续0增天数
    prov_compare = pd.DataFrame(prov_compare.values.T, index=prov_compare.columns, columns=prov_compare.index) # 转置
    df_to_csv(prov_compare, filepath_cn, '各省今日数据比较.csv', retain_index=True) # 保留索引


# 外国数据（比率和排名）
def get_foreign_rate_rank(url, headers):
    # url2 = 'https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryWeekCompRank,FAutoContinentConfirmStatis,FAutoConfirmMillionRankList,FAutoHealDeadRateRankList'
    res2 = requests.get(url, headers=headers) # 这里用了headers2
    data2 = res2.json()['data']
    
    # 存储数据直接用 二次包装的to_csv方法 这里并没有修改列名为中文
    df_to_csv(pd.DataFrame(data2['FAutoConfirmMillionRankList']), filepath_fg, '外国每百万人确诊数.csv')
    df_to_csv(pd.DataFrame(data2['FAutoHealDeadRateRankList']['deadHead']), filepath_fg, '外国死亡率前10名.csv')
    df_to_csv(pd.DataFrame(data2['FAutoHealDeadRateRankList']['deadTail']), filepath_fg, '外国死亡率后10名.csv')
    df_to_csv(pd.DataFrame(data2['FAutoHealDeadRateRankList']['healHead']), filepath_fg, '外国治愈前10名.csv')
    df_to_csv(pd.DataFrame(data2['FAutoHealDeadRateRankList']['healTail']), filepath_fg, '外国治愈后10名.csv')


# 外国数据（排名和部分国家具体行政区数据）
def get_foreign_rank_region(url, headers)
    # url3 = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign' # 外国数据（排名）
    res3 = requests.get(url, headers=headers)
    data3 = json.loads(res3.json()['data']) # 因为data对应的值还是json字符串，还要转成Python字典
    
    # 存储数据
    df_to_csv(pd.DataFrame(data3['importStatis']['TopList']), filepath_cn, '国内输入病例前十省.csv')
    df_to_csv(pd.DataFrame(data3['countryAddConfirmRankList']), filepath_fg, '外国24小时新增确诊前10名.csv')
    
    # 存储部分国家的具体行政区数据数据  不过这里面就几个国家，同
    for i in data3['foreignList']: # i为国家的数据
        # 先判断这个国家有没有具体类似我国省这样的行政区的数据，即判断有没有 children 这个字段
        if 'children' in i: # 等同于 in i.keys()
            # 当存在时，可直接转换成DataFrame并存储
            df_to_csv(pd.DataFrame(i['children']), filepath_fg+'/部分国家具体行政区数据', f"{i['name']}-具体行政区数据.csv")


# 全球总体数据（随时间变化）
def get_foreign_time_data(url, headers):
    # url4 = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd"
    res4 = requests.get(url, headers=headers) # 这里用了headers2
    data4 = res4.json()['data']
    
    for i in data4['FAutoContinentStatis']: # 各大洲历史每七天的数据统计
        i.update(i.pop('statis')) # 把statis弹出再追加进去就可以直接转成DataFrame
    # 存储数据
    df_to_csv(pd.DataFrame(data4['FAutoContinentStatis']), filepath_fg, '各大洲历史每七天的数据统计.csv')
    
    global_daily_data = [] # 存储全球每日数据的列表
    for i in data4['FAutoGlobalDailyList']:
        day_data = {'date': i['date']}
        day_data.update(i['all']) # 就all字段中的每日数据追加进去
        global_daily_data.append(day_data)
    # 存储数据
    df_to_csv(pd.DataFrame(global_daily_data), filepath_fg, '全球历史每日数据.csv') # 转换成DataFrame，并存储到本地


# 外国数据（按国家或大洲查看）
def get_foreign_country_continent(url, headers):
    # url5 = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
    res5 = requests.get(url, headers=headers)
    data5 = res5.json()['data']
    
    # 存储
    df_to_csv(pd.DataFrame(data5), filepath_fg, '外国疫情数据（按国家或大洲查看）.csv')


# 外国部分国家历史每日数据（随时间变化）
def get_foreign_day_time_data(url, headers):
    # url6 = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country="

    # 这里就会用到data5，其中name字段就是国家名
    country_list = [c['name'] for c in data5] # 获取国家列表
    for i in country_list:  
        # 请求每个国家的数据，这里并不是所有的国家都有统计每日数据
        # 因此最终只能得到部分国家的数据
        res6 = requests.get(url+i, headers=headers) 
        data6 = res6.json()['data'] # 提取具体数据

        if data6: # 当该国有数据的时候就存储下来
            # 可直接存储数据
            df_to_csv(pd.DataFrame(data6), filepath_fg+'/部分国家历史每日数据', f'{i}.csv')
            print(f"{i} 每日数据爬取OK")

        # 这里由于频繁请求，怕被封因此睡眠1秒
        time.sleep(1)


# 国内具体省市的每日数据
def get_china_district_day_data(url, headers):
    # url7 = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="
    filepath_cn = "./疫情数据/国内数据"
    provinces = ['安徽', '澳门', '香港', '北京', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北', '河南', '黑龙江', '湖北', '湖南', '吉林', '江苏', '江西', '辽宁', '内蒙古', '宁夏', '青海', '山东', '山西', '陕西', '上海', '四川', '台湾', '天津', '西藏', '香港', '新疆', '云南', '浙江', '重庆']
    for p in provinces:
        res7 = requests.get(url+p, headers=headers)
        data7 = res7.json()['data'] # 提取具体数据

        df_to_csv(pd.DataFrame(data7), filepath_cn+'/各省每日数据', f'{p}.csv')
        print(f"{p} 每日数据爬取OK")

        # 这里由于频繁请求，怕被封因此睡眠1秒
        time.sleep(1)




if __name__ == '__main__':
	# 请求头 
	headers = {
	    'accept-encoding': 'gzip, deflate, br',
	    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	    'cookie': 'pgv_pvid=7838988661; ptcz=a749c13713fc703b48592a49922470ed1eda1bcc7b68d2cf5be6fa79c731b76d; pgv_pvi=9718182912; RK=vkrweAJtMM; o_cookie=763074310; pac_uid=1_763074310; luin=o0763074310; lskey=000100007d08c463d9cc757cc4c5ae2cf3732897a65bf7de58e88b9524158f61b02e143bcf6124869366ea7d; tvfe_boss_uuid=e1c916f5e5e6e6bd; _txjk_whl_uuid_aa5wayli=58f307f1d8264ccb8aeb92b2f6225b14',
	    'referer': 'https://news.qq.com/zt2020/page/feiyan.htm',
	    'sec-fetch-dest': 'script',
	    'sec-fetch-mode': 'no-cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
	}
	# 由于网址不同需要的请求头也不太一样，故设置两个请求头
	headers2 = {
	    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'Accept-Encoding': 'gzip, deflate, br',
	    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
	    'Cache-Control': 'max-age=0',
	    'Connection': 'keep-alive',
	    'Cookie': 'pgv_pvid=7838988661; ptcz=a749c13713fc703b48592a49922470ed1eda1bcc7b68d2cf5be6fa79c731b76d; pgv_pvi=9718182912; RK=vkrweAJtMM; o_cookie=763074310; pac_uid=1_763074310; luin=o0763074310; lskey=000100007d08c463d9cc757cc4c5ae2cf3732897a65bf7de58e88b9524158f61b02e143bcf6124869366ea7d; tvfe_boss_uuid=e1c916f5e5e6e6bd; _txjk_whl_uuid_aa5wayli=58f307f1d8264ccb8aeb92b2f6225b14; uin=o0763074310; skey=@xEkmEQkwn; qqmusic_uin=; qqmusic_key=; qqmusic_fromtag=; pgv_info=ssid=s1515695283',
	    'Host': 'api.inews.qq.com',
	    'Sec-Fetch-Dest': 'document',
	    'Sec-Fetch-Mode': 'navigate',
	    'Sec-Fetch-Site': 'none',
	    'Sec-Fetch-User': '?1',
	    'Upgrade-Insecure-Requests': '1',
	    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
	}


	# 国内数据
	url0 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
	 # 国内数据（随时间变化）
	url1 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_other"
	# 外国数据（比率和排名）
	url2 = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoCountryWeekCompRank,FAutoContinentConfirmStatis,FAutoConfirmMillionRankList,FAutoHealDeadRateRankList"
	# 外国数据（排名）
	url3 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"
	# 全球总体数据（随时间变化）
	url4 = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoGlobalStatis,FAutoContinentStatis,FAutoGlobalDailyList,FAutoCountryConfirmAdd"
	# 外国数据（按国家或大洲查看）
	url5 = "https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist"
	# 外国部分国家历史每日数据（随时间变化）
	url6 = "https://api.inews.qq.com/newsqa/v1/automation/foreign/daily/list?country="
	# 国内具体省市每日数据
	url7 = "https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province="


	# 执行爬虫
	get_china_data(url0, headers)
	get_china_time_data(url1, headers)
	get_foreign_rate_rank(url2, headers2)
	get_foreign_rank_region(url3, headers)
	get_foreign_time_data(url4, headers2)
	get_foreign_country_continent(url5, headers)
	get_foreign_day_time_data(url6, headers2)
	get_china_district_day_data(url7, headers2)

