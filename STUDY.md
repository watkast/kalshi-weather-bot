# 1¢ Study

*Updated Mon Oct 12, 3:42 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 43 finished bets | 2% | $7.55 | +117% | +17.56¢ | -$3.15 / $10.70 |

*Expect about **3 buys a day**, roughly **$0.52/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 43 | $0.30 | +5% |
| ESPN win probability ≥ 2%, sell at 25¢ | 43 | -$3.14 | -49% |
| ESPN win probability ≥ 2%, sell at 3¢ | 43 | -$4.11 | -64% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 11159 | 918 | 6 (1%) | 1.1% | -$53.70 (-39%) | Hold to the end: -$53.70 (-39%) |

*In play right now: 17. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 204 | 3.1% | 0.5% (1) | -30% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 204 | 1 | -54% | -75% | -73% | -72% |
| ESPN win probability ≥ 2% | 43 | 1 | +117% | -68% | -64% | -80% |
| ESPN win probability ≥ 5% | 18 | 1 | +419% | -81% | -71% | -76% |
| ESPN win probability ≥ 10% | 12 | 1 | +678% | -71% | -57% | -64% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 918 | 15% | 10% | 7% | 4% | 1% | 1% |
| Unverified | 10224 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 6 | 1% | -$53.70 | -39% |
| Sell at 2¢ | 135 | 15% | -$102.60 | -75% |
| Sell at 3¢ | 94 | 10% | -$101.04 | -73% |
| Sell at 5¢ | 64 | 7% | -$96.10 | -70% |
| Sell at 10¢ | 34 | 4% | -$93.16 | -68% |
| Sell at 25¢ | 13 | 1% | -$94.67 | -69% |
| Sell at 50¢ | 9 | 1% | -$76.95 | -56% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 3005 | 0 | 0% | 0% | -100% | -100% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 563 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Counter-Strike 2 Game | ✘ | 548 | 1 | 4% | 3% | -83% | -93% | 11 min |
| ITF Men's Match | ✘ | 476 | 1 | 9% | 5% | -80% | -84% | 5 min |
| Challenger ATP  | ✘ | 378 | 2 | 8% | 2% | -51% | -85% | 5 min |
| eBasketball Game | ✘ | 315 | 1 | 0% | 0% | -70% | -70% | 1 min |
| TT Star Series Match | ✘ | 237 | 1 | 2% | 2% | -61% | -96% | 4 min |
| College Football Game | partly | 188 | 2 | 13% | 6% | -1% | -78% | 31 min |
| Darts Match | ✘ | 170 | 0 | 1% | 1% | -100% | -99% | 9 min |
| Women's College Volleyball Match | ✘ | 156 | 2 | 7% | 3% | +20% | -88% | 105 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Men's T20 Cricket Match | ✘ | 125 | 1 | 14% | 4% | -25% | -76% | 21 min |
| League of Legends Game | ✘ | 123 | 0 | 7% | 2% | -100% | -89% | 11 min |
| Serie C Game | ✘ | 111 | 1 | 5% | 2% | -16% | -92% | 6 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Challenger WTA | ✘ | 106 | 0 | 12% | 7% | -100% | -79% | 8 min |
| NHL Game | ✔ | 87 | 0 | 15% | 7% | -100% | -74% | 5 min |
| Dota 2 Game | ✘ | 81 | 0 | 2% | 2% | -100% | -96% | 29 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| AHL Game | ✘ | 59 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Brasileiro Serie B Game | ✘ | 58 | 0 | 5% | 2% | -100% | -91% | 10 min |
| R6 Game | ✘ | 55 | 0 | 5% | 2% | -100% | -91% | 9 min |
| Ettan Game | ✘ | 53 | 0 | 8% | 2% | -100% | -87% | 5 min |
| KHL Game | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 5 min |
| Argentina Primera Division Game | ✘ | 51 | 0 | 16% | 6% | -100% | -73% | 8 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| KBO Game | ✘ | 49 | 0 | 8% | 6% | -100% | -86% | 5 min |
| Argentine Nacional B Game | ✘ | 48 | 0 | 8% | 8% | -100% | -86% | 10 min |
| Overwatch Game | ✘ | 46 | 0 | 4% | 0% | -100% | -92% | 5 min |
| Liga DIMAYOR Game | ✘ | 45 | 1 | 11% | 4% | +107% | -81% | 6 min |
| LaLiga 2 Game | partly | 44 | 0 | 16% | 7% | -100% | -72% | 8 min |
| USL Championship Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 6 min |
| Brasileiro Serie A Game | partly | 41 | 1 | 20% | 10% | +128% | -66% | 2 min |
| Liga Leumit Game | ✘ | 40 | 0 | 2% | 2% | -100% | -96% | 14 min |
| Japan J2 League Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 8 min |
| Major League Soccer Game | partly | 39 | 1 | 18% | 5% | +139% | -69% | 6 min |
| Uruguay Primera Division Game | ✘ | 38 | 0 | 8% | 5% | -100% | -86% | 10 min |
| ATP Tennis Match | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 3 min |
| National League Game | ✘ | 35 | 1 | 3% | 3% | +167% | -95% | 5 min |
| Eerste Divisie Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 11 min |
| LNBP Basketball Game | ✘ | 34 | 0 | 6% | 0% | -100% | -90% | 12 min |
| WTA Tennis Match | ✘ | 34 | 0 | 12% | 0% | -100% | -80% | 4 min |
| Slovakian 2. Liga Game | ✘ | 34 | 0 | 6% | 6% | -100% | -90% | 111 min |
| Liiga Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NBA Game | ✔ | 34 | 0 | 15% | 3% | -100% | -75% | 4 min |
| ELH Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liga Expansion Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 10 min |
| NFL Game | ✔ | 30 | 1 | 20% | 7% | +211% | -65% | 4 min |
| FIFA Women's Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 43 min |
| Euroleague Game | ✘ | 29 | 0 | 21% | 3% | -100% | -64% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| SHL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 5 min |
| DEL Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Japan NPB Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Valorant game winner | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 16 min |
| Chinese Basketball Association Game  | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Tweede Divisie Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| China League 1 Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Finland Korisliiga Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Peru Liga 1 Game | ✘ | 20 | 0 | 25% | 20% | -100% | -57% | 7 min |
| Italy Serie A2 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Japan J League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 12 min |
| German 3. Liga Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 7 min |
| Liga MX Game | ✔ | 19 | 0 | 16% | 16% | -100% | -73% | 1 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Adriatic ABA Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| TFF 1. Lig Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 8 min |
| Polish Ekstraklasa Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 11 min |
| Serie A Game | ✔ | 19 | 0 | 11% | 11% | -100% | -82% | 11 min |
| Professional Baseball Game | partly | 18 | 0 | 11% | 6% | -100% | -81% | 2 min |
| Bundesliga 2 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 8 min |
| Eredivisie Game | ✔ | 18 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Ligue 2 Game | ✘ | 18 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Ligue 1 Game | ✔ | 18 | 0 | 17% | 11% | -100% | -71% | 10 min |
| La Liga Game | ✔ | 18 | 0 | 44% | 33% | -100% | -23% | 9 min |
| Canadian Premier League | ✘ | 17 | 1 | 24% | 24% | +449% | -59% | 29 min |
| Spain Liga ACB Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 17 min |
| College Hockey Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australia NBL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 7 min |
| Czech NBL Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 11 min |
| LNB Elite Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| EFL League One Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 4 min |
| Italy Serie A Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 6 min |
| Korea K-League 2 Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 6 min |
| Indonesia Super League Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 10 min |
| Thai League 1 Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 7 min |
| Eliteserien Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 9 min |
| Turkish Super Lig Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 14 min |
| Serie B Game | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 15 min |
| Ecuador Liga Pro Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 6 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Men's ODI Cricket Match | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 20 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Chinese Super League Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 22 min |
| Czech National Football League Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 12 min |
| Czech First League Game | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 11 min |
| Allsvenskan Game | ✘ | 15 | 0 | 20% | 20% | -100% | -65% | 14 min |
| Brasileiro Serie C Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 5 min |
| APF Division de Honor Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 5 min |
| Austria BSL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Chile Liga de Primera Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 9 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Saudi Pro League Game | ✘ | 14 | 0 | 21% | 21% | -100% | -63% | 15 min |
| Bolivia Premier Division Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| English Premier League Game | ✔ | 14 | 0 | 7% | 7% | -100% | -88% | 7 min |
| Israeli Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Super League Greece Game | ✘ | 14 | 0 | 21% | 7% | -100% | -63% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| Women's Pro Basketball Game | ✔ | 13 | 0 | 23% | 8% | -100% | -60% | 6 min |
| Sweden SBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Turkey BSL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovakia SBL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Vietnam V-League 1 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Korea K League Game | ✘ | 12 | 0 | 42% | 17% | -100% | -28% | 14 min |
| Danish Superliga Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Serbian SuperLiga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Women's ODI Cricket Match | ✘ | 11 | 0 | 18% | 9% | -100% | -68% | 50 min |
| Croatia Premijer Liga Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Finnish Ykkosliiga Game | ✘ | 11 | 1 | 9% | 9% | +748% | -84% | 15 min |
| EFL Championship Game | ✔ | 11 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Russia VTB United Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 12 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Egyptian Premier League Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Women's T20 Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 17 min |
| LKL Lithuania Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Croatia HNL Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 16 min |
| Bundesliga Game | ✔ | 9 | 1 | 22% | 22% | +937% | -61% | 13 min |
| Latvian Virsliga Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 10 min |
| Slovenian Prva Liga Game | ✘ | 9 | 0 | 22% | 11% | -100% | -61% | 14 min |
| Slovenia 1. SKL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 11 min |
| England Super League Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Singapore Premier League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 17 min |
| AFC Champions League Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 10 min |
| Scottish Premiership Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 390 | 6% | 2% | 0% | -89% |
| 5–15 min | 185 | 18% | 6% | 2% | -69% |
| 15–30 min | 129 | 31% | 17% | 2% | -46% |
| 30–60 min | 112 | 16% | 10% | 0% | -72% |
| Over 60 min | 96 | 21% | 14% | 0% | -64% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 48 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-12 21:38 | Challenger ATP  | Santiago De la Fuente | ✘ | — | — | In play | — |
| 10-12 21:36 | eSoccer Game | Real Madrid (Kovboj) | ✘ | — | — | In play | — |
| 10-12 21:36 | eSoccer Game | Real Betis (Krocs) | ✘ | — | — | In play | — |
| 10-12 21:34 | eSoccer Game | Boca Juniors (Eder) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:34 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:33 | eSoccer Game | Universitario (Shaq) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:33 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:32 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:30 | eSoccer Game | Manchester Utd (Adri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:30 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:25 | ITF Women's Match | Shria Atturu | ✘ | — | — | In play | — |
| 10-12 21:22 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:22 | eSoccer Game | Sevilla FC (Zaroth) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:20 | Chile Liga de Primera Game | Tie | ✘ | — | — | In play | — |
| 10-12 21:20 | eSoccer Game | River Plate (Fede) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:20 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:19 | eSoccer Game | Boca Juniors (Eder) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:18 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:16 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:16 | eSoccer Game | Manchester Utd (Adri) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:16 | eBasketball Game | Dallas Mavericks (Ray) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:16 | eBasketball Game | Indiana Pacers (Jason) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:11 | ITF Women's Match | Diae El Jardi | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 10-12 21:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:09 | eSoccer Game | RCD Mallorca (Zaroth) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-12 21:09 | ITF Women's Match | Sara Shumate | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-12 21:09 | ITF Men's Match | Jefferson Wendler Filho | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
