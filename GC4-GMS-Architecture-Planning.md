## Summary
- GMS reconvened with CoverGo to reassess the financial integration strategy, acknowledging that the current CoverGo → Azure → IMAN → Sage 300 chain has become the program’s longest critical-path item and is jeopardizing launch timelines.
- The group aligned on exploring a simplified data flow that either bypasses Azure/IMAN or reduces their footprint by pushing canonical financial postings (AR/AP, revenue recognition, claims) directly from CoverGo into Sage 300 via APIs, connectors, or batch drops.
- Immediate focus areas include cataloging every financial transaction scenario (“laundry list”), evaluating Sage 300 web APIs/Swagger access, and validating whether CoverGo’s existing financial posting engine can satisfy GMS’s accounting use cases (including accrual nuances and reversals).
- Parallel workstreams will continue on ESC eligibility while a specialized deep dive—led by Phil and consultants—maps the financial events, required data entities, and dependency on upcoming provider launch milestones (Nov 1).

## Business Requirements
- **Accelerate critical path:** Shorten end-to-end financial integration timelines to unblock program delivery dates and the Nov 1 travel provider launch.
- **Maintain customer transparency:** Ensure claims and payment activity flows back into CoverGo so members see a single source of truth in the portal.
- **Support multi-origin adjudication:** Accommodate claims processed by Robin Assist, ESC, and CoverGo while maintaining consistent accounting treatment.
- **Simplify operations:** Reduce the 40+ bespoke IMAN pipelines by consolidating transaction variants (e.g., “with/without broker”) where possible.
- **Adopt canonical terminology:** Enforce consistent product/coverage naming across business units to avoid duplicate integration work.

## Technical Requirements
- **Direct Sage integration option:** Evaluate Sage 300 Web API/web screens for on-prem deployment; confirm feasibility of calling APIs from CoverGo or Azure.
- **Canonical financial data model:** Define AR/AP entities (customers, brokers, invoices, line items) plus supporting IDs so CoverGo can emit Sage-ready payloads.
- **Posting coverage matrix:** Document every transaction/event (new policy, claims, accruals, reversals, provider-paid claims, etc.) and map to CoverGo’s posting capabilities.
- **Batch + event flexibility:** Support daily batch exports for ledger postings while retaining event-driven triggers where beneficial.
- **Data validation & dependencies:** Enforce entity existence (customer, broker, invoice) before posting; auto-create missing references when safe.
- **Azure/RBC alignment:** Preserve necessary flows for payments originating from RBC or other bank integrations even if Sage is fed directly.

## Architecture / Integration Notes
- Current chain: `CoverGo → Azure orchestrations → IMAN translators → Sage 300 → RBC payments`. Testing and maintenance of ~40 connectors is unsustainable.
- Proposed direction emphasizes either:
  - **CoverGo → Sage 300 (API or connector):** CoverGo emits AR/AP postings, revenue accounting entries, and accruals directly, reducing reliance on IMAN.
  - **CoverGo → canonical file drop → Sage import:** If APIs are unavailable, CoverGo supplies Sage-formatted batch files via SFTP.
- IMAN’s role will be challenged; if Sage APIs suffice, IMAN can be retired for most streams, keeping only the paths that truly require Azure orchestration.
- Revenue recognition: CoverGo already implements receipt → collection → revenue accounting phases (suspense, premium due, policy income) and can serve as the system of record for accrual calculations (e.g., annual travel policies recognized at travel date).
- Claims data from partners (Robin Assist, ESC) must still flow back into CoverGo before reaching Sage, ensuring explanation-of-benefits triggers remain intact.
- Naming inconsistencies (e.g., “health” vs “health coverage”) create downstream fragmentation; business teams must standardize master data to avoid duplicate connectors.

## Action Items
| # | Action | Owner | Target/Due |
|---|--------|-------|------------|
| 1 | Compile and share the full “laundry list” of financial transaction scenarios (policies, claims, accruals, reversals, provider-paid flows). | Kacey / Terri / Donovan | Next architecture call (week of 2025-10-13) |
| 2 | Provide sample JSON payloads + specs for at least two priority transactions (new policy, claims) to CoverGo for joint review. | Donovan / Augustine | 2025-10-11 |
| 3 | Enable and expose Sage 300 Web API/Swagger on the on-prem instance (install web screens, confirm endpoint). | Donovan / Anan / Muhammad | 2025-10-14 |
| 4 | CoverGo to share their financial posting diagrams plus mapping guidance for AR/AP, revenue recognition, and collections. | Alex Montgomery / Godavari Gopal | 2025-10-11 |
| 5 | Document product/coverage naming discrepancies and initiate remediation with product owners. | Godavari + Edin (GMS) | 2025-10-18 |
| 6 | Schedule finance stakeholder deep dive once preliminary mappings are ready. | Phil Degenstein | 2025-10-21 |

## Next Steps & Upcoming Sessions
- **Weekly Architecture Call (week of 2025-10-13):** Decide whether session focuses on financial integration progress or ESC eligibility. Required attendees: Kacey, Phil, Donovan, Terri, Alex, Godavari, Anan (if API updates ready). Agenda: review action item status, walkthrough initial CoverGo ↔ Sage mappings, confirm scope for prototype flow.
- **Financial Mapping Workshop (target 2025-10-15):** Participants: CoverGo architects (Alex, Godavari), GMS finance/IT (Phil, Donovan, Finance lead). Agenda bullets: walk through transaction matrix, align on canonical entities, identify gaps (e.g., reversals).
- **Sage API Enablement Session (target 2025-10-14):** Participants: Donovan, Anan, Muhammad, Sage rep. Agenda: install/configure web screens, validate Swagger endpoint, confirm auth model/network constraints.
- **Finance Stakeholder Review (target 2025-10-21):** Bring finance SMEs to validate accounting treatment, revenue recognition, and compliance expectations before committing to build.

## Technical Requirements (Detailed Matrix)
- **AR / New Policy issuance**
  - Inputs: policy master data, broker association, invoice lines per product/coverage.
  - Outputs: Sage AR invoice + line items, customer/broker creation if absent.
  - Variants: broker vs non-broker policies to be collapsed via optional broker payload.
- **Claims / AP**
  - Inputs: claim header, payee, GL mapping, payment ID, adjudicator source (CoverGo vs partner).
  - Outputs: Sage AP invoice & items; ensure claim data returns to CoverGo for portal/EOB.
- **Accruals & revenue recognition**
  - Need monthly and event-based accrual logic sourced from CoverGo transactions rather than IMAN scripts.
- **Reversals / adjustments**
  - Currently weak in CoverGo; must define how reversals trigger counter-postings.
- **Bank/payment integration**
  - RBC payment execution still depends on Azure; need handshake between Sage outputs and bank instructions.

## Constraints & Assumptions
- **Constraints**
  - Limited finance SME availability on the call; deeper validation pending.
  - GMS engineering bandwidth constrained by Nov 1 provider launch.
  - Sage 300 is on-prem; API access depends on installing/configuring web components.
  - Legacy decisions around IMAN undocumented; original decision-makers unavailable.
- **Assumptions**
  - CoverGo financial postings remain the source of truth and can be transformed into Sage-ready records.
  - Daily batch cadence is acceptable for ledgers; near-real-time not mandatory.
  - Naming cleanup (products/coverages) can be enforced without breaking upstream systems.

## Mermaid Diagrams
```mermaid
graph LR
    A[CoverGo Events<br/>(Policy, Claim, Revenue)] --> B[Canonical Financial Payloads]
    B -->|Option 1| C[Sage 300 Web API]
    B -->|Option 2| D[Secure SFTP Batch Files]
    C --> E[General Ledger (AR/AP)]
    D --> E
    E --> F[RBC Payment Instructions]
    subgraph Legacy Path (to be reduced)
        A --> G[Azure Orchestrations]
        G --> H[IMAN Translators]
        H --> E
    end
```

```mermaid
sequenceDiagram
    participant CG as CoverGo
    participant VAL as Validation Layer
    participant S300 as Sage 300 API
    participant RBC as RBC Payments
    CG->>VAL: Emit Posting Event (AR/AP/Accrual)
    VAL->>VAL: Ensure Customer/Broker/Invoice Exists
    VAL->>S300: Create/Update Entities & Post Transactions
    S300-->>VAL: Posting Confirmation / IDs
    VAL-->>CG: Status + IDs (for portal/EOB sync)
    S300->>RBC: (When payable) Generate Payment Batch
    RBC-->>S300: Payment Confirmation
    CG<<--RBC: Claim/Payment status for member transparency
```

## Risks & Open Questions
- **Sage API readiness:** Unclear whether web API is licensed/installed on-prem; without it, retirement of IMAN stalls.
- **Coverage naming misalignment:** Inconsistent taxonomy may force duplicate connectors if not resolved quickly.
- **Reversal handling gaps:** CoverGo’s current limitation on payment reversals may require custom development before go-live.
- **Partner dependency:** Need clarity on how ESC/Robin Assist data will be standardized before entering CoverGo/Sage.
- **Resource contention:** Same GMS team balancing November provider launch could delay financial stream deliverables.
- **Testing complexity:** Even with APIs, 40+ scenarios require regression coverage; need automated validation strategy.

## Appendix
- **Meeting details:** “GC-4 GMS Architecture Call” — 2025-10-09, Notes by Gemini.
- **Participants mentioned:** Kacey M, Alex Montgomery, Godavari Gopal, Donovan Owen, Phil Degenstein, Terri Corney, Manraj Bilkhu, Augustine Ayo, Trideep Roy, Anan, Muhammad, Robin Assist & ESC referenced.
- **Key references:** Existing JSON integration diagrams (IMAN connectors), CoverGo financial posting diagrams (to be shared), Sage 300 Web API Swagger endpoint (TBD).
- **Context reminders:** GMS is reassessing both ESC eligibility and financial integration tracks; Monday 2025-10-13 is a GMS holiday, impacting scheduling.
