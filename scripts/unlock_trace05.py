"""Uso: python3 unlock_trace05.py trace.py packetghost.
Lee las constantes con AST; no ejecuta el proceso recuperado.
"""
import ast
import hashlib
from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit('Uso: python3 unlock_trace05.py trace.py packetghost')
tree = ast.parse(Path(sys.argv[1]).read_text())
records = next(ast.literal_eval(node.value) for node in tree.body
               if isinstance(node, ast.Assign)
               and any(isinstance(t, ast.Name) and t.id == '_R' for t in node.targets))
q = sum(i*i + 3*i + 7 for i in range(1, 18))
index = (q ^ 0x2A) & 1
body = bytes(records[index])
nonce = b'NULLTRACE5'
pad = b''
counter = 0
while len(pad) < len(body):
    pad += hashlib.sha256(sys.argv[2].encode() + b'|' + nonce
                          + counter.to_bytes(4, 'big')).digest()
    counter += 1
plain = bytes(a ^ b for a, b in zip(body, pad))
print('Registro seleccionado:', index)
print('Nonce:', nonce.decode())
print(plain.decode())
