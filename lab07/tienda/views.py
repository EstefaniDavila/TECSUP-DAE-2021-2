from tienda.carrito import Cart
from tienda.models import Producto, categoria
from django.shortcuts import render

# Create your views here.
def index(request):
    product_list = Producto.objects.order_by('nombre')[:10]
    category_list = categoria.objects.all()
    context = {
        'product_list':product_list,
        'category_list':category_list,
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    objProducto = Producto.object.get(pk=producto_id )
    context = {
        'producto':objProducto
    }
    return render(request, 'productos.html', context)
    
def agregarCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,1)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def eliminarProductoCarrito(request,producto_id):
    objProducto = Producto.objects.get(id=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.remove(objProducto)
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def limpiarCarrito(request):
    CarritoProducto = Cart(request)
    CarritoProducto.clear()
    print(request.session.get("cart"))
    return render(request,'carrito.html')

def carrito(request):
    print(request.session.get("cart"))
    return render(request,'carrito.html')
