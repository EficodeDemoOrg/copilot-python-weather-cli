---
agent: Lead Developer
description: "Create detailed implementation plan and context-efficient tasks"
---
Transform research into executable tasks optimized for limited context windows.

⚠️ **REQUIRED CONTEXT**: User must attach:
- The epic's ADR file
- `REQUIREMENTS-ANALYSIS.md` (used if `TEST-ANALYSIS.md` is not provided)

**OPTIONAL CONTEXT**:
- `TEST-ANALYSIS.md` (if provided, `REQUIREMENTS-ANALYSIS.md` will be ignored)

# PHASE 1: PLANNING

**MANDATORY OUTPUT FILE**: `docs/epic_<epic_name>/plans/IMPLEMENTATION_PLAN.md`

```markdown
# Implementation Plan: [Epic Name]
Generated: [Date]
Based on: docs/epic_[epic_name]/research/RESEARCH.md

## Objective
[From ADR - one sentence]

## Implementation Strategy
[3-4 sentences describing the approach]

## Task Decomposition Rationale
We divide this epic into [N] tasks to:
- Keep each task under 25k context tokens
- Ensure linear execution without blocking
- Minimize file switching per task

## Task Sequence
| # | Task Name | Files Touched | Est. Context | Dependencies |
|---|-----------|---------------|--------------|--------------|
| 01 | Create feature structure | 0 existing, 3 new | ~5k | None |
| 02 | Implement state slice | 1 existing, 1 new | ~10k | Task 01 |
| 03 | Create base component | 0 existing, 1 new | ~8k | Task 02 |

## Success Metrics
From ADR requirements:
- [ ] [Requirement 1]
- [ ] [Requirement 2]

## Risk Mitigations
| Risk (from research) | Mitigation Strategy | Implemented in Task # |
|---------------------|--------------------|-----------------------|
| [Risk] | [Strategy] | [Task number] |
```

# PHASE 2: DECISION DOCUMENTATION

**MANDATORY OUTPUT FILE**: `docs/epic_<epic_name>/plans/DECISION_LOG.md`

```markdown
# Decision Log: [Epic Name]
Generated: [Date]

## Decision 001: Task Granularity
**Choice**: Split into [N] tasks
**Rationale**: Each task touches max 3 files to stay under context limit
**Affects**: All tasks
**Trade-off**: More tasks but guaranteed context fit

## Decision 002: Implementation Order
**Choice**: [Describe sequence]
**Rationale**: [Why this order]
**Affects**: Tasks [numbers]
**Trade-off**: [What we sacrifice for this order]

[Continue for each significant decision...]
```

# PHASE 3: TASK GENERATION

For EACH task, create **MANDATORY OUTPUT FILE**: 
`docs/epic_<epic_name>/tasks/[NN]_[descriptive_name].md`

```markdown
# Task [NN]: [Clear, Specific Title]

## Meta
- **Estimated Context**: ~[X]k tokens
- **Files to Read**: [N] files
- **Files to Modify**: [M] files
- **Dependencies**: Task [NN-1] must be complete

## Objective
[Single sentence describing what THIS task accomplishes]

## Context Files Required
```yaml
required_context:
  - path: "docs/ADR/[EPIC]_ADR.md"
    sections: ["Decision", "Consequences"]
    reason: "Understand requirements"
  
  - path: "src/store/index.ts"
    lines: [12, 35]
    reason: "See reducer registration pattern"
```

## Implementation Steps

### Step 1: [Specific Action]
**File**: `src/weather_cli/[feature_name].py`
**Operation**: CREATE

Create new file with this content:
```python
"""Module for [feature description]."""
from dataclasses import dataclass
from typing import Optional
import logging

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class [FeatureName]Data:
    """Immutable data class for [feature]."""
    
    property1: str
    property2: float
    
    def __post_init__(self) -> None:
        """Validate data on construction."""
        if not isinstance(self.property1, str):
            raise TypeError("property1 must be a string")
        if not self.property1.strip():
            raise ValueError("property1 cannot be empty")


class [FeatureName]Service:
    """Service class for [feature] business logic."""
    
    def __init__(self, client: Optional[SomeClient] = None) -> None:
        """Initialize with optional dependency injection for testing."""
        self.client = client or DefaultClient()
        logger.info("[FeatureName]Service initialized")
    
    def process(self, input_data: str) -> [FeatureName]Data:
        """Process input and return feature data."""
        # ... implementation from research
        pass
```

### Step 2: [Next Specific Action]
**File**: `src/weather_cli/main.py`
**Operation**: MODIFY
**Location**: Line 12 (in import section)

Add import:
```python
from weather_cli.[feature_name] import [FeatureName]Service
```

**Location**: Line 45 (in main function, after service initialization)

Add service initialization:
```python
[feature_name]_service = [FeatureName]Service()
```

## Verification Checklist
- [ ] File `src/weather_cli/[feature_name].py` exists
- [ ] File has complete type hints (passes `mypy src`)
- [ ] All dataclasses use `@dataclass(frozen=True)` with `__post_init__` validation
- [ ] Services use dependency injection pattern
- [ ] No linting errors (`flake8 src tests`)
- [ ] Code is formatted (`black src tests`)

## Definition of Done
- [ ] All verification items checked
- [ ] Code follows patterns from `copilot-instructions.md`
- [ ] Data models match specification from RESEARCH.md
- [ ] Tests written covering happy path and error cases
- [ ] Test coverage >90% (`pytest --cov=weather_cli tests/`)
- [ ] API keys are redacted in logs (security requirement)

## Troubleshooting
If type checking errors occur:
1. Ensure all functions have complete type hints
2. Use `Optional[T]` for nullable types
3. Check imports are absolute (e.g., `from weather_cli.module import Class`)
4. Verify return types match function signatures

## Context Note
This task intentionally isolated to just state management.
UI components come in Task [NN+1].

# PHASE 4: COMPLETION MANIFEST

**MANDATORY OUTPUT FILE**: `docs/epic_<epic_name>/MANIFEST.md`

```markdown
# Task Manifest: [Epic Name]
Generated: [Date]

## Overview
- Total Tasks: [N]
- Total Context (all tasks): ~[X]k tokens
- Average Context per Task: ~[Y]k tokens

## Task List
| # | File | Purpose | Context Budget |
|---|------|---------|----------------|
| 01 | `tasks/01_create_data_model.md` | Create dataclasses | 5k |
| 02 | `tasks/02_implement_service.md` | Business logic layer | 10k |
| 03 | `tasks/03_add_tests.md` | Unit tests with mocks | 8k |
[...]

## Execution Instructions
1. Activate virtual environment: `source venv/bin/activate`
2. Execute tasks in numerical order
3. Run code quality gate after each task:
   - `black src tests` (format)
   - `flake8 src tests` (lint)
   - `mypy src` (type check)
   - `pytest --cov=weather_cli tests/` (tests)
4. Verify each task's DoD before proceeding
5. If a task fails, stop and report

## Deliverables
Upon completion, these files will exist:
- `src/weather_cli/[feature_name].py` (feature implementation)
- `tests/test_[feature_name].py` (unit tests with >90% coverage)
- [List all expected files]

STATUS: Planning complete. [N] tasks ready for implementation.
```