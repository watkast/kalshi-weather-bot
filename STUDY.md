# 1¢ Study

*Updated Sat Oct 3, 9:16 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 347 finished bets | 0% | -$38.05 | -73% | -10.97¢ | -$11.95 / -$26.10 |

*Expect about **57 buys a day**, roughly **$8.52/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 347 | -$38.55 | -74% |
| ESPN-verified leagues only, sell at 5¢ | 347 | -$40.35 | -78% |
| ESPN-verified leagues only, sell at 2¢ | 347 | -$41.39 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3826 | 347 | 1 (0%) | 1.1% | -$38.05 (-73%) | Hold to the end: -$38.05 (-73%) |

*In play right now: 13. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 67 | 2.0% | 0.0% (0) | -157% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 67 | 0 | -100% | -77% | -84% | -74% |
| ESPN win probability ≥ 2% | 10 | 0 | -100% | -83% | -100% | -100% |
| ESPN win probability ≥ 5% | 2 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 10% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 347 | 12% | 7% | 5% | 2% | 1% | 1% |
| Unverified | 3466 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$38.05 | -73% |
| Sell at 2¢ | 41 | 12% | -$41.39 | -80% |
| Sell at 3¢ | 23 | 7% | -$43.08 | -83% |
| Sell at 5¢ | 18 | 5% | -$40.35 | -78% |
| Sell at 10¢ | 8 | 2% | -$41.57 | -80% |
| Sell at 25¢ | 3 | 1% | -$42.12 | -81% |
| Sell at 50¢ | 2 | 1% | -$38.55 | -74% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 250 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 246 | 1 | 3% | 2% | -62% | -94% | 9 min |
| ITF Women's Match | ✘ | 234 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 157 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 88 | 0 | 9% | 5% | -100% | -84% | 9 min |
| College Football Game | partly | 87 | 2 | 14% | 6% | +115% | -76% | 46 min |
| League of Legends Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 11 min |
| CONCACAF Nations League Game | partly | 65 | 1 | 22% | 9% | +44% | -63% | 26 min |
| Women's College Volleyball Match | ✘ | 59 | 0 | 5% | 2% | -100% | -91% | 68 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 31 min |
| Men's T20 Cricket Match | ✘ | 38 | 0 | 18% | 8% | -100% | -68% | 18 min |
| International Friendly Game | partly | 34 | 0 | 3% | 0% | -100% | -95% | 17 min |
| NHL Game | ✔ | 31 | 0 | 13% | 6% | -100% | -78% | 4 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Serie C Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 5 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| KHL Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 5 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| USL Championship Game | partly | 24 | 0 | 17% | 4% | -100% | -71% | 8 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| National League Game | ✘ | 20 | 1 | 5% | 5% | +367% | -91% | 5 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Liga DIMAYOR Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| AHL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 8 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| NWSL Game | ✔ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 111 min |
| Eerste Divisie Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 3 min |
| Liga Expansion Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 17 min |
| Valorant game winner | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Uruguay Primera Division Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 14 min |
| Argentine Nacional B Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 11 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Rugby French 14 Match | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 42 min |
| Argentina Primera Division Game | ✘ | 11 | 0 | 18% | 18% | -100% | -68% | 12 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| LaLiga 2 Game | ✔ | 10 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Overwatch Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan J2 League Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Czech NBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Professional Baseball Game | partly | 8 | 0 | 25% | 12% | -100% | -57% | 7 min |
| Australia NBL Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 8 min |
| Canadian Premier League | ✘ | 7 | 1 | 57% | 57% | +1233% | -1% | 29 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Adriatic ABA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Copa Del Rey Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 69 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Bundesliga Basketball Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 13 min |
| College Hockey Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Russia VTB United Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 5 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
| LKL Lithuania Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| England Women's Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| PREM Rugby Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Spain Liga ACB Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Italy Serie A2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Italy Serie A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Women's T20 Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 52 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 124 | 4% | 1% | 0% | -93% |
| 5–15 min | 59 | 12% | 3% | 0% | -79% |
| 15–30 min | 66 | 27% | 11% | 2% | -53% |
| 30–60 min | 51 | 12% | 6% | 0% | -80% |
| Over 60 min | 47 | 11% | 11% | 0% | -82% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 35 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-04 03:06 | College Football Game | Washington | ✔ | 0:45 - 4th · WASH 21 - USC 25 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | USL Championship Game | Colorado Springs Sw. | ✔ | 90'+8' · OAK 0 - COS 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | USL Championship Game | Oakland Roots SC | ✔ | 90'+8' · OAK 0 - COS 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | Liga Expansion Game | Atletico Morelia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:00 | Challenger ATP  | Yan Lang Chen | ✘ | — | — | In play | — |
| 10-04 03:00 | Liga Expansion Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:59 | College Football Game | Arkansas St. | ✔ | 0:03 - 4th · ARST 20 - UL 20 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:55 | Women's College Volleyball Match | Virginia Tech | ✘ | — | — | In play | — |
| 10-04 02:54 | College Football Game | Idaho St. | ✘ | — | — | In play | — |
| 10-04 02:54 | College Football Game | Utah Tech | ✘ | — | — | In play | — |
| 10-04 02:51 | AHL Game | Texas Stars | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:48 | Liga Expansion Game | Tapatio | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:48 | NWSL Game | Tie | ✔ | 90'+4' · BOS 4 - POR 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:46 | College Hockey Game | Massachusetts | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:44 | NHL Game | Boston | ✔ | 1:42 - 3rd · BOS 1 - MIN 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:43 | College Football Game | South Florida | ✔ | 0:51 - 4th · TEM 17 - USF 13 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:43 | NHL Game | St. Louis | ✔ | 1:58 - 2nd · STL 0 - COL 5 | — | In play | — |
| 10-04 02:42 | ITF Women's Match | Julieta Pareja | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:41 | Women's College Volleyball Match | California State Bakersfield | ✘ | — | — | In play | — |
| 10-04 02:40 | Liga Expansion Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:38 | College Football Game | Colorado | ✔ | 7:10 - 4th · TTU 22 - COLO 7 | 1¢ | ❌ Lost | -$0.15 |
| 10-04 02:36 | NHL Game | Dallas | ✔ | End of 3rd · DAL 1 - NSH 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:36 | NWSL Game | Portland Thorns | ✔ | 81' · BOS 2 - POR 1 | 2¢ | ❌ Lost | -$0.15 |
| 10-04 02:35 | AHL Game | Rockford Icehogs | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:32 | Liga Expansion Game | Oaxaca | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:31 | College Football Game | Army | ✔ | 3:52 - 4th · ARMY 22 - LT 31 | 5¢ | ❌ Lost | -$0.15 |
| 10-04 02:30 | Liga Expansion Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:28 | Liga Expansion Game | Zacatecas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:26 | LNBP Basketball Game | Fuerza Regia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:18 | Liga Expansion Game | Tlaxcala | ✘ | — | 6¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
