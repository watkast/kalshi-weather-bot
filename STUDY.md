# 1¢ Study

*Updated Tue Sep 29, 3:17 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 83 finished bets | 13% | -$9.59 | -77% | -11.55¢ | -$4.33 / -$5.26 |

*Expect about **43 buys a day**, roughly **$6.44/day** at risk; max loss per buy **15¢**; typical wait to sell **3 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 83 | -$9.83 | -79% |
| ESPN-verified leagues only, sell at 5¢ | 83 | -$9.85 | -79% |
| ESPN-verified leagues only, sell at 3¢ | 83 | -$10.11 | -81% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1163 | 83 | 0 (0%) | 1.1% | -$12.45 (-100%) | Sell at 2¢: -$9.59 (-77%) |

*In play right now: 6. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 2 | 0.8% | 0.0% (0) | +17% | ✅ Better |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 83 | 13% | 7% | 5% | 2% | 0% | 0% |
| Unverified | 1074 | 5% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$12.45 | -100% |
| Sell at 2¢ | 11 | 13% | -$9.59 | -77% |
| Sell at 3¢ | 6 | 7% | -$10.11 | -81% |
| Sell at 5¢ | 4 | 5% | -$9.85 | -79% |
| Sell at 10¢ | 2 | 2% | -$9.83 | -79% |
| Sell at 25¢ | 0 | 0% | -$12.45 | -100% |
| Sell at 50¢ | 0 | 0% | -$12.45 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 442 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 98 | 0 | 11% | 7% | -100% | -81% | 4 min |
| Challenger ATP  | ✘ | 79 | 0 | 9% | 1% | -100% | -85% | 5 min |
| ITF Men's Match | ✘ | 79 | 0 | 9% | 4% | -100% | -85% | 5 min |
| Counter-Strike 2 Game | ✘ | 67 | 1 | 6% | 4% | +39% | -90% | 10 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| League of Legends Game | ✘ | 38 | 0 | 11% | 3% | -100% | -82% | 11 min |
| TT Star Series Match | ✘ | 38 | 1 | 3% | 3% | +146% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 24 | 0 | 17% | 8% | -100% | -71% | 25 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 13 min |
| Challenger WTA | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 8 min |
| Dota 2 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 27 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| R6 Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| International Friendly Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Euroleague Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 68 min |
| WTA Tennis Match | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 3 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| National League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Japan NPB Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 67 min |
| KHL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 96 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie B Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 204 min |
| EuroCup Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 124 min |
| Professional Baseball Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 3 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 29 | 3% | 0% | 0% | -94% |
| 5–15 min | 17 | 29% | 6% | 0% | -49% |
| 15–30 min | 16 | 12% | 12% | 0% | -78% |
| 30–60 min | 13 | 23% | 8% | 0% | -60% |
| Over 60 min | 8 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 34 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-29 21:15 | R6 Game | Heretics | ✘ | — | — | In play | — |
| 09-29 21:15 | Counter-Strike 2 Game | Aimhaus | ✘ | — | — | In play | — |
| 09-29 21:11 | League of Legends Game | 9z Globant | ✘ | — | — | In play | — |
| 09-29 21:05 | TT Elite Series Match | Mucha Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 21:01 | ITF Women's Match | Olivia Lincer | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 21:00 | ITF Women's Match | Ekaterina Maklakova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:59 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:59 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:58 | TT Elite Series Match | Oskar Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:58 | TT Elite Series Match | Przemyslaw Blocho | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:58 | CONCACAF Nations League Game | Bahamas | ✘ | — | — | In play | — |
| 09-29 20:58 | AFCON Game Winner | Cameroon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:58 | AFCON Game Winner | Congo Republic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:55 | ITF Men's Match | Adhithya Ganesan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:53 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:53 | AFCON Game Winner | Niger | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:52 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:52 | Counter-Strike 2 Game | HyperSpirit | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:50 | AFCON Game Winner | Somalia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:48 | Challenger ATP  | Duncan Chan | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-29 20:44 | AFCON Game Winner | Liberia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:43 | ITF Men's Match | Eudald Gonzalez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:43 | English National League Game | Forest Green | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:43 | English National League Game | Wealdstone | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:42 | TT Elite Series Match | Michal Skorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:41 | Professional Baseball Game | Philadelphia | ✔ | Top 9th · PHI 3 - ATL 5 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:41 | ITF Women's Match | Isabella Kruger | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:40 | TT Elite Series Match | Tkocz Marek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:40 | English National League Game | Aldershot | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:40 | English National League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
