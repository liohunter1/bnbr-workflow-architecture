# WORKFLOW 3 — PAYMENT APPROVAL & EXECUTION
## Source: Workflow Plan Extract — Section 5.3 / Tables 6, 7

```mermaid
flowchart TD
    START([🟢 START: Bills marked AWAITING PAYMENT in Xero]) --> BATCH

    BATCH["📋 STEP 1 — ACTING FINANCE OFFICER\nJanerose Nduta Motende\nPrepares payment batch in Xero:\n① Selects approved bills\n② Confirms bank details against approved vendor list\n③ Verifies payment is to entity named on approved LPO\n⚠️ Third-party payment? → Written authorization required\n   and attached in ApprovalMax\nPayment batch forwarded to ApprovalMax approval gate"]

    BATCH --> BANK_VER["📋 STEP 2 — BANK DETAIL VERIFICATION\nActing Finance Officer\n① Verifies bank account details match\n   approved vendor registration\n② Any bank detail change? → Requires Operations & HR\n   Manager re-approval of vendor record BEFORE processing\n   (Finance Policy Section 4.7)"]

    BANK_VER --> BANK_CHG{"Bank details\nchanged from\nmaster vendor file?"}
    BANK_CHG -->|"YES — details differ"| OHR_VENDOR["🏢 OPERATIONS & HR MANAGER\nJachtolinah Ndinda Nzive\nRe-approves vendor record\nFlag raised in ApprovalMax\nSLA: Same day"]
    OHR_VENDOR --> CHG_OK{"Re-approval\ngranted?"}
    CHG_OK -->|"❌ Rejected"| HALT_PAY(["🔴 HALT: Payment blocked\nVendor record not validated"])
    CHG_OK -->|"✅ Approved"| FM_REVIEW
    BANK_CHG -->|"NO — details match"| FM_REVIEW

    FM_REVIEW["💼 STEP 3 — ACTING FINANCE MANAGER\nPaul Celvins Ochieng'\nReviews payment batch:\n① Total amount correct?\n② All payees verified?\n③ Supporting bill references complete?\n④ Threshold tier compliance confirmed?\n⚠️ Returns ENTIRE BATCH if any single item queried\nAll queries resolved before resubmission\nSLA: 24 hours"]

    FM_REVIEW --> D1{"Finance Manager\nDecision"}
    D1 -->|"❌ Queries raised"| RESOLVE(["🟡 BATCH RETURNED TO FO\nFO resolves all queries & resubmits full batch"])
    D1 -->|"✅ Approved"| TIER_GATE

    TIER_GATE{"💰 PAYMENT TIER GATE\nWhat is the payment batch total?"}

    TIER_GATE -->|"KES 0–99,999\n(Tier 1)"| SCHED_CHK["⏰ PAYMENT SCHEDULE CHECK\n(Finance SWOP Section 9)\nBank transfer? → Tue/Thu only\nM-Pesa B2C? → Mon/Wed/Fri only\nActing ED mandatory bank signatory"]

    TIER_GATE -->|"KES 100,001–499,999\n(Tier 2)"| AED_T2["🔑 STEP 4a — ACTING EXECUTIVE DIRECTOR\nRebecca Mbaya\nSLA: 48 hours"]
    AED_T2 --> D2a{"AED Decision"}
    D2a -->|"❌ Rejected"| REJ_T2(["🔴 REJECTED\nExplanation documented"])
    D2a -->|"✅ Approved"| SCHED_CHK

    TIER_GATE -->|"KES 500,001–999,999\n(Tier 3)"| AED_BT["🔑 STEP 4b — ACTING ED + BOARD TREASURER\nBoth MANDATORY\nSLA: 48 hours"]
    AED_BT --> D2b{"Both approved?"}
    D2b -->|"❌ Either rejects"| REJ_T3(["🔴 REJECTED"])
    D2b -->|"✅ Both approved"| SCHED_CHK

    TIER_GATE -->|"KES 1,000,000+\n(Tier 4)"| BOARD_ALL["🏛️ STEP 4c — ACTING ED + BOARD TREASURER + BOARD CHAIRPERSON\nAll THREE MANDATORY\nSLA: 48 hours (Board up to 3 weeks)"]
    BOARD_ALL --> D2c{"All three approved?"}
    D2c -->|"❌ Any rejection"| REJ_T4(["🔴 REJECTED\nBoard resolution documented"])
    D2c -->|"✅ All approved"| SCHED_CHK
    
    SCHED_CHK --> EXEC(["🟢 EXECUTED\nActing Finance Officer executes\nAudit trail in ApprovalMax"])

    style START fill:#2d6a4f,color:#fff
    style EXEC fill:#2d6a4f,color:#fff
    style HALT_PAY fill:#c1121f,color:#fff
    style REJ_T2 fill:#c1121f,color:#fff
    style REJ_T3 fill:#c1121f,color:#fff
    style REJ_T4 fill:#c1121f,color:#fff
    style RESOLVE fill:#e07a5f,color:#fff
    style BOARD_ALL fill:#1a1a2e,color:#fff
    style TIER_GATE fill:#264653,color:#fff
```

---

## FIXED PAYMENT SCHEDULE (Finance SWOP Section 9)

```mermaid
flowchart LR
    MON["📅 MONDAY\nM-Pesa B2C only"]
    TUE["📅 TUESDAY\nBank Transfers only"]
    WED["📅 WEDNESDAY\nM-Pesa B2C only"]
    THU["📅 THURSDAY\nBank Transfers only"]
    FRI["📅 FRIDAY\nM-Pesa B2C only"]
    SAT["📅 SAT–SUN\n🚫 No payments"]
    CASH["🚫 CASH PAYMENTS\nPROHIBITED — ALL DAYS"]

    MON --- WED --- FRI
    TUE --- THU

    style MON fill:#264653,color:#fff
    style WED fill:#264653,color:#fff
    style FRI fill:#264653,color:#fff
    style TUE fill:#0f3460,color:#fff
    style THU fill:#0f3460,color:#fff
    style SAT fill:#4a4e69,color:#ccc
    style CASH fill:#c1121f,color:#fff
```

> **Activity participant payments:** Same day or next day after activity. Documentation to Finance by 3pm on activity day.
> **Per diem advances:** 1 working day before travel. Accountability due within 5 working days of return.
> **ApprovalMax payment reference** must appear on ALL bank transfer instructions.
> **Acting ED (Rebecca Mbaya)** is the MANDATORY bank signatory on all bank transfers.
