# 1¢ Study

*Updated Sat Oct 3, 2:06 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 269 finished bets | 0% | -$26.35 | -65% | -9.80¢ | -$6.10 / -$20.25 |

*Expect about **47 buys a day**, roughly **$7.04/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 269 | -$32.03 | -79% |
| ESPN-verified leagues only, sell at 10¢ | 269 | -$32.49 | -81% |
| ESPN-verified leagues only, sell at 5¢ | 269 | -$32.55 | -81% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3633 | 269 | 1 (0%) | 1.1% | -$26.35 (-65%) | Hold to the end: -$26.35 (-65%) |

*In play right now: 48. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 30 | 1.0% | 0.0% (0) | +1% | ≈ Same |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30 | 0 | -100% | -71% | -83% | -71% |
| ESPN win probability ≥ 2% | 4 | 0 | -100% | -57% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 269 | 12% | 6% | 4% | 2% | 0% | 0% |
| Unverified | 3316 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$26.35 | -65% |
| Sell at 2¢ | 32 | 12% | -$32.03 | -79% |
| Sell at 3¢ | 17 | 6% | -$33.72 | -84% |
| Sell at 5¢ | 12 | 4% | -$32.55 | -81% |
| Sell at 10¢ | 6 | 2% | -$32.49 | -81% |
| Sell at 25¢ | 1 | 0% | -$37.04 | -92% |
| Sell at 50¢ | 1 | 0% | -$33.60 | -83% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 249 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 243 | 1 | 3% | 2% | -62% | -94% | 9 min |
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
| National League Game | ✘ | 19 | 1 | 5% | 5% | +391% | -91% | 5 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| College Football Game | partly | 19 | 0 | 21% | 11% | -100% | -64% | 34 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serie C Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 5 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| Liga DIMAYOR Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Valorant game winner | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Slovakian 2. Liga Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 109 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Eerste Divisie Game | ✘ | 12 | 0 | 17% | 17% | -100% | -71% | 2 min |
| LaLiga 2 Game | ✔ | 10 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Overwatch Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
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
| Argentina Primera Division Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 20 min |
| AHL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Australia NBL Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 8 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 6 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Professional Baseball Game | partly | 6 | 0 | 17% | 0% | -100% | -71% | 7 min |
| Adriatic ABA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Expansion Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
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
| Spain Liga ACB Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 97 | 5% | 1% | 0% | -91% |
| 5–15 min | 50 | 12% | 2% | 0% | -79% |
| 15–30 min | 48 | 25% | 8% | 2% | -57% |
| 30–60 min | 42 | 14% | 7% | 0% | -75% |
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
| 10-03 20:05 | College Football Game | Buffalo | ✔ | 0:02 - 4th · WMU 20 - BUFF 17 | — | In play | — |
| 10-03 20:05 | UEFA Nations League Game | North Macedonia | ✔ | 61' · SCO 1 - MKD 0 | — | In play | — |
| 10-03 20:05 | Argentine Nacional B Game | Tie | ✘ | — | — | In play | — |
| 10-03 20:04 | College Football Game | UConn | ✔ | OT · SYR 40 - CONN 41 | — | In play | — |
| 10-03 20:03 | National League Game | Fribourg Gottéron | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 20:01 | Italy Serie A Game | Aquila Basket Trento | ✘ | — | — | In play | — |
| 10-03 19:59 | National League Game | EHC Kloten | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:59 | Men's T20 Cricket Match | Reddy's XI | ✘ | — | — | In play | — |
| 10-03 19:59 | Argentine Nacional B Game | Tie | ✘ | — | — | In play | — |
| 10-03 19:59 | Argentine Nacional B Game | Tie | ✘ | — | — | In play | — |
| 10-03 19:58 | Dota 2 Game | Team Yandex | ✘ | — | — | In play | — |
| 10-03 19:58 | Argentine Nacional B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:58 | National League Game | HC Lausanne | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:57 | College Football Game | Mississippi Valley St. | ✘ | — | — | In play | — |
| 10-03 19:57 | Argentine Nacional B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:57 | Serie C Game | Carpi | ✘ | — | — | In play | — |
| 10-03 19:56 | Argentine Nacional B Game | Tristan Suarez | ✘ | — | — | In play | — |
| 10-03 19:56 | Argentine Nacional B Game | Quilmes | ✘ | — | — | In play | — |
| 10-03 19:55 | National League Game | HC Davos | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:55 | Professional Baseball Game | Cleveland | ✔ | Bot 9th · CHW 3 - CLE 0 | 1¢ | ❌ Lost | -$0.15 |
| 10-03 19:54 | Italy Serie A2 Game | Basket Mestre 1958 | ✘ | — | — | In play | — |
| 10-03 19:54 | LNB Elite 2 Game | Rouen Metropole Basket | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:54 | Argentine Nacional B Game | Jujuy | ✘ | — | — | In play | — |
| 10-03 19:54 | Uruguay Primera Division Game | Tie | ✘ | — | — | In play | — |
| 10-03 19:53 | Eerste Divisie Game | FC Eindhoven | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:53 | Eerste Divisie Game | De Graafschap | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:53 | Eerste Divisie Game | Waalwijk | ✘ | — | — | In play | — |
| 10-03 19:53 | LNB Elite 2 Game | Poitiers Basket 86 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 19:53 | Argentine Nacional B Game | Estudiantes | ✘ | — | — | In play | — |
| 10-03 19:53 | Eerste Divisie Game | Emmen | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
