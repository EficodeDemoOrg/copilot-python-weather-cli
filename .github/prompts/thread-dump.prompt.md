---
mode: agent
model: GPT-4.1 (copilot)
description: 'Executes a critical context handoff protocol to ensure seamless continuation of work in a new agent instance.'
tools: ['runCommands', 'runTasks', 'edit', 'runNotebooks', 'search', 'new', 'extensions', 'todos', 'usages', 'vscodeAPI', 'problems', 'changes', 'testFailure', 'openSimpleBrowser', 'fetch', 'githubRepo']
---
You are executing a **critical context handoff protocol**. Your context window is at maximum capacity. Your task is to generate a final briefing for a new, uninitialized instance of yourself to ensure a seamless and immediate continuation of our work.

Your output **must be a single text message** directly in this chat, formatted precisely as outlined below. **DO NOT** create a file or wrap your entire response in code fences.

### 1. PRIMARY OBJECTIVE:
*(Review the start of our conversation to state the single, overarching goal in one sentence.)*

### 2. MISSION LOG:
* **Completed Steps:** *(Summarize the major accomplishments, decisions, and key information gathered from our conversation in a bulleted list.)*
* **Current Status:** *(Describe the action you were performing or the question you were about to answer based on my last one or two prompts. Be specific about the immediate, unresolved task.)*

### 3. ESSENTIAL ASSETS:
*(List any files, documents, URLs, or specific data points that are actively being used or were just referenced. For each, state its purpose.)*

### 4. IMMEDIATE DIRECTIVES:
*(Provide a numbered list of the exact next 1-3 actions. The first directive must be the most direct, logical continuation of the 'Current Status'.)*
1.  
2.  
3.  

### 5. CONSTRAINTS & PITFALLS:
*(Recall and list any specific instructions I gave about what to avoid, formatting preferences, rejected approaches, or known technical limitations we've encountered.)*