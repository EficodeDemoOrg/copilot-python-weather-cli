# GitHub Copilot Comprehensive Training Exercises - Session 2: Agent-Based Development Workflow (Python Edition)

Welcome to Session 2! You'll now dive into advanced agent-based development workflows. These exercises implement the structured approach outlined in our development specs, focusing on **multi-agent collaboration**, and **complex feature implementation**.

## Model Recommendations

Different agents work best with different AI models

- **Lead Developer**: Claude Sonnet 4/4.5 (better at detailed planning and research)
- **Implementer**: Claude Sonnet 4/4.5 (superior code generation and precision)
- **Deep reasoning and debugging**: Gemini 2.5 Pro

**Always verify before running a prompt:**
1. Check the chatmode selector shows the correct agent
2. Check the model selector shows your preferred model for that agent
3. Manually switch back if needed

## Exercise 1: Complete Weather History and Analytics System Implementation

### Scenario: Multi-Agent Epic Development

You've been tasked with adding a complete weather history and analytics system to the Python Weather CLI. This comprehensive exercise demonstrates the full agent-based development workflow from requirements analysis through implementation and completion. This will require weather data persistence, historical data analysis, weather alerts, and data visualization capabilities.

### Phase 1: Multi-Agent Feature Planning

#### Part 1.1: Requirements Analysis with Ask Agent

1. **Create Context Understanding**
   - Open a new Copilot Chat and select **Ask** from the agent picker
   - Set the context: "I am analyzing requirements for a weather history and analytics system"
   - Ask: `@workspace #codebase Analyze the current architecture. How would adding weather history and analytics impact the existing weather CLI system?`
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

#### Part 1.2: Strategic Planning with Plan Agent

1. **Create High-Level Implementation Strategy**
   - Start a fresh Copilot Chat session
   - Select **Plan** from the agent picker
   - Attach the `REQUIREMENT-ANALYSIS.md` file as context
   - Request: `Create a strategic plan for implementing weather history and analytics in this application. Break down the work into logical phases and identify dependencies.`

   **The Plan agent will:**
   - Analyze the requirements and create a high-level implementation strategy
   - Identify major phases of work (e.g., data storage setup, analytics engine, visualization, CLI integration)
   - Suggest the order of implementation
   - Highlight potential risks and dependencies

2. **Review and Refine the Strategy**
   - Review the strategic plan provided by the Plan agent
   - Ask follow-up questions to clarify any ambiguous areas
   - Request: `What are the critical milestones for this implementation?`
   - Ask: `What would be a good MVP (Minimum Viable Product) for this feature?`

**Deliverable:** Document the strategic plan in `docs/epic_weather_analytics/STRATEGIC_PLAN.md`

#### Part 1.3: Detailed Task Planning with Lead Developer Agent

1. **Convert Strategy into Executable Tasks**
   - Start a fresh Copilot Chat session
   - In the chat interface, locate the agent picker dropdown
   - Select **"Lead Developer"** custom agent from the picker
   - Attach both `REQUIREMENT-ANALYSIS.md` and `STRATEGIC_PLAN.md` as context
   - Use the reusable prompt: `/lead-plan`

   **The Lead Developer will:**
   - Convert the strategic plan into detailed, actionable tasks
   - Generate numbered task files (01_task_name.md, 02_task_name.md, etc.)
   - Document technical decisions in a decision log
   - Create a task manifest

   **Task numbering:** Tasks are numbered sequentially (01, 02, 03...) to enforce execution order. Each task is designed to be completed without blocking on others.

2. **Review the Detailed Plan**
   - Read each task file to ensure it makes sense
   - Verify tasks are small enough (each should be completable in one session)
   - Check that file paths use project structure (`src/weather_cli/`, `tests/`, etc.)
   - Ensure tasks align with the strategic plan from Part 1.2

   **Deliverable:**
   - Output files in `docs/epic_weather_analytics/`:
   - `plans/IMPLEMENTATION_PLAN.md`
   - `plans/DECISION_LOG.md`
   - `tasks/01_[name].md`, `tasks/02_[name].md`, etc.
   - `MANIFEST.md`

#### Part 1.4: Experimenting with Custom Planning Prompts (Optional)

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

#### Part 2.1: Implement the Tasks

1. Start a **new chat session**
2. Select the **Implementer** chatmode
3. **Set model to Claude Sonnet 4 or 4.5** (best for precise code generation)
4. Drag the first task file as a context: `docs/epic_weather_analytics/tasks/01_[task_name].md`
5. Run: `/implement`

The Implementer will:
- Read and summarize what it plans to do
- List all files it will create/modify
- Ask for your approval to proceed

**Your responsibility:**
- Review the implementation plan
- Confirm it matches the task specification
- Approve with "yes" or request clarification

Once approved, the Implementer will:
- Execute the task step by step
- Run Python linter (`black`, `flake8`, `mypy`) on modified files
- Execute tests with `pytest` if applicable
- Report completion status

#### Step 2.2: Handle Implementation Issues

**If the task succeeds:**
- Review the code changes
- Verify type hints follow Python 3.10+ standards
- Move to the next task (repeat Step 6 with `02_[task_name].md`)

**If verification fails:**
- Read the Implementer's explanation
- Minor issues (linting warnings): Let it proceed if non-critical items failed
- Major issues (type errors, test failures): The Implementer will use `/ask_advice`

**If the Implementer gets blocked:**
The agent will present an escalation request with:
- What went wrong
- What was attempted
- Proposed solutions

You can:
- Approve a proposed solution
- Provide alternative approach
- Modify the task specification
- Abort and go back to Lead Developer for task revision

#### Step 2.3: Complete Remaining Tasks

Repeat Step 2.2 for each task file in sequence (02, 03, etc.) until all tasks in the epic are complete.

**Important:** Each task should be run in a fresh Implementer session with just that task file as context.

#### Part 2.4: Experimenting with Custom Implementation Prompts (Optional)

Want to try a different implementation approach? Create your own prompt!

1. **Start a new chat session**
2. **Add task context**: `#file:docs/epic_weather_analytics/tasks/01_[task_name].md`
3. **Craft your prompt**: Try variations like:
   > "Act as a senior Python developer. Implement the attached task using Python 3.10+ and pytest. List all files you'll modify, explain your approach, and then implement it step by step. Follow existing project patterns in weather_service.py and weather_data.py. Use proper logging and exception handling. Test your implementation with pytest."

4. **Apply changes**: Copy code blocks and apply them to your workspace

This hands-on approach helps you understand how to guide an agent through complex tasks.

#### Part 2.5: Complete the Epic

After the last task succeeds:

1. Stay in **Implementer** mode or start new session
2. Attach:
   - `docs/epic_weather_analytics/plans/IMPLEMENTATION_PLAN.md`
   - `docs/epic_weather_analytics/MANIFEST.md`
3. Run: `/report_to_lead`

The Implementer generates a completion report with:
- Summary of work completed
- Any deviations from plan
- Recommendations for future epics

## Exercise 2: Comprehensive Testing and QA

### Scenario: Agent-Driven Quality Assurance

The weather analytics system from Exercise 1 is feature-complete, but it hasn't been tested! Your task is to use a QA-focused agent workflow to create and implement a comprehensive test suite, ensuring the new features are robust, reliable, and bug-free.

### Phase 1: Test Strategy and Planning

#### Part 1.0: Create a Custom QA Agent

Before beginning test analysis, create a specialized QA agent to focus on testing concerns.

1. **Create the QA Agent File**
   - In your project, create the directory `.github/agents/` if it doesn't exist
   - Create a new file: `.github/agents/QA Specialist.agent.md`

2. **Define the QA Agent**
   - Define the Agent as required. Refer to the existing custom agents for structure.

3. **Verify Agent Availability**
   - Open Copilot Chat
   - Click the agent picker dropdown
   - Verify **"QA Specialist"** appears in the list of available agents

**Deliverable:** Custom QA Specialist agent ready to use for test analysis.

#### Part 1.1: Test Analysis with QA Specialist Agent

1. **Analyze the Feature Implementation**
   - Open a new Copilot Chat session
   - Select **"QA Specialist"** from the agent picker
   - Provide context by attaching relevant implementation files or using `@workspace #codebase`
   - Ask: `@workspace #codebase Based on the recently added weather analytics system, what are the critical code paths that require testing?`
   - Follow up: `Generate a list of test cases covering unit, integration, and end-to-end scenarios for weather data persistence, historical analysis, and CLI commands.`
   - Request: `What are the primary error conditions (like API failures, data corruption, or file system issues) we should test for in the weather analytics flow?`

2. **Python Testing Framework and Setup Recommendations**
   - Ask: `Given the Python project structure with pytest, what additional testing patterns would you recommend for CLI applications?`
   - Request: `Outline the steps and code needed to enhance the existing pytest setup for testing the new analytics features.`
   - Analyze: `How should we test CLI argument parsing and output formatting for the new analytics commands?`

**Deliverable:** Create a `docs/TEST-ANALYSIS.md` file documenting the test cases, error conditions, and setup plan.

#### Part 1.2: Test Strategy with Plan Agent

1. **Create High-Level Test Strategy**
   - Start a fresh Copilot Chat session
   - Select **Plan** from the agent picker
   - Attach the `TEST-ANALYSIS.md` file as context
   - Request: `Create a strategic test plan for the weather analytics system. Organize tests by priority (critical, high, medium) and type (unit, integration, e2e). Identify dependencies between test suites.`

2. **Review and Prioritize**
   - Review the test strategy provided by the Plan agent
   - Identify which tests are essential for MVP vs. nice-to-have
   - Request: `What tests are absolutely critical before deploying to production?`

**Deliverable:** Document the test strategy in `docs/epic_weather_analytics_testing/TEST_STRATEGY.md`

#### Part 1.3: Manual Plan Generation (Alternative Approach)

As an alternative to using structured agents, you can experiment with generating the plan manually using the built-in Agent mode. This is a great way to understand how to craft effective prompts and compare the outputs of different models.

1. **Start a new chat session** and select **Agent** from the agent picker
2. **Provide Context**: Drag both `TEST-ANALYSIS.md` file into the chat
3. **Prompt the Agent**: Use a custom prompt to generate the plan. For example:
   > "Based on the attached `TEST-ANALYSIS.md`, create a detailed, step-by-step implementation plan for the "weather_analytics_testing" epic. Break the work into small, numbered, sequential task files following Python testing best practices. For each task, define a clear goal and acceptance criteria. Also generate a MANIFEST.md file listing all the files you will create."
4. **Create Files Manually**: Based on the agent's output, create the directory structure (`docs/epic_weather_analytics_testing/`) and the corresponding plan, task, and manifest files yourself.

This approach gives you more fine-grained control and is an excellent exercise in prompt engineering.

**Deliverable:** Document the test strategy in `docs/epic_weather_analytics_testing/TEST_STRATEGY.md`

#### Part 1.4: (Recommended) Detailed Test Plan with QA Specialist Agent

1. **Create the Test Implementation Plan**
   - Start a new Copilot Chat session and select **"QA Specialist"** from the agent picker
   - Provide both `TEST-ANALYSIS.md` and `TEST_STRATEGY.md` files as context
   - Use the prompt: `/lead-plan Create a detailed, step-by-step test implementation plan based on the provided analysis and strategy. The epic name is "weather_analytics_testing".`
   
   **Note:** The `/lead-plan` prompt works with any custom agent. The QA Specialist will use its testing expertise to create test-focused tasks.

2. **Review the Generated Plan**
   - The QA Specialist agent will create a new epic in `docs/epic_weather_analytics_testing/` containing:
     - `plans/IMPLEMENTATION_PLAN.md`: The overall test implementation strategy
     - `plans/DECISION_LOG.md`: Testing framework and approach decisions
     - `tasks/01_[name].md`, `tasks/02_[name].md`, etc.: Sequenced tasks like:
       - Enhancing pytest configuration for analytics testing
       - Writing unit tests for the weather storage module
       - Writing integration tests for analytics CLI commands
       - Creating error condition test cases (API failures, data corruption, etc.)
       - Implementing edge case tests
     - `MANIFEST.md`: A manifest of all generated files
   - Verify that the tasks are logical, sequential, and appropriately sized
   - Confirm that all error conditions and edge cases from earlier analysis are covered

#### Part 1.5: Experimenting with Custom Test Planning (Optional)

Try creating the test plan with your own prompt:

1. **Start a new chat session**
2. **Add context**: `#file:docs/TEST-ANALYSIS.md`
3. **Custom prompt example**:
   > "Based on the attached test analysis, create a step-by-step test implementation plan for the 'weather_persistence_testing' epic. Break into numbered task files: setup test infrastructure, unit tests for persistence classes, integration tests for WeatherService, edge case tests, etc. Use pytest, unittest.mock, and Python testing patterns. Generate MANIFEST.md."

4. **Create files manually** based on the output
5. **Compare** with the structured prompt approach

### Phase 2: Test Implementation and Debugging

#### Part 2.1: Implement the Test Tasks

1. **Execute Tasks with the Implementer**
   - For each task file (starting with `01_...`), start a **new chat session** with the **"Implementer"** agent.
   - Drag the task file into the chat as context.
   - Run the `/implement` command.
   - Review the Implementer's plan and approve it by typing "yes".
   - The agent will write the test files, configuration, and any necessary helper code following Python conventions.

#### Part 2.2: Experimenting with Custom Test Implementation

Try implementing tests with custom prompts:

1. **Start a new chat session**
2. **Add task**: `#file:docs/epic_weather_analytics_testing/tasks/01_[task_name].md`
3. **Custom prompt**:
   > "Based on the attached task, generate the necessary pytest test code for Python 3.10+. Use proper test structure, follow AAA pattern (Arrange-Act-Assert), use unittest.mock for mocking, and include proper test naming conventions. List all files you'll create or modify before implementing."

4. **Apply changes manually** from the agent's response

#### Part 2.3: Running Tests and Fixing Bugs

This is the core of the Python QA workflow.

1. **Run the Newly Created Tests**
   - After the Implementer creates a test file, run it from your terminal:
     ```bash
     # Run specific test file
     pytest tests/test_analytics.py -v
     
     # Run with coverage
     pytest tests/test_analytics.py --cov=src/weather_cli
     
     # Run all tests
     pytest --cov=src
     ```

2. **Run Code Quality Checks**
   ```bash
   # Format code
   black src tests
   
   # Check linting
   flake8 src tests
   
   # Type checking
   mypy src
   ```

3. **If Tests Pass:**
   - Congratulations! Move to the next task in the sequence.

4. **If Tests Fail (Bug Found):**
   - Start a **new chat session**.
   - Paste the full error output from the failed test run into the chat.
   - Ask: `@workspace #codebase This Python test is failing with the error below. Analyze the relevant code and the test to identify the bug. Propose a fix that maintains type safety and follows our coding standards.`
   - Review the agent's analysis and the proposed code change.
   - Apply the fix, re-run the test to confirm it passes, and then commit your changes.

5. **If Linting or Type Checking Fails:**
   - Address formatting issues with `black src tests`
   - For type errors, ask the agent: `This mypy error needs to be fixed while maintaining type safety. Propose a solution.`

#### Part 2.4: Complete the Test Suite

- Repeat the implement-run-fix cycle for all tasks in the `docs/epic_weather_analytics_testing/tasks/` directory until the entire test suite is implemented and all tests are passing.
- Ensure final code coverage meets project standards (aim for >90% coverage on new code).

## Tips for Success

- **One agent, one task, one chat session** - Don't mix contexts
- **Double-check agent and model** - Every time you switch threads, verify the agent picker and model picker show the correct selections
- **Use Claude Sonnet 4/4.5 for implementation** - It's superior for code generation and detailed planning
- **Start fresh when stuck** - If an agent loses context or becomes confused, start a new chat session with clear context
- **Start fresh when stuck** - If an agent loses context or becomes confused, start a new chat session with clear context
- **Read everything** - The agents generate detailed documentation for a reason
- **Commit frequently** - After each successful task or epic
- **Trust but verify** - Agents follow patterns but can make mistakes
- **When in doubt, escalate** - Go back to higher abstraction levels

This experimental system will evolve. When you find issues, use Copilot to improve the prompts and share your enhancements with the community.