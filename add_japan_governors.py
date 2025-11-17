#!/usr/bin/env python3
import json

# Read the existing seed data
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'r') as f:
    data = json.load(f)

# Japanese Prefecture Governors (as of 2025)
# Prefecture numbering follows the official JIS X 0401 standard
japanese_governors = [
    {"personId": "person:jp:01:governor:suzuki", "name": "Naomichi Suzuki", "title": "Governor of Hokkaido", "regionId": "pref:jp:01", "partyName": "Independent", "startDate": "2019-04-23", "endDate": None},
    {"personId": "person:jp:02:governor:miyashita", "name": "Sōichirō Miyashita", "title": "Governor of Aomori", "regionId": "pref:jp:02", "partyName": "Independent", "startDate": "2023-06-29", "endDate": None},
    {"personId": "person:jp:03:governor:tasso", "name": "Takuya Tasso", "title": "Governor of Iwate", "regionId": "pref:jp:03", "partyName": "Independent", "startDate": "2007-04-30", "endDate": None},
    {"personId": "person:jp:04:governor:murai", "name": "Yoshihiro Murai", "title": "Governor of Miyagi", "regionId": "pref:jp:04", "partyName": "Independent", "startDate": "2005-11-21", "endDate": None},
    {"personId": "person:jp:05:governor:suzuki", "name": "Kenta Suzuki", "title": "Governor of Akita", "regionId": "pref:jp:05", "partyName": "Independent", "startDate": "2025-04-20", "endDate": None},
    {"personId": "person:jp:06:governor:yoshimura", "name": "Mieko Yoshimura", "title": "Governor of Yamagata", "regionId": "pref:jp:06", "partyName": "Independent", "startDate": "2009-02-14", "endDate": None},
    {"personId": "person:jp:07:governor:uchibori", "name": "Masao Uchibori", "title": "Governor of Fukushima", "regionId": "pref:jp:07", "partyName": "Independent", "startDate": "2014-11-12", "endDate": None},
    {"personId": "person:jp:08:governor:oigawa", "name": "Kazuhiko Ōigawa", "title": "Governor of Ibaraki", "regionId": "pref:jp:08", "partyName": "Independent", "startDate": "2017-09-26", "endDate": None},
    {"personId": "person:jp:09:governor:fukuda", "name": "Tomikazu Fukuda", "title": "Governor of Tochigi", "regionId": "pref:jp:09", "partyName": "Independent", "startDate": "2004-12-09", "endDate": None},
    {"personId": "person:jp:10:governor:yamamoto", "name": "Ichita Yamamoto", "title": "Governor of Gunma", "regionId": "pref:jp:10", "partyName": "Independent", "startDate": "2019-07-28", "endDate": None},
    {"personId": "person:jp:11:governor:ono", "name": "Motohiro Ōno", "title": "Governor of Saitama", "regionId": "pref:jp:11", "partyName": "Independent", "startDate": "2019-08-31", "endDate": None},
    {"personId": "person:jp:12:governor:kumagai", "name": "Toshihito Kumagai", "title": "Governor of Chiba", "regionId": "pref:jp:12", "partyName": "Independent", "startDate": "2021-04-05", "endDate": None},
    {"personId": "person:jp:13:governor:koike", "name": "Yuriko Koike", "title": "Governor of Tokyo", "regionId": "pref:jp:13", "partyName": "Independent", "startDate": "2016-08-02", "endDate": None},
    {"personId": "person:jp:14:governor:kuroiwa", "name": "Yūji Kuroiwa", "title": "Governor of Kanagawa", "regionId": "pref:jp:14", "partyName": "Independent", "startDate": "2011-04-23", "endDate": None},
    {"personId": "person:jp:15:governor:hanazumi", "name": "Hideyo Hanazumi", "title": "Governor of Niigata", "regionId": "pref:jp:15", "partyName": "Independent", "startDate": "2018-06-10", "endDate": None},
    {"personId": "person:jp:16:governor:nitta", "name": "Hachiro Nitta", "title": "Governor of Toyama", "regionId": "pref:jp:16", "partyName": "Independent", "startDate": "2020-11-09", "endDate": None},
    {"personId": "person:jp:17:governor:hase", "name": "Hiroshi Hase", "title": "Governor of Ishikawa", "regionId": "pref:jp:17", "partyName": "Independent", "startDate": "2022-03-27", "endDate": None},
    {"personId": "person:jp:18:governor:sugimoto", "name": "Tatsuji Sugimoto", "title": "Governor of Fukui", "regionId": "pref:jp:18", "partyName": "Independent", "startDate": "2019-04-23", "endDate": None},
    {"personId": "person:jp:19:governor:nagasaki", "name": "Kotaro Nagasaki", "title": "Governor of Yamanashi", "regionId": "pref:jp:19", "partyName": "Independent", "startDate": "2019-02-17", "endDate": None},
    {"personId": "person:jp:20:governor:abe", "name": "Shuichi Abe", "title": "Governor of Nagano", "regionId": "pref:jp:20", "partyName": "Independent", "startDate": "2010-09-01", "endDate": None},
    {"personId": "person:jp:21:governor:esaki", "name": "Yoshihide Esaki", "title": "Governor of Gifu", "regionId": "pref:jp:21", "partyName": "Independent", "startDate": "2025-02-06", "endDate": None},
    {"personId": "person:jp:22:governor:suzuki", "name": "Yasutomo Suzuki", "title": "Governor of Shizuoka", "regionId": "pref:jp:22", "partyName": "Independent", "startDate": "2024-05-26", "endDate": None},
    {"personId": "person:jp:23:governor:omura", "name": "Hideaki Omura", "title": "Governor of Aichi", "regionId": "pref:jp:23", "partyName": "Independent", "startDate": "2011-02-15", "endDate": None},
    {"personId": "person:jp:24:governor:ichimi", "name": "Katsuyuki Ichimi", "title": "Governor of Mie", "regionId": "pref:jp:24", "partyName": "Independent", "startDate": "2021-09-14", "endDate": None},
    {"personId": "person:jp:25:governor:mikazuki", "name": "Taizō Mikazuki", "title": "Governor of Shiga", "regionId": "pref:jp:25", "partyName": "Independent", "startDate": "2014-07-20", "endDate": None},
    {"personId": "person:jp:26:governor:nishiwaki", "name": "Takatoshi Nishiwaki", "title": "Governor of Kyoto", "regionId": "pref:jp:26", "partyName": "Independent", "startDate": "2018-04-16", "endDate": None},
    {"personId": "person:jp:27:governor:yoshimura", "name": "Hirofumi Yoshimura", "title": "Governor of Osaka", "regionId": "pref:jp:27", "partyName": "Osaka Restoration Association", "startDate": "2019-04-04", "endDate": None},
    {"personId": "person:jp:28:governor:saito", "name": "Motohiko Saitō", "title": "Governor of Hyogo", "regionId": "pref:jp:28", "partyName": "Independent", "startDate": "2021-08-01", "endDate": None},
    {"personId": "person:jp:29:governor:yamashita", "name": "Makoto Yamashita", "title": "Governor of Nara", "regionId": "pref:jp:29", "partyName": "Independent", "startDate": "2023-05-02", "endDate": None},
    {"personId": "person:jp:30:governor:miyazaki", "name": "Izumi Miyazaki", "title": "Governor of Wakayama", "regionId": "pref:jp:30", "partyName": "Independent", "startDate": "2025-06-03", "endDate": None},
    {"personId": "person:jp:31:governor:hirai", "name": "Shinji Hirai", "title": "Governor of Tottori", "regionId": "pref:jp:31", "partyName": "Independent", "startDate": "2007-04-13", "endDate": None},
    {"personId": "person:jp:32:governor:maruyama", "name": "Tatsuya Maruyama", "title": "Governor of Shimane", "regionId": "pref:jp:32", "partyName": "Independent", "startDate": "2019-04-30", "endDate": None},
    {"personId": "person:jp:33:governor:ibaragi", "name": "Ryūta Ibaragi", "title": "Governor of Okayama", "regionId": "pref:jp:33", "partyName": "Independent", "startDate": "2012-11-12", "endDate": None},
    {"personId": "person:jp:34:governor:yuzaki", "name": "Hidehiko Yuzaki", "title": "Governor of Hiroshima", "regionId": "pref:jp:34", "partyName": "Independent", "startDate": "2009-11-29", "endDate": None},
    {"personId": "person:jp:35:governor:muraoka", "name": "Tsugumasa Muraoka", "title": "Governor of Yamaguchi", "regionId": "pref:jp:35", "partyName": "Independent", "startDate": "2014-02-25", "endDate": None},
    {"personId": "person:jp:36:governor:gotoda", "name": "Masazumi Gotoda", "title": "Governor of Tokushima", "regionId": "pref:jp:36", "partyName": "Independent", "startDate": "2023-05-18", "endDate": None},
    {"personId": "person:jp:37:governor:ikeda", "name": "Toyohito Ikeda", "title": "Governor of Kagawa", "regionId": "pref:jp:37", "partyName": "Independent", "startDate": "2022-09-05", "endDate": None},
    {"personId": "person:jp:38:governor:nakamura", "name": "Tokihiro Nakamura", "title": "Governor of Ehime", "regionId": "pref:jp:38", "partyName": "Independent", "startDate": "2010-12-01", "endDate": None},
    {"personId": "person:jp:39:governor:hamada", "name": "Seiji Hamada", "title": "Governor of Kōchi", "regionId": "pref:jp:39", "partyName": "Independent", "startDate": "2019-12-07", "endDate": None},
    {"personId": "person:jp:40:governor:hattori", "name": "Seitaro Hattori", "title": "Governor of Fukuoka", "regionId": "pref:jp:40", "partyName": "Independent", "startDate": "2021-04-14", "endDate": None},
    {"personId": "person:jp:41:governor:yamaguchi", "name": "Yoshinori Yamaguchi", "title": "Governor of Saga", "regionId": "pref:jp:41", "partyName": "Independent", "startDate": "2015-01-14", "endDate": None},
    {"personId": "person:jp:42:governor:oishi", "name": "Kengo Oishi", "title": "Governor of Nagasaki", "regionId": "pref:jp:42", "partyName": "Independent", "startDate": "2022-03-02", "endDate": None},
    {"personId": "person:jp:43:governor:kimura", "name": "Takashi Kimura", "title": "Governor of Kumamoto", "regionId": "pref:jp:43", "partyName": "Independent", "startDate": "2024-04-16", "endDate": None},
    {"personId": "person:jp:44:governor:sato", "name": "Kiichiro Satō", "title": "Governor of Ōita", "regionId": "pref:jp:44", "partyName": "Independent", "startDate": "2023-04-28", "endDate": None},
    {"personId": "person:jp:45:governor:kono", "name": "Shunji Kōno", "title": "Governor of Miyazaki", "regionId": "pref:jp:45", "partyName": "Independent", "startDate": "2011-01-21", "endDate": None},
    {"personId": "person:jp:46:governor:shiota", "name": "Kōichi Shiota", "title": "Governor of Kagoshima", "regionId": "pref:jp:46", "partyName": "Independent", "startDate": "2020-07-28", "endDate": None},
    {"personId": "person:jp:47:governor:tamaki", "name": "Denny Tamaki", "title": "Governor of Okinawa", "regionId": "pref:jp:47", "partyName": "Independent", "startDate": "2018-10-04", "endDate": None}
]

# Add all governors
data['officeholders'].extend(japanese_governors)

print(f"✅ Added {len(japanese_governors)} Japanese prefecture governors")
print(f"Total officeholders: {len(data['officeholders'])}")

# Write back to file
with open('/Users/ubongjosiah/gpt_iphone/GPT/Resources/seed_data.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
