from flask import Flask, render_template, request
from faker import Faker
import requests
import random
import json
import cv2
import glob



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route('/lotto')
def lotto():
    #이부분 부터는 파이썬코드로 작성 가능
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
    print(lotto_dict["drwNoDate"])
    '''week_num = []
    drwtNo = ["drwtNo1","drwtNo2","drwtNo3","drwtNo4","drwtNo5","drwtNo6"]
    for num in drwtNo:
        number = lotto_dict[num]
        week_num.append(number)
    
    print(week_num)
    '''
    week_format_num = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week_format_num.append(num)
    print(num)
    
    # print(type(res))
    # print(type(json.loads(res)))
    
    num_list = range(1,46)
    pick = random.sample(num_list,6)
    #html파일 하나를 보내줌
    
    #render는 flask에서 가져오는거기 때문에 render_template를 추가해주어야 함
    
    # pick = 우리가 생성한 번호
    # week_format_num =  이번 주 당첨번호
    ###위의 두 값을 비교해서 로또 당첨 등수를 출력!!!!
    
    #sorted()
    # 1등 : 6개의 숫자를 다 맞출 때
    # 2등 : 5개 
    # 3등 : 5개
    # 4등 : 4개
    # 5등 : 3개
    # 꽝
    
    count_num = 0
    bonus = lotto_dict["bnusNo"]
    
    for i in range(6):
        for j in range(6):
            if(pick[i] == week_format_num[j]):
                count_num = count_num +1
            
                
    if(count_num==5):
        for i in range(6):
            if(pick[i] == bonus):
                count_num=10
                
                
    if(count_num ==6):
        ss="1등이여"
    elif(count_num==10):
        ss="2등이여"
    elif(count_num==5):
        ss="3등이여"
    elif(count_num==4):
        ss="4등이여"
    elif(count_num==3):
        ss="5등이여"
    else:
        ss="꽝이여"
        
        
    return render_template("lotto.html",lotto=pick,week_format_num=week_format_num,ss=ss)
    
@app.route('/lottery/')
def lottery():
    # 로또 정보를 가져온다
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
    res = requests.get(url).text
    lotto_dict = json.loads(res)
   
    
    # 1등 당첨 번호를 week리스트에 넣는다.
    week = []
    for i in range(1,7):
        num = lotto_dict["drwtNo{}".format(i)]
        week.append(num)
    
    # 보너스 번호를  bonus 변수에 넣는다
    bonus = lotto_dict["bnusNo"]
    
    
    # 임의의 로또 번호를 생성한다.
    pick = random.sample(range(1,46),6)
    
    # 비교해서 몇등인지 저장한다.
    match = len(set(pick) & set(week))
    
    if(match == 6):
        text = "1등"
    elif(match == 5):
        if(bonus in pick):
            text = "2등"
        else:
            text = "3등"
    elif(match ==4):
        text = "4등"
    else :
        text = "꽝"
    
    # 사용자에게 데이터를 넘겨준다.
    return render_template("lottery.html", pick=pick, week=week, text = text)
    
@app.route('/ping')
def ping():
    # 사용자가 입력하는 페이지
    
    return render_template("ping.html")
    
@app.route('/pong')
def pong():
    input_name = request.args.get('name')
    
    
    images = glob.glob('{C:\Users\student\change\startbootstrap-resume-gh-pages\img}/*.jpg')
    for fname in images:
        original = cv2.imread(fname, cv2.IMREAD_COLOR)
        cv2.imshow('Original', original)
        
    
    return render_template("pong.html",html_name=input_name, original=original)
    
