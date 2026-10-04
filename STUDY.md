# 1¢ Study

*Updated Sat Oct 3, 10:27 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 358 finished bets | 0% | -$39.70 | -74% | -11.09¢ | -$12.85 / -$26.85 |

*Expect about **58 buys a day**, roughly **$8.64/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 358 | -$40.20 | -75% |
| ESPN-verified leagues only, sell at 5¢ | 358 | -$42.00 | -78% |
| ESPN-verified leagues only, sell at 2¢ | 358 | -$43.04 | -80% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3844 | 358 | 1 (0%) | 1.1% | -$39.70 (-74%) | Hold to the end: -$39.70 (-74%) |

*In play right now: 9. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 70 | 2.1% | 0.0% (0) | -160% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 70 | 0 | -100% | -78% | -85% | -75% |
| ESPN win probability ≥ 2% | 11 | 0 | -100% | -84% | -100% | -100% |
| ESPN win probability ≥ 5% | 3 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 10% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 358 | 11% | 6% | 5% | 2% | 1% | 1% |
| Unverified | 3477 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$39.70 | -74% |
| Sell at 2¢ | 41 | 11% | -$43.04 | -80% |
| Sell at 3¢ | 23 | 6% | -$44.73 | -83% |
| Sell at 5¢ | 18 | 5% | -$42.00 | -78% |
| Sell at 10¢ | 8 | 2% | -$43.22 | -80% |
| Sell at 25¢ | 3 | 1% | -$43.77 | -82% |
| Sell at 50¢ | 2 | 1% | -$40.20 | -75% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 250 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 246 | 1 | 3% | 2% | -62% | -94% | 9 min |
| ITF Women's Match | ✘ | 234 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 160 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| College Football Game | partly | 91 | 2 | 13% | 5% | +105% | -77% | 46 min |
| UEFA Nations League Game | ✔ | 88 | 0 | 9% | 5% | -100% | -84% | 9 min |
| League of Legends Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 11 min |
| CONCACAF Nations League Game | partly | 67 | 1 | 21% | 9% | +39% | -64% | 25 min |
| Women's College Volleyball Match | ✘ | 61 | 0 | 5% | 2% | -100% | -91% | 68 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 31 min |
| Men's T20 Cricket Match | ✘ | 39 | 0 | 18% | 8% | -100% | -69% | 17 min |
| International Friendly Game | partly | 36 | 0 | 3% | 0% | -100% | -95% | 17 min |
| NHL Game | ✔ | 32 | 0 | 12% | 6% | -100% | -78% | 5 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Championship Game | partly | 26 | 0 | 15% | 4% | -100% | -73% | 8 min |
| Serie C Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 5 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| KHL Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 5 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| National League Game | ✘ | 20 | 1 | 5% | 5% | +367% | -91% | 5 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| AHL Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 8 min |
| Liga DIMAYOR Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| ATP Tennis Match | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 2 min |
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
| Professional Baseball Game | partly | 9 | 0 | 22% | 11% | -100% | -61% | 5 min |
| Czech NBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
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
| NBA Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 20 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 126 | 4% | 1% | 0% | -93% |
| 5–15 min | 63 | 11% | 3% | 0% | -81% |
| 15–30 min | 68 | 26% | 10% | 1% | -54% |
| 30–60 min | 53 | 11% | 6% | 0% | -80% |
| Over 60 min | 48 | 10% | 10% | 0% | -82% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 36 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-04 04:27 | USL Championship Game | San Antonio | ✔ | 86' · SAFC 0 - LVL 1 | — | In play | — |
| 10-04 04:26 | AHL Game | Tucson Roadrunners | ✘ | — | — | In play | — |
| 10-04 04:07 | Professional Baseball Game | San Diego | ✔ | Top 9th · SD 2 - MIL 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 04:02 | USL Championship Game | Tie | ✔ | 90'+7' · MTB 2 - OCSC 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:57 | Women's College Volleyball Match | Michigan | ✘ | — | — | In play | — |
| 10-04 03:54 | USL Championship Game | Orange County | ✔ | 90' · MTB 2 - OCSC 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:53 | Challenger ATP  | Naoya Honda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:47 | International Friendly Game | Tie | ✔ | 78' · MEX 0 - USA 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:45 | ATP Tennis Match | Kyrian Jacquet | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:44 | Challenger ATP  | Ajeet Rai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:43 | AHL Game | Bakersfield Condors | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:42 | AHL Game | Ontario Reign | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:42 | CONCACAF Nations League Game | Tie | ✔ | 86' · GUF 1 - BLZ 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:39 | CONCACAF Nations League Game | Belize | ✔ | 84' · GUF 1 - BLZ 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:36 | International Friendly Game | Mexico | ✔ | 67' · MEX 0 - USA 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:36 | College Hockey Game | Alaska Anchorage | ✘ | — | — | In play | — |
| 10-04 03:34 | Men's T20 Cricket Match | Indonesia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:28 | Women's College Volleyball Match | Virginia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:06 | College Football Game | Washington | ✔ | 0:45 - 4th · WASH 21 - USC 25 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | USL Championship Game | Colorado Springs Sw. | ✔ | 90'+8' · OAK 0 - COS 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | USL Championship Game | Oakland Roots SC | ✔ | 90'+8' · OAK 0 - COS 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:02 | Liga Expansion Game | Atletico Morelia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 03:00 | Challenger ATP  | Yan Lang Chen | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 03:00 | Liga Expansion Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:59 | College Football Game | Arkansas St. | ✔ | 0:03 - 4th · ARST 20 - UL 20 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:55 | Women's College Volleyball Match | Virginia Tech | ✘ | — | — | In play | — |
| 10-04 02:54 | College Football Game | Idaho St. | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:54 | College Football Game | Utah Tech | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 02:51 | AHL Game | Texas Stars | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 02:48 | Liga Expansion Game | Tapatio | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
