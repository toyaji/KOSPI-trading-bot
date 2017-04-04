import requests
import pandas as pd
import time
#코빗 토큰 얻기 - 다이렉트 인증으로 바이 안에다가 유저명이랑 비번 다 집어넣음

client_id = 'wvOfwR3yvlw5WvAn74ro1pRWStb8HT3450NprLlUe1PTYl1ZccoPUtSlxwRGe'
client_secret = 'Dqt8gWcJd1eCtVfotr8Z5EXC0nowmFVbs9vWwrmhsM1A8lrzeXDfvEior1OcV'
username = 'happytoday83@naver.com'
password = 'qkdnf87!'


def get_token():
    post_data = {
        "client_id": client_id,
        "client_secret":client_secret,
        "username": username,
        "password": password,
        'grant_type': 'password'
    }

    respon = requests.post('https://api.korbit.co.kr/v1/oauth2/access_token', data=post_data)
    print(respon)
    tokendata = respon.json()
    print(tokendata)
    return tokendata

def get_userinfo(tokendata):
    token = tokendata['access_token']
    headers = {'Authorization': 'Bearer ' + token}
    respon = requests.get('https://api.korbit.co.kr/v1/user/info', headers=headers)

    print(respon)
    info = respon.json()
    print(info)

def get_ticker():
    """코빗에서 json 파일로 틱 가져오는 함수"""
    params = {'currency_pair': 'btc_krw'}
    respon = requests.get("https://api.korbit.co.kr/v1/ticker/detailed", params=params)

    info = respon.json()
    print(info)
    return info



if __name__ == '__main__':
    #tokendata = get_token()
    #get_userinfo(tokendata)

    data = []
    flag = 1
    while True:
        # 단일 틱 가져오기
        tick = get_ticker()
        df = pd.DataFrame(tick, index=[0])

        # 데이터 프레임으로 전환하고 한시간마다 합쳐서 csv 로 로딩하고 비우기
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        data.append(df)

        # 날짜 넘어갈때 지금까지 쌓은 녀석 저장하고 새 파일 만들기
        # todo 여기에다가 날짜 넘어갈때 색인가지고 셋팅하는법 설정해야함
        print(df['timestamp'])
        # if df['timestamp']time.strftime()

        # 30초 재우고 플래그 올리기
        time.sleep(30)
        flag += 1


        if flag >= 10:
            hourdata = pd.concat(data)
            hourdata = hourdata.set_index(['timestamp'])
            t = time.strftime('%Y%m%d')
            with open(r'./%s.csv' % t, 'a') as f:
                hourdata.to_csv(f, header=False)

            flag = 0

