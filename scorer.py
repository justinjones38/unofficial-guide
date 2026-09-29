"""Scoring for the eval run.
"""

import questions

# The five questions, filtered to the ones actually filled in.
CASES = questions.answered()


def contains(haystack: str, needle: str) -> bool:
  """The whole scorer, in one line: is the phrase in the text?

  Case-insensitive, because "$30 of Printing" and "$30 of printing" are the
  same answer. Nothing else is normalized yet — see the note at the bottom of
  this file for the two ways that bites.
  """
  if not needle:
    return False
  return needle.strip().lower() in haystack.lower()


def judge(question, expect, answer, results) -> bool:
  """Did the ANSWER contain the phrase we decided on last week?

  This is the criterion about generation: the model had the chunks, did it
  actually say the thing. `results` is unused here on purpose — the retrieval
  criterion is `judge_retrieval` below.
  """
  return contains(answer, expect)


def judge_retrieval(question, expect, answer, results) -> bool:
  """Did RETRIEVAL put the phrase in front of the model?

  Same substring test, different haystack: the chunks instead of the answer.
  A question can fail here and pass `judge` (the model knew it anyway) or pass
  here and fail `judge` (we fetched the fact, the model dropped it) — which is
  the point of scoring them separately.
  """
  chunks = "\n".join(r.text for r in results)
  return contains(chunks, expect)


def report(rows) -> int:
  """Print one line per question and a total. Returns the number passed."""
  passed = 0
  for row in rows:
    ok = row["passed"]
    print(f"  {'PASS' if ok else 'FAIL'}  {row['question']}")
    print(f"        expected {row['expect']!r}")
    passed += bool(ok)
  print(f"\n  {passed} of {len(rows)} passed")
  return passed


if __name__ == "__main__":
  import config
  from run_eval import run_once

  print(f"{len(CASES)} questions loaded\n")

  answer_rows = []
  retrieval_rows = []
  for case in CASES:
    question, expect = case["question"], case["expects"]
    answer, results, _decision = run_once(
      question, config.TOP_K, config.THRESHOLD, config.CORPUS, "default"
    )
    answer_rows.append({
      "question": question,
      "expect": expect,
      "passed": judge(question, expect, answer, results),
    })
    retrieval_rows.append({
      "question": question,
      "expect": expect,
      "passed": judge_retrieval(question, expect, answer, results),
    })

  print("Answer contains the expected phrase:")
  report(answer_rows)
  print("\nRetrieved chunks contain the expected phrase:")
  report(retrieval_rows)
