# OUTPUT 1 — GOVERNANCE HIERARCHY MAP
## BNBR Kenya | ApprovalMax Workflow Architecture

---

```mermaid
flowchart TD
    BC["🏛️ BOARD CHAIRPERSON\nBoniface Chitayi\n(Ultimate Authority — Board Level)"]
    BT["💼 BOARD TREASURER\nCPA Charles Muhia\n(Co-Approver — Tier 3 & Tier 4)"]
    AED["🔑 ACTING EXECUTIVE DIRECTOR\nRebecca Mbaya\n(Final Approver — KES 100,000+\nMandatory Bank Signatory)"]
    OHR["📋 OPERATIONS & HR MANAGER\nJachtolinah Ndinda Nzive\n(Operations Review — All Workflows)"]
    AFM["📊 ACTING FINANCE MANAGER\nPaul Celvins Ochieng'\n(Finance Approver — KES 5,000–99,999)"]
    AFO["📄 ACTING FINANCE OFFICER\nJanerose Nduta Motende\n(Preparer — Bills, Journals, Payroll, Payments)"]
    PM["📁 PROGRAMS MANAGER\nGeoffrey Omega Khira\n(Budget Holder — Programs)"]
    ML["🔍 MERL LEAD\nJefferson Ponde Ochilo\n(Budget Holder — MERL & Beneficiary Data)"]
    DS["👥 DEPARTMENTAL STAFF\n(Requestors / Initiators)"]

    BC -->|"Co-approves Tier 4 (KES 1M+)\nBoard-level hirings\nExtended acting (6+ months)"| BT
    BT -->|"Co-approves Tier 3 (KES 500K–999K)\nFinal signatory if AED unavailable"| AED
    AED -->|"Delegates Tier 1 only (KES <100K)\nper formal delegation instruction"| OHR
    AED -->|"Supervises finance function"| AFM
    OHR -->|"Reviews all procurement\nHR and payroll review\nAsset and exit workflows"| AFM
    AFM -->|"Approves bills, payments, procurement\nup to KES 99,999"| AFO
    PM -->|"Budget holder approvals\nDonor report sign-off\nProcurement committee (KES 100K+)"| DS
    ML -->|"MERL/beneficiary data approvals\nProcurement committee (KES 100K+)"| DS
    AFO -->|"Prepares all financial documents"| DS

    style BC fill:#1a1a2e,color:#fff,stroke:#e94560
    style BT fill:#16213e,color:#fff,stroke:#e94560
    style AED fill:#0f3460,color:#fff,stroke:#e94560
    style OHR fill:#533483,color:#fff,stroke:#a8a8a8
    style AFM fill:#533483,color:#fff,stroke:#a8a8a8
    style AFO fill:#2d6a4f,color:#fff,stroke:#a8a8a8
    style PM fill:#2d6a4f,color:#fff,stroke:#a8a8a8
    style ML fill:#2d6a4f,color:#fff,stroke:#a8a8a8
    style DS fill:#4a4e69,color:#fff,stroke:#a8a8a8
```

---

## APPROVAL TIER LEGEND

| Tier | Amount Range | Final Authority |
|------|-------------|-----------------|
| Tier 1 | KES 0 – 99,999 | Acting Finance Manager (Paul Ochieng') |
| Tier 2 | KES 100,000 – 500,000 | Acting ED (Rebecca Mbaya) |
| Tier 3 | KES 500,001 – 999,999 | Acting ED + Board Treasurer |
| Tier 4 | KES 1,000,000+ | Board Treasurer + Board Chairperson |

---

## ESCALATION CHAIN (Authority Override)

```mermaid
flowchart TD
    S1["Staff Member\n(Requestor)"] -->|"submits"| L1

    subgraph L1 ["First Level Approvers (Any ONE approves)"]
        direction TB
        S2["Line Manager /\nDept Head"]
        S3["Programs Manager /\nMERL Lead"]
        S4["Operations & HR\nManager"]
        S5["Acting Finance\nManager"]
    end

    L1 -->|"approves ≤KES 99K\nforwards ≥KES 100K"| S6["Acting ED"]
    S6 -->|"forwards ≥KES 500K"| S7["Board Treasurer"]
    S7 -->|"forwards ≥KES 1M"| S8["Board Chairperson"]

    style S1 fill:#4a4e69,color:#fff
    style S2 fill:#4a4e69,color:#fff
    style S3 fill:#2d6a4f,color:#fff
    style S4 fill:#533483,color:#fff
    style S5 fill:#533483,color:#fff
    style S6 fill:#0f3460,color:#fff
    style S7 fill:#16213e,color:#fff
    style S8 fill:#1a1a2e,color:#fff
    style L1 fill:none,stroke:#d0d4e8,stroke-width:2px,stroke-dasharray: 5 5
```
