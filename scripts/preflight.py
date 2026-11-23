#!/usr/bin/env python3
"""Read-only summary of an easy-apply-ai CSV tracker."""
import csv
import sys
from collections import Counter
from pathlib import Path


def main():
    if len(sys.argv) != 2:
        print('Usage: preflight.py TRACKER.csv', file=sys.stderr)
        return 2
    path = Path(sys.argv[1]).expanduser()
    try:
        with path.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            required = {'company', 'role', 'posting_url', 'status'}
            if not reader.fieldnames or not required.issubset(reader.fieldnames):
                print('Tracker must have company, role, posting_url, and status columns.', file=sys.stderr)
                return 2
            rows = list(reader)
    except (OSError, csv.Error) as exc:
        print(f'Could not read tracker: {exc}', file=sys.stderr)
        return 2
    counts = Counter((row.get('status') or 'unset').strip().lower() for row in rows)
    urls = Counter((row.get('posting_url') or '').strip().rstrip('/').lower() for row in rows)
    print(f'Records: {len(rows)}')
    for status, count in sorted(counts.items()):
        print(f'{status}: {count}')
    print(f'URLs appearing more than once: {sum(1 for url, count in urls.items() if url and count > 1)}')
    print('Counts are tracker entries, not independently verified submissions.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
