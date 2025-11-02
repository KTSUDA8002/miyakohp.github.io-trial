#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
イベント追加自動化スクリプト

使用方法:
    python3 add_event.py --date 2025-12-15 --time "18:30-19:30" \
        --title "イベント名" --organizer "主催者名" \
        --format "オンライン" --location "場所" \
        --pdf "pdfs/20251215_event.pdf" --ical "icals/20251215_event.ics"
"""

import json
import argparse
from datetime import datetime
import os

def load_events(json_file='events.json'):
    """既存のイベントデータを読み込む"""
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    else:
        return {"events": [], "last_updated": ""}

def save_events(data, json_file='events.json'):
    """イベントデータを保存"""
    data['last_updated'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_event(event_data, json_file='events.json'):
    """新しいイベントを追加"""
    data = load_events(json_file)
    
    # イベントIDが重複していないか確認
    existing_ids = [event['id'] for event in data['events']]
    if event_data['id'] in existing_ids:
        print(f"⚠️  警告: ID '{event_data['id']}' は既に存在します")
        return False
    
    # イベントを追加
    data['events'].append(event_data)
    
    # 日付順にソート
    data['events'].sort(key=lambda x: x['date'])
    
    # 保存
    save_events(data, json_file)
    
    print(f"✅ イベントを追加しました: {event_data['title']}")
    print(f"📅 日時: {event_data['date']} {event_data['time']}")
    print(f"📝 合計イベント数: {len(data['events'])}件")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='イベントをevents.jsonに追加')
    parser.add_argument('--id', required=True, help='イベントID (例: 20251215_event)')
    parser.add_argument('--date', required=True, help='日付 (YYYY-MM-DD形式)')
    parser.add_argument('--time', required=True, help='時刻 (例: 18:30-19:30)')
    parser.add_argument('--title', required=True, help='イベント名')
    parser.add_argument('--organizer', required=True, help='主催者名')
    parser.add_argument('--format', required=True, help='開催形式 (例: オンライン, 現地のみ)')
    parser.add_argument('--location', default='', help='場所')
    parser.add_argument('--pdf', default='', help='PDFファイルのパス')
    parser.add_argument('--ical', default='', help='iCalファイルのパス')
    parser.add_argument('--note', default='', help='追加メモ')
    
    args = parser.parse_args()
    
    # イベントデータを作成
    event_data = {
        "id": args.id,
        "date": args.date,
        "time": args.time,
        "title": args.title,
        "organizer": args.organizer,
        "format": args.format,
        "location": args.location,
        "pdf": args.pdf,
        "ical": args.ical
    }
    
    if args.note:
        event_data['note'] = args.note
    
    # イベントを追加
    add_event(event_data)

if __name__ == '__main__':
    main()
