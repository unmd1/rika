import requests
import json
import time
import math
import os
import re
import json
class recon:
    def __init__(self,s="",proxy="",ua="",prjID=""):



        # Session
        self.s=s
        if type(s) == str:
            self.s=requests.session()
        self.s.cookies.clear()


        # Proxy
        self.proxy = {
            "proxy":proxy,
            "start":""
            }
        
        #uSER aGENT
        if ua == "":
            self.ua = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
            }
        else:
            self.ua = ua




        # Prj_data
        if prjID != "":
            self.prjname = self.mysql_show("SELECT * FROM `project` WHERE id='"+ prjID +"'")[0]["name"]
            scopes = self.mysql_show("SELECT * FROM `scope` WHERE prj='"+ self.prjname +"'")
            self.scopes = []
            for scope in scopes:
                self.scopes.append(scope)

    

#####################################/////////////############################################
#####################################-- Request --############################################
#####################################/////////////############################################




####################
### Post Section ###


    def original_s_post(self,url,data,files,typereq =""):
        s=self.s
        sleep=5
        while True:
            try:

                if self.proxy['proxy'] == "":
                    try:
                        if files != []:
                            if typereq == "":
                                return s.post(url,data = data,headers = self.ua,files=files)
                            else:
                                return s.request(typereq,url,data = data,headers = self.ua,files=files)
                        else:
                            if typereq == "":
                                return s.post(url,data = data,headers = self.ua)
                            else:
                                return s.request(typereq,url,data = data,headers = self.ua)
                    except:
                        print(s)
                        if files != []:
                            if typereq == "":
                                return s.post(url,data = data,headers = self.ua,files=files)
                            else:
                                return s.request(typereq,url,data = data,headers = self.ua,files=files)
                        else:
                            if typereq == "":
                                return s.post(url,data = data,headers = self.ua)
                            else:
                                return s.request(typereq,url,data = data,headers = self.ua)
                else:
                    if files != []:
                        if typereq == "":
                            return s.post(url,data = data,headers = self.ua,files=files)
                        else:
                            return s.request(typereq,url,data = data,headers = self.ua,files=files)
                    else:
                        print("proxy")
                        return s.post(url,data = data,proxies=self.proxy['proxy'],headers = self.ua)
            except Exception as e:
                print("Conncetion Error Sleep For " + str(sleep) + " Second")
                print(str(e))
                print(s)
                time.sleep(sleep)
                
                sleep=sleep*2
                pass


    def s_post_err429(self,url,data,files,typereq = ""):
        # self.proxy_changer()
        r = self.original_s_post(url,data = data,files=files,typereq = typereq)
        return r


    def s_post(self,url,data,json_checker = False,status_200_checker = False,dkp="",dkpc="",job=0,des="",files=[],typereq = ""):
        time.sleep(0.6)
        r = self.original_s_post(url,data = data,files=files,typereq = typereq)
        sleep_time = 8

        while r.status_code == 429 or "خطای ۵۰۴" in r.text:
            sleep_time = sleep_time * 2
            # print(str(sleep_time))
            # print(r.text)
            # print(str(r.status_code))
            # print("4")
            time.sleep(sleep_time)
            r = self.s_post_err429(url,data,files,typereq = typereq)


        while status_200_checker == True and r.status_code != 200 and r.status_code != 429:
            sleep_time *= 2
            # print(str(sleep_time))
            # print(r.text)
            # print(str(r.status_code))
            # print("2")
            time.sleep(sleep_time)
            r = self.s_post_err429(url,data,files)

        while json_checker == True:

            try:
                json.loads(r.text)
                json_checker = False
                # print(r.text)
                # print(str(r.status_code))
                # print("t4")
                break
            except:

                sleep_time *= 2
                print(str(sleep_time))
                print(r.text)
                print(str(r.status_code))
                time.sleep(sleep_time)
                r = self.s_post_err429(url,data,files)
                
        return r     





###################
### Get Section ###


    def original_s_get(self,url,params):
        s=self.s
        sleep=5
        while True:
            try:
                if self.proxy['proxy'] == "":
                    return s.get(url,headers = self.ua,params=params)
                else:
                    return s.get(url,proxies=self.proxy['proxy'],headers = self.ua,params=params)

            except:
                print("Conncetion Error Sleep For " + str(sleep) + " Second")
                time.sleep(sleep)
                sleep=sleep*2
                pass


    def s_get_err429(self,url,params):

        self.s = self.loginu()
        r = self.original_s_get(url,params)
        return r


    def s_get(self,url,params={}):
        time.sleep(0.6)
        r = self.original_s_get(url,params)
        sleep_time = 8
       
        while r.status_code == 429:
            sleep_time = sleep_time * 2
            time.sleep(sleep_time)
            r = self.s_get_err429(url,params)

        return r   























#####################################/////////////############################################
#####################################-- MYSQL --############################################
#####################################/////////////############################################





    def mysql_main(self,query,page=1,dbname="psmglass_hunt",type="show"):
        data={
            "type":type,
            "sql":query,
            "dbname":dbname,
            "page":page
        }
        result = ""
        while (True):
            try:
                result = self.s_post("https://psmglass.com/dbctrl.php",data=data).text
                # print(data)
                break
            except:
                print("Error")

        return result


    def mysql_show(self,query,dbname="psmglass_hunt"):
        result = self.mysql_main(query,dbname=dbname)
        # print(result)
        count_rows = int(result.split("/pgc/")[0])

        result = result.split("/pgc/")[1]
        sql_data = result.split("/n/")[:-1]
        sql_data_list = []
        for i in range(1,math.ceil(count_rows/5000)+1):

            result = self.mysql_main(query,page=i,dbname=dbname)
            result = result.split("/pgc/")[1]
            sql_data = result.split("/n/")[:-1]
            # sql_data_list = []
            for rows in sql_data:
                sql_data_dic = {}
                for cloumns in rows.split("/s/")[:-1]:
                    spliter_data = cloumns.split("/d/")
                    sql_data_dic.update({spliter_data[0]:spliter_data[1]})
                sql_data_list.append(sql_data_dic)
            # print(str(len(sql_data_list)))
            # print(sql_data_list)
        return sql_data_list


    def mysql_query(self,query,dbname="psmglass_hunt"):
        result = self.mysql_main(query,dbname=dbname,type="query")

        if result != "":
            return True
        else:
            return False
        

    def mysql_insert(self,keys,values,table="hunt",dbname="psmglass_hunt",):
        keys_str = ", ".join(keys)
        # if isinstance(values[0], list): 
            #########agar list bod bayad yejor dg sql besaze###############################################
        values_str = "\", \"".join(values)
        query = "INSERT INTO " + table + " (" + keys_str + ") VALUES (\"" + values_str.strip() + "\")"
        # print(query)
        if self.mysql_query(query):
            # print("insert Successfully!")
            pass
        else:
            # print("insert Failed!")
            return "false"
        return "true"


    def mysql_insert_to_many(self,keys,values,table="hunt",dbname="psmglass_hunt"):
        keys_str = ", ".join(keys)
        # if isinstance(values[0], list): 
            #########agar list bod bayad yejor dg sql besaze###############################################
        values_list=[]
        for value in values:
            values_list.append("(\"" + "\", \"".join(value) + "\")") 
        # print(values_list)
        
        query = "INSERT INTO " + table + " (" + keys_str + ") VALUES " + ",".join(values_list) + ""
        with open("query.txt","w",encoding="utf-8") as f:
            f.write(query)
        # print(query)
        if self.mysql_query(query):
            # print("insert Successfully!")
            pass
        else:
            # print("insert Failed!")
            pass


    def value_directory(self):
        return ['directory','url','Furl','statusCode','size','scopeId','tag','comment','activity','status','created_by','prj']
    
    def value_flog(self):
        return ['url','keywords','statusCode','size','scopeId','tag','comment','activity','status','created_by','prj']
    
    def value_parameters(self):
        return ['parameter','value','url','payload','Furl','reflect','statusCode','size','scopeId','tag','comment','activity','status','created_by','prj']
    
    def value_scope(self):
        return ['address','comment','activity','status','created_by','prj']
    
    def value_subs(self):
        return ['address','scopeId','uniq','comment','activity','status','created_by','prj','result']
    
    def value_urls(self):
        return ['url','statusCode','size','scopeId','tag','comment','activity','status','created_by','prj']
    
    def value_wlog(self):
        return ['url','req_header','res_header','res_cockie','req_cockie','past_reqId','type','response','domain','tag','comment','activity','status','created_by','prj']
    
    def value_wordlist(self):
        return ['keyword','WLname','bestfor','testOn','tag','comment','activity','status','created_by','prj']
    




    def insert_directory(self,directory="",url="",Furl="",statusCode="",size="",scopeId="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_directory()
        values=[directory,url,Furl,statusCode,size,scopeId,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="directory")

    
    def insert_flog(self,url="",keywords="",statusCode="",size="",scopeId="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_flog()
        values=[url,keywords,statusCode,size,scopeId,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="flog")
    
    def insert_parameters(self,parameter="",value="",url="",payload="",Furl="",reflect="",statusCode="",size="",scopeId="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_parameters()
        values=[parameter,value,url,payload,Furl,reflect,statusCode,size,scopeId,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="parameters")
    
    def insert_scope(self,address="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_scope()
        values=[address,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="scope")
    
    def insert_subs(self,address="",scopeId="",uniq="",comment="",activity="",status="",created_by="",prj="",result=""):
        if not uniq=="":
            keys = self.value_subs()
            values=[address,scopeId,uniq,comment,activity,status,created_by,prj,result]
            self.mysql_insert(keys,values,table="subs")
        else:
            print("Uniq must be not empty")
    
    def insert_urls(self,url="",statusCode="",size="",scopeId="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_urls()
        values=[url,statusCode,size,scopeId,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="urls")
    
    def insert_wlog(self,url="",req_header="",res_header="",res_cockie="",req_cockie="",past_reqId="",type="",response="",domain="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_wlog()
        values=[url,req_header,res_header,res_cockie,req_cockie,past_reqId,type,response,domain,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="wlog")
    
    def insert_wordlist(self,keyword="",WLname="",bestfor="",testOn="",tag="",comment="",activity="",status="",created_by="",prj=""):
        keys = self.value_wordlist()
        values=[keyword,WLname,bestfor,testOn,tag,comment,activity,status,created_by,prj]
        self.mysql_insert(keys,values,table="wordlist")




#####################################/////////////############################################
#####################################-- Commands --############################################
#####################################/////////////############################################

###################
###### Extra ######
###################




    def geturltxt_old(self,txt,domain):
        URLs=[]
        if domain["address"] in txt:
            indexes = [ (i.start(), i.end()) for i in re.finditer(domain["address"], txt)]
            for index in indexes:
                try:
                    start = txt[0:index[0]].rindex(" ")+1
                except:
                    start = 0
                end = index[1]
                URLs.append(txt[start:end])
        return URLs
    

    def geturltxt(self,txt,domain):
        txt = txt.replace("\\n"," ")
        pattern = '[^\"\s\'\*]+.'+domain["address"]
        URLs = list(set(result.lower().strip() for result in re.findall(pattern,txt)))
        return URLs



    def run_command(self,command,scope):
        with os.popen(command) as pse:
            for line in pse:
                URLs=self.geturltxt_old(line,scope) 
                for URL in URLs:
                    self.insert_subs(URL,scope["id"],URL+"subfinder","test","justFind","rika","subfinder",self.prjname)
                    print(URL)


    def run_command_json(self,command):
        print(command)
        with os.popen(command) as pse:
            for line in pse:
                try:
                    js_res = json.loads(line)
                    scope = js_res["input"]
                    self.mysql_query("UPDATE `subs` SET `result`='"+ line +"',`activity`='httpx' WHERE address = '" + scope + "'")
                except:
                    print("__________|||||||__________")
                    print(line)
                    
    
    def run_command2(self,command):
        print(command)
        with os.popen(command) as pse:
            for line in pse:
                pass
    
    def run_command_return(self,command):
        lines=[]
        with os.popen(command) as pse:
            for line in pse:
                lines.append(line)
        return lines

###################
###### Main  ######
###################


    def forbidden_solve(self,url):
        outputs = self.run_command_return("./bypass-403.sh " + url)
        for output in outputs:
            if "200," in output:
                print(output)
            

    def subfinder(self,scope,silent=True):
        params = []
        if silent : params.append("-silent")
        if not params == [] : paramtxt = " ".join(params)
        self.run_command("subfinder -d "+ scope["address"]  + " " + paramtxt ,scope)


    def crtsh(self,scope,silent=True):
        crt_result  = self.s_get("https://crt.sh/?q="+ scope["address"] +"&output=json")
        # print(crt_result.text)
        URLs=self.geturltxt(crt_result.text,scope)
        for URL in URLs:
            for URL_0 in URL.split(" "):
                if str(URL_0).startswith("."):
                    URL_0 = URL_0[1:]
                self.insert_subs(URL_0,scope["id"],URL_0+"crt.sh","test","justFind","rika","crt.sh",self.prjname)
                print(URL_0)


