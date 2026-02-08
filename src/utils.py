def normalize_name(txt):
	"""
		This function normalize strings.
		Remove blank spaces in the beginning and 
		in the end of the string.
		E.g.
		cArlOS     AntonIO  ,---> Carlos Antonio
		:params (str): input text
		:return: formated text
	"""
	return " ".join(txt.strip().title().split())

def to_mxn(value, rate: float=1.0):
	"""
		conver a number value to MXN multiplying the rate
"""
	return float(value)*float(rate)

