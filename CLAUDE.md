# TOTALLY RADIMALS '98 — project brief for Claude Code

Single-file HTML game (`www/index.html`, ~200 KB, no dependencies) wrapped for iOS with Capacitor.
Everything below was decided with the owner in a long design session. Do not undo these decisions
without asking.

## What the game is
A complete Game-Boy-style creature-collecting RPG with a sarcastic late-90s theme. 151 original
"Radimals", 5 towns, 5 routes, beach/woods/caverns/snow/"The Internet", 4 Cap (badge) leaders,
a rival (Chad) fought 3 times, Y2K Tower, a boss (Y2Kraken), a legendary (Keychainos) behind a
post-game unlock, shops, storage, fishing, bike, dark caves, Mix Tapes (TMs), Sour Bombs (rare
candy), holographic shinies (1/64), leader rematches, 8 easter eggs, 3 save slots, 15 chiptune
tracks, and an App Store legal pass.

## Hard rules (legal)
- NO Nintendo/Pokémon names, art, music, text, or the words Pokémon/Pokédex/Poké Ball/"gotta catch".
- Never use a live trademark as a name. Puns must be altered (see LEGAL-REVIEW.md for the list of
  renames already done). "Pog" is a mark → we say "Cap". "Rolodex" → "Binder". Etc.
- All art/music/text must be original. Keep the in-app disclaimer and the (C) line.

## Art rules
- Creatures: ALL 151 ARE 48x48 (Nov 2026 redesign), drawn at 1x so they fill the same on-screen box
  the old 24px art did at 2x; the player's back view is the front flipped, drawn at 2x and cut off
  by the text box. Design rules (silhouette, base animal + one 90s object fused into a body part,
  baby proportions for base forms, chunky figure-like evolutions, plush test, look-alike check):
  `art/CREATURE-DESIGN-GUIDE.md`. READ IT before drawing or changing a creature.
- 48px art is authored in `tools/sprites/designs48_*.py` (one function per creature, helpers in
  `tools/sprites/kit48.py`: bigeye, blush, soft_flame, coil, plug) and injected with
  `python tools/sprites/build48.py` between `/*ART48_START*/` and `/*ART48_END*/`. Never hand-edit
  that block. Palette letters: `a` main, `d` main shadow, `b` light/belly, `c` accent, `e` metal,
  plus globals (`#` outline, `k`, `w`, `f`/`F`, `l`/`L`/`G`, `t`, `z`, `y`, `q`, `m`, `r`/`R`, `n`, `v`, `o`, `g`).
  Review: `python tools/sprites/sheet48.py out.png Name ...` (old | new | silhouette);
  roster: `python tools/sheet.py` -> `art/all-151-radimals.png`.
- The old 24px art (`MON_ART`/`HAND_ART`/`HAND_ART2`, `tools/sprites/designs.py`) is kept as a
  fallback for anything without 48px art (e.g. Glitchy) and frozen in `art/legacy-24px-art.json`.
  `drawMon()`/battle/title/Binder/party code handles either size.
- People (rebuilt Nov 2026): map sprites are 16x20 (one tile of body plus 4 rows of headroom for
  hair/hats, drawn 6px above the tile), built per direction from `P_HEAD` / `P_BODY` (3 frames:
  stand, step A, step B; right = left mirrored) plus `HATS` (hair and hats), `OUTFITS`, `ACCS`.
  Every character's look lives in `CAST` (`C(hat, skin 0-5, hair, top, legs, opts)`); shades and
  highlights are derived in `lookPal`, and `autoOutline` closes any outline gap. Never put a look
  inline on an NPC, add it to `CAST`. Face rule stays: eyes 2px with highlight, close-set, bangs.
  Battle portraits are 24x24, hand-drawn per trainer in `TRAINER_ART[look.art]` (drawn at 2x),
  coloured from the same look so map sprite and portrait match; extra prop colours in
  `TRAINER_PAL`. Each has a pose or prop that sells the trainer's joke (Chad's talk-to-the-hand
  palm, Pretzel Pete's pretzel, DJ Skatie drawn from behind because nobody has seen her face).
  `tools/audit.py` fails any trainer without a portrait. Review sheets: `tools/people_sheet.py` ->
  `art/people-sheet.png`, `tools/portrait_sheet.py [out] [names]` -> `art/trainer-portraits.png`.
  Open follow-up: the portraits are still 24px while creatures are 48px.
- Screen is 160x144 rendered at an integer scale; in-canvas text uses a 3x5 pixel font (`FONT`).
  HTML menus use the embedded 5x7 TTF "RadPix" (source: `art/radimals-pixel-font.ttf`).

## Visual/UX decisions (keep)
- Palette "Bondi": primary #1fa3e0 (--pink var name is historical), secondary #ff9a2a, lime
  #b6ff3b, navy title bg #0e1e2c. Dark grey 3D shell, recessed control wells, engraved labels,
  buttons travel down 3px on press, LED + fixed-width sound button in the header.
- Text box lives INSIDE the screen over the bottom third (true to a single-screen handheld).
  Battle layout is shifted up to leave it clear. Move menu is single-column.
- SAVE/MENU pills sit below the d-pad/AB cluster. Controls must never be cramped.
- Menu is a paper card inside the shell with tabs PARTY / BACKPACK / BINDER / HELP; HELP holds
  SETTINGS (text speed, music vol, SFX vol, battle anims, haptics; localStorage
  `radimals98_settings`), controls, type chart, and the ABOUT/legal text.
- The text box NEVER scrolls or overflows: `say()` pages long text to fit (`paginate()`), and
  `pickMenu()` shows a window of rows with ▲/▼ markers. Box height = 34% of the screen
  (`--tbh`, set in `fitScreen`). Keep menu labels short; subs are one line with ellipsis.
  Menus can take `desc:i=>text` (prompt follows the cursor, used by the shop) and `id` (test hook).
- Battle HUD: enemy info top-left (y3-22), player info right (y52-84), clear of the text box
  (canvas y≥95). Back sprite is drawn under the box.

## Audio decisions
- Web Audio only. MASTER gain for mute, with MUSICBUS and SFXBUS under it for the volume
  settings; each track plays through its own bus (`TRACKBUS` → MUSICBUS) and
  switching tracks fades+stops the old bus (fixes layering). Sound toggle is volume-only.
  iOS: resume on gesture, mute on background.
- SFX use two voices like the original handheld: `tone()` (pulse/saw/triangle) and `noise()` (filtered
  white-noise channel). Each move type has a wind-up sound (`sfxMove`); hits are 'thud', super
  effective 'crunch', crits add 'crit'; low HP plays a short 'lowhp' alarm once when crossing 25%.
- Every Radimal has its own cry, `cry(name,pitch,slow)`, generated deterministically from its name
  (evolved forms lower). Played on appear/send-out, faint (low+slow), evolution and Binder tap.

## Battle animation decisions
- Per-type particles (`spawnFx`/`drawFx`, colors in `FXCOL`), white impact flash (`whiteOf`),
  hit-pause (60ms, 110ms on super/crit), screen shake on super effective (`B.quake`), stat arrows
  (`spawnRise`), idle bob while a menu waits. All respect SETTINGS > BATTLE ANIMS.

## Game logic decisions
- Catch: `catchChance()` = rarity x ball x HP factor x level factor + small rarity floor, cap
  95%; Golden Slammer (one per game, from the Prof at 4 Caps) = 100%. Trainers' Radimals not
  catchable; legendaries are; Glitchy (#000, fishing at the pier tip) is not.
- Status effects are battle-only (cleared when a battle ends): BRN/FRZ/PAR/SOUR, rolled by the
  moves in `STATUS_FX`, type immunities in `STATUS_IMMUNE`; JUICE POUCH cures. Move list shows
  ▲/▼/✕/= once that move-type vs defender-type matchup has been seen (`G.seenEff`).
- Autosave on background/pagehide and after every warp (`autosave()`, only once a starter exists).
- Haptics: `buzz()` → Capacitor Haptics on iOS (`@capacitor/haptics`), navigator.vibrate elsewhere.
- Binder detail shows habitat (`habitat()`: map wild/fish tables, else specials, else evolution).
- Collection loop (no timers, no streaks, no pay hooks: kids play this): catch CHAINS of the same
  species raise holo odds (`holoOdds`: 1/64, 1/32 at 3, 1/20 at 6, 1/12 at 10); pager SWARM alerts
  (`maybeSwarm`, 1/7 on entering a route, lasts that visit only); BINDER milestones (`MILES`, prizes
  at 10/25/50/80/120/151 caught); 12 STICKERS (`STICKERS`, checked in `rewardsCheck()` at battle end).
- Run chance clamped 15–95%. Exp = level^3, cap 50. Evolutions at level (and via Sour Bomb).
- Gating: can't leave town without a starter; trainers refuse an empty party; rival fights must be
  done in order. Chad 1 (owner's call, Nov 2026) is NOT fought in the lab: he ambushes you the moment
  you step out of the lab with a starter (`watch` + `spotCheck()` after an outdoor warp), is a
  tutorial fight that can't be failed (`tutorial:` line, he heals you win or lose), walks off north
  afterwards (`leaveTo` + `npcLeave`) and blocks the town exit until it has happened. Chad 2 and 3
  stay in tree-walled chokepoints; bouncer needs 4 Caps; Marv needs the
  Arcade Cap; Chad 3 must be beaten before the Y2Kraken; Internet needs champion + Free Trial CD.

## Trainers
`T(id,x,y,dir,look,name,team,opts)` builds a trainer; `look` is a `CAST` entry and drives both the
map sprite and the battle portrait intro (every trainer gets one). `watch:N` = sight range;
`leaveTo:[x,y]` = walks off there after the fight; NPCs moved by a cutscene snap back on blackout.
Leaders can set `dir` and `noturn` in `LEADERS` (DJ Skatie faces the wall and never turns round).
Headless screenshots: launch Chromium with `--disable-accelerated-2d-canvas --disable-gpu` or the
game canvas can come out black even though the game is rendering fine.

## Testing (already written — reuse them)
`tools/` has Playwright scripts: `audit.py` (warps/edges/NPCs/species/items), `playthrough.py`
(scripted full arc: starter → all leaders → tower → boss → legendary), `fuzz.py` (random
battles + rule checks), `textfit.py` (text box never overflows at 3 screen widths; optional
screenshot dir arg), `sweep.py` (500-battle fuzz with invariants, every dialogue string fits,
save/load + old-save compatibility, field items, swarm expiry, shop limits), `sheet.py` (renders all 151 with hand/generated tags), `shots.py`.
Run `pip install playwright && playwright install chromium` first (in the cloud sandbox, set
`PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers` instead of installing). Every change should pass
audit + playthrough + fuzz + textfit + sweep before it ships.

## Build / ship
See README-SHIP.md (Capacitor → Xcode), PRIVACY-POLICY.md, APP-STORE-LISTING.md, LEGAL-REVIEW.md.

## Suggested first tasks in Claude Code
1. `git init`, commit as-is ("v2.0 from chat handoff").
2. Split `www/index.html` into `src/` modules + a build script that emits the single file
   (verify byte-for-byte behavior with the test scripts).
3. ~~Hand-draw the remaining sprites~~ — done (all 151, redrawn at 48px Nov 2026).
4. Optional: name change (owner is considering "Y2Kritters", "Tubulars", "Dial-Up Monsters").
