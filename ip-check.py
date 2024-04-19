import ipaddress

def check_ip_type(ip_address):
    try:
        ip = ipaddress.ip_address(ip_address)
        if ip.version == 4:
            return "IPv4"
        elif ip.version == 6:
            return "IPv6"
        else:
            return "Unknown"
    except ValueError:
        return "Invalid IP address"

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    ip_type = check_ip_type(ip_address)
    print(f"The IP address {ip_address} is of type {ip_type}.")

