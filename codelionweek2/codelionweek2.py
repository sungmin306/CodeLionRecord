#likelion.py

set_dinner = set(["된장찌개", "피자", "제육볶음", "짜장면"])
food = "짜장면"
set_dinner = set_dinner- set([food])
print(set_dinner)

#codelion.py

lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]

while True:
    print(lunch)
    item = input("음식을 추가 해주세요 : ")
    if(item == "q"):
        break
    else:
        lunch.append(item)
    
print(lunch)
set_lunch = set(lunch)

#이상형이 뭐에요 code

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)