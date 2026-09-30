# 1¢ Study

*Updated Tue Sep 29, 6:51 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 87 finished bets | 13% | -$10.19 | -78% | -11.71¢ | -$4.63 / -$5.56 |

*Expect about **43 buys a day**, roughly **$6.48/day** at risk; max loss per buy **15¢**; typical wait to sell **3 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 87 | -$10.43 | -80% |
| ESPN-verified leagues only, sell at 5¢ | 87 | -$10.45 | -80% |
| ESPN-verified leagues only, sell at 3¢ | 87 | -$10.71 | -82% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1227 | 87 | 0 (0%) | 1.1% | -$13.05 (-100%) | Sell at 2¢: -$10.19 (-78%) |

*In play right now: 9. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 3 | 0.9% | 0.0% (0) | +8% | ✅ Better |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 87 | 13% | 7% | 5% | 2% | 0% | 0% |
| Unverified | 1131 | 5% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$13.05 | -100% |
| Sell at 2¢ | 11 | 13% | -$10.19 | -78% |
| Sell at 3¢ | 6 | 7% | -$10.71 | -82% |
| Sell at 5¢ | 4 | 5% | -$10.45 | -80% |
| Sell at 10¢ | 2 | 2% | -$10.43 | -80% |
| Sell at 25¢ | 0 | 0% | -$13.05 | -100% |
| Sell at 50¢ | 0 | 0% | -$13.05 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 478 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 104 | 0 | 11% | 7% | -100% | -82% | 4 min |
| ITF Men's Match | ✘ | 81 | 0 | 10% | 4% | -100% | -83% | 5 min |
| Challenger ATP  | ✘ | 80 | 0 | 9% | 1% | -100% | -85% | 5 min |
| Counter-Strike 2 Game | ✘ | 70 | 1 | 6% | 4% | +33% | -90% | 10 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| League of Legends Game | ✘ | 39 | 0 | 13% | 3% | -100% | -78% | 11 min |
| TT Star Series Match | ✘ | 39 | 1 | 3% | 3% | +139% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 28 | 0 | 21% | 7% | -100% | -63% | 25 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 13 min |
| Challenger WTA | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 8 min |
| Dota 2 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 27 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| R6 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga DIMAYOR Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 12 min |
| International Friendly Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Euroleague Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 68 min |
| WTA Tennis Match | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 3 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| National League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan NPB Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 67 min |
| KHL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 96 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Valorant game winner | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 14 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Women's ODI Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| SHL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Finland Korisliiga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 124 min |
| Liiga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Professional Baseball Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 204 min |
| EuroCup Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 124 min |
| NHL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 2 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 33 | 3% | 0% | 0% | -95% |
| 5–15 min | 17 | 29% | 6% | 0% | -49% |
| 15–30 min | 16 | 12% | 12% | 0% | -78% |
| 30–60 min | 13 | 23% | 8% | 0% | -60% |
| Over 60 min | 8 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 32 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 00:48 | TT Elite Series Match | Mariusz Koczyba | ✘ | — | — | In play | — |
| 09-30 00:47 | TT Elite Series Match | Rudomina Kamil | ✘ | — | — | In play | — |
| 09-30 00:46 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | — | In play | — |
| 09-30 00:45 | CONCACAF Nations League Game | Tie | ✔ | 89' · ARU 1 - AIA 0 | — | In play | — |
| 09-30 00:44 | Women's Pro Basketball Game | Las Vegas | ✔ | 1:17 - 4th · LV 87 - IND 96 | — | In play | — |
| 09-30 00:37 | TT Elite Series Match | Pawel Kurek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 00:33 | CONCACAF Nations League Game | Anguilla | ✔ | 77' · ARU 1 - AIA 0 | — | In play | — |
| 09-30 00:28 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 00:21 | TT Elite Series Match | Pawel Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 00:20 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 00:19 | Professional Baseball Game | Houston | ✔ | Bot 9th · CHW 6 - HOU 3 | 1¢ | ❌ Lost | -$0.15 |
| 09-30 00:14 | ITF Women's Match | Annika Penickova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 00:11 | TT Elite Series Match | Andriej Fomin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:59 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:58 | NHL Game | Carolina | ✔ | 0:17 - OT · FLA 0 - CAR 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:56 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:52 | Brasileiro Serie B Game | Tie | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 23:46 | TT Elite Series Match | Jerzy Michalik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:43 | Counter-Strike 2 Game | MEIA NOITE | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:36 | TT Elite Series Match | Lukasz Pietraszko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:36 | TT Elite Series Match | Jaroslaw Rolak | ✘ | — | — | In play | — |
| 09-29 23:34 | TT Elite Series Match | Mariusz Koczyba | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:34 | ITF Women's Match | Arina Bulatova | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 23:28 | TT Elite Series Match | Oskar Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:20 | ITF Women's Match | Mimi Xu | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 23:18 | ITF Women's Match | Eugenia Zozaya Menendez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:16 | TT Elite Series Match | Marian Brunner | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:12 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:10 | Brasileiro Serie B Game | Ponte Preta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 23:07 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
