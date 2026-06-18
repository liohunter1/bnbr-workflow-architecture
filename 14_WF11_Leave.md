# WORKFLOW 11 — LEAVE APPLICATION
## Source: Workflow Plan Extract — Section 5.10a / Table 15

```mermaid
flowchart TD
    START([🟢 START: Staff Member Requires Leave]) --> TYPE_GATE{"Leave Category"}

    TYPE_GATE -->|"Routine Leaves"| ROUTINE_GATE{"Select Type"}
    ROUTINE_GATE -->|"Annual Leave\n(28 days/year)"| ANNUAL
    ROUTINE_GATE -->|"Urgent Leave\n(max 5 days)"| URGENT
    ROUTINE_GATE -->|"Sick / Convalescence"| SICK
    ROUTINE_GATE -->|"Compassionate Leave\n(5-10 days)"| COMPASSIONATE

    TYPE_GATE -->|"Statutory Leaves"| STAT_GATE{"Select Type"}
    STAT_GATE -->|"Maternity Leave\n(4 months)"| MATERNITY
    STAT_GATE -->|"Paternity Leave\n(21 days)"| PATERNITY
    STAT_GATE -->|"Adoption Leave"| ADOPTION

    TYPE_GATE -->|"Special Leaves"| SPEC_GATE{"Select Type"}
    SPEC_GATE -->|"Unpaid Leave\n(max 3 months)"| UNPAID
    SPEC_GATE -->|"Study Leave\n(max 3 months)"| STUDY
    SPEC_GATE -->|"Compulsory Leave\n(max 30 days)"| COMPULSORY

    %% ANNUAL LEAVE
    ANNUAL --> ADVANCE_CHK{"Submitted minimum\n7 working days in advance?"}
    ADVANCE_CHK -->|"NO"| EARLY_WARN["⚠️ Warning: Policy requires\n7 working days advance notice\n(HR Policy Section 5.2)\nExceptional circumstances\nmay waive requirement"]
    EARLY_WARN --> LINE_A
    ADVANCE_CHK -->|"YES"| LINE_A
    LINE_A["Line Manager: Reviews & recommends\nWith leave balance"]
    LINE_A --> HR_A["HR Officer: Computes leave balance\nChecks entitlement (2.08 days/month)"]
    HR_A --> AED_A["🔑 ACTING ED (Rebecca Mbaya)\nFinal approval"]
    AED_A --> D_A{"AED Decision"}
    D_A -->|"❌"| REJ_A["🔴 DECLINED"]
    D_A -->|"✅"| END_A(["🟢 Annual Leave Approved"])

    %% URGENT LEAVE
    URGENT --> LINE_U["Line Manager: Reviews\nJustification attached for unusual circumstances"]
    LINE_U --> AED_U["🔑 ACTING ED (Rebecca Mbaya)\nFinal approval"]
    AED_U --> D_U{"AED Decision"}
    D_U -->|"❌"| REJ_U["🔴 DECLINED"]
    D_U -->|"✅"| END_U(["🟢 Urgent Leave Approved\nDeducted from annual leave balance"])

    %% SICK LEAVE
    SICK --> MEDCERT["Staff Member\nProvides medical certificate from\naccredited medical practitioner"]
    MEDCERT --> HR_S["HR Officer\nProcesses based on medical certificate\nFull salary: 3 months\nHalf salary: further 3 months (per 12-month cycle)"]
    HR_S --> RTW["Return-to-work interview\nby supervisor on return"]
    RTW --> END_S(["🟢 Sick Leave Processed"])

    %% COMPASSIONATE LEAVE
    COMPASSIONATE --> LINE_C["Line Manager reviews\nDocumentary evidence required\n(separate from annual leave)"]
    LINE_C --> OHR_C["Operations & HR Manager\nConfirms entitlement and evidence"]
    OHR_C --> END_C(["🟢 Compassionate Leave Approved"])

    %% MATERNITY / PATERNITY
    MATERNITY --> DOCS_M["Staff submits:\nAppointment + antenatal documentation"]
    DOCS_M --> OHR_M["Operations & HR Manager\nJachtolinah Ndinda Nzive\nReviews documentation"]
    OHR_M --> AED_M["🔑 ACTING ED (Rebecca Mbaya)\nFinal approval\n4 months full pay\nFlextime (30hrs/week, 8 months post-delivery)\napproved separately"]
    AED_M --> END_M(["🟢 Maternity Leave Approved"])

    PATERNITY --> DOCS_P["Staff submits:\nRegistered spouse birth documentation"]
    DOCS_P --> OHR_P["Operations & HR Manager\nReviews"]
    OHR_P --> AED_P["🔑 ACTING ED\nFinal approval\n21 calendar days"]
    AED_P --> END_P(["🟢 Paternity Leave Approved"])

    %% UNPAID / STUDY / ADOPTION
    UNPAID --> AED_UP["🔑 ACTING ED (Rebecca Mbaya)\nFinal approval\nWritten full details required\nMax 3 months\nConfidentiality maintained"]
    AED_UP --> END_UP(["🟢 Unpaid Leave Approved"])

    STUDY --> STUDY_CHK{"Minimum 3 years\ncontinuous service?"}
    STUDY_CHK -->|"NO"| REJ_STY["🔴 INELIGIBLE\nDoes not meet service requirement"]
    STUDY_CHK -->|"YES"| AED_STY["🔑 ACTING ED\nApproves (max 3 months, no pay)\nEvidence of registration required\nEmployee meets course cost"]
    AED_STY --> END_STY(["🟢 Study Leave Approved"])

    ADOPTION --> AED_AD["🔑 ACTING ED\nApproves\nLegal adoption documents required\nDays vary by child age (HR Policy Section 5.8)"]
    AED_AD --> END_AD(["🟢 Adoption Leave Approved"])

    %% COMPULSORY LEAVE
    COMPULSORY --> INVEST_GATE{"Does investigation\ninvolve Acting ED?"}
    INVEST_GATE -->|"NO"| AED_COMP["🔑 ACTING ED ORDERS\nCompulsory leave max 30 days\nFull salary maintained\nFormal investigation trigger documented"]
    INVEST_GATE -->|"YES — AED is subject"| BC_COMP["🏛️ BOARD CHAIRPERSON\nBoniface Chitayi\nOrders compulsory leave"]
    AED_COMP --> END_COMP(["🟢 Compulsory Leave Ordered\nFormal investigation proceeds"])
    BC_COMP --> END_COMP

    style START fill:#2d6a4f,color:#fff
    style END_A fill:#2d6a4f,color:#fff
    style END_U fill:#2d6a4f,color:#fff
    style END_S fill:#2d6a4f,color:#fff
    style END_C fill:#2d6a4f,color:#fff
    style END_M fill:#2d6a4f,color:#fff
    style END_P fill:#2d6a4f,color:#fff
    style END_UP fill:#2d6a4f,color:#fff
    style END_STY fill:#2d6a4f,color:#fff
    style END_AD fill:#2d6a4f,color:#fff
    style END_COMP fill:#2d6a4f,color:#fff
    style REJ_A fill:#c1121f,color:#fff
    style REJ_U fill:#c1121f,color:#fff
    style REJ_STY fill:#c1121f,color:#fff
    style EARLY_WARN fill:#f4a261,color:#000
    style BC_COMP fill:#1a1a2e,color:#fff
```

---

## LEAVE ENTITLEMENT SUMMARY (HR Policy)

| Leave Type | Entitlement | Final Approver |
|-----------|------------|----------------|
| Annual | 28 days/year (2.08 days/month) | Acting ED |
| Urgent | Max 5 days (deducted from annual) | Acting ED |
| Sick/Convalescence | 3 months full pay + 3 months half pay (per 12-month cycle) | HR Officer (medical cert) |
| Compassionate | 10 days (bereavement) / 5 days (exceptional) | Ops & HR Manager |
| Maternity | 4 months full pay | Acting ED |
| Paternity | 21 calendar days | Acting ED |
| Unpaid | Max 3 months | Acting ED |
| Study | Max 3 months (min 3 years service) | Acting ED |
| Adoption | Varies by child age | Acting ED |
| Compulsory | Max 30 days (full salary) | Acting ED (Board Chair if AED is subject) |
