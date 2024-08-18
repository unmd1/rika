import recon
import dict
import re
import string
import sys
from collections import deque

#############functions#################




def extend_subdomain(subdomain):
    # Regex to find a pattern like 'a100' (single alphabet followed by digits)
    match = re.search(r'\b([a-zA-Z])(\d*)\b', subdomain)
    
    if match:
        # List to hold all possible subdomains
        results = []
        
        # Capture the single alphabet and the digits
        alphabet = match.group(1)
        digits = match.group(2)
        
        # The position of the match in the subdomain
        start_pos = match.start()
        end_pos = match.end()
        
        # Replace the single alphabet with all possible alphabets
        for char in string.ascii_lowercase:  # 'a' to 'z'
            new_subdomain = subdomain[:start_pos] + char + digits + subdomain[end_pos:]
            results.extend(replace_digits_non_recursive(new_subdomain))
            
        return results
    else:
        # If no such pattern is found, return the original subdomain
        return replace_digits_non_recursive(subdomain)








def replace_digits_non_recursive(input_string_0):
    input_string = ".".join(input_string_0.split(".")[:-2])
    digit_positions = [m.start() for m in re.finditer(r'\d', input_string)]
    if len(digit_positions) > 3 :
        digit_positions = digit_positions[-3:]

    if not digit_positions:
        return [input_string_0]
    
    # صف برای نگهداری رشته‌ها
    queue = deque([input_string_0])
    
    # لیستی برای ذخیره نتایج
    results = []
    
    # پردازش هر موقعیت عدد
    for pos in digit_positions:
        # تعداد فعلی رشته‌ها در صف
        current_length = len(queue)
        
        # تکرار روی همه رشته‌های موجود در صف
        for _ in range(current_length):
            current_string = queue.popleft()
            
            # جایگزینی عدد با همه اعداد ممکن (0 تا 9)
            for i in range(10):
                new_string = current_string[:pos] + str(i) + current_string[pos+1:]
                queue.append(new_string)
    
    # تبدیل صف به لیست و برگرداندن آن
    results.extend(queue)
    
    return results






















def sub_smart(subs):

    dik = dict.dic_to_list(subs,"address")
    final_subs = {}
    values=[]
    outputs=[]
    insert_to_wordlist = False
    for sub in subs:
        sub_org = sub["address"].replace("www.","").lstrip('.')

        if "." in sub_org and len(sub_org.split("."))>3:
            sub_dots = sub_org.split(".")

            for i in range(0,len(sub_dots)-2):

                sub_dots_temp = sub_org.split(".")


                sub_dash = sub_dots_temp[i].split("-")

                for i2 in range(0,len(sub_dash)):

                    sub_dash_temp = sub_org.split(".")[i].split("-")

                    value= [sub_dash_temp[i2],"subdomain_duplicate.py",rc.prjname,"","","","","","subdomain_duplicate",rc.prjname]
                    if not value in values and not "www" == value :
                        values.append(value)

                    sub_dash_temp[i2]="*"
                    sub_dots_temp[i]="-".join(sub_dash_temp)
                    final = ".".join(sub_dots_temp)


                    if not final in final_subs:
                        final_subs.update({final:1})
                    else:
                        final_subs[final]+=1


    if insert_to_wordlist:
        rc.mysql_insert_to_many(rc.value_wordlist(),values,"wordlist")


    for final_sub in final_subs:
        if final_subs[final_sub] > hardness:
            for values_2 in values:
                outputs.append(final_sub.replace("*",values_2[0]))
    outputs = list(set(outputs) - set(dik))
    return outputs


















#############functions#################













hardness = 3
outputs=[]
rc=recon.recon(prjID="1")
subs = rc.mysql_show("SELECT `address` from `subs`")

startfrom = sys.argv[1]
limit = sys.argv[2]

outputs = sub_smart(subs)
for sub in subs:
    address = sub["address"]
    new_outputs = extend_subdomain(address)
    new_outputs.remove(address)
    outputs.extend(new_outputs)

outputs = list(set(outputs))

for output in outputs[int(startfrom):int(limit)]:
    print(output)