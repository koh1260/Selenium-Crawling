import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com/")
res.raise_for_status()
soup =  BeautifulSoup(res.text,  "lxml")

images = soup.find_all("img", attrs = {"class":"thumb_img"})

for idx, image in enumerate(images):
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "http:"+image_url

    print(image_url)
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("imgs","movie{}.jpg".format(idx+1), "wb")as f:
        f.write(image_res.content)

# for idx, image in enumerate(images):
#     image
   
# for image in images:
#     print(image["src"])
# soup = BeautifulSoup(res.text, "lxml")
# #res.text 파일을 lxml parser를 통해 Beautiful soup 객체로 만듦

# # print(soup.title) #파일 속 html태그 불러오기 처음으로 발견되는
# # print(soup.img) #얘는 text만
# print(soup.img.attrs) #해당 태그의 속성
# print(soup.img['class']) #해당 태그의 속성 중 class 값 다른 값도 가능
# print(soup.find(attrs = {'class': 'bg_loading'}))#해당 값을 가지는 태그 찾기
# print(soup.find('img',attrs = {'class': 'bg_loading'}))




# res = requests.get("https://www.google.com/search?q=%EA%B6%8C%EC%A0%95%EC%97%B4&sxsrf=APq-WBv5GUhx1Qmsr2jowenzif7vgXLc_A:1650972853100&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi-ksWT0bH3AhUKwosBHT6CALwQ_AUoAXoECAIQAw&biw=720&bih=707&dpr=2")
# res.raise_for_status() #문제 있으면 종료 없으면 진행

# print(res.status_code) #응답 권한 확인 200은 있음 403은 없음

# # if res.status_code == requests.codes.ok:
# #     print("good")
# # else:
# #     print("not good")
# # res.raise_for_status()
# # print("웹 스크래핑 진행")
# print(len(res.text))
# print(res.text)

# with open("mt google.html", "w", encoding="utf-8")as f:
#     f.write(res.text)

# from cgitb import html
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.google.co.kr/search?q=%EA%B6%8C%EC%A0%95%EC%97%B4&hl=ko&tbm=isch&sxsrf=APq-WBsFGTotyklSAB3kJ5EoqXEXW1m55g%3A1651083148281&source=hp&biw=720&bih=707&ei=jIdpYp_uD8mD-Qash76QBQ&iflsig=AHkkrS4AAAAAYmmVnILkZd8EViA9NO-rpTpL2yn_rPsO&ved=0ahUKEwif5K-E7LT3AhXJQd4KHayDD1IQ4dUDCAc&uact=5&oq=%EA%B6%8C%EC%A0%95%EC%97%B4&gs_lcp=CgNpbWcQAzIICAAQgAQQsQMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgjEO8DECc6CwgAEIAEELEDEIMBOgQIABADOggIABCxAxCDAToKCCMQ7wMQ6gIQJ1AAWIsLYO0LaAJwAHgAgAFqiAHHB5IBAzYuNJgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img#imgrc=h--oFVB-CQl3jM"

# res = requests.get(url)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, 'lxml')

# images = soup.find_all("img", attrs={"jsname":"Q4LuWd"})

# for image in images:
#     print(image["src"])
#     print(len(image))
