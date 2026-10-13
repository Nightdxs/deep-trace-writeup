"""Reproduce las transformaciones textuales de TRACE 01, 07 y 08."""
import base64

def vigenere_decrypt(text, key):
    result, index = [], 0
    for char in text:
        if char.isascii() and char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shift = ord(key[index % len(key)].upper()) - ord('A')
            result.append(chr((ord(char) - start - shift) % 26 + start))
            index += 1
        else:
            result.append(char)
    return ''.join(result)

def rot47(text):
    return ''.join(chr(33 + (ord(c) - 33 + 47) % 94)
                   if 33 <= ord(c) <= 126 else c for c in text)

intercept = "5(d=*(*e{JhJ+wqH{)9H4v|E3>}D4w<E+v'F*)pE|$d?4>IF4w<F5(u9{Hll"
stage2 = vigenere_decrypt(base64.b64decode(rot47(intercept), validate=True).decode(), 'NULL')
assert stage2 == 'https://xsec-deep-trace-stage-1.vercel.app/'
print('TRACE 01 ->', stage2)

key = b'publicshadow'
parts = []
for value in ['ET0wXAorPl4tHVYNESIwACU0PQc4M1oC', 'KiIVGQ0OJRE4VjkEPBgkGwogS1U=']:
    encrypted = base64.b64decode(value, validate=True)
    inner = bytes(byte ^ key[i % len(key)] for i, byte in enumerate(encrypted))
    parts.append(base64.b64decode(inner, validate=True).decode())
stage8 = ''.join(parts)
assert stage8 == 'https://side-channel.vercel.app/'
print('TRACE 07 ->', stage8)

value = 'TkZQRksgUk9UTSA0MjAyIEVQTVNQIFFaIE5BUEdYTg=='
room = vigenere_decrypt(base64.b64decode(value, validate=True).decode()[::-1], 'NULL')
assert room == 'ADVENT OF CYBER 2024 SIDE QUEST'
print('TRACE 08 ->', room)

