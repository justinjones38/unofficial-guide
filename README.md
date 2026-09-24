# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does
This is a retrieval Q&A system that covers campus life at a fictional university. It answers all questions that helps student deal with dining halls, dorms, course workloads, and administrative deadlines. I picked the corpus because each response is a quick answer to a question. It lets me see the quality of retrivals without too much complexiness.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** 700 characters
**Overlap:** 100 characters

The document run between 178-549 characters, so there was no need for code splitting.
<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on theregistrar's site says this plainly, and students find out from each other.

======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment:four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.

======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.

======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::fallback_split
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.

For each one, ask: could someone answer a question using only this,
without reading what came before or after?

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:**
python app.py ask "How many hours a week does CS 340 take?"
 
**Answer:**

```
  (best distance 0.243, cutoff 0.7)

CS 340 takes 6 hours a week early, and 15 hours a week in the last three weeks when the project lands (course_cs_340_workload.txt and course_cs_340.txt).

Sources retrieved: course_cs_210_workload.txt, course_cs_340.txt, course_cs_340_workload.txt, course_phys_130_workload.txt, course_stat_150_workload.txt

1 model calls this session, 631 tokens (578 in, 53 out)
(.venv) 
```

**My relevance cutoff:**
The relevance cutoff is still 0.70 because the gate verification still held 5/5 answered and 5/5 refused.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| What is the printing quota per student  | yes | 0.314 |
| How much do official transcripts cost | yes | 0.163 |
| How does pass/fail option work | yes | 0.582 |
| How many hours a week does CS 340 take? | yes | 0.243 |
| How to register for classes | yes | 0.564 |
| What is the capital of Mongolia? | no | 0.824 |
| How do I change the oil in a diesel engine? | no | 0.934 |
| Who won the 1994 World Cup? | no | 0.886 |
| What is the recommended dosage of ibuprofen for a headache? | no | 0.844 |
| How do I write a for loop in Rust? | no | 0.896 |



## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
I asked Claude for advice on running certain commands in the terminal. I was unsure of which commands to write, so I asked for advice and made adjustments based on the feedback

**2.**
I asked Claude to offer feedback on the relevance cutoff and it advised me to keep it relatively similar. 
<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

Added a switching embedding model. However, it made the question groups worse than the original one.
---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. No chunk ends mid-sentence or runs under 150 chars | 0 violations | 0 | 0 | 0 | MET |
| 5. Answer names the correct source document | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->
**Criteria 1 and 3** — produced by `run_eval.py::main`, which scores each run
with `scorer.py::judge`. Retrieval and the gate are deterministic, so the
distances are identical across the three runs; only the model call varies.

```bash
$ python run_eval.py --label before

What is the printing quota per student
  run 1: pass  (best distance 0.314)
  run 2: pass  (best distance 0.314)
  run 3: pass  (best distance 0.314)

How much do official transcripts cost
  run 1: pass  (best distance 0.163)
  run 2: pass  (best distance 0.163)
  run 3: pass  (best distance 0.163)

How does pass/fail option work
  run 1: pass  (best distance 0.582)
  run 2: pass  (best distance 0.582)
  run 3: pass  (best distance 0.582)

How many hours a week does CS 340 take?
  run 1: pass  (best distance 0.243)
  run 2: pass  (best distance 0.243)
  run 3: pass  (best distance 0.243)

How to register for classes
  run 1: pass  (best distance 0.564)
  run 2: pass  (best distance 0.564)
  run 3: pass  (best distance 0.564)

Out-of-scope questions (the gate should refuse these):
  refused  (best distance 0.825)  What is the capital of Mongolia?
  refused  (best distance 0.934)  How do I change the oil in a diesel engine?
  refused  (best distance 0.886)  Who won the 1994 World Cup?
  refused  (best distance 0.844)  What is the recommended dosage of ibuprofen for a headache?
  refused  (best distance 0.896)  How do I write a for loop in Rust?
  -> gate refused 5 of 5

Wrote results\run_2026-09-23_1937.md

```

**Criterion 1, measured properly** — the column above is `judge`, which checks
the ANSWER. Criterion 1 is about retrieval, so it needs `scorer.py::judge_retrieval`,
which runs the same substring test against the retrieved chunks instead:

```bash
$ python scorer.py

Retrieved chunks contain the expected phrase:
  PASS  What is the printing quota per student
        expected '$30 of printing'
  PASS  How much do official transcripts cost
        expected '$8'
  PASS  How does pass/fail option work
        expected 'your major'
  PASS  How many hours a week does CS 340 take?
        expected '6 hours'
  PASS  How to register for classes
        expected 'adviser hold'

  5 of 5 passed
```

**Criteria 2 and 5** — the answers themselves, from the "Real output" section of
`results/run_2026-09-23_1937.md`. Every one names a source, and the source named
is the document the fact came from:

```
Every student gets $30 of printing per semester, which is roughly 600
black-and-white pages (admin_printing_quota.txt).

Official transcripts cost $8.

Source: admin_transcript_requests.txt

Any course outside your major can be taken pass/fail, and you can declare it as
late as week eight after seeing your midterm. A pass requires a C- or better,
with a maximum of two per year and eight across a degree
(*admin_pass_fail_option.txt*).

CS 340 takes 6 hours a week early, and 15 hours a week in the last three weeks
when the project lands.

Sources: `course_cs_340_workload.txt` and `course_cs_340.txt`

To register for classes, you must first have your adviser hold lifted, and you
should book your adviser two weeks out because they get busy. Registration times
are then staggered by credit hours. (Source: `advising_registration.txt`)
```

**Criterion 4** — measured over every chunk the indexer produces, via
`ingest.py::load_documents` and `chunker.py::split_documents`:

```
documents: 88
chunks:    88
shorter than 150 chars: 0
ending mid-sentence:    0
chunk length min/median/max: 178 / 309 / 549
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | `judge_retrieval` found the expected phrase in the retrieved chunks for all 5 questions. Retrieval is deterministic, so this is the same on every run. Not close: the target was 4 of 5 and the weakest match was "how does pass/fail work" at distance 0.582, still well inside the 0.70 cutoff. |
| 2 | Every answer names a source | MET | Read all 15 answers in the "Real output" section of the run log and counted the ones naming a filename: 15 of 15, so 5/5 on each run. The target was 5 of 5 with no margin, so I checked each run separately rather than sampling. |
| 3 | Gate stops out-of-corpus questions | MET | `check_out_of_scope` refused 5 of 5. Closest out-of-scope question was 0.825 against a 0.70 cutoff, so nothing was near the line. |
| 4 | No chunk ends mid-sentence or runs under 150 chars | MET | Counted across all 88 chunks, not per run — chunking doesn't change between runs. 0 chunks under 150 characters (shortest was 178) and 0 ending on anything other than terminal punctuation. |
| 5 | Answer names the correct source document | MET | Stricter than criterion 2: I checked the named file actually contains the fact, not just that a filename appeared. All 15 correct. The one at risk was CS 340, where nine near-identical workload files could be confused — it cited `course_cs_340_workload.txt`, the right one, on all three runs. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
