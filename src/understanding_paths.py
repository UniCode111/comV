from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
print(BASE) # Carpeta de mi proyecto

raw = BASE / "data" / "raw"
clean = BASE / "data" / "clean"

#Creacion
raw.mkdir(parents=True, exist_ok =True)
clean.mkdir(parents=True, exist_ok=True)

#Escribir a un archivo txt
txt_path = raw / "notas.txt"

txt= """
	Los alumnos que van a reprobar son
todos los que no tienen asistencia

hoy. Algo bien
"""

txt_path.write_text("Mis alumnos favoritos\n hola chavos\n No van a reprobar", encoding="utf-8")

contenido=txt_path.read_text(encoding="utf-8")
print(contenido)
