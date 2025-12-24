---
allowed-tools: Bash(git status:*), Bash(git log:*), Bash(git branch:*), Bash(gh issue create:*), Bash(ls:*), Bash(date:*)
argument-hint: [brief-session-description]
description: Create Context & Compact - Save session state to GitHub issue
---

# Create Context & Compact (ccc)

## Your Task

Execute the **ccc workflow** from CLAUDE.md:

1. **Gather git context** by running these commands in parallel:
   - `git status --porcelain`
   - `git log --oneline -5`
   - `git branch --show-current`
   - `ls -la`

2. **Create comprehensive GitHub context issue** with this format:

```markdown
# Session Context

**Date**: [current date YYYY-MM-DD]
**Time**: [current time HH:MM GMT+7 (HH:MM UTC)]
**Branch**: [current branch name]
**Last Commit**: [latest commit hash]

## Current State

### Working Directory Status
[git status output - describe if clean or list changes]

### Recent Commits
```
[git log output]
```

### Project Structure
```
[ls -la output - key directories and files]
```

## Key Discoveries

[Analyze the recent conversation and list 2-3 key findings, decisions, or insights from this session]

## Current Focus

**Task**: [Brief description based on argument $1 or recent conversation context]

## Next Steps

[List 3-5 logical next steps based on current work]

## Session Notes

[Important observations, user preferences, or context from this session]

## Open Questions

[List any unresolved questions or decisions that need to be made]

---
*This is a context issue for session continuity. Refer to this when resuming work.*
```

3. **Use this title format**:
   - If argument provided: `context: $1`
   - Otherwise: `context: Session state - [infer from recent conversation]`

4. **After creating the issue**:
   - Show the issue URL
   - Remind user: "✅ Context issue created! Don't forget to run `/compact` to optimize the conversation."

## Guidelines

- Be thorough but concise in the issue body
- Include actual command outputs, not placeholders
- Analyze the conversation to provide meaningful context
- Always use GMT+7 (Bangkok) as primary timezone
- The issue should be immediately useful for resuming work later

## Example Usage

```
/ccc Implementing authentication system
```

This creates issue: "context: Implementing authentication system"
