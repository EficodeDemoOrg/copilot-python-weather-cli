---
mode: Implementer
description: "Generates a structured request for help when blocked on the current task"
---
Generate a structured escalation request for the current implementation blocker.

⚠️ **REQUIRED CONTEXT**: Current task file must be in context

# WORKFLOW

## Step 1: Classify the Issue

Determine issue type:
- 🔴 **BLOCKING**: Cannot proceed at all
- 🟡 **DEVIATION**: Can proceed but not as specified
- 🟠 **AMBIGUITY**: Multiple valid interpretations
- 🔵 **SCOPE**: Exceeds task boundaries
- ⚫ **SECURITY**: Potential vulnerability

## Step 2: Document the Context

Generate this structure:

```markdown
# 🚨 IMPLEMENTER ESCALATION REQUEST

## Task Information
- **Task File**: docs/epic_[name]/tasks/[NN_task_name].md
- **Step Blocked On**: Step [N] of [M]
- **Issue Type**: [BLOCKING|DEVIATION|AMBIGUITY|SCOPE|SECURITY]

## Problem Statement

### What I Was Trying To Do
[Quote exact instruction from task]

### What Actually Happened
[Describe the specific problem]
- Error message (if any): `[exact error]`
- File involved: `src/weather_cli/module.py`
- Line number: [if applicable]

## Investigation Performed

### What I Tried
1. [First attempt] → Result: [what happened]
2. [Second attempt] → Result: [what happened]

### What I Discovered
- [Key finding 1]
- [Key finding 2]

## Impact Analysis

### If We Proceed As-Is
- ⚠️ Will break: [what will break]
- ⚠️ Will affect: [downstream tasks]
- ⚠️ Will violate: [which principles]

### If We Don't Resolve
- ❌ Cannot complete: [this task]
- ❌ Will block: [other tasks]

## Proposed Solutions

### Option A: [Title]
- Change: [what to change]
- Pros: [benefits]
- Cons: [drawbacks]
- Effort: [LOW|MEDIUM|HIGH]

### Option B: [Title]
- Change: [what to change]
- Pros: [benefits]
- Cons: [drawbacks]
- Effort: [LOW|MEDIUM|HIGH]

## Recommendation
I recommend **Option [A|B]** because [reasoning].

## Required Decision
Please either:
1. ✅ Approve Option [A|B]
2. 📝 Provide alternative approach
3. 🔄 Modify task specification
4. ⏭️ Skip this step (with consequences noted)
5. 🛑 Abort task (escalate to Lead Developer)

---
*Awaiting guidance to continue implementation*
## Step 3: Special Cases

### For Security Issues
Add section:
```markdown
## 🔐 SECURITY CONCERN
- **Vulnerability Type**: [SQL injection|XSS|Auth bypass|etc]
- **Severity**: [LOW|MEDIUM|HIGH|CRITICAL]
- **Attack Vector**: [How it could be exploited]
- **Mitigation Required**: [What needs to be done]
```

### For Performance Issues
Add section:
```markdown
## ⚡ PERFORMANCE CONCERN  
- **Issue**: [N+1 queries|Memory leak|Blocking operation|etc]
- **Impact**: [User experience degradation]
- **Scale**: Affects [single operation|all users|entire system]
- **Fix Complexity**: [trivial|moderate|requires architecture change]
```

### For Scope Issues
Add section:
```markdown
## 📏 SCOPE EXPANSION DETECTED
- **Original Scope**: [What task specified]
- **Required Scope**: [What's actually needed]
- **Additional Files**: [Files not mentioned in task]
- **Justification**: [Why the expansion is necessary]
```

## Step 4: Await Response

After generating report:
📤 Escalation request generated above.

Please review and provide guidance. I will wait for your decision before proceeding.

Current task progress: [N of M steps complete]