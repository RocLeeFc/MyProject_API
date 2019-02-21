# -*-coding:utf-8-*-

"""
@Time       :2019/2/1917:12
@Author     :pengpeng
@Email      :743463927@qq.com
@File       :context.py
@Software   :PyCharm
@Function   :
"""

# s 是目标字符串
# d 是替换的内容
# 找到目标字符串里面的标识符key，去d 里面拿到替换的值
# 替换到s 里面去，然后再返回

import re
from common.config import ReadConfig

config = ReadConfig()


class Context:
    admin_user = config.get('data', 'admin_user')
    admin_pwd = config.get('data', 'admin_pwd')
    loan_member_id = config.get('data', 'loan_member_id')
    normal_user = config.get('data', 'normal_user')
    normal_pwd = config.get('data', 'normal_pwd')
    normal_member_id = config.get('data', 'normal_member_id')

def replace(s):
    p = "\$\{(.*?)}"
    while re.search(p, s):
        m = re.search(p, s)
        key = m.group(1)
        if hasattr(Context, key):
            value = getattr(Context, key)
            s = re.sub(p, value, s, count=1)
        else:
            return None
    return s
