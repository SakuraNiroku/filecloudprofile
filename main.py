import hashlib
import json

data = {}

def generate_hash(text, algorithm='sha256'):
    # 创建哈希对象
    hash_obj = hashlib.new(algorithm)
    
    # 更新哈希对象（需要传入字节流）
    hash_obj.update(text.encode('utf-8'))
    
    # 获取十六进制格式的哈希值
    return hash_obj.hexdigest()

with open('files.json','r',encoding='UTF-8') as f:
    data = json.loads(f.read())

files : list = data


import os
import shutil

OUTPUT_DIR = 'dist'

if os.path.exists(OUTPUT_DIR):
    shutil.rmtree(OUTPUT_DIR)
os.mkdir(OUTPUT_DIR)

os.chdir(OUTPUT_DIR)

if os.path.exists('files'):
    shutil.rmtree('files')
os.mkdir('files')

fileList = []

for file in files:
    shortID = file['version']+'-'+generate_hash(f"{file['tag']}-{file['version']}")[:6].upper()
    downUrl = file['link']

    fileList.append({
        "tag":file['tag']
    })

    with open(f"files/{file['tag']}.json",'w',encoding='UTF-8') as f:
        f.write(json.dumps({
            "shortId":shortID,
            "downloadUrl":downUrl
        },indent=4))

with open('files.json','w',encoding='UTF-8') as f:
    f.write(json.dumps(fileList,indent=4))
    