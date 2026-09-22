"""Build demo/longtone-demo.html: the app inside a phone frame, for sharing."""
import pathlib
root = pathlib.Path(__file__).resolve().parent.parent
app = (root / 'www/index.html').read_text(encoding='utf-8')
frame = (root / 'tools/demo-frame.html').read_text(encoding='utf-8')
app = app.replace('<script src="capacitor.js"></script>\n', '', 1)
app = app.replace('<title>Bundled Page</title>', '<title>Longtone</title>', 1)
app = app.replace('</head>', frame + '</head>', 1)
out = root / 'demo/longtone-demo.html'
out.write_text(app, encoding='utf-8')
print(out)
