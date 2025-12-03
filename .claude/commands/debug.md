---
description: Fix a bug based on a previous /bug investigation
---

Fix the bug that was just investigated.

## Prerequisites

This command expects a /bug investigation to have been run first in this conversation. Use that context to fix the issue.

## Fixing Steps

1. **Review the investigation** - Look at the bug summary, relevant files, likely cause, and starting point from the /bug output

2. **Confirm the hypothesis** - Read the suspected files and verify the root cause matches the hypothesis

3. **Implement the fix**
   - Make the minimal change needed to fix the bug
   - Follow existing code patterns
   - Handle edge cases identified in the investigation

4. **Verify the fix**
   - Trace through the corrected data flow
   - Ensure the fix doesn't break other functionality
   - Run related tests if they exist

5. **Test edge cases** - Consider related scenarios that might be affected

## Output

Provide:
- **Root cause**: (confirmed explanation)
- **Fix applied**: (what was changed and why)
- **Files modified**: (list with line numbers)
- **Testing notes**: (how to verify the fix works)
