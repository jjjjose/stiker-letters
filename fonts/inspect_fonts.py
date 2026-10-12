"""Read SFNT metadata without changing fonts; Python standard library only."""
from pathlib import Path
import struct
import json


def inspect(path):
    data = path.read_bytes()
    u16 = lambda offset: struct.unpack_from('>H', data, offset)[0]
    u32 = lambda offset: struct.unpack_from('>I', data, offset)[0]
    tables = {}
    for i in range(u16(4)):
        p = 12 + i * 16
        tag, checksum, offset, length = struct.unpack_from('>4sIII', data, p)
        tables[tag.decode()] = (offset, length)
    os2 = tables['OS/2'][0]
    name = tables['name'][0]
    names = []
    for i in range(u16(name + 2)):
        p = name + 6 + i * 12
        platform, encoding, language, name_id, length, offset = struct.unpack_from('>6H', data, p)
        raw = data[name + u16(name + 4) + offset: name + u16(name + 4) + offset + length]
        value = raw.decode('utf-16-be' if platform in (0, 3) else 'mac_roman', errors='replace')
        if name_id in (0, 1, 2, 8, 9, 13, 14) and (name_id, value) not in names:
            names.append((name_id, value))
    cmap = tables['cmap'][0]
    supported = set()
    for i in range(u16(cmap + 2)):
        p = cmap + 4 + i * 8
        platform, encoding = u16(p), u16(p + 2)
        if not (platform == 0 or platform == 3 and encoding in (1, 10)):
            continue
        sub = cmap + u32(p + 4)
        fmt = u16(sub)
        if fmt == 4:
            count = u16(sub + 6) // 2
            ends = sub + 14
            starts = ends + count * 2 + 2
            deltas = starts + count * 2
            ranges = deltas + count * 2
            for j in range(count):
                for cp in range(u16(starts + 2 * j), u16(ends + 2 * j) + 1):
                    delta, ro = u16(deltas + j * 2), u16(ranges + j * 2)
                    glyph = u16(ranges + j * 2 + ro + 2 * (cp - u16(starts + j * 2))) if ro else cp
                    glyph = (glyph + delta) & 0xffff if glyph or not ro else 0
                    if glyph:
                        supported.add(cp)
        elif fmt == 12:
            for j in range(u32(sub + 12)):
                start, end, glyph = struct.unpack_from('>III', data, sub + 16 + j * 12)
                supported.update(range(start + (glyph == 0), end + 1))
    test = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzÁÉÍÓÚÜÑáéíóúüñ¿¡'
    missing = ''.join(c for c in test if ord(c) not in supported)
    return {'path': path.as_posix(), 'weight': u16(os2 + 4), 'fsType': u16(os2 + 8), 'names': names,
            'spanish': {'tested': test, 'missing': missing, 'complete': not missing}, 'unicodeCodepoints': len(supported)}

if __name__ == '__main__':
    files = sorted(p for p in Path('fonts').glob('*/original/*') if p.suffix.lower() in ('.ttf', '.otf'))
    print(json.dumps([inspect(p) for p in files], ensure_ascii=False, indent=2))
