# Connect DAS to an engineering workflow

Use this recipe when an authorized product task needs design work and implementation through an engineering agent, skill set or project workflow. Map responsibilities into the consumer's existing process; create no new approval authority or required record type. Concrete tools, artifact formats and approval policies come from that project.

## Join the existing task

Use the project's existing coordinator and progress record. DAS supplies the needed design work and its evidence; the engineering workflow handles technical planning, implementation and engineering verification. A design-only task may remain led by DAS. Carry the same task identity, sources, decisions and unresolved scope; do not repeat intake or create a second backlog. Routine conformance still uses the compact handoff.

## Attach the controlling specification

Give engineering the effective Design Contract or other controlling effective canon, its exact revision and effectivity reference, approved scope, acceptance references and evidence locators. Use that artifact as the controlling product specification and derive technical tasks against its requirement references. Preserve source conditions, outcomes, exceptions and implementation freedoms; do not create competing product requirements. Technical decomposition may add implementation detail without inventing product behavior.

## Map decisions to the consumer's gates

Use the consumer's actual instructions to map which recorded decisions satisfy which gates and what authority remains. Artifact format alone does not establish approval. If that mapping is unresolved, prepare safe work and ask only about the dependent scope; do not assume a DAS effectivity decision satisfies a separate engineering or release approval. Conversely, a projection must not invent another approval for an already authorized step. Follow any stronger consumer policy.

## Continue and return scoped gaps

When the required gates are satisfied and the next step is authorized, continue the engineering workflow. Return an implementation defect for correction against the effective requirement. Return a material behavior change, source conflict or genuine decision gap to the design/owner lane with evidence and the smallest needed choice. Continue independent authorized work. A recommendation, prototype or proposed delta never changes the controlling source by itself.

Engineering DoD and DAS design parity can cite the same suitable runtime evidence; neither substitutes for the other. State what was actually observed and what remains untested. Do not rerun a check solely to give each workflow its own copy, or turn unavailable evidence into a product failure or approval. Follow the consumer's cumulative budget and stop conditions; this recipe starts no experiment.

For one requirement carried through source, acceptance, handoff and engineering task, see the [worked example](packet-projections.md#worked-handoff-example).

## Example: Addy's Agent Skills

For Addy 0.6.13, commit aeac41d4d005999432bb7312f7ff06383a91d59d, the existing-spec adapter preserves an external specification's format but retains its clarification/content/approval gates. A consumer can map the effective DAS contract to that specification and explicitly record which approvals are already satisfied. The engineering tasks then cite the contract's requirement references. Check the remaining technical and release gates against the consumer's instructions; format reuse does not waive them.

This example describes the pinned adapter. Other versions and engineering workflows may map differently; the shared recipe does not establish tested compatibility with every tool.
