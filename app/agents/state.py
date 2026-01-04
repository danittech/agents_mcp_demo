# (c) Danit Consultancy and Development, September-2023, danittech@yahoo.com

""" Agent state definition """

from typing import Annotated, TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages

# ----------------------------------------------------------------------------------------

class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
