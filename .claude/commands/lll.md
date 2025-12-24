---
allowed-tools: Bash(gh issue list:*), Bash(gh pr list:*), Bash(git log:*), Bash(git status:*)
description: List Project Status - Show issues, PRs, and current state
---

# List Project Status (lll)

## Your Task

Execute these commands **in parallel** to get a comprehensive project overview:

1. **GitHub Issues**:
   ```bash
   gh issue list --limit 10 --json number,title,state,labels,createdAt --jq '.[] | "\(.number)\t\(.state)\t\(.title)\t(\(.labels | map(.name) | join(", ")))"'
   ```

2. **Pull Requests**:
   ```bash
   gh pr list --limit 5 --json number,title,state,headRefName --jq '.[] | "\(.number)\t\(.state)\t\(.headRefName)\t\(.title)"'
   ```

3. **Recent Commits**:
   ```bash
   git log --oneline -5
   ```

4. **Current Status**:
   ```bash
   git status
   ```

## Your Output

After gathering the data, provide a **visual summary** in this format:

```
📊 Project Status - [Project Name]

🎯 Current Focus
[Identify the main work in progress based on open issues/PRs]

📝 Open Issues ([count])
  #X [state] - [title] [labels]
  #Y [state] - [title] [labels]
  ...

🔀 Pull Requests ([count])
  #X [state] [branch] - [title]
  #Y [state] [branch] - [title]
  ...

📚 Recent Commits
  [hash] [commit message]
  [hash] [commit message]
  ...

🌿 Branch: [current branch]
   Status: [clean / X files changed]

💡 Suggested Next Steps
[Based on the current state, suggest 2-3 logical next actions]
```

## Guidelines

- Use emojis for visual clarity
- Highlight important information
- Provide actionable suggestions
- Keep it concise but informative
- Run all commands in parallel for speed

## Example Usage

```
/lll
```

Shows complete project status overview.
