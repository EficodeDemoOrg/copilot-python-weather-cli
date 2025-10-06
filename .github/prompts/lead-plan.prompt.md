---
mode: Lead Developer
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
**File**: `src/features/[epic]/slice.ts`
**Operation**: CREATE

Create new file with this content:
```typescript
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface FeatureState {
  // ... specific properties from research
}

const initialState: FeatureState = {
  // ... from research
};

export const featureSlice = createSlice({
  name: '[epic]',
  initialState,
  reducers: {
    // ... specific reducers from research
  }
});

export const { actionName } = featureSlice.actions;
export default featureSlice.reducer;
```

### Step 2: [Next Specific Action]
**File**: `src/store/index.ts`
**Operation**: MODIFY
**Location**: Line 15 (after last reducer import)

Add import:
```typescript
import epicReducer from '../features/[epic]/slice';
```

**Location**: Line 35 (in combineReducers)

Add to reducers object:
```typescript
[epic]: epicReducer,
```

## Verification Checklist
- [ ] File `src/features/[epic]/slice.ts` exists
- [ ] File exports default reducer
- [ ] Store includes `[epic]` key in root state
- [ ] No TypeScript errors in modified files
- [ ] Redux DevTools shows `[epic]` in state tree

## Definition of Done
- [ ] All verification items checked
- [ ] Code follows pattern from `src/features/users/slice.ts`
- [ ] State shape matches specification from RESEARCH.md
- [ ] Manual test: State updates visible in Redux DevTools

## Troubleshooting
If TypeScript errors occur:
1. Check import paths are relative
2. Verify type exports from slice
3. Ensure RootState type is updated

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
| 01 | `tasks/01_create_structure.md` | Set up directories | 5k |
| 02 | `tasks/02_implement_state.md` | Redux slice | 10k |
[...]

## Execution Instructions
1. Execute tasks in numerical order
2. Verify each task's DoD before proceeding
3. If a task fails, stop and report

## Deliverables
Upon completion, these files will exist:
- `src/features/[epic]/` (directory structure)
- `src/features/[epic]/slice.ts` (state management)
- [List all expected files]

STATUS: Planning complete. [N] tasks ready for implementation.
```