# 1¢ Study

*Updated Tue Sep 29, 2:23 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 66 finished bets | 3% | -$7.28 | -74% | -11.03¢ | -$4.95 / -$2.33 |

*Expect about **41 buys a day**, roughly **$6.09/day** at risk; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 66 | -$7.30 | -74% |
| ESPN-verified leagues only, sell at 5¢ | 66 | -$7.30 | -74% |
| ESPN-verified leagues only, sell at 3¢ | 66 | -$7.95 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1104 | 66 | 0 (0%) | 1.1% | -$9.90 (-100%) | Sell at 10¢: -$7.28 (-74%) |

*In play right now: 30. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 66 | 15% | 8% | 6% | 3% | 0% | 0% |
| Unverified | 1008 | 5% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$9.90 | -100% |
| Sell at 2¢ | 10 | 15% | -$7.30 | -74% |
| Sell at 3¢ | 5 | 8% | -$7.95 | -80% |
| Sell at 5¢ | 4 | 6% | -$7.30 | -74% |
| Sell at 10¢ | 2 | 3% | -$7.28 | -74% |
| Sell at 25¢ | 0 | 0% | -$9.90 | -100% |
| Sell at 50¢ | 0 | 0% | -$9.90 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 433 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 92 | 0 | 12% | 8% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 77 | 0 | 8% | 1% | -100% | -86% | 5 min |
| ITF Men's Match | ✘ | 75 | 0 | 8% | 4% | -100% | -86% | 5 min |
| Counter-Strike 2 Game | ✘ | 65 | 1 | 6% | 5% | +44% | -89% | 10 min |
| TT Star Series Match | ✘ | 38 | 1 | 3% | 3% | +146% | -95% | 4 min |
| League of Legends Game | ✘ | 36 | 0 | 11% | 3% | -100% | -81% | 11 min |
| AFCON Game Winner | ✘ | 33 | 1 | 15% | 6% | +183% | -74% | 14 min |
| CONCACAF Nations League Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 25 min |
| UEFA Nations League Game | ✔ | 20 | 0 | 10% | 0% | -100% | -83% | 1 min |
| Men's T20 Cricket Match | ✘ | 15 | 0 | 13% | 13% | -100% | -77% | 14 min |
| Challenger WTA | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| Dota 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 27 min |
| R6 Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| International Friendly Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
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
| Women's ODI Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Sweden SBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 31 min |
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
| English National League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 204 min |
| Euroleague Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 94 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 25 | 4% | 0% | 0% | -93% |
| 5–15 min | 15 | 27% | 7% | 0% | -54% |
| 15–30 min | 10 | 20% | 20% | 0% | -65% |
| 30–60 min | 10 | 30% | 10% | 0% | -48% |
| Over 60 min | 6 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 30 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-29 20:23 | English National League Game | Woking | ✘ | — | — | In play | — |
| 09-29 20:23 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | — | In play | — |
| 09-29 20:22 | CONCACAF Nations League Game | Virgin Islands, British | ✘ | — | — | In play | — |
| 09-29 20:21 | ITF Women's Match | Trinetra Vijayakumar | ✘ | — | — | In play | — |
| 09-29 20:19 | UEFA Nations League Game | Tie | ✔ | 74' · SUI 2 - SCO 0 | — | In play | — |
| 09-29 20:19 | TT Elite Series Match | Mariusz Koczyba | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:19 | UEFA Nations League Game | Tie | ✔ | 74' · ISL 3 - LUX 0 | — | In play | — |
| 09-29 20:19 | AFCON Game Winner | Mauritania | ✘ | — | — | In play | — |
| 09-29 20:19 | TT Elite Series Match | Mateusz Sikon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:18 | English National League Game | Scunthorpe | ✘ | — | — | In play | — |
| 09-29 20:18 | UEFA Nations League Game | Tie | ✔ | 73' · CRO 1 - ESP 3 | — | In play | — |
| 09-29 20:14 | UEFA Nations League Game | North Macedonia | ✔ | 71' · MKD 0 - SVN 1 | — | In play | — |
| 09-29 20:13 | UEFA Nations League Game | Tie | ✔ | 69' · ENG 1 - CZE 0 | — | In play | — |
| 09-29 20:09 | TT Elite Series Match | Skorupa Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:07 | UEFA Nations League Game | Croatia | ✔ | 63' · CRO 1 - ESP 2 | — | In play | — |
| 09-29 20:07 | Euroleague Game | KK Crvena zvezda Belgrade | ✘ | — | — | In play | — |
| 09-29 20:07 | National League Game | HC Lugano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:06 | Euroleague Game | Baskonia Vitoria-Gasteiz | ✘ | — | — | In play | — |
| 09-29 20:05 | TT Elite Series Match | Linek Adam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:03 | TT Elite Series Match | Dariusz Szlubowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:02 | National League Game | EHC Biel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:02 | Dota 2 Game | Yakult's Brothers | ✘ | — | — | In play | — |
| 09-29 20:01 | TT Elite Series Match | Jakub Nowak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:01 | National League Game | HC Ambri-Piotta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:01 | R6 Game | Virtus.pro | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:00 | UEFA Nations League Game | Scotland | ✔ | 55' · SUI 1 - SCO 0 | — | In play | — |
| 09-29 20:00 | National League Game | HC Lausanne | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 19:59 | TT Star Series Match | Tormos Kilian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 19:58 | ITF Men's Match | Oscar Jose Gutierrez | ✘ | — | — | In play | — |
| 09-29 19:57 | TT Elite Series Match | Tkocz Marek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
