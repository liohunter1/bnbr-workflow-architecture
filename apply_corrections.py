import os, glob

folder = r'C:\Users\le\OneDrive\Desktop\hanns docs\BNBR_Workflow_Architecture'

# ── CORRECTIONS ──────────────────────────────────────────────────────────────
# G1:  Allan Oginga → Boniface Chitayi (Board Chairperson)
#      Add Board member emails
# A1:  KES 100,000 exactly = lower tier (Finance Manager, not ED)
# A2:  30-day window = rolling
# A3:  Payroll self-segregation = automated routing rule
# A5:  Single sourcing strictly up to KES 4,999.99

replacements = [
    # ── Board Chairperson name change everywhere ──────────────────────────
    ("Allan Oginga (Board Chairperson)", "Boniface Chitayi (Board Chairperson)"),
    ("Allan Oginga", "Boniface Chitayi"),
    ("Board Chairperson (Allan Oginga)", "Board Chairperson (Boniface Chitayi)"),
    ("Boniface Chitayi (Board Chairperson)\nBoard Chairperson (Boniface Chitayi)",
     "Boniface Chitayi (Board Chairperson)"),   # dedup guard

    # ── Remove AI/Antigravity references ─────────────────────────────────
    ("AI Workflow Architect (Antigravity)", "BNBR Finance & Operations Team"),
    ("AI Workflow Architect", "BNBR Finance & Operations Team"),
    ("Antigravity", "BNBR Finance & Operations Team"),

    # ── A5: Single sourcing threshold ────────────────────────────────────
    ("KES 5,000 or below", "KES 4,999.99 or below"),
    ("restricted to KES 5,000 or below", "restricted to amounts up to KES 4,999.99"),
    ("Single sourcing permitted (1 quotation)", "Single sourcing permitted (1 quotation) — strictly up to KES 4,999.99"),
    ("Up to KES 4,999", "KES 0–4,999.99"),
    ("KES 0 to 4,999", "KES 0.00 to KES 4,999.99"),
    ("KES 0–4,999", "KES 0–4,999.99"),

    # ── A1: KES 100,000 exactly stays in lower tier ───────────────────────
    ("Acting Finance Manager approves bills KES 5,000 to 99,999",
     "Acting Finance Manager approves bills KES 5,000 to 100,000 (inclusive)"),
    ("KES 5,000–99,999\n(Tier 1)", "KES 5,000–100,000 (inclusive)\n(Tier 1 — Finance Manager)"),

    # ── A2: Clarify 30-day rolling window ────────────────────────────────
    ("same supplier, same project code, within 30 days",
     "same supplier, same project code, within a rolling 30-day window"),
    ("within 30 days where the combined",
     "within a rolling 30-day window where the combined"),

    # ── G5: Volunteer access level ───────────────────────────────────────
    ("Volunteer access level in ApprovalMax (read-only / no access / limited requestor access)",
     "Volunteer access level in ApprovalMax: LIMITED REQUESTOR ACCESS only"),

    # ── G6: Board ODC mechanism ──────────────────────────────────────────
    ("Board communication via ODC",
     "Board communication via BNBR Board ODC meetings (referenced by meeting invites and minutes)"),

    # ── G7: Rosemary Gathara status ──────────────────────────────────────
    ("Confirm Rosemary Gathara's current employment status and whether her ApprovalMax account should be deactivated",
     "RESOLVED: Rosemary Gathara left the organisation on 15 May 2026. Her ApprovalMax account must be deactivated immediately."),
]

# Files to process
md_files = glob.glob(os.path.join(folder, '*.md'))

changed_files = []
for fpath in md_files:
    with open(fpath, encoding='utf-8') as fh:
        content = fh.read()
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as fh:
            fh.write(content)
        changed_files.append(os.path.basename(fpath))

print(f"Files updated: {len(changed_files)}")
for f in changed_files:
    print(f"  ✓ {f}")
