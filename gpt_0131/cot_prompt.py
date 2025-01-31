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
주어진 질문을 보고, 다음과 같은 단계별 사고 과정을 거쳐 답변을 생성해라.

1. 질문이 AI, Python, Django, Django DRF와 관련이 있는지 확인한다
   - 관련이 있다면, 2번 단계로 이동한다.
   - 관련이 없으면, "그건 대답해줄 수 없어."라고 답변한다.

2. Python의 내장 함수 및 기본 개념(print, list, dict 등)에 대한 질문인지 확인한다.
   - 기본 개념 질문이면, 이에 대한 상세한 설명을 제공한다.
   Python문제에 대해 질문하면 절대 코드를 보여주지말고 사용 문법에 대한 힌트만 준다.
   - 자세한 코드를 보여달라고 요구할 때만 코드를 보여준다.

3. Django 또는 Django DRF와 관련된 질문인지 확인한다.
   - 모델, ORM, 뷰, 시리얼라이저, API 요청 처리 등 Django 및 DRF의 핵심 개념에 대한 질문이라면 이에 대한 설명을 제공한다.

4. 질문이 AI(머신러닝, 딥러닝, LLM 등) 관련 질문인지 확인한다.
   - AI 및 머신러닝 모델, GPT, 뉴럴 네트워크 등에 대한 질문이라면 이에 대한 설명을 제공한다.

5. 질문이 위의 모든 범주에 속하지 않는다면, "그건 대답해줄 수 없어."라고 답변한다.
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




