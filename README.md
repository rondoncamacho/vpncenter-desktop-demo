# VPNCenter - Gestor Unificado de Clientes VPN

**Prototipo funcional** de una aplicación de escritorio para centralizar la gestión de múltiples clientes VPN en entornos corporativos.

---

![Vista del Panel](https://github.com/rondoncamacho/vpncenter-desktop-demo/blob/335c83bbb4721b71ff347ac26db90fa617a52c79/screenshots/vpn-center.png)

## 🚀 El Problema
En entornos de soporte N2, los usuarios suelen tener que abrir 4 o 5 aplicaciones distintas (FortiClient, OpenVPN, Cisco AnyConnect, etc.) para acceder a diferentes clientes. Esto ralentiza los tiempos de respuesta.

## 💡 La Solución
VPNCenter unifica el control de **5 clientes VPN** en una sola interfaz moderna desarrollada con **CustomTkinter**. Detecta en tiempo real el estado de la VPN mediante el análisis de adaptadores de red y procesos de Windows.

## 🛠️ Tecnologías
- Python 3.10+
- CustomTkinter (UI Moderna)
- Subprocess / Psutil (Gestión de procesos y servicios)
- `ipconfig` y `taskkill` nativos de Windows
- Threading (Monitoreo en background)

## ✨ Funcionalidades actuales
- ✅ Panel único para FortiClient, OpenVPN, Cisco AnyConnect, SonicWall GVC y NetExtender.
- ✅ Monitoreo en tiempo real del estado (Conectado/Desconectado) vía adaptadores de red.
- ✅ Visualización de la **IP asignada** y el **tiempo de conexión**.
- ✅ Apertura y cierre de los procesos/servicios de cada VPN con un clic.
- ✅ Panel de recursos por cliente con enlaces inteligentes que se habilitan/deshabilitan según el estado de la VPN.
- ✅ Detección y apertura automática del navegador predeterminado.

---

## 🔒 Nota de Seguridad

Este repositorio es una **demo pública**. No contiene:
- IPs reales
- Nombres de enlaces reales
- Credenciales
- Datos operativos

---

## 📬 Contacto

**Ing. Luis Rondón**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rondoncamacho/)
