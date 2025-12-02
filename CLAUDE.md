# FitMentor V2

## Project Context

Evidence-based fitness coaching app. All requirements are in `/docs/PRD.md`. Read it before any work.

## Principles

- No partial implementations. Every feature is complete or not started.
- No placeholder code. If it exists, it works.
- No TODO comments. Resolve everything now.
- Follow existing patterns. Check the codebase before introducing new conventions.
- Minimal dependencies. Only add packages that provide clear value.

## Slash Commands

### /feature

Define and document a new feature. Do not write implementation code.

1. Read PRD.md for context
2. Create `/docs/features/<name>.md` with:
   - Overview (2-3 sentences)
   - User stories
   - Acceptance criteria (measurable)
   - Technical requirements (endpoints, models, components)
   - Dependencies (existing code this touches)
   - Edge cases and error states
3. Output summary

---

### /blueprint

Create implementation plan. Requires existing feature doc at `/docs/features/<name>.md`. Do not write implementation code.

1. Read the feature document
2. Analyze codebase for integration points
3. Create `/docs/plans/<name>-plan.md` with:
   - Phases (ordered steps)
   - Files to create/modify
   - Data models or schema changes
   - API contracts
   - Component hierarchy
   - Testing strategy
   - Complexity estimate (low/medium/high)
4. Output plan for review

---

### /implement

Execute the plan. Requires both:
- `/docs/features/<name>.md`
- `/docs/plans/<name>-plan.md`

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

---

## Code Standards

- Self-documenting code; comments explain why, not what
- Functions do one thing
- Fail fast with clear error messages
- Tests cover happy path + edge cases

## When Uncertain

1. Check PRD.md
2. Check existing codebase
3. Check feature/plan docs
4. Ask for clarification

Do not assume. Do not improvise requirements.
