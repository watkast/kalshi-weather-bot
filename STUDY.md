# 1¢ Study

*Updated Sun Oct 11, 7:30 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 2¢ | 37 finished bets | 16% | -$3.99 | -72% | -10.78¢ | -$1.66 / -$2.33 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**; typical wait to sell **2 min**.*

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
| 9270 | 813 | 5 (1%) | 1.1% | -$51.95 (-43%) | Hold to the end: -$51.95 (-43%) |

*In play right now: 72. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 187 | 2.6% | 0.0% (0) | -216% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 187 | 0 | -100% | -75% | -75% | -72% |
| ESPN win probability ≥ 2% | 37 | 0 | -100% | -72% | -72% | -88% |
| ESPN win probability ≥ 5% | 14 | 0 | -100% | -88% | -81% | -100% |
| ESPN win probability ≥ 10% | 8 | 0 | -100% | -78% | -68% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 813 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 8385 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 5 | 1% | -$51.95 | -43% |
| Sell at 2¢ | 117 | 14% | -$91.53 | -75% |
| Sell at 3¢ | 80 | 10% | -$90.75 | -74% |
| Sell at 5¢ | 54 | 7% | -$86.85 | -71% |
| Sell at 10¢ | 26 | 3% | -$87.89 | -72% |
| Sell at 25¢ | 10 | 1% | -$88.85 | -73% |
| Sell at 50¢ | 8 | 1% | -$67.95 | -56% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 1981 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 527 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 516 | 1 | 4% | 3% | -82% | -93% | 11 min |
| ITF Men's Match | ✘ | 447 | 1 | 9% | 5% | -79% | -84% | 5 min |
| Challenger ATP  | ✘ | 329 | 2 | 9% | 2% | -43% | -85% | 5 min |
| TT Star Series Match | ✘ | 225 | 1 | 2% | 2% | -59% | -96% | 4 min |
| eBasketball Game | ✘ | 213 | 1 | 0% | 0% | -56% | -56% | 1 min |
| College Football Game | partly | 188 | 2 | 13% | 6% | -1% | -78% | 31 min |
| Darts Match | ✘ | 161 | 0 | 1% | 1% | -100% | -99% | 9 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 120 | 0 | 7% | 2% | -100% | -88% | 11 min |
| Women's College Volleyball Match | ✘ | 109 | 2 | 6% | 3% | +71% | -89% | 64 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Men's T20 Cricket Match | ✘ | 106 | 1 | 14% | 5% | -12% | -75% | 20 min |
| Challenger WTA | ✘ | 85 | 0 | 13% | 7% | -100% | -78% | 8 min |
| NHL Game | ✔ | 83 | 0 | 16% | 7% | -100% | -73% | 5 min |
| Serie C Game | ✘ | 83 | 1 | 5% | 1% | +12% | -92% | 6 min |
| Dota 2 Game | ✘ | 71 | 0 | 3% | 3% | -100% | -95% | 30 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| R6 Game | ✘ | 52 | 0 | 2% | 2% | -100% | -97% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| AHL Game | ✘ | 49 | 0 | 4% | 2% | -100% | -93% | 6 min |
| Brasileiro Serie B Game | ✘ | 46 | 0 | 2% | 0% | -100% | -96% | 11 min |
| KBO Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 7 min |
| KHL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 5 min |
| Ettan Game | ✘ | 43 | 0 | 5% | 0% | -100% | -92% | 7 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| Liga DIMAYOR Game | ✘ | 39 | 1 | 10% | 3% | +139% | -82% | 6 min |
| Argentina Primera Division Game | ✘ | 39 | 0 | 18% | 8% | -100% | -69% | 8 min |
| Overwatch Game | ✘ | 38 | 0 | 5% | 0% | -100% | -91% | 5 min |
| Major League Soccer Game | partly | 37 | 1 | 16% | 5% | +152% | -72% | 6 min |
| ATP Tennis Match | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 3 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| Liga Leumit Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 34 | 1 | 3% | 3% | +175% | -95% | 5 min |
| Uruguay Primera Division Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Liga Expansion Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 10 min |
| NBA Game | ✔ | 31 | 0 | 13% | 3% | -100% | -78% | 4 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| WTA Tennis Match | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 4 min |
| Slovakian 2. Liga Game | ✘ | 30 | 0 | 7% | 7% | -100% | -88% | 111 min |
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
| Chinese Basketball Association Game  | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 10 min |
| China League 1 Game | ✘ | 23 | 0 | 13% | 9% | -100% | -77% | 6 min |
| DEL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Finland Korisliiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Baseball Game | partly | 17 | 0 | 12% | 6% | -100% | -80% | 2 min |
| Bundesliga Basketball Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 12 min |
| NFL Game | ✔ | 17 | 0 | 24% | 6% | -100% | -59% | 3 min |
| Adriatic ABA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 10 min |
| College Hockey Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australia NBL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 7 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Mobile Legends Bang Bang Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Ligue 2 Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| TFF 1. Lig Game | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 15 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Czech NBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Peru Liga 1 Game | ✘ | 14 | 0 | 29% | 21% | -100% | -50% | 6 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Spain Liga ACB Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 19 min |
| Indonesia Super League Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 13 min |
| German 3. Liga Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Liga MX Game | ✔ | 13 | 0 | 15% | 15% | -100% | -73% | 1 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Men's ODI Cricket Match | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 20 min |
| Canadian Premier League | ✘ | 13 | 1 | 31% | 31% | +618% | -47% | 29 min |
| LNB Elite Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Czech National Football League Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Italy Serie A2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Thai League 1 Game | ✘ | 12 | 0 | 17% | 0% | -100% | -71% | 8 min |
| Bundesliga 2 Game | ✔ | 12 | 0 | 8% | 8% | -100% | -86% | 4 min |
| Eredivisie Game | ✔ | 12 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Ligue 1 Game | ✔ | 12 | 0 | 25% | 17% | -100% | -57% | 19 min |
| Women's ODI Cricket Match | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 50 min |
| Austria BSL Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 5 min |
| Chinese Super League Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 34 min |
| Czech First League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 11 min |
| EFL Championship Game | ✔ | 11 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Croatia Premijer Liga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Turkey BSL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Vietnam V-League 1 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Saudi Pro League Game | ✘ | 10 | 0 | 20% | 20% | -100% | -65% | 16 min |
| Turkish Super Lig Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 12 min |
| Serie B Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 14 min |
| Ecuador Liga Pro Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Belgian Pro League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 22 min |
| Israeli Premier League Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Polish Ekstraklasa Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 30 min |
| Russia VTB United Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Finnish Ykkosliiga Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Liga Portugal Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| La Liga Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 9 min |
| Slovenia 1. SKL Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 15 min |
| England Super League Basketball Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 12 min |
| CFL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Allsvenskan Game | ✘ | 7 | 0 | 43% | 43% | -100% | -26% | 12 min |
| Serie A Game | ✔ | 7 | 0 | 14% | 14% | -100% | -75% | 28 min |
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
| Women's T20 Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Croatia HNL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 11 min |
| Bundesliga Game | ✔ | 5 | 1 | 40% | 40% | +1767% | -31% | 19 min |
| Latvian Virsliga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Scottish Premiership Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 78 min |
| Slovenian Prva Liga Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Serbian SuperLiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Super League Greece Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
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
| Under 5 min | 345 | 6% | 1% | 0% | -90% |
| 5–15 min | 157 | 18% | 6% | 2% | -68% |
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
| 10-11 13:30 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:29 | eSoccer Game | Manchester Utd (Adri) | ✘ | — | — | In play | — |
| 10-11 13:28 | Thai League 1 Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:28 | Counter-Strike 2 Game | Spirit | ✘ | — | — | In play | — |
| 10-11 13:26 | Bundesliga 2 Game | Tie | ✔ | 90'+5' · DSC 1 - BOC 0 | — | In play | — |
| 10-11 13:25 | Chinese Basketball Association Game  | Jiangsu Dragons | ✘ | — | — | In play | — |
| 10-11 13:25 | Chinese Super League Game | Wuhan Three Towns FC | ✘ | — | — | In play | — |
| 10-11 13:24 | Challenger ATP  | Guilherme Valdoleiros | ✘ | — | — | In play | — |
| 10-11 13:24 | Men's T20 Cricket Match | Old Hararians 1 | ✘ | — | — | In play | — |
| 10-11 13:23 | Belgian Pro League Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:23 | China League 1 Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:23 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:23 | eSoccer Game | Hoffenheim (Zaroth) | ✘ | — | — | In play | — |
| 10-11 13:22 | WTA Tennis Match | Mirra Andreeva | ✘ | — | — | In play | — |
| 10-11 13:22 | Thai League 1 Game | Chonburi | ✘ | — | — | In play | — |
| 10-11 13:20 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:20 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:19 | Bundesliga 2 Game | Bochum | ✔ | 88' · DSC 1 - BOC 0 | — | In play | — |
| 10-11 13:19 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:19 | Singapore Premier League Game | Tie | ✘ | — | — | In play | — |
| 10-11 13:18 | Bundesliga 2 Game | Tie | ✔ | 87' · KSC 0 - STP 2 | — | In play | — |
| 10-11 13:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:18 | eSoccer Game | Rennes (Sheerpy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:17 | eSoccer Game | Manchester Utd (Adri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:17 | German 3. Liga Game | Ingolstadt | ✘ | — | — | In play | — |
| 10-11 13:17 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:14 | eBasketball Game | Denver Nuggets (Barry) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-11 13:14 | Men's T20 Cricket Match | CSA Emerging | ✘ | — | — | In play | — |
| 10-11 13:14 | Belgian Pro League Game | Standard | ✘ | — | — | In play | — |
| 10-11 13:13 | Bundesliga 2 Game | Tie | ✔ | 85' · SGF 0 - BSC 2 | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
