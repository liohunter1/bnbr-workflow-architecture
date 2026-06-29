# 04b: WF01b — Purchase Order Generation

This workflow handles the final generation of the LPO in Xero and the Tier Gates. It operates as a Xero-linked Purchase Order Workflow in ApprovalMax, manually initiated by the Procurement Officer after the Standalone Requisition (WF01a) is complete.

```mermaid
flowchart TD
    START([🟢 START: Standalone Requisition Approved]) --> LPO_GEN

    LPO_GEN["🖨️ STEP 1 — PROCUREMENT INITIATION\nProcurement Officer manually creates Purchase Order\nCopies data from approved Standalone PDF\nIf split was detected, multiple distinct POs generated and routed separately"]

    LPO_GEN --> TIER_GATE{"TIER APPROVAL GATE\nWhat tier is this procurement?"}

    TIER_GATE -->|"Tier 1 or Tier 2\n(KES 0–99,999)"| APPROVED_T1T2["✅ APPROVED — Tier 1 / Tier 2\nFinal authority: Acting Finance Manager"]

    TIER_GATE -->|"Tier 3\n(KES 100,000–500,000)"| AED_APPR["🔑 STEP 2a — ACTING EXECUTIVE DIRECTOR\nApproves via ApprovalMax mobile or web\nSLA: 48–72 hours"]
    AED_APPR --> D5a{"AED Decision"}
    D5a -->|"❌ Reject"| REJ5a(["🔴 REJECTED\nFull explanation required"])
    D5a -->|"✅ Approved"| APPROVED_T3["✅ APPROVED — Tier 3\nFinal authority: Acting ED"]

    TIER_GATE -->|"Tier 4\n(KES 500,001–999,999)"| AED_BT["🔑 STEP 2b — ACTING ED + BOARD TREASURER\nBoth approvals MANDATORY\nSLA: 48–72 hours"]
    AED_BT --> D5b{"Both approved?"}
    D5b -->|"❌ Either rejects"| REJ5b(["🔴 REJECTED\nExplanation required"])
    D5b -->|"✅ Both approved"| APPROVED_T4["✅ APPROVED — Tier 4\nFinal authority: AED + Board Treasurer"]

    TIER_GATE -->|"Tier 5\n(KES 1,000,000+)"| BOARD_FULL["🏛️ STEP 2c — FULL BOARD APPROVAL\nBoard Treasurer + Board Chairperson\nFull tendering process\nBoard award decision\nSLA: Up to 3 weeks"]
    BOARD_FULL --> D5c{"Board Decision"}
    D5c -->|"❌ Rejected"| REJ5c(["🔴 REJECTED\nBoard resolution documented"])
    D5c -->|"✅ Approved"| APPROVED_T5["✅ APPROVED — Tier 5\nFinal authority: Board Treasurer + Board Chairperson"]

    APPROVED_T1T2 --> GRN_STEP
    APPROVED_T3 --> GRN_STEP
    APPROVED_T4 --> GRN_STEP
    APPROVED_T5 --> GRN_STEP

    GRN_STEP["🤖 SYSTEM ACTION (ApprovalMax/Xero)\nPurchase Order formally created in Xero.\nReady to be sent to Supplier.\nAudit trail locked in ApprovalMax"]
    
    GRN_STEP --> END_OK(["🟢 END WF01b: Procurement Complete"])

    style START fill:#2d6a4f,color:#fff
    style END_OK fill:#2d6a4f,color:#fff
    style REJ5a fill:#c1121f,color:#fff
    style REJ5b fill:#c1121f,color:#fff
    style REJ5c fill:#c1121f,color:#fff
    style APPROVED_T1T2 fill:#2d6a4f,color:#fff
    style APPROVED_T3 fill:#2d6a4f,color:#fff
    style APPROVED_T4 fill:#2d6a4f,color:#fff
    style APPROVED_T5 fill:#2d6a4f,color:#fff
```
