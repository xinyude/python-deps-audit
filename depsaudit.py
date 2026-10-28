"""Identify requirements lines that are not exact version pins, offline."""
import argparse
import pathlib
import re

NAME = r'[A-Za-z0-9][A-Za-z0-9_.-]*(?:\[[A-Za-z0-9_,. -]+\])?'
EXACT = re.compile(r'^' + NAME + r'\s*==\s*[A-Za-z0-9][A-Za-z0-9.!+_-]*$')
REQUIREMENT = re.compile(r'^' + NAME + r'(?:\s*(?:[<>=!~]|$))')


def audit(text):
    results = []
    for number, line in enumerate(text.splitlines(), 1):
        line = re.split(r'\s+#', line, maxsplit=1)[0].strip()
        if not line or line.startswith('#'):
            continue
        requirement = line.split(';', 1)[0].strip()
        if EXACT.fullmatch(requirement):
            continue
        category = 'unpinned' if REQUIREMENT.match(requirement) else 'unsupported'
        results.append((number, category))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=pathlib.Path)
    args = parser.parse_args()
    try:
        results = audit(args.file.read_text(encoding='utf-8'))
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f'Cannot read requirements file: {exc}\n')
    for number, kind in results:
        print(f'Line {number}: {kind}')
    if not results:
        print('All supported entries use exact version pins.')
    return int(bool(results))


if __name__ == '__main__':
    raise SystemExit(main())
