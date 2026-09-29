# 1¢ Study

*Updated Tue Sep 29, 2:43 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 77 finished bets | 14% | -$8.69 | -75% | -11.29¢ | -$3.88 / -$4.81 |

*Expect about **43 buys a day**, roughly **$6.52/day** at risk; max loss per buy **15¢**; typical wait to sell **3 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 77 | -$8.93 | -77% |
| ESPN-verified leagues only, sell at 5¢ | 77 | -$8.95 | -77% |
| ESPN-verified leagues only, sell at 3¢ | 77 | -$9.21 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1142 | 77 | 0 (0%) | 1.1% | -$11.55 (-100%) | Sell at 2¢: -$8.69 (-75%) |

*In play right now: 34. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 77 | 14% | 8% | 5% | 3% | 0% | 0% |
| Unverified | 1031 | 5% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$11.55 | -100% |
| Sell at 2¢ | 11 | 14% | -$8.69 | -75% |
| Sell at 3¢ | 6 | 8% | -$9.21 | -80% |
| Sell at 5¢ | 4 | 5% | -$8.95 | -77% |
| Sell at 10¢ | 2 | 3% | -$8.93 | -77% |
| Sell at 25¢ | 0 | 0% | -$11.55 | -100% |
| Sell at 50¢ | 0 | 0% | -$11.55 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 435 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 94 | 0 | 12% | 7% | -100% | -80% | 4 min |
| Challenger ATP  | ✘ | 78 | 0 | 8% | 1% | -100% | -87% | 5 min |
| ITF Men's Match | ✘ | 76 | 0 | 9% | 4% | -100% | -84% | 5 min |
| Counter-Strike 2 Game | ✘ | 66 | 1 | 6% | 5% | +41% | -89% | 10 min |
| League of Legends Game | ✘ | 38 | 0 | 11% | 3% | -100% | -82% | 11 min |
| TT Star Series Match | ✘ | 38 | 1 | 3% | 3% | +146% | -95% | 4 min |
| AFCON Game Winner | ✘ | 33 | 1 | 15% | 6% | +183% | -74% | 14 min |
| UEFA Nations League Game | ✔ | 31 | 0 | 10% | 0% | -100% | -83% | 5 min |
| CONCACAF Nations League Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 25 min |
| Men's T20 Cricket Match | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 13 min |
| English National League Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Challenger WTA | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 8 min |
| Dota 2 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 27 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
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
| Euroleague Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 94 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 204 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 28 | 4% | 0% | 0% | -94% |
| 5–15 min | 17 | 29% | 6% | 0% | -49% |
| 15–30 min | 14 | 14% | 14% | 0% | -75% |
| 30–60 min | 11 | 27% | 9% | 0% | -53% |
| Over 60 min | 7 | 0% | 0% | 0% | -100% |

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
| 09-29 20:43 | ITF Men's Match | Eudald Gonzalez | ✘ | — | — | In play | — |
| 09-29 20:43 | English National League Game | Forest Green | ✘ | — | — | In play | — |
| 09-29 20:43 | English National League Game | Wealdstone | ✘ | — | — | In play | — |
| 09-29 20:42 | TT Elite Series Match | Michal Skorski | ✘ | — | — | In play | — |
| 09-29 20:41 | Professional Baseball Game | Philadelphia | ✔ | Top 9th · PHI 3 - ATL 5 | — | In play | — |
| 09-29 20:41 | ITF Women's Match | Isabella Kruger | ✘ | — | — | In play | — |
| 09-29 20:40 | TT Elite Series Match | Tkocz Marek | ✘ | — | — | In play | — |
| 09-29 20:40 | English National League Game | Aldershot | ✘ | — | — | In play | — |
| 09-29 20:40 | English National League Game | Tie | ✘ | — | — | In play | — |
| 09-29 20:40 | English National League Game | Tie | ✘ | — | — | In play | — |
| 09-29 20:40 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | — | In play | — |
| 09-29 20:39 | ITF Men's Match | Segundo Goity Zapico | ✘ | — | — | In play | — |
| 09-29 20:39 | English National League Game | Tie | ✘ | — | — | In play | — |
| 09-29 20:38 | ITF Women's Match | Isabella Marton | ✘ | — | — | In play | — |
| 09-29 20:38 | English National League Game | Gateshead | ✘ | — | — | In play | — |
| 09-29 20:38 | CONCACAF Nations League Game | Tie | ✘ | — | — | In play | — |
| 09-29 20:37 | English National League Game | Hartlepool | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:37 | English National League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:36 | English National League Game | Worthing | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:36 | English National League Game | Yeovil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:36 | UEFA Nations League Game | Bulgaria | ✔ | 90'+3' · EST 0 - BUL 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:36 | Euroleague Game | Paris Basketball | ✘ | — | — | In play | — |
| 09-29 20:35 | UEFA Nations League Game | Estonia | ✔ | 90'+3' · EST 0 - BUL 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:35 | UEFA Nations League Game | Tie | ✔ | 90'+3' · KAZ 1 - SVK 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:35 | English National League Game | Boston | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:35 | English National League Game | Halifax | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:35 | English National League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:34 | TT Elite Series Match | Kacper Kwiatkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:34 | ITF Women's Match | Anita Sahdiieva | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 20:33 | Men's T20 Cricket Match | Lexus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
