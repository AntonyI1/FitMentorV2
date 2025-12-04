Prepare context for a specific area of the codebase.

Area: $ARGUMENTS

1. Identify and read all relevant files for the "$ARGUMENTS" area
2. Create a structured summary file at `.claude/primed/$ARGUMENTS.md` containing:
   - **Area**: What this covers
   - **Key Files**: List with 1-line descriptions of each file's role
   - **Important Types/Interfaces**: The main data structures
   - **Patterns**: How things are done in this area (state management, API calls, etc.)
   - **Dependencies**: What this area depends on and what depends on it
   - **Entry Points**: Where to hook in new functionality
3. Output should be concise (aim for 100-300 lines) - this is a summary, not a copy

Do NOT update CLAUDE.md. Just write to the `.claude/primed/` folder.

The goal is to create a disposable context file that a fresh chat can read
instead of re-reading all the raw files. Primes are single-use and will be
deleted after implementation.
