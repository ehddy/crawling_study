# 코드 출처: https://uipath.tistory.com/135
# api 참고 https://developers.google.com/drive/api/v3/reference?hl=ko
from Google import Gdrive
 
 
CLIENT_SECRET_FILE = '/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5/credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Gdrive(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

print(dir(service)) 




# 폴더 생성 테스트 
folders = ['folder1', 'folder2', 'folder3']

for folder in folders:
    file_metadata = {
        'name' : folder, 
        'mimeType' : 'application/vnd.google-apps.folder'
    }

    service.files().create(body=file_metadata).execute()




