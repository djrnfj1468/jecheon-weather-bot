import requests

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1509537983374557357/9AGe4mkfnUm0ESk45duHNEjGx6ihKdlS28vwZefRDIVK4NL7qfu-3i5rb-zP5cu3viYI"
API_KEY = "c5b724c78b0a4df3292cf2d326799747"

def send_jecheon_weather_api():
    print("날씨 API를 호출하는 중...")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Jecheon&appid={API_KEY}&units=metric&lang=kr"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        weather_desc = data['weather'][0]['description'] 
        temp = data['main']['temp']                      
        humidity = data['main']['humidity']             
        
        message = (
            f"📡 **오늘의 제천 날씨 (API 연동)**\n"
            f"현재 날씨 상태는 **{weather_desc}**이며, "
            f"온도는 **{temp}°C**, 습도는 **{humidity}%** 입니다. 오늘도 좋은 하루 보내세요!"
        )
        
    except Exception as e:
        message = f"❌ 날씨 API를 불러오는 데 실패했습니다. (에러: {e})"

    requests.post(WEBHOOK_URL, json={"content": message})
    print("디스코드 전송 완료!")

if __name__ == "__main__":
    send_jecheon_weather_api()
