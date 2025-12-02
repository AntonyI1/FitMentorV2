Execute the implementation plan.

Feature name: $ARGUMENTS

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
