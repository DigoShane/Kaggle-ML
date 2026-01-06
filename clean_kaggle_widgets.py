import json
from pathlib import Path

def clean_notebook(path):
    nb = json.loads(path.read_text(encoding="utf-8"))

    md = nb.get("metadata", {})
    widgets = md.get("widgets")

    # Remove malformed widget metadata (breaks GitHub rendering)
    if isinstance(widgets, dict) and "state" not in widgets:
        print("Removing malformed metadata.widgets")
        md.pop("widgets", None)
        nb["metadata"] = md

    path.write_text(json.dumps(nb, indent=1), encoding="utf-8")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python clean_kaggle_widgets.py notebook.ipynb")
        raise SystemExit(1)

    clean_notebook(Path(sys.argv[1]))
    print("Notebook cleaned successfully.")

