# Hello Browser Use

macOS で [browser-use](https://github.com/browser-use/browser-use) を試した記録。

```shell
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install
```

.env ファイルを作成し、OPENAI_API_KEY を設定する。

```txt
OPENAI_API_KEY=sk-proj-****
```

2025年に開催される世界の PyCon および Python 関連技術のカンファレンスについて、開催場所、開催日程、概要、ウェブサイトURLをGoogleで調べてください。概要を日本語にして、日付順に出力してください。

```shell
% python main.py 
```

実行すると Chrome が起動し、ブラウザの操作が行われる。

```csv
Name,Location,Date,Description,URL
PyCon US 2025,"Pittsburgh, Pennsylvania, USA",2025年5月14日 - 5月22日,PyCon US 2025はピッツバーグで完全対面で開催されます。今年はメインコンファレンスのライブストリーミングはありません。,https://us.pycon.org
PyCon+Web 2025,"Berlin, Germany",2025年1月24日 - 1月25日,ベルリンで開催されるPyCon+Web 2025。,https://python.org/events
Python Meeting Düsseldorf,"Düsseldorf, Germany",2025年1月22日,デュッセルドルフで開催されるPythonミーティング。,https://python.org/events
PyCon APAC 2025,フィリピン,TBD,フィリピンで開催されるPyCon APAC 2025。,https://pycon-apac.python.ph
PyCon JP 2025,"広島市, Japan",2025年9月26日 - 9月27日,広島国際会議場で開催されるPyCon JP 2025。,https://2025.pycon.jp
```

agent_history.gif が作成される。

![agent_history](./agent_history.gif)

## Output Format

[Output Format](https://docs.browser-use.com/customize/output-format) サンプルを参考にしている。

```python
from pydantic import BaseModel

class Conference(BaseModel):
    name: str
    location: str
    date: str
    description: str
    url: str

class Conferences(BaseModel):
    conferences: list[Conference]

controller = Controller(output_model=Conferences)
```
