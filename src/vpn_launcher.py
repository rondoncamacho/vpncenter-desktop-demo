"""
VPNCenter - Lanzador de clientes VPN
Abre y cierra clientes VPN mediante procesos y servicios de Windows.
"""

import os
import subprocess


def open_vpn_client(install_path, exe_name):
    """Abre un cliente VPN."""
    exe_path = os.path.join(install_path, exe_name)
    
    if not os.path.exists(exe_path):
        return False, f"Cliente no encontrado en: {exe_path}"
    
    try:
        os.startfile(exe_path)
        return True, f"VPN abierta: {exe_name}"
    except:
        try:
            subprocess.Popen([exe_path], shell=False)
            return True, f"VPN abierta: {exe_name}"
        except Exception as e:
            return False, str(e)


def close_vpn_client(process_names, service_name=None):
    """Cierra un cliente VPN (procesos + servicio)."""
    closed = 0
    
    # Cerrar procesos
    for proc in process_names:
        try:
            subprocess.run(
                ['taskkill', '/F', '/IM', proc],
                capture_output=True,
                timeout=5
            )
            closed += 1
        except:
            pass
    
    # Detener servicio
    if service_name:
        try:
            subprocess.run(
                ['net', 'stop', service_name],
                capture_output=True,
                timeout=10
            )
        except:
            pass
    
    return closed > 0, f"{closed} procesos cerrados"


if __name__ == "__main__":
    # Ejemplo: Abrir FortiClient
    ok, msg = open_vpn_client(
        r"C:\Program Files\Fortinet\FortiClient",
        "FortiClientConsole.exe"
    )
    print(msg)
    
    # Ejemplo: Cerrar FortiClient
    ok, msg = close_vpn_client(
        ["FortiClient.exe", "FortiClientConsole.exe"],
        "FortiClient"
    )
    print(msg)
