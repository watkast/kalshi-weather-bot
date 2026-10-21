# 1¢ Study

*Updated Wed Oct 21, 6:57 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 32 finished bets | 3% | $9.20 | +192% | +28.75¢ | $11.60 / -$2.40 |

*Expect about **2 buys a day**, roughly **$0.27/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 66 | $4.10 | +41% |
| ESPN win probability ≥ 5%, sell at 50¢ | 32 | $1.95 | +41% |
| ESPN win probability ≥ 5%, sell at 25¢ | 32 | -$1.49 | -31% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 23912 | 1547 | 7 (0%) | 1.1% | -$134.05 (-58%) | Hold to the end: -$134.05 (-58%) |

*In play right now: 25. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 287 | 3.3% | 0.3% (1) | -64% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 287 | 1 | -67% | -75% | -75% | -73% |
| ESPN win probability ≥ 2% | 66 | 1 | +41% | -66% | -68% | -74% |
| ESPN win probability ≥ 5% | 32 | 1 | +192% | -84% | -84% | -86% |
| ESPN win probability ≥ 10% | 19 | 1 | +391% | -82% | -73% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1547 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 22340 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$134.05 | -58% |
| Sell at 2¢ | 216 | 14% | -$175.89 | -76% |
| Sell at 3¢ | 148 | 10% | -$174.33 | -75% |
| Sell at 5¢ | 102 | 7% | -$165.75 | -71% |
| Sell at 10¢ | 51 | 3% | -$165.24 | -71% |
| Sell at 25¢ | 15 | 1% | -$182.40 | -79% |
| Sell at 50¢ | 10 | 1% | -$164.55 | -71% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 9714 | 5 | 0% | 0% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| eBasketball Game | ✘ | 977 | 1 | 0% | 0% | -90% | -90% | 2 min |
| ITF Women's Match | ✘ | 946 | 2 | 14% | 5% | -80% | -76% | 4 min |
| Russia Liga Pro Match | ✘ | 873 | 0 | 0% | 0% | -100% | -100% | 4 min |
| ITF Men's Match | ✘ | 872 | 1 | 12% | 6% | -89% | -79% | 5 min |
| Counter-Strike 2 Game | ✘ | 859 | 2 | 5% | 3% | -78% | -92% | 11 min |
| Challenger ATP  | ✘ | 608 | 2 | 11% | 4% | -69% | -81% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 265 | 2 | 13% | 7% | -30% | -77% | 24 min |
| Darts Match | ✘ | 241 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 208 | 2 | 6% | 3% | -10% | -89% | 74 min |
| Men's T20 Cricket Match | ✘ | 189 | 1 | 14% | 4% | -51% | -76% | 26 min |
| Dota 2 Game | ✘ | 180 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 174 | 2 | 5% | 3% | +7% | -91% | 8 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| NHL Game | ✔ | 150 | 0 | 11% | 5% | -100% | -80% | 4 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 134 | 0 | 7% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 99 | 1 | 11% | 4% | -6% | -81% | 6 min |
| AHL Game | ✘ | 95 | 0 | 3% | 2% | -100% | -95% | 5 min |
| WTA Tennis Match | ✘ | 93 | 0 | 11% | 2% | -100% | -81% | 5 min |
| Brasileiro Serie B Game | ✘ | 86 | 0 | 7% | 2% | -100% | -88% | 9 min |
| Argentina Primera Division Game | ✘ | 86 | 1 | 17% | 9% | +9% | -70% | 6 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| KHL Game | ✘ | 81 | 0 | 5% | 4% | -100% | -91% | 5 min |
| Japan J2 League Game | ✘ | 80 | 0 | 15% | 6% | -100% | -74% | 7 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| Overwatch Game | ✘ | 74 | 0 | 3% | 0% | -100% | -95% | 5 min |
| Liga DIMAYOR Game | ✘ | 73 | 1 | 10% | 3% | +28% | -83% | 6 min |
| USL Championship Game | partly | 68 | 0 | 13% | 3% | -100% | -77% | 5 min |
| NBA Game | ✔ | 67 | 0 | 12% | 3% | -100% | -79% | 6 min |
| ATP Tennis Match | ✘ | 66 | 0 | 12% | 5% | -100% | -79% | 3 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| LaLiga 2 Game | partly | 66 | 0 | 21% | 9% | -100% | -63% | 8 min |
| Brasileiro Serie A Game | partly | 65 | 1 | 15% | 9% | +44% | -73% | 8 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Japan J League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 13 min |
| German 3. Liga Game | ✘ | 60 | 0 | 12% | 5% | -100% | -80% | 7 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Liiga Game | ✘ | 58 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Leumit Game | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 138 min |
| National League Game | ✘ | 55 | 1 | 2% | 2% | +70% | -97% | 5 min |
| EFL Championship Game | ✔ | 55 | 0 | 9% | 5% | -100% | -84% | 8 min |
| UEFA Champions League Game | partly | 55 | 1 | 11% | 4% | +70% | -81% | 9 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| EFL League One Game | ✔ | 54 | 0 | 11% | 4% | -100% | -81% | 11 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| TFF 1. Lig Game | ✘ | 53 | 0 | 19% | 11% | -100% | -67% | 10 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Eerste Divisie Game | ✘ | 50 | 0 | 8% | 6% | -100% | -86% | 11 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| EuroCup Basketball Game | ✘ | 49 | 0 | 6% | 4% | -100% | -89% | 10 min |
| Liga Expansion Game | ✘ | 49 | 0 | 6% | 4% | -100% | -89% | 10 min |
| LNBP Basketball Game | ✘ | 48 | 0 | 6% | 0% | -100% | -89% | 14 min |
| ELH Game | ✘ | 48 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Liga MX Game | ✔ | 45 | 0 | 16% | 11% | -100% | -73% | 2 min |
| Mobile Legends Bang Bang Game | ✘ | 45 | 0 | 0% | 0% | -100% | -100% | 4 min |
| DEL Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 44 | 1 | 20% | 9% | +112% | -65% | 4 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| SHL Game | ✘ | 43 | 0 | 2% | 2% | -100% | -96% | 6 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Chinese Basketball Association Game  | ✘ | 43 | 0 | 2% | 0% | -100% | -96% | 10 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| Indonesia Super League Game | ✘ | 40 | 0 | 12% | 5% | -100% | -78% | 8 min |
| Saudi Pro League Game | ✘ | 39 | 1 | 18% | 13% | +139% | -69% | 11 min |
| Serie A Game | ✔ | 39 | 0 | 8% | 8% | -100% | -87% | 12 min |
| Peru Liga 1 Game | ✘ | 38 | 0 | 13% | 11% | -100% | -77% | 10 min |
| La Liga Game | ✔ | 38 | 0 | 29% | 21% | -100% | -50% | 8 min |
| LNB Elite 2 Game | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 7 min |
| Polish Ekstraklasa Game | ✘ | 37 | 0 | 11% | 3% | -100% | -81% | 9 min |
| NWSL Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 7 min |
| Valorant game winner | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| Serie B Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Eredivisie Game | ✔ | 36 | 0 | 11% | 8% | -100% | -81% | 4 min |
| Ligue 2 Game | ✘ | 36 | 0 | 17% | 11% | -100% | -71% | 7 min |
| Ligue 1 Game | ✔ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Turkish Super Lig Game | ✘ | 34 | 0 | 18% | 0% | -100% | -69% | 14 min |
| English Premier League Game | ✔ | 34 | 0 | 12% | 6% | -100% | -80% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
| Ecuador Liga Pro Game | ✘ | 32 | 0 | 9% | 3% | -100% | -84% | 6 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Czech National Football League Game | ✘ | 31 | 0 | 10% | 10% | -100% | -83% | 9 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Allsvenskan Game | ✘ | 31 | 0 | 13% | 13% | -100% | -78% | 12 min |
| Italy Serie A2 Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| APF Division de Honor Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 5 min |
| Adriatic ABA Game | ✘ | 29 | 0 | 3% | 3% | -100% | -94% | 10 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Japan B League Game | ✘ | 28 | 0 | 7% | 0% | -100% | -88% | 15 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Bundesliga Game | ✔ | 27 | 1 | 15% | 11% | +246% | -74% | 5 min |
| Serbian SuperLiga Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Egyptian Premier League Game | ✘ | 26 | 0 | 4% | 4% | -100% | -93% | 12 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Australia NBL Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 6 min |
| Men's ODI Cricket Match | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 31 min |
| LNB Elite Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Danish Superliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 9 min |
| Sweden SBL Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 14 min |
| eFootball Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovakian Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 20 min |
| Czech NBL Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Vietnam V-League 1 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Russia VTB United Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Faroe Islands Premier League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 131 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Turkey BSL Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Croatia HNL Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Austria BSL Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 6 min |
| Liga Portugal Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Croatia Premijer Liga Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Spanish Liga F Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Basketball Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Slovenia 1. SKL Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 17 min |
| LKL Lithuania Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| FIBA Europe Cup Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 10 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Romanian Liga I Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 5 min |
| Korea KBL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 9 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Indian Super League Game | ✘ | 12 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Qatar Stars League | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 4 min |
| German Women's Bundesliga Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 23 min |
| Austrian Bundesliga Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| FIBA Champions League Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Brazil NBB Basketball Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 10 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga Nacional de Basquetbol Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Colombia LBP Basketball Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| CONMEBOL Sudamericana Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Israel Super League Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 16 min |
| Philippines PBA Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Polish Hockey Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 639 | 5% | 1% | 0% | -91% |
| 5–15 min | 343 | 17% | 6% | 1% | -71% |
| 15–30 min | 228 | 29% | 16% | 1% | -50% |
| 30–60 min | 177 | 20% | 12% | 0% | -66% |
| Over 60 min | 144 | 18% | 10% | 0% | -69% |

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
| 10-21 12:57 | ITF Women's Match | Yasmin Ezzat | ✘ | — | — | In play | — |
| 10-21 12:54 | ITF Men's Match | Sebastian Sorger | ✘ | — | — | In play | — |
| 10-21 12:53 | Russia Liga Pro Match | Cheklin Mihail | ✘ | — | — | In play | — |
| 10-21 12:51 | Russia Liga Pro Match | SHipitsyn Gennadii | ✘ | — | — | In play | — |
| 10-21 12:51 | eSoccer Game | Manchester City (Mei) | ✘ | — | — | In play | — |
| 10-21 12:51 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-21 12:50 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:49 | eSoccer Game | Arsenal (Demi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:47 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:47 | eSoccer Game | Spurs (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:46 | eBasketball Game | Dallas Mavericks (Barry) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:45 | eBasketball Game | Indiana Pacers (Shaq) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:45 | eSoccer Game | Werder Bremen (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:45 | ITF Men's Match | Arthur Bellegy | ✘ | — | — | In play | — |
| 10-21 12:45 | ITF Women's Match | Marylee Longpre | ✘ | — | — | In play | — |
| 10-21 12:44 | Counter-Strike 2 Game | Saint Sinners | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:44 | eSoccer Game | Hoffenheim (Rendeto) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:44 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:44 | ITF Men's Match | Ruslan Serazhetdinov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:38 | Men's ODI Cricket Match | Denmark | ✘ | — | — | In play | — |
| 10-21 12:38 | Valorant game winner | Rare Atom | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:35 | ITF Men's Match | Saveliy Ivanov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:34 | eSoccer Game | Newcastle Utd (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:34 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:33 | ITF Women's Match | Eleejah Inisan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:31 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:31 | Russia Liga Pro Match | Safonov Vladimir | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:31 | eSoccer Game | FC Bayern (Nate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-21 12:29 | eSoccer Game | Werder Bremen (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
