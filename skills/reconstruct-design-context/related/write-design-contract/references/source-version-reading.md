# Read the source into the procedure

Use the task's authoritative sources to connect each observation to the next permitted action. The first example varies the next observation under one unchanged rule. The later pairs vary one authoritative sentence while keeping the action and history fixed. In both forms, carry the decisive source condition into the contract's behavior and checks.

## 1. A mandatory observation with different next steps

**Fixed case:** A greenhouse controller changed a sprayer from `Run` to `Service`; `Service` remains active. The assigned technician intends to invoke `ClearPlan`. The earlier observation was `pumpState=Idle`, `bannerText=Ready`. The next mandatory observation has not yet occurred.

**Complete governing source**

> The greenhouse controller is authoritative for sprayer mode and pump state. Only the assigned technician may issue configuration mutations. `InstallPlan` and `ClearPlan` are configuration mutations; `ReadPump` is a read that returns pump state and informational banner text. After the controller enters `Service`, refuse every new configuration mutation until it restores `Run`, except `ClearPlan` when the immediately preceding `ReadPump` reports `pumpState=Idle`. The technician must perform that read before each `ClearPlan`. If the read reports another pump state or supplies no pump state, keep `ClearPlan` unissued and retry `ReadPump`; an `Idle` result permits it. Banner text does not affect permission. These are the complete restrictions for this procedure.

**Authored procedure**

1. Confirm the recorded `Run → Service` history and the assigned technician. Keep `ClearPlan` pending while performing the source-required `ReadPump`; the earlier `Idle` observation does not replace this step.
2. If the new result is `pumpState=Idle`, `bannerText=Ready`, invoke `ClearPlan`. The read establishes the named exception despite the continuing general restriction on configuration mutations.
3. If the new result is `pumpState=Running`, `bannerText=Ready`, keep `ClearPlan` unissued. Retry `ReadPump` as the source directs. A later `Idle` result reaches step 2; another non-idle result stays on this recovery branch.
4. If the new result is `pumpState=Idle`, `bannerText=Line B`, invoke `ClearPlan`. The changed banner is informational; the read still establishes the same permission condition.
5. If pump state is missing, permission is not established. Keep `ClearPlan` unissued and retry the read, following the same source-defined recovery until an `Idle` result is available.

The contract must include these branches, and its checks must exercise all four read outcomes. Branches 2 and 4 permit the same mutation; branch 3 defeats its exception; branch 5 leaves its prerequisite unknown. The relevant difference is the observed pump state specified by the source. A changed observation is therefore neither permission by itself nor a reason to stop every action. `InstallPlan` remains within the broad restriction throughout this history because the exception names only `ClearPlan`.

## 2. Joint requirements and an actual presentation choice

**Fixed case:** A kiln completes a firing and returns status `Fired` together with receipt `R7`. The contract must specify the final banner. No presentation choice has been supplied.

**Source version A**

> A completed firing returns status `Fired` and a batch receipt together. The final banner has room for both values. The final banner must display both status `Fired` and the supplied batch receipt. The product owner must select among any permitted alternative final banners before review handoff. No presentation choice has been supplied.

**Source version B**

> A completed firing returns status `Fired` and a batch receipt together. The final banner has room for both values. The final banner must display either status `Fired` or the supplied batch receipt, but never both. The product owner must select among any permitted alternative final banners before review handoff. No presentation choice has been supplied.

**A → consequence:** Specify a banner containing `Fired` and `R7`; check both in the completed-firing case. Both required values are available, and the source explicitly permits their shared presentation. There is no missing selection to resolve.

**B → consequence:** The banner must contain exactly one of the two values. The contract must retain the unresolved presentation choice and obtain the product owner's selection before review handoff; checking both values would now violate the explicit exclusion. Physical room for both does not override that rule.

The changed sentence creates the choice. Different informational roles alone do not make two requirements incompatible. Conversely, a real “never both” restriction cannot be repaired by combining them. Carry this distinction into the contract's open decisions and checks.

## 3. Authority attached to the correct stage

**Fixed case:** A library's lighting profile has complete technical sections, remains inactive, and has no operations-owner signature. The action under consideration is handing the profile document over for review.

**Source version A**

> The profile's technical sections are complete and the profile remains inactive. Only the operations owner may authorize activation. An operations-owner signature is required before activation. Review-ready means every stated prerequisite for review handoff is satisfied. No operations-owner signature has been recorded.

**Source version B**

> The profile's technical sections are complete and the profile remains inactive. Only the operations owner may authorize activation. An operations-owner signature is required before review handoff. Review-ready means every stated prerequisite for review handoff is satisfied. No operations-owner signature has been recorded.

**A → consequence:** The document can be review-ready and handed over while activation remains blocked. The contract should preserve owner authorization for activation. Its readiness check evaluates review prerequisites; its activation check requires the owner authorization and signature.

**B → consequence:** Review handoff is blocked because its stated signature prerequisite is absent. Mark that readiness condition unmet and check it before handoff. The operations owner's authority over activation also remains in force.

Changing “before activation” to “before review handoff” changes which stage the missing signature blocks. Preserve the actual gate, its authority, and its stage together. Neither technical completeness nor a general preference for fewer gates can substitute for that source reading.
