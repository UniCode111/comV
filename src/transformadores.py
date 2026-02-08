from utils import normalize_name, to_mxn

# Nesting lista de diccionarios raw
raw=[
	{"nombre": "	ana 	", "activo": True, "monto": "120.50" },
	{"nombre": " LUIS ", "activo": False, "monto":"0"},
	{"nombre": " mara ", "activo": True, "monto":"99.9"},
]


def clean (reg):
	return {
		"nombre": normalize_name(reg["nombre"]),
		"activo": bool(reg["activo"]),
		"monto_mxn": to_mxn(reg["monto"], rate=1.0),
	}

#Lista de diccionarios limpia-clean
#List comprehension engloba  append y for
#r es una variable auxiliar
clean = [clean(r) for r in raw if r.get("activo")]

print(raw)
print(clean)
