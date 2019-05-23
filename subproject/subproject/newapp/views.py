from django.shortcuts import render

# Create your views here.
def main(request): # 요청을 받아와서 main(main이라고 안하고 a라고 해도됨 임의로 정한 것)을 수행하겠다
    text="글자를 입력하세요."
    context={'text':text}
    return render(request,'newapp/index.html',context) #request에는 누구로부터 받아왔는지 담겨있음

def result(request):
    text=request.GET.get('text')
    words=[]
    d={}
    if text is not None:
        words=text.split(" ")
        for i in words:
            if i in d:
                    d[i]=d[i]+1
            else:
                    d[i]=1
    context={'text':text, 'words':words, 'd':d, 'd_item':d.items()}
    return render(request,'newapp/result.html',context)

def menu(request):
    text="menu입니다"
    context={'text':text}
    return render(request,'newapp/menu.html',context)