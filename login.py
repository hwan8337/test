import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase 앱 초기화
if not firebase_admin._apps:
    cred = credentials.Certificate('secret.json')
    firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

# 회원가입 페이지
def signup_page():
    st.title("회원가입")

    email = st.text_input("이메일 주소")
    password = st.text_input("비밀번호", type="password")
    confirm_password = st.text_input("비밀번호 확인", type="password")

    if st.button("회원가입"):
        if password != confirm_password:
            st.error("비밀번호가 일치하지 않습니다.")
        else:
            user_ref = db.collection("users").document(email)
            user = user_ref.get()
            if user.exists:
                st.error("이미 등록된 사용자입니다.")
            else:
                # 비밀번호 평문으로 저장
                user_ref.set({
                    "password": password
                })
                st.success("회원가입 성공! 로그인 페이지로 이동합니다.")
                st.experimental_rerun()

# 로그인 페이지
def login_page():
    st.title("로그인")

    email = st.text_input("이메일 주소")
    password = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        user_ref = db.collection("users").document(email)
        user = user_ref.get()

        if user.exists:
            # 비밀번호 확인 (평문 비밀번호와 비교)
            if user.to_dict().get("password") == password:
                st.success("로그인 성공!")
                # 로그인 성공 후 처리 (예: 사용자 정보 표시, 다른 페이지로 이동)
            else:
                st.error("비밀번호가 올바르지 않습니다.")
        else:
            st.error("사용자가 존재하지 않습니다.")

# Streamlit 실행
def main():
    st.sidebar.title("네비게이션")
    option = st.sidebar.selectbox("페이지 선택", ["로그인", "회원가입"])

    if option == "로그인":
        login_page()
    elif option == "회원가입":
        signup_page()

if __name__ == "__main__":
    main()
