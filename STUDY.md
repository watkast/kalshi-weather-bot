# 1¢ Study

*Updated Fri Oct 2, 9:41 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 224 finished bets | 0% | -$19.60 | -58% | -8.75¢ | -$2.80 / -$16.80 |

*Expect about **43 buys a day**, roughly **$6.52/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 224 | -$26.32 | -78% |
| ESPN-verified leagues only, sell at 5¢ | 224 | -$26.45 | -79% |
| ESPN-verified leagues only, sell at 50¢ | 224 | -$26.85 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3210 | 224 | 1 (0%) | 1.1% | -$19.60 (-58%) | Hold to the end: -$19.60 (-58%) |

*In play right now: 11. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 224 | 12% | 7% | 5% | 2% | 0% | 0% |
| Unverified | 2975 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$19.60 | -58% |
| Sell at 2¢ | 28 | 12% | -$26.32 | -78% |
| Sell at 3¢ | 16 | 7% | -$27.36 | -81% |
| Sell at 5¢ | 11 | 5% | -$26.45 | -79% |
| Sell at 10¢ | 5 | 2% | -$27.05 | -81% |
| Sell at 25¢ | 1 | 0% | -$30.29 | -90% |
| Sell at 50¢ | 1 | 0% | -$26.85 | -80% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1295 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 239 | 0 | 9% | 5% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 227 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 218 | 1 | 3% | 2% | -57% | -94% | 9 min |
| Challenger ATP  | ✘ | 147 | 0 | 8% | 1% | -100% | -86% | 4 min |
| TT Star Series Match | ✘ | 103 | 1 | 3% | 3% | -9% | -95% | 4 min |
| League of Legends Game | ✘ | 78 | 0 | 8% | 3% | -100% | -87% | 12 min |
| UEFA Nations League Game | ✔ | 72 | 0 | 7% | 3% | -100% | -88% | 6 min |
| CONCACAF Nations League Game | partly | 61 | 1 | 21% | 8% | +53% | -63% | 25 min |
| Darts Match | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| Women's College Volleyball Match | ✘ | 37 | 0 | 5% | 0% | -100% | -91% | 28 min |
| Dota 2 Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 28 min |
| Men's T20 Cricket Match | ✘ | 32 | 0 | 19% | 6% | -100% | -68% | 20 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 25 | 0 | 16% | 12% | -100% | -72% | 10 min |
| International Friendly Game | partly | 24 | 0 | 4% | 0% | -100% | -93% | 10 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| KHL Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 5 min |
| NHL Game | ✔ | 19 | 0 | 16% | 5% | -100% | -73% | 5 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Brasileiro Serie B Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| WTA Tennis Match | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 3 min |
| National League Game | ✘ | 15 | 1 | 7% | 7% | +522% | -88% | 5 min |
| Liga DIMAYOR Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 4 min |
| Japan NPB Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 3 min |
| SHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| LNBP Basketball Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 24 min |
| Valorant game winner | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| LNB Elite 2 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Sweden SBL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 31 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| NWSL Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's ODI Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Ettan Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Argentina Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 14 min |
| AHL Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Finland Korisliiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Australia NBL Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 20 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| College Football Game | ✔ | 5 | 0 | 20% | 20% | -100% | -65% | 24 min |
| LaLiga 2 Game | ✔ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Overwatch Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Croatia Premijer Liga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Liga Expansion Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 22 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Adriatic ABA Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eerste Divisie Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | -0 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie A Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Turkey BSL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 382 min |
| LNB Elite Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 102 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 86 | 6% | 1% | 0% | -90% |
| 5–15 min | 43 | 14% | 2% | 0% | -76% |
| 15–30 min | 38 | 26% | 11% | 3% | -54% |
| 30–60 min | 34 | 15% | 9% | 0% | -75% |
| Over 60 min | 23 | 9% | 9% | 0% | -85% |

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
| 10-03 03:39 | TT Elite Series Match | Kowalski Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:39 | TT Elite Series Match | Mikolaj Lukaszewski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:37 | Women's College Volleyball Match | Purdue | ✘ | — | — | In play | — |
| 10-03 03:36 | Women's College Volleyball Match | Washington | ✘ | — | — | In play | — |
| 10-03 03:36 | TT Elite Series Match | Maciej Sinicki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:32 | AHL Game | Abbotsford Canucks | ✘ | — | — | In play | — |
| 10-03 03:31 | Women's College Volleyball Match | UCLA | ✘ | — | — | In play | — |
| 10-03 03:30 | CONCACAF Nations League Game | Tie | ✔ | 73' · JAM 2 - SLV 0 | — | In play | — |
| 10-03 03:28 | Women's College Volleyball Match | Virginia Tech | ✘ | — | — | In play | — |
| 10-03 03:26 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:23 | Liga DIMAYOR Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:21 | TT Elite Series Match | Jakub Michalski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:20 | CONCACAF Nations League Game | El Salvador | ✔ | 63' · JAM 1 - SLV 0 | — | In play | — |
| 10-03 03:20 | Women's Pro Basketball Game | Dallas | ✔ | 6.9 - 4th · DAL 73 - GS 76 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:20 | TT Elite Series Match | Tadeusz Piotrowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:17 | TT Elite Series Match | Jakub Jesiek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:16 | TT Elite Series Match | Linek Adam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:14 | Liga DIMAYOR Game | Alianza FC Valledupar | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-03 03:04 | Women's College Volleyball Match | California Riverside | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 03:00 | Liga Expansion Game | Correcaminos | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:59 | TT Elite Series Match | Roman Wiza | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:58 | NHL Game | Winnipeg | ✔ | 1:39 - OT · BOS 4 - WPG 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:57 | Liga Expansion Game | Cruz Azul Hidalgo | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-03 02:56 | LNBP Basketball Game | Gambusinos De Fresnillo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:52 | TT Elite Series Match | Krzysztof Malcher | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:52 | Women's College Volleyball Match | California State Fullerton | ✘ | — | — | In play | — |
| 10-03 02:51 | AHL Game | Iowa Wild | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:48 | Women's College Volleyball Match | Arizona | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:44 | College Football Game | Virginia Tech | ✔ | 0:03 - 4th · PITT 35 - VT 33 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 02:44 | TT Elite Series Match | Oracz Lukasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
