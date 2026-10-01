# 1¢ Study

*Updated Wed Sep 30, 7:56 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 119 finished bets | 1% | -$3.85 | -22% | -3.24¢ | -$8.85 / $5.00 |

*Expect about **39 buys a day**, roughly **$5.90/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 119 | -$11.10 | -62% |
| ESPN-verified leagues only, sell at 10¢ | 119 | -$13.92 | -78% |
| ESPN-verified leagues only, sell at 2¢ | 119 | -$13.95 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1882 | 119 | 1 (1%) | 1.1% | -$3.85 (-22%) | Hold to the end: -$3.85 (-22%) |

*In play right now: 8. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 8 | 1.1% | 0.0% (0) | -10% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 119 | 13% | 8% | 5% | 3% | 1% | 1% |
| Unverified | 1755 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$3.85 | -22% |
| Sell at 2¢ | 15 | 13% | -$13.95 | -78% |
| Sell at 3¢ | 10 | 8% | -$13.95 | -78% |
| Sell at 5¢ | 6 | 5% | -$13.95 | -78% |
| Sell at 10¢ | 3 | 3% | -$13.92 | -78% |
| Sell at 25¢ | 1 | 1% | -$14.54 | -81% |
| Sell at 50¢ | 1 | 1% | -$11.10 | -62% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 764 | 0 | 1% | 1% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 162 | 0 | 11% | 6% | -100% | -81% | 5 min |
| ITF Men's Match | ✘ | 161 | 0 | 9% | 4% | -100% | -84% | 6 min |
| Challenger ATP  | ✘ | 107 | 0 | 9% | 2% | -100% | -84% | 5 min |
| Counter-Strike 2 Game | ✘ | 92 | 1 | 4% | 3% | +1% | -92% | 11 min |
| TT Star Series Match | ✘ | 67 | 1 | 3% | 3% | +39% | -95% | 4 min |
| League of Legends Game | ✘ | 58 | 0 | 9% | 2% | -100% | -85% | 11 min |
| AFCON Game Winner | ✘ | 45 | 1 | 16% | 4% | +107% | -73% | 12 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Men's T20 Cricket Match | ✘ | 21 | 0 | 14% | 10% | -100% | -75% | 17 min |
| Challenger WTA | ✘ | 19 | 0 | 16% | 11% | -100% | -73% | 10 min |
| Dota 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 28 min |
| R6 Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 8 min |
| International Friendly Game | ✔ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Champions League Women's Game | partly | 11 | 1 | 27% | 18% | +748% | -53% | 20 min |
| Liga DIMAYOR Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| KHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| Euroleague Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 45 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| National League Game | ✘ | 9 | 1 | 11% | 11% | +937% | -81% | 4 min |
| Japan NPB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Women's College Volleyball Match | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 26 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| USL Championship Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 11 min |
| Women's Pro Basketball Game | ✔ | 5 | 0 | 20% | 20% | -100% | -65% | 16 min |
| Valorant game winner | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| NHL Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Major League Soccer Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Women's ODI Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Professional Baseball Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 19 min |
| SHL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Australia NBL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Croatia Premijer Liga Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 98 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 44 | 5% | 0% | 0% | -92% |
| 5–15 min | 25 | 20% | 4% | 0% | -65% |
| 15–30 min | 22 | 18% | 14% | 5% | -68% |
| 30–60 min | 17 | 24% | 12% | 0% | -59% |
| Over 60 min | 11 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 29 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-01 01:50 | TT Elite Series Match | Lebek Marian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:43 | USL Championship Game | New Mexico United | ✔ | 77' · NMU 0 - TUL 1 | — | In play | — |
| 10-01 01:42 | League of Legends Game | Vietnam | ✘ | — | — | In play | — |
| 10-01 01:35 | TT Elite Series Match | Skorupa Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:34 | Women's College Volleyball Match | Alabama Birmingham | ✘ | — | — | In play | — |
| 10-01 01:31 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:30 | USL Championship Game | Tie | ✔ | 90'+3' · INDY 0 - RHI 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:29 | Counter-Strike 2 Game | METANOIA WOLVES | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:28 | USL Championship Game | Indy Eleven | ✔ | 90'+1' · INDY 0 - RHI 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:25 | Major League Soccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:24 | Major League Soccer Game | New York RB | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:24 | TT Elite Series Match | Jerzy Michalik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:14 | Canadian Premier League | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:11 | TT Elite Series Match | Mucha Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:05 | TT Elite Series Match | Andriej Fomin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 01:04 | TT Elite Series Match | Jozefiak Michal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:59 | Women's Pro Basketball Game | Washington | ✔ | 6:10 - 4th · ATL 78 - WSH 62 | 1¢ | ❌ Lost | -$0.15 |
| 10-01 00:58 | TT Elite Series Match | Przemyslaw Blocho | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:57 | Women's College Volleyball Match | Arkansas Pine Bluff | ✘ | — | — | In play | — |
| 10-01 00:57 | USL Championship Game | Tie | ✔ | 90'+3' · DET 0 - BFKC 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:54 | Canadian Premier League | Cavalry | ✘ | — | 16¢ | ❌ Lost | -$0.15 |
| 10-01 00:53 | NHL Game | Philadelphia | ✔ | 9:37 - 2nd · PIT 5 - PHI 0 | — | In play | — |
| 10-01 00:52 | Uruguay Primera Division Game | Penarol | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:52 | Uruguay Primera Division Game | Montevideo City | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:52 | USL Championship Game | Tie | ✔ | HT · JAX 1 - MIA 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:51 | TT Elite Series Match | Michał Machelski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:47 | TT Elite Series Match | Jakub Lamperski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:44 | USL Championship Game | Brooklyn FC | ✔ | 80' · DET 0 - BFKC 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:43 | TT Elite Series Match | Adrian Burkacki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 00:41 | USL Championship Game | Sporting Jax | ✔ | HT · JAX 1 - MIA 2 | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
