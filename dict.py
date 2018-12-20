phonebook = {
    "치킨집" : "02-000-0000", 
    "피자집" : "062-123-3457"
}
#print(phonebook["치킨집"])

# 가수 그룹의 딕셔너리를 만들어주세요
# 변수명 : 그룹이름
# key : 이름
# value : 나이

Winner = {
    "송민호" : 26,
    "김진우":28,
    "이승훈":27,
    "강승윤":25
}

Bigbang = {
    "승리":27,
    "지디":29,
    "탑":29,
    "대성":26,
    "태양":29
}

# 변수명 : idol
# 두개의 그룹을 넣어주세요
# 딕셔너리안에 딕셔너리를 넣어줌
idol = {
    "Winner":Winner,
    "Bigbang":Bigbang
}
# print(idol)
# print(idol["Bigbang"]["승리"])  # 27 출력
# print(idol["Winner"]["송민호"]) # 26 출력

score = {
    "수학":50,
    "국어":70,
    "영어":100
}
'''
# 둘다 반복하는 경우
for key, value in score.items():
    pass # print를 주석처리하면 for문 혼자 도니까 pass처리를 해줌
    #print(key, value)

# 키값만     
for key in score.keys():
    print(key)

# value만
for value in score.values():
    print(value)

score_sum = 0
for value in score.values():
    score_sum = score_sum + value
print(score_sum/3)
'''



ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj1":  {
            "lecturer": "ChangE",
            "manager": "pro1",
            "class president": "서희수",
            "groups": {
                "두드림": ["구종민", "김녹형", "윤은솔", "이준원", "이창훈"],
                "런치타임": ["문영국", "박나원","박희승", "서희수", "황인식"],
                "Friday": ["강민지", "박현진", "서상준", "안현상", "최진호"],
                "TMM": ["김훈", "송건희", "이지선", "정태준", "조호근"],
                "살핌": ["문동식", "이중봉", "이지희", "차상권", "최보균"]
            }
        },
        "gj2": {
            "lecturer": "teacher2",
            "manager": "pro2"
        },
        "gj3": {
            "lecturer": "teacher3",
            "manager": "pro3"
        }
    }
}

# 1. ssafy를 진행하는 지역은 몇개 인가요?
print(len(ssafy["location"]))

# 2. python standard library 'requests'가 있나요?? (True or False)
if ssafy["language"]["python"]["python standard library"] == "requests":
    print(True)
else:
    print(False)

# 3. 광주 1반에 반장의 이름을 출력하세요
print(ssafy["classes"]["gj1"]["class president"])

# 4. ssafy에서 배우는 언어들을 출력하세요 dictionary.keys 활용
for i in ssafy["language"].keys():
    print(i)

# 5. ssafy gj2의 강사와 매니저의 이름을 출력하세요
    # 예시 ) teacher2
    #       pro2

for i in ssafy["classes"]["gj2"].values():
    print(i)
    
# 6. framework들의 이름과 설명을 다음과 같이 출력하세요
    # 예시)
    # flask는 micro이다.
    # django 는 full-functioning 이다.

for i in ssafy["language"]["python"]["frameworks"].items():
    print(i)
    
# 7. 오늘 당번을 뽑기 위해 '살핌'조원중 1명을 랜덤으로 뽑아라
    # 예시)
    # 오늘 당번은 문동식입니다.
import random
print(random.choice(ssafy["classes"]["gj1"]["groups"]["살핌"]))


