# czipdata
纯真IP数据库镜像及mysql同步更新 for Python

# 功能
1. 通过Python实现纯真IP数据库的镜像更新，数据库在data文件夹下；
2. 将数据文件解析为txt格式；
3. 将数据文件全量导入mysql中；
4. 将mysql数据库中的IP数据库内的地址细分为省市区；
5. 生成sql文件。

# 数据文件
文件 | 内容
---|:---
correct.json|地址细分纠错文件
czipdata_version.bin|本地数据文件版本记录
czipdata.dat|纯真IP数据文件
czipdata.txt|纯真IP数据TXT文件

# TODO
1. 将数据文件导入sqlite3数据库db文件中；
2. 实现数据库的增量更新。