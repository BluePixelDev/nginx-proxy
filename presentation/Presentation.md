---
marp: true
theme: neobeam-ecobeam
paginate: true
footer: "**Prostředí Webu**
  **NGINX**"
---

<!-- _class: title -->

# Ukázka aplikace proxy serveru pomoci Nginx

## Jaroslav Štěpán, Ondřej Kačírek, Daniela Hušková

### 18.12.2025

---

<!-- header: 'Obsah' -->

1. Co je **NGINX**
2. Proxy
   1. Forward
   2. Reverse
3. Ukázka
4. Zdroje

---

<!-- header: 'NGINX' -->

# NGINX

- Vysoce výkonný bezplatný **webový server**, **reverzní proxy** a **load balancer**.
- Navržený pro vysokou propustnost, nízkou paměťovou náročnost a práci s velkým počtem souběžných spojení (ruský programátor Igor Sysoev, rok 2004)
- **Použití**: webhosting, API brány, CDN, microservices, reverse proxy vrstva.
- Napsán s cílem překonat webový server **Apache**

---

<!-- header: 'Proxy' -->

# Proxy

- Zástupce / Prostředník
- Jedná jménem jiné osoby, systému nebo služby
- Rozděluje se na:
  - **Forward**
  - **Reverse**

---

<!-- header: 'Proxy: Forward' -->

# Forward

- Mezi klientem a internetem
- Klient → Proxy → Internet
- **Použití**: Filtrace, Anonymizace, Bezpečnost

---

<!-- header: 'Proxy: Reverse' -->

# Reverse

- Mezi klientem a backend serverem
- Klient → Reverse Proxy → Aplikační / Backend Server
- **Použití**: Load Balancing, Cache, TLS terminace, Bezpečnost

---

<!-- header: 'Ukázka' -->

- **Docker**
- Software pro kontejnirizaci prostředí ("odlehčená virtualizace")
- **MacOS**, **Windows**, **Linux**

## ![w:400](media/docker_logo.png)

---

<!-- header: 'Zdroje' -->
<!-- _class: 'top' --->

- https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
- https://docs.docker.com/compose/gettingstarted
