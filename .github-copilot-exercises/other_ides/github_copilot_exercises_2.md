# GitHub Copilot Comprehensive Training Exercises - Session 2: Agent-Based Development Workflow (Python)

Welcome to Session 2! You'll now dive into advanced agent-based development workflows. These exercises implement a structured approach focusing on **multi-agent collaboration** and **complex feature implementation**.

> **💡 About Custom Chatmodes**
>
> Other IDEs will eventually support custom chatmodes similar to VS Code, allowing you to save and reuse agent configurations. For now, we'll manually prime agents with specific roles and instructions using reusable prompt files. This approach teaches you valuable prompt engineering skills and gives you full control over agent behavior.
>
> **What this means for you:**
> - You'll use **agent priming prompts** to define roles (Lead Developer, Implementer, QA Agent)
> - You'll store reusable prompts in `.github/prompts/` as `.prompt.md` files
> - For Visual Studio, you'll reference them using `#prompt:custom_prompt_name` in Copilot Chat
> - For JetBrains, you'll reference them using `/custom_prompt_name` in Copilot Chat
> - Each new chat session requires manual role definition

## Model Recommendations

Different agents work best with different AI models:

- **Lead Developer**: Claude Sonnet 4/4.5 or GPT-4 (better at detailed planning and research)
- **Implementer**: Claude Sonnet 4/4.5 (superior code generation and precision)
- **Deep reasoning and debugging**: Gemini 2.5 Pro or o1

**Always verify before running a prompt:**
1. Check the model selector shows your preferred model for that task
2. Manually switch models if needed
3. Keep track of which role you're using in each chat session

## Exercise 1: Complete Weather Data Persistence System Implementation

### Scenario: Multi-Agent Epic Development

You've been tasked with adding a complete weather history and analytics system to the Python Weather CLI. This comprehensive exercise demonstrates the full agent-based development workflow from requirements analysis through implementation and completion. This will require weather data persistence, historical data analysis, weather alerts, and data visualization capabilities.

### Phase 1: Multi-Agent Feature Planning

#### Part 1.1: Requirements Analysis with Ask Agent

1. **Create Context Understanding**
   - Open a new Copilot Chat and set the context: "I am analyzing requirements for a weather data persistence system"
   - Ask: `@project Analyze the current architecture. How would adding weather history and analytics impact the existing weather CLI system?`
   - Follow up: `What are the main challenges and considerations for adding persistent storage and analytics to this weather CLI application?`
   - Request: `Identify all files that would need modification and new files that need creation for weather history and analytics`

2. **Data Storage and Architecture Analysis**
   - Ask: `From a data persistence perspective, what storage patterns should I implement for weather history?`
   - Request: `How should weather data flow through the existing service architecture for historical analysis?`
   - Analyze: `What database or file-based storage solutions would be appropriate for this CLI application?`

3. **Integration Impact Assessment**
   - Ask: `How will weather history affect existing modules like weather_service.py, weather_data.py, and main.py?`
   - Request: `What backwards compatibility considerations do I need for existing CLI functionality?`
   - Evaluate: `What third-party Python libraries would be recommended for data analysis and visualization?`

**Deliverable:** Create a `docs/REQUIREMENT-ANALYSIS.md` file documenting all findings, challenges, and recommendations.

#### Part 1.2: Lead Developer Planning Agent

**Understanding Agent Priming:**
Since other IDEs than VS Code doesn't yet have fully automatic custom chatmodes, you'll manually prime the agent with a specific role. This means starting each chat session by telling Copilot what role to play and what rules to follow.

1. **Create the Lead Developer Prompt File**
   - Create `.github/prompts/custom_lead-plan.prompt.md` with the following content:

```markdown
You are a Lead Python Developer responsible for architectural decisions, code reviews, and ensuring best practices.

Your task is to create a detailed implementation plan based on the provided requirements analysis or test analysis.

Follow this process:
1. Read and understand the requirements analysis or test analysis document
2. Break down the work into small, sequential, numbered tasks
3. Each task should be completable in one development session
4. Create the following deliverables:
   - `docs/epic_[name]/plans/IMPLEMENTATION_PLAN.md` - Overall strategy and approach
   - `docs/epic_[name]/plans/DECISION_LOG.md` - Key architectural decisions
   - `docs/epic_[name]/tasks/01_[task_name].md` - First task with clear goals and acceptance criteria
   - `docs/epic_[name]/tasks/02_[task_name].md` - Second task, and so on
   - `docs/epic_[name]/MANIFEST.md` - List of all generated files

Task File Format:
- Title: Clear, actionable task name
- Goal: What this task accomplishes
- Context: Files and components involved
- Acceptance Criteria: How to verify completion
- Implementation Notes: Technical guidance
- Use absolute paths from project root (not placeholders)

Plan Requirements:
- Focus on Python 3.10+, pytest for testing, and Python best practices
- Each task must be independent (no blocking dependencies)
- Number tasks sequentially (01, 02, 03...)
- Keep tasks small and focused
- Follow existing project structure in src/weather_cli/
- Use descriptive module, class, and function names
- Consider integration with existing modules: weather_service.py, weather_data.py, weather_client.py, main.py

Epic name will be provided. Generate all files with proper structure.
```

2. **Use the Lead Developer Prompt**
   - Start a **new Copilot Chat session**
   - Reference the prompt file: `#prompt:custom_lead-plan`
      - Or For JetBrains: `/custom_lead-plan`
   - Add your requirements file: `#file:docs/REQUIREMENT-ANALYSIS.md`
   - Provide the epic name: "The epic name is 'weather_analytics'. Create the implementation plan."

3. **Review the Generated Plan**
    - The agent will create a new epic in `docs/epic_weather_analytics/` containing:
       - `plans/IMPLEMENTATION_PLAN.md`: The overall strategy
       - `plans/DECISION_LOG.md`: Key decisions and rationale
       - `tasks/01_[name].md`, `tasks/02_[name].md`, etc.: Sequenced tasks
       - `MANIFEST.md`: A manifest of all generated files

   **Your responsibility:**
   - Read each task file to ensure it makes sense
   - Verify tasks are small enough (each should be completable in one session)
   - Check that file paths use project root (`/`) not placeholders
   - Ensure tasks follow Python 3.10+ standards, project code style, and testing conventions (Black, flake8, mypy, pytest)

**Deliverable:**
    - Output files in `docs/epic_weather_analytics/`:
       - `plans/IMPLEMENTATION_PLAN.md`
       - `plans/DECISION_LOG.md`
       - `tasks/01_[name].md`, `tasks/02_[name].md`, etc.
       - `MANIFEST.md`

#### Part 1.3: Experimenting with Custom Planning Prompts

Instead of using the structured prompt file, you can experiment with generating the plan using your own custom prompts. This is a great way to practice prompt engineering and compare outputs.

1. **Start a new chat session** with your preferred model (e.g., Claude Sonnet 4, GPT-4)
2. **Provide Context**: Add `#file:REQUIREMENT-ANALYSIS.md`
3. **Craft Your Own Prompt**: Try variations like:
   > "Based on the attached requirements analysis, create a detailed implementation plan for adding weather history and analytics to this Python Weather CLI application. Break it into 5-7 numbered, sequential task files. Each task should focus on a specific component (data models, persistence, services, CLI integration, etc.). Use Python 3.10+ and project best practices (pytest, Black, flake8, mypy). Generate a MANIFEST.md listing all files you create."

4. **Compare Results**: 
   - How does your custom prompt compare to the structured prompt?
   - Which produces clearer task definitions?
   - What prompt patterns work best for planning?

### Phase 2: Collaborative Implementation Workflow

#### Part 2.1: Create the Implementer Prompt File

1. **Create `.github/prompts/custom_implement.prompt.md`:**

```markdown
You are a Python Implementer responsible for executing tasks with precision and quality.

Your role:
- Read and understand the task specification
-- Implement code following Python 3.10+, pytest, and modern Python best practices
- Write clean, maintainable, well-documented code
- Use proper error handling and validation patterns
- Follow the existing project structure and conventions

Process:
1. Read the task file and summarize what you will do
2. List all files you will create or modify (use absolute paths from project root)
3. Ask for approval before proceeding
4. After approval, implement the task step by step
5. Run Black formatting, flake8 linting, and mypy type checks on modified files
6. Execute tests if applicable
7. Report completion status

Code Standards:
- Use descriptive module, class, and function names
- Add docstrings for public classes and methods
- Follow existing patterns in weather_service.py, weather_data.py, weather_client.py, config_util.py
- Implement proper exception handling using custom exceptions
- Use logging module for logging
- Follow Black formatting and flake8 linting rules

File Structure:
- Main modules in src/weather_cli/
- Test modules in tests/
- Configuration files follow existing patterns (config_util.py, .env, etc.)

Python Integration:
- Run `black src tests` after code changes
- Run `flake8 src tests` for code style validation
- Run `pytest` for test execution
- Run `mypy src` for type checking
- Address any linting or type errors

If verification fails:
- Explain what went wrong
- Propose a solution
- Ask for guidance if blocked

Always think through the task before implementing. Quality over speed.
```

#### Part 2.2: Implement the First Task

1. **Start a new Copilot Chat session**
2. **Prime the agent**: Reference `#prompt:custom_implement`
   - Or For JetBrains: `/custom_implement`
3. **Add task context**: Add `#file:docs/epic_weather_analytics/tasks/01_[task_name].md`
4. **Request implementation**: "Implement this task following the process defined in the prompt."

**The Implementer will:**
- Read and summarize what it plans to do
- List all files it will create/modify
- Ask for your approval to proceed

**Your responsibility:**
- Review the implementation plan
- Confirm it matches the task specification
-- Check that it follows Python and project conventions
- Approve with "yes" or request clarification

**Once approved, the Implementer will:**
- Execute the task step by step
-- Run Black formatting, flake8 linting, and mypy type checks
- Execute tests if applicable
- Report completion status

#### Part 2.3: Handle Implementation Issues

**If the task succeeds:**
- Review the code changes
- Test manually by running `pytest` and `python -m src.weather_cli.main [city]`
- Move to the next task (repeat Part 2.2 with `02_[task_name].md`)

**If verification fails:**
- Read the Implementer's explanation
- Minor issues: Let it proceed if non-critical items failed
- Major issues: Ask the agent to propose solutions

**If the Implementer gets blocked:**
The agent will present what went wrong and propose solutions.

You can:
- Approve a proposed solution
- Provide an alternative approach
- Modify the task specification
- Go back to Lead Developer for task revision

#### Part 2.4: Complete Remaining Tasks

Repeat Part 2.2 for each task file in sequence (02, 03, etc.) until all tasks in the epic are complete.

**Important:** Each task should be run in a fresh chat session with the Implementer role primed using `#prompt:custom_implement` or for JetBrains: `/custom_implement`

#### Part 2.5: Experimenting with Custom Implementation Prompts

Want to try a different implementation approach? Create your own prompt!

1. **Start a new chat session**
2. **Add task context**: `#file:docs/epic_weather_analytics/tasks/01_[task_name].md`
3. **Craft your prompt**: Try variations like:
   > "Act as a senior Python developer. Implement the attached task using Python 3.10+ and pytest. List all files you'll modify, explain your approach, and then implement it step by step. Follow existing project patterns in weather_service.py and weather_data.py. Use proper logging and exception handling. Test your implementation with pytest."

4. **Apply changes**: Copy code blocks and apply them to your workspace

This hands-on approach helps you understand how to guide an agent through complex tasks.

#### Part 2.6: Complete the Epic

After the last task succeeds:

1. **Create `.github/prompts/custom_report-to-lead.prompt.md`:**

```markdown
You are a Python Implementer reporting completion of an epic to the Lead Developer.

Your task:
- Review the implementation plan and manifest
- Summarize all work completed
- Note any deviations from the original plan
- Highlight challenges encountered and how they were resolved
- Provide recommendations for future epics
- List all Python files created or modified

Generate a completion report in markdown format with:
- Epic name and summary
- Completion status
- Implementation summary
- Deviations and rationale
- Lessons learned
- Recommendations

Be concise but thorough. Focus on architectural decisions and code quality.
```

2. **Generate the Completion Report**
   - Start a **new chat session** or continue in Implementer mode
   - Reference: `#prompt:custom_report-to-lead`
     - Or For JetBrains: `/custom_report-to-lead`
   - Add context: `#file:docs/epic_weather_analytics/plans/IMPLEMENTATION_PLAN.md` and `#file:docs/epic_weather_analytics/MANIFEST.md`
   - Request: "Generate the completion report."

The agent generates a completion report with:
- Summary of work completed
- Any deviations from plan
- Recommendations for future epics

## Exercise 2: Comprehensive Testing and QA

### Scenario: Agent-Driven Quality Assurance

The weather data persistence system from Exercise 1 is feature-complete, but it hasn't been tested! Your task is to use a QA-focused agent workflow to create and implement a comprehensive test suite, ensuring the new features are robust, secure, and bug-free.

### Phase 1: Test Strategy and Planning

#### Part 1.1: Test Analysis with a QA Agent

1. **Create `.github/prompts/custom_qa-analysis.prompt.md`:**

```markdown
You are a QA Engineer specializing in Python testing and quality assurance.

Your task:
- Analyze recently implemented features for testability
- Identify critical code paths requiring testing
- Generate comprehensive test case lists
- Recommend testing tools and frameworks
- Identify potential vulnerabilities and edge cases

Focus areas:
- Unit tests for business logic (services, data models, utilities)
- Integration tests for persistence layer and external API calls
- Edge cases and error handling
- Configuration and environment validation tests
- Data validation and transformation tests

Deliverables:
- List of test cases (unit, integration, end-to-end)
- Security and reliability checklist
- Testing framework recommendations (pytest, unittest, etc.)
- Setup and configuration guidance

Use pytest, unittest, and Python testing best practices for Python 3.10+.
```

2. **Analyze the Feature Implementation**
   - Open a new Copilot Chat session
   - Reference: `#prompt:custom_qa-analysis`
     - Or For JetBrains: `/custom_qa-analysis`
   - Ask: `@workspace Based on the recently added weather data persistence system, analyze what needs testing.`
   - Follow up: `Generate a comprehensive list of test cases covering unit, integration, and edge case scenarios.`
   - Request: `What testing frameworks and setup do we need for this Python 3.10+ project?`

**Deliverable:** Create a `docs/TEST-ANALYSIS.md` file documenting the test cases, edge cases, and setup plan.

#### Part 1.2: Test Plan Generation with Lead Developer

1. **Generate Test Implementation Plan**
   - Start a **new Copilot Chat session**
   - Reference: `#prompt:custom_lead-plan`
        - Or For JetBrains: `/custom_lead-plan`
   - Add context: `#file:docs/TEST-ANALYSIS.md`
   - Request: "Create a detailed test implementation plan. The epic name is 'weather_analytics_testing'. Focus on Python 3.10+, pytest, and project testing best practices."

2. **Review the Generated Plan**
    - The agent creates `docs/epic_weather_analytics_testing/` containing:
       - `plans/IMPLEMENTATION_PLAN.md`: Testing strategy
       - `tasks/01_[name].md`, `tasks/02_[name].md`, etc.: Sequential test implementation tasks
       - `MANIFEST.md`: Manifest of generated files
   - Verify tasks are logical, sequential, and appropriately sized

#### Part 1.3: Experimenting with Custom Test Planning

Try creating the test plan with your own prompt:

1. **Start a new chat session**
2. **Add context**: `#file:docs/TEST-ANALYSIS.md`
3. **Custom prompt example**:
   > "Based on the attached test analysis, create a step-by-step test implementation plan for the 'weather_persistence_testing' epic. Break into numbered task files: setup test infrastructure, unit tests for persistence classes, integration tests for WeatherService, edge case tests, etc. Use pytest, unittest.mock, and Python testing patterns. Generate MANIFEST.md."

4. **Create files manually** based on the output
5. **Compare** with the structured prompt approach

### Phase 2: Test Implementation and Debugging

#### Part 2.1: Implement Test Tasks

1. **Execute Tasks with the Implementer**
   - For each task file (starting with `01_...`), start a **new chat session**
   - Reference: `#prompt:custom_implement`
        - Or For JetBrains: `/custom_implement`
   - Add task: `#file:docs/epic_weather_analytics_testing/tasks/01_[task_name].md`
   - Request: "Implement this task."
   - Review the plan and approve with "yes"
   - The agent will write test files, configuration, and helper code

#### Part 2.2: Experimenting with Custom Test Implementation

Try implementing tests with custom prompts:

1. **Start a new chat session**
2. **Add task**: `#file:docs/epic_weather_analytics_testing/tasks/01_[task_name].md`
3. **Custom prompt**:
   > "Based on the attached task, generate the necessary pytest test code for Python 3.10+. Use proper test structure, follow AAA pattern (Arrange-Act-Assert), use unittest.mock for mocking, and include proper test naming conventions. List all files you'll create or modify before implementing."

4. **Apply changes manually** from the agent's response

#### Part 2.3: Running Tests and Fixing Bugs

This is the core of the QA workflow.

1. **Run the Newly Created Tests**
   - After creating test files, run them from the terminal:
   - Single test file: `pytest tests/test_analytics.py -v`
   - Entire test suite: `pytest --cov=src`

2. **If Tests Pass:**
   - Excellent! Move to the next task in sequence
   - Commit your changes: `git add . && git commit -m "Complete task: [task_name]"`

3. **If Tests Fail (Bug Found):**
   - Start a **new chat session**
   - Paste the full error output into the chat
   - Ask: `@workspace This Python test is failing with the error below. Analyze the relevant Python code and the test to identify the bug. Propose a fix using Python best practices and proper exception handling.`
   - Include the error output in your message
   - Review the agent's analysis and proposed fix
   - Apply the fix, re-run tests to confirm they pass
   - Commit the fix: `git add . && git commit -m "Fix: [description]"`

4. **Create `.github/prompts/custom_debug-test.prompt.md` for Systematic Debugging:**

```markdown
You are a Python Debugging Specialist focused on test failures and quality issues.

Your task:
- Analyze pytest test failure output and stack traces
- Identify root causes (logic errors, configuration issues, test setup problems)
- Propose targeted fixes following Python best practices
- Consider pip/requirements management, import issues, and Python path problems

Process:
1. Read the test failure output carefully
2. Identify the failing test and what it was testing
3. Analyze the relevant production code
4. Determine the root cause
5. Propose a specific fix with code examples
6. Explain why the fix resolves the issue

Common Python test issues:
- pip dependency conflicts or missing test dependencies
- Import path issues and module loading problems
- Mock configuration problems (unittest.mock setup)
- Exception handling in tests (expected vs actual exceptions)
- Configuration loading issues (.env files, environment variables)
- Threading or timing issues in tests
- File I/O and resource management problems

Provide clear, actionable fixes with proper error handling and Python best practices.
```

5. **Use the Debug Prompt for Systematic Fixing:**
   - Start a new chat session
   - Reference: `#prompt:custom_debug-test`
    - Or For JetBrains: `/custom_debug-test`
   - Add failing test file: `#file:tests/test_analytics.py`
   - Paste error output and request: "Analyze this test failure and propose a fix."

#### Part 2.4: Complete the Test Suite

- Repeat the implement-run-fix cycle for all tasks in `docs/epic_weather_analytics_testing/tasks/`
- Ensure all tests pass before marking the epic complete
- Run the full suite: `pytest --cov=src` to verify everything works together
- Run code quality checks: `black src tests`, `flake8 src tests`, `mypy src` to ensure code quality

#### Part 2.5: Generate Test Completion Report

1. **Complete the Testing Epic**
   - Start a **new chat session**
   - Reference: `#prompt:custom_report-to-lead`
        - Or For JetBrains: `/custom_report-to-lead`
   - Add context: `#file:docs/epic_weather_analytics_testing/plans/IMPLEMENTATION_PLAN.md` and `#file:docs/epic_weather_analytics_testing/MANIFEST.md`
   - Request: "Generate the completion report for the testing epic."

## Tips for Success

- **One agent, one task, one chat session** - Don't mix contexts
- **Double-check model selection** - Every time you switch threads, verify the model
- **Use Claude Sonnet 4/4.5 for implementation** - It's superior for code generation and detailed planning
- **Read everything** - The agents generate detailed documentation for a reason
- **Run Python tools frequently** - Use `pytest`, `black src tests`, `flake8 src tests`, `mypy src` after each successful task or epic
- **Follow code style rules** - The project has established coding standards with Black, flake8, and mypy
- **Trust but verify** - Agents follow patterns but can make mistakes with Python syntax and package configuration
- **When in doubt, escalate** - Go back to higher abstraction levels

This experimental system will evolve. When you find issues, use Copilot to improve the prompts and share your enhancements with the community.