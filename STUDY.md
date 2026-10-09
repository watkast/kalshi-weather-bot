# 1¢ Study

*Updated Fri Oct 9, 1:17 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 599 finished bets | 1% | -$47.85 | -53% | -7.99¢ | -$30.85 / -$17.00 |

*Expect about **51 buys a day**, roughly **$7.58/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 599 | -$56.10 | -62% |
| ESPN-verified leagues only, sell at 10¢ | 599 | -$64.96 | -72% |
| ESPN-verified leagues only, sell at 5¢ | 599 | -$66.45 | -74% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 6678 | 599 | 3 (1%) | 1.1% | -$47.85 (-53%) | Hold to the end: -$47.85 (-53%) |

*In play right now: 23. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 126 | 2.7% | 0.0% (0) | -219% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 126 | 0 | -100% | -72% | -73% | -72% |
| ESPN win probability ≥ 2% | 29 | 0 | -100% | -70% | -73% | -100% |
| ESPN win probability ≥ 5% | 11 | 0 | -100% | -84% | -76% | -100% |
| ESPN win probability ≥ 10% | 6 | 0 | -100% | -71% | -57% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 599 | 15% | 10% | 6% | 3% | 1% | 1% |
| Unverified | 6056 | 5% | 4% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 3 | 1% | -$47.85 | -53% |
| Sell at 2¢ | 87 | 15% | -$67.23 | -75% |
| Sell at 3¢ | 57 | 10% | -$67.62 | -75% |
| Sell at 5¢ | 36 | 6% | -$66.45 | -74% |
| Sell at 10¢ | 19 | 3% | -$64.96 | -72% |
| Sell at 25¢ | 7 | 1% | -$66.68 | -74% |
| Sell at 50¢ | 5 | 1% | -$56.10 | -62% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eSoccer Game | ✘ | 779 | 0 | 0% | 0% | -100% | -100% | 2 min |
| ITF Women's Match | ✘ | 506 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 444 | 1 | 3% | 2% | -79% | -94% | 10 min |
| ITF Men's Match | ✘ | 429 | 1 | 9% | 5% | -78% | -84% | 5 min |
| Challenger ATP  | ✘ | 287 | 2 | 9% | 2% | -35% | -85% | 5 min |
| TT Star Series Match | ✘ | 200 | 1 | 2% | 2% | -53% | -96% | 5 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Darts Match | ✘ | 124 | 0 | 1% | 1% | -100% | -99% | 9 min |
| League of Legends Game | ✘ | 113 | 0 | 6% | 3% | -100% | -89% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| College Football Game | partly | 104 | 2 | 14% | 7% | +79% | -75% | 45 min |
| Women's College Volleyball Match | ✘ | 103 | 1 | 6% | 2% | -9% | -90% | 66 min |
| Men's T20 Cricket Match | ✘ | 86 | 0 | 16% | 5% | -100% | -72% | 21 min |
| eBasketball Game | ✘ | 86 | 1 | 0% | 0% | +9% | +9% | 1 min |
| Challenger WTA | ✘ | 65 | 0 | 15% | 9% | -100% | -73% | 8 min |
| NHL Game | ✔ | 65 | 0 | 14% | 5% | -100% | -76% | 4 min |
| Dota 2 Game | ✘ | 62 | 0 | 3% | 3% | -100% | -94% | 29 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| R6 Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 10 min |
| KBO Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 8 min |
| KHL Game | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 5 min |
| ATP Tennis Match | ✘ | 33 | 0 | 9% | 3% | -100% | -84% | 3 min |
| Ettan Game | ✘ | 33 | 0 | 3% | 0% | -100% | -95% | 5 min |
| Liga DIMAYOR Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 7 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| Liiga Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Liga Leumit Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| ELH Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Euroleague Game | ✘ | 26 | 0 | 23% | 4% | -100% | -60% | 15 min |
| SHL Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 24 | 1 | 4% | 4% | +289% | -93% | 5 min |
| Brasileiro Serie A Game | partly | 24 | 0 | 21% | 12% | -100% | -64% | 8 min |
| FIFA Women's Game | ✘ | 24 | 0 | 12% | 8% | -100% | -78% | 38 min |
| Japan NPB Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Valorant game winner | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 15 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| Overwatch Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 6 min |
| NBA Game | ✔ | 22 | 0 | 18% | 5% | -100% | -68% | 4 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Finland Korisliiga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| Liga Expansion Game | ✘ | 17 | 0 | 12% | 12% | -100% | -80% | 21 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| Professional Baseball Game | partly | 16 | 0 | 12% | 6% | -100% | -78% | 2 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| DEL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| APF Division de Honor Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 5 min |
| Sweden SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Australia NBL Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Women's Pro Basketball Game | ✔ | 11 | 0 | 27% | 9% | -100% | -53% | 7 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovakia SBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 11 | 1 | 36% | 36% | +748% | -37% | 32 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Men's ODI Cricket Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 18 min |
| Austria BSL Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 5 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Women's ODI Cricket Match | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 50 min |
| China League 1 Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 14 min |
| Chinese Basketball Association Game  | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Major League Soccer Game | partly | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| College Hockey Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Mobile Legends Bang Bang Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| TFF 1. Lig Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 16 min |
| Finnish Ykkosliiga Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech National Football League Game | ✘ | 8 | 0 | 25% | 25% | -100% | -57% | 11 min |
| Russia VTB United Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 16 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Slovenia 1. SKL Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 18 min |
| Peru Liga 1 Game | ✘ | 6 | 0 | 33% | 17% | -100% | -42% | 12 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Korea K League Game | ✘ | 6 | 0 | 50% | 17% | -100% | -13% | 16 min |
| Korea K-League 2 Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 5 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Chinese Super League Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Japan J League Game | ✘ | 4 | 0 | 50% | 25% | -100% | -13% | 35 min |
| Saudi Pro League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Bundesliga 2 Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 1 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Vietnam V-League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Indonesia Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 43 min |
| Thai League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 32 min |
| Czech First League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Croatia HNL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 14 min |
| Allsvenskan Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Eliteserien Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Turkish Super Lig Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Danish Superliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| German 3. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 241 | 7% | 1% | 0% | -88% |
| 5–15 min | 112 | 15% | 4% | 1% | -74% |
| 15–30 min | 96 | 28% | 12% | 2% | -51% |
| 30–60 min | 78 | 14% | 8% | 0% | -76% |
| Over 60 min | 70 | 21% | 14% | 0% | -63% |

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
| 10-09 19:13 | ITF Women's Match | Mell Elizabeth Reasco Gonzalez | ✘ | — | — | In play | — |
| 10-09 19:12 | Bundesliga Basketball Game | Medipolis SC Jena | ✘ | — | — | In play | — |
| 10-09 19:08 | eSoccer Game | West Ham (Danny) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:08 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:08 | Eerste Divisie Game | FC Eindhoven | ✘ | — | — | In play | — |
| 10-09 19:07 | eSoccer Game | France (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:07 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:05 | Serie B Game | Sampdoria | ✘ | — | — | In play | — |
| 10-09 19:05 | eSoccer Game | Portugal (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:04 | eSoccer Game | Fulham (Luis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:03 | TT Star Series Match | Prokopcov Dmitrij | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:01 | Sweden SBL Game | Sloga Uppsala | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 19:00 | Darts Match | Alan Soutar | ✘ | — | — | In play | — |
| 10-09 18:58 | Turkish Super Lig Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:57 | Allsvenskan Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:56 | Liiga Game | KalPa Kuopio | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:56 | ITF Women's Match | Francesca Mattioli | ✘ | — | 5¢ | ❌ Lost | -$0.15 |
| 10-09 18:56 | Sweden SBL Game | KFUM Umea | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | Counter-Strike 2 Game | Team Falcons | ✘ | — | — | In play | — |
| 10-09 18:55 | German 3. Liga Game | Munster | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | German 3. Liga Game | Rot-Weiss Essen | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | eSoccer Game | Arsenal (Zaroth) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | Danish Superliga Game | Nordsjaelland | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:55 | Danish Superliga Game | Odense | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:54 | eSoccer Game | England (Demi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:54 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-09 18:54 | KHL Game | HC Dynamo Moscow | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
