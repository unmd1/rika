import re
import string
from collections import deque
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

# Test the function
outputs = []
subdomain = "c.mio.example.com"
outputs.extend(extend_subdomain(subdomain))
# Display results
for item in outputs:
    print(item)



















