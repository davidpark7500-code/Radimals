"""Inject every 48px design (designs48_*.py) into www/index.html between /*ART48_START*/ and /*ART48_END*/.
Usage: python tools/sprites/build48.py"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kit48  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
HTML = os.path.join(ROOT, 'www', 'index.html')
ALLOWED = set("#.kwsrRbnygGtcqlLfFzmvoade")


def main():
    kit48.load_all()
    data = {}
    for n in kit48.ORDER:
        rows = kit48.render48(n)
        bad = set(''.join(rows)) - ALLOWED
        assert not bad, f'{n}: unknown palette letters {bad}'
        data[n] = {'rows': rows, 'pal': kit48.PAL48[n]}
    html = open(HTML).read()
    block = '/*ART48_START*/const ART48=' + json.dumps(data, separators=(',', ':')) + ';/*ART48_END*/'
    new, k = re.subn(r'/\*ART48_START\*/.*?/\*ART48_END\*/', lambda m: block, html, flags=re.S)
    assert k == 1, 'markers not found'
    open(HTML, 'w').write(new)
    print(f'injected {len(data)} 48px sprites into www/index.html')


if __name__ == '__main__':
    main()
