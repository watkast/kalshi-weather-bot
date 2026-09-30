# 1¢ Study

*Updated Wed Sep 30, 6:28 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 101 finished bets | 12% | -$12.03 | -79% | -11.91¢ | -$5.16 / -$6.87 |

*Expect about **39 buys a day**, roughly **$5.90/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

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
| 1493 | 101 | 0 (0%) | 1.1% | -$15.15 (-100%) | Sell at 2¢: -$12.03 (-79%) |

*In play right now: 7. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Unverified | 1385 | 5% | 3% | 2% | 1% | 1% | 0% |

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
| TT Elite Series Match | ✘ | 615 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 123 | 0 | 11% | 7% | -100% | -80% | 4 min |
| ITF Men's Match | ✘ | 120 | 0 | 9% | 4% | -100% | -84% | 6 min |
| Challenger ATP  | ✘ | 95 | 0 | 11% | 2% | -100% | -82% | 5 min |
| Counter-Strike 2 Game | ✘ | 78 | 1 | 5% | 4% | +20% | -91% | 11 min |
| TT Star Series Match | ✘ | 47 | 1 | 2% | 2% | +99% | -96% | 4 min |
| League of Legends Game | ✘ | 44 | 0 | 11% | 2% | -100% | -80% | 11 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 17 | 0 | 12% | 12% | -100% | -80% | 12 min |
| Challenger WTA | ✘ | 17 | 0 | 18% | 12% | -100% | -69% | 10 min |
| Dota 2 Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 27 min |
| International Friendly Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
| R6 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga DIMAYOR Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| Japan NPB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Euroleague Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 68 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| KBO Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 85 min |
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
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Professional Baseball Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 19 min |
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
| Our buy vs Kalshi's first 1¢ trade | 30 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 12:26 | TT Elite Series Match | Igor Szymanski | ✘ | — | — | In play | — |
| 09-30 12:23 | Challenger ATP  | Dimitar Kuzmanov | ✘ | — | — | In play | — |
| 09-30 12:14 | ITF Men's Match | Saba Purtseladze | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:12 | KBO Game | LG Twins | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:09 | ITF Men's Match | Leonid Sheyngezikht | ✘ | — | — | In play | — |
| 09-30 12:08 | Women's ODI Cricket Match | Zimbabwe | ✘ | — | — | In play | — |
| 09-30 12:08 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:07 | ITF Men's Match | Harrison Satara | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-30 12:07 | Counter-Strike 2 Game | Leo Team | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:06 | TT Elite Series Match | Buczynski Witold | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:06 | ITF Women's Match | Irem Kurt | ✘ | — | 11¢ | ❌ Lost | -$0.15 |
| 09-30 12:04 | League of Legends Game | Galions | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:04 | TT Elite Series Match | Mateusz Rutkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:04 | TT Elite Series Match | Stapor Rafal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 12:00 | KBO Game | Hanwha Eagles | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:58 | Counter-Strike 2 Game | HyperSpirit | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:58 | TT Star Series Match | Kargarmazraeh Salar | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:58 | Valorant game winner | LOUD | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:58 | ITF Men's Match | Nicolas Robert | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:58 | ITF Men's Match | Jan Werblinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:57 | TT Elite Series Match | Artur Grela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:57 | TT Star Series Match | Koblížek Martin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:57 | Dota 2 Game | MOUZ | ✘ | — | — | In play | — |
| 09-30 11:57 | ITF Men's Match | Andrea Colombo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:54 | Challenger ATP  | Niels Visker | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:54 | TT Star Series Match | Alexandrov Teodor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:53 | TT Star Series Match | Liao Cheng-Ting | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:52 | TT Star Series Match | Koblížek Martin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:51 | TT Star Series Match | Alexandrov Teodor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 11:49 | Challenger WTA | Viktoria Hruncakova | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
