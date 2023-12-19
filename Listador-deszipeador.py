from tkinter.filedialog import askdirectory
import os
from zipfile import ZipFile
from tkinter.messagebox import showinfo

# Lsitar todos los archivos de un directorio y subdirectorios
def listador(ruta):
    lista_archivos = []
    for root, dirs, files in os.walk(ruta):
        for name in files:
            lista_archivos.append(os.path.join(root, name))
    return lista_archivos

# Seleccionar directorio
directorio = askdirectory(title="Seleccionar directorio")

# Listar archivos
lista_archivos = listador(directorio)

# Reemplazar los "/" por "\" para que sea compatible con Windows
lista_archivos = [x.replace("/", "\\") for x in lista_archivos]

# Lista de archivos ZIP
lista_archivos_zip = [x for x in lista_archivos if x.endswith(".zip")]

# Extraer archivos ZIP en una carpeta con el mimsmo nombre del zip
for z in lista_archivos_zip:
    with ZipFile(z, 'r') as zipObj:
        zipObj.extractall(z[:-4])

# Guardar en un archivo txt
lista_archivos_2 = listador(directorio)

# Reemplazar los "/" por "\" para que sea compatible con Windows
lista_archivos_2 = [x.replace("/", "\\") for x in lista_archivos_2]

# Guardar en un archivo txt
with open("lista_archivos.txt", "w") as f:
    for item in lista_archivos_2:
        f.write("%s\n" % item)

# Mostrar mensaje
showinfo("Listador", "Se ha creado el archivo lista_archivos.txt")