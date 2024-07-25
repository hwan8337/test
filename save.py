import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase 앱 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')  # Firebase 서비스 계정 키 파일 경로
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

def save_score(user_id, answers, score):
    try:
        user_ref = db.collection("quiz_scores").document(user_id)
        user_ref.set({
            "answers": answers,
            "score": score
        })
        st.success("점수가 Firestore에 저장되었습니다!")
    except Exception as e:
        st.error(f"점수를 저장하는 데 오류가 발생했습니다: {e}")

def load_score(user_id):
    try:
        user_ref = db.collection("quiz_scores").document(user_id)
        doc = user_ref.get()
        if doc.exists:
            data = doc.to_dict()
            return data
        else:
            st.warning("해당 사용자 ID로 저장된 데이터가 없습니다.")
            return None
    except Exception as e:
        st.error(f"데이터를 불러오는 데 오류가 발생했습니다: {e}")
        return None

def main():
    st.title("반도체 공정 퀴즈")

    # 문제와 보기
    st.write("Q1. 다음중 반도체의 8대 공정이 아닌것은?")
    answer1 = st.radio("보기중 정답을 고르시오", ["산화공정", "포토공정", "식각공정", "si추출", "이온주입공정"], key="q1")

    st.write("Q2. 다음중 포토공정의 과정이 아닌것은?")
    answer2 = st.radio("보기중 정답을 고르시오", ["노광", "pr 코팅", "HARD BAKE", "PEB", "ETCHING"], key="q2")

    st.write("Q3. 다음중 반도체 공정 장비가 아닌것은?")
    answer3 = st.radio("보기중 정답을 고르시오", ["퍼니스", "스테퍼", "스크러버", "스핀 코터", "튀져"], key="q3")

    st.write("Q4. HMDS의 역할로 옳은 것을 고르시오")
    answer4 = st.radio("보기중 정답을 고르시오", ["웨이퍼를 보호하기 위해", "웨이퍼 표면을 친수성으로 변환하기 위해", "점도를 약화시키기 위해", "PR을 잘 벗겨내기 위해", "PR코팅이 잘 되게 만들기 위해"], key="q4")

    st.write("Q5. pitch를 줄이는 방법이 아닌것을 고르시오?")
    answer5 = st.radio("보기중 정답을 고르시오", ["파장을 줄인다", "pr의 두께를 줄인다", "cos세타를 키운다", "굴절률을 키운다", "웨이퍼를 물에 담군다"], key="q5")

    # 정답과 점수 계산
    correct_answers = ["si추출", "ETCHING", "튀져", "PR코팅이 잘 되게 만들기 위해", "cos세타를 키운다"]
    user_answers = [answer1, answer2, answer3, answer4, answer5]
    score = 0

    # 각 문제의 배점
    points_per_question = 20

    if st.button("점수 확인"):
        for i in range(len(correct_answers)):
            if user_answers[i] == correct_answers[i]:
                score += points_per_question
        
        st.write(f"당신의 점수는: {score}점 입니다.")

        # 사용자 ID 입력 필드와 점수 저장 버튼
        user_id = st.text_input("사용자 ID를 입력하세요")

        if user_id:
            if st.button("점수 저장"):
                save_score(user_id, user_answers, score)
            
            if st.button("점수 불러오기"):
                data = load_score(user_id)
                if data:
                    st.write(f"저장된 점수: {data['score']}점")
                    st.write(f"저장된 답변: {data['answers']}")

if __name__ == "__main__":
    main()
