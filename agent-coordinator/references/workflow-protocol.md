# Workflow protocol

The parent session is the only controller. It owns repository reconciliation, requirements, the
dependency graph, assessment, refinement and splitting, write scopes, routing, execution claims,
integration, and completion. Each specialist receives one bounded executable node and returns evidence;
specialists never mutate the graph.

## Control loop

1. Inspect repository instructions, require a readable target directory, and open private workflow
   state outside the repository.
2. Record requirements and build the smallest useful DAG with one atomic `plan-apply` manifest whenever
   the initial graph is known. Forward references inside that manifest are valid; a malformed manifest
   exposes no partial plan. Use `node-add` only for a later incremental node. Give every node a complete specification,
   acceptance criteria, and rubric-v2 complexity dimensions plus objective, input, boundary, dependency,
   and acceptance ambiguity factors. Declare artifact write scopes, or an empty scope list for
   evidence-only work. Score `change_surface` as 0 exactly when the scope list is empty; the state
   owner rejects either mismatch. Scope names use NFC-normalized platform-safe segments so filesystem
   aliases cannot claim independent ownership of one artifact. Every new node also declares exact,
   non-blank `evidence`, `evidence_positive_proof_command`, and
   `evidence_negative_proof_command` fields. Make the commands repeatable and idempotent.
3. Read planning diagnostics. For every non-blocked assessable leaf, reassess `stale` work, use
   `node-refine` for unresolved or changed specification, and use `node-split` for over-budget work.
   Re-read after each revisioned mutation until all such leaves are current and `executable`. Blocked
   leaves stay diagnosed without fencing independent dispatch; a workflow-level blocker still stops it.
4. Reject capacity-stranding plans: every assessable leaf whose current recorded total or dimension
   scores reach an inclusive split threshold counts even when `stale` or `refinement_required`. It cannot be at maximum
   depth, and two unused node records remain reserved for it.
5. Record `node-observe` when material execution evidence changes remaining complexity, ambiguity,
   cost, confidence, or progress. Accept only the policy-derived projection. When `next` selects
   `reconcile_runtime`, run `graph-reconcile` with the required discovery/execution proof bundle for one
   highest-live-critical-path actionable node, or use
   `graph-expand-auto` when a bounded explicit topology is already known. Generated topology may be
   nested or an arbitrary acyclic DAG; it must remain within node, depth, history, and scope bounds.
6. Configure `judge-gate-add` before target completion when independent evidence is part of acceptance.
   A successful target waits in `judging` while every configured evidence-only judge runs. Every judge
   manifest carries the same three proof fields. Complete each with `judge-complete`; an optional loop
   creates versioned acyclic iterations until a gate passes or
   the hard iteration limit is exhausted. Never bypass a gate or loop with generic graph mutations.
7. Treat routes created by add, refine, split, runtime expansion, or a loop iteration as provisional.
   After the latest assessment and global fixed point, use `node-route-auto` to derive the existing
   router request from persisted assessment, rank only runtime-advertised candidates, and persist the
   route in the same mutation; inherit the parent route when no candidate is available. Manual
   `node-route` is an advanced override.
8. Read the compact, deterministic `next` action after each material mutation. An empty initialized
   workflow returns `plan`, never `finish`; apply a non-empty manifest before dispatch. Then inspect the tool
   surface before selecting claims. With callable delegation, select a maximal
   genuinely runnable subset of the ordered frontier: remaining capacity first, then dependency and
   write-scope safety. Without callable delegation, runtime capacity is one: select and claim one node,
   take that inline attempt terminal, and only then claim the next. Never preclaim an inline backlog.
   Order candidates by descending critical-path load, priority, and node ID. Live dependency ordering
   and remaining-work load both stop through terminal-success bridges because downstream is
   concurrently runnable. Recompute after each claim rather than assuming the original frontier remains
   safe.
9. Read `agents/roles/<role>.toml`, replacing `<role>` with each selected node's persisted role.
   Include native specification, effective requirements/outputs/
   acceptance, lineage provenance, planned evidence, and both proof commands in its task packet. Run
   `node-claim` before delegation, then
   `node-start` after a child is definitely created, and `node-complete` only after inspecting outputs
   and acceptance evidence. The state owner runs positive then negative proof while holding the mutation
   fence; `succeeded` requires exit `0`/nonzero and `failed` requires nonzero/`0`. Inline execution uses
   the same lifecycle and consumes the parent sequentially.
10. Reconcile an ambiguous delegation before inline fallback or retry. Never duplicate uncertain work.
11. Let the state owner persist the positive proof command's combined output as terminal `result` and
   its exit metadata as `proof`, then reassess affected work. Planned `evidence` remains descriptive.
   Dependency effective-output
   changes, normalized terminal disposition, result/evidence, or retry can stale direct assessable
   dependents; nonterminal status transitions cannot.
12. Repeat refinement and execution until no runnable work remains. Resolve blockers, validate the
   integrated result, confirm every declared artifact scope has attempt-scoped change evidence anchored
   to the original repository filesystem object and remains materialized, then use one
   `workflow-complete` payload to satisfy exactly the active requirements and finish atomically. Close
   the private session. Completed artifact work must be covered by a successful evidence-only review
   in its transitive dependency ancestry or the completion payload must contain a non-blank
   `review_waiver` reason. Closeout reruns every non-exempt graph record's proof commands in sorted
   node-ID order, including decomposed and superseded history, and requires every pair to prove success.
   Evidence-only nodes use the same proof contract and empty scope maps.

## Mutation boundaries and recovery

Ordinary planning keeps active work immutable. Policy-driven runtime reconciliation is the narrow
exception: it can checkpoint a consistent `running` attempt as terminal failure and then atomically
replace that leaf. It cannot touch `claimed`, `bound`, or `reconcile_required` launches. A configured
judge gate may follow a rewrite only to one completion exit. Once judgment is pending or resolved, or a
loop is active around the node, generic structural operations are fenced.

Active work is immutable to ordinary graph planning. Never refine, split, rewire, or replace a node whose launch
is `claimed`, `reconcile_required`, `bound`, or `running`. Let it reach a terminal outcome first. A
`failed` leaf with an `unclaimed` or `terminal` launch may then be refined or split, but its completed
attempt record remains part of history.

Likewise, do not rewrite a linked requirement's `text` or `source` while a resolution endpoint is
active or done. Reconcile an uncertain launch back to rewritable work before changing requirement
semantics. Requirement status and evidence may still resolve the workflow-level requirement gate.

When reconciliation returns uncertain active work to `unclaimed`, re-derive its assessment; changed
inputs make it `stale`, requiring refinement and a fresh `node-route-auto` (or advanced manual route) before retry.

Refinement atomically replaces one eligible leaf's native specification, current scopes, and assessment
inputs while first preserving its full prior effective specification and scope provenance as carried
lineage obligations. Splitting atomically replaces one leaf with children, explicitly covers every
native and carried requirement/output/acceptance obligation, carries objectives, inputs, constraints,
and non-goals to every child, preserves artifact scope provenance, and validates the final DAG. It maps,
rewires, and stales every
current rewritable assessable direct dependent. It omits direct terminal-success dependents, atomically
prunes their obsolete parent edge, and never maps them to children. A child must retain each original
prerequisite directly or through only other new children; retained terminal intermediaries do not
witness it. Recursive splitting repeats effective coverage. Supersede copies every missing source
effective obligation (native plus carried) into the replacement's carried obligations, preserves every
source prerequisite directly or transitively, and stales the replacement.
Supersede chains are always acyclic. Outside
aborted recovery, they and each carried item's combined coverage/supersede path must resolve acyclically
to live, active, repairable, or done work; dead ends and cycle-only resolution reject. Direct skip/cancel
is reserved for atomic decomposition, supersede, or abort, and replanning has no obligation-dropping
remove operation. Partial application is never visible.

A stale node is not executable even when its previous score was below every threshold. Reassessment
must incorporate the evidence that changed its digest; copying the prior rationale is not a
recalculation. Repeat until the assessment states stabilize, because one split or new piece of evidence
can make additional assessable work stale or reveal a new boundary.

Use file-backed inputs for multiline or shell-sensitive content. Mutation IDs are operation identities,
not labels to reuse. Receipts and up to 32 attempts per node remain in the atomic workflow snapshot;
explicit capacity exhaustion requires operator action instead of a second persistence layer. A revision
conflict requires a fresh read and decision; it is never solved by overwriting newer state. Controller
takeover converts every claimed, bound, or running launch to `reconcile_required`; resume does not waive
provider reconciliation. Aborting the workflow also does not make an uncertain or discovered child
terminal: `next` continues to select reconciliation until the provider outcome is terminal or absence is
proved. Only an unclaimed future node may be blocked.

Proof commands execute at the repository root with the inherited environment, a five-minute timeout,
and a 32 KiB combined-output limit per command. They may have ordinary shell side effects. A failed
node-completion or workflow-completion mutation leaves durable state unchanged, but those side effects
cannot be rolled back. Persisted receipt replay never reruns commands.


## Review convergence and user control

Default to one integrated review wave after implementation and focused validation. A new fix and
revalidation wave requires a concrete acceptance-relevant finding backed by a file, behavior, or test;
a clean review does not justify a replacement judge. Use parallel judges only for explicitly distinct
risk surfaces, merge their findings into one set, and decide from that merged evidence whether another
wave is warranted. There is no arbitrary numeric ceiling that hides a real defect, but there is a hard
convergence rule: no new concrete finding, no new wave.

A successful evidence-only `review` node covers completed artifact nodes in its transitive dependency
ancestry. If any completed artifact work remains uncovered at closeout, `next` requires
`review_waiver`; `workflow-complete` accepts that optional field only in this case and records its
non-blank reason in a durable `review_waived` event. Advanced `finish` provides the equivalent
`--review-waiver` option. Do not waive a known unresolved finding.

An explicit user instruction to stop, accept, or finish overrides speculative quality expansion. Stop
spawning immediately, reconcile or interrupt active providers, preserve completed evidence, and close
without launching another review pass.
