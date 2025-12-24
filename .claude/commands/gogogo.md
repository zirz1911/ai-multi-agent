---
allowed-tools: Bash(gh issue view:*), Read(*), Write(*), Edit(*), Bash(git add:*), Bash(git commit:*), Bash(git push:*), Bash(gh pr create:*), Bash(npm:*), Bash(pytest:*), Bash(python:*)
argument-hint: [#issue-number]
description: Execute implementation plan step-by-step
---

# Execute Implementation (gogogo)

## Your Task

Execute the **gogogo workflow** from CLAUDE.md - Implement the planned solution:

1. **Find the implementation plan**:
   - If argument provided: Use issue #$1
   - Otherwise: Find the most recent `plan:` issue
   - View the issue: `gh issue view [number]`

2. **Execute implementation step-by-step**:
   - Follow the plan's implementation steps in order
   - Check off each step as completed
   - Make all necessary code changes
   - Follow existing codebase patterns

3. **Testing**:
   - Run relevant tests after implementation
   - Verify functionality works as expected
   - Check for errors or warnings
   - Test edge cases mentioned in the plan

4. **Commit & Push**:
   - Stage all changes: `git add -A`
   - Create descriptive commit message:
     ```
     [type]: [Brief description from plan]

     - What: [Specific changes made]
     - Why: [Motivation from plan]
     - Impact: [What this affects]

     Closes #[plan-issue-number]
     ```
   - Push to feature branch
   - If branch doesn't exist, create: `git checkout -b feat/issue-[number]-[description]`

5. **Create/Update Pull Request**:
   - Create PR if it doesn't exist:
     ```bash
     gh pr create --title "[Same as commit]" --body "Implements #[issue-number]"
     ```
   - Return the PR URL

6. **⚠️ CRITICAL - DO NOT MERGE**:
   - **NEVER** use `gh pr merge`
   - Provide PR URL and wait for user review
   - User will merge when ready

## Guidelines

- Follow the plan exactly (don't add extra features)
- Test thoroughly before committing
- Use descriptive commit messages
- Respect the safety rules from CLAUDE.md
- **NEVER** use force flags (-f, --force)
- Ask for clarification if plan is unclear

## Commit Message Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting, no code change
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

## Example Usage

```
/gogogo #3
```

Implements the plan from issue #3.

```
/gogogo
```

Implements the most recent plan issue.
