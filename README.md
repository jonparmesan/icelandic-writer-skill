# Icelandic Writer Skill for Claude Code

A Claude Code skill that enables advanced Icelandic writing with correct grammar, natural style, and automated spell/grammar checking via GreynirCorrect.

## What it does

- Writes, translates, and reviews Icelandic text with proper grammar
- Enforces rules Claude commonly gets wrong: dative sickness, indicative encroachment, V2 word order, strong/weak adjective declension
- Automatically verifies output with GreynirCorrect before presenting to the user
- Includes reference files for noun declension, verb conjugation, and syntax rules

## Structure

```
icelandic-writer/
├── SKILL.md                    # Core instructions and grammar rules (~180 lines)
├── scripts/
│   └── check_icelandic.py      # GreynirCorrect verification script
└── references/
    ├── noun-declension.md      # Paradigm tables, articles, pronouns
    ├── verb-conjugation.md     # All verb classes, subjunctive, middle voice
    └── syntax-rules.md         # V2 details, Stylistic Fronting, topicalization
```

## Installation

Copy the entire directory into your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills/icelandic-writer
cp -r SKILL.md scripts/ references/ ~/.claude/skills/icelandic-writer/
```

## Requirements

For the automated grammar checking, install GreynirCorrect:

```bash
pip3 install reynir-correct
```

## License

MIT
