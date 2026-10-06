# 1¢ Study

*Updated Tue Oct 6, 4:03 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 486 finished bets | 0% | -$44.90 | -62% | -9.24¢ | -$22.45 / -$22.45 |

*Expect about **57 buys a day**, roughly **$8.61/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 486 | -$52.65 | -72% |
| ESPN-verified leagues only, sell at 2¢ | 486 | -$56.00 | -77% |
| ESPN-verified leagues only, sell at 5¢ | 486 | -$57.30 | -79% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4557 | 486 | 2 (0%) | 1.1% | -$44.90 (-62%) | Hold to the end: -$44.90 (-62%) |

*In play right now: 3. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 99 | 2.5% | 0.0% (0) | -207% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 99 | 0 | -100% | -74% | -74% | -78% |
| ESPN win probability ≥ 2% | 19 | 0 | -100% | -64% | -59% | -100% |
| ESPN win probability ≥ 5% | 7 | 0 | -100% | -75% | -63% | -100% |
| ESPN win probability ≥ 10% | 4 | 0 | -100% | -57% | -35% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 486 | 13% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 4068 | 5% | 4% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 2 | 0% | -$44.90 | -62% |
| Sell at 2¢ | 65 | 13% | -$56.00 | -77% |
| Sell at 3¢ | 39 | 8% | -$57.69 | -79% |
| Sell at 5¢ | 24 | 5% | -$57.30 | -79% |
| Sell at 10¢ | 11 | 2% | -$58.49 | -80% |
| Sell at 25¢ | 4 | 1% | -$59.66 | -82% |
| Sell at 50¢ | 3 | 1% | -$52.65 | -72% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 298 | 0 | 10% | 5% | -100% | -82% | 4 min |
| Counter-Strike 2 Game | ✘ | 287 | 1 | 4% | 3% | -67% | -93% | 9 min |
| ITF Men's Match | ✘ | 281 | 1 | 9% | 5% | -67% | -84% | 4 min |
| Challenger ATP  | ✘ | 238 | 1 | 8% | 2% | -61% | -86% | 5 min |
| TT Star Series Match | ✘ | 130 | 1 | 2% | 2% | -28% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 120 | 0 | 8% | 4% | -100% | -86% | 6 min |
| CONCACAF Nations League Game | partly | 98 | 2 | 19% | 8% | +90% | -66% | 19 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| League of Legends Game | ✘ | 96 | 0 | 6% | 2% | -100% | -89% | 12 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| Darts Match | ✘ | 68 | 0 | 1% | 1% | -100% | -97% | 9 min |
| Men's T20 Cricket Match | ✘ | 53 | 0 | 15% | 6% | -100% | -74% | 19 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Challenger WTA | ✘ | 49 | 0 | 18% | 10% | -100% | -68% | 9 min |
| Dota 2 Game | ✘ | 49 | 0 | 2% | 2% | -100% | -96% | 28 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| International Friendly Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 17 min |
| NHL Game | ✔ | 43 | 0 | 14% | 5% | -100% | -76% | 4 min |
| R6 Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| Liga DIMAYOR Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| KBO Game | ✘ | 28 | 0 | 7% | 7% | -100% | -88% | 7 min |
| ATP Tennis Match | ✘ | 27 | 0 | 11% | 4% | -100% | -81% | 3 min |
| KHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 5 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Overwatch Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| NFL Game | ✔ | 16 | 0 | 25% | 6% | -100% | -57% | 3 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Professional Baseball Game | partly | 11 | 0 | 18% | 9% | -100% | -68% | 4 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's Pro Basketball Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 9 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 9 | 1 | 44% | 44% | +937% | -23% | 32 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| APF Division de Honor Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| NBA Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 14 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Men's ODI Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 14 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 191 | 7% | 1% | 0% | -87% |
| 5–15 min | 94 | 13% | 4% | 1% | -78% |
| 15–30 min | 83 | 28% | 11% | 1% | -52% |
| 30–60 min | 61 | 11% | 5% | 0% | -80% |
| Over 60 min | 56 | 16% | 11% | 0% | -72% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 43 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-06 09:56 | ITF Men's Match | Adrian Arcon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:51 | ITF Women's Match | Kei Yau Cheung | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:51 | ITF Women's Match | Serife Pelin Sari | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:51 | ITF Women's Match | Nissa Finnigan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:51 | ITF Women's Match | Warona Mdlulwa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:43 | Darts Match | Steve Lennon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:34 | ATP Tennis Match | Dane Sweeny | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:33 | ITF Men's Match | Filippo Alfano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:31 | Challenger ATP  | Samuele Pieri | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:29 | ITF Men's Match | Louis Herman | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:29 | ITF Women's Match | Anna Lena Ebster | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 09:23 | Darts Match | Andreas Harrysson | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:18 | League of Legends Game | Natus Vincere | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 09:08 | Dota 2 Game | Direborn | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 09:07 | Darts Match | Alex Spellman | ✘ | — | — | In play | — |
| 10-06 08:58 | ITF Women's Match | Valeria Monko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:55 | Darts Match | Niek Tuik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:36 | ITF Men's Match | Nikolai Barsukov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:30 | ITF Men's Match | Reece Falck | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:28 | TT Star Series Match | Goldír Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:27 | ITF Men's Match | Stefan Storch | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 08:23 | Challenger ATP  | Yuta Kikuchi | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-06 08:09 | Challenger ATP  | Enzo Aguiard | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 08:03 | TT Star Series Match | Thamer Ameer | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 07:56 | Men's T20 Cricket Match | Bhutan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 07:55 | Challenger WTA | Yushan Shao | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 07:47 | ITF Men's Match | Zhao Zhao | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 07:40 | TT Star Series Match | Roșca Mihai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 07:36 | ITF Women's Match | Mariya Zharkikh | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 07:31 | ITF Women's Match | Meiling Wang | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
