"""Uso: python3 extract_zip_tail.py recovered_archive.zip"""
from pathlib import Path
import gzip
import struct
import sys

if len(sys.argv) != 2:
    raise SystemExit('Uso: python3 extract_zip_tail.py recovered_archive.zip')
data = Path(sys.argv[1]).read_bytes()
position = data.rfind(b'PK\x05\x06')
if position < 0 or position + 22 > len(data):
    raise SystemExit('EOCD no encontrado o incompleto')
comment_length = struct.unpack_from('<H', data, position + 20)[0]
end = position + 22 + comment_length
if end > len(data):
    raise SystemExit('Longitud de comentario fuera del archivo')
tail = data[end:]
print('Bytes posteriores al EOCD:', len(tail))
if tail:
    print(gzip.decompress(tail).decode())
