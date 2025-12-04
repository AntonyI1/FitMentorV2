Execute the implementation plan.

Feature name: $ARGUMENTS

Before starting, check `.claude/primed/` for any files related to this feature area.
Use primed context as your primary understanding of the codebase; only read
additional files if the primed context is missing something specific you need.

Requires both:
- `/docs/features/$ARGUMENTS.md`
- `/docs/plans/$ARGUMENTS-plan.md`

1. Read both documents
2. Follow phases in order
3. For each phase:
   - Complete fully before moving on
   - Write tests alongside code
   - Validate against acceptance criteria
4. After completion:
   - Run all tests
   - Update affected documentation
   - Commit with descriptive message

Rules:
- Complete each file before creating the next
- Handle all error states from feature doc
- Match existing code patterns

After implementation is complete:
- Delete any primed context files in `.claude/primed/` that were used for this feature
- Primes are single-use and should not persist after implementation
