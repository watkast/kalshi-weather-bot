# 1¢ Study

*Updated Tue Sep 29, 12:02 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 58 finished bets | 3% | -$6.08 | -70% | -10.48¢ | -$4.35 / -$1.73 |

*Expect about **45 buys a day**, roughly **$6.70/day** at risk; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 58 | -$6.10 | -70% |
| ESPN-verified leagues only, sell at 5¢ | 58 | -$6.10 | -70% |
| ESPN-verified leagues only, sell at 3¢ | 58 | -$6.75 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 606 | 58 | 0 (0%) | 1.1% | -$8.70 (-100%) | Sell at 10¢: -$6.08 (-70%) |

*In play right now: 5. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1 | 0.9% | 0.0% (0) | +13% | ✅ Better |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 58 | 17% | 9% | 7% | 3% | 0% | 0% |
| Unverified | 543 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$8.70 | -100% |
| Sell at 2¢ | 10 | 17% | -$6.10 | -70% |
| Sell at 3¢ | 5 | 9% | -$6.75 | -78% |
| Sell at 5¢ | 4 | 7% | -$6.10 | -70% |
| Sell at 10¢ | 2 | 3% | -$6.08 | -70% |
| Sell at 25¢ | 0 | 0% | -$8.70 | -100% |
| Sell at 50¢ | 0 | 0% | -$8.70 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 259 | 0 | 0% | 0% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 42 | 0 | 7% | 0% | -100% | -88% | 5 min |
| ITF Women's Match | ✘ | 42 | 0 | 12% | 10% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 13 min |
| ITF Men's Match | ✘ | 25 | 0 | 8% | 4% | -100% | -86% | 4 min |
| League of Legends Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 10 min |
| CONCACAF Nations League Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 25 min |
| TT Star Series Match | ✘ | 21 | 1 | 5% | 5% | +344% | -92% | 5 min |
| UEFA Nations League Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 3 min |
| Men's T20 Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AFCON Game Winner | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 25 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| ATP Tennis Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| WTA Tennis Match | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie B Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| International Friendly Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 18 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Dota 2 Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Valorant game winner | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |
| Women's ODI Cricket Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 61 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 20 | 5% | 0% | 0% | -91% |
| 5–15 min | 14 | 29% | 7% | 0% | -50% |
| 15–30 min | 9 | 22% | 22% | 0% | -61% |
| 30–60 min | 9 | 33% | 11% | 0% | -42% |
| Over 60 min | 6 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 29 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-29 05:59 | ITF Women's Match | Xiaowei Li | ✘ | — | — | In play | — |
| 09-29 05:59 | ITF Women's Match | Niehua Tian | ✘ | — | — | In play | — |
| 09-29 05:58 | ITF Men's Match | Kazuki Nakajima | ✘ | — | — | In play | — |
| 09-29 05:57 | ITF Women's Match | Xiao Tang | ✘ | — | — | In play | — |
| 09-29 05:54 | TT Elite Series Match | Felkel Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:53 | ITF Men's Match | Thomas Linley | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 05:53 | TT Elite Series Match | Mariusz Baron | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:53 | TT Elite Series Match | Artur Sobel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:51 | TT Elite Series Match | Grzegorz Poliniewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:50 | ITF Women's Match | Ziyan Zhang | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:48 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:40 | ITF Women's Match | I Wen Wan | ✘ | — | 9¢ | ❌ Lost | -$0.15 |
| 09-29 05:39 | ITF Women's Match | Natsuho Arakawa | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 05:37 | TT Elite Series Match | Blazej Warpas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:35 | TT Elite Series Match | Piotr Chodorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:29 | Challenger ATP  | Keisuke Saitoh | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 05:28 | ITF Men's Match | LIANGXUAN LIU | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:26 | TT Elite Series Match | Wojciech Urban | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:25 | TT Elite Series Match | Rafal Gajda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:22 | Challenger ATP  | Aleksandar Vukic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:18 | TT Elite Series Match | Mariusz Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:17 | TT Elite Series Match | Bartosz Czerwinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:16 | TT Elite Series Match | Miroslav Sklensky | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:13 | TT Elite Series Match | Petr David | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:08 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:08 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:02 | ITF Women's Match | Guyu Xu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 05:01 | WTA Tennis Match | Valeria Savinykh | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 04:56 | ITF Men's Match | Yue Xia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 04:54 | Dota 2 Game | Team Kinetix | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
