import recon
# import os
# import tldextract
# import re
# import requests




# def geturltxt(txt,domain):
#     URLs=[]
#     if domain in txt:
#         indexes = [ (i.start(), i.end()) for i in re.finditer(domain, txt)]
#         for index in indexes:
#             start=0
#             try:
#                 if start == 0 : start = txt[0:index[0]].rindex('"')+1
#             except:
#                 start = 0
#             end = index[1]
#             URLs.append(txt[start:end])
#     return URLs


# print(geturltxt('',''))


rc = recon.recon(prjID="1")
# for scope in rc.scopes:
#     print(scope)
#     rc.subfinder(scope)
#     rc.crtsh(scope)
src_directory = r"H:\HUNT\tikkie\httpx"
rc.run_command_json("python h:/HUNT/rika/stdout.py SELECT_`address`_FROM_`subs` address | httpx -silent -j -irrb -srd " + src_directory)


