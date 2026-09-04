# Lontyle Games — Portfolio estático

Portfolio de [lontylegames.com](https://www.lontylegames.com) migrado de WordPress a un sitio 100% estático.
Coste de mantenimiento: **solo el dominio** (~10-12 €/año). Hosting gratis.

## Estructura

- `docs/` — el sitio web generado, listo para publicar (GitHub Pages sirve esta carpeta).
- `_scrape/` — herramientas de migración y contenido fuente:
  - `extracted/*.json` — contenido extraído del WordPress original (copia de seguridad).
  - `build.py` — generador del sitio. Edita aquí y regenera con `python _scrape/build.py`.
  - `extract.py`, `download_images.py`, `verify.py` — scraping y verificación.

## URLs conservadas

Todas las URLs importantes del sitio original se mantienen (importante para las
políticas de privacidad enlazadas desde Google Play / App Store):

- `/title/<juego>/` — las 7 fichas de juegos y apps
- `/<app>-privacy-policy/` y `/<app>-terms-conditions/` — 14 páginas legales
- `/how-to-play-*/`, `/our-games/`, `/about-us/`, `/contact/`
- Las URLs antiguas (`/shop/`, `/our-studio/`, `/contact-us/`, `/portfolio-category/*`…) redirigen a su equivalente.

## Cómo publicar gratis (GitHub Pages)

1. Crea un repositorio en GitHub (por ejemplo `lontylegames-web`) y sube este proyecto:
   ```
   git init
   git add .
   git commit -m "Portfolio estatico Lontyle Games"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/lontylegames-web.git
   git push -u origin main
   ```
2. En GitHub: **Settings → Pages → Build and deployment**
   - Source: *Deploy from a branch*
   - Branch: `main`, carpeta `/docs`
3. En **Settings → Pages → Custom domain** escribe `www.lontylegames.com`
   (el archivo `docs/CNAME` ya está creado). Activa *Enforce HTTPS* cuando esté disponible.

## DNS del dominio

En el panel DNS de tu registrador (o en Cloudflare si transfieres el dominio):

| Tipo  | Nombre | Valor |
|-------|--------|-------|
| CNAME | `www`  | `TU_USUARIO.github.io` |
| A     | `@`    | `185.199.108.153` |
| A     | `@`    | `185.199.109.153` |
| A     | `@`    | `185.199.110.153` |
| A     | `@`    | `185.199.111.153` |

GitHub renueva el certificado SSL automáticamente (adiós al certificado caducado).

## Para dejar de pagar los 60 €/año

1. Publica el sitio (pasos de arriba) y comprueba que `www.lontylegames.com` funciona.
2. Si el dominio está registrado con tu hosting actual, **transfiérelo antes de cancelar**
   a un registrador barato (Cloudflare Registrar ~10 €/año, Porkbun, Namecheap).
   Necesitarás el código de autorización (EPP) que te da tu proveedor actual.
3. Cancela el plan de hosting WordPress. El dominio es lo único que se renueva.

## Probar en local

```
python -m http.server 8756 --directory docs
```

Abre http://localhost:8756
