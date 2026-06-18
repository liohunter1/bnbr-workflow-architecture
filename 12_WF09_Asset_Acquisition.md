# WORKFLOW 9 — ASSET ACQUISITION
## Source: Workflow Plan Extract — Section 5.9a / Table 13

```mermaid
flowchart TD
    START([🟢 START: Asset Acquisition Required]) --> INIT

    INIT["📝 STEP 1 — INITIATING STAFF MEMBER\nSubmits asset acquisition request via\nPurchase Requisition Workflow (Section 5.1)\nFlagged as: CAPITAL EXPENDITURE\nIncludes:\n① Asset description\n② Estimated cost\n③ Useful life\n④ Depreciation rate (Finance Policy Section 6.2.1a-ii)\n⑤ Donor or funding source"]

    INIT --> COST_GATE{"💰 Estimated Cost\nvs KES 30,000\nCapitalization Threshold\n(Finance Policy Section 6.2.1a)"}

    COST_GATE -->|"Below KES 30,000\nOR useful life < 3 years"| EXPENSE["📋 PROCESS AS EXPENSE\nDo NOT flag as capital\nProcess via standard procurement\nNOT asset register"]
    EXPENSE --> STD_PROC(["→ Refer to Procurement Workflow\n(WF01) for relevant tier"])

    COST_GATE -->|"KES 30,000 or above\nAND useful life > 3 years"| FM_CONFIRM

    FM_CONFIRM["💼 STEP 2 — ACTING FINANCE MANAGER\nPaul Celvins Ochieng'\nConfirms:\n① Cost meets KES 30,000 capitalization threshold\n② Correct depreciation rate applied\n③ Donor rules on asset ownership at grant end confirmed\n④ Asset to be tagged with unique ID for Xero register\nSLA: 24 hours"]

    FM_CONFIRM --> D1{"Finance Manager\nDecision"}
    D1 -->|"❌ Query / Below threshold"| REJ1["🟡 RETURNED\nReclassify as expense or correct data"]
    REJ1 --> INIT
    D1 -->|"✅ Confirmed as CapEx"| PROC_WF["🔄 PROCUREMENT WORKFLOW APPLIED\nSection 5.1 — per applicable threshold tier\nAll procurement controls apply:\n• Quotation requirements\n• Bid Analysis Form\n• COI declaration\n• LPO generated"]

    PROC_WF --> GRN["📦 GOODS RECEIVED\nOperations & HR Manager\nJachtolinah Ndinda Nzive\nVerifies asset against specification\nSigns Goods Received Note (GRN)\nSLA: Per procurement tier SLA"]

    GRN --> REGISTER["🤖 ASSET REGISTERED IN XERO\nActing Finance Officer + Operations & HR Manager\nXero entry includes:\n① Unique Asset ID\n② Cost\n③ Date of acquisition\n④ Donor code\n⑤ Depreciation rate\n⑥ Location\nAsset register audit trail locked in ApprovalMax"]

    REGISTER --> AUDIT_CHK["📋 ONGOING CONTROLS\n• Quarterly inventory audits\n• Unannounced spot checks\n• Annual physical inventory count\n(Asset Policy BNBR/OPS/002/V1)"]

    AUDIT_CHK --> END_OK(["🟢 END: Asset Acquired & Registered\nXero asset register updated\nAudit trail complete"])

    style START fill:#2d6a4f,color:#fff
    style END_OK fill:#2d6a4f,color:#fff
    style EXPENSE fill:#264653,color:#fff
    style STD_PROC fill:#4a4e69,color:#fff
    style REJ1 fill:#e07a5f,color:#fff
    style COST_GATE fill:#264653,color:#fff
```

---

## ASSET CAPITALIZATION RULE

| Condition | Treatment |
|-----------|-----------|
| Cost ≥ KES 30,000 AND useful life > 3 years | Capitalized — add to Xero asset register |
| Cost < KES 30,000 OR useful life < 3 years | Expensed — do NOT add to asset register |

> **Source:** Finance Policy Section 6.2.1a
> **Quarterly audits** with unannounced spot checks required (Asset Policy BNBR/OPS/002/V1)
