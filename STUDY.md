# 1¢ Study

*Updated Wed Sep 30, 1:09 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 101 finished bets | 12% | -$12.03 | -79% | -11.91¢ | -$5.16 / -$6.87 |

*Expect about **43 buys a day**, roughly **$6.46/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

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
| 1347 | 101 | 0 (0%) | 1.1% | -$15.15 (-100%) | Sell at 2¢: -$12.03 (-79%) |

*In play right now: 6. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Unverified | 1240 | 5% | 3% | 2% | 1% | 0% | 0% |

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
| TT Elite Series Match | ✘ | 549 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 115 | 0 | 11% | 6% | -100% | -80% | 4 min |
| Challenger ATP  | ✘ | 89 | 0 | 11% | 2% | -100% | -81% | 5 min |
| ITF Men's Match | ✘ | 85 | 0 | 9% | 4% | -100% | -84% | 5 min |
| Counter-Strike 2 Game | ✘ | 72 | 1 | 6% | 4% | +30% | -90% | 10 min |
| AFCON Game Winner | ✘ | 43 | 1 | 14% | 5% | +117% | -76% | 10 min |
| League of Legends Game | ✘ | 42 | 0 | 12% | 2% | -100% | -79% | 11 min |
| TT Star Series Match | ✘ | 41 | 1 | 2% | 2% | +128% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 13 min |
| Challenger WTA | ✘ | 13 | 0 | 15% | 8% | -100% | -73% | 8 min |
| Dota 2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 27 min |
| International Friendly Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 9 min |
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
| NHL Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 4 | 0 | 25% | 25% | -100% | -57% | 22 min |
| Valorant game winner | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 14 min |
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
| Our buy vs Kalshi's first 1¢ trade | 31 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 07:08 | TT Elite Series Match | Pawel Adamus | ✘ | — | — | In play | — |
| 09-30 07:06 | WTA Tennis Match | Yexin Ma | ✘ | — | — | In play | — |
| 09-30 07:04 | TT Elite Series Match | Michal Olbrycht | ✘ | — | — | In play | — |
| 09-30 07:02 | Counter-Strike 2 Game | EVO Elite | ✘ | — | — | In play | — |
| 09-30 06:59 | Challenger ATP  | Hanyi Liu | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-30 06:56 | ITF Women's Match | Alana Subasic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:53 | TT Star Series Match | Koszyk Boguslaw | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:50 | TT Elite Series Match | Blazej Warpas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:50 | ITF Men's Match | Shu Muto | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:48 | TT Elite Series Match | Krzysztof Wloczko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:45 | ITF Women's Match | Alina Yuneva | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:45 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:44 | ITF Men's Match | Anthony Susanto | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-30 06:42 | TT Elite Series Match | Adrian Spychala | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:39 | TT Elite Series Match | Rus Maksymilian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:27 | TT Elite Series Match | Milosz Kukawka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:25 | TT Elite Series Match | Petr David | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:21 | TT Elite Series Match | Piotr Przewlocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:17 | TT Elite Series Match | Michal Olbrycht | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:17 | ITF Women's Match | Guyun Yuchi | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-30 06:17 | TT Star Series Match | Alexandrov Teodor | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:16 | TT Elite Series Match | Schaniel Krzysztof | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:12 | Challenger ATP  | Dalibor Svrcina | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-30 06:12 | TT Elite Series Match | Milosz Cesarz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 06:05 | TT Elite Series Match | Adrian Wiecek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 05:57 | TT Elite Series Match | Mariusz Zwolinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 05:54 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 05:54 | ITF Women's Match | Francesca Franchi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 05:51 | TT Elite Series Match | Grzegorz Poliniewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 05:49 | ITF Women's Match | Belle Thompson | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
