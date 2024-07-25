import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
key_dict = json.loads(st.secrets["textkey"])

# Firebase 앱 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate(key_dict)  # Firebase 서비스 계정 키 파일 경로
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()


def save_score(user_id, answers, score):
    """사용자 ID, 답변 및 점수를 Firestore에 저장합니다."""
    try:
        # JSON 형식으로 저장하기 위해 문자열을 파싱합니다
        # 파싱할 필요가 없는 경우 이 부분을 제거할 수 있습니다
        import json
        try:
            answers_json = json.loads(answers)
        except json.JSONDecodeError:
            st.error("답변을 JSON 형식으로 입력해 주세요.")
            return

        user_ref = db.collection("quiz_scores").document(user_id)
        user_ref.set({
            "answers": answers_json,
            "score": score
        })
        st.success("점수가 Firestore에 저장되었습니다!")
    except Exception as e:
        st.error(f"점수를 저장하는 데 오류가 발생했습니다: {e}")

def load_score(user_id):
    """사용자 ID로 Firestore에서 저장된 점수를 불러옵니다."""
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
    st.title("점수 저장 및 불러오기")

    # 사용자 ID 입력 필드와 점수 저장 버튼
    user_id = st.text_input("사용자 ID를 입력하세요")

    if user_id:
        score = st.number_input("점수를 입력하세요", min_value=0, step=1)

        answers = st.text_area("답변을 입력하세요 (JSON 형식)", "[]")

        if st.button("점수 저장"):
            save_score(user_id, answers, score)
        
        if st.button("점수 불러오기"):
            data = load_score(user_id)
            if data:
                st.write(f"저장된 점수: {data['score']}점")
                st.write(f"저장된 답변: {data['answers']}")

if __name__ == "__main__":
    main()
