# 1¢ Study

*Updated Sat Oct 24, 4:36 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 37 finished bets | 3% | $8.45 | +152% | +22.84¢ | $11.30 / -$2.85 |

*Expect about **2 buys a day**, roughly **$0.27/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 74 | $2.90 | +26% |
| ESPN win probability ≥ 5%, sell at 50¢ | 37 | $1.20 | +22% |
| ESPN win probability ≥ 5%, sell at 25¢ | 37 | $1.07 | +19% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 28590 | 1725 | 7 (0%) | 1.1% | -$160.75 (-62%) | Hold to the end: -$160.75 (-62%) |

*In play right now: 18. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 323 | 3.3% | 0.3% (1) | -75% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 323 | 1 | -71% | -73% | -73% | -70% |
| ESPN win probability ≥ 2% | 74 | 1 | +26% | -65% | -68% | -71% |
| ESPN win probability ≥ 5% | 37 | 1 | +152% | -77% | -79% | -77% |
| ESPN win probability ≥ 10% | 23 | 1 | +306% | -70% | -66% | -62% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1725 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 26847 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$160.75 | -62% |
| Sell at 2¢ | 242 | 14% | -$195.83 | -76% |
| Sell at 3¢ | 165 | 10% | -$194.40 | -75% |
| Sell at 5¢ | 114 | 7% | -$184.65 | -71% |
| Sell at 10¢ | 54 | 3% | -$188.01 | -73% |
| Sell at 25¢ | 16 | 1% | -$205.79 | -80% |
| Sell at 50¢ | 10 | 1% | -$191.25 | -74% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 12321 | 5 | 0% | 0% | -96% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Russia Liga Pro Match | ✘ | 1248 | 0 | 0% | 0% | -100% | -100% | 4 min |
| eBasketball Game | ✘ | 1227 | 1 | 1% | 0% | -92% | -91% | 2 min |
| ITF Women's Match | ✘ | 1076 | 2 | 13% | 5% | -83% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 997 | 2 | 5% | 3% | -81% | -91% | 11 min |
| ITF Men's Match | ✘ | 980 | 1 | 12% | 6% | -90% | -79% | 5 min |
| Challenger ATP  | ✘ | 643 | 2 | 11% | 4% | -71% | -81% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 275 | 2 | 13% | 7% | -32% | -77% | 23 min |
| Darts Match | ✘ | 249 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 230 | 2 | 6% | 3% | -19% | -89% | 73 min |
| Men's T20 Cricket Match | ✘ | 225 | 1 | 14% | 4% | -59% | -75% | 25 min |
| Dota 2 Game | ✘ | 202 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 184 | 2 | 5% | 3% | +1% | -92% | 7 min |
| eFootball Game | ✘ | 168 | 0 | 0% | 0% | -100% | -100% | 2 min |
| NHL Game | ✔ | 166 | 0 | 11% | 5% | -100% | -81% | 4 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 139 | 0 | 7% | 2% | -100% | -88% | 11 min |
| WTA Tennis Match | ✘ | 130 | 0 | 11% | 2% | -100% | -81% | 5 min |
| AHL Game | ✘ | 111 | 0 | 3% | 2% | -100% | -95% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| KHL Game | ✘ | 94 | 0 | 6% | 3% | -100% | -89% | 5 min |
| Argentina Primera Division Game | ✘ | 92 | 1 | 16% | 9% | +1% | -72% | 6 min |
| NBA Game | ✔ | 92 | 0 | 15% | 5% | -100% | -74% | 7 min |
| Brasileiro Serie B Game | ✘ | 90 | 0 | 8% | 3% | -100% | -87% | 9 min |
| Ettan Game | ✘ | 89 | 0 | 4% | 1% | -100% | -92% | 6 min |
| Japan J2 League Game | ✘ | 84 | 0 | 14% | 6% | -100% | -75% | 7 min |
| Liga DIMAYOR Game | ✘ | 83 | 1 | 10% | 4% | +12% | -83% | 6 min |
| ATP Tennis Match | ✘ | 81 | 0 | 15% | 7% | -100% | -74% | 4 min |
| Overwatch Game | ✘ | 80 | 0 | 2% | 0% | -100% | -96% | 5 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| R6 Game | ✘ | 72 | 0 | 8% | 3% | -100% | -86% | 9 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| Japan J League Game | ✘ | 70 | 0 | 17% | 7% | -100% | -70% | 13 min |
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
| College Hockey Game | ✘ | 60 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga MX Game | ✔ | 59 | 0 | 15% | 8% | -100% | -74% | 5 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| Valorant game winner | ✘ | 57 | 0 | 4% | 2% | -100% | -94% | 14 min |
| EFL Championship Game | ✔ | 57 | 0 | 11% | 5% | -100% | -82% | 9 min |
| EFL League One Game | ✔ | 56 | 0 | 11% | 4% | -100% | -81% | 11 min |
| ELH Game | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 5 min |
| Chinese Basketball Association Game  | ✘ | 55 | 0 | 5% | 2% | -100% | -91% | 10 min |
| TFF 1. Lig Game | ✘ | 55 | 0 | 18% | 11% | -100% | -68% | 10 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| Liga Expansion Game | ✘ | 53 | 0 | 6% | 4% | -100% | -90% | 10 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| DEL Game | ✘ | 51 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Mobile Legends Bang Bang Game | ✘ | 51 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Indonesia Super League Game | ✘ | 50 | 0 | 12% | 6% | -100% | -79% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| SHL Game | ✘ | 49 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Saudi Pro League Game | ✘ | 49 | 1 | 18% | 12% | +90% | -68% | 13 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Ligue 2 Game | ✘ | 46 | 0 | 13% | 9% | -100% | -77% | 8 min |
| China League 1 Game | ✘ | 45 | 0 | 9% | 4% | -100% | -85% | 9 min |
| NFL Game | ✔ | 45 | 1 | 22% | 9% | +107% | -61% | 4 min |
| LNB Elite 2 Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| NWSL Game | ✔ | 42 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Peru Liga 1 Game | ✘ | 42 | 0 | 14% | 10% | -100% | -75% | 10 min |
| La Liga Game | ✔ | 42 | 0 | 29% | 21% | -100% | -50% | 8 min |
| Czech National Football League Game | ✘ | 41 | 0 | 12% | 7% | -100% | -79% | 7 min |
| Polish Ekstraklasa Game | ✘ | 41 | 0 | 12% | 5% | -100% | -79% | 8 min |
| Serie A Game | ✔ | 41 | 0 | 7% | 7% | -100% | -87% | 12 min |
| Bundesliga 2 Game | ✔ | 40 | 0 | 15% | 8% | -100% | -74% | 7 min |
| Japan B League Game | ✘ | 40 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Serie B Game | ✘ | 38 | 0 | 16% | 8% | -100% | -73% | 9 min |
| Eredivisie Game | ✔ | 38 | 0 | 11% | 8% | -100% | -82% | 5 min |
| Ligue 1 Game | ✔ | 38 | 0 | 18% | 8% | -100% | -68% | 9 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Finland Korisliiga Game | ✘ | 36 | 1 | 6% | 6% | +159% | -90% | 9 min |
| Korea K-League 2 Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Turkish Super Lig Game | ✘ | 36 | 0 | 17% | 0% | -100% | -71% | 13 min |
| English Premier League Game | ✔ | 36 | 0 | 11% | 6% | -100% | -81% | 9 min |
| Allsvenskan Game | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 11 min |
| Ecuador Liga Pro Game | ✘ | 34 | 0 | 9% | 3% | -100% | -85% | 5 min |
| Serbian SuperLiga Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| APF Division de Honor Game | ✘ | 33 | 0 | 12% | 3% | -100% | -79% | 6 min |
| Adriatic ABA Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 10 min |
| Men's ODI Cricket Match | ✘ | 32 | 1 | 16% | 3% | +192% | -73% | 53 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
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
| Australia NBL Game | ✘ | 27 | 0 | 4% | 0% | -100% | -94% | 7 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Danish Superliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 11 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| LNB Elite Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Russia VTB United Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Serie A Femminile Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Czech NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 18 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Professional Baseball Game | partly | 21 | 0 | 14% | 10% | -100% | -75% | 2 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Latvian Virsliga Game | ✘ | 21 | 0 | 14% | 5% | -100% | -75% | 17 min |
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
| Korea KBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Romanian Liga I Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 8 min |
| Spanish Liga F Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 11 min |
| England Super League Basketball Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Australian A League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 5 min |
| Brazil NBB Basketball Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Women's ODI Cricket Match | ✘ | 15 | 0 | 20% | 7% | -100% | -65% | 61 min |
| Slovenia 1. SKL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 19 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| LKL Lithuania Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| CFL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Indian Super League Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 12 min |
| German Women's Bundesliga Game | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 28 min |
| Austrian Bundesliga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| Liga Nacional de Basquetbol Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Hungarian NB I Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| French Women's Première Ligue Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 5 min |
| BNXT League Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
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
| Under 5 min | 698 | 5% | 1% | 0% | -91% |
| 5–15 min | 392 | 17% | 7% | 1% | -70% |
| 15–30 min | 261 | 28% | 15% | 1% | -52% |
| 30–60 min | 194 | 19% | 11% | 0% | -67% |
| Over 60 min | 161 | 17% | 9% | 0% | -70% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 44 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-24 10:35 | eSoccer Game | Spain (Kate) | ✘ | — | — | In play | — |
| 10-24 10:35 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-24 10:35 | Russia Liga Pro Match | Kulikov Sergey | ✘ | — | — | In play | — |
| 10-24 10:34 | Australian A League Game | Melbourne City | ✘ | — | — | In play | — |
| 10-24 10:34 | Australian A League Game | Melbourne Victory | ✘ | — | — | In play | — |
| 10-24 10:31 | Russia Liga Pro Match | Konashkov Ilia | ✘ | — | — | In play | — |
| 10-24 10:30 | Valorant game winner | KeepBest Gaming | ✘ | — | — | In play | — |
| 10-24 10:30 | eBasketball Game | Golden State Warriors (Jordan) | ✘ | — | — | In play | — |
| 10-24 10:30 | eSoccer Game | Crystal Palace (Homie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:30 | eSoccer Game | Chelsea (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:26 | eSoccer Game | Frankfurt (Castle) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:26 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:26 | eSoccer Game | Freiburg (Kevin) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:26 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:25 | eSoccer Game | France (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:24 | eBasketball Game | New York Knicks (Kyle) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:23 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:22 | eSoccer Game | United States (Rose) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:21 | Russia Liga Pro Match | Grishaev Evgeny | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:21 | Overwatch Game | Solus Victorem | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:21 | Counter-Strike 2 Game | 9INE Academy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:21 | Dota 2 Game | 1win | ✘ | — | — | In play | — |
| 10-24 10:21 | Counter-Strike 2 Game | Ryvex | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:21 | eFootball Game | Atlanta (Pablo) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:20 | Indonesia Super League Game | Adhyaksa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:20 | Indonesia Super League Game | Yogyakarta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:19 | Counter-Strike 2 Game | Aurora Gaming | ✘ | — | — | In play | — |
| 10-24 10:14 | eSoccer Game | Everton (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:14 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 10:11 | Russia Liga Pro Match | Abanokov Zalimgeri | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
