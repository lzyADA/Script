import asyncio
import requests
import time
import aiohttp
import aiomultiprocess
import redis
import pymysql
import pypinyin

#
# async def execute(x):
#     print("num",x)
#     return x
#
# cor = execute(1)
# print("coroutline",cor)
# print("after calling execute")
#
# loop = asyncio.get_event_loop()
# task = loop.create_task(cor)
# print("task",task)
# loop.run_until_complete(task)
# print("task2",task)
# print("after call loop")
# 定义task的另一种方式
"""
async def execute(x):
    print("num",x)
    return x


cor = execute(1)
print("cor",cor)
print("after call execute")

task = asyncio.ensure_future(cor)
print(task)
loop = asyncio.get_event_loop()

loop.run_until_complete(task)
print(task)
print("after call loop")
"""
# 为某个task绑定回调
"""
async def request():
    url = "http://www.baidu.com"
    resp = requests.get(url)
    return resp

# def callback(task):
#     print("resp",task.result())

coro = request()

task = asyncio.ensure_future(coro)

# task.add_done_callback(callback)

print("task1",task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print("task2",task.result())
"""
"""

#多任务协程

async def request():
    url = "http://www.baidu.com"
    resp = requests.get(url)
    return resp


tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print("tasks",tasks)
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

for task in tasks:
    print("task result",task.result())

a = [print(_) for _ in range(5)]
print(f"a的值{a}")"""

"""start = time.time()

async def get(url):
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    result= await resp.text()
    session.close()
    return result


async def request():
    url= "http://127.0.0.1:5000"
    print("waiting url",url)
    resp = await get(url)
    print("git resp from ",url,"result",resp)

tasks =[asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()

print("cost time",end-start)
"""

# -*- coding: utf-8 -*-
import redis
import time
timee = time.strftime("%Y-%m-%d",time.localtime())

class City_Search:
    def __init__(self):
        self.timee = time.strftime("%Y-%m-%d", time.localtime())
        self.mysql_data = Myqsl().search_data()
        self.citys = {
                    "zibo":"10",
                    "zhumadian": "10",
                    "zhuhai": "9",
                    "chongqing": "9",
                    "zhongshan": "9",
                    "zhengzhou": "9",
                    "changsha": "8",
                    "yangzhou": "8",
                    "yancheng": "8",
                    "suqian": "8",
                    "xinxiang": "7",
                    "xian": "7",
                    "wuxi": "7",
                    "tianjin": "7",
                    "suzhou": "6",
                    "shijiazhuang": "6",
                    "shenyang": "6",
                    "shenzhen": "6",
                    "shaoxing": "5",
                    "shanghai": "5",
                    "sanya": "5",
                    "quanzhou": "5",
                    "nantong": "4",
                    "nanning": "4",
                    "nanjing": "4",
                    "nanchang": "4",
                    "luoyang": "11",
                    "lianyungang": "11",
                    "lanzhou": "11",
                    "kunming": "11",
                    "jiaxing": "3",
                    "jinan": "3",
                    "huaian": "3",
                    "hefei": "3",
                    "haikou": "2",
                    "haerbin": "2",
                    "foshan": "2",
                    "dongguan": "2",
                    "dalian": "1",
                    "chengdu": "1",
                    "changzhou": "1",
                    "beijing": "1",
                    }
        self.city_select = [
            'anjukenew-sell_fingerprint',
            'nanjing-anjukenew-sell_seed'
        ]
        self.city_statu = {1:'例行完成',3:'等待例行',2:'正在例行'}
        self.r = redis.StrictRedis(
            host='',
            port=,
            db=0,
            password='',
            decode_responses=True
        )

    # ## 打印输出表格
    def print_city(self,data,num):
        for city,datas in data.items():

            print('-' * 150)
            print(
                f' \033[1;31;0m{city}\033[0m',' '*(12-len(city)),'|',
                f' \033[1;31;0m{self.city_statu[num]}\033[0m', ' ' * (5 - len(self.city_statu[num])), '|',
                f' \033[1;31;0m{datas[0]}\033[0m', ' ' * (7 - len(f"{datas[0]}")), '|',
                f' \033[1;31;0m{datas[1]}\033[0m', ' ' * (7 - len(f"{datas[1]}")), '|',
                f' \033[1;31;0m{datas[2]}\033[0m', ' ' * (5 - len(f"{datas[2]}")), '|',
                # f' \033[1;31;0m{save_data}\033[om',' ' * (7 - len(f"{save_data}")),'|'
            )




    def citysearch(self):
        print('正在查询。。。。。')
        exit_citys = {i:[self.r.hlen(f"{i}-anjukenew-sell_fingerprint"),0,self.citys[i]] for i in self.citys.keys() if f"{i}-anjukenew-sell_fingerprint" in self.r.keys() and f"{i}-anjukenew-sell_seed" not in self.r.keys()}

        run_citys = {i:[self.r.hlen(f"{i}-anjukenew-sell_fingerprint"),self.r.llen(f"{i}-anjukenew-sell_seed"),self.citys[i]] for i in self.citys.keys() if f"{i}-anjukenew-sell_seed" in self.r.keys()}
        wait_citys = {i:[0,0,self.citys[i]] for i in self.citys.keys() if (i not in exit_citys.keys()) and (i not in run_citys.keys())}
        print('-' * 150)
        # print(' ' * 4, f'\033[1;37;0m {self.timee} Ajukenew城市报告 {len(exit_citys)}(end)/{len(run_citys)}(ing)/{len(wait_citys)}(wait)\033[0m')
        print(' '*4,f'\033[1;37;0m {self.timee} Ajukenew城市报告 {len(exit_citys)}(end)/{len(run_citys)}(ing)/{len(wait_citys)}(wait)\033[0m')
        print('-' * 150)
        print(f'\033[7;37;0m  cityname     \033[0m|\033[7;37;0m   city状态  \033[0m|\033[7;37;0m   目前总量  \033[0m|\033[7;37;0m 种子剩余   \033[0m|\033[7;37;0m 例行日期   \033[0m|\033[7;37;0m 以存储数据 \033[0m')
        self.print_city(exit_citys,1)
        self.print_city(run_citys,2)
        self.print_city(wait_citys,3)
        print("-"*150)
        save_data = self.mysql_data
        for city,data_count in save_data.items():
            if city == '':
                print(f'数据抓空  \033[1;31;0m{data_count}\033[0m')
                continue
            city = self.header_pinyin(city)
            for ex_city, datas in exit_citys.items():
                if ex_city == city:
                    print("-"*150)
                    # print(ex_city,city)
                    print(f'抓取城市    \033[1;31;0m{ex_city}\033[0m',   ' '*(12-len(city)), '|',
                          f'抓取数量    \033[1;31;0m{datas[0]}\033[0m',  ' '*(7-len(str(datas[0]))), '|',
                          f'库中数量    \033[1;31;0m{data_count}\033[0m',' '*(5-len(str(data_count))) )
                else:
                    pass
        # print(f'\033[036m城市数据抓取完成有:{",".join(exit_citys.keys())}  共城市:{len(exit_citys.keys())}\033[0m')





    def header_pinyin(self,data):
        s = ''
        for i in pypinyin.pinyin(data, style=pypinyin.NORMAL):
            s += ''.join(i)
        return s


class Myqsl:
    def __init__(self):
        self.host = ''
        self.port = 
        self.db = ''
        self.user =  ''
        self.passwd = ''
        self.charset = ''
        try:
            self.sqldb = pymysql.connect(host=self.host,port=self.port,db=self.db,user=self.user,passwd=self.passwd,charset=self.charset)
            self.mysqlcro = self.sqldb.cursor()
        except Exception as  e:
            print(f"链接失败:{e}")
            # raise (f"链接失败:{e}")

    def search_data(self):
        sql = """select house_city,count(1) from house_anjukesell_spider3 group by house_city"""
        self.mysqlcro.execute(sql)
        city_data = self.mysqlcro.fetchall()
        pa= {i[0]:i[1] for i in city_data }
        return pa


if __name__=="__main__":
    s=City_Search().citysearch()
    # a = Myqsl().search_data()


