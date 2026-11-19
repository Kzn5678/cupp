# cupp

# CUPP — Common User Passwords Profiler (Compatible Rewrite)

A compatible rewrite of the classic CUPP wordlist generator, with bilingual
(Persian / English) interactive prompts, a `cupp.cfg` config file, and
`-i` / `-w` / `-l` / `-a` / `-v` command-line modes.

WARNING: Ethical use only. This tool is intended for authorized security
testing, CTF, and research on accounts you own or have explicit permission
to test. Do not use it against third parties.

---

## Features

- Interactive profile collection (`-i`): first name, surname, nickname,
  birthdate, partner, child, pet, company, car, keywords, special chars,
  random numbers, leet mode.
- Enhance an existing wordlist (`-w`).
- Download a large wordlist from SecLists (`-l`).
- Parse an Alecto DB file (`-a`).
- Bilingual prompts: Persian and English, chosen at startup.
- `cupp.cfg` config file for default leet / special / random settings.
- Per-stage snapshots (`base`, `leet`, `special`, `random_nums`, `common`,
  `komb`) plus a main output file named after the target.

## Requirements

- Python 3.8+
- No third-party packages required (`urllib` is used for `-l`).

## Installation

    git clone https://github.com/<your-username>/cupp.git
    cd cupp
    python3 cupp.py -v

## Usage

    python3 cupp.py                 # interactive mode (default)
    python3 cupp.py -i              # interactive mode (explicit)
    python3 cupp.py -w old.txt      # enhance an existing wordlist
    python3 cupp.py -l              # download a large wordlist from SecLists
    python3 cupp.py -a alecto.txt   # parse an Alecto DB file
    python3 cupp.py -v              # show version

On startup the tool asks for language (1 = Persian, 2 = English), then walks
through the profile questions. Press Enter to skip any field.

## Output

Generated files are written to `cupp_wordlists/`:

- `<target>_base_<timestamp>.txt`
- `<target>_leet_<timestamp>.txt`
- `<target>_special_<timestamp>.txt`
- `<target>_random_nums_<timestamp>.txt`
- `<target>_common_<timestamp>.txt`
- `<target>_komb_<timestamp>.txt`
- `<target>_<timestamp>.txt` (main merged output)

## Configuration

On first run, `cupp.cfg` is created with defaults:

    {
      "leet_mode": false,
      "special_chars": false,
      "random_numbers": false,
      "min_length": 1,
      "max_length": 32
    }

Set any of these to `true` to make the corresponding step run by default.

## Differences from the original CUPP

- Adds bilingual (Persian / English) prompts.
- Adds `cupp.cfg` as JSON instead of the original config format.
- Uses per-stage snapshot files instead of a single output file, plus a
  merged main file.
- `komb()` and symbol concatenation are simplified compared to the original.
- `-l` downloads from SecLists by default (URL can be changed in code).

## License

This rewrite is released under the MIT License. The original CUPP by
Muris Kurgas is licensed under GPL-3.0; see the original repository for
details.

## Disclaimer

The author is not responsible for any misuse or damage caused by this tool.
Use it only on systems and accounts you own or have written permission to test.

---

# CUPP — پروفایل‌ساز رمز عبور کاربران (بازنویسی سازگار)

بازنویسی سازگار ابزار کلاسیک CUPP برای تولید wordlist، با پرسش‌های دوزبانه
(فارسی / انگلیسی)، فایل پیکربندی `cupp.cfg`، و حالت‌های خط فرمان
`-i` / `-w` / `-l` / `-a` / `-v`.

هشدار: فقط استفاده اخلاقی. این ابزار برای تست نفوذ مجاز، CTF و پژوهش روی
حساب‌هایی است که مالک آن‌ها هستید یا اجازه صریح تست دارید. آن را علیه
اشخاص ثالث استفاده نکنید.

---

## امکانات

- جمع‌آوری تعاملی پروفایل (`-i`): نام، نام خانوادگی، نام مستعار، تاریخ تولد،
  همسر، فرزند، حیوان خانگی، شرکت، مدل ماشین، کلمات کلیدی، کاراکتر خاص،
  اعداد تصادفی، حالت Leet.
- تقویت دیکشنری موجود (`-w`).
- دانلود دیکشنری بزرگ از SecLists (`-l`).
- تجزیه فایل Alecto DB (`-a`).
- پرسش‌های دوزبانه: فارسی و انگلیسی، انتخاب در شروع اجرا.
- فایل پیکربندی `cupp.cfg` برای پیش‌فرض‌های Leet / کاراکتر خاص / اعداد تصادفی.
- snapshot مرحله‌ای (`base`، `leet`، `special`، `random_nums`، `common`،
  `komb`) به‌همراه یک فایل خروجی اصلی با نام هدف.

## پیش‌نیازها

- Python 3.8+
- بدون نیاز به پکیج شخص ثالث (`urllib` برای `-l` استفاده می‌شود).

## نصب

    git clone https://github.com/<your-username>/cupp.git
    cd cupp
    python3 cupp.py -v

## استفاده

    python3 cupp.py                 # حالت تعاملی (پیش‌فرض)
    python3 cupp.py -i              # حالت تعاملی (صریح)
    python3 cupp.py -w old.txt      # تقویت دیکشنری موجود
    python3 cupp.py -l              # دانلود دیکشنری بزرگ از SecLists
    python3 cupp.py -a alecto.txt   # تجزیه فایل Alecto DB
    python3 cupp.py -v              # نمایش نسخه

در شروع اجرا، ابزار زبان را می‌پرسد (1 = فارسی، 2 = انگلیسی) و سپس
سوالات پروفایل را می‌پرسد. هر فیلدی را نمی‌دانید با Enter رد کنید.

## خروجی

فایل‌های تولیدشده در `cupp_wordlists/` ذخیره می‌شوند:

- `<target>_base_<timestamp>.txt`
- `<target>_leet_<timestamp>.txt`
- `<target>_special_<timestamp>.txt`
- `<target>_random_nums_<timestamp>.txt`
- `<target>_common_<timestamp>.txt`
- `<target>_komb_<timestamp>.txt`
- `<target>_<timestamp>.txt` (خروجی اصلی ادغام‌شده)

## پیکربندی

در اولین اجرا، `cupp.cfg` با مقادیر پیش‌فرض ساخته می‌شود:

    {
      "leet_mode": false,
      "special_chars": false,
      "random_numbers": false,
      "min_length": 1,
      "max_length": 32
    }

هر کدام را `true` کنی، مرحله مربوطه به‌صورت پیش‌فرض اجرا می‌شود.

## تفاوت‌ها با CUPP اصلی

- پرسش‌های دوزبانه (فارسی / انگلیسی) اضافه شده.
- `cupp.cfg` به‌صورت JSON است، نه فرمت اصلی.
- خروجی به‌صورت فایل‌های مرحله‌ای است، نه یک فایل واحد؛ به‌علاوه یک فایل
  اصلی ادغام‌شده.
- `komb()` و چسباندن نمادها نسبت به نسخه اصلی ساده‌شده است.
- `-l` به‌صورت پیش‌فرض از SecLists دانلود می‌کند (آدرس در کد قابل تغییر است).

## مجوز

این بازنویسی تحت مجوز MIT منتشر می‌شود. CUPP اصلی اثر Muris Kurgas تحت
مجوز GPL-3.0 است؛ برای جزئیات به مخزن اصلی مراجعه کنید.

## سلب مسئولیت

نویسنده هیچ مسئولیتی در قبال سوءاستفاده یا خسارت ناشی از این ابزار ندارد.
آن را فقط روی سیستم‌ها و حساب‌هایی استفاده کنید که مالک آن‌ها هستید یا
اجازه کتبی تست دارید.
