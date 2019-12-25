import yaml

data = {"search_data": {
    "search_test_002": {"expect": {'value': '你好'}, 'value': '你好'},
    "search_test_001": {'expect': [4, 5, 6], 'value': 456}}}

with open("./write_yam", "a", encoding="utf-8") as f:
    # 写yaml文件
    yaml.safe_dump(data, f, encoding="utf-8", allow_unicode=True)

"""
Search_Data:
  search_test_002:
    except:
         value:你好
    value:你好
  search_test_001:
    expect:
        - 4
        - 5
        - 6
    value: 456
"""
