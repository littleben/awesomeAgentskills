---
name: coordinator
description: Coordinate complex work through durable specialist workflows that delegate when available and execute inline otherwise.
---

# Coordinator

Use Coordinator when a task benefits from bounded specialist passes, durable recovery, or explicit
dependency and write-scope control. The parent task remains the sole controller: it owns requirements,
graph mutations, integration, reconciliation, and completion. A specialist owns only its assigned node.

## Start

Resolve this file's directory as `SKILL_DIR`. Keep Coordinator code and role profiles inside that
directory. Never copy them into the target repository, edit Codex settings, or register custom agents.
The only persistent external Coordinator-owned data is private runtime state under
`~/.agent-coordinator`; initialization creates and removes one private-name case-behavior probe.

Inspect repository instructions, confirm the target is a readable directory, and open a controller
session with Python 3.11 or newer:

```sh
python3 "$SKILL_DIR/scripts/coordinator_state.py" session-open \
  --repo /absolute/repository --session-file /private/path/session.json --json
python3 "$SKILL_DIR/scripts/coordinator_state.py" init \
  --repo /absolute/repository --task-file /private/path/task.txt \
  --session-file /private/path/session.json --mutation-id init-001 --json
```

Keep the returned workflow ID and revision. Every ordinary mutation requires the private session file,
a never-reused mutation ID, and the exact observed prior revision. If a persistence outcome is uncertain,
run `reconcile-mutation` with the same mutation ID before deciding whether to retry.

## Build a bounded graph

Create the smallest useful dependency graph. Prefer one file-backed `plan-apply` mutation for the
initial requirements and nodes: it validates the complete manifest, permits forward dependency
references inside that manifest, and publishes either the whole plan or none of it. The top-level JSON
object has exactly `requirements` and `nodes`; each requirement has `id`, `text`, and `source`, and each
node uses the same strict fields as a split child. Use `node-add` only for a genuinely incremental node
or as an advanced fallback.

```sh
python3 "$SKILL_DIR/scripts/coordinator_state.py" plan-apply \
  --workflow-id WORKFLOW --session-file /private/path/session.json \
  --mutation-id plan-001 --expected-revision REVISION \
  --plan-file /private/path/plan.json --json
```

Each node has an execution specification, acceptance criteria, zero or more repository-relative write
scopes, one role, a rubric-v2 assessment, descriptive `evidence`, and positive and negative proof
commands. The positive command must demonstrate the accepted behavior and print non-blank output; the
negative command must independently detect its absence, not merely exit nonzero unconditionally. Make
both commands repeatable and idempotent because they run
at node completion and again at workflow closeout. Valid stages are `architecture`, `design`,
`documentation`, `fix`, `implementation`, `integration`, `research`, `review`, and `validation`.
Omit write scopes only for evidence-only work that will not change repository artifacts, and score its
`change_surface` as 0. Any positive `change_surface` requires at least one scope, and any declared
scope requires a positive `change_surface`; the state owner rejects mismatches. The workflow's
schema-v8 conventions default `node_complexity_split_threshold` to 6,
`dimension_complexity_split_threshold` to 3, `node_ambiguity_refine_threshold` to 4,
`factor_ambiguity_refine_threshold` to 2, and `max_refinement_depth` to 8. Thresholds are inclusive:
reaching one requires another planning mutation. Independent nodes may not overlap scopes.

```sh
python3 "$SKILL_DIR/scripts/coordinator_state.py" node-add \
  --workflow-id WORKFLOW --session-file /private/path/session.json \
  --mutation-id add-api-001 --expected-revision REVISION \
  --node-id api --title "Implement API" --stage implementation --priority 70 \
  --write-scope src/api --role implementer \
  --objective "Implement the accepted API behavior" --output "Working API implementation" \
  --acceptance "Focused API tests pass" --breadth 2 --change-surface 2 --coupling 1 \
  --evidence "Focused API tests demonstrate the accepted behavior" \
  --evidence-positive-proof-command "npm test -- --runInBand api" \
  --evidence-negative-proof-command "test ! -f src/api/index.ts" \
  --novelty 1 --verification 2 \
  --ambiguity-objective 0 --ambiguity-inputs 0 --ambiguity-boundaries 0 \
  --ambiguity-dependencies 0 --ambiguity-acceptance 0 \
  --complexity-rationale "Known owner-layer change with focused integration evidence" \
  --rationale "Initial role; route again immediately before execution" --json
```

`node-add` records an invalid provisional route attempt. It does not authorize a claim, even when a
role, model, or effort was supplied; run `node-route-auto` after the latest assessment, or use manual `node-route` only as an advanced override.

Before routing anything, repeatedly inspect planning diagnostics and repair every non-blocked
assessable leaf whose assessment is `stale`, `refinement_required`, or `split_required`:

1. Reassess stale work against the current specification and effective obligations; requirements;
   dependency effective outputs, normalized terminal disposition, result, and evidence; scopes; and
   planning conventions. Use `node-refine --node-id ...
   (--refinement-json|--refinement-file)` to atomically persist clarified or reassessed inputs. A
   refinement of a schema-v8 node replaces all three planned proof fields as part of that exact payload.
2. Resolve ambiguity through concrete inputs and refine the leaf. Resolve or remove every open question
   before launch; keep bounded non-decision uncertainty in the ambiguity score. A factor of 2–4 must
   identify at least one open question, and every open question requires a factor of at least 2.
3. Decompose over-budget work with `node-split (--plan-json|--plan-file)`. The plan must cover every
   native and carried requirement, output, and acceptance obligation; map every current rewritable
   assessable direct dependent for explicit rewiring and staling; preserve each original prerequisite
   directly or through only other new children; preserve a valid DAG; respect depth; and make measurable
   complexity progress. Omit direct terminal-success dependents—their obsolete parent edge is atomically
   pruned, and they must not map to children. Retained terminal intermediaries do not witness a
   prerequisite.
4. Re-read the new revision and repeat until every non-blocked assessable leaf is current and
   `executable`. This global pre-route loop must reach a fixed point, not merely repair the next
   dispatch candidate. Blocked leaves stay in diagnostics but do not fence independent work; a
   workflow-level blocker still stops dispatch.

At `max_refinement_depth`, an assessable leaf's current recorded total and dimension scores must be
bounded. State capacity reserves two unused node records for every assessable leaf whose raw scores are
at or beyond policy, even when its assessment is `stale` or `refinement_required`. `node-add`, `node-refine`,
and `node-split` reject capacity-stranding candidate states.

Supersede chains are always acyclic. Outside aborted recovery, every effective obligation must also have
an acyclic path through recursive decomposition coverage and supersede to live, active, repairable, or
done work; reject dead ends and cycle-only resolution. Supersede transfers the source's full effective
obligations (native plus carried) and every source prerequisite, directly or transitively. Direct
skip/cancel is reserved for decomposition, supersede, or abort.

Never refine or split active work. A failed leaf with an `unclaimed` or `terminal` launch may be
repaired without erasing its attempt record. Dependency evidence or a requirement text/source change
can stale assessable leaves. Requirement semantics are immutable while referenced execution is active
or completed; first reconcile uncertain launches back to `unclaimed`. Run the same fixed-point loop
after each semantic mutation. See
`references/complexity-accounting.md` for the rubric, payloads, and split rules.
`node-refine` cannot rescore a current `split_required` leaf below policy; that leaf must use
`node-split`.

Only a non-blocked leaf with a current `executable` assessment at the global fixed point may be routed,
returned as ready, or claimed. `node-add`, `node-refine`, and `node-split` leave the next route attempt
invalid. Normally run `node-route-auto`: it derives the router's 1–5 request from the persisted
assessment, validates caller-supplied `criticality` and `determinism`, calls the existing selector, and
persists the selected route in one fenced mutation. Supply `--profile-file` only from the active
runtime's advertised candidates. Never invent a catalog, probe models, or author a second complexity
score. With no candidate catalog, model and effort remain unset so execution inherits the parent route.
Keep manual `node-route` only for an explicit advanced override. See `references/model-routing.md`.

```sh
python3 "$SKILL_DIR/scripts/coordinator_state.py" node-route-auto \
  --workflow-id WORKFLOW --session-file /private/path/session.json \
  --mutation-id route-NODE-001 --expected-revision REVISION --node-id NODE \
  --criticality 3 --determinism 4 --json
```

A claim may consume a routed `pending` frontier leaf directly; the state owner atomically promotes it
to `ready` before recording `claimed`, so `pending+claimed` is never persisted. Scope overlap is checked
from NFC-normalized, platform-safe repository-relative ownership using case behavior detected from that
repository. At completion, each declared path and its ancestors must stay inside the original
repository filesystem object; unrelated pre-existing entries below a declared directory are allowed.

## Execute adaptively

After every material mutation, call read-only `next --workflow-id WORKFLOW --json`. Treat its compact
action as an oracle for the next legal action class, then supply the required semantic inputs; it never
contains secrets or shell-escaped commands. On a newly initialized workflow with no nodes, `plan`
means apply one non-empty `plan-apply` manifest rather than attempting closeout. Planning diagnostics
order ready work by descending critical-path load, then priority, then node ID. Runtime projections
replace a node's static load only for remaining-work ordering; they never overwrite its authored
assessment.

Record `node-observe` only when execution reveals material new evidence: current progress, remaining
five-dimension complexity, remaining ambiguity, cost, confidence, signals, and a note. The state owner
derives `stable`, `refine`, or `split`; never author or edit that recommendation. Progress is monotonic.
When `next` returns `reconcile_runtime`, run `graph-reconcile` with an exact discovery/execution proof
bundle to adapt exactly one highest-live-load actionable leaf and then inspect the new graph. It may
checkpoint running work and replace it with a bounded discovery → execution pipeline. For a known
topology, use `graph-expand-auto`; auto mode may
choose pipeline, parallel, fan-out/fan-in, map/reduce, diamond, or arbitrary acyclic DAG. Keep explicit
fragments bounded and deterministic. Nested expansions preserve graph paths. Persisted dependencies
must remain acyclic; recurrence uses versioned iterations, never back-edges.

Attach `judge-gate-add` to live leaf work before it completes when acceptance requires independent
review or validation. Judge manifests are evidence-only and use `review` or `validation` stages. A
successful target then enters `judging`; route, claim, start, and finish every configured judge, using
`judge-complete` for its `pass` or `fail` verdict. The gate resolves only after the full panel reports.
An optional loop may materialize another acyclic target-and-judge iteration up to its hard limit.
A configured gate follows a runtime rewrite only when the rewrite has one completion exit; add a join
before expanding gated work into multiple branches. Do not use generic split or replan operations to
bypass active gates, judge nodes, or feedback loops. See `references/dynamic-runtime-graphs.md`.

Inspect the current tool surface before selecting a claim batch. If no delegation tool is callable,
runtime capacity is one: select and claim exactly one inline node, then take it terminal before claiming
another. Never preclaim work for later inline execution. Otherwise fill all genuinely available
delegation capacity with independent nodes from the ordered frontier, subject to dependencies,
write-scope exclusion, the workflow maximum, and reserve. Recompute the safe frontier after every claim
or result. Terminal-success bridges stop live dependency ordering and remaining-work critical paths;
downstream is concurrently runnable, while repairable failed work retains its complexity. Do not leave
a real slot idle when a compliant leaf can run. For every selected node:

1. Read `agents/roles/<role>.toml` from `SKILL_DIR`, replacing `<role>` with the node's persisted role;
   for example, an `implementer` node uses `agents/roles/implementer.toml`. Build one task packet
   containing its `description`
   and `developer_instructions` verbatim, plus the repository, node objective, dependencies, write
   scopes, native specification, effective requirements/outputs/acceptance, lineage provenance,
   planned evidence and both proof commands, and a ban on graph mutation. Carried obligations remain
   acceptance commitments;
   do not hide them behind the child's narrower native fields. This packet is the specialist profile;
   do not depend on a globally registered agent.
2. Confirm the current tool surface. Treat delegation as enabled only when a subagent creation or
   delegation tool is callable. Do not infer it from a settings file or a configured maximum.
3. Run `node-claim` before execution. It atomically promotes a routed frontier node when necessary,
   fingerprints its scopes, and returns a deterministic request ID plus a suggested child ID. If
   delegation is enabled, pass the task packet in the tool's task/message argument. Pass the routed
   `model` and map `effort` to the tool's reasoning-effort argument only when each value is set and the
   tool schema accepts it; otherwise omit it so the child inherits its parent.
4. After a child is definitely created, run `node-start --child-id RETURNED_ID`; this atomically binds
   that unique child and marks the attempt running. If no delegation tool is callable, or a call
   definitively creates no child, bind `inline-` followed by the lowercase SHA-256 digest of the request
   ID and execute the same packet in the parent. Inline execution is a full node attempt, not weaker
   acceptance.
5. If a delegation result could have created a child, use the low-level reconciliation fields of
   `node-update` to persist `reconcile_required` and inspect the provider edge. Bind the existing child
   if found; bind the inline executor only after proving no child exists. Never duplicate uncertain work.
6. Inspect actual outputs and run the node acceptance checks. Then use `node-complete` with `succeeded`
   or `failed` and optional actual cost. While holding the mutation fence, the state owner validates
   artifact changes, runs the node's positive proof followed by its negative proof, and accepts only the
   exit-code pair matching the declared outcome. It stores only the positive command's combined output
   as `result`, records proof metadata, and re-fingerprints successful artifact scopes after proof side
   effects. Reassess affected work to the fixed point before its next route.

Monitor delegated work according to expected duration. Inline nodes run sequentially in the parent;
do not count them as parallel. Serialize overlapping write ownership in both modes. A reported frontier
width is not permission to exceed actual tool capacity or the capacity-safe, non-overlapping subset.

## Complete or recover

Use node-scoped blockers when independent work can continue. A satisfied or superseded requirement
needs concrete evidence. Prefer one `workflow-complete` payload that exactly covers every active
requirement with evidence and supplies the integrated summary and validation; it resolves requirements
and completes the workflow atomically without resupplying immutable requirement text or source. Keep
`requirement-set` plus `finish` for incremental or advanced recovery. Completion succeeds only when
every runtime node is `done`, every decomposed parent is `skipped`, every superseded leaf is `skipped`,
and no ordinary `cancelled` node remains; all requirements and blockers are resolved, validation is
recorded, and all artifact evidence remains valid. Closeout reruns both commands for every non-exempt
graph record in deterministic node-ID order, including decomposed and superseded history, and requires
positive exit `0` plus negative nonzero for each. There is no proof waiver. A failed closeout leaves
durable workflow state unchanged, although proof-command filesystem side effects cannot be rolled back.
A node can become blocked only before its launch is claimed; pending and blocked nodes never retain an
active launch.
When a launch is claimed, the state owner fingerprints every declared artifact scope. A `done`
transition requires each declared scope to be a materialized regular file or directory whose fingerprint
changed during that attempt; the before/after evidence remains in the attempt record. Each snapshot
is rooted in the persisted repository filesystem identity, using anchored descriptor traversal where
supported. Both `workflow-complete` and `finish` recheck that every done artifact scope remains materialized. Evidence-only nodes declare no write scopes and
must have `change_surface=0`; they use the same proof execution contract. Coordinator does not invoke or inspect a
version-control system. An explicitly deleted path cannot itself be a completed scope; deletion work
must declare a containing directory that remains materialized or be modeled as evidence-only work.

Review must converge on evidence. Default to one integrated review wave after implementation and
focused validation. Add another fix/revalidation wave only for a concrete acceptance-relevant finding
with file or test evidence; reviewing a clean review is not itself a reason to spawn more judges.
Parallel judges are justified only by explicitly distinct risk surfaces, and their findings must be
merged before deciding on another wave. A successful evidence-only `review` node covers completed
artifact work in its transitive dependency ancestry. Closeout rejects any other completed artifact
work unless `workflow-complete` includes a non-blank `review_waiver` reason (or advanced `finish` uses
`--review-waiver`); the state owner records that decision as a `review_waived` event. Use a waiver only
for a deliberate stop or acceptance decision, never to hide an unresolved review finding. On an
explicit user stop or acceptance instruction, stop
spawning immediately, reconcile or interrupt active providers, and close with already-completed
evidence—never reinterpret “finish” as permission for another quality wave.

A replacement controller uses `controller-takeover`, which marks every claimed, bound, or running
launch `reconcile_required`, then `resume` before provider reconciliation and ordinary mutation. An
aborted workflow is not reported as cleanly done while any launch remains `reconcile_required` or a
discovered child remains `bound`; use `next` until every provider outcome is terminal or proven absent.
Mutation receipts and up to 32 attempts per node remain in the atomic workflow snapshot; exhaustion is
reported instead of adding a second persistence system. Close the private session file with
`session-close` after completion. Read-only `list`, `status`, `context`, and `next` commands inspect
persisted state without mutation.

See `references/workflow-protocol.md`, `references/complexity-accounting.md`,
`references/state-schema.md`, `references/dynamic-runtime-graphs.md`, and
`references/model-routing.md` for the stable contracts.
