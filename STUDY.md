# 1¢ Study

*Updated Tue Sep 29, 11:07 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 100 finished bets | 12% | -$11.88 | -79% | -11.88¢ | -$5.16 / -$6.72 |

*Expect about **44 buys a day**, roughly **$6.64/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 3¢ | 100 | -$12.27 | -82% |
| ESPN-verified leagues only, sell at 10¢ | 100 | -$12.38 | -83% |
| ESPN-verified leagues only, sell at 5¢ | 100 | -$12.40 | -83% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1299 | 100 | 0 (0%) | 1.1% | -$15.00 (-100%) | Sell at 2¢: -$11.88 (-79%) |

*In play right now: 4. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 7 | 1.2% | 0.0% (0) | -23% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 100 | 12% | 7% | 4% | 2% | 0% | 0% |
| Unverified | 1195 | 5% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$15.00 | -100% |
| Sell at 2¢ | 12 | 12% | -$11.88 | -79% |
| Sell at 3¢ | 7 | 7% | -$12.27 | -82% |
| Sell at 5¢ | 4 | 4% | -$12.40 | -83% |
| Sell at 10¢ | 2 | 2% | -$12.38 | -83% |
| Sell at 25¢ | 0 | 0% | -$15.00 | -100% |
| Sell at 50¢ | 0 | 0% | -$15.00 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 522 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 108 | 0 | 10% | 6% | -100% | -82% | 4 min |
| Challenger ATP  | ✘ | 84 | 0 | 10% | 2% | -100% | -83% | 5 min |
| ITF Men's Match | ✘ | 82 | 0 | 10% | 4% | -100% | -83% | 5 min |
| Counter-Strike 2 Game | ✘ | 72 | 1 | 6% | 4% | +30% | -90% | 10 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| League of Legends Game | ✘ | 42 | 0 | 12% | 2% | -100% | -79% | 11 min |
| TT Star Series Match | ✘ | 39 | 1 | 3% | 3% | +139% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 13 min |
| Challenger WTA | ✘ | 13 | 0 | 15% | 8% | -100% | -73% | 8 min |
| International Friendly Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Dota 2 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Liga DIMAYOR Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| R6 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
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
| Women's Pro Basketball Game | ✔ | 4 | 0 | 25% | 25% | -100% | -57% | 22 min |
| Valorant game winner | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 14 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Professional Baseball Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 19 min |
| NHL Game | ✔ | 4 | 0 | 25% | 0% | -100% | -57% | 3 min |
| Women's ODI Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| SHL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
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

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 39 | 5% | 0% | 0% | -91% |
| 5–15 min | 21 | 24% | 5% | 0% | -59% |
| 15–30 min | 17 | 12% | 12% | 0% | -80% |
| 30–60 min | 14 | 21% | 7% | 0% | -63% |
| Over 60 min | 9 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 31 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 05:06 | TT Elite Series Match | Milosz Kukawka | ✘ | — | — | In play | — |
| 09-30 05:04 | TT Elite Series Match | Lukasz Jarocki | ✘ | — | — | In play | — |
| 09-30 04:48 | NHL Game | Edmonton | ✔ | 3:01 - OT · VAN 5 - EDM 5 | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:44 | TT Elite Series Match | Marcin Jadczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:43 | TT Elite Series Match | Milosz Cesarz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:43 | TT Elite Series Match | Karol Sulkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:41 | TT Elite Series Match | Brozek Piotr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:38 | TT Elite Series Match | Jakub Kuzmicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:33 | ITF Men's Match | Sasikumar Mukund | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:26 | TT Elite Series Match | Adrian Wiecek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:22 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:21 | TT Elite Series Match | Blazej Warpas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:17 | Challenger ATP  | Moise Kouame | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:16 | TT Elite Series Match | Adrian Spychala | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:11 | Counter-Strike 2 Game | LAG Gaming | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:10 | TT Elite Series Match | Skorupa Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:08 | TT Elite Series Match | Marcin Jadczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:07 | Challenger ATP  | Masamichi Imamura | ✘ | — | 5¢ | ❌ Lost | -$0.15 |
| 09-30 04:05 | TT Elite Series Match | Stapor Rafal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:04 | TT Elite Series Match | Piotr Przewlocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:04 | Challenger WTA | Chenting Zhu | ✘ | — | 4¢ | ❌ Lost | -$0.15 |
| 09-30 04:04 | Challenger ATP  | Alexandre Muller | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:02 | ITF Women's Match | Jizelle Sibai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 04:01 | Challenger WTA | Jia-Jing Lu | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-30 03:58 | League of Legends Game | Hong Kong | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-30 03:54 | TT Elite Series Match | Lukasz Jarocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 03:52 | ITF Women's Match | Chihiro Muramatsu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 03:50 | CONCACAF Nations League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 03:50 | TT Elite Series Match | Marian Brunner | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 03:46 | TT Elite Series Match | Krzysztof Wloczko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
