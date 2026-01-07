# GitHub Copilot Comprehensive Training Exercises

Welcome to your comprehensive GitHub Copilot training journey! These exercises are designed to progressively learn GitHub Copilot's features starting with foundational concepts and building up to advanced techniques through hands-on practice with our Python weather CLI project.

## Phase 1: Getting Started with Copilot Basics

### Exercise 1.1: Understanding Your Python Weather CLI Project with Chat Participants

**Welcome to the project!** Before diving into code generation, let's use GitHub Copilot to understand the Python weather CLI application you'll be working with.

1. **@workspace Participant - Project Overview**
   - Press `Ctrl+Alt+I` (or `Cmd+Alt+I`) to open Copilot Chat and select **Ask** from the agent picker
   - Ask: `@workspace Tell me about this Python weather CLI project?`
   - Try: `@workspace /explain Give me a comprehensive overview of this weather application`
   - Request: `@workspace What are the main features and components I should know about?`

2. **@workspace Participant - Code Structure**
   - Ask: `@workspace How are the Python modules organized in this project?`
   - Try: `@workspace Show me all the exception handling patterns used`
   - Request: `@workspace How are dependencies managed with pip and pyproject.toml?`

3. **@vscode Participant - Development Setup**
   - Ask: `@vscode What Python extensions would help with development in this project?`
   - Try: `@vscode How do I configure debugging for this Python CLI application?`
   - Request: `@vscode How to set up tasks for Python development and testing?`

4. **@terminal Participant - Running the Project**
   - Ask: `@terminal What's the best way to run this Python weather CLI application?`
   - Try: `@terminal Show me common Python dependency management commands for this project`
   - Request: `@terminal How do I run pytest tests from command line?`

**Learning Goal:** Use different chat participants to get familiar with the Python project structure, setup, and workflow before starting development.

### Exercise 1.2: First Steps with Code Suggestions

1. **Explore Auto-Suggestions**
   - Open `src/weather_cli/weather_data.py`
   - Position your cursor at the end of the file and press Enter
   - Type `# Method to check if weather is considered severe` and press Enter
   - Watch Copilot suggest a method implementation
   - Try accepting the suggestion with `Tab`.

2. **Practice with Comments**
   - Add this comment: `# Calculate temperature difference from average for the season`
   - Let Copilot suggest the implementation
   - Notice how descriptive comments lead to better suggestions

3. **Experiment with Method Names**
   - Start typing `def format_temperature` and see what Copilot suggests
   - Try `def is_rainy` and observe the different suggestion

4. **Quick Edits with Inline Chat**
   - With `src/weather_cli/weather_data.py` still open, select any method
   - Press `Ctrl+I` (or `Cmd+I` on Mac) to open inline chat directly in the editor
   - Try: "Add a docblock comment to this method"
   - Notice how inline chat allows quick edits without leaving your code

**Learning Goal:** Understand how Copilot uses context and comments to generate relevant Python code suggestions.

### Exercise 1.3: Exploring the Suggestion Interface

1. **Navigation Practice**
   - Open `src/weather_cli/config_util.py`
   - Add a comment: `# Validate API key format using regex`
   - Hover mouse over the suggestion to see alternative suggestions
   - Press `tab` to accept a suggestion

2. **Partial Acceptance**
   - Start typing a function and accept only part of a suggestion using `Ctrl+→` or `Cmd+→`
   - Try modifying the suggestion before accepting it

**Learning Goal:** Master the Copilot interface and keyboard shortcuts.

### Exercise 1.4: Introduction to Copilot Chat

1. **Opening Chat**
   - Press `Ctrl+Alt+I` (or `Cmd+Alt+I`) to open Copilot Chat
   - Select **Ask** from the agent picker
   - Open `src/weather_cli/main.py` in VS Code
   - Ask: "Explain what this file does"

2. **Basic Chat Questions**
   - Ask: "What are the main components of this weather CLI application?"
   - Try: "How is the weather API integration handled in this project?"
   - Notice how Copilot provides explanations and guidance

**Learning Goal:** Get comfortable with basic Copilot Chat interactions.

### Exercise 1.5: Understanding Built-in Agents

VS Code provides **four built-in agents** that you can switch between using the **agent picker** in the Chat view. Each agent is optimized for different tasks.

1. **Ask Agent - Questions & Explanations**

   - Select **Ask** from the agent picker in the Chat view
   - Ask questions about code without making changes
   - Try: "What design patterns are used in this codebase?"
   - Notice how Ask provides explanations, guidance, and learning resources

2. **Edit Agent - Direct Code Changes**

   - Select **Edit** from the agent picker
   - Add files as context using the **Add Context** button or by opening them in the editor
   - Request: "Add input validation to this method"
   - Observe how Edit focuses on making targeted code changes to specific files

3. **Agent - Autonomous Coding**

   - Select **Agent** from the agent picker (this is the most powerful mode)
   - Agent autonomously plans and executes complex tasks
   - It can run terminal commands, create/modify multiple files, and iterate on solutions
   - Try: "Create a temperature conversion utility class for this weather project"
   - Notice how Agent determines what needs to be done and makes changes across your workspace

4. **Plan Agent - Strategic Planning**
   - Select **Plan** from the agent picker
   - Use for breaking down complex features into actionable steps
   - Try: "Create a plan for adding weather alerts to this application"
   - Plan helps you think through implementation before coding

**Learning Goal:** Understand when and how to use each of the four built-in agents for different development tasks.

### Exercise 1.6: Setting Up Project Context with Copilot Instructions

**Why This Matters:** Creating a `copilot-instructions.md` file helps Copilot understand your project's specific patterns, conventions, and architecture, leading to more accurate and relevant suggestions throughout your development session.

1. **Generate Instructions Using VS Code**

   - Open the Chat view
   - Click the **Configure Chat (gear icon ⚙️)** button in the Chat view
   - Select **"Generate Chat Instructions"** from the menu
   - VS Code will analyze your codebase and create a `.github/copilot-instructions.md` file
   - Wait for the generation process to complete

2. **Review the Generated Instructions**

   - Open the newly created `.github/copilot-instructions.md` file
   - Read through the generated content to understand what Copilot discovered about your project
   - Notice how it identifies:
     - Project architecture and patterns
     - Key conventions and coding styles
     - Important file structures and relationships
     - Development workflows and commands

3. **Test the Instructions with Copilot**

   - Open Copilot Chat
   - Ask: "Based on the project instructions, explain the main architecture of this application"
   - Try: "Following this project's patterns, how would I add a new field to the WeatherData model?"
   - Request: "What are the key conventions I should follow when adding a new service method?"
   - Compare the responses to earlier interactions - they should be more specific and aligned with your project

4. **Explore Additional Instruction Types (Optional)**
   VS Code now supports multiple types of instruction files:

   - **`.github/copilot-instructions.md`** - Applies to all chat requests in the workspace
   - **`.instructions.md` files** - Use `applyTo` patterns to target specific file types (e.g., only Python files)
   - **`AGENTS.md`** - Useful when working with multiple AI agents

   To create additional instruction files:

   - Click **Configure Chat (gear icon) → Chat Instructions → New instruction file**
   - Choose whether to store in your workspace or user profile

5. **Refine the Instructions (Optional)**
   - If you notice any missing patterns or inaccurate information in the generated instructions
   - Edit the `.github/copilot-instructions.md` file to add project-specific details
   - Consider adding information about:
     - Specific coding conventions you follow
     - Common debugging approaches
     - Testing strategies used in the project

**Learning Goal:** Understand how to leverage VS Code's instruction generation feature to provide Copilot with better project context, resulting in more accurate and relevant code suggestions.

---

## Phase 2: Mastering Chat Commands

### Exercise 2.1: Basic Slash Commands

1. **Understanding Code with `/explain`**
   - Select the `get_weather()` method in `src/weather_cli/weather_service.py`
   - Type: `/explain #selection`
   - Try: `/explain How do the service and client classes interact?`
   - Compare explanations with different context levels

2. **Code Documentation with `/doc`**
   - Select the `WeatherData` class constructor
   - Type: `/doc #selection`
   - Try: `/doc Generate comprehensive docstrings for this weather data class`

3. **Quick Fixes with `/fix`**
   - Create intentional issues (missing imports, wrong variable name)
   - Use: `/fix` to address the issues
   - Try: `/fix Address all PEP 8 compliance issues in this file`

**Learning Goal:** Master basic slash commands for common Python development tasks.

### Exercise 2.2: Code and Structure Generation with `/new`

1. **Simple Utility Creation**

   - Try: `/new Create a weather data formatting utility class for this project`
   - Experiment: `/new Generate a cache manager that fits this weather CLI architecture`
   - Advanced: `/new Create a plugin system for weather data sources`

2. **Folder and File Structure Creation**

   - Try: `/new Create a new folder structure for weather data providers with client interfaces`
   - Experiment: `/new Generate a plugins directory with sample weather source plugin architecture` (Note: always check where the workspace is getting created)
   - Advanced: `/new Create a complete testing structure with unit and integration test directories`

3. **Multi-file Component Generation**
   - Request: `/new Create a weather alerting module with service, data model, and notification components`
   - Try: `/new Generate a weather history system with data storage and analysis modules`

**Learning Goal:** Learn to use `/new` for generating code components, folder structures, and multi-file modules.

### Exercise 2.3: Generating Tests with `/tests`



1. **Unit Test Generation**
   - Open `src/weather_cli/weather_data.py`
   - Select the `WeatherData` class constructor
   - In chat: `/tests #selection`
   - Examine the generated pytest test structure

2. **Service Testing**
   - Select a method from `src/weather_cli/weather_service.py`
   - Use `/tests` and observe how Copilot handles more complex scenarios
   - Ask follow-up questions like "How would I mock the API client dependencies?"

3. **Custom Test Scenarios**
   - Ask: "Generate edge case tests for the weather API client error handling"
   - Request: "Create integration tests for the WeatherService class"

**Learning Goal:** Understand how to generate comprehensive tests and testing strategies.

---

## Phase 3: Chat Variables and Context Control

> **💡 Context Setup Guide**  
> 
> **Using #file**: Start typing `#` and begin typing the filename you want to add as context. VS Code will show you a dropdown of available files to choose from. Select the file you want and it will appear as `#file` in your prompt.
> 

### Exercise 3.1: Chat Variables Deep Dive  

1. **File Context Variables**
   - Select `src/weather_cli/weather_service.py` in Explorer
   - Ask: `Analyze the code structure in #file`
   - Try with different files: `What potential issues exist in #file?`

2. **Selection and Editor Variables**
   - Select a method in any Python file
   - Ask: `Optimize this code #selection for better performance`
   - With cursor in editor: `What's the context around #editor position?`

3. **Codebase Structure Analysis**

   - Ask: `What design patterns are used in #codebase?`
   - Try: `How is error handling implemented across #codebase?`
   - Request: `Show me the data flow in #codebase`

4. **Terminal Context Variables**

   - Run a command in the terminal and select the output
   - Ask: `Explain this error #terminalSelection`
   - Or reference the last command: `What does #terminalLastCommand do?`
   - Try: `Debug the issue shown in #terminalSelection`

5. **Web Content and External Repositories**

   - Fetch content from a URL: `Summarize the main points #fetch https://code.visualstudio.com/updates`

6. **Advanced Variable Combinations**
   - Try: `@workspace #codebase What would be the impact of adding weather data caching?`
   - Experiment: `#file #selection How does this relate to the overall weather CLI architecture?`
   - Combine multiple contexts: `Compare #selection with similar code in #file and #codebase patterns`

**Learning Goal:** Master chat variables and tools for precise context control and analysis.

---

## Phase 4: Advanced Context and File Analysis

### Exercise 4.1: Working with File Context

1. **File-Based Questions**
   - Open `src/weather_cli/weather_service.py`
   - Ask: "What design patterns are used in #file?"
   - Try: "How can I improve error handling in #file?"
   - Request: "Explain the dependency injection pattern in #file"

2. **Cross-File Analysis**
   - Ask: "How does weather_service.py interact with weather_client.py?"
   - Request: "Show me the data flow from WeatherService to WeatherData model"

**Learning Goal:** Learn to leverage file context for deeper code understanding.

---

## Phase 5: Practical Development Scenarios

### Exercise 5.1: Feature Development Guidance

1. **Planning New Features**
   - Open Copilot Chat in Ask mode
   - `I want to add weather alerts functionality. How should I implement this feature?`
   - `Walk me through adding multiple weather data sources to this application`
   - `How would I add weather history tracking without breaking existing functionality?`

2. **Implementation Guidance**
   - Ask: `Show me step-by-step how to add temperature unit conversion`
   - Request code examples for each step
   - Ask for configuration strategies for API keys and settings

**Learning Goal:** Learn to use Copilot for weather CLI feature planning and implementation guidance.

### Exercise 5.2: Debugging and Problem Solving

1. **Common Issues**
   - Open Copilot Chat in Ask mode
   - Ask: `What could cause the weather API requests to fail silently?`
   - Request: `How should I debug API connection and timeout issues?`

2. **Error Handling Improvements**
   - Ask: `How can I improve error handling throughout this weather CLI application?`
   - Request: `Show me best practices for logging in Python CLI applications`

**Learning Goal:** Develop debugging skills for Python CLI applications with Copilot assistance.

---

## Phase 6: Specialized Agent Interactions

### Exercise 6.1: Security-Focused Reviews

1. **Security Agent Role**
   - Open Copilot Chat
   - `Act as a security expert and review the configuration handling in src/weather_cli/config_util.py`
   - `As a security specialist, what vulnerabilities do you see in the API client?`
   - `From a security perspective, how should I improve the API key management?`

2. **Security Best Practices**
   - `What security issues should I check for in this CLI application?`
   - `Provide specific security improvements for API key and sensitive data handling`

**Learning Goal:** Learn to use Copilot for security-focused code reviews in Python CLI applications.

### Exercise 6.2: Performance and Code Quality

1. **Performance Expert Role**
   - Open Copilot Chat
   - `As a performance expert, analyze the efficiency of WeatherService.py`
   - `How can I optimize the HTTP requests and JSON parsing?`

2. **Code Quality Reviewer**
   - `Act as a senior Python developer and review the code quality in the src/weather_cli directory`
   - `What Python coding standards and best practices should I implement in this codebase?`

**Learning Goal:** Understand how different expert perspectives can improve your code.

### Exercise 6.3: Code Review Workflow

GitHub Copilot provides built-in code review capabilities directly in VS Code, allowing you to get instant feedback on your code without leaving the editor.

1.  **Context Menu Code Review**

    - Right-click anywhere in an open file
    - Select **Copilot → Review and Comment** from the context menu
    - Copilot will analyze the file and provide inline review comments
    - Navigate through the suggestions using the review panel

2.  **Targeted Code Reviews with Selection**

    - Select specific methods or sections you want reviewed
    - Use: `/review #selection` for focused analysis
    - Ask follow-up questions: `Are there any edge cases I'm missing in #selection?`
    - Request specific reviews: `/review #selection for security vulnerabilities`

3.  **Custom Review Requests in Chat**

    - Open Copilot Chat and select **Ask** from the agent picker
    - Ask: `Act as a senior code reviewer and analyze this file for quality, performance, and best practices`
    - For specific concerns: `Review this code for potential race conditions and concurrency issues`
    - Request architecture feedback: `Are there any design pattern violations or anti-patterns here?`

4.  **Implementing Review Feedback**
    - Switch to the **Edit** agent in Copilot Chat
    - Reference the review findings: `Based on the code review feedback, apply the recommended security improvements`
    - Ask: `Generate updated code that addresses these review comments`
    - Use inline chat (`Ctrl+I` or `Cmd+I`) for quick fixes to specific issues
    - Review and accept the changes into your workflow

**Learning Goal:** Master code review workflows to catch issues and improve code quality before committing.

---

## Phase 7: Advanced Context Optimization

### Exercise 7.1: Strategic Context Building

1. **Minimal vs. Maximum Context**

   - Ask the same question with different context levels:
     - Minimal: `How do I add validation?`
     - Medium: `How do I add validation to #file?`
     - Maximum: `@workspace #codebase How do I add consistent validation across all controllers following the existing patterns?`
   - Compare response quality and relevance

2. **Context Layering Technique**
   - Start broad: `@workspace What's the error handling strategy?`
   - Layer specific: `#file How does this service handle exceptions?`
   - Drill down: `#selection Improve this error handling logic`
   - Notice how each layer builds understanding

3. **Cross-Reference Optimization**
   - Use multiple file references: `Compare error handling approaches in weather_service.py vs weather_client.py`
   - Combine selection with file context: `How does #selection relate to patterns in #file?`
   - Mix variables effectively: `#codebase #selection Where else is this pattern used?`

### Exercise 7.2: Context Quality Assessment  
1. **Response Quality Testing**
   - Ask the same question 3 different ways with varying context
   - Rate responses on: accuracy, completeness, actionability
   - Document which context combinations work best for different question types

2. **Context Efficiency**
   - Time how long different context levels take to process
   - Find the sweet spot between comprehensive context and response speed
   - Learn when minimal context is sufficient vs. when maximum context is necessary

**Learning Goal:** Master the art of providing optimal context for different scenarios.

### Exercise 7.3: Leveraging Multiple LLMs for Specialized Tasks

VS Code allows you to switch between different AI models using the **model picker** in the chat input field. Different models are optimized for different tasks - some excel at complex reasoning, others at fast code generation.

1. **Scenario: Adding Weather Alert Notifications - A Multi-Model Workflow**

   **Step 1: Analysis with a Reasoning Model**

   - Click the **model picker** in the Chat view and select a reasoning-focused model (e.g., o1, o3-mini, or similar)
   - Ask: `Looking at the current weather CLI structure in this project, what would be the architectural implications of adding weather alert notifications? What potential issues should I consider?`
   - Follow up with: `Based on the existing WeatherService and WeatherData model, what's the most logical way to integrate alert functionality without breaking current functionality?`

   **Step 2: Implementation with a Code Generation Model**

   - Switch to a code-optimized model (e.g., Claude Sonnet, GPT-4o, or similar)
   - Say: `Based on the analysis above, generate the code changes needed to add weather alert functionality to the weather CLI. Include alert threshold validation and notification methods.`
   - Then: `Now generate the corresponding service changes to handle alert checking and triggering.`

   **Step 3: Documentation with a Fast Model**

   - Switch to a faster model for quick tasks (e.g., GPT-4o-mini, Claude Haiku, or similar)
   - Request: `Get the current git status and create a summary of what files would be changed for this weather alert feature.`
   - Follow with: `Generate a concise commit message and brief documentation for these weather alert changes.`

   **Step 4: Validation with a Reasoning Model**

   - Return to the reasoning model and ask: `Review the generated code changes. Are there any logical flaws or edge cases I should address before implementing?`

2. **Exploring Available Models**

   - Click the model picker to see all available models for your subscription
   - Note: Available models vary based on your Copilot subscription and may change over time

3. **Reflect on the Multi-Model Experience**
   - Compare how each model approached their specialized task
   - Note the differences in reasoning depth, code quality, and response speed
   - Consider how this workflow could be applied to other feature development scenarios

**Learning Goal:** Master a practical multi-model workflow that leverages each LLM's strengths for analysis, implementation, and project management tasks.

---

## Phase 8: Advanced Prompt Engineering with Custom Agents

### Exercise 8.1: Understanding Custom Agents

VS Code allows you to create **custom agents** (`.agent.md` files) that define specialized personas with specific tools, instructions, and behaviors. This repository includes two custom agents in `.github/agents/`.

1. **Explore the Custom Agents in This Repository**

   - Open `.github/agents/Implementer.agent.md` and review its structure:
     - **description**: Brief summary of the agent's purpose
     - **tools**: List of VS Code tools the agent can use (edit, search, runCommands, etc.)
     - **Instructions**: Detailed behavioral guidelines in the body
   - Open `.github/agents/Lead Developer.agent.md` and compare the differences

2. **Using Custom Agents**

   - Open the Chat view
   - Click the **agent picker** dropdown
   - Your custom agents appear alongside the built-in agents (Agent, Plan, Ask, Edit)
   - Select **Implementer** to activate that persona

3. **Practice with the Implementer Agent**

   - With Implementer selected, notice it follows a strict execution protocol:
     - Reads task specifications precisely
     - Creates TODO lists before implementing
     - Focuses only on code changes, not planning
   - Try: "Add a `format_for_display()` method to the WeatherData class"
   - Observe how it follows its defined execution phases

4. **Practice with the Lead Developer Agent**

   - Switch to **Lead Developer** in the agent picker
   - This agent focuses on planning and research, never writing production code
   - Try: "Analyze the architecture for adding weather forecast functionality"
   - Notice how it decomposes the problem into tasks rather than implementing directly

5. **Creating Your Own Custom Agent (Optional)**
   - Click **Configure Chat (gear icon) → Custom Agents → New agent**
   - Define the agent's description, allowed tools, and behavioral instructions
   - Consider creating agents for: code review, documentation, testing, or security analysis

**Learning Goal:** Understand how custom agents extend Copilot's capabilities with specialized personas and workflows.

### Exercise 8.2: Role-Based Collaboration with Custom Agents

1. **Simulate a Lead Developer / Implementer Workflow**

   This exercise demonstrates how custom agents can work together like a real development team:

   **Step 1: Planning with Lead Developer**

   - Select **Lead Developer** from the agent picker
   - Ask: "Create a plan for adding weather forecast functionality (5-day forecast) to this application"
   - The Lead Developer will:
     - Analyze the existing codebase
     - Identify files that need changes
     - Break down the work into discrete tasks
   - Review the generated plan

   **Step 2: Implementation with Implementer**

   - Switch to **Implementer** in the agent picker
   - Reference the plan: "Implement the first task from the weather forecast feature plan"
   - The Implementer will:
     - Follow the task specification precisely
     - Create a TODO list of changes
     - Execute the code modifications
   - Review and approve the changes

   **Step 3: Iterate**

   - Return to Lead Developer for the next task assignment
   - Switch back to Implementer to execute
   - Continue until the feature is complete

2. **Understanding Agent Boundaries**
   - Notice how Lead Developer refuses to write production code
   - Notice how Implementer focuses only on execution, not architecture decisions
   - This separation prevents scope creep and maintains quality

**Learning Goal:** Master role-based collaboration using custom agents that mirror real team dynamics.

### Exercise 8.3: Reusable Prompt Files

VS Code supports **prompt files** (`.prompt.md`) that define reusable prompt templates you can invoke with `/` commands. This repository includes several prompts in `.github/prompts/`.

1. **Explore the Available Prompt Files**

   - Open `.github/prompts/` and review the available prompts:
     - `implement.prompt.md` - For executing implementation tasks
     - `lead-plan.prompt.md` - For creating implementation plans
     - `ask_advice.prompt.md` - For getting guidance and recommendations
     - `report_to_lead.prompt.md` - For reporting progress back to lead developer

2. **Using Prompt Files**

   - In the Chat view, type `/` to see available prompt commands
   - Your custom prompts appear alongside built-in commands like `/new`, `/explain`, `/fix`
   - Select a prompt to insert its template into the chat

3. **Practice with Implementation Prompts**

   - Use `/implement` when working with the Implementer agent
   - Use `/lead-plan` when working with the Lead Developer agent
   - Notice how prompts and agents work together for structured workflows

4. **Creating Your Own Prompt Files (Optional)**
   - Click **Configure Chat (gear icon) → Prompt Files → New prompt file**
   - Define reusable templates for common tasks in your workflow
   - Consider creating prompts for: code reviews, documentation, testing scenarios

**Learning Goal:** Leverage reusable prompt files to standardize common workflows and ensure consistency across your team.

### Exercise 8.4: Effective Context Management

1. **Context Window Awareness**

   - Be aware that each thread has a limited context window
   - When a conversation gets long, create a summary before starting a new thread

2. **Creating Handoff Documents**

   - Before closing a complex thread, ask: "Summarize our discussion and decisions in a format I can use to continue in a new thread"
   - Save these summaries in your project docs

3. **Thread Hygiene**
   - Name your threads descriptively
   - Close threads when their purpose is complete
   - Don't mix different concerns in the same thread

**Learning Goal:** Master the art of managing multiple focused agent threads effectively.

---

## Phase 9: Creative and Exploratory Exercises

### Exercise 9.1: Code Refactoring Challenges

1. **Refactoring Scenarios**
   - `How would you refactor the WeatherService to use dependency injection patterns?`
   - `Show me how to implement the Repository pattern for weather data access.`

2. **Design Pattern Implementation**
   - `How could I implement the Observer pattern for weather condition changes?`
   - `Show me how to add a Factory pattern for creating different weather data sources.`

**Learning Goal:** Explore advanced Python programming concepts with Copilot's guidance.

### Exercise 9.2: Alternative Implementations

1. **Different Approaches**
   - `Show me 3 different ways to implement weather data caching.`
   - `What are alternative approaches to API client configuration management?`

2. **Technology Comparisons**
   - `How would this application look if built with Click framework instead of argparse?`
   - `Compare this implementation with an async/await approach using aiohttp.`

**Learning Goal:** Understand different Python implementation strategies and trade-offs.

### Exercise 9.3: Multi-Thread Task Management with Custom Agents

This exercise demonstrates how to use multiple chat views with different custom agents to organize complex development workflows. Each chat maintains its own context and agent selection, allowing you to separate concerns like planning, implementation, and review.

1. **Opening Multiple Chat Views**

   - Open the Chat view
   - Click the **"+"** button in the Chat view toolbar to create a new chat thread
   - Each thread maintains its own conversation history and context

2. **Scenario: Implementing Weather Data Persistence - Organized Workflow**

   **Setup: Create Two Chat Panels Side-by-Side**

   - Create a new chat thread
   - Right-click the Chat tab → **"Split Right"**
   - You now have two independent chat views

   **Left Panel: Lead Developer (Planning)**

   - In the left chat panel, select **Lead Developer** from the agent picker
   - Ask: `I need to add weather data persistence to this CLI application. What's the overall architecture and implementation strategy you recommend?`
   - Follow up: `Create a detailed implementation plan with data storage considerations and SQLite integration.`
   - The Lead Developer agent will analyze the codebase and provide a strategic plan
   - **Copy the plan text** to share with the implementation thread or **Save the plan**: Ask the agent to `Create a PLANNING.md file with this weather persistence plan`

   **Right Panel: Implementer (Execution)**

   - In the right chat panel, select **Implementer** from the agent picker
   - **Paste the plan** from the Lead Developer thread or Drag and drop `PLANNING.md` into the chat window for context
   - Ask: `Based on this persistence plan, implement the weather data storage model with SQLite.`
   - The Implementer agent will create TODO lists and execute the code changes
   - Request: `Generate comprehensive pytest tests for the weather data persistence system.`

3. **Cross-Thread Collaboration Workflow**

   **Step 1: Planning → Implementation**

   - In Lead Developer thread, get the complete plan
   - **Option A**: Ask agent to create `docs/PERSISTENCE_PLAN.md` file
   - **Option B**: Copy the plan text manually
   - Switch to Implementer thread
   - Add the plan file as context: `#file:docs/PERSISTENCE_PLAN.md` or drag-and-drop
   - Implementer executes based on the plan

   **Step 2: Implementation → Review**

   - After Implementer makes changes, note the modified files
   - Switch back to Lead Developer thread
   - Add the implemented files as context: `#file:src/weather_cli/persistence.py #file:src/weather_cli/cache.py`
   - Or drag-and-drop the files into the chat
   - Ask: `Review this weather persistence implementation. What improvements or performance concerns do you see?`
   - Ask the agent to create a `docs/PERSISTENCE_REVIEW.md` file with the feedback

   **Step 3: Refinement Loop**

   - Switch back to Implementer thread
   - Add review context: `#file:docs/PERSISTENCE_REVIEW.md`
   - Ask: `Address the review feedback and refine the code`
   - Continue iterating between threads until both agents approve

4. **Tips for Multi-Chat Workflows**
   - **Use bookmarks**: Pin important responses in each thread for quick reference
   - **Leverage prompt files**: Use `/lead-plan` in Lead Developer thread, `/implement` in Implementer thread
   - **One task at a time**: Complete planning fully before switching to implementation
   - **Document decisions**: Keep a running note of key decisions from each thread

**Learning Goal:** Master multi-chat organization techniques using custom agents to separate planning, implementation, and review concerns, creating a structured development workflow that mirrors professional team collaboration.

---

Happy coding with GitHub Copilot!
