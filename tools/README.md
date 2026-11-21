Playwright test scripts used during development. Run from the project root:
  pip install playwright pillow && playwright install chromium
  python tools/audit.py        # world integrity
  python tools/playthrough.py  # full scripted arc
  python tools/fuzz.py         # random battles + rules
  python tools/textfit.py [dir] # text box never overflows (330/390/600 px); optional screenshots
  python tools/sweep.py         # broad bug sweep (long fuzz + invariants, dialogue fit, saves, items)
  python tools/sheet.py        # renders art/all-151-radimals.png

Sprite authoring (all 101 non-legacy sprites):
  python tools/sprites/preview.py out.png Name1 Name2   # review sheet from designs.py
  python tools/sprites/build.py                         # inject designs.py into www/index.html

48px creature art:
  python tools/sprites/build48.py              # inject designs48_*.py into the game
  python tools/sprites/sheet48.py out.png Name # old | new | silhouette review sheet
