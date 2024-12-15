"""
This file is based on the original Weather Notifier project by DESalhi.
Original repository: https://github.com/DESalhi/Weather_Notifier

Modified by Your Name, 2024.
Modifications include:
- Added travel destination recommendations.
- Updated GUI to display recommendations and weather conditions.
- Improved API error handling.
"""

# 웹 데이터를 받아오기 위한 라이브러리이다.
import requests 

# 버튼과 같은 사용자 인터페이스를 위한 라이브러리이다.
from tkinter import Tk, Label, Button

# 사용자의 API Key를 하단에 붙여 넣으십시오.
API_KEY = "a120cd36c9154d06ab6142705231602"
# 날씨 데이터를 가져올 수 있는 API 주소이다.
API_URL = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q="

# 날씨를 가져오는 함수이다.
def get_weather_data(city):
    # 도시에 맞는 데이터 URL을 요청한다.
    url = API_URL + city
    try:
        # request.get으로 날씨 정보를 가져온다.
        response = requests.get(url)

        # 가져온 데이터에 문제가 있으면 오류가 발생한다.    
        response.raise_for_status()

        # 데이터를 딕셔너리 타입으로 변환한다.
        data = response.json()

        # 날씨 상태를 출력한다.
        condition = data['current']['condition']['text']
        return condition

    # 오류 발생 시 오류 메시지를 출력한다.
    except requests.exceptions.RequestException as e:
        return f"Error: Could not retrieve weather data. {str(e)}"

# 여행지 추천함수이다.
def recommend_travel_destination(city, weather_condition):

    #지역별 비 올 때 추천 장소를 설정한 함수이다. rain, rainy 등 "rain"이 날씨 상태에 들어있을 때 작동, 대소문자 통일을 위해 .lower를 사용한다. 
    if 'rain' in weather_condition.lower():
        if city == "Seoul":
            destinations = [
                {"name": "북촌 한옥마을", "rating": 4.28},
                {"name": "동대문 디자인 플라자", "rating": 4.31},
                {"name": "국립현대미술관 서울관", "rating": 4.51}
            ]
        elif city == "Busan":
            destinations = [
                {"name": "국립해양박물관", "rating": 4.32},
                {"name": "부산시립미술관", "rating": 4.63},
                {"name": "트릭아이뮤지엄 부산", "rating": 4.31}
            ]
        elif city == "Daegu":
            destinations = [
                {"name": "스파크랜드", "rating": 4.47},
                {"name": "대구오페라하우스", "rating": 4.64},
                {"name": "대구 향촌문화관", "rating": 4.66}
            ]
        elif city == "Jeju":
            destinations = [
                {"name": "노형수퍼마켙", "rating": 4.31},
                {"name": "오설록 티뮤지엄", "rating": 4.46},
                {"name": "동문재래시장", "rating": 4.35}
            ]
        elif city == "Incheon":
            destinations = [
                {"name": "NC 큐브 커낼워크", "rating": 4.22},
                {"name": "인천 차이나타운", "rating": 4.24}
            ]
                    
        else:
            destinations = [
                {"name": "국립중앙과학관", "rating": 4.46},
                {"name": "대전시립미술관", "rating": 4.67}
            ]
    # 비가 안올때 장소와 별점을 설정한 함수이다.
    else:        
        if city == "Seoul":
            destinations = [
                {"name": "남산 서울타워", "rating": 4.36},
                {"name": "경복궁", "rating": 4.69},                
                {"name": "남이섬", "rating": 4.54}
            ]
        elif city == "Busan":
            destinations = [
                {"name": "해운대 해변", "rating": 4.33},
                {"name": "광안리 해변", "rating": 4.34},
                {"name": "감천문화마을", "rating": 4.4}
            ]
        elif city == "Daegu":
            destinations = [
                {"name": "대구 이월드", "rating": 4.55},
                {"name": "앞산 공원", "rating": 4.35},
                {"name": "달성공원", "rating": 4.37}
            ]
        elif city == "Jeju":
            destinations = [
                {"name": "한라산", "rating": 4.45},
                {"name": "성산일출봉", "rating": 4.43},
                {"name": "포레스트 공룡 사파리", "rating": 4.27}
            ]
        elif city == "Incheon":
            destinations = [
                {"name": "르 스페이스 인스파이어", "rating": 4.9},
                {"name": "동막해변", "rating": 4.16},
                {"name": "늘솔길공원 양떼목장", "rating":4.09}
            ]
        else:
            destinations = [
                {"name": "한밭수목원", "rating": 4.31},
                {"name": "오월드", "rating": 4.45}
            ]
    # 날씨를 고려하여 여행지 목록을 반환한다.        
    return destinations 

def display_notification(city):
    # 날씨 상태를 가져온다.
    weather = get_weather_data(city)
    if weather:

        # 반환 값인 여행지 목록을 가져온다.
        travel_destinations = recommend_travel_destination(city, weather)
        # 창을 생성한다.
        root = Tk()
        # 제목을 설정한다.
        root.title(f"{weather}한 {city} 여행지")
        # 크기를 설정한다.
        root.geometry("400x150")
        # 날씨를 표시한다.
        Label(root, text=f"{city}의 날씨: {weather}").pack() 
        # 여행지 목록, 별점을 출력한다.
        Label(root, text="추천 여행지와 별점:").pack()  

        # for 문으로 지역해당 정보를  전부 출력한다.
        for destination in travel_destinations:
            Label(root, text=f"{destination['name']} - {destination['rating']}점").pack()
        Button(root, text="닫기", command=root.destroy).pack()
        root.mainloop()

# 프로그램을 시작한다.
if __name__ == "__main__":
    # 사용자로부터 도시를 입력받는다.
    city_name = input("날씨를 확인할 도시를 입력하세요 (Seoul, Busan, Daegu, Jeju, Incheon, 기본 설정: Daejeon): ")
    # 창 생성함수를 불러온다.
    display_notification(city_name)

