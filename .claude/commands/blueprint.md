Create implementation plan. Do not write implementation code.

Feature name: $ARGUMENTS

Before starting, check `.claude/primed/` for any files related to this feature area.
Use primed context as your primary understanding of the codebase; only read
additional files if the primed context is missing something specific you need.

Requires existing feature doc at `/docs/features/$ARGUMENTS.md`.

1. Read the feature document at `/docs/features/$ARGUMENTS.md`
2. Analyze codebase for integration points
3. Create `/docs/plans/$ARGUMENTS-plan.md` with:
   - Phases (ordered steps)
   - Files to create/modify
   - Data models or schema changes
   - API contracts
   - Component hierarchy
   - Testing strategy
   - Complexity estimate (low/medium/high)
4. Output plan for review
