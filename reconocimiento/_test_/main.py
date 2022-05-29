import os


  
def obtencionImagenes(datos):
 dato = datos
 if dato is None:
  print("Error.... Data is Null")
 else:
  rutaimagenes = os.path.join(dato,'img')
  dataPath = rutaimagenes
  peopleList = os.listdir(dataPath)
  print("Data correcta") 
  return rutaimagenes


if __name__ == '__main__':
  
    obtencionImagenes(None)

    obtencionImagenes("C://Users//favia//OneDrive//Imágenes")

    obtencionImagenes("C://Users//favia//OneDrive//Imágenex")
    
 