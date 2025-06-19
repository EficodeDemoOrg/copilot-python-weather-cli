# GitHub Copilot Exercises: Python Weather CLI App

This document provides a series of exercises designed to help you learn and practice using GitHub Copilot features within the context of the Python Weather CLI application. We will cover exploring the codebase, ideating new features, and implementing them using Copilot's capabilities.

**Key Copilot Interaction Points:**

* **Chat View:** Used for asking questions, generating code/tests/docs, and initiating actio### Exercise 3.6: Extracting and Applying Project Style Guidelines

* **Purpose:** To ensure Copilot-generated code aligns with your project's style and linting rules.
* **Aim:** Practice using Copilot to summarize your code style (from Black, Flake8, and mypy), and use that summary to create a `.copilot-instructions.md` file for consistent code generation.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Requires analysis of configuration files and synthesis into actionable guidelines
* **Steps:**odes like "Ask" (default), "Edits", and "Agent" might be selectable via a dropdown menu within the Chat view interface itself.
* **Inline Chat:** Quick chat directly in the editor (Default: `Cmd+I` / `Ctrl+I`), often used for quick explanations or edits on selected code. Allows reviewing multiple suggestions using keyboard shortcuts (e.g., `Alt+]`/`Option+]` or check the Command Palette for "Copilot: View Next/Previous Suggestion").
* **Participants (`@` references):** Used to bring specific, broad contexts into the chat, such as the entire workspace (`@workspace`) or the VS Code environment itself (`@vscode`). **Important Limitation:** You can only use **one participant** (e.g., `@workspace` OR `@vscode`) in a single chat prompt.
* **Variables (`#` references):** Used to provide more granular context to Copilot (e.g., files `#file`, selections `#selection`, symbols `#sym`, symbol usages/definitions `#usage`, changes `#changes`, codebase structure `#codebase`, web content `#fetch`, last terminal command `#terminalLastCommand`, terminal selection `#terminalSelection`). Variables *can* be combined with a participant (e.g., `@workspace #file:weather_data.py`).
    * **Interactive Selection:** For files, folders, symbols (`#sym`), and usage queries (`#usage`), you typically type `#` and then start typing the name; VS Code's UI will suggest matching items from your workspace for you to select easily (e.g., typing `#weather` might suggest the `weather_client.py` file and the `WeatherService` class symbol).
    * **Drag and Drop:** You can also often drag files or folders directly from the VS Code Explorer into the Chat input area to add them as context. **Tip:** Use whichever method feels most convenient for you—both achieve the same result.
* **Slash Commands:** Used within the Chat view or inline chat to direct Copilot's actions (e.g., `/explain`, `/tests`, `/fix`, `/new`).
* **Code Completion:** Automatic suggestions as you type.
* **Custom Instructions:** Files like `.github/copilot-instructions.md` can guide Copilot's suggestions for the workspace.

**Note on `@workspace` vs `#codebase` and Participant Usage:**

Both `@workspace` and `#codebase` provide Copilot with context about your entire project or workspace files, serving **essentially the same core function**. However, their usage context can differ:
* `@workspace` is the standard **participant** for general questions about the project, typically used within the default "Ask" mode of the Chat view. As a participant, it adheres to the **one-participant-per-prompt** rule.
* `#codebase` is a **variable** that also refers to the workspace context. You might observe that `#codebase` is particularly effective or required when using specific modes like "Edits" or "Agent" (`/new`), where a deeper analysis or generation based on the entire codebase structure is required. Since it's a variable, it doesn't conflict with the one-participant rule if you needed to use `@vscode` alongside workspace context (though combining `@vscode` and `#codebase` is an uncommon scenario).

> **Tip:** While Copilot often uses the whole codebase as context by default, explicitly referencing `#codebase` can help ensure your intent is clear—especially for tasks that require broad project understanding or when using modes like "Edits" or "Agent". Making context explicit can improve the quality and relevance of Copilot’s responses.

These exercises generally use `@workspace` for broad "Ask" queries and `#codebase` when broad context seems needed for Agent/Edit tasks, reflecting common patterns and the potential need for `#codebase` in those specific modes. Feel free to experiment to see what works best in your specific scenario.

**Prerequisites:**

* Visual Studio Code installed.
* GitHub Copilot and Copilot Chat extensions installed and configured.
* The Python Weather CLI project (as described in the structure diagram) opened in VS Code.
* An integrated terminal open within VS Code (e.g., View > Terminal).
* Basic understanding of Python and package management (pip).
* An OpenWeatherMap API key set as the `OPENWEATHERMAP_API_KEY` environment variable (required for some implementation/testing steps).

---

## Model Selection Guide

**🤖 CHOOSING THE RIGHT AI MODEL:**

For detailed information about available AI models, their capabilities, and pricing, see the [GitHub Copilot AI Models Documentation](https://docs.github.com/en/copilot/using-github-copilot/ai-models/choosing-the-right-ai-model-for-your-task).

Each exercise below includes a specific model recommendation with rationale. You can always experiment with different models to see how they perform for your specific use case.

---

## Section 1: Explore the Codebase and Environment

**Goal:** Use Copilot Chat with various context providers (`@workspace`, `#file`, `#folder`, `#sym`, `#usage`, `#fetch`, `#terminalLastCommand`, `#terminalSelection`, `@vscode`) to quickly understand the project, its dependencies, relationships between components, the development environment, and external information.

---

### Exercise 1.1: Project Overview (`@workspace`, `/explain`)

* **Purpose:** To get a high-level understanding of the project's goals, main components, and structure using the broad workspace context.
* **Aim:** Practice using the `@workspace` participant in Copilot Chat for broad project questions in "Ask" mode.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple explanation task that doesn't require advanced reasoning
* **Steps:**
    1.  Open the Copilot Chat view in VS Code. Ensure the mode is "Ask".
    2.  In the chat input, type the following prompt and press Enter:
        ```
        @workspace /explain What is the main purpose of this project and how is it structured? What are the key Python modules involved according to the source code and README?
        ```
    3.  Review Copilot's explanation.

### Exercise 1.2: Understanding a Specific Class (`#` file reference, `/explain`)

* **Purpose:** To dive deeper into the functionality of a single module.
* **Aim:** Practice referencing a file using the `#` prefix with interactive selection.
* **🤖 Recommended Model:** GPT-4.1 (default) - Straightforward code analysis task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type `#` in the chat input.
    3.  Start typing `weather_client`. VS Code should suggest matching files and symbols. Select the *file* `src/weather_cli/weather_client.py` from the list (it will likely insert `#file:src/...`).
    4.  Append the command `/explain Explain the role of this module. How does it fetch data from the OpenWeatherMap API? What dependencies does it seem to have?` to the prompt and press Enter.
    5.  Analyze the response.
    6.  *(Alternative)* Try dragging the `weather_client.py` file from the Explorer into the Chat input instead of using `#` to achieve the same context.

### Exercise 1.3: Explaining Dependencies (`#` file reference, `/explain`)

* **Purpose:** To understand the external libraries.
* **Aim:** Practice referencing `requirements.txt` and `pyproject.toml` using the `#` prefix with interactive selection.
* **🤖 Recommended Model:** GPT-4.1 (default) - Basic dependency explanation task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type `#` and start typing `requirements`. Select `requirements.txt` from the suggestions.
    3.  Type `#` again and select `pyproject.toml` from the suggestions.
    4.  Append `/explain Explain the roles of the main dependencies listed in these files, such as requests, python-dotenv, and any development dependencies like pytest, black, flake8, and mypy.` and press Enter.
    5.  Review the explanation.

### Exercise 1.4: Generating Documentation (`#selection`)

* **Purpose:** To automatically generate documentation.
* **Aim:** Practice using the `#selection` variable for editor content.
* **🤖 Recommended Model:** GPT-4.1 (default) - Standard docstring generation task
* **Steps:**
    1.  Open the file `src/weather_cli/weather_service.py`.
    2.  Locate and select the entire method signature and body of the `get_weather(self, city: str)` method.
    3.  Open the Copilot Chat view.
    4.  Ensure the mode is set to "Ask" (the default).
    5.  Type the following prompt:
        ```
        #selection Generate Python docstring documentation for the selected method. Explain its purpose, parameters, return value, and potential exceptions based on the code.
        ```
    6.  Copilot should provide the docstring. Review it and potentially copy it into your code.

### Exercise 1.5: Explore Folder Contents (`#` folder reference, `/explain`)

* **Purpose:** To get a summary of the code within a directory.
* **Aim:** Practice referencing a folder using the `#` prefix with interactive selection.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple code summarization task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type `#` and start typing `weather_cli`. Select the *folder* `src/weather_cli` from the suggestions (it will likely insert `#folder:src/...`).
    3.  Append `/explain Summarize the purpose of the Python modules inside this package.` and press Enter.
    4.  Review Copilot's summary.
    5.  *(Alternative)* Try dragging the `weather_cli` folder from the Explorer into the Chat input.

### Exercise 1.6: Explore a Specific Symbol (`#` symbol reference, `/explain`)

* **Purpose:** To understand a specific function or class.
* **Aim:** Practice referencing a symbol using the `#` prefix with interactive selection.
* **🤖 Recommended Model:** GPT-4.1 (default) - Focused code analysis task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  **Example 1 (Method):**
        * Type `#` and start typing `get_weather_from_api`. Select the *symbol* `OpenWeatherMapClient.get_weather_from_api` from the suggestions (it will likely insert `#sym:...`).
        * Append `/explain Explain what this method does, its parameters, and what it returns.` and press Enter.
    3.  **Example 2 (Class):**
        * Type `#` start typing `WeatherData` and select the *class symbol* `WeatherData` (likely inserts `#sym:WeatherData`).
        * Append `/explain Explain the purpose of this class and its attributes.` and press Enter.
    4.  Analyze the explanations provided for these valid symbols.

### Exercise 1.7: Previewing API Documentation (`#openSimpleBrowser`)

* **Purpose:** To quickly view external web content, such as API documentation, directly within VS Code's simple browser. This is useful for easily checking the contents of a page before using `#fetch` or for general browsing related to the project.
* **Aim:** Practice using the `#openSimpleBrowser` variable to open URLs.
* **🤖 Recommended Model:** Not applicable - This is a browser functionality, not AI-powered
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  To preview the OpenWeatherMap API documentation page directly in VS Code before potentially using `#fetch` on it, type the following prompt:
        ```
        #openSimpleBrowser:https://openweathermap.org/current
        ```
    3.  Observe that VS Code opens the URL in the Simple Browser tab. This allows you to visually inspect the page content and structure.
    4.  This feature is helpful for quick checks of web resources without leaving the editor.

### Exercise 1.7.1: Fetching External Info (`#fetch`, `/explain`)

* **Purpose:** To pull in information from an external URL.
* **Aim:** Practice using the `#fetch` variable.
* **🤖 Recommended Model:** GPT-4.1 (default) - Web content analysis and summarization
* **Steps:**
    1.  The README mentions the OpenWeatherMap API. Let's ask about its current weather endpoint documentation.
    2.  Open the Copilot Chat view.
    3.  Type the following prompt:
        ```
        #fetch:[https://openweathermap.org/current](https://openweathermap.org/current) /explain Based on the content from this URL, what are the main parameters needed to call the current weather data API, and what key information is typically included in the JSON response (e.g., temperature, weather description)?
        ```
    4.  Review Copilot's summary based on the fetched web page content.

### Exercise 1.7.2: Correlating API Documentation with `weather_data.py` (`#fetch`, `#file`, `/explain`)

* **Purpose:** To understand how the fields in the `WeatherData` class correspond to the actual data provided by the OpenWeatherMap API.
* **Aim:** Practice using `#fetch` to get API schema details and `#file` to reference a specific project file for comparison.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Requires cross-referencing and analytical reasoning between web content and code. Alternative: Gemini 2.0 Flash for larger context handling
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type the following prompt:
        ```
        /explain Based on the API documentation from #fetch:https://openweathermap.org/current and the fields in #file:src/weather_cli/weather_data.py, which fields in our `WeatherData` class directly map to the API response? Are there any fields in `WeatherData` that are derived or not directly present in the main part of the API response (e.g., inside `main`, `wind`, `weather[]`)?
        ```
    3.  Review Copilot's analysis. This helps in understanding the data source for your application's core data object.

### Exercise 1.8: Asking About VS Code (`@vscode`, `/explain`)

* **Purpose:** To get help with VS Code features or settings relevant to the project.
* **Aim:** Practice using the `@vscode` participant to ask questions about the editor environment. Remember only one `@` participant per prompt.
* **🤖 Recommended Model:** GPT-4.1 (default) - Standard VS Code feature explanations
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Think of a question about VS Code relevant to Python development (see examples below).
    3.  Type your prompt using `@vscode`:
        * Example 1: `@vscode /explain How can I see the definition of a Python function quickly without leaving my current file?`
        * Example 2: `@vscode /explain Are there settings to automatically format Python files with Black when I save?`
        * Example 3: `@vscode /explain How do I configure task configurations in VS Code to run specific Python commands for this project?`
    4.  Review Copilot's explanation about VS Code features.

### Exercise 1.9: Understanding Terminal Commands (`#terminalLastCommand`, `/explain`)

* **Purpose:** To use Copilot to explain commands executed in the integrated terminal.
* **Aim:** Practice using the `#terminalLastCommand` variable.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple command explanation task
* **Steps:**
    1.  Open the integrated terminal in VS Code (View > Terminal).
    2.  Run a command relevant to the project, for example:
        ```bash
        pip install -r requirements-dev.txt
        ```
    3.  Wait for the command to complete.
    4.  Open the Copilot Chat view.
    5.  Type the following prompt:
        ```
        #terminalLastCommand /explain Explain what the last command run in the terminal does, including the purpose of any flags used.
        ```
    6.  Review Copilot's explanation of the pip command.

### Exercise 1.10: Explaining Terminal Output (`#terminalSelection`, `/explain`)

* **Purpose:** To get clarification on specific parts of the output shown in the integrated terminal.
* **Aim:** Practice using the `#terminalSelection` variable.
* **🤖 Recommended Model:** GPT-4.1 (default) - Basic output interpretation task
* **Steps:**
    1.  In the integrated terminal, run a command that produces some detailed output, for example:
        ```bash
        python --version
        ```
    2.  **Select a specific part** of the output in the terminal, for instance, the line showing the Python version.
    3.  Open the Copilot Chat view.
    4.  Type the following prompt:
        ```
        #terminalSelection /explain What does the selected line from the terminal output signify in the context of my development environment?
        ```
    5.  Review Copilot's explanation of the selected output.

### Exercise 1.11: Finding Symbol Usages (`#usage`)

* **Purpose:** To understand where a specific class, method, or variable is used within the project.
* **Aim:** Practice using the `#usage` variable combined with interactive symbol selection to find references.
* **🤖 Recommended Model:** GPT-4.1 (default) - Code reference analysis task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Think of a symbol you want to find usages for (e.g., the `WeatherData` class or the `WeatherService#getWeather` method).
    3.  Type `#` and start typing the symbol name (e.g., `WeatherData`). Select the desired *symbol* from the suggestions (it will likely insert `#usage:WeatherData` or similar).
    4.  Append `/explain Where is this symbol used throughout the codebase? List the files and lines.` and press Enter.
    5.  Review the locations identified by Copilot. This helps understand the impact of changing this symbol.

### Exercise 1.12: Finding Interface Implementations (`#usage`)

* **Purpose:** To discover all classes that implement a specific interface.
* **Aim:** Practice using `#usage` with an interface symbol to find its implementations.
* **🤖 Recommended Model:** GPT-4.1 (default) - Interface implementation discovery task
* **Steps:**
    1.  The project structure indicates a `WeatherApiClient` abstract base class. Let's find its implementations.
    2.  Open the Copilot Chat view.
    3.  Type `#` and start typing `WeatherApiClient`. Select the *class symbol* `WeatherApiClient` from the suggestions.
    4.  Append `/explain Find all classes in the workspace that inherit from this abstract base class.` and press Enter.
    5.  Copilot should identify `OpenWeatherMapClient` (and potentially others if they existed) as implementations.

### Exercise 1.13: Using VS Code Search Results (`#searchResults`, `/explain`)

* **Purpose:** To bring the results from VS Code's Search view into Copilot Chat for summarization, analysis, or to provide context for further questions.
* **Aim:** Practice using the `#searchResults` variable.
* **🤖 Recommended Model:** GPT-4.1 (default) - Search result summarization task
* **Steps:**
    1.  First, perform a search in VS Code. For example, open the Search view (View > Search or `Cmd+Shift+F` / `Ctrl+Shift+F`) and search for the term `WeatherData` across the project.
    2.  Once the search results are populated in the Search panel, open the Copilot Chat view.
    3.  Type the following prompt to ask Copilot about these results:
        ```
        #searchResults /explain Summarize what is found in these search results. Which files mention 'WeatherData' and in what context?
        ```
    4.  Review Copilot's explanation, which will be based on the exact files and lines shown in your Search view. This helps in understanding the scope of a term or feature within the codebase.

---

## Section 2: Ideate New Features with Copilot Chat

**Goal:** Use Copilot Chat as a brainstorming partner, leveraging its understanding of the codebase (`#codebase` or `@workspace`).

---

### Exercise 2.1: Brainstorming Feature Ideas (`#codebase`)

* **Purpose:** To generate a list of potential enhancements.
* **Aim:** Practice using `#codebase` (or `@workspace`) for creative suggestions.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Creative ideation benefits from superior reasoning capabilities
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type the following prompt:
        ```
        #codebase Suggest 3-5 ideas for new features or significant improvements for this command-line weather application. For each idea, briefly explain the potential benefit.
        ```
    3.  Consider the suggestions.

### Exercise 2.2: Exploring an Idea (`#codebase`)

* **Purpose:** To flesh out the details of one specific feature idea.
* **Aim:** Practice having a conversational follow-up using `#codebase` (or `@workspace`) context.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Deep analysis and architectural thinking required
* **Steps:**
    1.  Choose one idea (e.g., adding forecast data).
    2.  In the Copilot Chat view, ask:
        ```
        #codebase Let's explore adding a 3-day forecast option. How could we modify the application? Would we need new API calls (check OpenWeatherMap docs if needed)? How would the output look different? What classes might need changes?
        ```
    3.  Discuss the approach with Copilot.

### Exercise 2.3: Improving Error Handling (`#codebase`)

* **Purpose:** To identify areas where error handling could be improved.
* **Aim:** Practice using `#codebase` (or `@workspace`) to analyze potential weaknesses.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Requires thorough code analysis and architectural understanding
* **Steps:**
    1.  In the Copilot Chat view, type:
        ```
        #codebase Review the error handling in this application (e.g., in WeatherService, OpenWeatherMapClient, main module). Suggest ways to make it more robust or provide better user feedback for errors like invalid API keys, network timeouts, city not found, or unexpected API responses.
        ```
    2.  Evaluate Copilot's suggestions.

### Exercise 2.4: Assessing Feature Feasibility with API Documentation (`#codebase`, `#fetch`, `/explain`)

* **Purpose:** To determine if a potential new feature (e.g., displaying "feels like" temperature) is supported by the OpenWeatherMap API and how it might be accessed.
* **Aim:** Practice using `#fetch` to consult API documentation when considering new features and `#codebase` to provide context of the current application.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Complex cross-referencing between API docs and codebase. Alternative: Gemini 2.0 Flash for handling large context from multiple sources
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Assume you are considering adding a "feels like" temperature reading to the weather output.
    3.  Type the following prompt:
        ```
        #codebase I want to add a "feels like" temperature to our weather display. According to the API documentation at #fetch:https://openweathermap.org/current, is "feels like" temperature data available? If so, which field in the API response provides this, and how might I add it to the `WeatherData` class and the application's output?
        ```
    4.  Review Copilot's response to understand if the feature is feasible with the current API and get initial pointers for implementation.

---

## Section 3: Implement Features using Copilot

**Goal:** Use Copilot's code generation capabilities (autocompletion, Edits mode, agents, slash commands, inline chat suggestions) to implement changes, using `#codebase` where broad context is needed for generation/editing modes.

---

### Exercise 3.1: Adding a New Field (Code Completion & Edits Mode)

* **Purpose:** Add humidity data, use Edits mode.
* **Aim:** Practice completion & Edits mode.
* **🤖 Recommended Model:** GPT-4.1 (default) for code completion, Claude Sonnet 3.7 for Edits mode - Simple field addition with targeted edits
* **Steps:**
    1.  **Modify `weather_data.py` (Code Completion):**
        * Open the file. Add `humidity: int` as a new field to the `WeatherData` dataclass. Use code completion for the field definition.
        * Update the `__str__` method to include humidity using completion (e.g., start typing `f"Humidity: {self.hum`).
    2.  **Modify `weather_client.py` (Edits Mode):**
        * Open the file. Find where the `WeatherData` object is created after parsing JSON.
        * **Select the lines of code** within that block responsible for extracting values (like temperature, description) and creating the `WeatherData` instance.
        * Open the Copilot Chat view.
        * **From the dropdown menu** in the Chat input area, select the **"Edits"** mode.
        * In the chat input, **type the instruction** (without any slash command prefix):
            ```
            Extract the 'humidity' integer value from the 'main' section of the JSON response and pass it to the WeatherData constructor along with the existing values.
            ```
        * Press Enter. Copilot should show a diff proposing the changes to your selected code. Review and apply if correct.
    3.  **Modify `main.py` (Display - Code Completion):**
        * Open the file. Find where the weather data is displayed. The humidity should already be included via the updated `__str__` method, but you can modify the display format if needed using code completion.

### Exercise 3.2: Generating Unit Tests (`#` file references, `/tests`)

* **Purpose:** Automatically generate unit tests.
* **Aim:** Practice `/tests` with `#` file referencing (interactive selection).
* **🤖 Recommended Model:** GPT-4.1 (default) - Standard test generation task
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type `#` and select `tests/test_weather_client.py`.
    3.  Type `#` again and select `src/weather_cli/weather_client.py`.
    4.  Append the following prompt and press Enter:
        ```
        /tests Generate a new pytest test method for OpenWeatherMapClient. It should mock the requests.get call and JSON response (include 'main: { humidity: 85 }') and verify that get_weather_from_api correctly parses the humidity into the WeatherData object.
        ```
    5.  Copy the generated test method into your test file, adjust imports/mocks if needed, and run the tests (`pytest tests/`).

### Exercise 3.3: Refactoring with Edits Mode

* **Purpose:** Modify existing code via Edits mode.
* **Aim:** Practice Edits mode for refactoring.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Refactoring requires understanding code flow and making intelligent changes
* **Steps:**
    1.  *(Assumption: `config_util.py` exists with `get_api_key()` reading only the environment variable.)*
    2.  Open `src/weather_cli/config_util.py`.
    3.  **Select the entire body** of the `get_api_key()` method.
    4.  Open the Copilot Chat view.
    5.  **Select the "Edits" mode** from the dropdown.
    6.  In the chat input, **type the instruction**:
        ```
        Refactor this: First, try the 'OPENWEATHERMAP_API_KEY' environment variable. If None or empty, try loading from a '.env' file using python-dotenv. If still not found, raise a ConfigException indicating the key is missing.
        ```
    7.  Review the proposed diff and apply the changes.

### Exercise 3.4: Creating a New Component (`#codebase`, `/new`)

* **Purpose:** Use Copilot Agents (`/new`) to scaffold.
* **Aim:** Practice the `/new` command with `#codebase` context (as `/new` often requires broad project understanding).
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Agent tasks requiring codebase understanding and new component creation
* **Steps:**
    1.  Open the Copilot Chat view.
    2.  Type the following prompt:
        ```
        #codebase /new Create a new Python module named 'weather_cache.py' in the 'src/weather_cli' package. Include:
        1. A global dictionary cache storage using threading.Lock for thread safety.
        2. A CACHE_DURATION_SECONDS = 300 (5 minutes) constant.
        3. A CacheEntry class (or namedtuple) with 'data: WeatherData' and 'timestamp: float'.
        4. A put(city: str, data: WeatherData) -> None function.
        5. A get(city: str) -> Optional[WeatherData] function checking for non-expired entries.
        Include proper type hints and docstrings.
        ```
    3.  Copilot should propose creating the new file (`src/weather_cli/weather_cache.py`). Review and approve.
    4.  *(Follow-up Task)* Manually integrate this `weather_cache` into `WeatherService` (you could use "Edits" mode for this).

### Exercise 3.5: Reviewing Code Changes (`#changes`, `/explain`)

* **Purpose:** Use Copilot to summarize pending changes.
* **Aim:** Practice using `#changes`.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple change summarization task
* **Steps:**
    1.  Make a few small, distinct changes to one or two files (e.g., add a comment in `main.py`, modify the output format slightly).
    2.  **Save the files.**
    3.  Open the Source Control view in VS Code (usually the Git icon). You should see your modified files listed under "Changes".
    4.  *(Optional)* Stage one of the changes, leaving another unstaged.
    5.  Open the Copilot Chat view.
    6.  Type the following prompt:
        ```
        #changes /explain Summarize the main themes or purposes of the current staged and unstaged code changes.
        ```
    7.  Review Copilot's summary of your pending modifications.

### Exercise 3.6: Extracting and Applying Project Style Guidelines

* **Purpose:** To ensure Copilot-generated code aligns with your project’s style and linting rules.
* **Aim:** Practice using Copilot to summarize your code style (from Black, Flake8, and mypy), and use that summary to create a `.copilot-instructions.md` file for consistent code generation.
* **Steps:**
    1. **Summarize Style Rules:**
        - Open Copilot Chat.
        - Reference your `pyproject.toml`, `setup.cfg`, and `requirements-dev.txt` (add them to context using `#` or drag-and-drop).
        - Prompt:  
          ```
          /explain Summarize the most important code style and linting rules for this project, based on Black, Flake8, and mypy configurations. Focus on formatting, naming, typing, and any strict rules that should be followed.
          ```
        - Review Copilot’s summary and copy the key points.
    2. **Draft Copilot Instructions:**
        - In Copilot Chat, prompt:  
          ```
          Based on the summarized style rules, generate a concise .copilot-instructions.md file that guides Copilot to produce code matching these standards. Include only the most important and actionable rules.
          ```
        - Review and refine the generated instructions.
    3. **Create the Instructions File:**
        - Create a `.github` folder in your project root if it doesn’t exist.
        - Add a `.copilot-instructions.md` file with the generated content.
    4. **Explain the Rationale:**
        - Note: By providing Copilot with your style guide, you help ensure that generated code is consistent with your project’s standards, reducing the need for manual reformatting or linting fixes.

### Exercise 3.7: Customizing Copilot with Shared Instructions

* **Purpose:** Influence Copilot generation via `.github/copilot-instructions.md`.
* **Aim:** Define instruction, observe effect.
* **🤖 Recommended Model:** Claude Sonnet 3.5 for creating instructions, GPT-4.1 for applying them - Instructions creation requires reasoning, application is straightforward
* **Steps:**
    1.  **Create Instruction File:**
        * In the root of your project workspace, create a folder named `.github` if it doesn't already exist.
        * Inside the `.github` folder, create a new file named `copilot-instructions.md`.
    2.  **Define Instruction:**
        * Open `copilot-instructions.md` and add the following content:
            ```markdown
            # Copilot Instructions for Python Weather CLI App

            ## Python Development Guidelines

            - **Logging:** For application logging, always use the `logging` module. Get logger instances using `logging.getLogger(__name__)`. Avoid using `print()` statements for routine logging within application logic. Use appropriate log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) and log exceptions within except blocks using `logger.exception()` or `logger.error()` with exc_info=True.
            - **Type Hints:** Always include type hints for function parameters and return values. Use `typing` module imports like `Optional`, `List`, `Dict` when needed.
            ```
        * Save the file. *Note: Copilot should automatically detect and use these instructions for subsequent requests in this workspace. It might take a moment to register.*
    3.  **Apply Instruction (Add Logging):**
        * Open the file `src/weather_cli/weather_service.py`.
        * Locate the `get_weather(self, city: str)` method.
        * **Select the entire body** of the `get_weather` method (from the docstring to the return statement).
        * Open the Copilot Chat view.
        * **Select the "Edits" mode** from the dropdown menu.
        * In the chat input, **type the instruction** (notice we *don't* specify *how* to log, letting the instructions file guide Copilot):
            ```
            Add logging to this method:
            1. At the beginning, log the city being requested at INFO level.
            2. After successfully fetching weather_data, log the retrieved temperature at INFO level.
            3. Within the except block, log the caught WeatherApiException at ERROR level, including the exception details.
            Ensure the necessary logger instance is created if it doesn't exist.
            ```
        * Press Enter.
    4.  **Observe Result:**
        * Review the diff proposed by Copilot.
        * **Verify:** Did Copilot add code to get a logger using `logging.getLogger(__name__)`? Did it use appropriate logging methods like `logger.info()` and `logger.error()` or `logger.exception()` for logging, rather than `print()` statements?
        * If the instructions were picked up correctly, the generated code should follow the guideline specified in `copilot-instructions.md`. Apply the changes if they look correct and follow the instructions.

### Exercise 3.8: Full Implementation Workflow (Ideate -> Spec -> Implement -> Refactor)

* **Purpose:** To simulate a small feature development lifecycle using various Copilot capabilities sequentially.
* **Aim:** Practice using Ask mode for ideation/spec, `#` file referencing for implementation guidance, and Edits mode for refinement.
* **🤖 Recommended Model:** GPT-4.1 for ideation, Claude Sonnet 3.7 for specifications and implementation - Gradual increase in complexity
* **Steps:**
    1.  **A. Ideate (Ask):** In Copilot Chat (Ask mode), prompt:
        ```
        @workspace Suggest a simple new feature for this weather CLI app. For example, something related to units or output format.
        ```
        Let's assume Copilot suggests adding a choice between Celsius and Fahrenheit units.
    2.  **B. Specify (Ask):** Continue the chat:
        ```
        Generate a short technical specification in Markdown format for adding a command-line option (`--units`) to specify temperature units (Celsius 'C' or Fahrenheit 'F'). Default should be Celsius. Specify required changes to input handling, data storage/processing (if any), and output display.
        ```
    3.  **C. Save Specification:** Copy the generated Markdown spec. Create a new file in the `docs/` directory named `UnitsFeature.md` and paste the content. Save the file.
    4.  **D. Plan Implementation (Ask):** In Copilot Chat:
        ```
        #codebase Based on the feature described in #file:docs/UnitsFeature.md, outline the implementation steps. Which Python files likely need changes, and what are the key modifications required in each (e.g., argument parsing, data model, service logic, output formatting)?
        ```
        Review the plan provided by Copilot.
    5.  **E. Implement Changes (Edits/Ask/Completion):** Based on the plan from Step D:
        * Open the primary file for argument parsing (likely `main.py`). Use Edits mode (selecting relevant sections) or Ask mode (`#file:docs/UnitsFeature.md #file:src/weather_cli/main.py Show me how to add command-line argument parsing for '--units' using argparse.`) to implement argument handling. Use code completion.
        * Open `weather_data.py`. If the spec requires storing the unit or performing conversion, use Edits mode or Ask (`#file:docs/UnitsFeature.md #file:src/weather_cli/weather_data.py Suggest changes needed in this class based on the spec.`)
        * Open `main.py` again (or the relevant display class). Use Edits mode or Ask (`#file:docs/UnitsFeature.md #file:src/weather_cli/main.py Update the output display logic to show the temperature in the selected unit (C or F) and include the unit symbol.`) Apply changes.
    6.  **F. Refine (Edits):** Review the implemented code. Select sections that could be cleaner or more robust. Use Edits mode with prompts like "Refactor this temperature conversion logic for clarity" or "Add error handling if the --units argument is invalid."

### Exercise 3.9: Reviewing Inline Chat Suggestions

* **Purpose:** To practice exploring multiple code suggestions provided by Copilot's inline chat.
* **Aim:** Use inline chat for a simple task and explicitly cycle through the different options Copilot offers.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple docstring generation with multiple suggestions
* **Steps:**
    1.  Open `src/weather_cli/weather_data.py`.
    2.  Select the entire `WeatherData` class definition.
    3.  Open inline chat (Default: `Cmd+I` / `Ctrl+I`).
    4.  Type the prompt: `/doc Generate docstring for this class.` and press Enter.
    5.  Copilot will show its first suggestion.
    6.  **Cycle Suggestions:** Use the keyboard shortcut for viewing the next/previous suggestion (e.g., `Alt+]` / `Alt+[` or `Option+]` / `Option+[` - check VS Code's keybindings or the Copilot documentation if these don't work). Observe if Copilot offers alternative phrasings or formats for the docstring.
    7.  Choose the suggestion you prefer and accept it (often by pressing `Tab` or clicking "Accept").

---

## Section 4: Optional Advanced Exercises

**Goal:** Explore more nuanced or specialized applications of GitHub Copilot beyond the basic workflows.

---

### Exercise 4.1: Debugging Assistance (Runtime Errors)

* **Purpose:** Practice using Copilot Chat to understand runtime errors.
* **Aim:** Use `#` file referencing and pasted stack traces to ask Copilot for insights.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Error analysis and debugging requires deeper reasoning and code understanding. Alternative: o3-mini for step-by-step logical debugging analysis
* **Steps:**
    1.  **(Optional Setup - Induce an Error):** Modify `weather_client.py`. Find where data is extracted from the JSON response, for example, `response_data["main"]["temp"]`. Temporarily remove any error handling or default values around a potentially missing field (like `humidity` if you added it, or even `description`). Alternatively, modify a unit test's mock response to return incomplete JSON.
    2.  **Trigger the Error:** Run the application (`python -m weather_cli "London"`) or the modified unit test (`pytest tests/`) in a way that triggers the error (e.g., using a specific city or relying on the faulty mock data). You should see an error message and traceback (like `KeyError`) printed to the console/terminal.
    3.  **Copy the Traceback:** Select and copy the complete traceback from the terminal output.
    4.  **Ask Copilot:** Open the Copilot Chat view. Type a prompt including the relevant file context (using `#` interactive selection) and the pasted traceback:
        ```
        #file:src/weather_cli/weather_client.py /explain I encountered the following runtime error when running the application. Based on the code in the referenced file and this traceback, what could be the likely cause? What are some potential fixes or checks I should add?

        [Paste the full traceback here]
        ```
    5.  **Analyze Suggestion:** Review Copilot's explanation of the error and the suggested fixes (e.g., adding key existence checks, using `.get()` method with defaults, checking response structure if applicable).

### Exercise 4.2: Commit Message Generation

* **Purpose:** To leverage Copilot for drafting standardized Git commit messages.
* **Aim:** Use the `#changes` context variable to ask Copilot Chat to generate a commit message based on pending code changes.
* **🤖 Recommended Model:** GPT-4.1 (default) - Simple commit message generation task
* **Steps:**
    1.  **Ensure Pending Changes:** Make sure you have some uncommitted changes in your workspace (staged or unstaged), perhaps from completing previous exercises.
    2.  **Open Copilot Chat:** Navigate to the Copilot Chat view.
    3.  **Generate Commit Message:** Type the following prompt:
        ```
        #changes /explain Generate a concise Git commit message summarizing these code changes. Follow the Conventional Commits specification (e.g., using prefixes like 'feat:', 'fix:', 'refactor:', 'test:', 'docs:', 'chore:').
        ```
    4.  **Review:** Evaluate the generated commit message. Is it accurate? Does it follow the requested format? You can use this as a starting point for your actual commit.

### Exercise 4.3: Code Review Assistance (Security & Performance) (`#codebase`)

* **Purpose:** To use Copilot as a preliminary reviewer to identify potential areas of concern in the codebase.
* **Aim:** Practice asking targeted questions about security and performance using `#codebase` (often works well for analysis requiring broad context).
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Comprehensive security and performance analysis requires advanced reasoning
* **Steps:**
    1.  **Open Copilot Chat:** Navigate to the Copilot Chat view.
    2.  **Ask about Security:** Type the following prompt:
        ```
        #codebase /explain Review the application, particularly how the OpenWeatherMap API key is handled and how external data is fetched and processed. Are there any potential security vulnerabilities, risks, or recommended best practices being missed?
        ```
        Review Copilot's analysis (it might point out risks if the key were hardcoded, suggest environment variables - which you already use, or comment on input validation if applicable).
    3.  **Ask about Performance:** Type the following prompt:
        ```
        #codebase /explain Analyze the application's code, focusing on areas like HTTP client interactions, JSON parsing, and any data manipulation. Are there any obvious potential performance bottlenecks or suggestions for optimization?
        ```
        Review Copilot's suggestions (it might mention caching - which you could explore, efficient string handling, or minimizing API calls if applicable).

### Exercise 4.4: Exploring Alternative Implementations

* **Purpose:** To ask Copilot for different ways to achieve the same programming task.
* **Aim:** Use `#selection` and `#` file referencing (interactive) to request alternatives.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Architectural alternatives and trade-off analysis requires deeper reasoning
* **Steps:**
    1.  **Select Code:** Open `src/weather_cli/weather_client.py`. Select the block of code inside the `get_weather_from_api` method that is responsible for parsing the JSON response into the `WeatherData` object (likely involving dictionary access and WeatherData construction).
    2.  **Open Copilot Chat:** Navigate to the Copilot Chat view.
    3.  **Add Context and Prompt:**
        * Type `#selection` (to add selected code).
        * Type `#` and select `requirements.txt`.
        * Append the following prompt and press Enter:
          ```
          /explain Show me an alternative way to implement the selected code's functionality (parsing JSON to a Python object). Could it be done using a different approach like Pydantic models, dataclasses with dacite, or perhaps using the requests library's built-in JSON handling differently? Check the available dependencies. Briefly discuss any trade-offs.
          ```
    4.  **Evaluate Options:** Review the alternative implementation(s) suggested by Copilot. Consider their clarity, efficiency, and dependencies compared to the original code.

---

## Section 5: Advanced GUI Development (Expert Level)

**⚠️ ADVANCED SECTION - EXPERT LEVEL ⚠️**

**Goal:** Create a graphical user interface for the weather CLI application using a structured, enterprise-grade workflow that emphasizes planning, specifications, and iterative development with proper documentation and testing guardrails.

**🔄 WORKFLOW APPROACH:**
This section follows a professional development workflow that progresses through distinct phases:
1. **Ideation** (Ask mode) → **Requirements** (Edits mode) → **Specifications** (Agent mode) → **Implementation Planning** → **Guided Implementation**

**🤖 MODEL RECOMMENDATIONS:**
- **Planning & Ideation:** Claude Sonnet 3.7 (high power for creative thinking and architectural reasoning)
- **Documentation & Specifications:** Claude Sonnet 4 (highest power for comprehensive analysis) - *Preview feature, may not be available to all users*
- **Implementation:** Claude Sonnet 3.7 or 4 (highest power for code generation and codebase analysis) - *Note: Claude 4 is a preview feature*
- **Simple Agent Tasks:** GPT-4.1 when given clear, specific instructions from higher-power model planning

**Prerequisites for Section 5:**
- Completion of Sections 1-4 (especially Exercise 3.5.1 for project style guidelines)
- Strong understanding of Python GUI frameworks
- Familiarity with testing GUI applications
- Experience with event-driven programming
- Understanding of TDD (Test-Driven Development) principles

---

### Exercise 5.1: Feature Ideation and Conceptualization (Ask Mode)

* **Purpose:** Use Ask mode to brainstorm and conceptualize the GUI feature at a high level.
* **Aim:** Practice using moderate-power models for creative exploration and requirement gathering.
* **🤖 Recommended Model:** Claude Sonnet 3.7 - Creative ideation and architectural thinking benefits from superior reasoning
* **Steps:**
    1.  Open the Copilot Chat view in Ask mode with Claude Sonnet.
    2.  Start broad ideation:
        ```
        @workspace I want to add a GUI interface to this weather CLI application. Let's brainstorm the approach:
        
        1. What are the key user workflows that the GUI should support?
        2. How should the GUI relate to the existing CLI functionality?
        3. What are the main technical considerations for GUI framework choice?
        4. What would be a good starting feature set for an MVP?
        
        Keep this high-level - we're exploring concepts, not implementation details yet.
        ```
    3.  Continue the discussion to refine the concept:
        ```
        Based on our discussion, let's focus on a specific GUI feature to implement first. I'm thinking of a simple weather lookup window. What should be the core user experience and main technical requirements?
        ```
    4.  **Decision Point:** When you feel the conceptual discussion has reached a good understanding of what you want to build, proceed to the next exercise.

### Exercise 5.2: Requirements Documentation (Edits Mode)

* **Purpose:** Create formal requirements documentation based on the ideation phase.
* **Aim:** Practice using Edits mode to generate structured documentation with higher-power models.
* **🤖 Recommended Model:** Claude Sonnet 4 - Complex documentation generation requiring comprehensive analysis (Preview feature)
* **Steps:**
    1.  Switch to Edits mode with Claude Sonnet 4.
    2.  Create a new requirements document:
        ```
        #codebase Create a comprehensive requirements document for the GUI weather application feature we discussed. Structure it as docs/GUI_Feature_Requirements.md with:
        
        1. Executive Summary
        2. User Stories and Use Cases
        3. Functional Requirements
        4. Non-Functional Requirements (performance, usability, compatibility)
        5. Technical Constraints and Dependencies
        6. Success Criteria and Acceptance Tests
        7. Risk Assessment and Mitigation
        
        Base this on our previous discussion and the existing codebase structure.
        ```
    3.  Review the generated requirements document and refine as needed.

### Exercise 5.3: Technical Specifications (Agent Mode)

* **Purpose:** Use Agent mode to create detailed technical specifications by analyzing the codebase.
* **Aim:** Practice using high-power models with Agent mode for comprehensive codebase analysis and specification generation.
* **🤖 Recommended Model:** Claude Sonnet 4 - Most complex analysis task requiring deep codebase understanding (Preview feature, fallback to Claude Sonnet 3.7). Alternative: Claude Sonnet 3.7 with thinking for step-by-step architectural analysis
* **Steps:**
    1.  Switch to Agent mode with Claude 3.7/4.
    2.  Generate comprehensive technical specifications:
        ```
        #codebase Based on the requirements in #file:docs/GUI_Feature_Requirements.md, create a detailed technical specification document docs/GUI_Technical_Specification.md. 
        
        Analyze the existing codebase thoroughly and include:
        
        1. Architecture Overview and Design Patterns
        2. Component Design (classes, modules, interfaces)
        3. Integration Points with Existing Code
        4. Data Flow and State Management
        5. Error Handling and Logging Strategy
        6. Testing Strategy and Test Cases
        7. File Structure and Module Organization
        8. Dependencies and Configuration Changes
        9. Performance Considerations
        10. Security Considerations
        
        Ensure the specification is implementable and follows the existing code patterns and style.
        ```
    3.  Review the technical specification for completeness and accuracy.

### Exercise 5.4: Implementation Planning and Task Breakdown

* **Purpose:** Break down the technical specification into manageable, commit-sized iterations.
* **Aim:** Practice creating detailed implementation plans that support incremental development.
* **🤖 Recommended Model:** Claude Sonnet 4 or 3.7 - Complex planning requiring understanding of dependencies and workflow optimization. Alternative: Claude Sonnet 3.7 with thinking for systematic breakdown of complex tasks
* **Steps:**
    1.  Continue with the high-power model in Agent mode:
        ```
        #codebase Based on #file:docs/GUI_Technical_Specification.md, create an implementation plan that breaks down the work into commit-sized iterations. Create docs/GUI_Implementation_Plan.md with:
        
        1. Development phases with clear milestones
        2. Iteration breakdown (each iteration should be 1-3 hours of work)
        3. Dependencies between iterations
        4. Testing checkpoints for each iteration
        5. Rollback strategies for each phase
        6. Integration points and validation steps
        
        Each iteration should be small enough to be completed and committed independently, allowing for incremental progress tracking.
        ```
    2.  Generate a TODO tracking document:
        ```
        Based on the implementation plan, create docs/GUI_Feature_TODO.md that tracks:
        
        1. Implementation status for each iteration
        2. Completed tasks with commit references
        3. Current focus area
        4. Blockers and issues
        5. Next steps
        
        Format it for easy updating as work progresses.
        ```

### Exercise 5.5: Establishing Implementation Guardrails

* **Purpose:** Set up proper guardrails and guidelines before starting implementation.
* **Aim:** Practice creating comprehensive development guidelines and test frameworks.
* **🤖 Recommended Model:** Claude Sonnet 4 or 3.7 - Complex guideline creation requiring deep understanding of best practices
* **Steps:**
    1.  **Update Project Guidelines:** Enhance the existing `.github/copilot-instructions.md`:
        ```
        #file:.github/copilot-instructions.md #file:tests/TESTING.md #codebase 
        
        Update the copilot-instructions.md file to include GUI-specific development guidelines:
        
        1. GUI framework conventions and patterns
        2. Testing approaches for GUI components (refer to TESTING.md)
        3. File organization for GUI modules
        4. Error handling patterns for GUI applications
        5. Performance considerations for GUI operations
        6. Accessibility requirements
        
        Keep existing guidelines and add GUI-specific ones.
        ```
    2.  **Create Agent Workflow Guidelines:** Create a new file for implementation workflow:
        ```
        Create docs/Agent_Implementation_Guidelines.md with:
        
        1. Agent workflow and responsibilities
        2. DO's and DON'Ts for implementation
        3. Code review and testing checkpoints
        4. How to reference specification and TODO files
        5. Commit message conventions for this feature
        6. When to pause and seek human review
        7. TDD workflow guidelines
        8. Integration testing procedures
        
        This should guide the agent during implementation without containing implementation-specific details.
        ```
    3.  **Set up TDD Framework:** Prepare the testing groundwork:
        ```
        #file:tests/TESTING.md #codebase Create initial test scaffolding for GUI components following TDD principles:
        
        1. Test file structure for GUI components
        2. Mock strategies for GUI testing
        3. Fixture setup for GUI test scenarios
        4. Test utilities and helpers
        5. Integration test framework setup
        
        Create the test files but leave test implementations for the TDD cycle during implementation.
        ```

### Exercise 5.6: Guided Agent Implementation

* **Purpose:** Execute the implementation using the agent with proper guidance and documentation.
* **Aim:** Practice managing an agent through complex implementation tasks with proper guardrails.
* **🤖 Recommended Model:** Claude Sonnet 4 for initial setup and complex decisions, GPT-4.1 for straightforward implementation tasks when given clear instructions
* **Steps:**
    1.  **Initialize Implementation Session:** Start with clear context:
        ```
        #codebase I'm ready to implement the GUI feature. Please review:
        
        - Technical specification: #file:docs/GUI_Technical_Specification.md
        - Implementation plan: #file:docs/GUI_Implementation_Plan.md  
        - Current TODO status: #file:docs/GUI_Feature_TODO.md
        - Implementation guidelines: #file:docs/Agent_Implementation_Guidelines.md
        - Project guidelines: #file:.github/copilot-instructions.md
        
        Start with the first iteration from the implementation plan. Follow TDD approach:
        1. Create failing tests first
        2. Implement minimal code to pass tests
        3. Refactor and improve
        4. Update TODO.md with progress
        5. Suggest when to commit
        
        Begin with iteration 1 from the implementation plan.
        ```
    2.  **Iterative Implementation:** For each iteration:
        - Let the agent implement following TDD
        - Review and commit after each iteration
        - Update the TODO.md file
        - Validate against specifications
        - Move to next iteration only after current is complete
    3.  **Integration Testing:** After core implementation:
        ```
        Now let's run integration tests and validate the implementation against our original requirements:
        
        1. Test all user workflows from the requirements document
        2. Validate non-functional requirements
        3. Run full test suite
        4. Check performance benchmarks
        5. Validate against success criteria
        
        Reference: #file:docs/GUI_Feature_Requirements.md
        ```

### Exercise 5.7: Implementation Review and Documentation

* **Purpose:** Complete the feature development cycle with proper documentation and review.
* **Aim:** Practice comprehensive feature completion and documentation.
* **🤖 Recommended Model:** Claude Sonnet 3.7 or 4 - Comprehensive review and documentation generation requiring analytical depth (Claude 4 is a preview feature)
* **Steps:**
    1.  **Final Documentation Update:**
        ```
        #codebase Create comprehensive end-user and developer documentation for the completed GUI feature:
        
        1. Update README.md with GUI usage instructions
        2. Create docs/GUI_User_Guide.md with screenshots and examples
        3. Update docs/api_documentation.md with new GUI components
        4. Create docs/GUI_Developer_Guide.md for future developers
        5. Update project documentation with lessons learned
        
        Ensure all documentation is consistent and up-to-date.
        ```
    2.  **Performance and Quality Review:**
        ```
        Conduct a final review of the implemented GUI feature:
        
        1. Performance analysis and optimization recommendations
        2. Code quality assessment
        3. Test coverage analysis
        4. Security review
        5. Accessibility compliance check
        6. Cross-platform compatibility validation
        
        Provide a summary report with any recommended follow-up actions.
        ```