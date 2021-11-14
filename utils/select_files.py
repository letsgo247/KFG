import os
import shutil

root_dir = './High_Resolution/'
dst_dir = './selected/'

S_array = ['S001', 'S002', 'S003', 'S005', 'S006']
L_array = ['L1', 'L2', 'L8', 'L12', 'L19', 'L22', 'L25']
E_array = ['E01', 'E02', 'E03']
C_array = ['C5', 'C6', 'C7', 'C8', 'C9', 'C15', 'C16', 'C17', 'C19', 'C20']

dirs = os.listdir(root_dir)

for id in dirs:
    for s in S_array:
        for l in L_array:
            for e in E_array:
                for c in C_array:
                    path = os.path.join(id,s,l,e,c) + '.jpg'
                    
                    print(path)

                    src_path = os.path.join(root_dir, path)
                    dst_path = os.path.join(dst_dir, path) 

                    print(src_path)
                    print(dst_path)

                    # if os.path.exists(src_path):
                    #     print('exists')

                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)   # 폴더가 없으면 shutil.copy가 에러남 ㄷㄷ so, 폴더 생성해주는 명령!

                    shutil.copy(src_path, dst_path)