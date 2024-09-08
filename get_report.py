from pathlib import Path
from anki.collection import Collection


def get_report():
    assert Path("collection.anki2").exists(), "collection.anki2 not found, check syncing is working"
    col = Collection("collection.anki2")
    Path("report.html").write_text(col.stats().report())


if __name__ == "__main__":
    get_report()
