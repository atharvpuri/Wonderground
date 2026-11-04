# Run:  python build-manifest.py   (re-run whenever you add/remove games)
import os, json
files = sorted(f for f in os.listdir("games") if f.lower().endswith(".html"))
open("games.js", "w").write("window.GAMES = " + json.dumps(files, indent=1) + ";\n")
print(len(files), "games written to games.js")
