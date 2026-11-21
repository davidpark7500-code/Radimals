# Legal / IP review notes (read before submitting)

I'm not a lawyer and this isn't legal advice — have an IP attorney do a one-hour review before
launch; it's cheap relative to a takedown. Here is what's been done and what's left.

## Clean by design
- **No Nintendo/Pokémon material.** No characters, names, sprites, music, sound effects,
  maps, or text are copied. "Creature-collecting RPG" is a genre, not protected expression;
  game mechanics are not copyrightable. The app never uses the words Pokémon, Pokédex,
  Poké Ball, "gotta catch 'em all", or any franchise creature names.
- **All art is original** (hand-drawn pixel art + a parts-based generator, both written for
  this project). **All music and sound are original** synthesized chiptunes. **All text is
  original.**
- **Fonts:** in-game text uses the system font (Courier) and an original 3×5 bitmap font.
- **Code:** no third-party libraries in the game itself. Capacitor (MIT license) is the only
  dependency in the wrapper — include its license text in the app's About/Settings if you
  add one, or in the App Store "Licenses" section.

## Trademark pass already applied
Names that were identical or near-identical to registered marks were renamed while keeping
the joke. Examples: Pog → Cap, Skip-It → Anklehop, Trapper Keeper → Binderbeast,
Koosh → Fuzzpuff, Rolodex → Binder, MapQuest → Route Printout, AOL Guy → Dial-Up Guy,
Capri → Juice Pouch, Ring Pop → Candy Ring, Warheads → Sour Bomb, Tamagotchi → Pixelgodchi,
Sea-Monkeys → Brineape, Discman → CD player, Segway → golf cart, Velcro → "the rip",
Super Soaker → Pumpsoakra, Hot Pocket → Lava Pocket, Chia → Sprout, Nerf → Foam,
Hacky Sack → Footbag, Zip drive → Zapdisk, Lite-Brite → Glowpeg, Speak & Spell → Spellbot,
Bagel Bites → Minibagel, Cabbage Patch → Cabbagebaby, Slinky → Springee,
Silly Putty → Goofyputt, Sunny D → Orangeglug, Hamster Dance → Hamsterjam.
Song titles/lyrics that were quoted in NPC dialogue (boy band lines, "Macarena", "Reader
beware") were replaced with original lines. Character names that matched real TV/film
characters (Mitch, Heather) were changed.

## Residual, lower-risk references (your call)
These are generic words, descriptive terms, or allusions rather than reproduced marks, and
parody of 90s culture is the whole premise. I'd keep them, but flag them for your attorney:
- Generic terms that are also brand-adjacent: "slammer", "milk cap", "beeper/pager",
  "boombox", "brick phone", "walkie-talkie", "lava lamp", "pet rock", "moon boots",
  "glow stick", "frosted tips", "troll" (dolls), "mix tape", "juice box", "pizza bagel".
- Allusions without the mark: Goosebumpy (common word), Blockstack ("the line piece"),
  Snakebyte (phone snake game), Toastwing (flying-toaster screensaver), Shaky Cam Woods
  (found-footage horror), Mall Cop Marv, Y2Kraken.
- "Y2K" and "Radimals" are not registered marks in this class as far as I know; run a
  USPTO TESS search on TOTALLY RADIMALS before you invest in the name, and consider filing.

## Housekeeping
- Put your legal name/company in the © line (bottom of index.html, title screen, listing).
- Keep the in-app disclaimer: "All characters, names, artwork and music are original. Any
  resemblance to real products is parody and no affiliation or endorsement is implied."
- Register the copyright in the game (US Copyright Office, ~$65) once you have a final build;
  it's optional but makes enforcement far easier if someone clones it.
- App Review guideline 5.2.1 (IP) is the one a reviewer would cite; the renames above are
  specifically to avoid a reviewer seeing a famous mark in a screenshot.
