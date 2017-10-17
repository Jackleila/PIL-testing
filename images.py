from PIL import Image, ImageFilter

#recortar imagen
def recortarIm(a,b,c,d):
    caja = (a,b,c,d)

# Obtener de la imagen original la región de la caja
    region = imagen.crop(caja)  

    region.show()  # Mostrar imagen de la region
    region.size   # Mostrar tamaño de imagen final 
    print("Guardar imagen? y/n")
    r = input()
    if(r=="y"):
        region.save("region.png")
        print("El recorte ha sido guardado con éxito")
    else:
        print("Seleccione otra acción")
def ReducirIm(a,b):
    reducida = imagen.resize(a, b)
    reducida.show()
#menu
print("Bienvenido a ImageEditorPython")
print("Insertar ruta de la imagen: ")
ruta= input()
print("a) Ver imagen")
print("b) Recortar")
print("c) Cambiar tamaño")
print("d) Borrosa")
print("e) Contorno")

res = input()
try:
        imagen = Image.open(ruta)
        
except:
        print("No ha sido posible cargar la imagen")

if(res=="a"):
    imagen.show()

if(res=="b"):

    print("Introduzca las coordenadas de recorte de la foto:")
    c1 = int(input())
    c2 = int(input())
    c3 = int(input())
    c4 = int(input())
    recortarIm(c1,c2,c3,c4)

if(res=="c"):

    print("Introduzca las coordenadas de escalado de la foto:")
    a1 = int(input())
    a2 = int(input())
    reducida = imagen.resize(a1, a2)
    reducida.show()

   
if(res=="d"):

     blurred = imagen.filter(ImageFilter.BLUR)
     blurred.show()

if(res=="e"):

     im = imagen.filter(ImageFilter.CONTOUR)
     im.show()