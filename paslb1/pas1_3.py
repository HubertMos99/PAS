import ipaddress

def sprawdz_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

adres_ip = input("Podaj adres IP: ")

if sprawdz_ip(adres_ip):
    print(f"Adres IP {adres_ip} jest poprawny.")
else:
    print(f"Adres IP {adres_ip} jest niepoprawny.")