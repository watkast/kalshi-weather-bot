# 1¢ Study

*Updated Sat Oct 10, 6:30 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 2¢ | 35 finished bets | 17% | -$3.69 | -70% | -10.54¢ | -$1.51 / -$2.18 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 3¢ | 35 | -$3.69 | -70% |
| ESPN win probability ≥ 2%, sell at 5¢ | 35 | -$4.60 | -88% |
| ESPN win probability ≥ 2%, hold to the end | 35 | -$5.25 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 8453 | 735 | 5 (1%) | 1.1% | -$40.25 (-37%) | Hold to the end: -$40.25 (-37%) |

*In play right now: 44. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 163 | 2.9% | 0.0% (0) | -250% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 163 | 0 | -100% | -74% | -74% | -73% |
| ESPN win probability ≥ 2% | 35 | 0 | -100% | -70% | -70% | -88% |
| ESPN win probability ≥ 5% | 13 | 0 | -100% | -87% | -80% | -100% |
| ESPN win probability ≥ 10% | 8 | 0 | -100% | -78% | -68% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 735 | 15% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 7674 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 5 | 1% | -$40.25 | -37% |
| Sell at 2¢ | 108 | 15% | -$82.17 | -75% |
| Sell at 3¢ | 75 | 10% | -$81.00 | -73% |
| Sell at 5¢ | 49 | 7% | -$78.40 | -71% |
| Sell at 10¢ | 23 | 3% | -$80.12 | -73% |
| Sell at 25¢ | 9 | 1% | -$80.46 | -73% |
| Sell at 50¢ | 7 | 1% | -$63.00 | -57% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 1558 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 515 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 503 | 1 | 4% | 3% | -81% | -93% | 10 min |
| ITF Men's Match | ✘ | 439 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 297 | 2 | 9% | 2% | -37% | -85% | 5 min |
| TT Star Series Match | ✘ | 225 | 1 | 2% | 2% | -59% | -96% | 4 min |
| eBasketball Game | ✘ | 175 | 1 | 0% | 0% | -47% | -47% | 1 min |
| College Football Game | partly | 165 | 2 | 12% | 5% | +13% | -79% | 34 min |
| Darts Match | ✘ | 153 | 0 | 1% | 1% | -100% | -99% | 9 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 119 | 0 | 7% | 3% | -100% | -88% | 11 min |
| Women's College Volleyball Match | ✘ | 109 | 2 | 6% | 3% | +71% | -89% | 64 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Men's T20 Cricket Match | ✘ | 98 | 0 | 14% | 4% | -100% | -75% | 19 min |
| Serie C Game | ✘ | 79 | 1 | 5% | 1% | +18% | -91% | 6 min |
| NHL Game | ✔ | 72 | 0 | 15% | 7% | -100% | -74% | 5 min |
| Dota 2 Game | ✘ | 70 | 0 | 3% | 3% | -100% | -95% | 30 min |
| Challenger WTA | ✘ | 69 | 0 | 14% | 9% | -100% | -75% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| R6 Game | ✘ | 51 | 0 | 2% | 2% | -100% | -97% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KHL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 5 min |
| KBO Game | ✘ | 44 | 0 | 9% | 7% | -100% | -84% | 7 min |
| Ettan Game | ✘ | 41 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Liga DIMAYOR Game | ✘ | 37 | 1 | 11% | 3% | +152% | -81% | 7 min |
| Argentina Primera Division Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 8 min |
| AHL Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 6 min |
| ATP Tennis Match | ✘ | 35 | 0 | 9% | 3% | -100% | -85% | 3 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 34 | 1 | 3% | 3% | +175% | -95% | 5 min |
| USL Championship Game | partly | 34 | 0 | 15% | 3% | -100% | -75% | 8 min |
| Uruguay Primera Division Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Japan J2 League Game | ✘ | 32 | 0 | 16% | 3% | -100% | -73% | 12 min |
| Overwatch Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 5 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| LaLiga 2 Game | partly | 28 | 0 | 14% | 7% | -100% | -75% | 8 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ELH Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| WTA Tennis Match | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 4 min |
| Valorant game winner | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 15 min |
| Brasileiro Serie A Game | partly | 26 | 0 | 19% | 12% | -100% | -67% | 4 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Japan NPB Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Argentine Nacional B Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 11 min |
| Slovakian 2. Liga Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 107 min |
| Liga Expansion Game | ✘ | 23 | 0 | 9% | 9% | -100% | -85% | 17 min |
| NBA Game | ✔ | 23 | 0 | 17% | 4% | -100% | -70% | 4 min |
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
| Ligue 2 Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| China League 1 Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 5 min |
| Adriatic ABA Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| TFF 1. Lig Game | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 15 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Australia NBL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Czech NBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Korea K-League 2 Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| German 3. Liga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Major League Soccer Game | partly | 13 | 1 | 15% | 8% | +618% | -73% | 6 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Canadian Premier League | ✘ | 13 | 1 | 31% | 31% | +618% | -47% | 29 min |
| LNB Elite Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech National Football League Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Peru Liga 1 Game | ✘ | 12 | 0 | 25% | 17% | -100% | -57% | 6 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Italy Serie A2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 18 min |
| College Hockey Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Japan J League Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 13 min |
| Bundesliga 2 Game | ✔ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Ligue 1 Game | ✔ | 12 | 0 | 25% | 17% | -100% | -57% | 19 min |
| Men's ODI Cricket Match | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 20 min |
| Austria BSL Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 5 min |
| Spain Liga ACB Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 21 min |
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
| Allsvenskan Game | ✘ | 7 | 0 | 43% | 43% | -100% | -26% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Liga MX Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 1 min |
| Chile Liga de Primera Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| CFL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LKL Lithuania Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eliteserien Game | ✘ | 6 | 0 | 33% | 17% | -100% | -42% | 14 min |
| English Premier League Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 1 min |
| Swiss Super League Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 30 min |
| Croatia HNL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 11 min |
| Bundesliga Game | ✔ | 5 | 1 | 40% | 40% | +1767% | -31% | 19 min |
| Serie A Game | ✔ | 5 | 0 | 20% | 20% | -100% | -65% | 40 min |
| Slovenian Prva Liga Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Bolivia Premier Division Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 4 min |
| Serbian SuperLiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Super League Greece Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Venezuela Liga FUTVE game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
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
| Under 5 min | 306 | 7% | 1% | 0% | -89% |
| 5–15 min | 138 | 18% | 6% | 2% | -69% |
| 15–30 min | 110 | 31% | 17% | 2% | -46% |
| 30–60 min | 93 | 13% | 8% | 0% | -78% |
| Over 60 min | 86 | 20% | 13% | 0% | -66% |

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
| 10-11 00:28 | AHL Game | Hartford Wolf Pack | ✘ | — | — | In play | — |
| 10-11 00:24 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 00:24 | eSoccer Game | Real Madrid (Mordor) | ✘ | — | — | In play | — |
| 10-11 00:23 | Dota 2 Game | Skyreavers | ✘ | — | — | In play | — |
| 10-11 00:21 | eSoccer Game | Botafogo (Hurricane) | ✘ | — | — | In play | — |
| 10-11 00:20 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 00:20 | eSoccer Game | Nantes (Ellen) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:19 | eSoccer Game | Estudiantes (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:18 | College Football Game | North Dakota | ✘ | — | — | In play | — |
| 10-11 00:18 | Women's College Volleyball Match | Wisconsin | ✘ | — | — | In play | — |
| 10-11 00:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:18 | eSoccer Game | OL Lyonnes (Leyla) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:10 | Argentina Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:08 | eBasketball Game | Los Angeles Lakers (Zach) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:07 | eBasketball Game | Brooklyn Nets (Bryce) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:07 | eSoccer Game | Universitario (Danny) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:07 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:06 | eSoccer Game | Nantes (Ellen) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:06 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:04 | Argentina Primera Division Game | Tigre | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:04 | eSoccer Game | RC Lens (Florie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 00:04 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:58 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:58 | USL Championship Game | Tie | ✔ | 90'+5' · LOU 2 - CHS 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:58 | eSoccer Game | CA Osasuna (Homie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:57 | Liga Expansion Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:54 | eSoccer Game | Estudiantes (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-10 23:54 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
