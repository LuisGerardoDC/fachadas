
from os import scandir, getcwd
import os
ruta = "D:/Pix2Pix/CasasData/"
carpetas = ["CasasImput/","CasasTarget/"]
def ls(ruta = getcwd()):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]

def main():
	i = 0
	global carpetas
	for carpeta in carpetas:
		i = 0
		casas = ls(ruta+carpeta)
		print(carpeta)
		for casa in casas:	
			print(ruta+carpeta+str(i)+'.jpg')
			os.rename(ruta+carpeta+casa,ruta+carpeta+str(i)+'.jpg')
			i +=1

def test():
	casas = ls(ruta+carpetas[0])
	print(ruta+carpetas[0]+casas[0])
	os.rename(ruta+carpetas[0]+casas[0],ruta+carpetas[0]+"preuba_.jpg")

if __name__ == '__main__':
	main()