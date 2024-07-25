import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase 프로젝트의 서비스 계정 키 파일 경로
cred = credentials.Certificate('secret.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred)

# Firestore 클라이언트 생성
db = firestore.client()

# 데이터 추가
doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})

# 데이터 가져오기
doc_ref = db.collection('users').document('alovelace')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print('No such document!')

# 데이터 업데이트
doc_ref.update({'born3': 18115})

# 데이터 삭제
#doc_ref.delete()
