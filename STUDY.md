# 1¢ Study

*Updated Sun Oct 11, 3:23 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 2¢ | 37 finished bets | 16% | -$3.99 | -72% | -10.78¢ | -$1.66 / -$2.33 |

*Expect about **3 buys a day**, roughly **$0.49/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 3¢ | 37 | -$3.99 | -72% |
| ESPN win probability ≥ 2%, sell at 5¢ | 37 | -$4.90 | -88% |
| ESPN win probability ≥ 2%, hold to the end | 37 | -$5.55 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 8985 | 806 | 5 (1%) | 1.1% | -$50.90 (-42%) | Hold to the end: -$50.90 (-42%) |

*In play right now: 53. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 186 | 2.6% | 0.0% (0) | -218% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 186 | 0 | -100% | -75% | -75% | -72% |
| ESPN win probability ≥ 2% | 37 | 0 | -100% | -72% | -72% | -88% |
| ESPN win probability ≥ 5% | 14 | 0 | -100% | -88% | -81% | -100% |
| ESPN win probability ≥ 10% | 8 | 0 | -100% | -78% | -68% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 806 | 15% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 8126 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 5 | 1% | -$50.90 | -42% |
| Sell at 2¢ | 117 | 15% | -$90.48 | -75% |
| Sell at 3¢ | 80 | 10% | -$89.70 | -74% |
| Sell at 5¢ | 54 | 7% | -$85.80 | -71% |
| Sell at 10¢ | 26 | 3% | -$86.84 | -72% |
| Sell at 25¢ | 10 | 1% | -$87.80 | -73% |
| Sell at 50¢ | 8 | 1% | -$66.90 | -55% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 1862 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 516 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 511 | 1 | 4% | 3% | -82% | -93% | 11 min |
| ITF Men's Match | ✘ | 439 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 308 | 2 | 9% | 2% | -39% | -85% | 5 min |
| TT Star Series Match | ✘ | 225 | 1 | 2% | 2% | -59% | -96% | 4 min |
| eBasketball Game | ✘ | 201 | 1 | 0% | 0% | -54% | -54% | 1 min |
| College Football Game | partly | 188 | 2 | 13% | 6% | -1% | -78% | 31 min |
| Darts Match | ✘ | 156 | 0 | 1% | 1% | -100% | -99% | 9 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 119 | 0 | 7% | 3% | -100% | -88% | 11 min |
| Women's College Volleyball Match | ✘ | 109 | 2 | 6% | 3% | +71% | -89% | 64 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Men's T20 Cricket Match | ✘ | 104 | 0 | 13% | 4% | -100% | -77% | 21 min |
| NHL Game | ✔ | 83 | 0 | 16% | 7% | -100% | -73% | 5 min |
| Serie C Game | ✘ | 79 | 1 | 5% | 1% | +18% | -91% | 6 min |
| Dota 2 Game | ✘ | 71 | 0 | 3% | 3% | -100% | -95% | 30 min |
| Challenger WTA | ✘ | 70 | 0 | 14% | 9% | -100% | -75% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| R6 Game | ✘ | 52 | 0 | 2% | 2% | -100% | -97% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| AHL Game | ✘ | 49 | 0 | 4% | 2% | -100% | -93% | 6 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KBO Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 7 min |
| KHL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 5 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Ettan Game | ✘ | 41 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Liga DIMAYOR Game | ✘ | 39 | 1 | 10% | 3% | +139% | -82% | 6 min |
| Argentina Primera Division Game | ✘ | 39 | 0 | 18% | 8% | -100% | -69% | 8 min |
| Japan J2 League Game | ✘ | 38 | 0 | 13% | 3% | -100% | -77% | 9 min |
| Major League Soccer Game | partly | 37 | 1 | 16% | 5% | +152% | -72% | 6 min |
| ATP Tennis Match | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 3 min |
| Overwatch Game | ✘ | 35 | 0 | 3% | 0% | -100% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 34 | 1 | 3% | 3% | +175% | -95% | 5 min |
| Uruguay Primera Division Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Liga Expansion Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 10 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| WTA Tennis Match | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 4 min |
| NBA Game | ✔ | 30 | 0 | 13% | 3% | -100% | -77% | 4 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| LaLiga 2 Game | partly | 28 | 0 | 14% | 7% | -100% | -75% | 8 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie A Game | partly | 28 | 0 | 18% | 11% | -100% | -69% | 4 min |
| Japan NPB Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 2 min |
| ELH Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Valorant game winner | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 15 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Argentine Nacional B Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 11 min |
| Slovakian 2. Liga Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 107 min |
| Chinese Basketball Association Game  | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| DEL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Finland Korisliiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| China League 1 Game | ✘ | 17 | 0 | 12% | 12% | -100% | -80% | 5 min |
| Professional Baseball Game | partly | 17 | 0 | 12% | 6% | -100% | -80% | 2 min |
| Bundesliga Basketball Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 12 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| College Hockey Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australia NBL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 7 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Ligue 2 Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| Adriatic ABA Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| TFF 1. Lig Game | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 15 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Czech NBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Peru Liga 1 Game | ✘ | 14 | 0 | 29% | 21% | -100% | -50% | 6 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| German 3. Liga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Liga MX Game | ✔ | 13 | 0 | 15% | 15% | -100% | -73% | 1 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Canadian Premier League | ✘ | 13 | 1 | 31% | 31% | +618% | -47% | 29 min |
| LNB Elite Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech National Football League Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Italy Serie A2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Mobile Legends Bang Bang Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Bundesliga 2 Game | ✔ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Ligue 1 Game | ✔ | 12 | 0 | 25% | 17% | -100% | -57% | 19 min |
| Men's ODI Cricket Match | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 20 min |
| Austria BSL Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 5 min |
| Spain Liga ACB Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 21 min |
| Women's ODI Cricket Match | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 45 min |
| Italy Serie A Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
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
| Under 5 min | 341 | 6% | 1% | 0% | -90% |
| 5–15 min | 154 | 19% | 6% | 2% | -67% |
| 15–30 min | 118 | 31% | 17% | 2% | -46% |
| 30–60 min | 101 | 13% | 8% | 0% | -78% |
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
| 10-11 09:21 | Challenger ATP  | Pyotr Nesterov | ✘ | — | — | In play | — |
| 10-11 09:20 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 09:20 | eSoccer Game | Manchester City (Mantis) | ✘ | — | — | In play | — |
| 10-11 09:19 | eSoccer Game | Benfica (Kevin) | ✘ | — | — | In play | — |
| 10-11 09:19 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 09:18 | Challenger ATP  | Petr Bar Biryukov | ✘ | — | — | In play | — |
| 10-11 09:17 | Overwatch Game | SHENGSHI Esports | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:16 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 09:16 | eSoccer Game | FC Bayern (Hazard) | ✘ | — | — | In play | — |
| 10-11 09:15 | Overwatch Game | Poker Face | ✘ | — | — | In play | — |
| 10-11 09:12 | Challenger WTA | Amandine Hesse | ✘ | — | — | In play | — |
| 10-11 09:10 | Counter-Strike 2 Game | Abyssal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:09 | Women's T20 Match | Lions Women | ✘ | — | — | In play | — |
| 10-11 09:09 | Challenger WTA | Alja Senica | ✘ | — | — | In play | — |
| 10-11 09:09 | eSoccer Game | Everton (Nairo) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:06 | eBasketball Game | New Orleans Pelicans (Tatum) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:05 | eSoccer Game | Manchester City (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:05 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:04 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:04 | eSoccer Game | Montpellier (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:03 | eBasketball Game | Dallas Mavericks (Shaq) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:03 | Challenger ATP  | Sergey Betov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:02 | Challenger ATP  | Gijs Brouwer | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-11 09:02 | eSoccer Game | Paris Saint-Germain (Kylian) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:02 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:01 | Chinese Basketball Association Game  | Ningbo Rockets | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:01 | eSoccer Game | RC Lens (Lotta) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:01 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 09:00 | Challenger ATP  | Thomas Fancutt | ✘ | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
