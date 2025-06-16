#!/usr/bin/env bash
#
# File: scripts/bootstrap_tractatus.sh
# Purpose: Seed an expressive Wittgenstein “Tractatus” corpus under data/tractatus

set -e

CORPUS_DIR="data/tractatus"
mkdir -p "$CORPUS_DIR"

echo "Bootstrapping corpus at $CORPUS_DIR …"

# Baseline: first proposition
cat > "$CORPUS_DIR/b1.md" << 'EOF'
# Baseline b1: The world is everything that is the case.

Wittgenstein’s opening line sets the stage: reality is not a collection of things but the totality of all facts. It invites us to think of “the world” as the structure of what is the case, laying the groundwork for a logical picture theory of language.
EOF

# Drift: shift in interpretation
cat > "$CORPUS_DIR/d1.md" << 'EOF'
# Drift d1: From static facts to dynamic language

Over time, readers have drifted from viewing the Tractatus as a strict logical atlas to understanding it as a living dialogue about how language shapes our perception of facts. The emphasis moves from immutable states of affairs to the active process of naming and mapping reality.
EOF

# Patterns: recurring themes
cat > "$CORPUS_DIR/p1.md" << 'EOF'
# Patterns p1: Fact, form, and the limits of expression

Key motifs emerge again and again:
- **Facticity**: the world as a network of atomic facts
- **Form**: the shared logical structure between language and reality
- **Silence**: the boundary where language fails and “what we cannot speak about we must pass over in silence.”
EOF

# Reflection: human commentary
cat > "$CORPUS_DIR/r1.md" << 'EOF'
# Reflection r1: How far can language carry us?

Reflect on this: if the world is entirely made of facts, and language can only picture facts up to a point, where do we find meaning beyond the logical scaffolding? Are there truths that lie forever outside the reach of propositional language?
EOF

echo "Done. Files created:"
ls -1 "$CORPUS_DIR"
