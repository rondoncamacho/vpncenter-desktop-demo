"""
VPNCenter - Componentes de UI
Sistema de diseño y tarjetas de VPN con CustomTkinter.
"""

import customtkinter as ctk


class DesignSystem:
    """Sistema de diseño centralizado."""
    
    @staticmethod
    def get_colors():
        return {
            "bg_primary": "#0a0a0f",
            "bg_secondary": "#14141e",
            "bg_card": "#1e3a5f",
            "success": "#10b981",
            "error": "#ef4444",
            "text_primary": "#ffffff",
            "text_secondary": "#cbd5e1",
            "card_connected": "#1a4d3e",
            "card_disconnected": "#2d2d2d"
        }
    
    @staticmethod
    def get_fonts():
        return {
            "TITLE": ("Segoe UI", 24, "bold"),
            "SECTION": ("Segoe UI", 16, "bold"),
            "BUTTON": ("Segoe UI", 14, "bold"),
            "SMALL": ("Segoe UI", 12)
        }


def create_vpn_card(parent, title, icon="🔒", connected=False):
    """
    Crea una tarjeta visual para una VPN.
    
    Args:
        parent: Widget padre.
        title: Nombre de la VPN.
        icon: Emoji/icono.
        connected: Estado inicial.
    
    Returns:
        dict: Referencias a los widgets de la tarjeta.
    """
    colors = DesignSystem.get_colors()
    fonts = DesignSystem.get_fonts()
    
    card_color = colors["card_connected"] if connected else colors["card_disconnected"]
    status_color = colors["success"] if connected else colors["error"]
    status_text = "CONECTADO" if connected else "DESCONECTADO"
    
    # Frame principal
    card = ctk.CTkFrame(parent, fg_color=card_color, corner_radius=8)
    card.pack(fill="x", pady=5)
    
    # Header
    header = ctk.CTkFrame(card, fg_color=card_color)
    header.pack(fill="x", padx=15, pady=(10, 5))
    
    # Título
    title_label = ctk.CTkLabel(
        header,
        text=f"{icon} {title}",
        font=fonts["SECTION"],
        text_color=colors["text_primary"]
    )
    title_label.pack(side="left")
    
    # Estado
    status_label = ctk.CTkLabel(
        header,
        text=status_text,
        font=fonts["BUTTON"],
        text_color=status_color
    )
    status_label.pack(side="right")
    
    # Botones
    btn_frame = ctk.CTkFrame(card, fg_color=card_color)
    btn_frame.pack(fill="x", padx=15, pady=(5, 12))
    
    connect_btn = ctk.CTkButton(
        btn_frame,
        text="CONECTAR",
        fg_color=colors["success"],
        font=fonts["BUTTON"],
        width=120
    )
    connect_btn.pack(side="left", padx=(0, 10))
    
    disconnect_btn = ctk.CTkButton(
        btn_frame,
        text="DESCONECTAR",
        fg_color=colors["error"],
        font=fonts["BUTTON"],
        width=120
    )
    disconnect_btn.pack(side="left")
    
    return {
        "card": card,
        "header": header,
        "title": title_label,
        "status": status_label,
        "connect_btn": connect_btn,
        "disconnect_btn": disconnect_btn
    }


if __name__ == "__main__":
    # Demo de UI
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    
    root = ctk.CTk()
    root.title("VPNCenter - Demo UI")
    root.geometry("400x300")
    root.configure(fg_color=DesignSystem.get_colors()["bg_primary"])
    
    # Crear tarjetas de ejemplo
    create_vpn_card(root, "FortiClient", "🔒", connected=False)
    create_vpn_card(root, "OpenVPN Connect", "🔒", connected=True)
    create_vpn_card(root, "Cisco AnyConnect", "🔒", connected=False)
    
    root.mainloop()
