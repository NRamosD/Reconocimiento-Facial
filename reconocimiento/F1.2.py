import cv2
import os
import imutils

#F1.2  Jimmy Granizo

def capturarrostro(personPath):

	cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

	faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
	count = 0

	try:
		while True:
			ret, frame = cap.read()
			if ret == False: break
			frame =  imutils.resize(frame, width=640)
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			auxFrame = frame.copy()
			faces = faceClassif.detectMultiScale(gray,1.3,5)

			for (x,y,w,h) in faces:
				cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
				rostro = auxFrame[y:y+h,x:x+w]
				rostro = cv2.resize(rostro,(360,360),interpolation=cv2.INTER_CUBIC)
				cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
				count = count + 1
			cv2.imshow('frame',frame)

			k =  cv2.waitKey(1)
			if k == 27 or count >= 300:
				break
		cap.release()

		cv2.destroyAllWindows()
	except: 
		print("Fallo algo")

if __name__ == "__main__":
	print("CASO DE PRUEBA 1:")
	personPath = ""
	print("CASO DE PRUEBA 2:")
	personPath = "C:\\Users\\jgran\\Documents\\CASOS DE PRUEBA\\"
	print("CASO DE PRUEBA 3:")
	personPath = "dfghjlkjhjjk"
	print("CASO DE PRUEBA 4:")
	personPath = "C:\Users\jgran\Documents\CASOS DE PRUEBA\\"
	capturarrostro(personPath)

