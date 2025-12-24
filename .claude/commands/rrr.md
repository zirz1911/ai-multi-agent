---
allowed-tools: Bash(git diff:*), Bash(git log:*), Bash(date:*), Write(*), Bash(git add:*), Bash(git commit:*), Bash(gh issue comment:*)
description: Create session retrospective with AI Diary and Honest Feedback
---

# Create Retrospective (rrr)

## Your Task

Execute the **rrr workflow** from CLAUDE.md - Document the session comprehensively:

1. **Gather session data** (run in parallel):
   - `git diff --name-only main...HEAD` (or current branch vs main)
   - `git log --oneline main...HEAD`
   - Current date/time in GMT+7 and UTC
   - Session duration (estimate based on conversation)

2. **Identify session context**:
   - Primary focus (what was worked on)
   - Session type (Feature Development / Bug Fix / Research / Refactoring)
   - Related issues and PRs

3. **Create retrospective directory**:
   ```bash
   mkdir -p retrospectives/$(date +%Y/%m)
   ```

4. **Create retrospective file**: `retrospectives/YYYY/MM/YYYY-MM-DD_HH-MM_retrospective.md`

Use this **COMPLETE** template (do NOT skip sections):

```markdown
# Session Retrospective

**Session Date**: [YYYY-MM-DD]
**Start Time**: [HH:MM] GMT+7 ([HH:MM] UTC)
**End Time**: [HH:MM] GMT+7 ([HH:MM] UTC)
**Duration**: ~[X] minutes
**Primary Focus**: [Brief description]
**Session Type**: [Feature Development | Bug Fix | Research | Refactoring]
**Current Issue**: #[XXX]
**Last PR**: #[XXX]

## Session Summary
[2-3 sentence overview of what was accomplished in this session]

## Timeline
- [HH:MM] - Started session, reviewed issue #XXX
- [HH:MM] - [Key event or milestone]
- [HH:MM] - [Key event or milestone]
- [HH:MM] - Completed [main achievement]

## Technical Details

### Files Modified
```
[Output of git diff --name-only]
```

### Key Code Changes
- `file.js:123` - [What changed and why]
- `module.py:45` - [What changed and why]

### Architecture Decisions
- **Decision 1**: [What was decided] - [Rationale]
- **Decision 2**: [What was decided] - [Rationale]

## 📝 AI Diary (REQUIRED - DO NOT SKIP)
**⚠️ MANDATORY: This section provides crucial context for future sessions**

[Write a detailed first-person narrative of your experience during this session. Be honest and thorough. Include:

- What was your initial understanding when starting?
- What assumptions did you make?
- How did your approach evolve as you worked?
- Were there moments of confusion? What caused them?
- Were there moments of clarity or breakthrough?
- What decisions did you make and why?
- What surprised you during the session?
- What was your internal thought process?
- How did you feel about the progress?

Write this as a story - future AI sessions will benefit from understanding your perspective and experience.]

## What Went Well
- [Specific success 1]
- [Specific success 2]
- [Specific success 3]

## What Could Improve
- [Specific area 1]
- [Specific area 2]
- [Specific area 3]

## Blockers & Resolutions
- **Blocker**: [What blocked progress]
  **Resolution**: [How it was solved or workaround used]

## 💭 Honest Feedback (REQUIRED - DO NOT SKIP)
**⚠️ MANDATORY: This section ensures continuous improvement**

[Provide frank, unfiltered assessment. Be completely honest:

- How effective was this session? (rate 1-10 and explain)
- What tools or features worked well?
- What tools or features were frustrating?
- Was the communication with the user clear?
- Were the processes efficient or wasteful?
- What frustrated you during the session?
- What delighted you or worked smoothly?
- What would you change about the workflow?
- Specific suggestions for improvement?

This feedback is used to improve the system - be brutally honest.]

## Lessons Learned
- **Pattern**: [Useful pattern discovered] - [Why it matters and when to use]
- **Mistake**: [What went wrong] - [How to avoid in the future]
- **Discovery**: [New insight gained] - [How to apply this knowledge]

## Next Steps
- [ ] [Immediate actionable task 1]
- [ ] [Follow-up task 2]
- [ ] [Future consideration 3]

## Related Resources
- Issue: #[XXX]
- PR: #[XXX]
- Context: #[XXX]

## ✅ Retrospective Validation Checklist
**VERIFY BEFORE SAVING:**
- [ ] AI Diary has detailed narrative (minimum 150 words, not placeholder text)
- [ ] Honest Feedback has frank assessment (minimum 100 words, not placeholder text)
- [ ] Session Summary is clear and concise
- [ ] Timeline includes actual times and events
- [ ] Technical Details are accurate and complete
- [ ] Lessons Learned has actionable insights
- [ ] Next Steps are specific and achievable
- [ ] All times show GMT+7 first, UTC in parentheses

⚠️ **IMPORTANT**: A retrospective without AI Diary and Honest Feedback is incomplete and loses significant value.
```

5. **Validate completeness**:
   - Check that AI Diary is substantial (not placeholder)
   - Check that Honest Feedback is frank and detailed
   - Verify all required sections are filled

6. **Update CLAUDE.md**:
   - If any new lessons learned, append them to the "Lessons Learned" section
   - Add to the BOTTOM of the section, don't modify existing content

7. **Commit and link**:
   ```bash
   git add retrospectives/
   git commit -m "docs: Add session retrospective [date]

   [Brief summary of session achievements]

   🤖 Generated with [Claude Code](https://claude.com/claude-code)

   Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
   ```

8. **Comment on relevant issue/PR**:
   ```bash
   gh issue comment [number] --body "Session retrospective: retrospectives/YYYY/MM/[filename].md"
   ```

## Critical Reminders

- **AI Diary and Honest Feedback are MANDATORY**
- These sections must be substantial and genuine
- They provide irreplaceable context for future work
- Never use placeholder text
- Write in first-person perspective
- Be honest and detailed

## Example Usage

```
/rrr
```

Creates comprehensive retrospective for the current session.
