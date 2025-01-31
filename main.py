from langchain_openai import ChatOpenAI
from browser_use import Agent, Controller
import asyncio
from pydantic import BaseModel
import csv

task = """
## タスク

以下の一覧を作ります。

- 2014年以降の PyCon US カンファレンス

英語または日本語で情報が記載されているものを調べてください。

なるべく多くの情報を見つけてください。

また、参加者や登壇者の評判がわかれば、要約して、クチコミとして出力してください。

## 出力したいデータ

概要を日本語にして、
- 名称 Name
- 開催場所 Location
- 開催日程 Date
- 概要(日本語でない場合は日本語に翻訳) Description
- ウェブサイトURL URL
- クチコミ Comment

### 備考

- 開催日程がある場合は、開始日を YYYY-MM-DD の形式にして、開催日程とする
- 開催日程がない場合は、開催日程を空文字列とする

## 出力形式

Name,Location,Date,Description,URL,Comment

"""

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
        task=task,
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
