# 1¢ Study

*Updated Sat Oct 3, 1:36 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 263 finished bets | 0% | -$25.45 | -65% | -9.68¢ | -$5.65 / -$19.80 |

*Expect about **46 buys a day**, roughly **$6.93/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 263 | -$31.59 | -80% |
| ESPN-verified leagues only, sell at 2¢ | 263 | -$31.65 | -80% |
| ESPN-verified leagues only, sell at 5¢ | 263 | -$31.65 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3589 | 263 | 1 (0%) | 1.1% | -$25.45 (-65%) | Hold to the end: -$25.45 (-65%) |

*In play right now: 32. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 24 | 1.0% | 0.0% (0) | -3% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24 | 0 | -100% | -78% | -78% | -64% |
| ESPN win probability ≥ 2% | 4 | 0 | -100% | -57% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 263 | 11% | 6% | 5% | 2% | 0% | 0% |
| Unverified | 3294 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$25.45 | -65% |
| Sell at 2¢ | 30 | 11% | -$31.65 | -80% |
| Sell at 3¢ | 17 | 6% | -$32.82 | -83% |
| Sell at 5¢ | 12 | 5% | -$31.65 | -80% |
| Sell at 10¢ | 6 | 2% | -$31.59 | -80% |
| Sell at 25¢ | 1 | 0% | -$36.14 | -92% |
| Sell at 50¢ | 1 | 0% | -$32.70 | -83% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 249 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 241 | 1 | 3% | 2% | -61% | -94% | 9 min |
| ITF Women's Match | ✘ | 233 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 157 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| League of Legends Game | ✘ | 85 | 0 | 7% | 2% | -100% | -88% | 11 min |
| UEFA Nations League Game | ✔ | 82 | 0 | 7% | 2% | -100% | -87% | 8 min |
| CONCACAF Nations League Game | partly | 63 | 1 | 21% | 8% | +48% | -64% | 25 min |
| Darts Match | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 11 min |
| Women's College Volleyball Match | ✘ | 47 | 0 | 4% | 0% | -100% | -93% | 46 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 40 | 0 | 2% | 2% | -100% | -96% | 30 min |
| Men's T20 Cricket Match | ✘ | 37 | 0 | 19% | 8% | -100% | -67% | 19 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| International Friendly Game | partly | 28 | 0 | 4% | 0% | -100% | -94% | 14 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| KHL Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 5 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NHL Game | ✔ | 21 | 0 | 14% | 5% | -100% | -75% | 5 min |
| Brasileiro Serie B Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serie C Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 5 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| National League Game | ✘ | 15 | 1 | 7% | 7% | +522% | -88% | 5 min |
| Liga DIMAYOR Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| College Football Game | partly | 13 | 0 | 15% | 15% | -100% | -73% | 34 min |
| Valorant game winner | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Slovakian 2. Liga Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 109 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| LaLiga 2 Game | ✔ | 10 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Overwatch Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| Japan J2 League Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Rugby French 14 Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 43 min |
| Finland Korisliiga Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Czech NBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Uruguay Primera Division Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 12 min |
| NWSL Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Slovakia SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 18 min |
| LNB Elite 2 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AHL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Australia NBL Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 8 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Adriatic ABA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eerste Divisie Game | ✘ | 6 | 0 | 33% | 33% | -100% | -42% | 8 min |
| Argentina Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 14 min |
| Liga Expansion Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| LNB Elite Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 16 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Bundesliga Basketball Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 10 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Copa Del Rey Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 43 min |
| Russia VTB United Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 5 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
| United Rugby Championship Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| LKL Lithuania Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie A Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 69 min |
| England Women's Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| PREM Rugby Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 27 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Women's T20 Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 52 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 96 | 5% | 1% | 0% | -91% |
| 5–15 min | 50 | 12% | 2% | 0% | -79% |
| 15–30 min | 46 | 24% | 9% | 2% | -59% |
| 30–60 min | 39 | 13% | 8% | 0% | -78% |
| Over 60 min | 32 | 9% | 9% | 0% | -84% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 32 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-03 19:30 | Uruguay Primera Division Game | Defensor | ✘ | — | — | In play | — |
| 10-03 19:27 | Counter-Strike 2 Game | BetBoom Team | ✘ | — | — | In play | — |
| 10-03 19:27 | College Football Game | West Virginia | ✔ | 0:29 - 4th · WVU 42 - ISU 45 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:26 | Spain Liga ACB Game | CB Malaga | ✘ | — | — | In play | — |
| 10-03 19:22 | UEFA Nations League Game | Tie | ✔ | 35' · CZE 0 - ESP 1 | — | In play | — |
| 10-03 19:20 | College Football Game | Michigan | ✔ | 0:37 - 4th · MICH 14 - MINN 20 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:17 | College Football Game | Georgetown | ✘ | — | — | In play | — |
| 10-03 19:17 | College Football Game | UCF | ✔ | 2:30 - 4th · UCF 17 - HOU 24 | — | In play | — |
| 10-03 19:13 | Counter-Strike 2 Game | Lavked | ✘ | — | — | In play | — |
| 10-03 19:12 | College Football Game | Merrimack | ✘ | — | — | In play | — |
| 10-03 19:12 | Challenger ATP  | Mitchell Krueger | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:10 | College Football Game | Navy | ✔ | 1:47 - 4th · NAVY 9 - AFA 14 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:08 | College Football Game | Vanderbilt | ✔ | 1:07 - 3rd · VAN 14 - UGA 28 | — | In play | — |
| 10-03 19:04 | Argentina Primera Division Game | Tie | ✘ | — | — | In play | — |
| 10-03 19:03 | College Football Game | St. Thomas | ✘ | — | — | In play | — |
| 10-03 19:02 | TT Star Series Match | Lorenzo Santiago | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:02 | Adriatic ABA Game | Spartak Subotica | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:02 | College Football Game | Boston College | ✔ | 6:26 - 4th · BC 10 - SMU 19 | — | In play | — |
| 10-03 18:56 | College Football Game | Michigan St. | ✔ | 1:10 - 3rd · MSU 3 - WIS 24 | — | In play | — |
| 10-03 18:55 | England Super League Rugby Match | Warrington Wolves | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:53 | College Football Game | Brown | ✘ | — | — | In play | — |
| 10-03 18:53 | UEFA Nations League Game | Czechia | ✔ | 6' · CZE 0 - ESP 0 | — | In play | — |
| 10-03 18:52 | International Friendly Game | Peru | ✔ | 35' · PER 0 - CAN 1 | — | In play | — |
| 10-03 18:52 | KHL Game | HC Sochi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:43 | Counter-Strike 2 Game | fnatic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:41 | Croatia Premijer Liga Game | KK Dubrovnik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:41 | College Football Game | VMI | ✘ | — | — | In play | — |
| 10-03 18:38 | College Football Game | Mississippi St. | ✔ | 4:00 - 3rd · ALA 42 - MSST 17 | — | In play | — |
| 10-03 18:34 | Slovakia SBL Game | Kosice Wolves | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:33 | Slovenia 1. SKL Game | Šentjur | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
