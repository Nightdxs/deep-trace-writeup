"""Lee CSV de tshark: ip.id,udp.payload. Filtrar TTL 42 antes de invocarlo."""
import base64
import csv
import sys

packets = []
for row in csv.reader(sys.stdin):
    if len(row) != 2 or not row[0] or not row[1]:
        continue
    token = row[0].strip()
    ident = int(token, 16) if token.lower().startswith('0x') else int(token, 10)
    payload = bytes.fromhex(row[1].replace(':', ''))
    packets.append((ident, payload))
packets.sort(key=lambda pair: pair[0])
if [ident for ident, _ in packets] != list(range(1, 17)):
    raise SystemExit('Se esperaban exactamente IP ID 1–16; revise el filtro UDP 4444 / TTL 42.')
value = b''.join(payload for _, payload in packets)
print('Paquetes:', len(packets))
print('Base64:', value.decode())
print('Clave:', base64.b64decode(value, validate=True).decode())
