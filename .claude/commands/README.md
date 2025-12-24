# Claude Code Slash Commands

Custom slash commands for the AI Multi-Agent project, implementing the workflows from `CLAUDE.md`.

## Available Commands

### 🔄 Context Management

#### `/ccc [description]`
**Create Context & Compact** - Save current session state to a GitHub issue.

```bash
/ccc Implementing authentication system
```

**What it does:**
1. Gathers git context (status, log, branch)
2. Creates comprehensive GitHub context issue
3. Reminds you to run `/compact`

**When to use:** Before switching tasks or when you need to save session state.

---

### 📋 Planning & Execution

#### `/nnn [#issue-number]`
**Next Task Planning** - Create detailed implementation plan (analysis only, NO coding).

```bash
/nnn #5          # Plan based on issue #5
/nnn             # Plan based on most recent issue
```

**What it does:**
1. Analyzes the specified or most recent issue
2. Researches codebase and patterns
3. Creates comprehensive implementation plan with phases
4. Identifies risks and testing strategy

**When to use:** After creating a feature/bug issue, before starting implementation.

---

#### `/gogogo [#issue-number]`
**Execute Implementation** - Follow the plan step-by-step.

```bash
/gogogo #3       # Implement plan from issue #3
/gogogo          # Implement most recent plan
```

**What it does:**
1. Finds the implementation plan issue
2. Executes each step sequentially
3. Tests thoroughly
4. Commits, pushes, and creates PR
5. **Never merges** - waits for your review

**When to use:** After creating a plan with `/nnn`.

---

### 📊 Status & Review

#### `/lll`
**List Project Status** - Show issues, PRs, commits, and current state.

```bash
/lll
```

**What it does:**
1. Lists open issues and PRs
2. Shows recent commits
3. Displays current branch status
4. Suggests next steps

**When to use:** When starting work or checking project status.

---

#### `/rrr`
**Create Retrospective** - Document session with AI Diary and Honest Feedback.

```bash
/rrr
```

**What it does:**
1. Gathers session data (commits, changes, time)
2. Creates comprehensive retrospective document
3. **Requires** AI Diary (first-person narrative)
4. **Requires** Honest Feedback (frank assessment)
5. Updates CLAUDE.md with lessons learned
6. Commits and links to relevant issues

**When to use:** At the end of a work session.

---

## Recommended Workflow

The commands are designed to work together in this pattern:

```
1. /lll              → Check project status
2. /ccc              → Save current context (if switching tasks)
3. /nnn #X           → Create implementation plan for issue #X
4. /gogogo           → Execute the plan
5. /rrr              → Document the session
```

### Example Session Flow

```bash
# Start of session
/lll                                    # What's the current state?

# Working on a new feature
/nnn #12                                # Create plan for issue #12
/gogogo                                 # Implement the plan
# ... test, review ...

# End of session
/rrr                                    # Document what was done
/ccc Planning next phase                # Save context for next time
```

## Command Locations

These commands are **project-specific** (stored in `.claude/commands/`). When committed to git, all team members automatically get access to them.

If you want **personal commands** (just for you), create them in:
```
~/.claude/commands/
```

## Key Principles

1. **Always create issues before implementation** (per CLAUDE.md)
2. **Never merge PRs yourself** - wait for user review
3. **Never use force flags** (-f, --force)
4. **Break work into 1-hour phases**
5. **AI Diary and Honest Feedback are mandatory** in retrospectives

## Safety Rules

From CLAUDE.md:

- ❌ Never use `git push --force`
- ❌ Never use `rm -rf`
- ❌ Never use `gh pr merge` without explicit permission
- ✅ Always test thoroughly before committing
- ✅ Always follow existing codebase patterns
- ✅ Always document decisions and learnings

## Troubleshooting

**Command not found?**
- Ensure you're in the project directory
- Check that `.claude/commands/` exists
- Restart Claude Code if needed

**Command fails?**
- Check that `gh` (GitHub CLI) is installed and authenticated
- Verify git repository is properly configured
- Review command output for specific errors

## Documentation

For more details, see:
- `CLAUDE.md` - Full AI assistant guidelines
- [Claude Code Slash Commands Docs](https://code.claude.com/docs/en/slash-commands.md)

---

**Last Updated**: 2024-12-24
**Version**: 1.0.0
