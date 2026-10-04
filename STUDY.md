# 1¢ Study

*Updated Sat Oct 3, 7:55 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 323 finished bets | 0% | -$34.45 | -71% | -10.67¢ | -$10.15 / -$24.30 |

*Expect about **54 buys a day**, roughly **$8.15/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 5¢ | 323 | -$38.70 | -80% |
| ESPN-verified leagues only, sell at 2¢ | 323 | -$39.09 | -81% |
| ESPN-verified leagues only, sell at 10¢ | 323 | -$39.28 | -81% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3787 | 323 | 1 (0%) | 1.1% | -$34.45 (-71%) | Hold to the end: -$34.45 (-71%) |

*In play right now: 24. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 55 | 2.1% | 0.0% (0) | -170% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 55 | 0 | -100% | -78% | -86% | -76% |
| ESPN win probability ≥ 2% | 8 | 0 | -100% | -78% | -100% | -100% |
| ESPN win probability ≥ 5% | 1 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 323 | 11% | 6% | 5% | 2% | 1% | 0% |
| Unverified | 3440 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$34.45 | -71% |
| Sell at 2¢ | 36 | 11% | -$39.09 | -81% |
| Sell at 3¢ | 20 | 6% | -$40.65 | -84% |
| Sell at 5¢ | 15 | 5% | -$38.70 | -80% |
| Sell at 10¢ | 7 | 2% | -$39.28 | -81% |
| Sell at 25¢ | 2 | 1% | -$41.83 | -86% |
| Sell at 50¢ | 1 | 0% | -$41.70 | -86% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 250 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 246 | 1 | 3% | 2% | -62% | -94% | 9 min |
| ITF Women's Match | ✘ | 233 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 157 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 88 | 0 | 9% | 5% | -100% | -84% | 9 min |
| League of Legends Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 11 min |
| College Football Game | partly | 68 | 2 | 12% | 6% | +175% | -80% | 50 min |
| CONCACAF Nations League Game | partly | 65 | 1 | 22% | 9% | +44% | -63% | 26 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| Women's College Volleyball Match | ✘ | 54 | 0 | 6% | 2% | -100% | -90% | 63 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 31 min |
| Men's T20 Cricket Match | ✘ | 38 | 0 | 18% | 8% | -100% | -68% | 18 min |
| International Friendly Game | partly | 32 | 0 | 3% | 0% | -100% | -95% | 14 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| NHL Game | ✔ | 27 | 0 | 11% | 4% | -100% | -81% | 4 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Serie C Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 5 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| KHL Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 5 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| National League Game | ✘ | 20 | 1 | 5% | 5% | +367% | -91% | 5 min |
| USL Championship Game | partly | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Liga DIMAYOR Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LNBP Basketball Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| AHL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 8 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 111 min |
| Eerste Divisie Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 3 min |
| Valorant game winner | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Uruguay Primera Division Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 14 min |
| Argentine Nacional B Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 11 min |
| NWSL Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
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
| Liga Expansion Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Copa Del Rey Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 69 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Bundesliga Basketball Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 13 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| College Hockey Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Russia VTB United Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 5 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
| CFL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 35 min |
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
| Under 5 min | 115 | 4% | 1% | 0% | -92% |
| 5–15 min | 57 | 11% | 2% | 0% | -82% |
| 15–30 min | 59 | 24% | 8% | 2% | -59% |
| 30–60 min | 51 | 12% | 6% | 0% | -80% |
| Over 60 min | 41 | 12% | 12% | 0% | -79% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 35 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-04 01:51 | CFL Game | Winnipeg Blue Bombers | ✘ | — | — | In play | — |
| 10-04 01:51 | College Football Game | TCU | ✔ | 2:06 - 4th · BYU 16 - TCU 7 | — | In play | — |
| 10-04 01:50 | NHL Game | Toronto | ✔ | End of 3rd · OTT 3 - TOR 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:50 | College Football Game | Nicholls St. | ✘ | — | — | In play | — |
| 10-04 01:46 | NHL Game | Philadelphia | ✔ | 2:20 - OT · CAR 2 - PHI 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:46 | AHL Game | Lehigh Valley Phantoms | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:45 | USL Championship Game | Sacramento Republic | ✔ | 79' · SAC 0 - TUL 1 | — | In play | — |
| 10-04 01:42 | NHL Game | Seattle | ✔ | 1:40 - 3rd · SEA 1 - EDM 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:40 | NHL Game | Washington | ✔ | 2:11 - 3rd · WSH 1 - TB 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:39 | College Football Game | Illinois St. | ✘ | — | — | In play | — |
| 10-04 01:38 | USL Championship Game | Tie | ✔ | 90'+11' · MIA 2 - TBR 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:37 | NHL Game | Chicago | ✔ | 0:17 - 3rd · CHI 3 - BUF 4 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:35 | Women's College Volleyball Match | California Riverside | ✘ | — | — | In play | — |
| 10-04 01:35 | College Football Game | Southern University | ✘ | — | — | In play | — |
| 10-04 01:34 | NHL Game | Columbus | ✔ | 5:47 - 3rd · UTA 4 - CBJ 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:31 | Women's College Volleyball Match | Iowa | ✘ | — | — | In play | — |
| 10-04 01:24 | USL Championship Game | Tampa Bay | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 01:19 | College Football Game | Charleston Southern | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:18 | NBA Game | Toronto | ✔ | 7:12 - 4th · MIA 110 - TOR 87 | — | In play | — |
| 10-04 01:17 | College Football Game | North Carolina A&T | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:08 | Professional Baseball Game | New York Y | ✔ | Top 9th · NYY 0 - TB 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:03 | Women's College Volleyball Match | Kansas State | ✘ | — | — | In play | — |
| 10-04 01:03 | College Football Game | Louisiana-Monroe | ✔ | 11:42 - 3rd · ULM 14 - USA 38 | — | In play | — |
| 10-04 01:02 | USL Championship Game | Tie | ✔ | 90'+6' · BRM 0 - DET 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 01:00 | College Hockey Game | Bowling Green | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 00:57 | College Football Game | Arkansas | ✔ | 14:15 - 3rd · ARK 7 - TA&M 24 | — | In play | — |
| 10-04 00:57 | College Football Game | Bryant | ✘ | — | 99¢ | ✅ Won | $13.85 |
| 10-04 00:55 | USL Championship Game | Tie | ✔ | 88' · ELP 1 - LEX 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 00:53 | College Football Game | Rutgers | ✔ | 11:36 - 2nd · IU 10 - RUTG 0 | — | In play | — |
| 10-04 00:52 | USL Championship Game | Tie | ✔ | 84' · RHI 3 - BFKC 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
