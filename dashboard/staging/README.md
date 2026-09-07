# Staging — Numbers editing drop box

Export from Numbers to **`features-edit.xlsx`** and drop it in this folder.

Then ask Claude to **run IMPORT**. It will:
1. validate the file (sheet, headers, ids, statuses, Level paths) — stops on any problem
2. print a cell-by-cell diff vs the master for `name`, `status`, `Level1`–`Level7`
3. wait for your confirmation, then apply only those cells through the 9-step guardrail
4. regenerate the JSON, verify counts, and delete this file

**The staging file never replaces `features-master.xlsx`.** Only differing cell values are
copied across, so formatting, fonts and column widths from Numbers are ignored.

Rows present in the master but absent from staging are ignored — never deleted.
Rows in staging with an id the master doesn't have are reported, not auto-created.
