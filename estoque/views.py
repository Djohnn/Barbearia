
from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Produto, Imagem
from django.http import HttpResponse
from PIL import Image, ImageDraw
from datetime import date
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.urls import reverse
from django.contrib import messages
from rolepermissions.decorators  import has_permission_decorator
from .forms import ProdutoForm



@has_permission_decorator('cadastrar_produtos')
def add_produto(request):
    if request.method == "GET":
        nome = request.GET.get('nome')
        categoria = request.GET.get('categoria')
        preco_min = request.GET.get('preco_min')
        preco_max = request.GET.get('preco_max')
        produtos = Produto.objects.all()
        
        if nome or categoria or preco_min or preco_max:
            
            if not preco_min:
                preco_min = 0

            if not preco_max:
                preco_max = 9999999

            if nome:
                produtos = produtos.filter(nome__icontains=nome)

            if categoria:
                produtos = produtos.filter(categoria=categoria)

            produtos = produtos.filter(preco_venda__gte=preco_min).filter(preco_venda__lte=preco_max)



        categorias = Categoria.objects.all()       
        return render(request, 'add_produto.html', {'categorias': categorias, 'produtos': produtos})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        categoria = request.POST.get('categoria')
        quantidade = request.POST.get('quantidade')
        preco_compra = request.POST.get('preco_compra')
        preco_venda = request.POST.get('preco_venda')
        codigo_barras = request.POST.get('codigo_barras')
         

        produto = Produto(nome=nome,
                          categoria_id=categoria,
                          quantidade=quantidade,
                          preco_compra=preco_compra,
                          preco_venda=preco_venda,
                          codigo_barras=codigo_barras)
        produto.save()
        
        for f in request.FILES.getlist('imagens'):
            name = f'{date.today()}-{produto.id}.jpg'
            
            img = Image.open(f)
            img = img.convert('RGB')
            img = img.resize((300, 300))
            draw = ImageDraw.Draw(img)
            draw.text((20, 280), f"BARBESHOP {date.today()}", (255, 255, 255))
            output = BytesIO()
            img.save(output, format="JPEG", quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(
                output, 'ImageField', name, 'image/jpeg', sys.getsizeof(output), None
            )

            img_dj = Imagem(imagem=img_final, produto=produto)
            img_dj.save()
        messages.add_message(request, messages.SUCCESS, 'Produto cadastrado com sucesso')
        return redirect(reverse(add_produto))       
    

# def produto(request, slug):
#     if request.method == "GET":
#         produto = Produto.objects.get(slug=slug)
#         data = produto.__dict__
#         data['categoria'] = produto.categoria.id
#         form = ProdutoForm(initial=data)
#         return render(request, 'produto.html', {'form': form})
    

def produto(request, slug):
    produto = get_object_or_404(Produto, slug=slug)
    
    if request.method == "POST":
        if "save" in request.POST:
            form = ProdutoForm(request.POST, request.FILES, instance=produto)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto atualizado com sucesso!')
                return redirect(reverse('add_produto'))  # Assumindo que existe uma view para listar produtos
        elif "delete" in request.POST:
            produto.delete()
            messages.success(request, 'Produto excluído com sucesso!')
            return redirect(reverse('add_produto'))  # Assumindo que existe uma view para listar produtos
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'produto.html', {'form': form})