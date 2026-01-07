# GitHub Copilot Comprehensive Training Exercises

Welcome to your comprehensive GitHub Copilot training journey! These exercises are designed to progressively learn GitHub Copilot's features starting with foundational concepts and building up to advanced techniques through hands-on practice with our Python weather CLI project.

## Important: IDE-Specific Setup

This guide is tailored for various IDEs supporting GitHub Copilot. Key concepts covered:
- Context is added using `@project` and `#file:filename` syntax (or similar depending on your IDE)
- Drag-and-drop files directly into chat for context (in supported IDEs)
- Agent threads are isolated chat sessions with their own context
- Reusable prompts help maintain consistency across threads

## Phase 1: Getting Started with Copilot Basics

### Exercise 1.1: Understanding Your Project with Context

**Welcome to the project!** Before diving into code generation, let's use GitHub Copilot to understand the project you'll be working with.

1. **Project Overview**
   - Open Copilot Chat and select "Ask" mode
   - Ask: `@project Tell me about this Python weather CLI project?`
   - Try: `@project /explain Give me a comprehensive overview of this weather application`
   - Request: `@project What are the main features and components I should know about?`

2. **Code Structure Analysis**
   - Ask: `@project How are the Python modules organized in this project?`
   - Try: `@project Show me all the exception handling patterns used`
   - Request: `@project How are dependencies managed with pip and pyproject.toml?`

3. **Development Setup**
   - Ask: `@project What development tools and configurations are recommended for this project?`
   - Request: `@project How do I set up the development environment?`

4. **Running the Project**
   - Ask: `@project What's the best way to run this weather CLI application?`
   - Request: `@project How do I run tests from command line?`

**Learning Goal:** Use project-wide context to get familiar with the project structure, setup, and workflow before starting development.

### Exercise 1.2: First Steps with Code Suggestions and Inline Chat

1. **Explore Auto-Suggestions**
   - Open `src/weather_cli/weather_data.py`
   - Position your cursor at the end of the file and press Enter
   - Type `# Method to check if weather is considered severe` and press Enter
   - Watch Copilot suggest a method implementation
   - Try accepting suggestions with `Tab`
   - Practice rejecting suggestions with `Esc`

2. **Practice with Comments**
   - Add this comment: `# Calculate temperature difference from average for the season`
   - Let Copilot suggest the implementation
   - Notice how descriptive comments lead to better suggestions

3. **Experiment with Method Names**
   - Start typing `def format_temperature` and see what Copilot suggests
   - Try `def is_rainy` and observe the different suggestion

4. **Quick Edits with Inline Chat**
   - With `src/weather_cli/weather_data.py` still open, select any method
   - The shortcut to open inline chat for GitHub Copilot in JetBrains IDEs is Alt+Enter. This brings up the Copilot chat or inline suggestions when your cursor is on a line of code.
   - Try: "Add a docstring comment to this method"
   - Notice how inline chat allows quick edits without leaving your code

**Learning Goal:** Understand how Copilot uses context and comments to generate relevant Python code suggestions.

### Exercise 1.3: Exploring the Suggestion Interface

1. **Navigation Practice**
   - Open `src/weather_cli/config_util.py`
   - Add a comment: `# Validate API key format using regex`
   - Hover mouse over the suggestion to see alternative suggestions
   - Press `tab` to accept a suggestion

2. **Partial Acceptance**
   - Start typing a method and accept only part of a suggestion using `Ctrl+→` or `Cmd+→`
   - Try modifying the suggestion before accepting it
   - Experiment with accepting word-by-word vs. accepting the entire suggestion

**Learning Goal:** Master the Copilot interface and keyboard shortcuts.

### Exercise 1.4: Introduction to Copilot Chat

1. **Opening Chat**
   - Open Copilot Chat
   - Select "Ask" mode from the dropdown
   - Open `src/weather_cli/main.py` in your editor
   - Ask: "Explain what this file does"

2. **Basic Chat Questions**
   - Ask: "What are the main components of this weather CLI application?"
   - Try: "How is the weather API integration handled in this project?"
   - Notice how Copilot provides explanations and guidance

**Learning Goal:** Get comfortable with basic Copilot Chat interactions.

### Exercise 1.5: Understanding Interaction Modes

1. **Ask Mode Practice**
   - In Copilot Chat, switch to "Ask" mode
   - Ask questions about code without expecting changes
   - Try: "What design patterns are used in this Python codebase?"
   - Notice how Ask mode provides explanations and guidance

2. **Edits Mode Exploration**  
   - Switch to "Edits" mode (if available in your IDE)
   - Click `+ Add Files` and select `src/weather_cli/weather_service.py`
   - Request: "Add input validation to this method"
   - Observe how Edits mode focuses on direct code changes

3. **Agent Mode**
   - Switch to "Agent" mode
   - Click `+ Add Context` (you can add both files and folders here)
   - Type: "Create a simple Python utility class for temperature conversions"
   - Notice how Agent mode can create new files and structures

4. **Plan Agent - Strategic Planning**
   - Select **Plan** mode (if available)
   - Use for breaking down complex features into actionable steps
   - Try: "Create a plan for adding weather alert notifications to this application"
   - Plan helps you think through implementation before coding

**Learning Goal:** Understand when and how to use different Copilot interaction modes.

### Exercise 1.6: Setting Up Project Context with Copilot Instructions

**Why This Matters:** Creating a `copilot-instructions.md` file helps Copilot understand your project's specific patterns, conventions, and architecture, leading to more accurate and relevant suggestions throughout your development session.

1. **Generate Instructions Using Your IDE**
   - Create the `.github` folder if it doesn't exist
   - Open Copilot Chat in your IDE
   - Add your project's README.md and main configuration files as context
   - Request: `Based on the project structure and README, create a comprehensive copilot-instructions.md file that defines our Python coding standards, pip practices, and development patterns`

2. **Review the Generated Instructions**
   - Open the newly created `.github/copilot-instructions.md` file
   - Read through the generated content to understand what Copilot discovered about your project
   - Notice how it identifies:
     - Project architecture and patterns
     - Key conventions and coding styles
     - Important Python module structures
     - Development workflows and commands

3. **Test the Instructions with Copilot**
   - Open Copilot Chat
   - Ask: "Based on the project instructions, explain the main architecture of this application"
   - Try: "Following this project's patterns, how would I add a new field to the WeatherData model?"
   - Request: "What are the key conventions I should follow when adding a new service method?"
   - Compare the responses to earlier interactions - they should be more specific and aligned with your project

4. **Refine the Instructions (Optional)**
   - If you notice any missing patterns or inaccurate information in the generated instructions
   - Edit the `.github/copilot-instructions.md` file to add project-specific details
   - Consider adding information about:

**Learning Goal:** Understand how to leverage instruction generation feature to provide Copilot with better project context, resulting in more accurate and relevant code suggestions.

---

## Phase 2: Mastering Chat Commands

### Exercise 2.1: Basic Slash Commands

1. **Understanding Code with `/explain`**
   - Select the `get_weather()` method in `src/weather_cli/weather_service.py`
   - Open Copilot inline chat
   - Ask: `/explain`
   - Try: `/explain How does this weather service integrate with the API client?`
   - Compare explanations with different context levels

2. **Code Documentation with `/doc`**
   - Select the `WeatherData` class constructor
   - Open Copilot inline chat
   - Try: `/doc`
   - Try: `/doc Generate comprehensive docstrings for this weather data class`
   - Review and accept the generated documentation

3. **Quick Fixes with `/fix`**
   - Create intentional issues (missing imports, wrong variable name)
   - Select the problematic code
   - Try: `/fix`
   - For broader fixes: `/fix Address all PEP 8 compliance issues in this file`

**Learning Goal:** Master basic slash commands for common Python development tasks.

### Exercise 2.2: Creative Generation

1. **Simple Utility Creation**
   - In Agent mode, request: "Create a weather data formatting utility class for this project"
   - Advanced: "Create a plugin system for weather data sources"

2. **Component Generation**
   - Try: "Generate a configuration class with validation for API settings"
   - Experiment: "Create a factory pattern implementation for weather clients"

**Learning Goal:** Learn to generate new code components effectively.

### Exercise 2.3: Creating Project Structure

1. **Folder and File Structure Creation**
   - Open Copilot Chat in Agent mode
   - Try: `@project Create a new folder structure for weather data providers with client interfaces`
   - Experiment: `@project Generate a utilities package with helper functions for data conversion`
   - Advanced: `@project Create a complete testing structure with unit and integration test directories`

2. **Multi-file Component Generation**
   - Request: `@project Create a weather alerting module with service, data model, and notification components`
   - Try: `@project Generate a weather history system with data storage and analysis modules`

**Learning Goal:** Learn to use agent mode for generating complete folder structures and multi-file components.

### Exercise 2.4: Generating Tests with `/tests`

1. **Unit Test Generation**
   - Open `src/weather_cli/weather_data.py`
   - Select the entire class or a method
   - In Chat with the selection as context, type: `/tests`
   - Examine the generated pytest test structure

2. **Service Testing**
   - Select a method from `src/weather_cli/weather_service.py`
   - Use `/tests` and observe comprehensive test generation
   - Ask follow-up questions like "How would I mock the API client dependencies?"

3. **Custom Test Scenarios**
   - Ask: "Generate edge case tests for the weather API client error handling"
   - Request: "Create integration tests for the WeatherService class"

**Learning Goal:** Understand how to generate comprehensive tests and testing strategies.

---

## Phase 3: Context Control

> **💡 Context Setup Guide**  
> 
> **Using #file**: Start typing `#file:` and begin typing the filename you want to add as context. Your IDE will show you a dropdown of available files to choose from. Select the file you want and it will appear as `#file:filename` in your prompt.
> 
> **Using #get_errors**: Type `#get_errors` to identify any compile or lint errors in the current file.
> 
> **Using #get_terminal_output**: Type `#get_terminal_output` to include the visible output from your terminal window.
> 
> **Drag and Drop**: You can also drag files directly from the Project/Explorer view into the chat window to add them as context (in supported IDEs).
> 
> **Using + Add Files/Context**: In Edits or Agent mode, click the `+ Add Files` or `+ Add Context` button to select files or folders.
> 
> **For Code Selections**: Select code in the editor, then either drag it into chat or use inline chat (`Alt+\` or `Option+\`) to work with the selection directly.

### Exercise 3.1: Chat Variables and Context Control

1. **File Context Variables**
   - Try: `What security issues exist in #file:config_util.py?`
   - Experiment with multiple files: `Compare #file:weather_service.py with #file:weather_client.py`
   - Note: You can also drag and drop files directly into chat (in supported IDEs)

2. **Working with Code Selections**
   - Select a method in any Python file
   - Open inline chat
   - Ask: "Optimize this code for better performance"
   - Or select code and drag it into the chat window
   - Try selecting multiple lines and asking: "Refactor this to improve readability"

3. **Project-wide Analysis**
   - Ask: `@project What design patterns are used in this codebase?`
   - Try: `@project How is error handling implemented across the codebase?`
   - Request: `@project Show me the data flow through the application`

4. **Error Context Variables**
   - Use `#get_errors` to reference all errors in your file
   - Ask: `#get_errors What are the most critical errors I should fix first?`
   - Try: `#get_errors Explain these errors and suggest fixes`
   - Request: `#get_errors How can I resolve these type checking issues?`
   - This automatically includes error messages from your IDE's Problems panel

5. **Terminal Output Variables**
   - Use `#get_terminal_output` to reference the output from your terminal
   - Run a command in the terminal, then ask: `#get_terminal_output What does this output mean?`
   - Try: `#get_terminal_output Debug this error message`
   - Request: `#get_terminal_output Based on this test output, what's failing?`
   - This captures the visible terminal content for analysis

6. **Folder Context (Agent Mode)**
   - Switch to Agent mode
   - Click `+ Add Context` and select a folder
   - Ask: "Analyze the code quality in the weather_cli folder"
   - You can add multiple folders to provide broader context

7. **Advanced Context Combinations**
   - Try: `@project What would be the impact of adding caching to #file:weather_service.py?`
   - Experiment: Add both `#file:weather_service.py` and `#file:weather_client.py`, then ask "How do these files interact?"
   - Combine project and file context: `@project Based on existing patterns in #file:weather_service.py, suggest improvements`
   - Mix error and file context: `#get_errors #file:weather_client.py Are these errors related to this file?`

**Learning Goal:** Master IDE-specific context mechanisms for precise analysis and code generation.

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

1. **Brainstorming New Features**
   - Open Copilot Chat in Ask mode
   - `I want to add weather forecast data. How should I implement this feature in this Python CLI?`
   - `Walk me through adding weather alerts to this weather CLI application`
   - `How would I add weather history tracking without breaking existing functionality?`

2. **Implementation Guidance**
   - Ask: `Show me step-by-step how to add temperature unit conversion`
   - Request code examples for each step
   - Ask for configuration strategies for API keys and settings

**Learning Goal:** Learn to use Copilot for feature brainstorming and implementation guidance.

### Exercise 5.2: Debugging and Problem Solving

1. **Common Issues**
   - Open Copilot Chat in Ask mode
   - Ask: `What could cause the weather API call to fail silently in this Python application?`
   - Request: `How should I debug API connection and timeout issues?`

2. **Debugging Terminal Output**
   - After running a failing command, ask: `#get_terminal_output Why did this command fail?`
   - Try: `#get_terminal_output How do I fix this based on our project setup?`
   - Request: `#get_terminal_output What does this error stack trace tell us?`

3. **Error Handling Improvements**
   - Ask: `How can I improve error handling throughout this weather CLI application?`
   - Request: `Show me best practices for logging in Python CLI applications`

**Learning Goal:** Develop debugging skills for Python CLI applications with Copilot assistance and leverage IDE-specific error context.

---

## Phase 6: Specialized Agent Interactions

### Exercise 6.1: Security-Focused Reviews

1. **Security Expert Role**
   - Open Copilot Chat
   - `Act as a security expert and review the API key handling in src/weather_cli/config_util.py`
   - `As a security specialist, what vulnerabilities do you see in the weather_client.py module?`
   - `From a security perspective, how should I improve the API key management?`

2. **Security Best Practices**
   - `What security issues should I check for in this CLI application?`
   - `Provide specific security improvements for API key and sensitive data handling`

**Learning Goal:** Learn to use Copilot for security-focused code reviews in Python CLI applications.

### Exercise 6.2: Performance and Code Quality

1. **Performance Expert Role**
   - Open Copilot Chat
   - `As a performance expert, analyze the efficiency of the weather service implementation`
   - `How can I optimize the HTTP requests and JSON parsing?`

2. **Code Quality Reviewer**
   - `Act as a senior Python developer and review the code quality in the src/weather_cli directory`
   - `What Python coding standards and best practices should I implement in this codebase?`

**Learning Goal:** Understand how different expert perspectives can improve your code.

### Exercise 6.3: Code Review Workflow

1. **Setting Up for Code Review**
   - Open the file you want to review
   - Open Copilot Chat and select **Ask** mode
   - Ask: `Act as a code reviewer and analyze this file for quality, performance, and best practices`

2. **Conducting the Review**
   - Select specific methods or sections with code selection
   - Ask: `Review this code for potential bugs, security issues, and maintainability`
   - Request: `Suggest refactoring opportunities and improvements following project conventions`
   - Ask for specific feedback: `Are there any design pattern violations or anti-patterns here?`

3. **Implementing Feedback**
   - Switch to the **Edits** mode in Copilot Chat
   - Paste the review findings: `Based on this code review feedback, apply the recommended improvements`
   - Ask: `Generate updated code that addresses these review comments`
   - Review the changes and accept them into your workflow

**Learning Goal:** Develop a structured code review process using Copilot to catch issues and improve code quality before committing.

---

## Phase 7: Advanced Context Optimization and Copilot Techniques

### Exercise 7.1: Strategic Context Building

1. **Minimal vs. Maximum Context**
   - Ask the same question with different context levels:
     - Minimal: `How do I add validation?`
     - Medium: `How do I add validation to #file:weather_service.py?`
     - Maximum: `@project How do I add consistent validation across all modules following the existing patterns in #file:weather_service.py?`
   - Compare response quality and relevance

2. **Context Layering Technique**
   - Start broad: `@project What's the error handling strategy?`
   - Layer specific: `#file:weather_service.py How does this module handle validation?`
   - Drill down: Select specific code, open inline chat, and ask "Improve this validation logic"
   - Notice how each layer builds understanding

3. **Cross-Reference Optimization**
   - Use multiple file references: `Compare error handling approaches in #file:weather_service.py vs #file:weather_client.py`
   - Combine selection with file context: Select code, then in chat add `#file:weather_data.py` and ask "How does this selected code relate to patterns in this file?"
   - Mix project and file context: `@project Based on patterns in #file:weather_service.py, where else is this approach used?`

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

Your IDE allows you to switch between different AI models using the **model picker** in the chat input field. Different models are optimized for different tasks - some excel at complex reasoning, others at fast code generation.

1. **Scenario: Adding Weather Alert Notifications - A Multi-Model Workflow**
   
   **Step 1: Analysis with a Reasoning Model**
   - Click the **model picker** in the Chat view and select a reasoning-focused model (e.g., o1, o3-mini, or similar)
   - Ask: `Looking at the current Python weather CLI structure, what would be the architectural implications of adding weather alert notifications? What potential issues should I consider?`
   - Follow up with: `Based on the existing WeatherService and WeatherData classes, what's the most logical way to integrate alert notifications without breaking current functionality?`

   **Step 2: Implementation with a Code Generation Model**
   - Switch to a code-optimized model (e.g., Claude Sonnet, GPT-4o, or similar)
   - Say: `Based on the analysis above, generate the code changes needed to add alert notification functionality to the weather CLI. Include new classes and methods.`
   - Then: `Now generate the corresponding service changes to handle alert processing and notification delivery.`
   
   **Step 3: Documentation with a Fast Model**
   - Switch to a faster model for quick tasks (e.g., GPT-4o-mini, Claude Haiku, or similar)
   - Request: `Get the current git status and create a summary of what files would be changed for this alert feature.`
   - Follow with: `Generate a concise commit message and brief docstring documentation for these alert changes.`

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

## Phase 8: Advanced Prompt Engineering and Agent Workflows

### Exercise 8.1: Understanding Custom Agents

You can create **custom agents** (`.agent.md` files) that define specialized personas with specific tools, instructions, and behaviors. This repository includes two custom agents in `.github/agents/`.

1. **Explore the Custom Agents in This Repository**
   - Open `.github/agents/Implementer.agent.md` and review its structure:
     - **description**: Brief summary of the agent's purpose
     - **tools**: List of tools the agent can use (edit, search, runCommands, etc.)
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
   - Try: "Add a `format_for_display()` method to the WeatherData model"
   - Observe how it follows its defined execution phases

4. **Practice with the Lead Developer Agent**
   - Switch to **Lead Developer**
   - This agent focuses on planning and research, never writing production code
   - Try: "Analyze the architecture for adding weather forecast caching"
   - Notice how it decomposes the problem into tasks rather than implementing directly

5. **Creating Your Own Custom Agent (Optional)**
   - Define the agent's description, allowed tools, and behavioral instructions
   - Consider creating agents for: code review, documentation, testing, or security analysis

**Learning Goal:** Understand how custom agents extend Copilot's capabilities with specialized personas and workflows.

### Exercise 8.2: Role-Based Collaboration with Custom Agents

1. **Simulate a Lead Developer / Implementer Workflow**
   
   This exercise demonstrates how custom agents can work together like a real development team:
   
   **Step 1: Planning with Lead Developer**
   - Select **Lead Developer** 
   - Ask: "Create a plan for adding temperature unit conversion (Celsius/Fahrenheit) to this weather CLI"
   - The Lead Developer will:
     - Analyze the existing codebase
     - Identify files that need changes
     - Break down the work into discrete tasks
   - Review the generated plan

   **Step 2: Implementation with Implementer**
   - Switch to **Implementer**
   - Reference the plan: "Implement the first task from the temperature conversion plan"
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

GitHub Copilot supports **prompt files** (`.prompt.md`) that define reusable prompt templates you can invoke with `/` commands. This repository includes several prompts in `.github/prompts/`.

1. **Explore the Available Prompt Files**
   - Open `.github/prompts/` and review the available prompts:
     - `implement.prompt.md` - For executing implementation tasks
     - `lead-plan.prompt.md` - For creating implementation plans
     - `ask_advice.prompt.md` - For getting guidance and recommendations
     - `report_to_lead.prompt.md` - For reporting progress back to lead developer
     - `summarize-session.prompt.md` - For capturing session outcomes
     - `thread-dump.prompt.md` - For context handoff between threads

2. **Using Prompt Files**
   - In the Chat view, type `/` to see available prompt commands
   - Your custom prompts appear alongside built-in commands like `/new`, `/explain`, `/fix`
   - Select a prompt to insert its template into the chat

3. **Practice with Implementation Prompts**
   - Use `/implement` when working with the Implementer agent
   - Use `/lead-plan` when working with the Lead Developer agent
   - Notice how prompts and agents work together for structured workflows

4. **Session Summaries and Context Handoff**
   - Use `summarize-session.prompt.md` to capture key outcomes and next steps
   - Use `thread-dump.prompt.md` when your chat context is at maximum capacity
   - Practice formatting output as a single, precise text message for handoffs

5. **Creating Your Own Prompt Files (Optional)**
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
   - Open Copilot Chat
   - `How would you refactor the WeatherService to use a dependency injection container?`
   - `Show me how to implement the Repository pattern for weather data access.`

2. **Design Pattern Implementation**
   - `How could I implement the Observer pattern for weather condition changes?`
   - `Show me how to add a Factory pattern for creating different weather data sources.`

**Learning Goal:** Explore advanced programming concepts with Copilot's guidance.

### Exercise 9.2: Alternative Implementations

1. **Different Approaches**
   - `Show me 3 different ways to implement weather data caching.`
   - `What are alternative approaches to API client configuration management?`

2. **Technology Comparisons**
   - `How would this application look if built with Click framework instead of argparse?`
   - `Compare this implementation with an async/await approach using aiohttp.`

**Learning Goal:** Understand different Python implementation strategies and trade-offs.

### Exercise 9.3: Multi-Thread Task Management with Custom Agents

This exercise demonstrates how to use multiple chat threads with different custom agents to organize complex development workflows. Each thread is isolated with its own context and agent selection, allowing you to separate concerns like planning, implementation, and review.

1. **Opening Multiple Chat Threads**
   - Open the Copilot Chat tool window from the sidebar
   - Click the **"+"** button to create a new chat thread
   - Each thread maintains its own conversation history and agent selection
   - You can switch between threads using the thread selector/tabs

2. **Scenario: Implementing Weather Data Caching - Organized Workflow**

   **Thread 1: Lead Developer (Planning)**
   - Create a new chat thread 
   - In the agent picker, select **Lead Developer**
   - Or use **Plan** mode if Lead Developer agent isn't available
   - Add project context: `@project`
   - Ask: `I need to add weather data caching to this CLI application. What's the overall architecture and implementation strategy you recommend?`
   - Follow up: `Create a detailed implementation plan with cache expiration and storage considerations.`
   - The Lead Developer will analyze the codebase and provide a strategic plan
   - **Save the plan**: Ask the agent to `Create a docs/CACHING_PLAN.md file with this caching plan`

   **Thread 2: Implementer (Execution)**
   - Create another new chat thread
   - Switch to **Agent** mode or select **Implementer** custom agent
   - Drag and drop `docs/CACHING_PLAN.md` into the chat window for context
   - Ask: `Based on this caching plan, implement the cache storage mechanism and WeatherService integration.`
   - The Implementer agent will create TODO lists and execute the code changes
   - Use `/implement` prompt if available
   - Request: `Generate comprehensive pytest tests for the caching system.`

3. **Cross-Thread Collaboration Workflow**

   **Step 1: Planning → Implementation**
   - In Lead Developer thread, get the complete plan
   - **Option A**: Ask agent to create `docs/CACHE_PLAN.md` file
   - **Option B**: Copy the plan text manually
   - Switch to Implementer thread
   - Add the plan file as context: `#file:docs/CACHE_PLAN.md` or drag-and-drop
   - Implementer executes based on the plan

   **Step 2: Implementation → Review**
   - After Implementer makes changes, note the modified files
   - Switch back to Lead Developer thread
   - Add the implemented files as context: `#file:src/weather_cli/cache.py #file:src/weather_cli/weather_service.py`
   - Or drag-and-drop the files into the chat
   - Ask: `Review this caching implementation. What improvements or performance concerns do you see?`
   - Ask the agent to create a `docs/CACHE_REVIEW.md` file with the feedback

   **Step 3: Refinement Loop**
   - Switch back to Implementer thread
   - Add review context: `#file:docs/CACHE_REVIEW.md`
   - Ask: `Address the review feedback and refine the code`
   - Continue iterating between threads until both agents approve

4. **Alternative: Single Thread with Role Switching**

   If managing multiple threads becomes complex, you can use a single thread and explicitly switch roles:
   
   - Create one thread: **"Weather Caching Feature"**
   - **Planning phase**: `Acting as Lead Developer, create an implementation plan for weather data caching`
   - **Save the plan**: Ask to create `docs/CACHE_PLAN.md`
   - **Implementation phase**: `Now acting as Implementer, based on #file:docs/CACHE_PLAN.md, implement the cache module`
   - **Review phase**: `Back to Lead Developer role, review #file:src/weather_cli/cache.py for performance issues`

5. **Tips for Multi-Thread Workflows**
   
   - **Use files for handoffs**: Create .md files to share context between threads
   - **Leverage drag-and-drop**: Quickly add files to any thread by dragging from the Project/Explorer view
   - **Use #file: syntax**: Reference specific files when switching threads
   - **Leverage prompt files**: Use `/lead-plan` in Lead Developer thread, `/implement` in Implementer thread
   - **Name threads descriptively**: Use clear names like "Feature X - Planning" vs "Feature X - Implementation"
   - **One task at a time**: Complete planning fully before switching to implementation thread
   - **Document decisions**: Keep running notes in docs/ folder for cross-thread reference
   - **Use @project sparingly**: Only use when you need full codebase context, as it can slow responses

**Learning Goal:** Master multi-thread organization techniques using custom agents to separate planning, implementation, and review concerns, creating a structured development workflow that mirrors professional team collaboration.

---

Happy coding with GitHub Copilot!