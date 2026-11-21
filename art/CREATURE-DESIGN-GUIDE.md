# Radimal design guide (Nov 2026)

What made the original 1996 handheld creatures memorable, translated into rules for Radimals.
Principles only: nothing here copies any existing creature, name, or sprite (see CLAUDE.md legal rules).

## What the research says worked

1. **Silhouette first.** Constraint forced every design to read in solid black at tiny size.
   If the blacked-out shape isn't recognizable, the design isn't done.
2. **One familiar base + one twist.** Most were a real animal (rat, bat, turtle, fox) bent by one
   striking feature (six tails, a shell cannon, a plant on the back). Objects-with-faces were rare.
3. **Few colors.** One main color, a lighter or darker accent, a contrasting marking (light belly,
   back stripes). Two to four colors total.
4. **Eyes carry the personality.** Sharp eyes = dangerous, round = friendly, odd = otherworldly.
   A small shared set of eye styles makes the roster feel like one world.
5. **Strength reads from the look.** Designers judged "how strong does it look?" before stats.
   Evolutions grow bigger, heavier, more confident, and keep one signature feature.
6. **One defining quirk, and keep a flaw.** The art lead's own rule: strip anything "too cool",
   keep an imperfection that makes it memorable (freckles, a blank stare, a dopey pose).
7. **Pose and back view.** Front sprites were 3/4 views with a pose, not flat mugshots.
   Back sprites made players "want to protect them".
8. **Mix cute and tough** across the roster so collecting and trading feel varied.
9. **Pixel budget.** Original battle sprites had roughly 40 to 56 pixels of width. Ours have 24,
   less than half. [Likely: exact original canvas sizes vary by source]

## Audit of our current 151

Strong: the names and dex jokes. Most concepts already pair a 90s thing with an animal
(Dialupine = dial-up + lupine, Floppuss = floppy + platypus). The drawings mostly don't deliver it.

- **About half are an object with a face** (Floppuss, Cassettle, Brickphone, Glowpeg, Chatbrat,
  Dunktank, Cartrolith, Spellbot...). No anatomy, so no pose and no personality beyond the face.
- **Silhouettes are mostly rectangles and circles.** The starters fail the black-silhouette test
  outright: all six read as boxes.
- **All front-facing, symmetric mugshots.** No 3/4 views, no action.
- **Evolutions are mostly "same thing, bigger and redder"** (Hotpockit to Scorchpockit,
  Pumpsoakra to Hydrosoakra, Glowpeg to Glowpegger) and every stage uses the same 24px box,
  so the final form doesn't look stronger.
- **Type doesn't read from the design** for several: Orangeglug/Glugdeluxe (a drink), Minibagel/
  Pizzarolla, Sourbomb are Fire; Dialupine is Fire with no visible fire logic beyond the color.
- **Busy palettes** on a few (Fuzzpuff, Fuzznado, Spicearachnid).

## Radimal rules (apply to every redesign)

1. **Base animal + one 90s object fused into ONE body part** (the floppy disk IS the platypus bill;
   the phone cord IS the wolf tail). Not an object wearing a face.
2. **Type shows on the body:** Fire = flame on head/back and sharp shapes; Water = smooth curves,
   fins, webbing, blues; Grass = leaves as hair/fur; Techno = LEDs, plugs, screens; Rock = blocky
   mass; Air = wings or loft; Bug = segments and antennae; Basic = soft round shapes.
3. **Passes the silhouette test** at 1x, recognizable from the shape alone.
4. **3/4 view facing LEFT**, with a pose (sitting, prowling, waving, arms crossed).
5. **Palette:** `a` main, `d` main shadow, `b` light/belly, `c` accent, plus globals. Max one extra
   accent. Outline `#`.
6. **Face with attitude:** pick from wide / tall / big eyes + brow; one mouth gag (scream, smirk,
   fangs, tusks, grin).
7. **Line signature:** one feature carries through every stage (Dialupine LEDs, Floppuss bill,
   Trollsprout gem belly) and grows with it.
8. **Evolution reads as stronger:** larger footprint, more confident pose, the joke escalates
   ("the hair is now load-bearing" becomes an actual tree with a bird nest).
9. **Keep one flaw** that makes it lovable (the smirk, the never-working luck, the dial-up scream).

## Make people want one (plush / figure appeal) — added after pilot v1

Pilot v1 fixed shape but leaned "cool": angry brows, fangs, scowls. That reads as an enemy, not
something you want to hug. Research on cuteness and toys:

- **Baby proportions trigger "cute".** Lorenz's baby schema: big head, big eyes, high forehead,
  round cheeks, small nose and mouth, short thick limbs, plump body. A controlled study found faces
  with more of these traits were rated cuter and made people want to take care of them.
- **Kawaii practice:** big head on a small round body, organic ovals not perfect circles, slight
  asymmetry or a 3/4 angle, a texture or highlight, and a name plus backstory.
- **Toys need a reason to collect and a "promise in the premise":** an accessory or gear, a
  feature that suggests play, and a world that supports many characters.
- **Plush survives only simple shapes:** flat color zones (no gradients), thick parts (thin horns,
  antennae, tails flop), a silhouette that works from every side, eyes big enough to embroider,
  a body that can sit or stand on its own.
- **Personality sells:** Squishmallows' team designs every character "with purpose", with a short
  relatable background people get invested in.

### Rules added

10. **Base forms are babies:** head about half the total height, eyes 4x5 with a 2x2 highlight set
    LOW and WIDE on the face, tiny mouth, blush, stubby limbs, plump body. No angry brows.
11. **Evolutions are action figures:** chunky legs that could stand on a shelf, confident (not mean)
    face, keep big eyes, the signature accessory grows (plug held up like a trophy, CD as a shield).
12. **One huggable accessory per line** that could be a separate toy piece: the phone-cord plug,
    the floppy bill, the gem belly button, the bird in the nest.
13. **Plush test:** no needle-thin parts (flames are soft curls, cords are chunky), 2 to 4 flat
    colors, would still make sense from the back.
14. **Lovable flaw in the face or pose**, never meanness: the one goofy fang, the bent disk corner,
    the sleepy giant who never moves, the troll whose luck never works.
15. **Give it a one-line personality** in the Binder entry that a kid would repeat.

v2 lives in `tools/sprites/pilot48v2.py`; `pilot_sheet.py` shows now / v1 / v2 / silhouette.

### More sources
- [Baby schema in infant faces induces cuteness perception (Glocker et al., 2009)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3260535)
- [10 tips for kawaii character design (Creative Bloq)](https://www.creativebloq.com/character-design/10-tips-kawaii-character-design-514833)
- [Character building: designing for toy potential (Mojo Nation)](https://www.mojo-nation.com/character-building/)
- [Squishmallows' brand SVP on designing with purpose (Mojo Nation)](https://mojo-nation.com/?p=36445)
- [Why a 2D sketch can fail in 3D: merch checklist](https://dev.to/mingyue_li_dcb369b1a73125/the-2026-collector-grade-merch-checklist-why-your-2d-sketch-might-fail-in-3d-22km)

## Pilot (tools/sprites/pilot48.py)

Six starter-line redesigns at 48x48, shown next to the current sprites with silhouettes:
`python tools/sprites/pilot_sheet.py out.png`. A 48px sprite drawn at 1x fills exactly the
same on-screen box as today's 24px sprite drawn at 2x, so the enemy layout doesn't move.
Not wired into the game yet.

## Rollout if approved

1. Engine: support 48px front sprites (`MON_ART48`) with a `d`/`e` palette slot; fall back to
   the 24px art for anything not redrawn yet, so the game stays shippable at every step.
   Decide the player back sprite (48px at 1x, or a separate chunky back view).
2. Redraw in priority order: starters, early routes (what players meet in the first 30 minutes),
   rival/leader teams, legendaries and box art, then the rest.
3. Re-concept the object-with-a-face entries onto a base animal; fix type/design mismatches.
4. Update CLAUDE.md art rules (24x24 becomes 48x48), roster sheet, sheet.py, tests.

## Sources
- [Sugimori & Masuda on building Gen 1 (Dr. Lava translation)](https://lavacutcontent.com/sugimori-masuda-developer-interview/)
- [Ken Sugimori 2000 interview, translated (Well Played)](https://www.well-played.com.au/pokemon-artist-ken-sugimori-talks-design-in-newly-translated-2000-interview/)
- [Sugimori wants designs to be as memorable as possible (Nintendo Life)](https://www.nintendolife.com/news/2018/07/ken_sugimori_wants_pokemon_designs_to_be_as_memorable_as_possible)
- [Evolution of designs, Gen 1 (Game Developer)](https://www.gamedeveloper.com/design/evolution-of-pokemon-designs-gen-1)
- [What artists can learn from 30 years of character design (Creative Bloq)](https://www.creativebloq.com/art/digital-art/what-artists-can-learn-from-30-years-of-pokemon-character-design)
- [How the Gen 1 designs made a great first impression (GamerBraves)](https://www.gamerbraves.com/how-the-gen-1-pokemon-designs-made-a-great-first-impression/)
- [A fan artist's design recipe (Nintendo Life)](https://www.nintendolife.com/news/2022/11/random-fakemon-artist-details-the-recipe-for-what-pokemon-should-look-like)
