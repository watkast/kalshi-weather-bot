# 1¢ Study

*Updated Thu Oct 1, 6:22 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 129 finished bets | 1% | -$5.35 | -28% | -4.15¢ | -$9.60 / $4.25 |

*Expect about **36 buys a day**, roughly **$5.43/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 129 | -$12.60 | -65% |
| ESPN-verified leagues only, sell at 2¢ | 129 | -$14.67 | -76% |
| ESPN-verified leagues only, sell at 3¢ | 129 | -$15.06 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 2107 | 129 | 1 (1%) | 1.1% | -$5.35 (-28%) | Hold to the end: -$5.35 (-28%) |

*In play right now: 5. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 9 | 1.1% | 0.0% (0) | -13% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 129 | 14% | 9% | 5% | 2% | 1% | 1% |
| Unverified | 1973 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$5.35 | -28% |
| Sell at 2¢ | 18 | 14% | -$14.67 | -76% |
| Sell at 3¢ | 11 | 9% | -$15.06 | -78% |
| Sell at 5¢ | 6 | 5% | -$15.45 | -80% |
| Sell at 10¢ | 3 | 2% | -$15.42 | -80% |
| Sell at 25¢ | 1 | 1% | -$16.04 | -83% |
| Sell at 50¢ | 1 | 1% | -$12.60 | -65% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 872 | 0 | 1% | 0% | -100% | -99% | 5 min |
| ITF Men's Match | ✘ | 194 | 0 | 9% | 4% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 181 | 0 | 11% | 7% | -100% | -81% | 4 min |
| Challenger ATP  | ✘ | 118 | 0 | 8% | 2% | -100% | -85% | 5 min |
| Counter-Strike 2 Game | ✘ | 103 | 1 | 4% | 3% | -9% | -93% | 10 min |
| TT Star Series Match | ✘ | 78 | 1 | 3% | 3% | +20% | -96% | 4 min |
| League of Legends Game | ✘ | 60 | 0 | 8% | 2% | -100% | -86% | 11 min |
| AFCON Game Winner | ✘ | 45 | 1 | 16% | 4% | +107% | -73% | 12 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Men's T20 Cricket Match | ✘ | 23 | 0 | 17% | 9% | -100% | -70% | 17 min |
| Challenger WTA | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 10 min |
| Dota 2 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 28 min |
| International Friendly Game | partly | 18 | 0 | 0% | 0% | -100% | -100% | 12 min |
| R6 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ATP Tennis Match | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 2 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan NPB Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Champions League Women's Game | partly | 11 | 1 | 27% | 18% | +748% | -53% | 20 min |
| KHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Euroleague Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 45 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| National League Game | ✘ | 9 | 1 | 11% | 11% | +937% | -81% | 4 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| NHL Game | ✔ | 8 | 0 | 25% | 0% | -100% | -57% | 4 min |
| Women's College Volleyball Match | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 30 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Women's Pro Basketball Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 15 min |
| Valorant game winner | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's ODI Cricket Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 61 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Major League Soccer Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| SHL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australia NBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Croatia Premijer Liga Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 98 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 47 | 4% | 0% | 0% | -93% |
| 5–15 min | 26 | 19% | 4% | 0% | -67% |
| 15–30 min | 25 | 28% | 12% | 4% | -51% |
| 30–60 min | 17 | 24% | 12% | 0% | -59% |
| Over 60 min | 14 | 0% | 0% | 0% | -100% |

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
| 10-01 12:19 | TT Elite Series Match | Jakub Nowak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:19 | TT Elite Series Match | Artur Grela | ✘ | — | — | In play | — |
| 10-01 12:17 | ITF Women's Match | Hania Abouelsaad | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:13 | TT Elite Series Match | Vincenec Oliver | ✘ | — | — | In play | — |
| 10-01 12:12 | Challenger ATP  | Dominic Stricker | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:11 | TT Star Series Match | Tymofieiev Oleksandr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:11 | TT Elite Series Match | Dawid Kosmal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:11 | Japan NPB Game | Chiba Lotte Marines | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:09 | TT Elite Series Match | Grzegorz Poliniewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:07 | ITF Women's Match | nour sahnoun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:06 | Challenger ATP  | Laurent Lokoli | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:06 | International Friendly Game | Ecuador | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-01 12:06 | International Friendly Game | Japan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:04 | ITF Women's Match | Zi Ying Ruan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:01 | Challenger ATP  | Laslo Djere | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 12:00 | Counter-Strike 2 Game | B8 | ✘ | — | — | In play | — |
| 10-01 11:59 | ITF Men's Match | Rodrigo Alujas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:57 | ITF Women's Match | Sarina Schnyder | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:54 | TT Elite Series Match | Dawid Michna | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:52 | Counter-Strike 2 Game | Krytiepacani | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:50 | TT Elite Series Match | Rafal Idaczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:48 | Challenger ATP  | Toby Samuel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:47 | Australia NBL Game | Melbourne United | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:45 | ITF Women's Match | Katherine Sebov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:43 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:40 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:39 | TT Elite Series Match | Michal Olbrycht | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:37 | ITF Men's Match | Michiel De Krom | ✘ | — | 5¢ | ❌ Lost | -$0.15 |
| 10-01 11:35 | Counter-Strike 2 Game | Falcons Force | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 11:35 | Valorant game winner | TYLOO | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
