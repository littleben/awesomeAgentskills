# Model routing contract

`model_router.py choose` accepts one UTF-8 JSON object through `--task-file PATH` or `-`. Unknown fields
are rejected.

Required fields are `summary`; a `stage` of `architecture`, `design`, `documentation`, `fix`,
`implementation`, `integration`, `research`, `review`, or `validation`; and numeric `complexity`,
`ambiguity`, `criticality`, `coupling`, `novelty`, and `determinism` scores from 1 through 5.

An optional profile contains `budget` (`value`, `balanced`, or `quality`) and up to 128 `candidates`.
Each candidate is one combination currently advertised by the runtime:

```json
{
  "model": "runtime-model-id",
  "effort": "runtime-effort-id",
  "capacity": 4.2,
  "relative_cost": 1.0
}
```

`model` accepts any non-blank runtime identifier. `effort` may be `null` when the model's default should
apply. Capacity and relative cost are non-negative caller-supplied planning heuristics, not model
allowlists, prices, or quality guarantees.

The router selects the stage's specialist role and ranks supplied candidates against task demand and
budget. With no profile or an empty candidate list, it returns `null` model and effort so a delegated
or inline executor inherits the parent route. If optional route selection cannot complete, the
controller uses the same inherited route instead of blocking the node. Node add, split, and refine
leave a provisional route whose attempt is invalid for claim. After the latest assessment and global
planning fixed point, the controller normally runs `node-route-auto`, which performs this translation and persists the selected
route in the same revision-fenced mutation immediately before each attempt. Manual `node-route` remains
an advanced override. Omit unset model/effort arguments from delegated invocations.

Route only a non-blocked assessable leaf whose persisted assessment is current and `executable`, and
only when every other non-blocked assessable leaf is also current and executable. Keep the router API
unchanged and adapt persisted schema-v8 assessment values to its existing 1–5 request fields as follows:

- `complexity = clamp(1, 5, ceil(assessment.total / 4))`
- `ambiguity = clamp(1, 5, assessment.ambiguity_total + 1)`
- `coupling = assessment.dimensions.coupling + 1`
- `novelty = assessment.dimensions.novelty + 1`

Use the node objective for `summary` and its stage for `stage`. Assess `criticality` and `determinism`
separately from current execution evidence because they are routing demand, not decomposition
complexity. Never author a second complexity, ambiguity, coupling, or novelty estimate during routing.
If evidence changes the assessment digest, reassess the node before constructing another request.

Runtime projections affect dispatch and reconciliation priority only. `node-route-auto` continues to
derive model demand from the current persisted assessment, so telemetry cannot silently replace the
auditable rubric used to authorize a claim. Runtime-generated nodes receive fresh assessments and
therefore route normally after reaching the global fixed point.
