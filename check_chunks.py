"""
Criterion 4: no chunk ends mid-sentence, and no chunk is shorter than 150
characters.

Measured over every chunk the indexer produces, so it does not vary between
runs — chunking is deterministic. Run it after any change to config.CHUNK_SIZE,
config.CHUNK_OVERLAP or chunker.py:

    python check_chunks.py
"""

from statistics import median

from chunker import split_documents
from ingest import load_documents

MIN_CHARS = 150
TERMINAL = (".", "!", "?", ":", '"', ")")


def main() -> None:
    documents = load_documents()
    chunks = split_documents(documents)

    lengths = sorted(len(c.text) for c in chunks)
    short = [c for c in chunks if len(c.text) < MIN_CHARS]
    mid_sentence = [c for c in chunks if not c.text.rstrip().endswith(TERMINAL)]

    print(f"documents: {len(documents)}")
    print(f"chunks:    {len(chunks)}")
    print(f"shorter than {MIN_CHARS} chars: {len(short)}")
    print(f"ending mid-sentence:    {len(mid_sentence)}")
    print(
        "chunk length min/median/max: "
        f"{lengths[0]} / {int(median(lengths))} / {lengths[-1]}"
    )
    # A chunk can break both rules at once, so count the chunks in violation
    # rather than adding the two numbers above.
    offenders = {c.label for c in short} | {c.label for c in mid_sentence}
    print(f"chunks in violation: {len(offenders)}")


if __name__ == "__main__":
    main()
