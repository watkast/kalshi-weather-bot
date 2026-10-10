# 1¢ Study

*Updated Sat Oct 10, 7:16 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 2¢ | 32 finished bets | 19% | -$3.24 | -68% | -10.13¢ | -$1.36 / -$1.88 |

*Expect about **3 buys a day**, roughly **$0.46/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 3¢ | 32 | -$3.24 | -68% |
| ESPN win probability ≥ 2%, sell at 5¢ | 32 | -$4.15 | -86% |
| ESPN win probability ≥ 2%, hold to the end | 32 | -$4.80 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 7624 | 634 | 4 (1%) | 1.1% | -$39.10 (-41%) | Hold to the end: -$39.10 (-41%) |

*In play right now: 50. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 134 | 2.6% | 0.0% (0) | -208% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 134 | 0 | -100% | -72% | -71% | -68% |
| ESPN win probability ≥ 2% | 32 | 0 | -100% | -68% | -68% | -86% |
| ESPN win probability ≥ 5% | 11 | 0 | -100% | -84% | -76% | -100% |
| ESPN win probability ≥ 10% | 6 | 0 | -100% | -71% | -57% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 634 | 15% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 6940 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 4 | 1% | -$39.10 | -41% |
| Sell at 2¢ | 94 | 15% | -$70.66 | -74% |
| Sell at 3¢ | 63 | 10% | -$70.53 | -74% |
| Sell at 5¢ | 42 | 7% | -$67.80 | -71% |
| Sell at 10¢ | 20 | 3% | -$68.90 | -72% |
| Sell at 25¢ | 8 | 1% | -$68.62 | -72% |
| Sell at 50¢ | 6 | 1% | -$54.60 | -57% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eSoccer Game | ✘ | 1263 | 0 | 0% | 0% | -100% | -100% | 2 min |
| ITF Women's Match | ✘ | 512 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 484 | 1 | 4% | 3% | -81% | -94% | 10 min |
| ITF Men's Match | ✘ | 437 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 294 | 2 | 9% | 2% | -37% | -85% | 5 min |
| TT Star Series Match | ✘ | 216 | 1 | 2% | 2% | -57% | -96% | 4 min |
| Darts Match | ✘ | 143 | 0 | 1% | 1% | -100% | -99% | 9 min |
| eBasketball Game | ✘ | 141 | 1 | 0% | 0% | -34% | -34% | 1 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 116 | 0 | 7% | 3% | -100% | -88% | 11 min |
| College Football Game | partly | 110 | 2 | 15% | 8% | +70% | -73% | 44 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Women's College Volleyball Match | ✘ | 107 | 1 | 6% | 2% | -13% | -90% | 64 min |
| Men's T20 Cricket Match | ✘ | 90 | 0 | 16% | 4% | -100% | -73% | 21 min |
| NHL Game | ✔ | 69 | 0 | 14% | 6% | -100% | -75% | 4 min |
| Challenger WTA | ✘ | 68 | 0 | 15% | 9% | -100% | -75% | 8 min |
| Dota 2 Game | ✘ | 65 | 0 | 3% | 3% | -100% | -95% | 30 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Serie C Game | ✘ | 55 | 1 | 7% | 2% | +70% | -87% | 8 min |
| R6 Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| English National League Game | ✘ | 48 | 0 | 8% | 6% | -100% | -86% | 11 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KBO Game | ✘ | 44 | 0 | 9% | 7% | -100% | -84% | 7 min |
| KHL Game | ✘ | 41 | 0 | 5% | 2% | -100% | -92% | 5 min |
| Ettan Game | ✘ | 41 | 0 | 2% | 0% | -100% | -96% | 7 min |
| AHL Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 6 min |
| Liga DIMAYOR Game | ✘ | 35 | 1 | 11% | 3% | +167% | -80% | 7 min |
| ATP Tennis Match | ✘ | 35 | 0 | 9% | 3% | -100% | -85% | 3 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| USL Championship Game | partly | 32 | 0 | 12% | 3% | -100% | -78% | 8 min |
| Japan J2 League Game | ✘ | 32 | 0 | 16% | 3% | -100% | -73% | 12 min |
| Argentina Primera Division Game | ✘ | 31 | 0 | 19% | 10% | -100% | -66% | 8 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Liiga Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| National League Game | ✘ | 28 | 1 | 4% | 4% | +233% | -94% | 5 min |
| ELH Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Overwatch Game | ✘ | 27 | 0 | 4% | 0% | -100% | -94% | 6 min |
| Uruguay Primera Division Game | ✘ | 26 | 0 | 4% | 4% | -100% | -93% | 11 min |
| WTA Tennis Match | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 4 min |
| Japan NPB Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Valorant game winner | ✘ | 25 | 0 | 8% | 4% | -100% | -86% | 15 min |
| SHL Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie A Game | partly | 24 | 0 | 21% | 12% | -100% | -64% | 8 min |
| NBA Game | ✔ | 23 | 0 | 17% | 4% | -100% | -70% | 4 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| DEL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Expansion Game | ✘ | 21 | 0 | 10% | 10% | -100% | -83% | 19 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| LNB Elite 2 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Finland Korisliiga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| Professional Baseball Game | partly | 16 | 0 | 12% | 6% | -100% | -78% | 2 min |
| Australia NBL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Korea K-League 2 Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| China League 1 Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 6 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Chinese Basketball Association Game  | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 8 min |
| APF Division de Honor Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 5 min |
| Czech NBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Japan J League Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 13 min |
| Men's ODI Cricket Match | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 20 min |
| Slovakia SBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 11 | 1 | 36% | 36% | +748% | -37% | 32 min |
| Bundesliga Basketball Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 13 min |
| College Hockey Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Austria BSL Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 5 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Korea K League Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 14 min |
| TFF 1. Lig Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Bundesliga 2 Game | ✔ | 10 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Ligue 2 Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's ODI Cricket Match | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 50 min |
| LNB Elite Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Mobile Legends Bang Bang Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Major League Soccer Game | partly | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Peru Liga 1 Game | ✘ | 8 | 0 | 25% | 12% | -100% | -57% | 9 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| Vietnam V-League 1 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Indonesia Super League Game | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech National Football League Game | ✘ | 8 | 0 | 25% | 25% | -100% | -57% | 11 min |
| Slovenia 1. SKL Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 15 min |
| Russia VTB United Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 16 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Liga MX Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 1 min |
| Croatia Premijer Liga Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Turkey BSL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 11 min |
| England Super League Basketball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| CFL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Saudi Pro League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 27 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Chinese Super League Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| PREM Rugby Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Thai League 1 Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Turkish Super Lig Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 10 min |
| Ecuador Liga Pro Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Portugal Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bundesliga Game | ✔ | 3 | 1 | 67% | 67% | +3011% | +16% | 14 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Czech First League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Croatia HNL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 14 min |
| Allsvenskan Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Eliteserien Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Danish Superliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| German 3. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 54 min |
| Eredivisie Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Polish Ekstraklasa Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Belgian Pro League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Ligue 1 Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 10 min |
| La Liga Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 5 min |
| EFL Championship Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Bolivia Premier Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Latvian Virsliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 58 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 259 | 7% | 2% | 0% | -88% |
| 5–15 min | 121 | 16% | 5% | 2% | -73% |
| 15–30 min | 101 | 30% | 15% | 2% | -49% |
| 30–60 min | 81 | 15% | 9% | 0% | -74% |
| Over 60 min | 70 | 21% | 14% | 0% | -63% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 45 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-10 13:15 | EFL League One Game | Notts | ✔ | 86' · OXF 1 - NCO 0 | — | In play | — |
| 10-10 13:14 | Singapore Premier League Game | Albirex Niigata (S) | ✘ | — | — | In play | — |
| 10-10 13:14 | EFL Championship Game | Norwich | ✔ | 86' · NOR 1 - SWA 2 | — | In play | — |
| 10-10 13:14 | eBasketball Game | Dallas Mavericks (Melo) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:13 | EFL Championship Game | West Bromwich | ✔ | 86' · BIR 1 - WBA 0 | — | In play | — |
| 10-10 13:13 | eBasketball Game | Indiana Pacers (Jason) | ✘ | — | — | In play | — |
| 10-10 13:12 | Chinese Basketball Association Game  | Sichuan Blue Whales | ✘ | — | — | In play | — |
| 10-10 13:11 | English National League Game | Aldershot | ✘ | — | — | In play | — |
| 10-10 13:11 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:11 | eSoccer Game | FC Bayern (Zaroth) | ✘ | — | — | In play | — |
| 10-10 13:09 | German 3. Liga Game | Havelse | ✘ | — | — | In play | — |
| 10-10 13:09 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:08 | Chinese Basketball Association Game  | Shenzhen Leopards | ✘ | — | — | In play | — |
| 10-10 13:08 | eSoccer Game | Nantes (Antonio) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:08 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:07 | English Premier League Game | Leeds United | ✔ | 78' · LEE 1 - ARS 2 | — | In play | — |
| 10-10 13:07 | Counter-Strike 2 Game | Nemiga | ✘ | — | — | In play | — |
| 10-10 13:06 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:06 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:05 | Darts Match | Martin Schindler | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:04 | eSoccer Game | Chelsea (Emily) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:04 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:00 | Women's ODI Cricket Match | Lions Women | ✘ | — | — | In play | — |
| 10-10 12:59 | Tweede Divisie Game | Tie | ✘ | — | — | In play | — |
| 10-10 12:56 | Chinese Super League Game | Tie | ✘ | — | — | In play | — |
| 10-10 12:56 | Thai League 1 Game | Ayutthaya Utd | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 12:56 | Thai League 1 Game | Pathum United | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 12:55 | Overwatch Game | JD Gaming | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 12:55 | Vietnam V-League 1 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 12:53 | Ettan Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
