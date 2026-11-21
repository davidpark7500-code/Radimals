# Sprite status: all 151 hand-drawn

- 50 original sprites live as raw 24x24 strings in `MON_ART` / `HAND_ART` inside `www/index.html`.
- The other 101 are authored in `tools/sprites/designs.py` (one function per creature, composed from
  shapes with an automatic outline) and injected by `python tools/sprites/build.py` into the
  `/*HAND_ART2_START*/ ... /*HAND_ART2_END*/` block of `www/index.html`. Edit the Python, rebuild — never
  hand-edit the generated block.
- Review a set: `python tools/sprites/preview.py out.png Name1 Name2 ...`
- Full in-game roster sheet: `python tools/sheet.py` -> `art/all-151-radimals.png`.
- The old `buildArt()`/`GEN` part generator is no longer used for any art (GEN still supplies stats/learnsets).

Quality bar for any new or revised sprite: clear silhouette, a face with attitude, a prop that sells the pun. No blobs.
