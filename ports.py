ports = [21, 22, 80, 135, 139, 443, 445, 3389]

for port in ports:
    print(f"Scanning port {port}...")
    # Here you would add the code to scan the port, e.g., using socket or a library like nmap
    # For demonstration purposes, we'll just simulate a scan result
    print(f"Port {port} is open.")