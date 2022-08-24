import shutil

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import sys

# argv[1] = json 경로
# argv[2] = 데이터베이스 경로
# argv[3] = 파일 아이디 경로
# argv[4] = 구글 드라이브에 올렸을 때의 파일명
# argv[5] = db_version

# argv[2]
# 압축할 파일의 경로
database_path = '/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5'

shutil.make_archive('database', 'zip', database_path, verbose=True)

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()

if not creds or creds.invalid:
    print("make new database file ")
    # argv[1]
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run_flow(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))



FILES = (
    '/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5/아이유 너.txt',
)
# argv[3]
folder_id = "1kUQrUZYfvnfmCByx0MZOxEtHMPDsu-T5"

for file_title in FILES:
    file_name = file_title
    # argv[4], argv[5] -> 'database' + db_version + '.zip'
    metadata = {'name': 'database.zip',
                'parents': [folder_id],
                'mimeType': None
                }

    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
    if res:
        print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))


print(1)
# from googleapiclient.discovery import build
# from httplib2 import Http
# from oauth2client import file, client, tools

# try:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
# except ImportError:
#     flags = None

# SCOPES = 'https://www.googleapis.com/auth/drive.file'
# store = file.Storage('storage.json')
# creds = store.get()


# if not creds or creds.invalid:
#     print("make new storage data file ")
#     credi = '/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5/client_secret_94739633831-rpoa5grhd5ddtlbhr1f79i4qiuu4ijp0.apps.googleusercontent.com.json'
#     flow = client.flow_from_clientsecrets(credi, SCOPES)
#     creds = tools.run_flow(flow, store, flags) if flags else tools.run(flow, store)


# DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

# FILES = (
#     ('/Users/dongyokim/main/jupyter/2022:Summer/크롤링 스터디/5/아이유 너.txt'),
# )

# folder_id = '1kUQrUZYfvnfmCByx0MZOxEtHMPDsu-T5'

# for file_title in FILES:
#     file_name = file_title
#     metadata = {'name': '업로드 이후 id',
#                 'parents': [folder_id],
#                 'mimeType': None
#                 }

#     res = DRIVE.files().create(body=metadata, media_body=file_name).execute()
#     if res:
#         print('Uploaded "%s" (%s)' % (file_name, res['mimeType']))
