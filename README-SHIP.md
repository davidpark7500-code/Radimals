# Totally Radimals '98 — App Store shipping guide

The game is a single self-contained `www/index.html` (no network calls, no external
scripts, no ads, no accounts). This folder wraps it as a native iOS app with Capacitor,
which is the standard way to ship an HTML5 game and satisfies App Review's
"not just a website" rule (Guideline 4.2) because everything is bundled offline.

## What you need
- A Mac with Xcode 15+ and an Apple Developer Program membership ($99/yr).
- Node 18+.
- An LLC or your legal name as the seller; a support URL and a privacy policy URL
  (see PRIVACY-POLICY.md — host it on any web page).

## Build steps
```
npm install
npx cap add ios
npx @capacitor/assets generate --ios     # makes all icon + splash sizes from resources/
npx cap sync ios
npx cap open ios                         # opens Xcode
```
In Xcode: set your Team, change the Bundle Identifier in capacitor.config.json
(now `com.holisticcreativestudios.radimals`) to your own reverse-domain id, set Deployment Target to
iOS 15, lock orientation to Portrait, then Product > Archive > Distribute > App Store Connect.

Haptics: `@capacitor/haptics` is in package.json, so `npm install` + `npx cap sync ios` registers
the native plugin. The game calls it through `window.Capacitor.Plugins.Haptics` (no bundler
needed); in a plain browser it falls back to `navigator.vibrate` or does nothing. Players can turn
it off in MENU > HELP > SETTINGS.

## App Store Connect checklist
- Category: Games > Role Playing (secondary: Adventure). Age rating questionnaire:
  "Cartoon or Fantasy Violence: Infrequent/Mild" → 9+. No IAP, no ads, no data collection.
- Privacy "nutrition label": select **Data Not Collected**. (The save file lives only in the
  device's localStorage; nothing leaves the phone.)
- Screenshots: 6.7" and 6.5" iPhone sizes required (1290×2796 / 1284×2778). Take them from
  the Simulator with Cmd+S. A short App Preview video is optional.
- Listing text is in APP-STORE-LISTING.md.
- Review notes: mention it is an offline single-player game with original characters and a
  parody 90s theme (see LEGAL-REVIEW.md) so the reviewer isn't surprised by pun names.

## Before you submit
1. Read LEGAL-REVIEW.md and decide on the residual-risk names.
2. Put your real name/company in the © line at the bottom of index.html and in
   APP-STORE-LISTING.md.
3. Test on a real device: sound starts on first tap (iOS requires a user gesture — already
   handled), safe-area padding at the bottom, and that saves survive an app restart.
4. Optional: Android is the same package — `npx cap add android`.
