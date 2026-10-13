"""El fragmento 06 incluido es reconstruido, no recuperado de la evidencia."""
import base64
import hashlib

fragments = [
    'VEhFX0ZJTkF', 'MX1RSQUNFX1', 'JFUVVJUkVTX',
    '0VWRVJZX0ZS', 'QUdNRU5UX0t', 'FWT1FVkVSWV',
    '9BQ1RJT05f', 'TEVBVkVTX0', 'FfVFJBQ0U=',
]
message = base64.b64decode(''.join(fragments), validate=True).decode()
key = message.split('KEY=', 1)[1]
assert key == 'EVERY_ACTION_LEAVES_A_TRACE'
digest = hashlib.md5(key.encode()).hexdigest()
assert digest == '1b74e5175e672a5af64c7ea7808801e7'
print('Fragmento 06: reconstruido; procedencia sin confirmar.')
print(message)
print(f'https://{digest}.vercel.app/')
