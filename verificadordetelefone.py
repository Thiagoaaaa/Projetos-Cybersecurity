import phonenumbers
from phonenumbers import geocoder, carrier, NumberParseException

try:
    phone = input('Digite o telefone no formato internacional (ex: +551140028922): ')
    phone_number = phonenumbers.parse(phone)

    # Verificar se o número é válido
    if phonenumbers.is_valid_number(phone_number):
        #Localização
        localizacao = geocoder.description_for_number(phone_number, 'pt')
        # Operadora
        operadora = carrier.name_for_number(phone_number, 'pt')

        print(f"\n[+] Localização: {localizacao}")
        print(f"[+] Operadora: {operadora}")
    else:
        print("\n[!] Número de telefone inválido. Por favor, verifique o formato.")

except NumberParseException as e:
    print(f"\n[!] Erro ao analisar o número: {e}")
