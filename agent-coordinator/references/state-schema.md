# Workflow state and recovery

Coordinator stores one bounded `schema-v8` JSON document with `schema_version` equal to 8 per
workflow under `~/.agent-coordinator/workflows`. Exact schema-version-6 documents first gain the v7
runtime graph, and exact v6 or v7 documents then upgrade in memory to v8. Every pre-existing node is
permanently marked `proof_exempt=true`; the upgrade is persisted only by the next successful mutation.
Every node created after migration is proof-enforced. The state owner validates the complete document on
every read and before every persisted mutation. It rejects unknown fields, unsafe identifiers and write paths,
missing or cyclic dependencies, concurrent scope collisions, invalid transitions, inconsistent
execution state, and capacity violations.

## Runtime graph control plane

The runtime control plane introduced in schema version 7 remains one exact-key `runtime_graph` object:

- `generation`: the latest monotonically increasing adaptation generation;
- `observations`: up to 64 timestamped live observations per node;
- `projections`: the policy-derived projection from exactly the latest observation;
- `node_metadata`: task, join, or judge kind; a nested graph path of at most 32 identifiers; selected
  shape; iteration; judge target; loop; and generator;
- `gates`: completion panels keyed by target node;
- `loops`: up to 32 bounded logical feedback loops;
- `adaptations`: up to 256 ordered audit records.

The state owner recomputes every stored projection and rejects tampering. Live observations contain
0–100 progress and confidence, remaining rubric dimensions and ambiguity factors, nullable
non-negative remaining cost, up to 16 bounded signals, and a note. Progress cannot decrease. A runtime
projection may reorder remaining critical-path load or recommend `stable`, `refine`, or `split`, but it
does not overwrite the authored assessment.

Generated topology is bounded to the workflow's 128-node ceiling and remains physically acyclic.
Explicit runtime expansions accept two through sixteen fragments and an optional join. Runtime node
metadata preserves nested provenance. A configured gate can move to one replacement exit; active or
resolved gates cannot be structurally moved. Generic split/replan paths are fenced from active gates,
judge nodes, and active loops.

A gated target that otherwise succeeds uses node status `judging`, with a terminal launch and
provisional result/evidence held from downstream dependency digests. Its one through eight judges are
evidence-only `review` or `validation` nodes. Gate modes are `all`, `any`, and `quorum`; the complete
configured panel reports before resolution. A passing gate exposes the target as `done`. A failed gate
either exposes `failed` or, for an active feedback loop, materializes a new versioned target and judge
panel. Loops permit two through sixteen iterations and become `passed` or `exhausted`; no persisted
back-edge is introduced.

See `dynamic-runtime-graphs.md` for command payloads, selection rules, and adaptation invariants.

## Planning policy and node records

Workflow `conventions` contains the execution capacity settings plus these integer planning limits:

- `node_complexity_split_threshold` defaults to 6.
- `dimension_complexity_split_threshold` defaults to 3.
- `node_ambiguity_refine_threshold` defaults to 4.
- `factor_ambiguity_refine_threshold` defaults to 2.
- `max_refinement_depth` defaults to 8.

All four split/refinement thresholds are inclusive. A value at a threshold is not executable.

Every node contains `spec`, `assessment`, `lineage`, `evidence`,
`evidence_positive_proof_command`, `evidence_negative_proof_command`, `proof_exempt`, and `proof`
alongside its execution fields. Exact-key validation applies at every level. `write_scopes` contains
zero through 32 repository-relative paths;
an empty list declares evidence-only work with no repository artifact change.

For every new node, the three planned proof fields are required non-blank strings and
`proof_exempt=false`; callers cannot request an exemption. `evidence` is the planned human-readable
description of what the commands establish; lifecycle transitions never replace it, while an eligible
refinement replaces the complete planned proof contract. `result` remains a string but, for proof-enforced nodes,
is state-owner-derived exclusively from the positive command's combined standard output and error.
`proof` is either `null` or an exact object with `phase`, integer `positive_exit_code`, integer
`negative_exit_code`, and `verified_at`. Phase is `node_completion` or `workflow_completion`.
Legacy-exempt nodes have null proof commands and `proof`, retain their prior result/evidence behavior,
and are the only nodes for which terminal APIs accept caller-provided result or evidence.

`spec` contains `objective`, `inputs`, `outputs`, `constraints`, `non_goals`, `requirement_ids`, and
`open_questions`. `assessment` contains `rubric_version`, `dimensions`, `total`,
`ambiguity_factors`, `ambiguity_total`, `ambiguity_peak`, `rationale`, `input_digest`, and `state`.
Rubric version 2 dimensions are integer `breadth`, `change_surface`, `coupling`, `novelty`, and
`verification`, each 0 through 4; `total` is their derived sum. Ambiguity factors are integer
`objective`, `inputs`, `boundaries`, `dependencies`, and `acceptance`, each 0 through 4;
`ambiguity_total` and `ambiguity_peak` are derived. Assessment state is exactly `executable`,
`split_required`, `refinement_required`, `stale`, or `decomposed`.
At least one ambiguity factor is 2–4 exactly when `open_questions` is non-empty; scores 0 and 1
describe resolved facts and bounded assumptions, not unresolved implementation choices.

`lineage` contains exactly nullable `parent_id`, integer `depth`, `child_ids`, nullable `split_reason`,
and `obligations`. `obligations` contains exactly `objectives`, `requirements`, `inputs`, `outputs`,
`constraints`, `non_goals`, `acceptance`, and `write_scopes` lists. New
roots start with depth 0 and empty carried obligations; supersede may later add source obligations to a
rewritable root replacement. A successful split records all child IDs and the reason on the parent,
gives every child the parent ID and next depth, materializes its coverage assignments as carried
obligations, and makes the parent `decomposed` and ineligible for execution.

A node's effective specification and ownership are ordered unions of its native objective,
requirements, inputs, outputs, constraints, non-goals, acceptance, and write scopes with the
corresponding carried obligations.
Refinement replaces native fields and current write scopes but first adds all prior effective obligations
to carried lineage; old broad scopes are historical context, not current collision ownership. Recursive splitting covers native
plus carried items; supersede transfers every missing source effective item (native plus carried) into a
rewritable replacement's carried obligations and preserves every source prerequisite directly or
transitively. Direct skip/cancel is not a legal ordinary transition;
those statuses arise only through atomic decomposition, supersede, or abort. Obligations participate in assessment digests,
requirement invalidation, effective dependency outputs, and specialist task packets.

Supersede chains are always acyclic. Outside aborted recovery, they must terminate in resolvable work,
and each carried obligation's combined decomposition-coverage and supersede graph must have an acyclic
path to a live leaf, active launch, repairable failed leaf, or `done` resolver. A dead end or cycle-only
resolution is invalid.

`input_digest` is derived from native specification and acceptance, the planned evidence and proof
commands for proof-enforced nodes, carried obligations and linked
effective requirement text/source, write scopes, dimension and ambiguity inputs, planning conventions, and each
dependency's identity, effective outputs, normalized terminal disposition, result, and evidence. A
dependency disposition is its exact `done`, `failed`, `skipped`, or `cancelled` status, or
`nonterminal` for every other status. Nonterminal status transitions do not change the digest; output
changes, terminal disposition/result/evidence, and retry from failure can stale direct dependents.

An assessable leaf has no children and is either pending, ready, or blocked with an `unclaimed` launch,
or `failed` with an `unclaimed` or `terminal` launch. A digest mismatch makes such a leaf `stale`; stale
work cannot be ready, routed, or claimed. Changed effective requirement text/source stales every
affected assessable leaf. Those semantic fields are immutable once a referenced resolution endpoint
is active or done; status/evidence resolves the separate workflow requirement gate without redefining
completed work.

For a split, `dependent_replacements` names exactly the parent's current rewritable assessable direct
dependents; each is explicitly rewired and staled. Direct terminal-success dependents (`done`, `skipped`,
or `cancelled`) are omitted and must not map to children: their obsolete parent edge is atomically
pruned. Any other current direct dependent rejects the split.

Each node stores one specialist role. Model and effort are bounded strings supplied by the active
runtime, or `null` to inherit the parent route; Coordinator has no built-in model catalog. A non-blocked
assessable leaf with a current `executable` assessment may be routed at the global fixed point; routing
a failed leaf resets it for retry. `ready_nodes` and claim additionally require an unclaimed future
leaf with satisfied dependencies. Claiming a routed `pending` frontier leaf atomically promotes its
status to `ready` before persisting `claimed`. Textual scope overlap prevents concurrent owners; path
containment is checked for each concrete declared scope without recursively banning unrelated entries
inside a broad directory.

The workflow planning fixed point requires every non-blocked assessable leaf to have a current
`executable` assessment. Node-scoped blocked leaves remain in planning diagnostics but do not fence
independent dispatch. A workflow-level blocker still empties the frontier. At
`max_refinement_depth`, an assessable leaf cannot have current recorded at-threshold or over-threshold total or dimension
scores. State validation reserves two unused node records for every assessable leaf with those raw
scores, even if its derived assessment state is `stale` or `refinement_required`. Add, refine, and split
mutations reject candidate states that leave too few node records for the required children.

Planning diagnostics expose `split_required_nodes`, `ambiguous_nodes`, `refinement_required_nodes`,
`stale_nodes`, and `decomposed_nodes`. `ambiguity_scores` exposes every assessable leaf's factor map,
derived total, and peak instead of collapsing uncertainty to Boolean membership. Diagnostics also expose
`frontier_width`, `available_parallelism`,
`usable_parallelism`, the node-to-load map `critical_path_load`, and `dispatch_order`; graph validation
retains `ready_nodes` as an alias. Dispatch order is descending critical-path load, then priority, then
node ID. Critical-path load measures remaining work. Terminal-success and decomposed nodes contribute
zero and sever the bridge to downstream dependents; a repairable failed leaf retains its assessment
complexity. Other remaining leaves contribute their live runtime load when a projection exists, otherwise their
assessment total, plus the greatest reachable downstream dependent load. Live load combines remaining
complexity, logarithmically bounded remaining cost, and a low-confidence penalty. `usable_parallelism` is
`max_parallel - reserve`; `available_parallelism` is the smaller of frontier width and usable capacity
remaining after active launches. These diagnostics do not relax dependencies, write-scope exclusion,
reserve, or actual runtime capacity. They describe graph capacity, not guaranteed executors. The
controller must cap its selected claim batch at one when no delegation tool is callable and must finish
that inline attempt before claiming another.

Write-scope comparison first normalizes Unicode to NFC and, on Windows, rejects Win32-trimmed,
reserved, control, and special-character path segments. It then follows case behavior probed from the repository
filesystem at initialization; when probing is unavailable, the result is treated conservatively as
case-insensitive. Write-scope ordering uses live dependency reachability. Traversal stops at a `done`, `skipped`, or
`cancelled` bridge because its downstream work is concurrently runnable; overlapping scopes between
those live peers remain a collision.

Node add and split create route attempt 0; refinement sets the route attempt to the number of completed
attempts. Both forms are provisional and invalid for the next claim. After the latest assessment and
global fixed point, `node-route-auto` normally persists the next attempt number; manual `node-route` remains an advanced override. Routing a failed
retry resets its disposition to nonterminal and can stale direct dependents before claim.

Each mutation supplies a unique mutation ID and expected prior revision. A persisted receipt makes
retry reconciliation idempotent; reuse of an ID for different content and stale revisions are rejected.
Atomic replacement and durability flushing ensure readers observe a complete old or new snapshot.
Receipts stay in that snapshot up to its explicit bound; `reconcile-mutation` distinguishes a recorded
mutation from one absent from persisted state. Capacity exhaustion is explicit rather than hidden behind
a second persistence format. Proof commands execute while the same workflow mutation fence is held;
receipt replay returns the recorded response without rerunning them.

One controller session owns an epoch, while immutable `origin_session_id` scopes initialization replay.
Bearer values exist only in the caller-selected private file and private session registry, never in
workflow state or command output. A takeover advances the epoch, fences the old controller, converts
every claimed, bound, or running launch to `reconcile_required`, and requires explicit `resume`.

Launch states distinguish `unclaimed`, `claimed`, `reconcile_required`, `bound`, `running`, and
`terminal`. Persist `claimed` before execution. A delegated executor binds its returned child ID; an
inline executor binds `inline-` plus the lowercase SHA-256 digest of the request ID, keeping the
derived identifier within the state limit. An uncertain delegation becomes `reconcile_required` and
must be reconciled before binding or retrying. Nodes retain up to 32 attempt records; reaching that
explicit bound requires operator resolution rather than archival. `pending` and `blocked` nodes
must have an unclaimed launch, and a transition to `blocked` is rejected once a launch is active.

Each attempt records `scope_baseline`, mapping the node's current declared scopes to either a SHA-256
filesystem fingerprint or `null` when the scope did not exist at claim time. A successful artifact
attempt records `scope_evidence` with distinct before/after fingerprints for every declared scope.
The after value exists only for a materialized regular file or directory; directory fingerprints cover
its deterministic structure, file contents, modes, and link targets without following links. Fields
are length-framed, file contents enter as fixed-size digests, and filesystem names use their native byte
encoding, so valid trees have an unambiguous representation. Successful node completion first confirms
that every scope changed, then runs proofs, and finally re-fingerprints the scopes so permitted test or
build side effects become the recorded final state. Workflow completion rechecks that every
done artifact scope remains materialized. Repository identity combines the canonical path with the
filesystem object's stable device and file identity. Every snapshot checks that identity; POSIX
fingerprinting opens the root without following links and traverses relative to that anchored
descriptor, so replacing or redirecting the repository pathname cannot attribute outside artifacts
to an attempt. Platforms without descriptor-relative traversal check object identity before and after
the snapshot. A node with no write scopes is explicitly evidence-only,
must have `assessment.dimensions.change_surface` equal to 0, and uses empty scope maps. Conversely, a
positive change-surface score requires a scope, and any scope requires a positive score. This relation
is validated for added, refined, split, and stored nodes. The runtime never invokes or inspects a
version-control system. A successful evidence-only `review` node covers completed artifact nodes in
its transitive dependency ancestry. Closeout rejects uncovered completed artifact work unless the
controller supplies a non-blank `review_waiver`; the same atomic mutation records a `review_waived`
event naming the uncovered nodes. A waiver is rejected when review coverage is already complete. The
combined finish summary,
separator, and validation text must fit the event-size bound. Skipped and cancelled nodes do not claim artifact evidence. Only a
`skipped` decomposed parent or `skipped` superseded leaf resolves without runtime completion; a
`cancelled` node never satisfies workflow completion.

Proof commands run sequentially through the platform shell at the repository root with the inherited
environment, positive first. Each command has a five-minute timeout and a 32 KiB combined-output
limit. Timeout, launch failure, invalid UTF-8, output overflow, or blank positive output rejects the
mutation. A successful node or passing judge requires positive exit `0` and negative nonzero; a failed
node or failing judge requires positive nonzero and negative `0`. Equal-polarity pairs are inconclusive
and rejected atomically. The state owner compares only exit codes, so the negative command must express
a real failure condition rather than return a constant nonzero status. Negative output is bounded and
validated but never persisted.

Both `finish` and `workflow-complete` rerun every non-exempt graph record in sorted node-ID order,
including decomposed and superseded nodes. Every pair must prove success. Closeout replaces each such
node's `result` and `proof` with the latest positive output and `workflow_completion` metadata,
preserves historical statuses and verdicts, refreshes derived assessment digests, and rechecks artifact
scopes before marking the workflow complete. No proof waiver exists. A failure leaves durable state
unchanged, although shell-command side effects cannot be rolled back; proof commands therefore must be
repeatable and idempotent.

Read-only `list`, `status`, `context`, and `next` operations never create, lock, repair, normalize, cache, or
clean state.
