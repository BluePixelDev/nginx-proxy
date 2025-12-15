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
3. Ukázka
4. Zdroje

---

<!-- header: 'NGINX' -->

# NGINX

- Vysoce výkonný bezplatný webový server, reverzní proxy a load balancer.
- Navržený pro vysokou propustnost, nízkou paměťovou náročnost a práci s velkým počtem souběžných spojení (ruský programátor Igor Sysoev, rok 2004)
- Použití: webhosting, API brány, CDN, microservices, reverse proxy vrstva.
- Napsán s cílem překonat webový server Apache

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

<!-- header: 'Architektura NGINX' -->

# Architektura NGINX

- EDA (event driven architecture) → neblokující a asynchronní
- klíčový pro spravování vícero připojení najednou

---

<!-- header: 'nginx.conf' -->

# Ukázka nginx.conf

```ruby
# Global settings

events {
    worker_connections 1024;
}

http {
include       mime.types;
    server {
        listen 80;
        server_name localhost;

        location / {
            root html;
            index index.html;
        }
    }
}

```


<!-- header: 'Zdroje' -->
<!-- _class: 'top' --->

- https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/
