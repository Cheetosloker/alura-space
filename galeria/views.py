from django.shortcuts import render



def index(request):
    
    dados = {
    1:{"nome": "Nebulosa de carina", "Legenda": "Webbtelecope.org/nasa/james webb"},
    2:{"nome": "Galaxia ngc 1079", "Legenda": "Webbtelecope.org/nasa/james webb"}
}
    return render(request, 'galeria/index.html', {"cards": dados})

def imagem(request):
    return render(request, 'galeria/imagem.html')