# 1¢ Study

*Updated Sat Oct 3, 12:12 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 254 finished bets | 0% | -$24.10 | -63% | -9.49¢ | -$5.05 / -$19.05 |

*Expect about **45 buys a day**, roughly **$6.72/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 254 | -$30.56 | -80% |
| ESPN-verified leagues only, sell at 5¢ | 254 | -$30.95 | -81% |
| ESPN-verified leagues only, sell at 50¢ | 254 | -$31.35 | -82% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3547 | 254 | 1 (0%) | 1.1% | -$24.10 (-63%) | Hold to the end: -$24.10 (-63%) |

*In play right now: 31. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 17 | 1.1% | 0.0% (0) | -11% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17 | 0 | -100% | -80% | -85% | -75% |
| ESPN win probability ≥ 2% | 4 | 0 | -100% | -57% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 254 | 11% | 6% | 4% | 2% | 0% | 0% |
| Unverified | 3262 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$24.10 | -63% |
| Sell at 2¢ | 29 | 11% | -$30.56 | -80% |
| Sell at 3¢ | 16 | 6% | -$31.86 | -84% |
| Sell at 5¢ | 11 | 4% | -$30.95 | -81% |
| Sell at 10¢ | 5 | 2% | -$31.55 | -83% |
| Sell at 25¢ | 1 | 0% | -$34.79 | -91% |
| Sell at 50¢ | 1 | 0% | -$31.35 | -82% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 249 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 239 | 1 | 3% | 3% | -61% | -94% | 9 min |
| ITF Women's Match | ✘ | 233 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 156 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 109 | 1 | 3% | 3% | -14% | -95% | 4 min |
| League of Legends Game | ✘ | 84 | 0 | 7% | 2% | -100% | -88% | 11 min |
| UEFA Nations League Game | ✔ | 82 | 0 | 7% | 2% | -100% | -87% | 8 min |
| CONCACAF Nations League Game | partly | 63 | 1 | 21% | 8% | +48% | -64% | 25 min |
| Darts Match | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| Women's College Volleyball Match | ✘ | 46 | 0 | 4% | 0% | -100% | -92% | 43 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 39 | 0 | 3% | 3% | -100% | -96% | 30 min |
| Men's T20 Cricket Match | ✘ | 37 | 0 | 19% | 8% | -100% | -67% | 19 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| International Friendly Game | partly | 28 | 0 | 4% | 0% | -100% | -94% | 14 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| KHL Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 5 min |
| NHL Game | ✔ | 21 | 0 | 14% | 5% | -100% | -75% | 5 min |
| Brasileiro Serie B Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serie C Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 5 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| National League Game | ✘ | 15 | 1 | 7% | 7% | +522% | -88% | 5 min |
| Liga DIMAYOR Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| SHL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Slovakian 2. Liga Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 109 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Valorant game winner | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Overwatch Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| Japan J2 League Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Rugby French 14 Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 43 min |
| Finland Korisliiga Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Czech NBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Uruguay Primera Division Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 12 min |
| NWSL Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| LaLiga 2 Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 9 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| LNB Elite 2 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AHL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Sweden SBL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 31 min |
| Australia NBL Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 8 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Eerste Divisie Game | ✘ | 6 | 0 | 33% | 33% | -100% | -42% | 8 min |
| Argentina Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 14 min |
| Liga Expansion Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| College Football Game | ✔ | 5 | 0 | 20% | 20% | -100% | -65% | 24 min |
| Adriatic ABA Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 7 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Croatia Premijer Liga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Slovenia 1. SKL Game | ✘ | 3 | 0 | 33% | 33% | -100% | -42% | 15 min |
| Russia VTB United Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 5 min |
| Bundesliga Basketball Game | ✘ | 3 | 0 | 33% | 33% | -100% | -42% | 13 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
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
| LNB Elite Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie A Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 69 min |
| United Rugby Championship Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| England Women's Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Women's T20 Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 52 min |
| PREM Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 13 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 94 | 5% | 1% | 0% | -91% |
| 5–15 min | 49 | 12% | 2% | 0% | -79% |
| 15–30 min | 44 | 25% | 9% | 2% | -57% |
| 30–60 min | 39 | 13% | 8% | 0% | -78% |
| Over 60 min | 28 | 7% | 7% | 0% | -88% |

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
| 10-03 18:07 | Challenger ATP  | Marcelo Tomas Barrios Vera | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 18:07 | Dota 2 Game | OG | ✘ | — | — | In play | — |
| 10-03 18:05 | LNB Elite Game | Boulazac Basket Dordogne | ✘ | — | — | In play | — |
| 10-03 18:03 | LaLiga 2 Game | Tie | ✔ | 72' · LEG 0 - CAD 2 | — | In play | — |
| 10-03 18:01 | Slovakia SBL Game | Nitra Blue Wings | ✘ | — | — | In play | — |
| 10-03 18:01 | Men's T20 Cricket Match | BD CC Lisbon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:59 | LaLiga 2 Game | Leganes | ✔ | 69' · LEG 0 - CAD 2 | — | In play | — |
| 10-03 17:58 | Canadian Premier League | Tie | ✘ | — | — | In play | — |
| 10-03 17:58 | League of Legends Game | LOUD | ✘ | — | — | In play | — |
| 10-03 17:58 | LNB Elite Game | Saint Quentin | ✘ | — | — | In play | — |
| 10-03 17:57 | LNB Elite Game | Elan Bearnais Pau-Lacq-Orthez | ✘ | — | — | In play | — |
| 10-03 17:57 | Slovenia 1. SKL Game | Kk Rogaska | ✘ | — | — | In play | — |
| 10-03 17:56 | Sweden SBL Game | Jamtland Basket | ✘ | — | — | In play | — |
| 10-03 17:56 | LKL Lithuania Game | BC Jonava | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:54 | Copa Del Rey Game | Reg Time: Tie | ✘ | — | — | In play | — |
| 10-03 17:54 | Copa Del Rey Game | Reg Time: CD Ceuta 6 de Junio | ✘ | — | — | In play | — |
| 10-03 17:52 | UEFA Nations League Game | Tie | ✔ | 90'+3' · LUX 0 - EST 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:51 | Women's College Volleyball Match | Arkansas University at Little Rocks | ✘ | — | — | In play | — |
| 10-03 17:50 | Serie A Femminile Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:49 | PREM Rugby Match | Harlequin FC | ✘ | — | — | In play | — |
| 10-03 17:49 | Slovakian 2. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-03 17:49 | Czech NBL Game | BK Gapa Hradec Kralove | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:47 | Slovakian 2. Liga Game | Banik Lehota | ✘ | — | — | In play | — |
| 10-03 17:46 | Canadian Premier League | Cavalry | ✘ | — | — | In play | — |
| 10-03 17:43 | UEFA Nations League Game | Luxembourg | ✔ | 84' · LUX 0 - EST 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:41 | Women's College Volleyball Match | Notre Dame | ✘ | — | — | In play | — |
| 10-03 17:40 | LNB Elite Game | Sluc Nancy Basket | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 17:39 | Copa Del Rey Game | Reg Time: Tedeon | ✘ | — | — | In play | — |
| 10-03 17:39 | Copa Del Rey Game | Reg Time: Tie | ✘ | — | — | In play | — |
| 10-03 17:37 | Serie A Femminile Game | Lazio | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
