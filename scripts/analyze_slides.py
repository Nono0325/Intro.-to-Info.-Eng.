import json
import sys

def show_module(filename, out_txt):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(out_txt, 'w', encoding='utf-8') as out:
        for item in data:
            out.write(f"=== Page {item['page']} ===\n")
            out.write(item['text'] + "\n\n")
    print(f"Wrote {len(data)} pages to {out_txt}")

show_module('extracted_m0.json', 'm0_dump.txt')
show_module('extracted_m1.json', 'm1_dump.txt')
show_module('extracted_m2.json', 'm2_dump.txt')
show_module('extracted_schedule.json', 'schedule_dump.txt')
