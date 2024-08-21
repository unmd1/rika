import requests

cookies = {
    'XSRF-TOKEN': '8349242e-c0a1-46ee-8582-7d0aae2b705e',
    'csrf-state': '""',
    'csrf-state-legacy': '""',
    'cognito-fl': '"W10="',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa;q=0.8,fa-IR;q=0.7,ar;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'XSRF-TOKEN=8349242e-c0a1-46ee-8582-7d0aae2b705e; csrf-state=""; csrf-state-legacy=""; cognito-fl="W10="',
    'origin': 'https://loan-monitor.auth.eu-west-1.amazoncognito.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://loan-monitor.auth.eu-west-1.amazoncognito.com/login?redirect_uri=https%3A%2F%2Fmonitor.loan.oaknorth.co.uk%2F&response_type=token&client_id=6dflioai9fuvjtcolmojaceigs&identity_provider=COGNITO&scope=&state=SHQiK6zKHSKxcqQ2FQ9eXnetdMGl6s1R',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
}

params = {
    'redirect_uri': 'https://monitor.loan.oaknorth.co.uk/',
    'response_type': 'token',
    'client_id': '6dflioai9fuvjtcolmojaceigs',
    'identity_provider': 'COGNITO',
    'scope': '',
    'state': 'SHQiK6zKHSKxcqQ2FQ9eXnetdMGl6s1R',
}

data = {
    '_csrf': '8349242e-c0a1-46ee-8582-7d0aae2b705e',
    'username': 'admin',
    'password': 'admin',
    'cognitoAsfData': 'eyJwYXlsb2FkIjoie1wiY29udGV4dERhdGFcIjp7XCJVc2VyQWdlbnRcIjpcIk1vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTZfNiBsaWtlIE1hYyBPUyBYKSBBcHBsZVdlYktpdC82MDUuMS4xNSAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vMTYuNiBNb2JpbGUvMTVFMTQ4IFNhZmFyaS82MDQuMVwiLFwiRGV2aWNlSWRcIjpcIjhsMW40ejYxNm5xaHJpZnZscHhyOjE3MjQyMTQ1MDA3MTVcIixcIkRldmljZUxhbmd1YWdlXCI6XCJlbi1VU1wiLFwiRGV2aWNlRmluZ2VycHJpbnRcIjpcIk1vemlsbGEvNS4wIChpUGhvbmU7IENQVSBpUGhvbmUgT1MgMTZfNiBsaWtlIE1hYyBPUyBYKSBBcHBsZVdlYktpdC82MDUuMS4xNSAoS0hUTUwsIGxpa2UgR2Vja28pIFZlcnNpb24vMTYuNiBNb2JpbGUvMTVFMTQ4IFNhZmFyaS82MDQuMWVuLVVTXCIsXCJEZXZpY2VQbGF0Zm9ybVwiOlwiV2luMzJcIixcIkNsaWVudFRpbWV6b25lXCI6XCIuNTozMFwifSxcInVzZXJuYW1lXCI6XCJtaW93JTI2JTIzeDIyJTNCXCIsXCJ1c2VyUG9vbElkXCI6XCJcIixcInRpbWVzdGFtcFwiOlwiMTcyNDIxNDUyMDI1NlwifSIsInNpZ25hdHVyZSI6IlB2TjVXMzg1aXlsOTV1cnVpMGdMUXd2MGpmcHE2d0NQWEZZdkh1SDN4Vk09IiwidmVyc2lvbiI6IkpTMjAxNzExMTUifQ==',
}

response = requests.post(
    'https://loan-monitor.auth.eu-west-1.amazoncognito.com/login',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
print(response.text)