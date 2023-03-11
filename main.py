#https://vk.com/video-91354503_171377712

import requests
import bs4
import tinytag

#https://vkvd216.mycdn.me/
# expires/1678823510713/clientType/13/srcIp/209.166.122.137/type/2/
# mid/4461412165842/id/3038823058130/
# ms/45.136.22.205/zs/43/srcAg/GECKO/urls/45.136.20.146/ct/29/
# sig/4fr3mcyhnrw/subs/y/asubs/y/ondemand/CNKV4L-4WCgDMAJiHQgCEhkKEQoKCIDI5IABEMTYAhACGPcXYgQoEFoAePcXxqBxM1mTcbw/
# fn/s24.a2.chk


default_params = {
    'expires': 1678823510713,
    'clientType': 13,
    'srcIp': '209.166.122.137',
    'type': 2,
    'mid': 4461412165842,
    'id': 3038823058130,
    'ms': '45.136.22.205',
    'zs': 43,
    'srcAg': 'GECKO',
    'urls': '45.136.20.146',
    'ct': 29,
    'sig': '4fr3mcyhnrw',
    'subs': 'n',
    'asubs': 'n',
    'ondemand': 'CNKV4L-4WCgCMAJiJwgBEiMKDwoICKDMhSMQ4F0QAhj3F1oQCgYIgAUQ6AIQGCgZWgIQAnj3F3D9QiCpEMTe',
    'fn': 's1.v1.chk'
}

headers = {
    #"Host": "vkvd216.mycdn.me",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Origin": "http://vk.com",
    "Referrer": "http://vk.com",
    "Connection": "keep-alive",
    "Cookie": "tstc=p",
    "Upgrade-Insecure-Requests": "0",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    #"Sec-Fetch-User": "?1",
    #"Pragma": "no-cache",
    #"Cache-Control": "no-cache"
}

def full_video():
    params = [default_params.copy() for _ in range(15)]
    params[0]['fn'] = 'v1.hdr'
    params[1]['fn'] = 'a2.hdr'

    for i,param in enumerate(params[2:]):
        param['fn'] = f's{i+1}.v1.chk'

    return params

def params_to_url(cdn_number, p):
    return f'http://vkvd{cdn_number}.mycdn.me/'+'/'.join('/'.join(map(str, item)) for item in p.items())

urls = [params_to_url(216, params) for params in full_video()]

with open('test.mp4', 'ab') as video:
    for url in urls:
        r = requests.get(url, headers=headers)
        print(r)
        #print(r.headers.get('Content-Disposition'))
        video.write(r.content)