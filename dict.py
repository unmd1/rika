import json
from os import path
def dic_updater(dictoanry,Index,data):
    # try:
    #     dictoanry[Index]
    # except:
    #     dictoanry.update({Index:data})
    if not Index in dictoanry:
        dictoanry.update({Index:data})
    return dictoanry
    
def dict_change_key(dict,key):
    out = {}
    for data in dict:
        if dict[key] in out:
            out[dict[key]].append(data)
        else:
            out.update({dict[key]:[data]})
def list_to_dic(dict,key):
    out = {}
    for data in dict:
        if data[key] in out:
            out[data[key]].append(data)
        else:
            out.update({data[key]:[data]})
    return out

def save_dataset(data_set,name):
    with open("dataset\\" + name + '.json', 'w',encoding="utf-8") as f:
        json.dump(data_set, f, ensure_ascii=False)

def find_dataset(name):
    if "\\" in name:
        address=name
    else:
        address= "dataset\\" + name + '.json'
    if path.exists(address):
        sample_data = open(address,"r",encoding="utf-8")
        return json.load(sample_data)
    return False

def unique(dic):
    return list(dict.fromkeys(dic))

def dic_to_list(dic,key):
    out_list = []
    for dic_v in dic:
        out_list.append(dic_v[key].replace("\n","").replace("\\n",""))
    return out_list

def is_list_in_string(list_1,str_1):
    for it in list_1:
        if it in str_1:
            return True
    
    return False