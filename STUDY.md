# 1¢ Study

*Updated Sat Oct 10, 7:57 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

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
| 7682 | 636 | 4 (1%) | 1.1% | -$39.40 (-41%) | Hold to the end: -$39.40 (-41%) |

*In play right now: 65. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 636 | 15% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 6981 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 4 | 1% | -$39.40 | -41% |
| Sell at 2¢ | 94 | 15% | -$70.96 | -74% |
| Sell at 3¢ | 63 | 10% | -$70.83 | -74% |
| Sell at 5¢ | 42 | 7% | -$68.10 | -71% |
| Sell at 10¢ | 20 | 3% | -$69.20 | -73% |
| Sell at 25¢ | 8 | 1% | -$68.92 | -72% |
| Sell at 50¢ | 6 | 1% | -$54.90 | -58% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eSoccer Game | ✘ | 1273 | 0 | 0% | 0% | -100% | -100% | 2 min |
| ITF Women's Match | ✘ | 513 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 487 | 1 | 4% | 3% | -81% | -94% | 10 min |
| ITF Men's Match | ✘ | 437 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 294 | 2 | 9% | 2% | -37% | -85% | 5 min |
| TT Star Series Match | ✘ | 216 | 1 | 2% | 2% | -57% | -96% | 4 min |
| Darts Match | ✘ | 144 | 0 | 1% | 1% | -100% | -99% | 8 min |
| eBasketball Game | ✘ | 142 | 1 | 0% | 0% | -34% | -34% | 1 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 116 | 0 | 7% | 3% | -100% | -88% | 11 min |
| College Football Game | partly | 110 | 2 | 15% | 8% | +70% | -73% | 44 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Women's College Volleyball Match | ✘ | 107 | 1 | 6% | 2% | -13% | -90% | 64 min |
| Men's T20 Cricket Match | ✘ | 91 | 0 | 15% | 4% | -100% | -73% | 21 min |
| Challenger WTA | ✘ | 69 | 0 | 14% | 9% | -100% | -75% | 8 min |
| NHL Game | ✔ | 69 | 0 | 14% | 6% | -100% | -75% | 4 min |
| Dota 2 Game | ✘ | 66 | 0 | 3% | 3% | -100% | -95% | 30 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Serie C Game | ✘ | 55 | 1 | 7% | 2% | +70% | -87% | 8 min |
| R6 Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| English National League Game | ✘ | 48 | 0 | 8% | 6% | -100% | -86% | 11 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KBO Game | ✘ | 44 | 0 | 9% | 7% | -100% | -84% | 7 min |
| KHL Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 5 min |
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
| Tweede Divisie Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| LNB Elite 2 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Finland Korisliiga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| Chinese Basketball Association Game  | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| Professional Baseball Game | partly | 16 | 0 | 12% | 6% | -100% | -78% | 2 min |
| China League 1 Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 5 min |
| Australia NBL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Korea K-League 2 Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| APF Division de Honor Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 5 min |
| Czech NBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Japan J League Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 13 min |
| Ligue 2 Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Men's ODI Cricket Match | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 20 min |
| Slovakia SBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 11 | 1 | 36% | 36% | +748% | -37% | 32 min |
| Bundesliga Basketball Game | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 13 min |
| College Hockey Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's ODI Cricket Match | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 45 min |
| Austria BSL Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 5 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Korea K League Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 14 min |
| TFF 1. Lig Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Bundesliga 2 Game | ✔ | 10 | 0 | 0% | 0% | -100% | -100% | 4 min |
| LNB Elite Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Mobile Legends Bang Bang Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Chinese Super League Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 36 min |
| Major League Soccer Game | partly | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Russia VTB United Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Peru Liga 1 Game | ✘ | 8 | 0 | 25% | 12% | -100% | -57% | 9 min |
| EFL League One Game | ✔ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| Vietnam V-League 1 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Indonesia Super League Game | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech National Football League Game | ✘ | 8 | 0 | 25% | 25% | -100% | -57% | 11 min |
| Slovenia 1. SKL Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 15 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Liga MX Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 1 min |
| Croatia Premijer Liga Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Turkey BSL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 11 min |
| England Super League Basketball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| CFL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Thai League 1 Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 7 min |
| Saudi Pro League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 27 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| PREM Rugby Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Turkish Super Lig Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 10 min |
| Ecuador Liga Pro Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Portugal Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| German 3. Liga Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 1 min |
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
| Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 54 min |
| Eredivisie Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Polish Ekstraklasa Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Belgian Pro League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Ligue 1 Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 10 min |
| La Liga Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 5 min |
| EFL Championship Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Bolivia Premier Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Latvian Virsliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 58 min |
| Singapore Premier League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 261 | 7% | 2% | 0% | -88% |
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
| 10-10 13:56 | Men's T20 Cricket Match | Mpumalanga Rhinos | ✘ | — | — | In play | — |
| 10-10 13:56 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:53 | German 3. Liga Game | Saarbrucken | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:53 | German 3. Liga Game | Fortuna Cologne | ✘ | — | — | In play | — |
| 10-10 13:52 | German 3. Liga Game | Meppen | ✘ | — | — | In play | — |
| 10-10 13:52 | German 3. Liga Game | Stuttgart II | ✘ | — | — | In play | — |
| 10-10 13:50 | Ligue 2 Game | Reims | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:49 | Ligue 2 Game | Nantes | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:47 | Valorant game winner | G2 Esports | ✘ | — | — | In play | — |
| 10-10 13:47 | Tweede Divisie Game | Rohda Raalte | ✘ | — | — | In play | — |
| 10-10 13:47 | Tweede Divisie Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:45 | German 3. Liga Game | Wurzburg | ✘ | — | — | In play | — |
| 10-10 13:42 | Chinese Basketball Association Game  | Zhejiang Golden Bulls | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:42 | Ligue 2 Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:41 | Turkish Super Lig Game | Samsunspor | ✘ | — | — | In play | — |
| 10-10 13:40 | Challenger WTA | Anna Blinkova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:39 | Serie C Game | Giugliano | ✘ | — | — | In play | — |
| 10-10 13:39 | Russia VTB United Game | BK Uralmash Yekaterinburg | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-10 13:38 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:38 | TFF 1. Lig Game | Batman | ✘ | — | — | In play | — |
| 10-10 13:35 | German 3. Liga Game | Großaspach | ✘ | — | — | In play | — |
| 10-10 13:35 | Darts Match | Ryan Searle | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:31 | Tweede Divisie Game | Rijnsburgse | ✘ | — | — | In play | — |
| 10-10 13:31 | Tweede Divisie Game | Tie | ✘ | — | — | In play | — |
| 10-10 13:30 | Singapore Premier League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:30 | Thai League 1 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:28 | Chinese Super League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:26 | Chinese Basketball Association Game  | Guangdong Southern Tigers | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:26 | ITF Women's Match | Jana Otzipka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 13:26 | Ligue 2 Game | Clermont Foot | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
