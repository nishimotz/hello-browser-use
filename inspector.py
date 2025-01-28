from browser_use import BrowserUse

async def inspect_ui_elements():
    browser = BrowserUse()
    
    try:
        # Google Flightsにアクセス
        await browser.goto("https://www.google.com/flights")
        
        # UIの要素を調査
        elements_info = await browser.inspect_elements([
            # 出発地入力フィールド
            {
                "name": "departure_input",
                "selector": "input[placeholder='出発地']",
                "attributes": ["id", "class", "aria-label"]
            },
            # 目的地入力フィールド
            {
                "name": "destination_input",
                "selector": "input[placeholder='目的地']",
                "attributes": ["id", "class", "aria-label"]
            },
            # 日付選択フィールド
            {
                "name": "date_picker",
                "selector": "input[placeholder='日付を選択']",
                "attributes": ["id", "class", "aria-label"]
            },
            # 検索ボタン
            {
                "name": "search_button",
                "selector": "button:has-text('検索')",
                "attributes": ["id", "class", "role"]
            },
            # フライト結果カード
            {
                "name": "flight_card",
                "selector": ".flight-result-card",
                "attributes": ["class", "role"]
            }
        ])
        
        # 結果をログに出力
        print("UI Elements Information:")
        print(json.dumps(elements_info, indent=2, ensure_ascii=False))
        
    except Exception as e:
        print(f"Error during inspection: {e}")
        
    finally:
        await browser.close()