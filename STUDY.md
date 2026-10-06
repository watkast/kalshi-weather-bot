# 1¢ Study

*Updated Tue Oct 6, 1:51 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 496 finished bets | 1% | -$32.40 | -44% | -6.53¢ | -$23.20 / -$9.20 |

*Expect about **57 buys a day**, roughly **$8.49/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 496 | -$47.40 | -64% |
| ESPN-verified leagues only, sell at 2¢ | 496 | -$56.98 | -77% |
| ESPN-verified leagues only, sell at 5¢ | 496 | -$57.50 | -77% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4721 | 496 | 3 (1%) | 1.1% | -$32.40 (-44%) | Hold to the end: -$32.40 (-44%) |

*In play right now: 18. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 496 | 14% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 4207 | 5% | 4% | 3% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 3 | 1% | -$32.40 | -44% |
| Sell at 2¢ | 67 | 14% | -$56.98 | -77% |
| Sell at 3¢ | 41 | 8% | -$58.41 | -79% |
| Sell at 5¢ | 26 | 5% | -$57.50 | -77% |
| Sell at 10¢ | 12 | 2% | -$58.68 | -79% |
| Sell at 25¢ | 5 | 1% | -$57.85 | -78% |
| Sell at 50¢ | 4 | 1% | -$47.40 | -64% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 336 | 0 | 10% | 4% | -100% | -82% | 4 min |
| ITF Men's Match | ✘ | 303 | 1 | 10% | 6% | -69% | -83% | 5 min |
| Counter-Strike 2 Game | ✘ | 300 | 1 | 4% | 3% | -69% | -94% | 9 min |
| Challenger ATP  | ✘ | 247 | 1 | 9% | 2% | -62% | -85% | 5 min |
| TT Star Series Match | ✘ | 139 | 1 | 3% | 3% | -33% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 122 | 0 | 8% | 4% | -100% | -86% | 6 min |
| League of Legends Game | ✘ | 102 | 0 | 6% | 2% | -100% | -90% | 11 min |
| CONCACAF Nations League Game | partly | 98 | 2 | 19% | 8% | +90% | -66% | 19 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| Darts Match | ✘ | 77 | 0 | 1% | 1% | -100% | -98% | 8 min |
| Men's T20 Cricket Match | ✘ | 56 | 0 | 16% | 7% | -100% | -72% | 19 min |
| International Friendly Game | partly | 53 | 1 | 13% | 6% | +76% | -77% | 17 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Dota 2 Game | ✘ | 52 | 0 | 2% | 2% | -100% | -97% | 29 min |
| Challenger WTA | ✘ | 50 | 0 | 18% | 10% | -100% | -69% | 8 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| NHL Game | ✔ | 43 | 0 | 14% | 5% | -100% | -76% | 4 min |
| R6 Game | ✘ | 37 | 0 | 0% | 0% | -100% | -100% | 9 min |
| KBO Game | ✘ | 33 | 0 | 6% | 6% | -100% | -89% | 8 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| KHL Game | ✘ | 30 | 0 | 3% | 3% | -100% | -94% | 5 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| ATP Tennis Match | ✘ | 29 | 0 | 10% | 3% | -100% | -82% | 3 min |
| Liga DIMAYOR Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| Japan NPB Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Overwatch Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| EuroCup Basketball Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 8 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| NFL Game | ✔ | 16 | 0 | 25% | 6% | -100% | -57% | 3 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| Finland Korisliiga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 9 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Professional Baseball Game | partly | 11 | 0 | 18% | 9% | -100% | -68% | 4 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's Pro Basketball Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 9 min |
| Slovakia SBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
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
| Men's ODI Cricket Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| China League 1 Game | ✘ | 3 | 0 | 33% | 33% | -100% | -42% | 17 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
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
| Under 5 min | 196 | 7% | 1% | 0% | -88% |
| 5–15 min | 94 | 13% | 4% | 1% | -78% |
| 15–30 min | 84 | 29% | 12% | 2% | -50% |
| 30–60 min | 65 | 12% | 6% | 0% | -79% |
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
| 10-06 19:50 | Counter-Strike 2 Game | maybe | ✘ | — | — | In play | — |
| 10-06 19:50 | EFL Trophy Game | Burton | ✘ | — | — | In play | — |
| 10-06 19:50 | EFL Trophy Game | Grimsby | ✘ | — | — | In play | — |
| 10-06 19:49 | Dota 2 Game | MOUZ | ✘ | — | — | In play | — |
| 10-06 19:47 | EFL Trophy Game | Mansfield | ✘ | — | — | In play | — |
| 10-06 19:47 | TT Star Series Match | Keinath Thomas | ✘ | — | — | In play | — |
| 10-06 19:44 | EFL Trophy Game | Rotherham | ✘ | — | — | In play | — |
| 10-06 19:42 | EFL Trophy Game | Shrewsbury | ✘ | — | — | In play | — |
| 10-06 19:42 | ITF Women's Match | Dalayna Hewitt | ✘ | — | — | In play | — |
| 10-06 19:39 | Counter-Strike 2 Game | Legacy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:38 | AFCON Game Winner | Malawi | ✘ | — | — | In play | — |
| 10-06 19:36 | Counter-Strike 2 Game | PENSIONERS | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:34 | EuroCup Basketball Game | KK Bosna Royal Sarajevo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:30 | UEFA Nations League Game | Moldova | ✔ | 45' · SVK 1 - MDA 0 | — | In play | — |
| 10-06 19:29 | UEFA Nations League Game | North Macedonia | ✔ | 43' · MKD 0 - SUI 1 | — | In play | — |
| 10-06 19:29 | EuroCup Basketball Game | JL Bourg Basket | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:29 | UEFA Nations League Game | Tie | ✔ | 43' · CZE 0 - ENG 2 | — | In play | — |
| 10-06 19:27 | TT Star Series Match | Turrini Rafael | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:26 | Counter-Strike 2 Game | WRAITH PCIFIC | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:22 | Counter-Strike 2 Game | PARTIZAN | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:16 | Counter-Strike 2 Game | GamersLab Esports | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:16 | EuroCup Basketball Game | BC Siauliai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:12 | Counter-Strike 2 Game | Inner Circle Prospect | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 19:12 | UEFA Nations League Game | Czechia | ✔ | 27' · CZE 0 - ENG 0 | — | In play | — |
| 10-06 19:01 | EFL Trophy Game | Bristol Rovers | ✘ | — | — | In play | — |
| 10-06 18:58 | League of Legends Game | Frites Esports Club | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 18:58 | UEFA Nations League Game | Tie | ✔ | 12' · SMR 0 - ALB 1 | — | In play | — |
| 10-06 18:53 | R6 Game | Shifters | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 18:53 | KHL Game | SKA St. Petersburg | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 18:52 | International Friendly Game | Jordan | ✔ | 90'+2' · VEN 0 - JOR 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
