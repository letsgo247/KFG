from django.shortcuts import render
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
from django.utils.text import get_valid_filename
from urllib import parse

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))    # stylegan 폴더 붙이기 위한 사전작업

from stylegan2_ada_pytorch.projector import run_projection

# Create your views here.

def index(request):
    os.system('cd')
    return render(request,'index.html')

def result(request):
    print('request.FILES=', request.FILES)
    fileObj = request.FILES['filePath']
    print('fileObj=', fileObj)
    fs = FileSystemStorage()
    filename_encoded = parse.quote(fileObj.name)    # 한글 에러나서 ?로 인코딩 해주는 함수
    print('fileObj.name =', filename_encoded)
    filename_cleaned = get_valid_filename(filename_encoded)     # 알파벳, 대시, 언더바, 닷 등 제거하고 클린하게 만들어줌
    print('filename_cleaned=', filename_cleaned)
    filename_final = fs.save(filename_cleaned, fileObj)
    print('filename_final=', filename_final)
    in_path = filename_final
    out_path = './media/out/proj.png'
    print('in_path=', in_path)

    
    # os.system('pwd')
    os.system('cd')

    run_projection(
        network_pkl = './dnnlib/ffhq.pkl',
        target_fname = './media/'+in_path,
        outdir = './media/out',
        save_video = False,
        seed = 100,
        num_steps = 100
    )



    
    context={'out_path':out_path}
    return render(request,'result.html', context)
