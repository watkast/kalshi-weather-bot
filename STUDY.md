# 1¢ Study

*Updated Fri Oct 23, 7:51 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 33 finished bets | 3% | $9.05 | +183% | +27.42¢ | $11.60 / -$2.55 |

*Expect about **2 buys a day**, roughly **$0.25/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 69 | $3.65 | +35% |
| ESPN win probability ≥ 5%, sell at 50¢ | 33 | $1.80 | +36% |
| ESPN win probability ≥ 5%, sell at 25¢ | 33 | -$1.64 | -33% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 27995 | 1699 | 7 (0%) | 1.1% | -$156.85 (-62%) | Hold to the end: -$156.85 (-62%) |

*In play right now: 23. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 309 | 3.3% | 0.3% (1) | -68% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 309 | 1 | -70% | -75% | -76% | -73% |
| ESPN win probability ≥ 2% | 69 | 1 | +35% | -67% | -70% | -75% |
| ESPN win probability ≥ 5% | 33 | 1 | +183% | -84% | -84% | -87% |
| ESPN win probability ≥ 10% | 20 | 1 | +367% | -83% | -74% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1699 | 14% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 26273 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$156.85 | -62% |
| Sell at 2¢ | 235 | 14% | -$193.75 | -76% |
| Sell at 3¢ | 161 | 9% | -$192.06 | -75% |
| Sell at 5¢ | 111 | 7% | -$182.70 | -72% |
| Sell at 10¢ | 53 | 3% | -$185.42 | -73% |
| Sell at 25¢ | 15 | 1% | -$205.20 | -81% |
| Sell at 50¢ | 10 | 1% | -$187.35 | -74% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 11982 | 5 | 1% | 0% | -96% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Russia Liga Pro Match | ✘ | 1207 | 0 | 0% | 0% | -100% | -100% | 4 min |
| eBasketball Game | ✘ | 1199 | 1 | 1% | 0% | -92% | -91% | 2 min |
| ITF Women's Match | ✘ | 1073 | 2 | 14% | 5% | -83% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 991 | 2 | 5% | 3% | -81% | -91% | 11 min |
| ITF Men's Match | ✘ | 974 | 1 | 12% | 5% | -90% | -79% | 5 min |
| Challenger ATP  | ✘ | 641 | 2 | 11% | 4% | -71% | -82% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 270 | 2 | 13% | 7% | -31% | -78% | 24 min |
| Darts Match | ✘ | 249 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Men's T20 Cricket Match | ✘ | 223 | 1 | 14% | 4% | -58% | -75% | 25 min |
| Women's College Volleyball Match | ✘ | 223 | 2 | 6% | 3% | -16% | -89% | 73 min |
| Dota 2 Game | ✘ | 201 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 184 | 2 | 5% | 3% | +1% | -92% | 7 min |
| NHL Game | ✔ | 164 | 0 | 10% | 5% | -100% | -82% | 4 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| eFootball Game | ✘ | 148 | 0 | 0% | 0% | -100% | -100% | 2 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 138 | 0 | 7% | 2% | -100% | -87% | 11 min |
| WTA Tennis Match | ✘ | 119 | 0 | 11% | 3% | -100% | -81% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| AHL Game | ✘ | 104 | 0 | 3% | 2% | -100% | -95% | 5 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| KHL Game | ✘ | 94 | 0 | 6% | 3% | -100% | -89% | 5 min |
| Argentina Primera Division Game | ✘ | 90 | 1 | 17% | 9% | +4% | -71% | 6 min |
| Ettan Game | ✘ | 89 | 0 | 4% | 1% | -100% | -92% | 6 min |
| Brasileiro Serie B Game | ✘ | 88 | 0 | 7% | 2% | -100% | -88% | 9 min |
| NBA Game | ✔ | 84 | 0 | 12% | 4% | -100% | -79% | 8 min |
| Liga DIMAYOR Game | ✘ | 81 | 1 | 10% | 4% | +15% | -83% | 6 min |
| ATP Tennis Match | ✘ | 81 | 0 | 15% | 7% | -100% | -74% | 4 min |
| Japan J2 League Game | ✘ | 80 | 0 | 15% | 6% | -100% | -74% | 7 min |
| Overwatch Game | ✘ | 77 | 0 | 3% | 0% | -100% | -95% | 5 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| R6 Game | ✘ | 71 | 0 | 8% | 3% | -100% | -85% | 9 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| LaLiga 2 Game | partly | 68 | 0 | 21% | 9% | -100% | -64% | 8 min |
| Eerste Divisie Game | ✘ | 68 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Brasileiro Serie A Game | partly | 67 | 1 | 15% | 9% | +39% | -74% | 8 min |
| Liiga Game | ✘ | 66 | 0 | 0% | 0% | -100% | -100% | 5 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| National League Game | ✘ | 62 | 1 | 2% | 2% | +51% | -97% | 5 min |
| German 3. Liga Game | ✘ | 62 | 0 | 11% | 5% | -100% | -80% | 7 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Japan J League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 13 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Valorant game winner | ✘ | 57 | 0 | 4% | 2% | -100% | -94% | 14 min |
| EFL Championship Game | ✔ | 57 | 0 | 11% | 5% | -100% | -82% | 9 min |
| EFL League One Game | ✔ | 56 | 0 | 11% | 4% | -100% | -81% | 11 min |
| Liga MX Game | ✔ | 55 | 0 | 16% | 9% | -100% | -72% | 5 min |
| ELH Game | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 5 min |
| Chinese Basketball Association Game  | ✘ | 55 | 0 | 5% | 2% | -100% | -91% | 10 min |
| TFF 1. Lig Game | ✘ | 55 | 0 | 18% | 11% | -100% | -68% | 10 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| LNBP Basketball Game | ✘ | 52 | 0 | 6% | 0% | -100% | -90% | 12 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| DEL Game | ✘ | 51 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Expansion Game | ✘ | 51 | 0 | 6% | 4% | -100% | -90% | 10 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| College Hockey Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| SHL Game | ✘ | 49 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Mobile Legends Bang Bang Game | ✘ | 49 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Saudi Pro League Game | ✘ | 49 | 1 | 18% | 12% | +90% | -68% | 13 min |
| Indonesia Super League Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Ligue 2 Game | ✘ | 46 | 0 | 13% | 9% | -100% | -77% | 8 min |
| NFL Game | ✔ | 45 | 1 | 22% | 9% | +107% | -61% | 4 min |
| LNB Elite 2 Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| Peru Liga 1 Game | ✘ | 42 | 0 | 14% | 10% | -100% | -75% | 10 min |
| La Liga Game | ✔ | 42 | 0 | 29% | 21% | -100% | -50% | 8 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| Czech National Football League Game | ✘ | 41 | 0 | 12% | 7% | -100% | -79% | 7 min |
| Polish Ekstraklasa Game | ✘ | 41 | 0 | 12% | 5% | -100% | -79% | 8 min |
| Serie A Game | ✔ | 41 | 0 | 7% | 7% | -100% | -87% | 12 min |
| Bundesliga 2 Game | ✔ | 40 | 0 | 15% | 8% | -100% | -74% | 7 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Serie B Game | ✘ | 38 | 0 | 16% | 8% | -100% | -73% | 9 min |
| Eredivisie Game | ✔ | 38 | 0 | 11% | 8% | -100% | -82% | 5 min |
| Ligue 1 Game | ✔ | 38 | 0 | 18% | 8% | -100% | -68% | 9 min |
| NWSL Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Finland Korisliiga Game | ✘ | 36 | 1 | 6% | 6% | +159% | -90% | 9 min |
| Turkish Super Lig Game | ✘ | 36 | 0 | 17% | 0% | -100% | -71% | 13 min |
| English Premier League Game | ✔ | 36 | 0 | 11% | 6% | -100% | -81% | 9 min |
| Allsvenskan Game | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 11 min |
| Ecuador Liga Pro Game | ✘ | 34 | 0 | 9% | 3% | -100% | -85% | 5 min |
| Serbian SuperLiga Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| APF Division de Honor Game | ✘ | 33 | 0 | 12% | 3% | -100% | -79% | 6 min |
| Adriatic ABA Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 10 min |
| Japan B League Game | ✘ | 33 | 0 | 9% | 0% | -100% | -84% | 14 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
| Men's ODI Cricket Match | ✘ | 31 | 1 | 16% | 3% | +201% | -72% | 51 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Vietnam V-League 1 Game | ✘ | 29 | 1 | 10% | 7% | +222% | -82% | 10 min |
| Bundesliga Game | ✔ | 29 | 1 | 17% | 10% | +222% | -70% | 5 min |
| Sweden SBL Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 15 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Australia NBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 7 min |
| Danish Superliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 11 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| LNB Elite Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Russia VTB United Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Czech NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 18 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Bundesliga Basketball Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 12 min |
| Turkey BSL Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga Portugal Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 10 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| Qatar Stars League | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Croatia Premijer Liga Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Croatia HNL Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Austria BSL Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 6 min |
| Chile Liga de Primera Game | ✘ | 18 | 0 | 11% | 0% | -100% | -81% | 9 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Romanian Liga I Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 8 min |
| Spanish Liga F Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| England Super League Basketball Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Brazil NBB Basketball Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Women's ODI Cricket Match | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 61 min |
| Slovenia 1. SKL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 19 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| LKL Lithuania Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Korea KBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 6 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Indian Super League Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 12 min |
| German Women's Bundesliga Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 28 min |
| Austrian Bundesliga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 14 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Australian A League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 4 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| French Women's Première Ligue Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 5 min |
| BNXT League Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Liga Nacional de Basquetbol Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Polish Hockey Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 9 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EuroLeague (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Philippines PBA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Israel Super League Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 19 min |
| Ligue Magnus Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Ukraine SuperLeague Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 12 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Denmark Basketligaen Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 689 | 5% | 1% | 0% | -91% |
| 5–15 min | 385 | 17% | 7% | 1% | -70% |
| 15–30 min | 255 | 27% | 15% | 1% | -52% |
| 30–60 min | 193 | 19% | 11% | 0% | -68% |
| Over 60 min | 160 | 18% | 9% | 0% | -70% |

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
| 10-24 01:51 | College Hockey Game | Ferris State | ✘ | — | — | In play | — |
| 10-24 01:47 | CFL Game | Toronto Argonauts | ✘ | — | — | In play | — |
| 10-24 01:46 | eSoccer Game | Chelsea (Minjori) | ✘ | — | — | In play | — |
| 10-24 01:45 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-24 01:45 | College Hockey Game | Lake Superior State | ✘ | — | — | In play | — |
| 10-24 01:44 | NWSL Game | Chicago | ✔ | 76' · HOU 2 - CHI 0 | — | In play | — |
| 10-24 01:43 | NBA Game | New York | ✔ | 28.9 - 4th · NY 100 - BOS 106 | — | In play | — |
| 10-24 01:42 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:42 | eSoccer Game | Montpellier (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:40 | eSoccer Game | OL Lyonnes (Demi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:40 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:39 | AHL Game | Syracuse Crunch | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:39 | Russia Liga Pro Match | Korneev Dmitriy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:38 | College Hockey Game | Michigan State | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:36 | Russia Liga Pro Match | Zubov Aleksei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:35 | College Hockey Game | Western Michigan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:33 | NBA Game | Washington | ✔ | 2:48 - 4th · TOR 107 - WSH 97 | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:33 | Women's College Volleyball Match | Alabama | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:33 | AHL Game | Providence Bruins | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:31 | College Hockey Game | Robert Morris | ✘ | — | — | In play | — |
| 10-24 01:31 | eSoccer Game | Everton (Arkon) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:31 | Women's College Volleyball Match | Minnesota | ✘ | — | — | In play | — |
| 10-24 01:31 | eBasketball Game | Indiana Pacers (Dirk) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:28 | NBA Game | Indiana | ✔ | 5:42 - 4th · DAL 110 - IND 92 | — | In play | — |
| 10-24 01:28 | College Hockey Game | Canisius | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:27 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:27 | eSoccer Game | Montpellier (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:26 | eBasketball Game | Dallas Mavericks (Zach) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 01:26 | Women's College Volleyball Match | Maryland | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
