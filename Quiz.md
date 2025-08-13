
---

**1. AgentHooks Callback**
Which AgentHooks method is called after the agent’s reasoning but before any **TOOL CALL**? 
A. on_agent_start
B. on_agent_action
C. on_tool_start✅
D. on_agent_end
E. None of the above
---

**2. AgentOutputSchemaBase**
Which two methods must any `AgentOutputSchemaBase` subclass implement?
A. `is_plain()` and `execute_tool()`
B. `name()` and `execute_tool()`
C. `json_schema()` and ` `is_plain()_text`✅
D. .format_output() and parse_input()
E.`to_dict()` and `from_json()`

---

**3. Runner Variants**
What’s the key difference between run_sync() and run_streamed()?
A. `run— sync` blocks until it complete and return RunResults;`run_streamed` yeilds RunltemStream event chunks as they arrive.✅
B. `run_stream()` — event stream version
C. `run_sync()` cannot invoke tools in streamed calls
D. They behave identically under the hood
E. None of the above

---

**4. FileSearchTool vs WebSearchTool**
When would you use a `FileSearchTool` instead of a `WebSearchTool`?
A. To search public APIs
B. To scrape live web pages
C. To call a local shell command for searching
D. To search within user-uploaded files stored in a vector store✅
E. None of the above

---

**5. Handoff Input Filter**
The `input_filter` parameter in a `handoff()` call controls:
A. Which messages from history are passed to the next agent✅
B. How many times a handoff can occur
C. Whether to log the handoff event
D. The tool schema used for the handoff
E. None of the above

---

**6. Input Guardrail Trigger**
A tripwire in an `input_guardrail` raises which exception?
A. `AgentException`
B. `InputGuardrailTripwireTriggered`✅
C. `UserError`
D. `ModelBehaviorError`
E. None of the above

---

**7. Span Types**
Which span type logs the execution of a function?
A. `GenerationSpanData`
B. `HandoffSpanData`
C. `FunctionSpanData`✅
D. `GuardrailSpanData`
E. `FunctionSpanDataOutput`

---

**8. trace() Usage**
To group several runs under the same trace ID for observabilty you should:
A. Call with `trace("my_trace_id")`: arround each Runner.run()✅
B. Pass trace="MyTrace'to each agent  constructor
C. Use add_trace_processor() only once at startup
D. Use `group_id` in `RunConfig`
E. All of them

---

**9. RunErrorDetails Contents**
Which field **isn`t** part of `RunErrorDetails`?
A. `message` (the error text)
B. `error_type` (the exception class name)
C. `stack_trace` (call stack)
D. `final_output` (the last successful output)✅
E. None of the above

---

**10. ModelProvider vs ModelSettings**
Which holds the credentials (e.g., API key) for calling an LLM?
A. `ModelSettings`
B. `ModelProvider`
C. `OpenAIChatCompletionsModel` directly
D. `RunConfig`
E. None of the above✅

---

**11. StreamEvent Subclass**
Which event type carries the raw chunk from the LLM before it’s parsed?
A. `AgentUpdatedStreamEvent`
B. `RawResponseStreamEvent`✅
C. `ToolCallOutputItem`
D. `ReadingItem`
E. None of the above

---

**12. Exception Hierarchy**
If an LLM returns output that fails the declared output-type schema, the SDK raises:
A. `InvalidSchemaError`
B. `UserError`
C. `ModelBehaviourError`✅
D. `AgentError`
E. None of above
---
