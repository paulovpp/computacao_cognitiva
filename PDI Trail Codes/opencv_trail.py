# Importação das bibliotecas
import cv2
import numpy as np
from cv2 import Mat
from numpy import mat
from pyparsing import col
from matplotlib import pyplot as plt


# def change_color(image:Mat, color:int):
#     '''
#     Função que altera a cor da imagem
#     change_color(image, color)
#     image: imagem a ser alterada
#     color: valor em inteiro da cor a ser alterada
#     '''
#     for y in range(0, image.shape[0]):
#         for x in range(0, image.shape[1]):
#             image[y, x] = (color,0,0)
    
#     cv2.imshow("Imagem modificada", image)
#     cv2.waitKey() #espera pressionar qualquer tecla
    

# # Leitura da imagem com a função imread()
# imagem = cv2.imread('PDI Trail Codes/entrada.jpg')
# (b, g, r) = imagem[0, 0] #veja que a ordem BGR e não RGB 

# change_color(imagem, 255) #altera a cor da imagem para qualquer valor inteiro

# print('R: {}, G: {}, B: {}'.format(r, g, b))

# # imprimir dimensões da imagem
# print('Largura em pixels: ', end='')
# print(imagem.shape[1])
# print('Comprimento em pixels: ', end='')
# print(imagem.shape[0])

# # #largura da imagem print('Altura em pixels: ', end='')
# # print(imagem.shape[0])

# # erro: imprime a quantidade de canais PVPP
# #altura da imagem
# print('Canais: ', end='')
# print(imagem.shape[2])

# # Mostra a imagem com a função imshow
# cv2.imshow("Nome da janela", imagem)
# cv2.waitKey(0) #espera pressionar qualquer tecla

# # # Salvar a imagem no disco com função imwrite()
# # cv2.imwrite("saida.jpg", imagem)

# import cv2 
# imagem = cv2.imread('ponte.jpg') 
# for y in range(0, imagem.shape[0], 10): #percorre linhas
#     for x in range(0, imagem.shape[1], 10): #percorre colunas
#         imagem[y:y+5, x: x+5] = (0,255,255)
# cv2.imshow("Imagem modificada", imagem) 
# cv2.waitKey(0)  

# ## CORTANDO UMA IMAGEM / CROP

# recorte = imagem[100:200, 100:200]
# cv2.imshow("Recorte da imagem", recorte)
# cv2.imwrite("recorte.jpg", recorte) #salva no disco 

# ## REDIMENSIONANDO UMA IMAGEM / RESIZE

# img = cv2.imread('ponte.jpg')
# cv2.imshow("Original", img)
# largura = img.shape[1]
# altura = img.shape[0]
# proporcao = float(altura/largura)
# largura_nova = 320 #em pixels
# altura_nova = int(largura_nova*proporcao)
# tamanho_novo = (largura_nova, altura_nova)
# img_redimensionada = cv2.resize(img,
# tamanho_novo, interpolation = cv2.INTER_AREA)
# cv2.imshow('Resultado', img_redimensionada)
# cv2.waitKey(0) 

# ## ESPELHANDO UMA IMAGEM / FLIP

# cv2.imshow("Original", img) 
# flip_horizontal = img[::-1,:]#comando equivalente abaixo
# #flip_horizontal = cv2.flip(img, 1)  

# cv2.imshow("Flip Horizontal", flip_horizontal) 
# flip_vertical = img[:,::-1] #comando equivalente abaixo 
# #flip_vertical = cv2.flip(img, 0)  

# cv2.imshow("Flip Vertical", flip_vertical) 
# flip_hv = img[::-1,::-1] #comando equivalente abaixo  
# #flip_hv = cv2.flip(img, -1) 
# cv2.imshow("Flip Horizontal e Vertical", flip_hv) 
# cv2.waitKey(0)

# ## ROTACIONANDO UMA IMAGEM / ROTATE

# (alt, lar) = img.shape[:2] #captura altura e largura 
# centro = (lar // 2, alt // 2) #acha o centro  
# M = cv2.getRotationMatrix2D(centro, 30, 1.0)#30 graus 
# img_rotacionada = cv2.warpAffine(img, M, (lar, alt))  
# cv2.imshow("Imagem rotacionada em 30 graus", img_rotacionada) 
# cv2.waitKey(0)

# ## SISTEMA DE CORES

# img = cv2.imread('ponte.jpg')
# cv2.imshow("Original", img)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray)
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV", hsv)
# lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow("L*a*b*", lab)
# cv2.waitKey(0)

# (canalAzul, canalVerde, canalVermelho) = cv2.split(img)
# cv2.imshow("Vermelho", canalVermelho) 
# cv2.imshow("Verde", canalVerde) 
# cv2.imshow("Azul", canalAzul) 
# cv2.waitKey(0) 

# resultado = cv2.merge([canalAzul, canalVerde, canalVermelho])

# img = cv2.imread('ponte.jpg')  
# (canalAzul, canalVerde, canalVermelho) = cv2.split(img)  
# zeros = np.zeros(img.shape[:2], dtype = "uint8")  
# cv2.imshow("Vermelho", cv2.merge([zeros, zeros, canalVermelho]))  
# cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros])) 
# cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros])) 
# cv2.imshow("Original", img) 
# cv2.waitKey(0)

# ## HISTOGRAMAS E EQUAÇÕES DE CORES

# img = cv2.imread('ponte.jpg') 
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converte P&B 
# cv2.imshow("Imagem P&B", img) 
# #Função calcHist para calcular o histograma da imagem 
# h = cv2.calcHist([img], [0], None, [256], [0, 256]) 
# plt.figure() 
# plt.title("Histograma P&B") 
# plt.xlabel("Intensidade") 
# plt.ylabel("Qtde de Pixels") 
# plt.plot(h) 
# plt.xlim([0, 256]) 
# plt.show() 
# cv2.waitKey(0)

# plt.hist(img.ravel(),256,[0,256]) 
# plt.show()
# cv2.waitKey(0)

# cv2.imshow("Imagem Colorida", img)

# #Separa os canais
# canais = cv2.split(img)
# cores = ("b", "g", "r")
# plt.figure()
# plt.title("'Histograma Colorido")
# plt.xlabel("Intensidade")
# plt.ylabel("Número de Pixels")
# for (canal, cor) in zip(canais, cores):

# #Este loop executa 3 vezes, uma para cada canal
# hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
# plt.plot(hist, cor = cor)
# plt.xlim([0, 256])
# plt.show() 

# ## EQUALIZAÇÃO DE HISTOGRAMA

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# h_eq = cv2.equalizeHist(img)
# plt.figure()
# plt.title("Histograma Equalizado")
# plt.xlabel("Intensidade")
# plt.ylabel("Qtde de Pixels")
# plt.hist(h_eq.ravel(), 256, [0,256])
# plt.xlim([0, 256])
# plt.show()
# plt.figure()
# plt.title("Histograma Original")
# plt.xlabel("Intensidade")
# plt.ylabel("Qtde de Pixels")
# plt.hist(img.ravel(), 256, [0,256])
# plt.xlim([0, 256])
# plt.show()
# cv2.waitKey(0) 

## SUAVIZAÇÃO DE IMAGENS

# img = cv2.imread('PDI Trail Codes\ponte.jpg')

# img = img[::2,::2] # Diminui a imagem  
# suave = np.vstack([np.hstack([img,cv2.blur(img, ( 3,  3))]),np.hstack([cv2.blur(img, (5,5)), cv2.blur(img, ( 7,  7))]),np.hstack([cv2.blur(img, (9,9)), cv2.blur(img, (11, 11))]),])
# cv2.imshow("Imagens suavisadas (Blur)", suave) 
# cv2.waitKey(0) 

# img = cv2.imread('ponte.jpg')
# img = img[::2,::2] # Diminui a imagem
# suave = np.vstack([
# np.hstack([img,
# cv2.medianBlur(img,  3)]),
# np.hstack([cv2.medianBlur(img,  5),
# cv2.medianBlur(img,  7)]),
# np.hstack([cv2.medianBlur(img,  9),
# cv2.medianBlur(img, 11)]),
# ])
# cv2.imshow("Imagem original e suavizadas pela mediana", suave)
# cv2.waitKey(0)

# img = img[::2,::2] # Diminui a imagem
# suave = np.vstack([
# np.hstack([img,
# cv2.bilateralFilter(img,  3, 21, 21)]),
# np.hstack([cv2.bilateralFilter(img,  5, 35, 35),
# cv2.bilateralFilter(img,  7, 49, 49)]),
# np.hstack([cv2.bilateralFilter(img,  9, 63, 63),
# cv2.bilateralFilter(img, 11, 77, 77)])
# ])

## BINARIZAÇÃO COM LIMIAR

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
# suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur  

# (T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY) 
# (T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV) 
# resultado = np.vstack([  np.hstack([suave, bin]),  np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])  ])   

# cv2.imshow("Binarização da imagem", resultado) 
# cv2.waitKey(0)

# img = cv2.imread('PDI Trail Codes\img1.jpg')

# img = img[::3,::3] # Diminui a imagem
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
# suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur  

# (T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY) 
# (T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV) 
# resultado = np.vstack([np.hstack([suave, bin]),  np.hstack([binI, cv2.bitwise_and(img, img, mask = binI)])])   

# cv2.imshow("Binarização da imagem", binI)
# cv2.waitKey(0)

# cv2.imshow("Binarização da imagem", resultado)
# cv2.imwrite('PDI Trail Codes\img1_res.jpg', resultado)
# cv2.waitKey(0) 

img = cv2.imread('ponte.jpg') 
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converte  
suave = cv2.GaussianBlur(img, (7, 7), 0) # aplica blur   
bin1 = cv2.adaptiveThreshold(suave, 255,  cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5) 
bin2 = cv2.adaptiveThreshold(suave, 255,  cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)  
resultado = np.vstack([  np.hstack([img, suave]),  np.hstack([bin1, bin2])  ])   
cv2.imshow("Binarização adaptativa da imagem", resultado) 
cv2.waitKey(0)






