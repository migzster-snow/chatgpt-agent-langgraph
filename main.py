from typing import TypedDict, List
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    message: List[HumanMessage]

llm = ChatOpenAI(model="gpt-4o")

def process(state: AgentState) -> AgentState:
    response = llm.invoke(state["message"], )
    print("gpt-4o:", response.content)
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)

agent = graph.compile()

user_input = input("Prompt: ")

agent.invoke({"message": [HumanMessage(content=user_input)]})

"""
Prompt: What is computer science?
gpt-4o: Computer science is the study of computers and computational systems. It encompasses a range of topics related to computation, such as algorithms, data structures, software design, artificial intelligence, machine learning, human-computer interaction, and more. Unlike electrical and computer engineers, computer scientists primarily deal with software and software systems, including their theory, design, development, and application.

Key areas within computer science include:

1. **Theoretical Computer Science**: This area focuses on understanding the fundamental capabilities and limitations of computers. It includes the study of algorithms, computation theory, complexity, and information theory.

2. **Algorithms and Data Structures**: This involves the study of step-by-step procedures for calculations (algorithms) and the organization of data (data structures) within a computer program.

3. **Programming Languages**: This involves designing and implementing languages for expressing computations. This includes syntax, semantics, and optimization of programming languages.

4. **Software Engineering**: This is the application of engineering principles to software development in a systematic method. It involves the design, development, testing, and maintenance of software systems.

5. **Artificial Intelligence and Machine Learning**: These fields concern creating systems that can perform tasks that would normally require human intelligence, including visual perception, speech recognition, decision-making, and language translation.

6. **Networking and Security**: This covers the principles and protocols for the communication between computers and the protection of data and systems from cyber threats.

7. **Databases and Data Science**: This involves storing, retrieving, and analyzing large amounts of data efficiently. Data science often involves the use of statistical methods and algorithms to extract insights from data.

8. **Computer Graphics**: This focuses on the creation, representation, and manipulation of visual images using computers.

9. **Human-Computer Interaction (HCI)**: This area looks at how people interact with computers and designs technologies that let humans interact with computers in novel ways.

Computer science is a dynamic field that has rapidly evolved and continues to grow with advancements in technology and the ever-increasing demand for computational solutions in various industries.
"""