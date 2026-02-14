"""
LiteLLM Skill
Provides LLM access through LiteLLM for both local and remote models.
"""

import logging
import os
from typing import Optional

from framework.api_management import api manager

logger = logging.getLogger(__name__)

try:
    import litellm

    HAS_LITELLM = True
except ImportError:
    HAS_LITELLM = False
    logger.warning("litellm not installed")


class LiteLLMSkill:
    """Skill for interacting with LLMs via LiteLLM."""

    def __init__(self):
        self.skill_name = "lite_llm"
        self.required_api_keys = ["OPENAI_API_KEY"]
        api_manager.register_required_keys(self.skill_name, self.required_api_keys)
        self.model = os.getenv("LITELLM_MODEL", "gpt-4o")
        self._initialized = False

    async def initialize(self) -> bool:
        """Initialize the LLM skill."""
        if not HAS_LITELLM:
            logger.error("litellm package not installed")
            return False

        try:
            api_key = await api_manager.get_api_key(self.skill_name, "OPENAI_API_KEY")
            if not api_key:
                logger.error("OpenAI API key not configured")
                return False

            self._initialized = True
            logger.info(f"LiteLLM skill initialized with model: {self.model}")
            return True

        except Exception as e:
            logger.error(f"Error initializing LiteLLM skill: {e}")
            return False

    async def chat(
        self,
        prompt: str,
        system_prompt: Optional[str] = None,
        max_tokens: int = 1024,
        temperature: float = 0.7,
    ) -> Optional[str]:
        """Send a chat completion request."""
        if not self._initialized:
            if not await self.initialize():
                return None

        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})

        try:
            response = litellm.completion(
                model=self.model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].message.content

        except Exception as e:
            logger.error(f"LiteLLM chat error: {e}")
            return None

    async def generate_code(self, description: str) -> Optional[str]:
        """Generate Python code from a description."""
        system = (
            "You are an expert Python developer. Generate clean, well-documented Python code. "
            "Return ONLY the code, no explanations."
        )
        return await self.chat(description, system_prompt=system, temperature=0.3)


lite_llm_skill = LiteLLMSkill()
