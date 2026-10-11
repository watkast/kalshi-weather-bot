# 1¢ Study

*Updated Sat Oct 10, 8:32 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 2¢ | 36 finished bets | 17% | -$3.84 | -71% | -10.67¢ | -$1.66 / -$2.18 |

*Expect about **3 buys a day**, roughly **$0.49/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 3¢ | 36 | -$3.84 | -71% |
| ESPN win probability ≥ 2%, sell at 5¢ | 36 | -$4.75 | -88% |
| ESPN win probability ≥ 2%, hold to the end | 36 | -$5.40 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 8605 | 774 | 5 (1%) | 1.1% | -$46.10 (-40%) | Hold to the end: -$46.10 (-40%) |

*In play right now: 53. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 170 | 2.8% | 0.0% (0) | -239% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 170 | 0 | -100% | -75% | -74% | -72% |
| ESPN win probability ≥ 2% | 36 | 0 | -100% | -71% | -71% | -88% |
| ESPN win probability ≥ 5% | 13 | 0 | -100% | -87% | -80% | -100% |
| ESPN win probability ≥ 10% | 8 | 0 | -100% | -78% | -68% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 774 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 7778 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 5 | 1% | -$46.10 | -40% |
| Sell at 2¢ | 112 | 14% | -$86.98 | -75% |
| Sell at 3¢ | 78 | 10% | -$85.68 | -74% |
| Sell at 5¢ | 52 | 7% | -$82.30 | -71% |
| Sell at 10¢ | 25 | 3% | -$83.35 | -72% |
| Sell at 25¢ | 10 | 1% | -$83.00 | -71% |
| Sell at 50¢ | 8 | 1% | -$62.10 | -53% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 1616 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 516 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 505 | 1 | 4% | 3% | -82% | -93% | 10 min |
| ITF Men's Match | ✘ | 439 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 297 | 2 | 9% | 2% | -37% | -85% | 5 min |
| TT Star Series Match | ✘ | 225 | 1 | 2% | 2% | -59% | -96% | 4 min |
| eBasketball Game | ✘ | 181 | 1 | 0% | 0% | -48% | -48% | 1 min |
| College Football Game | partly | 173 | 2 | 13% | 6% | +8% | -78% | 34 min |
| Darts Match | ✘ | 153 | 0 | 1% | 1% | -100% | -99% | 9 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 119 | 0 | 7% | 3% | -100% | -88% | 11 min |
| Women's College Volleyball Match | ✘ | 109 | 2 | 6% | 3% | +71% | -89% | 64 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Men's T20 Cricket Match | ✘ | 98 | 0 | 14% | 4% | -100% | -75% | 19 min |
| NHL Game | ✔ | 81 | 0 | 15% | 7% | -100% | -74% | 5 min |
| Serie C Game | ✘ | 79 | 1 | 5% | 1% | +18% | -91% | 6 min |
| Dota 2 Game | ✘ | 71 | 0 | 3% | 3% | -100% | -95% | 30 min |
| Challenger WTA | ✘ | 69 | 0 | 14% | 9% | -100% | -75% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| R6 Game | ✘ | 52 | 0 | 2% | 2% | -100% | -97% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KHL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 5 min |
| AHL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 6 min |
| KBO Game | ✘ | 44 | 0 | 9% | 7% | -100% | -84% | 7 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Ettan Game | ✘ | 41 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Liga DIMAYOR Game | ✘ | 39 | 1 | 10% | 3% | +139% | -82% | 6 min |
| Argentina Primera Division Game | ✘ | 39 | 0 | 18% | 8% | -100% | -69% | 8 min |
| ATP Tennis Match | ✘ | 35 | 0 | 9% | 3% | -100% | -85% | 3 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 34 | 1 | 3% | 3% | +175% | -95% | 5 min |
| Uruguay Primera Division Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Overwatch Game | ✘ | 32 | 0 | 3% | 0% | -100% | -95% | 5 min |
| Japan J2 League Game | ✘ | 32 | 0 | 16% | 3% | -100% | -73% | 12 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| LaLiga 2 Game | partly | 28 | 0 | 14% | 7% | -100% | -75% | 8 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie A Game | partly | 28 | 0 | 18% | 11% | -100% | -69% | 4 min |
| Major League Soccer Game | partly | 27 | 1 | 15% | 4% | +246% | -74% | 6 min |
| ELH Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| WTA Tennis Match | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 4 min |
| Valorant game winner | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 15 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| NBA Game | ✔ | 26 | 0 | 15% | 4% | -100% | -73% | 4 min |
| Japan NPB Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga Expansion Game | ✘ | 25 | 0 | 8% | 8% | -100% | -86% | 13 min |
| Argentine Nacional B Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 11 min |
| Slovakian 2. Liga Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 107 min |
| DEL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Finland Korisliiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Bundesliga Basketball Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 12 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| Chinese Basketball Association Game  | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Professional Baseball Game | partly | 16 | 0 | 12% | 6% | -100% | -78% | 2 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| College Hockey Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Ligue 2 Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| China League 1 Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 5 min |
| Adriatic ABA Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| TFF 1. Lig Game | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 15 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Australia NBL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Czech NBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Peru Liga 1 Game | ✘ | 14 | 0 | 29% | 21% | -100% | -50% | 6 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Korea K-League 2 Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| German 3. Liga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Canadian Premier League | ✘ | 13 | 1 | 31% | 31% | +618% | -47% | 29 min |
| LNB Elite Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech National Football League Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Italy Serie A2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Japan J League Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 13 min |
| Bundesliga 2 Game | ✔ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Ligue 1 Game | ✔ | 12 | 0 | 25% | 17% | -100% | -57% | 19 min |
| Men's ODI Cricket Match | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 20 min |
| Austria BSL Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 5 min |
| Spain Liga ACB Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 21 min |
| Liga MX Game | ✔ | 10 | 0 | 20% | 20% | -100% | -65% | 1 min |
| Women's ODI Cricket Match | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 45 min |
| Italy Serie A Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Korea K League Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 14 min |
| Mobile Legends Bang Bang Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Indonesia Super League Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 14 min |
| Saudi Pro League Game | ✘ | 10 | 0 | 20% | 20% | -100% | -65% | 16 min |
| Serie B Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 14 min |
| Eredivisie Game | ✔ | 10 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Ecuador Liga Pro Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Belgian Pro League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 22 min |
| Israeli Premier League Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Croatia Premijer Liga Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Turkey BSL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Chinese Super League Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 36 min |
| Polish Ekstraklasa Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 30 min |
| Czech First League Game | ✘ | 9 | 0 | 22% | 0% | -100% | -61% | 9 min |
| EFL Championship Game | ✔ | 9 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Russia VTB United Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Vietnam V-League 1 Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Thai League 1 Game | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Turkish Super Lig Game | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 13 min |
| Liga Portugal Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| La Liga Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 9 min |
| Slovenia 1. SKL Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 15 min |
| England Super League Basketball Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 12 min |
| CFL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Allsvenskan Game | ✘ | 7 | 0 | 43% | 43% | -100% | -26% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Chile Liga de Primera Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LKL Lithuania Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eliteserien Game | ✘ | 6 | 0 | 33% | 17% | -100% | -42% | 14 min |
| Bolivia Premier Division Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 5 min |
| English Premier League Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 1 min |
| Swiss Super League Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 30 min |
| Venezuela Liga FUTVE game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 20 min |
| Croatia HNL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 11 min |
| Bundesliga Game | ✔ | 5 | 1 | 40% | 40% | +1767% | -31% | 19 min |
| Serie A Game | ✔ | 5 | 0 | 20% | 20% | -100% | -65% | 40 min |
| Slovenian Prva Liga Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Serbian SuperLiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Super League Greece Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Latvian Virsliga Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Scottish Premiership Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 87 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Danish Superliga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Singapore Premier League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Faroe Islands Premier League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 86 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 323 | 6% | 1% | 0% | -89% |
| 5–15 min | 149 | 18% | 6% | 2% | -69% |
| 15–30 min | 116 | 30% | 17% | 2% | -48% |
| 30–60 min | 96 | 12% | 7% | 0% | -78% |
| Over 60 min | 88 | 20% | 14% | 0% | -65% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 47 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-11 02:28 | College Football Game | North Dakota St. | ✔ | 1:23 - 4th · NDSU 7 - UNLV 13 | — | In play | — |
| 10-11 02:27 | Major League Soccer Game | Tie | ✔ | 88' · NSH 2 - ATX 1 | — | In play | — |
| 10-11 02:27 | Major League Soccer Game | Houston | ✔ | 88' · HOU 1 - MIN 2 | — | In play | — |
| 10-11 02:26 | eSoccer Game | FSV Mainz 05 (Eder) | ✘ | — | — | In play | — |
| 10-11 02:25 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 02:24 | eSoccer Game | France (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:24 | eSoccer Game | Argentina (Millie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:24 | eSoccer Game | 1. FC Köln (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:23 | eSoccer Game | FC Augsburg (Danny) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:23 | eSoccer Game | United States (Leyla) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:23 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:22 | Counter-Strike 2 Game | Wanted Goons | ✘ | — | — | In play | — |
| 10-11 02:19 | Argentina Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:19 | AHL Game | Chicago Wolves | ✘ | — | — | In play | — |
| 10-11 02:19 | College Football Game | Austin Peay | ✘ | — | 17¢ | ❌ Lost | -$0.15 |
| 10-11 02:14 | eSoccer Game | Manchester City (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:14 | eSoccer Game | Everton (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:12 | College Football Game | Northern Colorado | ✘ | — | — | In play | — |
| 10-11 02:11 | eSoccer Game | Dortmund (Niskanen15) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:11 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:09 | eSoccer Game | 1. FC Köln (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:08 | eSoccer Game | United States (Leyla) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:07 | NHL Game | New York I | ✔ | 1:44 - 3rd · TB 3 - NYI 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:06 | Major League Soccer Game | Austin | ✔ | 68' · NSH 1 - ATX 0 | — | In play | — |
| 10-11 02:06 | College Hockey Game | Colgate | ✘ | — | — | In play | — |
| 10-11 02:05 | NBA Game | Detroit | ✔ | 34.7 - OT · DET 108 - WSH 110 | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:05 | College Hockey Game | Bemidji State | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 02:03 | R6 Game | Man eSports LFO | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
