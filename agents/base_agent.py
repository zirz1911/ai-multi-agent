"""
Base Agent class for all AI agents in the multi-agent system
"""
from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List
from pydantic import BaseModel, Field


class Message(BaseModel):
    """Message structure for agent communication"""
    sender: str
    content: str
    metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)


class BaseAgent(ABC):
    """Abstract base class for all AI agents"""

    def __init__(self, name: str, role: str, model_name: Optional[str] = None):
        """
        Initialize the agent

        Args:
            name: Unique identifier for the agent
            role: Description of agent's role/specialty
            model_name: Specific model to use (optional)
        """
        self.name = name
        self.role = role
        self.model_name = model_name
        self.conversation_history: List[Message] = []

    @abstractmethod
    def process(self, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """
        Process a message and return a response

        Args:
            message: Input message to process
            context: Optional context information

        Returns:
            Response string from the agent
        """
        pass

    def add_to_history(self, sender: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a message to conversation history"""
        msg = Message(sender=sender, content=content, metadata=metadata or {})
        self.conversation_history.append(msg)

    def get_history(self, last_n: Optional[int] = None) -> List[Message]:
        """
        Get conversation history

        Args:
            last_n: Number of recent messages to return (None = all)

        Returns:
            List of Message objects
        """
        if last_n is None:
            return self.conversation_history
        return self.conversation_history[-last_n:]

    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(name='{self.name}', role='{self.role}')"

    def __repr__(self) -> str:
        return self.__str__()
