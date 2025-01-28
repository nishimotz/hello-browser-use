from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
import asyncio
from pydantic import BaseModel
import csv


class Conference(BaseModel):
    name: str
    location: str
    date: str
    description: str
    url: str


class Conferences(BaseModel):
    conferences: list[Conference]


controller = Controller(output_model=Conferences)


async def main():
    agent = Agent(
        task="2025年に開催される世界の PyCon および Python 関連技術のカンファレンスについて、開催場所、開催日程、概要、ウェブサイトURLをGoogleで調べてください。概要を日本語にして、日付順に出力してください。",
        llm=ChatOpenAI(model="gpt-4o"),
        controller=controller,
    )
    history = await agent.run()
    result = history.final_result()
    if result:
        parsed: Conferences = Conferences.model_validate_json(result)
        for conference in parsed.conferences:
            print(
                conference.name,
                conference.location,
                conference.date,
                conference.description,
            )

        with open('conferences.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Location', 'Date', 'Description', 'URL'])
            for conference in parsed.conferences:
                writer.writerow([conference.name, conference.location, conference.date, conference.description, conference.url])
    else:
        print("No result")


if __name__ == "__main__":
    asyncio.run(main())
