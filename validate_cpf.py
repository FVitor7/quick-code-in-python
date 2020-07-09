import re

def validate_regex(cpf):
	validation = re.match(regex_validation,cpf)
	if validation == None:
		try:
			if validate_cpf(cpf) == True:
				print('CPF Válido')
			else:
				print('CPF Inválido')
		except:
			print('CPF Inválido')
	else:
		cpf = re.sub("\.", "", cpf, 2)
		cpf = re.sub("\-", "", cpf, 1)
		
		if validate_cpf(cpf) == False:
			print('CPF Inválido')
		else:
			print('CPF Válido')
		
	
def validate_cpf(cpf):
    if len(cpf) < 11:
        return False    
    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    
    calc = lambda t: int(t[1]) * (t[0] + 2)
    d1 = (sum(map(calc, enumerate(reversed(cpf[:-2])))) * 10) % 11
    d2 = (sum(map(calc, enumerate(reversed(cpf[:-1])))) * 10) % 11
    return str(d1) == cpf[-2] and str(d2) == cpf[-1]

regex_validation  = "^\d{3}\.\d{3}\.\d{3}\-\d{2}$"

#CPF gerado aleatoriamente para teste ;)
cpf = '854.653.390-39'
validate_regex(cpf) #True

cpf = '85465339039'
validate_regex(cpf) #True

cpf = '854.653.390.39'
validate_regex(cpf) #False

cpf = '854675339039'
validate_regex(cpf) #False
