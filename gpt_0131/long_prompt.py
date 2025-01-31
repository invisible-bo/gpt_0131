import openai
from dotenv import load_dotenv
import os

# 환경 변수 로드
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 생성
client = openai.OpenAI()

# 기본 프롬프트 설정 
base_prompt = """
너는 AI 및 Python, Django, Django DRF를 가르치는 선생님이야.  
AI, Python, Django, Django DRF와 직접적으로 관련된 질문에는 상세히 답변해줘.  
Python의 내장 함수 및 기본 개념(print, list, dict 등)에 대한 질문도 허용해야 해. 
python문제에 대해 질문하면 절대 코드를 보여주지말고 사용 문법에 대한 힌트만 줘야 해. 
그러나 AI, Python, Django, Django DRF와 관련이 없는 질문에 대해서는  
"그건 대답해줄 수 없어"라고만 응답해야 해.
"""

while True:
    user_input = input("\n 질문을 입력하세요 (종료하려면 'exit' 입력): ")

    if user_input.lower() == "exit":
        print("프로그램을 종료합니다.")
        break

    # 기본 프롬프트 + 사용자 입력 결합
    full_prompt = base_prompt + user_input

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": full_prompt}]
    )

    print("\n GPT 응답: ")
    print(response.choices[0].message.content)



