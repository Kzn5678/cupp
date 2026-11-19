#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CUPP - Common User Passwords Profiler (compatible rewrite, i18n)
"""

import os
import sys
import json
import random
import string
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

VERSION = "3.0-cupp"
CONFIG_FILE = "cupp.cfg"

DEFAULT_CONFIG = {
    "leet_mode": False,
    "special_chars": False,
    "random_numbers": False,
    "min_length": 1,
    "max_length": 32,
}

TEXTS = {
    "fa": {
        "banner": """
╔══════════════════════════════════════════════════════╗
║  CUPP - پروفایل‌ساز رمز عبور کاربران                  ║
║  نسخه بازنویسی سازگار                                 ║
╚══════════════════════════════════════════════════════╝
        """,
        "choose_lang": "زبان را انتخاب کنید / Choose language:",
        "lang_fa": "1. فارسی",
        "lang_en": "2. English",
        "lang_prompt": "عدد 1 یا 2 را وارد کنید: ",
        "profile_header": "جمع‌آوری پروفایل هدف (اگر چیزی را نمی‌دانید Enter بزنید):",
        "first_name": "نام: ",
        "surname": "نام خانوادگی: ",
        "nickname": "نام مستعار: ",
        "birthdate": "تاریخ تولد (DDMMYYYY): ",
        "partner_name": "نام همسر/شریک: ",
        "partner_nickname": "نام مستعار همسر/شریک: ",
        "partner_birthdate": "تاریخ تولد همسر/شریک (DDMMYYYY): ",
        "child_name": "نام فرزند: ",
        "child_nickname": "نام مستعار فرزند: ",
        "child_birthdate": "تاریخ تولد فرزند (DDMMYYYY): ",
        "pet": "نام حیوان خانگی: ",
        "company": "نام شرکت: ",
        "car": "مدل ماشین: ",
        "add_keywords": "آیا کلمات کلیدی درباره هدف اضافه شود؟ (y/n): ",
        "keywords_prompt": "کلمات را با کاما جدا کنید (مثلاً football,coding,bmw): ",
        "add_special": "آیا کاراکترهای خاص به انتهای کلمات اضافه شود؟ (y/n): ",
        "add_random_nums": "آیا اعداد تصادفی به انتهای کلمات اضافه شود؟ (y/n): ",
        "leet_mode": "حالت Leet فعال شود؟ (مثلاً leet = 1337) (y/n): ",
        "generating": "در حال ساخت دیکشنری...",
        "snapshot": "  [مرحله] {}: {:,} کلمه",
        "saved": "  ذخیره شد {}: {:,} کلمه، {:.2f} MB",
        "done": "تمام شد. مسیر خروجی: ",
        "another": "هدف بعدی؟ (y/n): ",
        "invalid_date": "تاریخ باید ۸ رقم باشد، رد شد.",
        "version": "نسخه CUPP",
        "enhance_header": "تقویت دیکشنری موجود: ",
        "enhance_done": "دیکشنری تقویت‌شده ذخیره شد.",
        "download_start": "در حال دانلود دیکشنری بزرگ از مخزن...",
        "download_done": "دانلود کامل شد: ",
        "download_fail": "دانلود ناموفق بود: ",
        "alecto_start": "در حال تجزیه Alecto DB...",
        "alecto_done": "تجزیه Alecto کامل شد: ",
        "alecto_fail": "فایل Alecto یافت نشد یا قابل خواندن نبود: ",
        "config_loaded": "پیکربندی بارگذاری شد: ",
        "config_created": "پیکربندی پیش‌فرض ساخته شد: ",
        "main_output": "فایل اصلی خروجی: ",
    },
    "en": {
        "banner": """
╔══════════════════════════════════════════════════════╗
║  CUPP - Common User Passwords Profiler               ║
║  compatible rewrite                                  ║
╚══════════════════════════════════════════════════════╝
        """,
        "choose_lang": "Choose language:",
        "lang_fa": "1. فارسی",
        "lang_en": "2. English",
        "lang_prompt": "Enter 1 or 2: ",
        "profile_header": "Profile collection (press Enter to skip):",
        "first_name": "First Name: ",
        "surname": "Surname: ",
        "nickname": "Nickname: ",
        "birthdate": "Birthdate (DDMMYYYY): ",
        "partner_name": "Partner's name: ",
        "partner_nickname": "Partner's nickname: ",
        "partner_birthdate": "Partner's birthdate (DDMMYYYY): ",
        "child_name": "Child's name: ",
        "child_nickname": "Child's nickname: ",
        "child_birthdate": "Child's birthdate (DDMMYYYY): ",
        "pet": "Pet's name: ",
        "company": "Company name: ",
        "car": "Car model: ",
        "add_keywords": "Do you want to add some key words about the victim? (y/n): ",
        "keywords_prompt": "Enter words, comma separated [i.e. hacker,juice]: ",
        "add_special": "Do you want to add special chars at the end of words? (y/n): ",
        "add_random_nums": "Do you want to add some random numbers at the end of words? (y/n): ",
        "leet_mode": "Leet mode? (i.e. leet = 1337) (y/n): ",
        "generating": "Now making a dictionary...",
        "snapshot": "  [snapshot] {}: {:,}",
        "saved": "  saved {}: {:,} words, {:.2f} MB",
        "done": "Done. Output: ",
        "another": "Another target? (y/n): ",
        "invalid_date": "Date must be 8 digits, skipped.",
        "version": "CUPP version",
        "enhance_header": "Enhancing existing wordlist: ",
        "enhance_done": "Enhanced wordlist saved.",
        "download_start": "Downloading large wordlist from repo...",
        "download_done": "Download complete: ",
        "download_fail": "Download failed: ",
        "alecto_start": "Parsing Alecto DB...",
        "alecto_done": "Alecto parsing complete: ",
        "alecto_fail": "Alecto file not found or unreadable: ",
        "config_loaded": "Config loaded: ",
        "config_created": "Default config created: ",
        "main_output": "Main output file: ",
    }
}

class CUPP:
    def __init__(self, output_dir="cupp_wordlists", lang="fa", config=None):
        self.profile = {}
        self.wordlist = []
        self.snapshots = {}
        self.output_dir = output_dir
        self.lang = lang
        self.t = TEXTS[lang]
        self.config = config or DEFAULT_CONFIG.copy()
        Path(self.output_dir).mkdir(exist_ok=True)

    def ask(self, key):
        return input(self.t[key]).strip()

    def ask_yes_no(self, key):
        return input(self.t[key]).strip().lower() == 'y'

    def valid_date(self, s):
        if not s:
            return ""
        if len(s) == 8 and s.isdigit():
            return s
        print(self.t["invalid_date"])
        return ""

    def get_profile(self):
        print(self.t["profile_header"])
        print("-" * 50)
        self.profile = {
            'first_name': self.ask("first_name"),
            'surname': self.ask("surname"),
            'nickname': self.ask("nickname"),
            'birthdate': self.valid_date(self.ask("birthdate")),
            'partner_name': self.ask("partner_name"),
            'partner_nickname': self.ask("partner_nickname"),
            'partner_birthdate': self.valid_date(self.ask("partner_birthdate")),
            'child_name': self.ask("child_name"),
            'child_nickname': self.ask("child_nickname"),
            'child_birthdate': self.valid_date(self.ask("child_birthdate")),
            'pet': self.ask("pet"),
            'company': self.ask("company"),
            'car': self.ask("car"),
            'keywords': [],
            'add_special': False,
            'add_random': False,
            'leet': False,
        }
        if self.ask_yes_no("add_keywords"):
            raw = input(self.t["keywords_prompt"]).strip()
            self.profile['keywords'] = [w.strip() for w in raw.split(',') if w.strip()]
        self.profile['add_special'] = self.ask_yes_no("add_special") or self.config.get("special_chars", False)
        self.profile['add_random'] = self.ask_yes_no("add_random_nums") or self.config.get("random_numbers", False)
        self.profile['leet'] = self.ask_yes_no("leet_mode") or self.config.get("leet_mode", False)

    def snapshot(self, name):
        self.wordlist = list(dict.fromkeys(self.wordlist))
        self.snapshots[name] = list(self.wordlist)
        print(self.t["snapshot"].format(name, len(self.snapshots[name])))

    def _date_parts(self, date):
        if not date:
            return []
        dd, mm, yyyy = date[:2], date[2:4], date[4:]
        return [date, yyyy, mm + dd, dd + mm, yyyy[-2:], dd + mm + yyyy[-2:]]

    def generate_base(self):
        names = []
        for k in ('first_name', 'surname', 'nickname', 'partner_name',
                  'partner_nickname', 'child_name', 'child_nickname', 'pet',
                  'company', 'car'):
            v = self.profile.get(k, "")
            if v:
                names.append(v)
        for name in names:
            self.wordlist.extend([
                name, name.title(), name.upper(), name.lower(),
                name[::-1], name.capitalize(),
            ])
        for dk in ('birthdate', 'partner_birthdate', 'child_birthdate'):
            self.wordlist.extend(self._date_parts(self.profile.get(dk, "")))
        fn, sn = self.profile.get('first_name', ''), self.profile.get('surname', '')
        if fn and sn:
            self.wordlist.extend([fn + sn, sn + fn, fn[0] + sn, fn + sn[0]])
        for kw in self.profile.get('keywords', []):
            self.wordlist.append(kw)
            self.wordlist.append(kw.lower())
            self.wordlist.append(kw.upper())
        self.snapshot('base')

    def leet_variations(self):
        if not self.profile.get('leet'):
            return
        leet_map = {'a': ['4', '@'], 'e': ['3'], 'i': ['1', '!'],
                    'o': ['0'], 's': ['5', '$'], 't': ['7']}
        extra = []
        for word in self.wordlist:
            for ch, subs in leet_map.items():
                if ch in word.lower():
                    for sub in subs:
                        new = word.lower().replace(ch, sub)
                        extra.append(new)
                        extra.append(new.upper())
        self.wordlist.extend(extra)
        self.snapshot('leet')

    def add_special(self):
        if not self.profile.get('add_special'):
            return
        chars = list("!@#$%^&*?~")
        extra = []
        for word in self.wordlist:
            for c in chars:
                extra.append(word + c)
        self.wordlist.extend(extra)
        self.snapshot('special')

    def add_random_nums(self):
        if not self.profile.get('add_random'):
            return
        extra = []
        for word in self.wordlist:
            for n in ('0', '1', '12', '123', '1234', '12345', '2024', '2025', '2026'):
                extra.append(word + n)
                extra.append(n + word)
        self.wordlist.extend(extra)
        self.snapshot('random_nums')

    def add_common(self):
        common = ["123", "1234", "12345", "123456", "qwerty", "asdf",
                  "admin", "pass", "password", "root", "toor", "letmein",
                  "welcome", "monkey", "dragon", "iloveyou", "master", "sunshine"]
        self.wordlist.extend(common)
        self.snapshot('common')

    def komb(self):
        words = [w for w in self.wordlist if 3 <= len(w) <= 12][:30]
        extra = []
        for i, a in enumerate(words):
            for b in words[i+1:]:
                extra.append(a + b)
                extra.append(b + a)
                extra.append(a[:4] + b)
                extra.append(b[:4] + a)
        self.wordlist.extend(extra)
        self.snapshot('komb')

    def save(self, name):
        words = self.snapshots.get(name, [])
        safe = (self.profile.get('first_name') or 'target').replace(' ', '_')
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = Path(self.output_dir) / f"{safe}_{name}_{ts}.txt"
        with open(path, 'w', encoding='utf-8') as f:
            for w in words:
                if w and w.isprintable():
                    f.write(w + '\n')
        size = path.stat().st_size / (1024 * 1024)
        print(self.t["saved"].format(path.name, len(words), size))
        return path

    def save_main(self):
        safe = (self.profile.get('first_name') or 'target').replace(' ', '_')
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = Path(self.output_dir) / f"{safe}_{ts}.txt"
        words = list(dict.fromkeys(self.wordlist))
        with open(path, 'w', encoding='utf-8') as f:
            for w in words:
                if w and w.isprintable():
                    f.write(w + '\n')
        print(self.t["main_output"] + str(path))
        return path

    def run_interactive(self):
        print(self.t["banner"])
        while True:
            self.profile = {}
            self.wordlist = []
            self.snapshots = {}
            self.get_profile()
            print(self.t["generating"])
            self.generate_base()
            self.leet_variations()
            self.add_special()
            self.add_random_nums()
            self.add_common()
            self.komb()
            for stage in ('base', 'leet', 'special', 'random_nums', 'common', 'komb'):
                if stage in self.snapshots:
                    self.save(stage)
            self.save_main()
            if input(self.t["another"]).strip().lower() != 'y':
                break
        print(self.t["done"] + self.output_dir)

    def enhance_wordlist(self, path):
        print(self.t["banner"])
        print(self.t["enhance_header"] + path)
        with open(path, encoding='utf-8', errors='ignore') as f:
            self.wordlist = [l.strip() for l in f if l.strip()]
        self.snapshot('base')
        self.leet_variations()
        self.add_special()
        self.add_random_nums()
        self.add_common()
        self.komb()
        self.save('enhanced')
        self.save_main()
        print(self.t["enhance_done"])

    def download_wordlist(self, url=None):
        print(self.t["download_start"])
        target = Path(self.output_dir) / "big_wordlist.txt"
        url = url or "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"
        try:
            import urllib.request
            urllib.request.urlretrieve(url, target)
            print(self.t["download_done"] + str(target))
        except Exception as e:
            print(self.t["download_fail"] + str(e))

    def parse_alecto(self, path):
        print(self.t["alecto_start"])
        if not Path(path).exists():
            print(self.t["alecto_fail"] + path)
            return
        try:
            with open(path, encoding='utf-8', errors='ignore') as f:
                raw = f.read()
            words = [w.strip() for w in raw.replace('\t', '\n').replace(',', '\n').splitlines() if w.strip()]
            self.wordlist.extend(words)
            self.snapshot('alecto')
            self.save('alecto')
            print(self.t["alecto_done"] + str(len(words)))
        except Exception as e:
            print(self.t["alecto_fail"] + str(e))


def load_config():
    if Path(CONFIG_FILE).exists():
        try:
            with open(CONFIG_FILE, encoding='utf-8') as f:
                cfg = json.load(f)
            merged = DEFAULT_CONFIG.copy()
            merged.update(cfg)
            print(TEXTS["en"]["config_loaded"] + CONFIG_FILE)
            return merged
        except Exception:
            pass
    with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
        json.dump(DEFAULT_CONFIG, f, indent=2)
    print(TEXTS["en"]["config_created"] + CONFIG_FILE)
    return DEFAULT_CONFIG.copy()


def choose_language():
    print(TEXTS["fa"]["choose_lang"])
    print(TEXTS["fa"]["lang_fa"])
    print(TEXTS["fa"]["lang_en"])
    c = input(TEXTS["fa"]["lang_prompt"]).strip()
    return "fa" if c == "1" else "en"


def main():
    parser = argparse.ArgumentParser(description="CUPP - Common User Passwords Profiler")
    parser.add_argument("-i", "--interactive", action="store_true", help="interactive profile mode (default)")
    parser.add_argument("-w", "--wordlist", help="enhance existing wordlist")
    parser.add_argument("-l", "--download", action="store_true", help="download large wordlist")
    parser.add_argument("-a", "--alecto", help="parse Alecto DB file")
    parser.add_argument("-o", "--output", default="cupp_wordlists", help="output directory")
    parser.add_argument("-v", "--version", action="store_true", help="show version")
    args = parser.parse_args()

    if args.version:
        print(f"{TEXTS['fa']['version']} {VERSION}")
        return

    config = load_config()
    lang = choose_language()
    cupp = CUPP(output_dir=args.output, lang=lang, config=config)

    if args.download:
        cupp.download_wordlist()
    elif args.alecto:
        cupp.parse_alecto(args.alecto)
    elif args.wordlist:
        cupp.enhance_wordlist(args.wordlist)
    else:
        cupp.run_interactive()

if __name__ == "__main__":
    main()
