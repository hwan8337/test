import streamlit as st

st.title("반도체 공정 퀴즈")

# 문제와 보기
st.write("Q1. 다음중 반도체의 8대 공정이 아닌것은?")
answer1 = st.radio("보기중 정답을 고르시오", ["산화공정", "포토공정", "식각공정", "si추출", "이온주입공정"], key="q1")

st.write("Q2 다음중 포토공정의 과정이 아닌것은?")
answer2 = st.radio("보기중 정답을 고르시오", ["노광", "pr 코팅", "HARD BAKE", "PEB", "ETCHING"], key="q2")

st.write("Q3 다음중 반도체 공정 장비가 아닌것은?")
answer3 = st.radio("보기중 정답을 고르시오", ["퍼니스", "스테퍼", "스크러버", "스핀 코터", "튀져"], key="q3")

st.write("Q4 HMDS의 역할로 옳은 것을 고르시오")
answer4 = st.radio("보기중 정답을 고르시오", ["웨이퍼를 보호하기 위해", "소수성으로 변환하기 위해", "점도를 약화시키기 위해", "PR을 잘 벗겨내기 위해", "PR코팅이 잘 되게 만들기 위해"], key="q4")

st.write("Q5 pitch를 줄이는 방법이 아닌것을 고르시오?")
answer5 = st.radio("보기중 정답을 고르시오", ["파장을 줄인다", "pr의 두께를 줄인다", "cos세타를 키운다", "굴절률을 키운다", "웨이퍼를 물에 담군다"], key="q5")
# 정답과 점수 계산
correct_answers = ["si추출", "ETCHING", "튀져", "소수성으로 변환하기 위해", "cos세타를 키운다"]
user_answers = [answer1, answer2, answer3, answer4, answer5]
score = 0

# 각 문제의 배점
points_per_question = 20

if st.button("점수 확인"):
    for i in range(len(correct_answers)):
        if user_answers[i] == correct_answers[i]:
            score += points_per_question
    
    st.write(f"당신의 점수는: {score}점 입니다.")
    
    # Session state에 점수 저장
    st.session_state['score'] = score
    st.write(f"세션에 저장된 점수: {st.session_state['score']}점")

# 주의: Streamlit은 매 페이지 로드 시 state를 초기화하기 때문에 세션 상태를 유지하려면 다른 방법을 사용해야 합니다.
