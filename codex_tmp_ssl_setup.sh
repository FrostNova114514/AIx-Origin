#!/usr/bin/env bash
set -euo pipefail

DOMAIN="aixorigin.innoai.org.cn"
WEBROOT="/www/wwwroot/aixorigin/frontend/dist"
VHOST="/www/server/panel/vhost/nginx/html_aixorigin.innoai.org.cn.conf"
HTTP_CONF="/tmp/codex_tmp_nginx_http.conf"
SSL_CONF="/tmp/codex_tmp_nginx_ssl.conf"

mkdir -p "$WEBROOT/.well-known/acme-challenge"
cp "$HTTP_CONF" "$VHOST"
nginx -t
/etc/init.d/nginx reload || /www/server/nginx/sbin/nginx -s reload

certbot certonly \
  --webroot \
  -w "$WEBROOT" \
  -d "$DOMAIN" \
  --agree-tos \
  --register-unsafely-without-email \
  --non-interactive \
  --deploy-hook '/etc/init.d/nginx reload || /www/server/nginx/sbin/nginx -s reload'

cp "$SSL_CONF" "$VHOST"
nginx -t
/etc/init.d/nginx reload || /www/server/nginx/sbin/nginx -s reload

crontab -l 2>/dev/null | grep -v 'certbot renew' > /tmp/codex_cron || true
printf '%s\n' '0 3 * * * /usr/bin/certbot renew --quiet --deploy-hook "/etc/init.d/nginx reload || /www/server/nginx/sbin/nginx -s reload"' >> /tmp/codex_cron
crontab /tmp/codex_cron

certbot renew --dry-run
openssl s_client -connect "$DOMAIN:443" -servername "$DOMAIN" </dev/null 2>/dev/null | openssl x509 -noout -subject -issuer -dates
