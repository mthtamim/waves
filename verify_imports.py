import os
import re

js_files = []
base_dir = os.path.join(os.path.dirname(__file__), 'js')
for root, dirs, fnames in os.walk(base_dir):
    for fn in fnames:
        if fn.endswith('.js'):
            js_files.append(os.path.join(root, fn))

broken = False
checked_count = 0
for jf in js_files:
    with open(jf, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match ES6 imports: import ... from '...' or import '...'
    imports = re.findall(r'(?:import|from)\s+[\'"]([^\'"]+)[\'"]', content)
    for imp in imports:
        # Ignore external CDN / bare specifiers like 'three'
        if imp.startswith('http') or imp.startswith('three'):
            continue
        dir_name = os.path.dirname(jf)
        target = os.path.normpath(os.path.join(dir_name, imp))
        checked_count += 1
        if not os.path.exists(target):
            print(f"BROKEN IMPORT: in {jf} -> {imp} (resolved: {target})")
            broken = True

if not broken:
    print(f'SUCCESS: Verified {checked_count} local imports across {len(js_files)} JS files. All resolved!')
else:
    print('FAILED: Some imports are broken.')