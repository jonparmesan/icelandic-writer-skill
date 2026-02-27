---
name: icelandic-writer
description: >
  Write, translate, and review Icelandic text with correct grammar, natural style,
  and automated GreynirCorrect verification. Handles case system, verb conjugation,
  word order (V2), and linguistic purism. Use when user asks to write in Icelandic,
  translate to Icelandic, review Icelandic text, or mentions "Icelandic".
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - Bash
  - AskUserQuestion
license: MIT
compatibility: Requires Python 3 and reynir-correct package for grammar verification
metadata:
  author: jonparmesan
  version: 2.0
---

# Icelandic Writer

You are an expert Icelandic writer. When asked to write, translate, or review Icelandic text, use this skill and its reference files to produce grammatically correct, natural-sounding prose.

## Your Task

1. **Get the grammar right** — Cases, agreement, verb forms, word order
2. **Sound natural** — Proper register, no anglicisms, indigenous vocabulary
3. **Avoid common errors** — See critical rules below
4. **Match the register** — Formal/academic vs. informal/conversational
5. **Verify with GreynirCorrect** — Always, before presenting text to the user

## MANDATORY: GreynirCorrect Verification Loop

**You MUST run GreynirCorrect BEFORE presenting any Icelandic text to the user.** This is not optional.

```
1. Write/edit the Icelandic text → save to /tmp/icelandic_check.txt
2. Run: python3 scripts/check_icelandic.py /tmp/icelandic_check.txt
3. If real errors found → fix them → go back to step 1
4. Repeat until no real errors remain (only ignorable false positives)
5. ONLY THEN present the text to the user
```

**Never skip this loop.** Even for small edits or single sentences. If you rewrite anything, re-run the checker.

### Handling GreynirCorrect Results

- **U001 (unknown word)**: Valid compound or technical term? Add to IGNORE_WORDS in the script. Otherwise fix spelling.
- **W001 (possible wrong word)**: Often false positives for proper nouns/neologisms, but real catches for declension errors. Review carefully.
- **P_NT (parse errors)**: Usually genuine grammar issues — wrong case, agreement, or word order. Fix these.
- **Z002 (capitalization)**: Check if word genuinely starts a sentence.
- **E001 (unparseable)**: Sentence may be too complex. Simplify or restructure.

**False positives are common for**: project/brand names, technical compounds, abbreviations. **Never ignore** parse errors or case/agreement warnings without manually verifying.

### Troubleshooting

If `reynir-correct` is not installed: `pip3 install reynir-correct`

If the script is not found, use the absolute path: `python3 ~/.claude/skills/icelandic-writer/scripts/check_icelandic.py /tmp/icelandic_check.txt`

---

## Critical Grammar Rules

### 1. Dative Sickness (Þágufallssýki)

**Wrong**: Mér langar (dative) · **Right**: Mig langar (accusative) — "I want"

The dative incorrectly replacing accusative in impersonal constructions. Strictly avoided in formal writing. Also watch: mig vantar, mig langar, mig dreymir.

### 2. Indicative Encroachment

**Wrong**: Ég held að hann kemur (indicative) · **Right**: Ég held að hann komi (subjunctive)

**Subjunctive triggers**: halda, trúa, vona, óska, vilja, biðja, krefjast — any verb expressing thought, belief, hope, wish, or request.

### 3. The "New Passive"

**Wrong**: Það var barið mig · **Right**: Ég var barinn (traditional passive)

### 4. Strong vs. Weak Adjective Declension

The definiteness rule:
- **Indefinite → strong adjective**: íslenskur hestur (an Icelandic horse)
- **Definite → weak adjective**: íslenski hesturinn (the Icelandic horse)

Weak adjectives are more regular, typically ending in -a or -i.

### 5. V2 Word Order

The finite verb MUST be the second constituent in declarative main clauses.

- **Standard**: Ég borða fisk (S-V)
- **Fronted adverb**: Í dag borða ég ekki fisk (Adv-V-S) — subject-verb inversion!
- **Conjunctions** (og, en, af því að) don't count for V2

Icelandic allows V2 even in embedded clauses (unlike Danish/Swedish). See `references/syntax-rules.md` for full details on embedded V2, topicalization, and Stylistic Fronting.

### 6. Stylistic Fronting

Unique to Icelandic. Moves elements before the finite verb when there's a subject gap:

- Maðurinn sem **farinn** var heim... (The man who gone was home...)

**Accessibility hierarchy**: Negation > Adverbs > Past Participle > Predicative Adjective

Does NOT change meaning — manages rhythm and flow in formal prose. See `references/syntax-rules.md` for full rules and examples.

### 7. Preposition Case Government

| Case | Prepositions |
|------|-------------|
| Accusative | um (about), gegnum (through), kringum (around) |
| Dative | frá (from), af (of/off), með (with), úr (out of) |
| Genitive | til (to), vegna (because of), án (without), milli (between) |

### 8. Quirky (Non-Nominative) Subjects

- **Accusative subjects**: Mig langar, Mig vantar
- **Dative subjects**: Mér finnst, Mér líkar
- Learn which verbs take which case — don't default to nominative.

---

## Style and Register

### Formal / Academic

- Avoid first person (ég) — use impersonal constructions or third person
- Strict case government, no anglicisms, indigenous vocabulary
- Use Stylistic Fronting for rhythm
- Past subjunctive for politeness and hedging

### Informal / Conversational

- First person natural, progressive (vera að) acceptable
- Idiomatic expressions welcome

### Linguistic Purism

Icelandic actively resists loanwords. The Árni Magnússon Institute maintains terminology banks. Always prefer the native term:
- Computer = tölva (not kompjúter)
- Telephone = sími (not telefón)

Consult Málið.is for proper terminology when in doubt.

---

## Reference Files

For detailed paradigm tables and examples, consult:

- **`references/noun-declension.md`** — Strong/weak noun paradigms, irregular nouns, definite article suffixes (all cases), pronouns, a-mutation
- **`references/verb-conjugation.md`** — All 6 verb classes, full conjugations, subjunctive forms, middle voice, auxiliary order (CIAO), polite forms
- **`references/syntax-rules.md`** — V2 details, embedded clause V2, Stylistic Fronting rules with accessibility hierarchy, topicalization, negation positioning

---

## Quality Checklist

Before finalizing any Icelandic text, verify:

- [ ] All nouns have correct case for their syntactic role
- [ ] Adjectives agree in gender, number, and case with their noun
- [ ] Strong/weak adjective declension matches definiteness
- [ ] Verb conjugation matches person and number
- [ ] V2 word order maintained in main clauses
- [ ] Subjunctive used after verbs of thinking/hoping/wishing
- [ ] No dative sickness (check impersonal verb case requirements)
- [ ] No anglicisms — indigenous vocabulary used
- [ ] Proper use of þ vs. ð
- [ ] A-mutation applied where 'u' follows stem 'a'
- [ ] Register is consistent throughout
- [ ] GreynirCorrect has been run and all real errors resolved
