# DELEGATION AUTHORITY ARCHITECTURE
## Source: Workflow Plan Extract — Section 6.2 / Table 21

```mermaid
flowchart TD
    START([🟢 START: Approver will be ABSENT\nor UNAVAILABLE]) --> PRE_REQ

    PRE_REQ["⚠️ PRE-CONDITION: Delegation must be set up\nin ApprovalMax BEFORE the absence begins\n(Section 6.2 — proactive setup required)"]

    PRE_REQ --> SEG_RULE["🔒 SEGREGATION OF DUTIES RULE\nDelegate CANNOT approve transactions\nthat THEY THEMSELVES initiated\n(regardless of delegation authority)"]

    SEG_RULE --> AUTH_REQ["📝 DELEGATION REQUIRES APPROVAL FROM:\n• For Operations & HR Manager or above delegating:\n  → Approved by Acting ED (Rebecca Mbaya)\n• Where delegation would rest with Acting ED:\n  → Approved by Board Chairperson (Boniface Chitayi)"]

    AUTH_REQ --> WHO{"Who is the\nPrimary Approver\nbeing delegated?"}

    %% OHR MANAGER DELEGATION
    WHO -->|"Operations & HR Manager\nJachtolinah Ndinda Nzive"| OHR_DEL

    OHR_DEL["DELEGATION: Operations & HR Manager\n→ Delegate: Acting Finance Manager\n   (Paul Celvins Ochieng')\n→ Delegation Limit: Up to KES 99,999 ONLY\n→ Items above KES 99,999: HELD until\n   Operations & HR Manager returns\n→ Requires: Acting ED approval\n→ Expiry: Set in ApprovalMax (auto-expires\n   on return date)"]

    OHR_DEL --> OHR_GATE{"Approval from\nActing ED?"}
    OHR_GATE -->|"❌ Not approved"| REJ_OHR["🔴 Delegation NOT activated\nOperations & HR Manager must\narrange alternative coverage"]
    OHR_GATE -->|"✅ Approved"| OHR_ACTIVE["✅ Delegation Active\nLogged in ApprovalMax\nImmutable audit trail\nAuto-expires on return date"]
    OHR_ACTIVE --> OVER_99K_OHR["⚠️ Items ABOVE KES 99,999:\nHELD in ApprovalMax queue\nNot processed until\nOperations & HR Manager returns"]

    %% FINANCE MANAGER DELEGATION
    WHO -->|"Acting Finance Manager\nPaul Celvins Ochieng'"| FM_DEL

    FM_DEL["DELEGATION: Acting Finance Manager\n→ Delegate: Operations & HR Manager\n   (Jachtolinah Ndinda Nzive)\n→ Delegation Limit: FULL Finance Manager\n   approval authority for duration\n→ Board Treasurer notified for any item\n   requiring Acting ED or Board approval\n→ Requires: Acting ED approval\n→ Expiry: Set in ApprovalMax (auto-expires\n   on return date)"]

    FM_DEL --> FM_GATE{"Approval from\nActing ED?"}
    FM_GATE -->|"❌ Not approved"| REJ_FM["🔴 Delegation NOT activated"]
    FM_GATE -->|"✅ Approved"| FM_ACTIVE["✅ Delegation Active\nFull Finance Manager authority transferred\nBoard Treasurer notified for escalations"]

    %% ACTING ED DELEGATION
    WHO -->|"Acting ED\nRebecca Mbaya"| AED_DEL

    AED_DEL["DELEGATION: Acting Executive Director\n→ Delegate: Per ED's delegation instruction\n→ Delegation Limit: Tier 1 ONLY (up to KES 99,999)\n→ Items requiring AED approval (KES 100,000+):\n   HELD until AED returns, or\n   per ED's delegation mandate\n→ Extended absence: Board Treasurer\n   (CPA Charles Muhia) acts as last-resort\n   signatory per Board mandate / Board Resolution\n→ Requires: Board Chairperson (Boniface Chitayi)\n   approval\n→ Expiry: Set in ApprovalMax"]

    AED_DEL --> AED_GATE{"Approval from\nBoard Chairperson?"}
    AED_GATE -->|"❌ Not approved"| REJ_AED["🔴 Delegation NOT activated\nItems held until AED returns"]
    AED_GATE -->|"✅ Approved"| AED_ACTIVE["✅ Delegation Active\nTier 1 only delegated\nKES 100,000+ items HELD\nBoard Treasurer on standby\nfor extended absence"]
    AED_ACTIVE --> OVER_100K_AED["⚠️ Items above KES 99,999:\nHELD or routed to\nBoard Treasurer per\nBoard mandate"]

    %% BOARD TREASURER DELEGATION
    WHO -->|"Board Treasurer\nCPA Charles Muhia"| BT_DEL

    BT_DEL["DELEGATION: Board Treasurer\n→ Delegate: Board Chairperson (Boniface Chitayi)\n→ Condition: Board Chairperson acts if\n   Treasurer is unavailable for\n   Tier 3 and Tier 4 approvals\n→ Requires: Full Board notification\n→ Expiry: Set in ApprovalMax"]

    BT_DEL --> BT_GATE{"Full Board\nNotified?"}
    BT_GATE -->|"NO"| REJ_BT["🔴 Delegation NOT valid\nBoard must be notified"]
    BT_GATE -->|"YES"| BT_ACTIVE["✅ Delegation Active\nBoard Chairperson covers\nTier 3 and Tier 4 approvals\nFull Board notification on record"]

    %% COMMON END
    OHR_ACTIVE --> LOG["📋 DELEGATION LOG\nImmutable audit trail in ApprovalMax\nIncludes:\n① Primary approver name\n② Delegate name\n③ Delegation limit\n④ Approval authority (who approved delegation)\n⑤ Start date\n⑥ Expiry date\n⑦ All transactions approved under delegation"]
    FM_ACTIVE --> LOG
    AED_ACTIVE --> LOG
    BT_ACTIVE --> LOG

    LOG --> END_OK(["🟢 Delegation Active and Logged"])

    style START fill:#2d6a4f,color:#fff
    style END_OK fill:#2d6a4f,color:#fff
    style REJ_OHR fill:#c1121f,color:#fff
    style REJ_FM fill:#c1121f,color:#fff
    style REJ_AED fill:#c1121f,color:#fff
    style REJ_BT fill:#c1121f,color:#fff
    style SEG_RULE fill:#533483,color:#fff
    style OVER_99K_OHR fill:#f4a261,color:#000
    style OVER_100K_AED fill:#f4a261,color:#000
    style BT_DEL fill:#1a1a2e,color:#fff
```

---

## DELEGATION RULES SUMMARY (Section 6.2)

| Primary Approver | Standard Delegate | Delegation Limit | Authorized By |
|-----------------|-------------------|-----------------|---------------|
| Operations & HR Manager (Jachtolinah Nzive) | Acting Finance Manager (Paul Ochieng') | Tier 1 only — up to KES 99,999. Items above KES 99,999 HELD. | Acting ED (Rebecca Mbaya) |
| Acting Finance Manager (Paul Ochieng') | Operations & HR Manager (Jachtolinah Nzive) | Full Finance Manager authority for duration. Board Treasurer notified for ED/Board-level items. | Acting ED (Rebecca Mbaya) |
| Acting ED (Rebecca Mbaya) | Per ED's delegation instruction | Tier 1 only — up to KES 99,999. KES 100K+ held / Board Treasurer covers extended absences. | Board Chairperson (Boniface Chitayi) |
| Board Treasurer (CPA Charles Muhia) | Board Chairperson (Boniface Chitayi) | Tier 3 & 4 approvals | Full Board notification required |

> **Mandatory conditions for ALL delegations:**
> 1. Set up BEFORE absence begins
> 2. Time-limited with automatic expiry date in ApprovalMax
> 3. Delegate cannot approve transactions they themselves initiated
> 4. All delegations logged as immutable audit trail in ApprovalMax
> 5. Segregation: ordering, quality certification, storage, and payment authorization remain with different individuals (Procurement Policy Section 6)
