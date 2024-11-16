def merge_dicts(dict1, dict2):
    tmp = dict1.copy()
    tmp.update(dict2)
    return tmp

dic1 = {1:'lan',2:'hoa'}
dic2 = {'sv1':10,'sv2':9}
res = merge_dicts(dic1, dic2)
print(res)