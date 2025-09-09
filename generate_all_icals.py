from icalendar import Calendar, Event
from datetime import datetime
import pytz

# 日本標準時のタイムゾーン
jst = pytz.timezone("Asia/Tokyo")

# 既存のイベント情報（元のウェブサイトから抽出）
events = [
    {
        "filename": "20250710_webinar.ics",
        "title": "依頼医が知っておくべきアミロイドPET検査の正しい使い方、評価方法 ~CSF検査との違いを含む~",
        "organizer": "日本メジフィジックス株式会社",
        "start_date": "2025-07-10",
        "start_time": "19:00",
        "end_time": "19:45",
        "format": "オンライン(ライブ)のみ",
        "location": "なし"
    },
    {
        "filename": "20250722_webinar.ics",
        "title": "乳癌周術期薬物療法のアルゴリズムにおけるPET/CTの重要性",
        "organizer": "日本メジフィジックス株式会社",
        "start_date": "2025-07-22",
        "start_time": "19:00",
        "end_time": "19:45",
        "format": "オンライン(ライブ)のみ",
        "location": "なし"
    },
    {
        "filename": "20250724_conference.ics",
        "title": "Alzheimer\\\\\\\'s Disease Network Conference in 大阪北部",
        "organizer": "エーザイ株式会社、バイオジェン・ジャパン株式会社",
        "start_date": "2025-07-24",
        "start_time": "19:30",
        "end_time": "20:40",
        "format": "現地のみ",
        "location": "梅田スカイビルタワーイースト33階 〒531-6032 大阪府大阪市北区大淀中1丁目1-88"
    },
    {
        "filename": "20250725_training.ics",
        "title": "弘道会7月合同研修会",
        "organizer": "弘道会",
        "start_date": "2025-07-25",
        "start_time": "18:00",
        "end_time": "20:00",
        "format": "現地のみ",
        "location": "守口文化センター・エナジーホール (京阪電車・守口市駅前)"
    },
    {
        "filename": "20250904_webinar.ics",
        "title": "WEB講演会 アキュミンR静注 臨床使用開始から 1年間の足跡",
        "organizer": "日本メジフィジックス株式会社",
        "start_date": "2025-09-04",
        "start_time": "19:00",
        "end_time": "19:45",
        "format": "オンライン(ライブ)のみ",
        "location": "なし"
    },
    {
        "filename": "20250916_webinar.ics",
        "title": "Dementia Live Seminar",
        "organizer": "エーザイ株式会社／バイオジェン・ジャパン株式会社",
        "start_date": "2025-09-16",
        "start_time": "19:00",
        "end_time": "20:00",
        "format": "Live配信",
        "location": "東京会場より Live配信"
    },
    {
        "filename": "20250919_training.ics",
        "title": "弘道会9月合同研修会",
        "organizer": "弘道会",
        "start_date": "2025-09-19",
        "start_time": "18:00",
        "end_time": "20:00",
        "format": "現地のみ",
        "location": "守口文化センター・エナジーホール (京阪電車・守口市駅前)"
    },
    {
        "filename": "20250924_webinar.ics",
        "title": "症例から学ぶ中枢神経領域の画像診断 〜脊髄・脊椎領域の押さえておくべきトピック2025〜",
        "organizer": "ゲルべ・ジャパン株式会社",
        "start_date": "2025-09-24",
        "start_time": "19:00",
        "end_time": "19:40",
        "format": "WEBセミナー",
        "location": "なし"
    },
    {
        "filename": "20251011_conference.ics",
        "title": "Brain Function Imaging Conference",
        "organizer": "日本メジフィジックス株式会社",
        "start_date": "2025-10-11",
        "start_time": "12:55",
        "end_time": "17:10",
        "format": "オンライン(ライブ+追いかけ再生)および別内容をオンデマンド配信",
        "location": "なし"
    },
    {
        "filename": "20251004_kansai_user_meeting.ics",
        "title": "第9回 関西ユーザ会",
        "organizer": "PSP株式会社",
        "start_date": "2025-10-04",
        "start_time": "14:30",
        "end_time": "19:30",
        "format": "現地のみ",
        "location": "大阪御堂筋ビル 貸し会議室（Ｍ3 会議室） 〒541-0056 大阪市中央区久太郎町 4-1-3 大阪御堂筋ビル地下 4 階"
    }
]

def create_ical_file(event_info):
    # カレンダーオブジェクトを作成
    cal = Calendar()
    cal.add("prodid", "-//Manus Agent//Event Calendar//JP")
    cal.add("version", "2.0")
    cal.add("calscale", "GREGORIAN")
    cal.add("method", "PUBLISH")
    
    # イベントオブジェクトを作成
    event = Event()
    event.add("summary", event_info["title"])
    event.add("organizer", event_info["organizer"])
    
    # 日時の設定（日本標準時）
    start_datetime = datetime.strptime(f"{event_info['start_date']} {event_info['start_time']}", "%Y-%m-%d %H:%M")
    end_datetime = datetime.strptime(f"{event_info['start_date']} {event_info['end_time']}", "%Y-%m-%d %H:%M")
    
    # JSTタイムゾーンを設定
    start_datetime_jst = jst.localize(start_datetime)
    end_datetime_jst = jst.localize(end_datetime)
    
    event.add("dtstart", start_datetime_jst)
    event.add("dtend", end_datetime_jst)
    
    # 説明とロケーション
    description = f"開催形式：{event_info['format']}"
    event.add("description", description)
    
    if event_info["location"] != "なし":
        event.add("location", event_info["location"])
    
    # 作成日時
    event.add("dtstamp", datetime.now(jst))
    event.add("uid", f"{event_info['filename'].replace('.ics', '')}@miyakohp.github.io")
    
    # カレンダーにイベントを追加
    cal.add_component(event)
    
    # ファイルに保存
    with open(f"icals/{event_info['filename']}", "wb") as f:
        f.write(cal.to_ical())
    
    print(f"iCalファイルを生成しました: {event_info['filename']}")

# 全てのイベントのiCalファイルを生成
for event in events:
    create_ical_file(event)

print("全てのiCalファイルの生成が完了しました。")


