# WORKFLOW 6 — JOURNAL ENTRY APPROVAL
## Source: Workflow Plan Extract — Section 5.6 / Table 10

```mermaid
flowchart TD
    START([🟢 START: Manual Journal Entry Required]) --> FO_PREP

    FO_PREP["📄 STEP 1 — ACTING FINANCE OFFICER\nJanerose Nduta Motende\nPrepares manual journal in Xero:\n① Narration included\n② Debit and credit entries\n③ Project tracking category\n④ Supporting document attached\n   (Finance Policy Section 7.2a)\n⚠️ Payroll data in journals subject to Data Protection\n   Policy access restrictions (Section 6.6)\nJournal saved as DRAFT in Xero\nForwarded to ApprovalMax"]

    FO_PREP --> CONTENT_CHK{"Journal type?"}

    CONTENT_CHK -->|"Payroll journal"| PAYROLL_ACCESS["⚠️ PAYROLL ACCESS CONTROL\nOnly accessible to:\n• HR\n• Finance\n• Acting ED\n(Data Protection Policy Section 6.6)"]
    PAYROLL_ACCESS --> OHR_REV

    CONTENT_CHK -->|"Non-payroll journal"| OHR_REV

    OHR_REV["🏢 STEP 2 — OPERATIONS & HR MANAGER\nJachtolinah Ndinda Nzive\nReviews journal for:\n① Accuracy\n② Completeness\n③ Proper donor coding\nSLA: 24 hours"]

    OHR_REV --> D1{"Ops & HR Mgr\nDecision"}
    D1 -->|"❌ Return with queries"| REJ1["🟡 RETURNED\nActing Finance Officer corrects\nand resubmits"]
    REJ1 --> FO_PREP
    D1 -->|"✅ Approved"| AMOUNT_GATE

    AMOUNT_GATE{"💰 Journal Amount or Type?\n① Above KES 100,000?\n   OR\n② Adjusting donor fund balances?"}

    AMOUNT_GATE -->|"NO — Below KES 100,000\nNOT adjusting donor funds"| POST_T1["🤖 JOURNAL POSTED TO XERO\nLocked from further editing\nAudit trail complete"]
    POST_T1 --> END_OK1(["🟢 END: Journal Posted\nApproved by Operations & HR Manager"])

    AMOUNT_GATE -->|"YES — Above KES 100,000\nOR adjusting donor fund balances"| AED_APPR["🔑 STEP 3 — ACTING EXECUTIVE DIRECTOR\nRebecca Mbaya\nApproves journals above KES 100,000\nor those adjusting donor fund balances\nSLA: 24 hours"]

    AED_APPR --> D2{"AED Decision"}
    D2 -->|"❌ Rejected"| REJ2["🔴 REJECTED\nJournal returned\nExplanation required"]
    D2 -->|"✅ Approved"| POST_T2["🤖 JOURNAL POSTED TO XERO\nLocked from further editing\nFull audit trail in ApprovalMax"]
    POST_T2 --> END_OK2(["🟢 END: Journal Posted\nApproved by Acting ED"])

    style START fill:#2d6a4f,color:#fff
    style END_OK1 fill:#2d6a4f,color:#fff
    style END_OK2 fill:#2d6a4f,color:#fff
    style REJ1 fill:#e07a5f,color:#fff
    style REJ2 fill:#c1121f,color:#fff
    style PAYROLL_ACCESS fill:#533483,color:#fff
    style AMOUNT_GATE fill:#264653,color:#fff
```

---

## JOURNAL ENTRY RULES (Finance Policy Section 7.2)

| Rule | Requirement |
|------|-------------|
| Accuracy | All entries accurate, complete, and timely |
| Supporting docs | Mandatory attachment for every journal |
| Donor coding | Correct tracking category required |
| Payroll journals | Restricted access — HR, Finance, Acting ED only |
| Post-approval lock | Journal locked from editing once approved |
| Retention | 10-year audit trail (Finance Policy Section 7.4) |
