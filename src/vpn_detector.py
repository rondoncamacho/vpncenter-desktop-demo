"""
VPNCenter - Detector de estado de VPNs
Monitorea adaptadores de red y procesos para determinar estado de VPNs.
"""

import subprocess
import re


def get_vpn_adapters():
    """Obtiene adaptadores de red con IP asignada."""
    try:
        result = subprocess.run(
            ['ipconfig', '/all'],
            capture_output=True,
            text=True,
            timeout=10
        )
        adapters = []
        current = None
        
        for line in result.stdout.split('\n'):
            if 'adapter' in line.lower() and ':' in line:
                current = line.strip()
            elif current and 'IPv4' in line:
                ip_match = re.search(r'([0-9]{1,3}\.){3}[0-9]{1,3}', line)
                if ip_match:
                    ip = ip_match.group(0)
                    if not ip.startswith('169.254.'):
                        adapters.append((current, ip))
        return adapters
    except:
        return []


def check_vpn_status(vpn_patterns):
    """
    Verifica si una VPN está conectada.
    
    Args:
        vpn_patterns: Lista de patrones a buscar en adaptadores.
    
    Returns:
        tuple: (conectado, ip_asignada)
    """
    adapters = get_vpn_adapters()
    for name, ip in adapters:
        for pattern in vpn_patterns:
            if pattern.lower() in name.lower():
                return True, ip
    return False, None


if __name__ == "__main__":
    # Ejemplo de uso
    patrones = ["fortinet", "openvpn", "anyconnect", "sonicwall"]
    conectado, ip = check_vpn_status(patrones)
    
    print(f"VPN: {'✅ CONECTADO' if conectado else '❌ DESCONECTADO'}")
    if ip:
        print(f"IP asignada: {ip}")
