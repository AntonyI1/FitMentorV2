---
description: Investigate a bug from a description and find what's involved
---

Investigate this bug: $ARGUMENTS

## Investigation Steps

1. **Understand the bug** - Parse the expected vs actual behavior from the description

2. **Search the codebase** - Find all files related to the keywords and concepts mentioned (e.g., if the bug mentions "weight", "height", "metric", "imperial" - search for those terms)

3. **Identify the relevant code paths**
   - UI components involved
   - State management (how values are stored/updated)
   - Conversion logic or handlers
   - Event handlers (onChange, onSwitch, etc.)

4. **Trace the data flow** - Map what happens step by step when the described action occurs

5. **Spot the likely culprit** - Based on the expected vs actual behavior, identify where the logic probably breaks

6. **Provide a debugging plan**
   - Which files to look at first
   - What to log or breakpoint
   - A hypothesis for the root cause

## Output

Give a concise summary:
- **Bug**: (one line)
- **Relevant files**: (list)
- **Likely cause**: (your hypothesis)
- **Where to start**: (specific function/line to investigate first)
