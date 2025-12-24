---
allowed-tools: Bash(gh issue view:*), Bash(gh issue create:*), Read(*), Glob(*), Grep(*)
argument-hint: [#issue-number]
description: Next Task Planning - Create detailed implementation plan (analysis only, no coding)
---

# Next Task Planning (nnn)

## Your Task

Execute the **nnn workflow** from CLAUDE.md - Analysis & Planning ONLY (NO CODING):

1. **Check for recent context issue**:
   - If no recent context issue exists, remind user to run `/ccc` first
   - Context issues have title format: "context: ..."

2. **Gather context**:
   - If argument provided: Analyze issue #$1 using `gh issue view $1`
   - Otherwise: Find and analyze the most recent open issue
   - Read relevant codebase files to understand current state

3. **Deep analysis** (spend time on this):
   - Read context and understand the problem thoroughly
   - Analyze affected components using Read, Glob, Grep tools
   - Research existing patterns in the codebase
   - Identify all files that need changes

4. **Create comprehensive plan issue** with this format:

```markdown
# Implementation Plan

## Problem Statement
[Clear description of what needs to be done and why]

## Research & Analysis

### Current State
[What exists now - be specific with file names and line numbers]

### Affected Components
- `path/to/file1.js:123` - [what needs to change]
- `path/to/file2.py:45` - [what needs to change]

### Existing Patterns
[Patterns found in codebase that should be followed]

## Proposed Solution

### Architecture Overview
[High-level approach and design decisions]

### Implementation Steps

#### Phase 1: [Name] (~1 hour)
- [ ] Step 1: [Specific, actionable task]
- [ ] Step 2: [Specific, actionable task]
- [ ] Step 3: [Specific, actionable task]

#### Phase 2: [Name] (~1 hour)
- [ ] Step 1: [Specific, actionable task]
- [ ] Step 2: [Specific, actionable task]

[Add more phases if needed, but prefer 1-hour chunks]

## Risks & Considerations
- **Risk 1**: [Description] - [Mitigation]
- **Risk 2**: [Description] - [Mitigation]

## Testing Strategy
- [ ] Unit tests: [specific tests needed]
- [ ] Integration tests: [specific scenarios]
- [ ] Manual testing: [specific checks]

## Success Criteria
- [ ] [Specific, measurable criterion]
- [ ] [Specific, measurable criterion]
- [ ] [Specific, measurable criterion]

## Related Issues
- Context: #[context-issue-number]
- Related: #[other-issues]

---
*Ready for implementation with `gogogo`*
```

5. **Issue title format**: `plan: [Brief description of what will be implemented]`

6. **After creating the plan**:
   - Show the issue URL
   - Provide brief summary of the plan
   - Suggest: "Run `gogogo` to start implementation"

## Guidelines

- **NO CODING** - This is analysis and planning only
- Break large tasks into 1-hour phases
- Be specific with file paths and line numbers
- Consider existing codebase patterns
- Include risks and testing strategy
- Make steps actionable and clear

## Example Usage

```
/nnn #5
```

Analyzes issue #5 and creates a detailed implementation plan.

```
/nnn
```

Finds the most recent open issue and creates a plan.
