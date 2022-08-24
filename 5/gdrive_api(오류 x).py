# 코드 참고) https://velog.io/@dkwjd131/%EC%9E%91%EC%84%B1%EC%A4%91Python-%EA%B5%AC%EA%B8%80%EB%93%9C%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%97%90-%ED%8F%B4%EB%8D%94%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%ED%95%98%EA%B8%B0
# 주피터에서 돌리면 오류남 

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

# api 연결 및 사전정보 입력
SCOPES = ['https://www.googleapis.com/auth/drive.metadata', 
          'https://www.googleapis.com/auth/drive.file',
          'https://www.googleapis.com/auth/drive']
store = file.Storage('storage.json')
creds = store.get()
    
# 권한 인증 창. 제일 처음만 창이 띄워짐
try :
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
if not creds or creds.invalid:
    print('make new cred')
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run_flow(flow, store)
    
service = build('drive','v3',credentials=creds)
    
# 업로드 할 파일
file_paths = "/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5/아이유 너.txt"
    
# 업로드할 파일 정보 정의
# parents: 업로드할 구글 드라이브 위치의 url 마지막 ID
file_metadata = {
"name": "아이유 너.txt",
"parents": ["1kUQrUZYfvnfmCByx0MZOxEtHMPDsu-T5"]}
# 파일 업로드
media = MediaFileUpload(file_paths, resumable=True)
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()


