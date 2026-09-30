# 1¢ Study

*Updated Wed Sep 30, 8:32 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 101 finished bets | 12% | -$12.03 | -79% | -11.91¢ | -$5.16 / -$6.87 |

*Expect about **38 buys a day**, roughly **$5.71/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 3¢ | 101 | -$12.42 | -82% |
| ESPN-verified leagues only, sell at 10¢ | 101 | -$12.53 | -83% |
| ESPN-verified leagues only, sell at 5¢ | 101 | -$12.55 | -83% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1567 | 101 | 0 (0%) | 1.1% | -$15.15 (-100%) | Sell at 2¢: -$12.03 (-79%) |

*In play right now: 8. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 101 | 12% | 7% | 4% | 2% | 0% | 0% |
| Unverified | 1458 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$15.15 | -100% |
| Sell at 2¢ | 12 | 12% | -$12.03 | -79% |
| Sell at 3¢ | 7 | 7% | -$12.42 | -82% |
| Sell at 5¢ | 4 | 4% | -$12.55 | -83% |
| Sell at 10¢ | 2 | 2% | -$12.53 | -83% |
| Sell at 25¢ | 0 | 0% | -$15.15 | -100% |
| Sell at 50¢ | 0 | 0% | -$15.15 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 638 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 137 | 0 | 11% | 6% | -100% | -81% | 4 min |
| ITF Men's Match | ✘ | 135 | 0 | 10% | 4% | -100% | -83% | 5 min |
| Challenger ATP  | ✘ | 98 | 0 | 10% | 2% | -100% | -82% | 5 min |
| Counter-Strike 2 Game | ✘ | 79 | 1 | 5% | 4% | +18% | -91% | 11 min |
| TT Star Series Match | ✘ | 52 | 1 | 4% | 4% | +79% | -93% | 4 min |
| League of Legends Game | ✘ | 48 | 0 | 10% | 2% | -100% | -82% | 11 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 18 | 0 | 17% | 11% | -100% | -71% | 13 min |
| Challenger WTA | ✘ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| Dota 2 Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 27 min |
| International Friendly Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| R6 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga DIMAYOR Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| KBO Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| Japan NPB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Euroleague Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 68 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| National League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| KHL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Valorant game winner | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| NHL Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 4 | 0 | 25% | 25% | -100% | -57% | 22 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Women's ODI Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Professional Baseball Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 19 min |
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
| Australia NBL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 204 min |
| EuroCup Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 124 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 39 | 5% | 0% | 0% | -91% |
| 5–15 min | 22 | 23% | 5% | 0% | -61% |
| 15–30 min | 17 | 12% | 12% | 0% | -80% |
| 30–60 min | 14 | 21% | 7% | 0% | -63% |
| Over 60 min | 9 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 29 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 14:31 | TT Elite Series Match | Petr David | ✘ | — | — | In play | — |
| 09-30 14:30 | TT Elite Series Match | Brozek Piotr | ✘ | — | — | In play | — |
| 09-30 14:27 | League of Legends Game | PCIFIC | ✘ | — | — | In play | — |
| 09-30 14:26 | League of Legends Game | JSK Esports | ✘ | — | — | In play | — |
| 09-30 14:26 | TT Star Series Match | Yefimov Viktor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:24 | ITF Men's Match | Nazim Makhlouf | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-30 14:21 | League of Legends Game | Lodis | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:21 | TT Elite Series Match | Grzegorz Poliniewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:16 | TT Elite Series Match | Mateusz Sikon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:16 | Dota 2 Game | OG | ✘ | — | — | In play | — |
| 09-30 14:12 | ITF Men's Match | Hugo Pierre | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:07 | ITF Women's Match | Madelief Hageman | ✘ | — | — | In play | — |
| 09-30 14:06 | TT Elite Series Match | Mariusz Zwolinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:05 | TT Elite Series Match | Marcin Jadczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:04 | Dota 2 Game | 1win | ✘ | — | — | In play | — |
| 09-30 14:03 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:03 | ITF Men's Match | Yahor Slizevich | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:02 | ITF Women's Match | Kira Voronina | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 14:01 | ITF Women's Match | Carlotta Moccia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:55 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:54 | TT Star Series Match | Kargarmazraeh Salar | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:53 | TT Elite Series Match | Brozek Piotr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:50 | ITF Women's Match | Eliz Maloney | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:49 | Challenger WTA | Fiona Crawley | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:47 | ITF Men's Match | Drazen Petrovic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:45 | TT Elite Series Match | Buczynski Witold | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:42 | TT Elite Series Match | Lukasz Jarocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:41 | TT Elite Series Match | Jakub Kuzmicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:39 | ITF Women's Match | Elena Milovanovic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 13:35 | ITF Men's Match | Aaron Gabet | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
