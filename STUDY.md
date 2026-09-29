# 1¢ Study

*Updated Tue Sep 29, 6:52 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 60 finished bets | 3% | -$6.38 | -71% | -10.63¢ | -$4.50 / -$1.88 |

*Expect about **38 buys a day**, roughly **$5.69/day** at risk; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 60 | -$6.40 | -71% |
| ESPN-verified leagues only, sell at 5¢ | 60 | -$6.40 | -71% |
| ESPN-verified leagues only, sell at 3¢ | 60 | -$7.05 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 802 | 60 | 0 (0%) | 1.1% | -$9.00 (-100%) | Sell at 10¢: -$6.38 (-71%) |

*In play right now: 11. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 60 | 17% | 8% | 7% | 3% | 0% | 0% |
| Unverified | 731 | 4% | 2% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$9.00 | -100% |
| Sell at 2¢ | 10 | 17% | -$6.40 | -71% |
| Sell at 3¢ | 5 | 8% | -$7.05 | -78% |
| Sell at 5¢ | 4 | 7% | -$6.40 | -71% |
| Sell at 10¢ | 2 | 3% | -$6.38 | -71% |
| Sell at 25¢ | 0 | 0% | -$9.00 | -100% |
| Sell at 50¢ | 0 | 0% | -$9.00 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 341 | 0 | 1% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 69 | 0 | 10% | 9% | -100% | -82% | 4 min |
| Challenger ATP  | ✘ | 59 | 0 | 8% | 0% | -100% | -85% | 5 min |
| ITF Men's Match | ✘ | 56 | 0 | 5% | 2% | -100% | -91% | 5 min |
| Counter-Strike 2 Game | ✘ | 43 | 0 | 5% | 2% | -100% | -92% | 11 min |
| TT Star Series Match | ✘ | 29 | 1 | 3% | 3% | +222% | -94% | 4 min |
| League of Legends Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 10 min |
| CONCACAF Nations League Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 25 min |
| UEFA Nations League Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 3 min |
| Men's T20 Cricket Match | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 12 min |
| Challenger WTA | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 8 min |
| ATP Tennis Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| AFCON Game Winner | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 25 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| WTA Tennis Match | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 3 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Dota 2 Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 23 min |
| International Friendly Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 14 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie B Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Valorant game winner | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's ODI Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 20 | 5% | 0% | 0% | -91% |
| 5–15 min | 15 | 27% | 7% | 0% | -54% |
| 15–30 min | 10 | 20% | 20% | 0% | -65% |
| 30–60 min | 9 | 33% | 11% | 0% | -42% |
| Over 60 min | 6 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-29 12:52 | TT Elite Series Match | Felkel Grzegorz | ✘ | — | — | In play | — |
| 09-29 12:51 | TT Elite Series Match | Adrian Spychala | ✘ | — | — | In play | — |
| 09-29 12:47 | ITF Women's Match | Lois Newberry | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:42 | China League 1 Game | Ningbo Professional | ✘ | — | — | In play | — |
| 09-29 12:40 | KBO Game | NC Dinos | ✘ | — | — | In play | — |
| 09-29 12:40 | ITF Men's Match | Filiberto Fumagalli | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:39 | ITF Women's Match | Carson Tanguilig | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:37 | TT Elite Series Match | Frantisek Krcil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:36 | ITF Women's Match | Berta Bonardi | ✘ | — | — | In play | — |
| 09-29 12:36 | TT Elite Series Match | Krystian Kolodziej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:35 | ITF Men's Match | Isaac Nortey | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:34 | ITF Women's Match | Louanne Djafari | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:33 | TT Elite Series Match | Pawel Polok | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:32 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:29 | Challenger ATP  | Max Wiskandt | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:29 | ITF Women's Match | Zi Ying Ruan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:27 | KBO Game | Hanwha Eagles | ✘ | — | — | In play | — |
| 09-29 12:27 | ITF Women's Match | Iulia Maria Buculei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:27 | TT Elite Series Match | Petr David | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:23 | Dota 2 Game | Direborn | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:19 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:15 | ITF Women's Match | Maria Andrienko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:15 | KBO Game | Kiwoom Heroes | ✘ | — | — | In play | — |
| 09-29 12:15 | ITF Men's Match | Aljaz Jeran | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:13 | TT Elite Series Match | Jakub Krawczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:12 | Challenger WTA | Lola Radivojevic | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 12:09 | ITF Men's Match | Ethan Cook | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:09 | Challenger ATP  | Billy Harris | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:09 | TT Elite Series Match | Ptak Wiktor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 12:08 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
