from folio import Agent

# 1. Normal MCP
agent = Agent(enable_mcp=True)
agent.run("Get the current weather in Mumbai and get information about Japan.")

#-------------------------------------------------------------------------------

# 2. Customized Multi-Step
agent = Agent(
    enable_mcp=True,
    agent_model="mistral-medium-latest",
    agent_prompt="summarize the content into 5 lines and no bullet points"
)

agent.run(
    "Get information about virat kholi, make a pdf of that information,"
    "and upload pdf to Slack."
)

#-------------------------------------------------------------------------------

# 3. Customized Agent
agent = Agent(
    enable_mcp=True,
    agent_model="mistral-medium-latest",
    agent_prompt="summarize the content into 5 lines and no bullet points"
)

agent.run("Get information about virat kholi")

#-------------------------------------------------------------------------------

# 4. Observer Recovery
agent = Agent(enable_mcp=True)

agent.run("Get information about the top programming languages and save it to Excel.")

#-------------------------------------------------------------------------------

# 5. RAG - AGENT
# Enable RAG -> can use RAG system
agent = Agent(enable_rag = True)    

# upload your file path
agent.ingest(r"C:/Users/Parin/Downloads/t.pdf")  

# QUESTIONS: 
print("<>-----------------------------------------<>")
agent.run("What is the name of company ?")
print("<>-----------------------------------------<>")
agent.run("Give me Financial Performance of year 2024.")
print("<>-----------------------------------------<>")
agent.run("Define Key Risks?")
print("<>-----------------------------------------<>")
agent.run("What are the growth strategy?")
print("<>-----------------------------------------<>")
agent.run("Who is the CEO of this company, and when was it founded?")
print("<>-----------------------------------------<>")