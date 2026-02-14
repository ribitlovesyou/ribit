"""
Chat Skill
Direct OpenAI chat integration.
"""

import logging
import os
from typing import Optional

from framework.api_management import api_manager

logger = logging.getLogger(__name__)

try:
    from openai import AsyncOpenAI

    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False
    logger.warning("openai package not installed")


class ChatSkill:
    """Skill for direct OpenAI chat interactions."""

    def __init__(self):
        self.skill_name = "chat"
        self.required_api_keys = ["OPENAI_API_KEY"]
        api_manager.register_required_keys(self.skill_name, self.required_api_keys)
        self.client: Optional[AsyncOpenAI] = None
        self.model = os.getenv("OPENAI_CHAT_MODEL", "gpt-4o")

    async def initialize(self) -> bool:
        """Initialize the OpenAI client."""
        if not HAS_OPENAI:
            logger.error("openai package not installed")
            return False

        try:
            api_key = await api_manager.get_api_key(self.skill_name, "OPENAI_API_KEY")
            if not api_key:
                logger.error("OpenAI API key not configured")
                return False

            self.client = AsyncOpenAI(api_key=api_key)
            logger.info("Chat skill initialized")
            return True

        except Exception as e:
            logger.error(f"Error initializing Chat skill: {e}")
            return False

    async def chat(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 1024,
    ) -> Optional[str]:
        """Send a chat message."""
        if not self.client:
            if not await self.initialize():
                return None

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"Chat error: {e}")
            return None


chat_skill = ChatSkill()
