from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

async def main():
    agent = Agent(
        task="2025年1月12日にバリからオマーンへの片道フライトをGoogleフライトで探してください。最も安いオプションを教えてください。",
        llm=ChatOpenAI(model="gpt-4o"),
    )
    result = await agent.run()
    print(result)

asyncio.run(main())
