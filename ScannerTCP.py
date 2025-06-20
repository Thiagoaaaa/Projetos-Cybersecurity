import socket


def scan_ports(host, ports):
    print(f"🔎 Iniciando o scan no host: {host}")

    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)  # Timeout curto pra não travar
            resultado = s.connect_ex((host, port))

            if resultado == 0:
                print(f"✅ Porta {port} [ABERTA]")
            else:
                print(f"❌ Porta {port} [FECHADA]")

            s.close()
        except Exception as e:
            print(f"Erro ao escanear a porta {port}: {e}")


def main():
    host = input("Digite o host ou IP para escanear: ")

    # Exemplo: Scan nas portas mais comuns
    portas_comuns = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306, 3389, 8080]

    scan_ports(host, portas_comuns)


if __name__ == "__main__":
    main()