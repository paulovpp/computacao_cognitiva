import numpy as np 
import cv2 
import mahotas
import csv

# #Função para facilitar a escrita nas imagem 
# def escreve(img, texto, cor=(255,0,0)):
#     fonte = cv2.FONT_HERSHEY_SIMPLEX 
#     cv2.putText(img, texto, (10,20), fonte, 0.5, cor, 0, cv2.LINE_AA)
    
# img = cv2.imread('Test\Img (1).jpg') #Carregamento da imagem  
# imgColorida = img[::8,::8] # Diminui a imagem

# #Se necessário o redimensionamento da imagem pode vir aqui.
# #Passo 1: Conversão para tons de cinza 
# img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)  
# #Passo 2: Blur/Suavização da imagem 
# suave = cv2.blur(img, (7, 7))  
# #Passo 3: Binarização resultando em pixels brancos e pretos 
# T = mahotas.thresholding.otsu(suave) 
# bin = suave.copy() 
# bin[bin > T] = 255 
# bin[bin < 255] = 0 
# bin = cv2.bitwise_not(bin)  
# #Passo 4: Detecção de bordas com Canny 
# bordas = cv2.Canny(bin, 70, 150)  

# #Passo 5: Identificação e contagem dos contornos da imagem 
# #cv2.RETR_EXTERNAL = conta apenas os contornos externos 
# (objetos, lx) = cv2.findContours(bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
# #A variável lx (lixo) recebe dados que não são utilizados

# escreve(img, "Imagem em tons de cinza", 0) 
# escreve(suave, "Suavizacao com Blur", 0) 
# escreve(bin, "Binarizacao com Metodo Otsu", 255) 
# escreve(bordas, "Detector de bordas Canny", 255)
# temp = np.vstack([  np.hstack([img, suave]), np.hstack([bin, bordas])])
# cv2.imwrite('Test\img1_res.jpg', temp)
# cv2.imshow("Quantidade de objetos: "+str(len(objetos)), temp) 
# cv2.waitKey(0) 
# imgC2 = imgColorida.copy() 
# # cv2.imshow("Imagem Original", imgColorida)
# cv2.drawContours(imgC2, objetos, -1, (255, 0, 0), 2) 
# escreve(imgC2, str(len(objetos))+" objetos encontrados!") 
# cv2.imshow("Resultado", imgC2) 
# cv2.waitKey(0) 

a = 2
c = [0,1,2,3,4,5,6,7,8,9]
# c.append((a))

# with open('./Test/test.csv', mode='w') as csvfile:
#     file = csv.writer(csvfile, delimiter=',')
#     for i in range(0, 2):
#         file.writerow([c])

print((c[5:]))