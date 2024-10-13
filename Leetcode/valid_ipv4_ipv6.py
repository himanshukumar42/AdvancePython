def check_ipv4_string(ip_string: str) -> bool:
    ip_parts = ip_string.split(".")
    if len(ip_parts) != 4:
        return False

    for octet in ip_parts:
        if not octet.isdigit() or not 0 <= int(octet) <= 256 or (octet == '0' and len(octet) > 1):
            return False
    return True


def check_ipv6_string(ip_string: str) -> bool:
    ip_parts = ip_string.split(":")
    if len(ip_parts) != 8:
        return False


def main() -> None:
    ipv4_string = "192.168.12.1"
    print(check_ipv4_string(ipv4_string))


if __name__ == '__main__':
    main()
