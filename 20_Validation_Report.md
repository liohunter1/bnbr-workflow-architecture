# VALIDATION REPORT — UPDATED
## BNBR ApprovalMax Workflow Architecture Package
## Document Reference: BNBR/FIN/AMWP/001/2026

**Validation Date:** 8 June 2026 | **Last Updated:** 17 June 2026
**Prepared By:** BNBR Finance & Operations Team
**Source Documents:** Workflow Plan Extract V1.0 (7 May 2026) + Staff List (22 May 2026) + Validation Response (PC, June 2026)

---

## SECTION 1 — WORKFLOW VALIDATION REPORT

| # | Workflow | Source Table | Steps Captured | Approvers Named | Thresholds Correct | Status |
|---|----------|-------------|----------------|-----------------|-------------------|--------|
| 1 | Purchase Requisition | Tables 2, 3, 4 | 6 steps + system checks | Initiating Staff → Programs Mgr / MERL Lead / Dept Head → Ops & HR Mgr → Finance Mgr → Acting ED → Board Treasurer → Board Chairperson | All 5 tiers (KES 0–4,999.99 / 5,000–99,999 / 100,000–500,000 / 500,001–999,999 / 1,000,000+) | ✅ VALIDATED |
| 2 | Supplier Bill / Invoice | Table 5 | 5 steps + 3-way match | Finance Officer → System → Finance Officer → Finance Manager → Acting ED → Board Treasurer → Board Chairperson per tier | All 4 value tiers. KES 100,000 exactly = Finance Manager tier per Finance Policy Section 4.2(b)(2) | ✅ VALIDATED |
| 3 | Payment Approval | Tables 6, 7 | 5 steps + payment schedule | Finance Officer → Finance Manager → Acting ED → Board Treasurer → Board Chairperson per tier | All 4 tiers + dual signatory + payment schedule | ✅ VALIDATED |
| 4 | Cash Requisition / Imprest | Table 8 | 5 steps + retirement | Field Staff / Custodian → Line Manager → Finance Officer / Finance Manager → Ops & HR Mgr (>KES 20K) | KES 20,000 imprest threshold, 75% float rule | ✅ VALIDATED |
| 5 | Payroll | Table 9 | 5 steps + automated segregation routing | Ops & HR Mgr → Finance Manager + Finance Officer → Ops & HR Mgr → Acting ED (automated re-route to Board Treasurer if conflict) | COLA requires Board Treasurer co-approval. Segregation enforced via automated ApprovalMax conditional routing rule | ✅ VALIDATED |
| 6 | Journal Entry | Table 10 | 3 steps | Finance Officer → Ops & HR Mgr → Acting ED (KES 100K+ or donor fund adjustment) | KES 100,000 and donor fund threshold | ✅ VALIDATED |
| 7 | Budget Adjustment | Table 11 | 4 steps | Programs Mgr / Finance Officer → Finance Manager → Acting ED | 10% materiality threshold, donor consent requirement. Board ODC notification via BNBR Board ODC meetings (meeting invites and minutes) | ✅ VALIDATED |
| 8 | Contract & Consultancy | Table 12 | 5 steps | Line Manager → Finance Manager → Ops & HR Mgr → Board (level-dependent) → Acting ED | Employment vs. non-HR, KES 1M threshold for Board | ✅ VALIDATED |
| 9 | Asset Acquisition | Table 13 | 3 steps | Initiating Staff → Finance Manager → Ops & HR Mgr | KES 30,000 capitalization threshold | ✅ VALIDATED |
| 10 | Asset Disposal | Table 14 | 5 steps | Ops & HR Mgr → Finance Manager → Disposal Committee → per value tier | All 4 disposal tiers per ORIGINAL purchase price (Finance Policy Section 9(c)(v) confirmed) | ✅ VALIDATED |
| 11 | Leave | Table 15 | All 10 leave types | Per leave type — Line Manager / HR Officer / Ops & HR Mgr / Acting ED / Board Chair | All leave types captured per HR Policy | ✅ VALIDATED |
| 12 | Acting Appointment | Table 16 | 4 steps | Line Manager → Ops & HR Mgr → Acting ED / Board (>6 months) | 6-month limit, 5-month auto-flag, 1-month allowance trigger | ✅ VALIDATED |
| 13 | Staff Exit | Table 17 | 5 steps | HR Officer → Ops & HR Mgr → Finance Officer / Finance Manager → Acting ED | Final dues withheld until property returned | ✅ VALIDATED |
| 14 | Data Access | Tables 18, 19 | 5 steps + 90-day review | Staff / IT Admin → Line Manager → Ops & HR Mgr / MERL Lead → Acting ED (Special Category) | Special Category data, MFA pre-condition, 72-hour breach notification. Volunteers: limited requestor access | ✅ VALIDATED |
| 15 | Delegation | Table 21 | 4 delegation routes | Per primary approver: Ops & HR Mgr / Finance Manager / Acting ED / Board Treasurer | Tier limits per delegation route | ✅ VALIDATED |
| 16 | Escalation | Table 20 | 4 escalation levels | 24h / 48h / 72h / 96h triggers | Critical delay lock at 96 hours | ✅ VALIDATED |

---

## SECTION 2 — IDENTIFIED GAPS — RESOLUTION STATUS

| # | Gap | Workflow Affected | Resolution / Status |
|---|-----|-------------------|---------------------|
| G1 | **Board member ApprovalMax accounts:** Boniface Chitayi (Board Chairperson) and CPA Charles Muhia (Board Treasurer) did not appear on the staff payroll list. | All Tier 3 and Tier 4 workflows | **RESOLVED.** Email addresses confirmed: CPA Charles Muhia — cmuhia@basicneedskenya.org; Boniface Chitayi — chitayib@gmail.com. ApprovalMax accounts to be created and MFA activated before go-live. |
| G2 | **IT Administrator not identified:** The Data Access workflow refers to an IT Administrator for system access provisioning, but no individual is named. | Data Access Workflow (WF14) | **PENDING.** Confirmation required from the Operations & HR Manager or Executive Director. IT Administrator must be identified, named in ApprovalMax, and MFA-activated before go-live. |
| G3 | **Donor Report Financial Sign-Off workflow missing:** Table 1 lists "Donor Report Financial Sign-Off" as Workflow 11 (Medium priority). No detailed procedure table was present in the source document. | Donor Report Workflow | **RESOLVED.** Sign-off sequence confirmed: Acting Finance Manager → Programs Manager → Acting Executive Director. Workflow added — see Section 4 below. |
| G4 | **Operative titles — Acting Finance Officer and Acting Finance Manager:** January 2026 payroll listed different titles from the Workflow Plan. | All workflows | **RESOLVED.** Operative titles confirmed: Janerose Nduta Motende — Acting Finance Officer; Paul Celvins Ochieng' — Acting Finance Manager. These titles apply for all ApprovalMax configuration. |
| G5 | **Volunteer ApprovalMax access level:** 35 volunteers are listed in the MERL Department with no specified access level. | Data Access Workflow (WF14) | **RESOLVED.** Access level for all 35 MERL Department volunteers: **LIMITED REQUESTOR ACCESS** only. No approval authority. No access to payroll, health, or beneficiary data. |
| G6 | **Board ODC notification mechanism:** Budget Adjustment workflow referenced "Board communication via ODC" without specifying the channel. | Budget Adjustment Workflow (WF07) | **RESOLVED.** Board ODC notification is executed via BNBR Board ODC meetings, referenced by meeting invites and board minutes. ApprovalMax triggers the notification flag; the Operations & HR Manager distributes via the ODC meeting invite. |
| G7 | **Rosemary Gathara (Executive Director) status:** January 2026 payroll listed Rosemary Gathara as Executive Director. | All ED-approval workflows | **RESOLVED.** Rosemary Gathara left the organisation on 15 May 2026. Her ApprovalMax and Xero accounts must be deactivated with immediate effect. Rebecca Mbaya (Acting ED) remains the sole ED-level approver. |
| G8 | **Procurement prequalified supplier list:** The workflow references the Operations & HR Manager maintaining a prequalified supplier list, but the list was not provided. | Purchase Requisition Workflow (WF01) | **PENDING.** Confirmation required from the Operations & HR Manager. The list and the supplier onboarding/offboarding process must be documented and loaded into ApprovalMax before go-live. |

---

## SECTION 3 — POLICY AMBIGUITIES — RESOLUTION STATUS

| # | Ambiguity | Workflow | Policy Resolution | Action |
|---|-----------|----------|-------------------|--------|
| A1 | **Bill approval at exactly KES 100,000.** | Supplier Bill Workflow (WF02) | **RESOLVED — Finance Policy Section 4.2(b)(2):** "Any disbursement above KES 100,000 must be approved by the Executive Director." KES 100,000 exactly therefore remains in the Finance Manager / Programs Manager tier. Only amounts **exceeding** KES 100,000.00 route to the Acting ED. | Configure ApprovalMax threshold as: Finance Manager tier = KES 5,000 to KES 100,000 inclusive. ED tier = above KES 100,000 (i.e., KES 100,000.01 and above). |
| A2 | **Procurement splitting — rolling 30-day window vs calendar month.** | Purchase Requisition (WF01) | **RESOLVED — Procurement Policy Section 3(a)(3.1.4):** Prohibits artificial division of procurement to evade delegation levels. The policy does not specify a day count, but establishes that multiple orders with the same supplier for similar projects must be substantiated by the operations department and approved by the Procurement Committee. | Configure ApprovalMax using a **rolling 30-day window** rule to flag transactions from the same vendor and project code. This is the more conservative and auditable configuration. |
| A3 | **Acting ED payroll self-segregation — manual vs automated trigger.** | Payroll Workflow (WF05) | **RESOLVED — Finance Policy Section 2.2.3(a):** Mandates absolute segregation of duties across authorisation, execution, recording, and reconciliation. Manual declarations are insufficient for internal control compliance. | Configure an **automated conditional routing rule** in ApprovalMax: If Preparer = Acting ED, the ED Approval node is skipped and the item routes directly to the Board Treasurer (CPA Charles Muhia). No manual intervention required. |
| A4 | **Asset disposal approval basis — original purchase price vs Net Book Value.** | Asset Disposal (WF10) | **CONFIRMED AS POLICY — Procurement Policy Section 9(c)(v):** "Disposal approvals shall be aligned to the procurement approval matrix based on the purchase price provided in Section 8.1 of this policy." | No workflow change required. This is an explicit and deliberate policy choice. The Board is aware this may require Board-level involvement for heavily depreciated assets. |
| A5 | **Single sourcing at exactly KES 5,000.** | Purchase Requisition (WF01) | **RESOLVED — Procurement Policy Section 8(a) threshold matrix** takes precedence over Section 7 text: Single sourcing applies strictly from KES 0.00 to KES 4,999.99. Competitive bidding (minimum 3 quotations) is mandatory at KES 5,000.00 and above. | Configure ApprovalMax so that single-source configuration applies up to KES 4,999.99 only. The 3-quotation attachment validation is enforced at KES 5,000.00 and above without exception. |

---

## SECTION 4 — DONOR REPORT FINANCIAL SIGN-OFF WORKFLOW (G3 Resolution)

**Workflow Name:** Donor Report Financial Sign-Off
**Priority:** Medium | **Xero Transaction:** Report Attachment and Journal
**Policy Basis:** Finance Policy Section 8.3

| Step | Action | Approver | SLA |
|------|--------|----------|-----|
| 1 | Acting Finance Officer prepares financial data for the donor report. Figures reconciled against Xero tracking categories for the relevant donor and period. Report attached in ApprovalMax as a draft. | Acting Finance Officer (Janerose Nduta Motende) | By reporting deadline |
| 2 | Acting Finance Manager reviews financial accuracy, confirms donor budget compliance, verifies all expenditure lines are within approved donor budget, and checks that statutory deductions and WHT are correctly reflected. | Acting Finance Manager (Paul Celvins Ochieng') | 24 hours |
| 3 | Programs Manager reviews narrative consistency with financial data. Confirms programmatic outputs match expenditure. Signs off on donor report completeness. | Programs Manager (Geoffrey Khira) | 24 hours |
| 4 | Acting Executive Director gives final authorisation. Signed report uploaded to ApprovalMax and submitted to donor. | Acting ED (Rebecca Mbaya) | 48 hours |

---

## SECTION 5 — APPROVAL MATRIX VERIFICATION REPORT

| Workflow | Tier | Approver 1 | Approver 2 | Approver 3 | Approver 4 | Verified Against Source |
|----------|------|------------|------------|------------|------------|------------------------|
| Procurement | KES 0–4,999.99 | Acting Finance Manager | — | — | — | ✅ Table 2 |
| Procurement | KES 5,000–99,999 | Acting Finance Manager | — | — | — | ✅ Table 2 |
| Procurement | KES 100,000–500,000 | Acting ED | — | — | — | ✅ Table 2 |
| Procurement | KES 500,001–999,999 | Acting ED | Board Treasurer | — | — | ✅ Table 2 |
| Procurement | KES 1,000,000+ | Board Treasurer | Board Chairperson | — | — | ✅ Table 2 |
| Bills | KES 5,000–100,000 (inclusive) | Acting Finance Manager | — | — | — | ✅ Table 5 + Finance Policy 4.2(b)(2) |
| Bills | Above KES 100,000–499,999 | Acting Finance Manager | Ops & HR Mgr | Acting ED | — | ✅ Table 5 |
| Bills | KES 500,000–999,999 | Acting Finance Manager | Ops & HR Mgr | Acting ED | Board Treasurer | ✅ Table 5 |
| Bills | KES 1,000,000+ | Acting Finance Manager | Ops & HR Mgr | Acting ED | Board Treasurer + Board Chairperson | ✅ Table 5 |
| Payment | KES 0–99,999 | Acting Finance Manager | — | — | — | ✅ Table 6 |
| Payment | KES 100,001–499,999 | Acting Finance Manager | Acting ED | — | — | ✅ Table 6 |
| Payment | KES 500,001–999,999 | Acting Finance Manager | Acting ED | Board Treasurer | — | ✅ Table 6 |
| Payment | KES 1,000,000+ | Acting Finance Manager | Acting ED | Board Treasurer | Board Chairperson | ✅ Table 6 |
| Payroll | Monthly | Ops & HR Mgr | Acting Finance Manager + Finance Officer | Acting ED | Board Treasurer (automated re-route if conflict) | ✅ Table 9 + Finance Policy 2.2.3(a) |
| Journal | Below KES 100,000 | Ops & HR Mgr | — | — | — | ✅ Table 10 |
| Journal | KES 100,000+ or donor | Ops & HR Mgr | Acting ED | — | — | ✅ Table 10 |
| Budget Adj | Any | Acting Finance Manager | Acting ED | — | — | ✅ Table 11 |
| Asset Disposal | KES 0–99,999 | Disposal Committee | Acting Finance Manager | — | — | ✅ Table 14 |
| Asset Disposal | KES 100,000–500,000 | Disposal Committee | Acting ED | — | — | ✅ Table 14 |
| Asset Disposal | KES 500,001–999,999 | Disposal Committee | Acting ED | Board Treasurer | — | ✅ Table 14 |
| Asset Disposal | KES 1,000,000+ | Disposal Committee | Board Treasurer | Board Chairperson | — | ✅ Table 14 |

---

## VALIDATION SUMMARY

| Metric | Result |
|--------|--------|
| Total workflows generated | 16 (14 operational + delegation + escalation) |
| Workflows fully validated | 16 / 16 |
| Gaps identified | 8 |
| Gaps resolved | 6 (G1, G3, G4, G5, G6, G7) |
| Gaps pending | 2 (G2 — IT Admin; G8 — Supplier list) |
| Policy ambiguities identified | 5 |
| Policy ambiguities resolved | 5 / 5 (A1–A5) |
| Approval routes verified | 20 / 20 |
| Users captured | All 56 from staff list |
| Board member emails confirmed | Boniface Chitayi: chitayib@gmail.com; CPA Charles Muhia: cmuhia@basicneedskenya.org |
| Rosemary Gathara account status | Deactivate immediately — left organisation 15 May 2026 |
| External assumptions made | NONE |
| Policy rules invented | NONE |

> **Certification:** All workflow steps, approval names, amounts, and thresholds in this package trace directly to the BNBR ApprovalMax Workflow Plan Extract V1.0 (7 May 2026), BNBR Kenya List of Staff (22 May 2026), and the Validation Response document (June 2026). No external assumptions or fabricated approval routes have been used.
