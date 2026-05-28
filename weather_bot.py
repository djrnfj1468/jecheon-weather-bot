import requests

# 1단계에서 복사한 웹훅 URL을 아래 따옴표 안에 넣으세요.
webhook_url = "https://discordapp.com/api/webhooks/1509537983374557357/9AGe4mkfnUm0ESk45duHNEjGx6ihKdlS28vwZefRDIVK4NL7qfu-3i5rb-zP5cu3viYI"

# 디스코드로 보낼 메시지 내용
# 예시로 제천의 날씨 정보를 담아봤습니다.
message_data = {
    "content": "🔔 오늘의 알림: 제천 날씨는 맑음! 외출하기 좋은 날씨입니다."
}

# 디스코드로 메시지 전송!
response = requests.post("https://discordapp.com/api/webhooks/1509537983374557357/9AGe4mkfnUm0ESk45duHNEjGx6ihKdlS28vwZefRDIVK4NL7qfu-3i5rb-zP5cu3viYI", json=message_data)

# 전송이 성공했는지 확인
if response.status_code == 204:
    print("디스코드로 메시지 전송 성공! 🎉")
else:
    print(f"전송 실패 ㅠㅠ 에러 코드: {response.status_code}")