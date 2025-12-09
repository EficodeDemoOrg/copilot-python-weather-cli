# compliance-rules

[![Install with APM](https://img.shields.io/badge/📦_Install_with-APM-blue?style=flat-square)](https://github.com/danielmeppiel/apm#-apm-packages) 

An APM (Agent Package Manager) application with comprehensive agent context compilation examples.

## Quick Start

```bash
# Install dependencies
apm install

# Compile APM context into AGENTS.md
apm compile

# Run the hello world prompt
apm run start --param name="<YourGitHubHandle>"

# Run feature implementation workflow
apm run feature --param feature_name="User Authentication" --param feature_description="Implement secure user login and registration"

# Preview before execution
apm preview --param name="<YourGitHubHandle>"
```

## APM context Compilation

This project demonstrates the full APM context system:

### Available Primitives
- **Chatmodes**: `default`, `backend-engineer`
- **Instructions**: TypeScript, Python, Testing guidelines
- **Context**: Project information, Architecture guidelines

For specification-driven development, consider using [Spec-kit](https://github.com/github/spec-kit) alongside APM for complete SDD workflows combined with advanced context management.

### Compilation Commands
```bash
# Compile all primitives into AGENTS.md
apm compile

# Watch for changes and auto-recompile
apm compile --watch

# Validate primitives without compiling
apm compile --validate

# Dry run to preview output
apm compile --dry-run

# Use specific chatmode
apm compile --chatmode backend-engineer
```

### Directory Structure
```
.apm/
├── chatmodes/
│   ├── default.chatmode.md
│   └── backend-engineer.chatmode.md
├── instructions/
│   ├── typescript.instructions.md
│   ├── python.instructions.md
│   └── testing.instructions.md
└── context/
    ├── project-info.context.md
    └── architecture.context.md

```

## Available Workflows
- `hello-world.prompt.md` - Basic hello world demonstration
- `feature-implementation.prompt.md` - Implement features with validation gates

## About

This project was created with APM - The package manager for AI-Native Development.

Learn more at: https://github.com/github/apm-cli
