# 1¢ Study

*Updated Tue Oct 6, 3:02 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 514 finished bets | 1% | -$35.10 | -46% | -6.83¢ | -$24.55 / -$10.55 |

*Expect about **58 buys a day**, roughly **$8.66/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 514 | -$43.35 | -56% |
| ESPN-verified leagues only, sell at 25¢ | 514 | -$57.24 | -74% |
| ESPN-verified leagues only, sell at 2¢ | 514 | -$58.90 | -76% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4772 | 514 | 3 (1%) | 1.1% | -$35.10 (-46%) | Hold to the end: -$35.10 (-46%) |

*In play right now: 12. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 514 | 14% | 9% | 5% | 3% | 1% | 1% |
| Unverified | 4246 | 5% | 4% | 3% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 3 | 1% | -$35.10 | -46% |
| Sell at 2¢ | 70 | 14% | -$58.90 | -76% |
| Sell at 3¢ | 44 | 9% | -$59.94 | -78% |
| Sell at 5¢ | 28 | 5% | -$58.90 | -76% |
| Sell at 10¢ | 13 | 3% | -$60.07 | -78% |
| Sell at 25¢ | 6 | 1% | -$57.24 | -74% |
| Sell at 50¢ | 5 | 1% | -$43.35 | -56% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 339 | 0 | 10% | 4% | -100% | -82% | 4 min |
| ITF Men's Match | ✘ | 304 | 1 | 10% | 6% | -69% | -83% | 5 min |
| Counter-Strike 2 Game | ✘ | 302 | 1 | 4% | 3% | -69% | -94% | 9 min |
| Challenger ATP  | ✘ | 248 | 1 | 8% | 2% | -62% | -85% | 5 min |
| TT Star Series Match | ✘ | 140 | 1 | 3% | 3% | -33% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 102 | 0 | 6% | 2% | -100% | -90% | 11 min |
| CONCACAF Nations League Game | partly | 98 | 2 | 19% | 8% | +90% | -66% | 19 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| Darts Match | ✘ | 77 | 0 | 1% | 1% | -100% | -98% | 8 min |
| Men's T20 Cricket Match | ✘ | 57 | 0 | 16% | 7% | -100% | -73% | 19 min |
| Dota 2 Game | ✘ | 53 | 0 | 2% | 2% | -100% | -97% | 28 min |
| International Friendly Game | partly | 53 | 1 | 13% | 6% | +76% | -77% | 17 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Challenger WTA | ✘ | 50 | 0 | 18% | 10% | -100% | -69% | 8 min |
| AFCON Game Winner | ✘ | 48 | 1 | 15% | 4% | +94% | -75% | 13 min |
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
| EFL Trophy Game | ✘ | 25 | 0 | 8% | 8% | -100% | -86% | 46 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| Japan NPB Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| EuroCup Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 10 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Overwatch Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
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
| Under 5 min | 201 | 7% | 1% | 0% | -88% |
| 5–15 min | 98 | 13% | 4% | 1% | -77% |
| 15–30 min | 86 | 28% | 12% | 2% | -52% |
| 30–60 min | 66 | 12% | 6% | 0% | -79% |
| Over 60 min | 62 | 18% | 13% | 0% | -69% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 44 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-06 21:02 | ITF Men's Match | Darwin Andres Macias Elizalde | ✘ | — | — | In play | — |
| 10-06 20:58 | R6 Game | Twisted Minds | ✘ | — | — | In play | — |
| 10-06 20:51 | ITF Women's Match | Chloe Noel | ✘ | — | — | In play | — |
| 10-06 20:49 | CONCACAF Nations League Game | Turks and Caicos Islands | ✔ | 45'+4' · TCA 0 - MSR 1 | — | In play | — |
| 10-06 20:42 | EuroCup Basketball Game | CB 1939 Canarias | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 20:38 | CONCACAF Nations League Game | Tie | ✘ | — | — | In play | — |
| 10-06 20:38 | ITF Men's Match | Bernardo Casares | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:37 | ITF Women's Match | Kylie Collins | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 20:37 | UEFA Nations League Game | Tie | ✔ | 90'+3' · SVN 2 - SCO 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:37 | EFL Trophy Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:36 | UEFA Nations League Game | Tie | ✔ | 90'+4' · ESP 2 - CRO 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:34 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:34 | UEFA Nations League Game | Estonia | ✔ | 90'+2' · ISL 0 - EST 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:34 | UEFA Nations League Game | Iceland | ✔ | 90'+2' · ISL 0 - EST 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:34 | UEFA Nations League Game | Tie | ✔ | 90'+1' · FIN 0 - BLR 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:33 | UEFA Nations League Game | Scotland | ✔ | 89' · SVN 2 - SCO 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:30 | UEFA Nations League Game | Croatia | ✔ | 88' · ESP 1 - CRO 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:30 | UEFA Nations League Game | Finland | ✔ | 88' · FIN 0 - BLR 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:28 | UEFA Nations League Game | Tie | ✔ | 86' · BUL 2 - LUX 0 | 3¢ | ❌ Lost | -$0.15 |
| 10-06 20:19 | CONCACAF Nations League Game | Bahamas | ✘ | — | — | In play | — |
| 10-06 20:15 | UEFA Nations League Game | Tie | ✔ | 73' · MKD 0 - SUI 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:15 | EuroCup Basketball Game | Rigas Zelli | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 20:15 | EFL Trophy Game | Bromley | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:14 | EFL Trophy Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:13 | UEFA Nations League Game | Luxembourg | ✔ | 71' · BUL 2 - LUX 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:12 | Men's T20 Cricket Match | Salwa Boys | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:06 | ITF Women's Match | Ena Koike | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:04 | Counter-Strike 2 Game | aimers | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:03 | UEFA Nations League Game | Tie | ✔ | 60' · SVK 2 - MDA 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 20:00 | Challenger ATP  | Jose Pereira | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
