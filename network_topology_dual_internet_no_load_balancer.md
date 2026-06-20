# 🧩 Network Topology (Dual Internet — No Load Balancer + NAS + Printers + Camera Network)

```
[ISP 1 - Primary] ----\
                       >--- [Firewall / Router]
[ISP 2 - Backup]  ----/          |
                                 +---> VPN Server (192.168.0.x)
                                 +---> DNS Server (192.168.1.x)
                                 +---> Switch-1 (192.168.2.x)
                                 |        ├── LAN Devices (PCs, IoT, Smart TVs)
                                 |        ├── NAS (192.168.2.x)
                                 |        ├── Printers / Scanners
                                 |        └── Backup / Utility Systems
                                 |
                                 +---> Switch-2 (192.168.3.x)
                                 |        └── Kubernetes Cluster (3 Nodes)
                                 |
                                 +---> Switch-3 (192.168.4.x)
                                          ├── IP Cameras (192.168.4.x)
                                          └── Camera NAS (192.168.4.x)
```

---

## ⚙️ Layered Architecture

### 1️⃣ WAN Layer (Dual Internet)
- **Primary:** ISP1  
- **Backup:** ISP2  
- **Failover only**, managed via route tracking or ping health checks  
- No load balancing — active-passive  

---

### 2️⃣ Firewall / Router
- Core routing, NAT, and security gateway  
- Manages **DHCP**, **static routes**, and **inter-subnet access rules**  
- Enforces:
  - IP/MAC filtering  
  - Port and protocol control  
  - URL and keyword-based blocking  
- Inbound: **VPN + DNS only**  
- Optional IDS/IPS (Suricata/Snort)  
- **Traffic isolation** enforced:
  - Camera subnet (192.168.4.0/24) can **write to Camera NAS only**, no access to LAN  
  - LAN subnet (192.168.2.0/24) can **view streams via VPN or NVR dashboard**

---

### 3️⃣ VPN Server (192.168.0.0/24)
- Secure remote access to all internal zones  
- **WireGuard** recommended  
- Push routes for:
  - 192.168.2.0/24 → LAN  
  - 192.168.3.0/24 → K8s  
  - 192.168.4.0/24 → Camera network (read-only access)

---

### 4️⃣ DNS Server (192.168.1.0/24)
- Internal resolver & ad-blocker  
- Forwards to **DNS-over-TLS/HTTPS** (Cloudflare/Quad9)  
- Blocks all external port 53 traffic  

---

### 5️⃣ LAN Network (192.168.2.0/24)
- **Switch-1** handles:  
  - Laptops, desktops, IoT, TVs  
  - Shared **NAS (192.168.2.x)** for media and backups  
  - **Printers / Scanners**  
  - **Utility systems** (UPS, Smart hubs, etc.)  
- VLAN optional for NAS/printer isolation  

---

### 6️⃣ Kubernetes Cluster (192.168.3.0/24)
- **Switch-2** connected  
- 3-node internal cluster  
- Internal DNS for service discovery  
- NAS volumes mounted over **NFS/iSCSI**  
- VPN-only external access  

---

### 7️⃣ Camera Network (192.168.4.0/24)
- **Switch-3** dedicated to surveillance  
- Components:
  - **IP Cameras** – static IPs, PoE preferred  
  - **Camera NAS (192.168.4.x)** – recording storage  
    - Optional NVR software (e.g., Shinobi, Blue Iris, Frigate)  
  - Access:  
    - Direct access from LAN **denied by default**  
    - Read-only view via **VPN** or authenticated **dashboard/NVR**  
- Optional VLAN/ACL for full isolation  
