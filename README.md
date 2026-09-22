# Longtone

Tuner, metronome and practice tools for wind players.

**[▶ Try the live preview](https://mattwren88.github.io/tuner/demo/longtone-demo.html)**: the whole app running in your browser, no download needed. Feedback welcome.

**[⬇ Download the Android APK](https://github.com/mattwren88/tuner/releases)**

`www/index.html` is the whole app as a single file. It's wrapped for Android with [Capacitor](https://capacitorjs.com), and GitHub Actions builds an installable APK on every push to `main`.

## Getting it into GitHub

The repo is `mattwren88/tuner`. Put the contents of this folder at the repo root:

```
.github/workflows/android.yml
www/index.html
capacitor.config.json
package.json
.gitignore
README.md
```

**Easiest — GitHub Desktop or git:**

```sh
git clone https://github.com/mattwren88/tuner.git
# copy this folder's contents (including the hidden .github folder) into it
cd tuner
git add -A
git commit -m "Longtone app"
git push
```

**Web only:** on github.com, *Add file → Upload files* and drag in `www/`, `package.json`, `capacitor.config.json`, `README.md`. macOS hides the `.github` folder, so add the workflow separately: *Add file → Create new file*, type `.github/workflows/android.yml` as the name, paste the file's contents, commit.

## Getting the APK onto your phone

1. After you push, open the repo's **Actions** tab — "Build APK" runs automatically (about 5 minutes).
2. When it's green, open the repo's **Releases** on your phone. Each build is published there as `longtone-N.apk`.
3. Tap the APK to download, then open it. Android will ask you to allow installs from your browser the first time — allow it.

To rebuild without changing anything: *Actions → Build APK → Run workflow*.

## Updating the app

Edit the design, re-export `www/index.html`, commit, push. A new build appears in Releases. Installing it over the old one keeps your settings.

## Known limits of this build

- **The tuner uses the microphone.** On first open, Android asks for mic permission — allow it.
- **Timing uses a JS timer**, so the metronome and Changes can drift slightly. The fix is Web Audio lookahead scheduling.
- It's a **debug build**, unsigned for the Play Store. Fine for your own phone; the Play Store needs a signed release build.
- The app icon is Capacitor's default until you add one.
