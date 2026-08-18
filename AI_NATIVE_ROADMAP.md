# HA2D — AI-Native Enterprise Roadmap

Enterprise role: **Context / Memory / Human–AI Adaptation Lab**.

HA2D's useful contribution is the attempt to model persistent context, temporary working state, semantic revision and integrity over multiple Human–AI iterations. The target is to turn those ideas into a strict memory/context provider for Cyber-Lion without allowing semantic coherence to become self-authorizing truth.

## Current conceptual assets

```text
PCE — persistent context entity
MCV — temporary memory/context
SNAP / THOUGHT / MORPH transitions
CMM — UUID + timestamp + payload + SHA256 integrity records
SMA / _neuro — semantic/adaptive process heuristics
HUD / revision viewer
```

## Target state taxonomy

Formalize four distinct states:

```text
WorkingContext
→ MemoryCandidate
→ CommittedMemory
→ SupersededMemory
```

Rules:

```text
working context != organizational memory
model output != memory commit
semantic stability != evidence
hash integrity != truth
```

## Phase 1 — CMM v2

Replace loose context records with a versioned contract containing:

```text
memory_id
entity_id
created_at
content_hash
payload/content_ref
source_event_ids
provenance
epistemic_status
sensitivity
retention_class
memory_policy_ids
candidate_event_id
supersedes
status
```

`MemoryCommitted` requires policy and provenance through Cyber-Lion MAND.

## Phase 2 — context scopes

Implement explicit scopes:

```text
agent working context
mission context
Mosaic Cell context
swarm context
enterprise memory
```

No agent receives broad enterprise memory by default.

## Phase 3 — Cyber-Lion Memory Provider

Expose bounded capabilities:

```text
memory.candidate.create
memory.read.scoped
memory.commit.request
memory.supersede
memory.integrity.verify
```

Memory writes are never read-only capabilities and always declare side effects / policy.

## Phase 4 — SMA / _neuro formalization

Treat `_neuro` as an experimental **process-state diagnostic model** for:

- semantic drift,
- context instability,
- excessive coupling,
- unresolved contradiction,
- adaptation pressure.

Outputs may prioritize review or create a `MemoryCandidate`. They cannot grant authority or claim physiological EEG measurement without actual physiological data.

## Phase 5 — revision and replay

Every memory transition emits:

```text
before state
after state
reason
source evidence
policy decision
supersession links
```

Support deterministic reconstruction of:

> What did this agent/swarm know at this moment, where did it come from, and which record later replaced it?

## Phase 6 — Human–AI HUD

HUD should distinguish visually:

```text
current working context
candidate memory
committed memory
stale/superseded memory
confidence/epistemic status
authority boundary
```

The HUD is a projection of state, not the source of truth.

## GlitchLab integration

Changes to memory schemas/policies become enterprise deltas:

```text
MODIFY_MEMORY_SCHEMA
MODIFY_MEMORY_POLICY
PROMOTE_MEMORY_CANDIDATE
SUPERSEDE_MEMORY
```

Security-critical memory changes require GlitchLab/contract validation and Cyber-Lion gate.

## Tests required

- wrong hash → reject;
- missing provenance → reject commit;
- missing memory policy → reject commit;
- cross-scope access → deny;
- replay with broken supersession chain → fail;
- stale candidate cannot silently overwrite newer committed memory;
- model cannot self-promote its output.

## Do not do

```text
SMA score == truth
semantic coherence == factual correctness
context persistence == permission persistence
hash == source provenance
implicit memory inheritance across spawned agents
```

## Enterprise reference

`https://github.com/DonkeyJJLove/ai_platform/tree/master/cyber_lion/enterprise`
