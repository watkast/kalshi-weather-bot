# 1¢ Study

*Updated Thu Nov 5, 7:58 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 49 finished bets | 2% | $6.65 | +90% | +13.57¢ | $10.40 / -$3.75 |

*Expect about **1 buys a day**, roughly **$0.22/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 49 | -$0.60 | -8% |
| ESPN win probability ≥ 5%, sell at 25¢ | 49 | -$0.73 | -10% |
| ESPN win probability ≥ 2%, hold to the end | 114 | -$3.10 | -18% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 49088 | 2710 | 11 (0%) | 1.1% | -$252.50 (-62%) | Hold to the end: -$252.50 (-62%) |

*In play right now: 43. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 543 | 2.9% | 0.2% (1) | -94% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 543 | 1 | -83% | -71% | -70% | -71% |
| ESPN win probability ≥ 2% | 114 | 1 | -18% | -60% | -64% | -70% |
| ESPN win probability ≥ 5% | 49 | 1 | +90% | -79% | -79% | -82% |
| ESPN win probability ≥ 10% | 32 | 1 | +192% | -73% | -68% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2710 | 14% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 46335 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 11 | 0% | -$252.50 | -62% |
| Sell at 2¢ | 366 | 14% | -$311.34 | -77% |
| Sell at 3¢ | 257 | 9% | -$306.27 | -75% |
| Sell at 5¢ | 176 | 6% | -$292.10 | -72% |
| Sell at 10¢ | 78 | 3% | -$304.32 | -75% |
| Sell at 25¢ | 29 | 1% | -$310.51 | -76% |
| Sell at 50¢ | 19 | 1% | -$278.25 | -68% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 22801 | 12 | 1% | 0% | -95% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2671 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 2241 | 3 | 2% | 1% | -88% | -93% | 2 min |
| ITF Women's Match | ✘ | 1606 | 6 | 14% | 6% | -65% | -77% | 4 min |
| ITF Men's Match | ✘ | 1521 | 3 | 13% | 6% | -82% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1439 | 2 | 6% | 3% | -87% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 920 | 3 | 11% | 4% | -70% | -82% | 5 min |
| eFootball Game | ✘ | 625 | 2 | 1% | 1% | -70% | -98% | 2 min |
| College Football Game | partly | 412 | 3 | 12% | 6% | -32% | -79% | 24 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Men's T20 Cricket Match | ✘ | 319 | 2 | 16% | 7% | -41% | -73% | 23 min |
| Women's College Volleyball Match | ✘ | 312 | 2 | 5% | 3% | -40% | -92% | 66 min |
| Dota 2 Game | ✘ | 294 | 1 | 1% | 1% | -68% | -98% | 31 min |
| Serie C Game | ✘ | 285 | 2 | 5% | 2% | -35% | -92% | 6 min |
| Challenger WTA | ✘ | 275 | 1 | 13% | 4% | -66% | -77% | 9 min |
| NHL Game | ✔ | 258 | 2 | 14% | 7% | -28% | -75% | 5 min |
| Women's College Basketball Game | partly | 194 | 0 | 10% | 5% | -100% | -82% | 43 min |
| Major League Soccer Game | partly | 187 | 1 | 12% | 6% | -50% | -80% | 8 min |
| Men's College Basketball Game | partly | 186 | 2 | 17% | 8% | +0% | -70% | 43 min |
| NBA Game | ✔ | 181 | 0 | 18% | 6% | -100% | -69% | 9 min |
| WTA Tennis Match | ✘ | 179 | 0 | 12% | 2% | -100% | -80% | 5 min |
| AHL Game | ✘ | 172 | 0 | 4% | 2% | -100% | -93% | 5 min |
| League of Legends Game | ✘ | 158 | 0 | 8% | 2% | -100% | -87% | 11 min |
| Argentina Primera Division Game | ✘ | 149 | 2 | 15% | 9% | +25% | -74% | 7 min |
| Ettan Game | ✘ | 145 | 0 | 3% | 1% | -100% | -94% | 7 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| Japan J2 League Game | ✘ | 141 | 1 | 11% | 4% | -34% | -82% | 6 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| KHL Game | ✘ | 134 | 0 | 4% | 2% | -100% | -92% | 6 min |
| Liga DIMAYOR Game | ✘ | 133 | 1 | 11% | 3% | -30% | -82% | 7 min |
| Brasileiro Serie B Game | ✘ | 129 | 1 | 8% | 4% | -28% | -87% | 9 min |
| ATP Tennis Match | ✘ | 129 | 0 | 16% | 6% | -100% | -73% | 4 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| EFL Championship Game | ✔ | 124 | 0 | 8% | 5% | -100% | -86% | 10 min |
| College Hockey Game | ✘ | 122 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Brasileiro Serie A Game | partly | 118 | 1 | 11% | 7% | -21% | -81% | 9 min |
| Overwatch Game | ✘ | 116 | 0 | 2% | 0% | -100% | -97% | 6 min |
| EFL League One Game | ✔ | 112 | 0 | 9% | 3% | -100% | -85% | 10 min |
| USL Championship Game | partly | 110 | 0 | 12% | 5% | -100% | -80% | 5 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Japan J League Game | ✘ | 101 | 1 | 15% | 6% | -8% | -74% | 13 min |
| LaLiga 2 Game | partly | 100 | 1 | 17% | 8% | -7% | -71% | 8 min |
| Liiga Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| German 3. Liga Game | ✘ | 95 | 0 | 12% | 5% | -100% | -80% | 7 min |
| Serie B Game | ✘ | 95 | 0 | 13% | 6% | -100% | -78% | 10 min |
| Serie A Game | ✔ | 94 | 0 | 9% | 4% | -100% | -85% | 12 min |
| EuroCup Basketball Game | ✘ | 92 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Liga MX Game | ✔ | 91 | 0 | 15% | 9% | -100% | -73% | 6 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Valorant game winner | ✘ | 88 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Peru Liga 1 Game | ✘ | 88 | 0 | 14% | 7% | -100% | -76% | 12 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Eerste Divisie Game | ✘ | 87 | 0 | 9% | 6% | -100% | -84% | 10 min |
| TFF 1. Lig Game | ✘ | 86 | 0 | 14% | 8% | -100% | -76% | 10 min |
| Women's T20 Match | ✘ | 85 | 0 | 16% | 5% | -100% | -71% | 28 min |
| Liga Expansion Game | ✘ | 83 | 0 | 6% | 2% | -100% | -90% | 12 min |
| Slovakian 2. Liga Game | ✘ | 82 | 0 | 6% | 5% | -100% | -89% | 78 min |
| Indonesia Super League Game | ✘ | 82 | 0 | 15% | 9% | -100% | -75% | 9 min |
| Uruguay Primera Division Game | ✘ | 80 | 0 | 8% | 2% | -100% | -87% | 10 min |
| R6 Game | ✘ | 80 | 1 | 10% | 5% | +17% | -83% | 9 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| Euroleague Game | ✘ | 80 | 0 | 21% | 6% | -100% | -63% | 13 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| La Liga Game | ✔ | 78 | 0 | 18% | 12% | -100% | -69% | 9 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| Japan B League Game | ✘ | 75 | 0 | 7% | 0% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| English Premier League Game | ✔ | 73 | 0 | 7% | 3% | -100% | -88% | 9 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 72 | 1 | 18% | 7% | +30% | -69% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Ligue 2 Game | ✘ | 72 | 0 | 8% | 6% | -100% | -86% | 8 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Men's ODI Cricket Match | ✘ | 71 | 3 | 21% | 7% | +294% | -63% | 51 min |
| Polish Ekstraklasa Game | ✘ | 69 | 0 | 13% | 7% | -100% | -77% | 9 min |
| Allsvenskan Game | ✘ | 69 | 1 | 16% | 10% | +35% | -72% | 10 min |
| NWSL Game | ✔ | 68 | 0 | 7% | 1% | -100% | -87% | 7 min |
| APF Division de Honor Game | ✘ | 65 | 0 | 17% | 5% | -100% | -71% | 11 min |
| Bundesliga 2 Game | ✔ | 65 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Korea K-League 2 Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 7 min |
| Eliteserien Game | ✘ | 64 | 0 | 9% | 5% | -100% | -84% | 10 min |
| Turkish Super Lig Game | ✘ | 64 | 0 | 14% | 3% | -100% | -76% | 13 min |
| Ecuador Liga Pro Game | ✘ | 64 | 0 | 6% | 2% | -100% | -89% | 10 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Bundesliga Game | ✔ | 63 | 1 | 16% | 10% | +48% | -72% | 7 min |
| LNBP Basketball Game | ✘ | 62 | 0 | 10% | 2% | -100% | -83% | 12 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Eredivisie Game | ✔ | 62 | 0 | 10% | 8% | -100% | -83% | 5 min |
| Ligue 1 Game | ✔ | 62 | 0 | 16% | 6% | -100% | -72% | 9 min |
| Czech First League Game | ✘ | 61 | 0 | 10% | 0% | -100% | -83% | 9 min |
| Italy Serie A2 Game | ✘ | 60 | 0 | 2% | 0% | -100% | -97% | 6 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Czech National Football League Game | ✘ | 59 | 0 | 12% | 7% | -100% | -79% | 8 min |
| LNB Elite 2 Game | ✘ | 58 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Bolivia Premier Division Game | ✘ | 58 | 0 | 9% | 2% | -100% | -85% | 5 min |
| Thai League 1 Game | ✘ | 56 | 0 | 18% | 7% | -100% | -69% | 11 min |
| KBO Game | ✘ | 55 | 0 | 11% | 5% | -100% | -81% | 5 min |
| FIBA Europe Cup Game | ✘ | 55 | 0 | 9% | 4% | -100% | -84% | 11 min |
| Liga Portugal Game | ✘ | 54 | 0 | 6% | 2% | -100% | -90% | 11 min |
| Israeli Premier League Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 8 min |
| Finland Korisliiga Game | ✘ | 52 | 1 | 8% | 4% | +79% | -87% | 8 min |
| England Women's Super League Game | ✘ | 52 | 0 | 17% | 8% | -100% | -70% | 23 min |
| Belgian Pro League Game | ✘ | 52 | 0 | 8% | 0% | -100% | -87% | 15 min |
| Serbian SuperLiga Game | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 12 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Super League Greece Game | ✘ | 49 | 0 | 20% | 4% | -100% | -65% | 12 min |
| Vietnam V-League 1 Game | ✘ | 48 | 1 | 6% | 4% | +94% | -89% | 10 min |
| Korea K League Game | ✘ | 48 | 1 | 15% | 8% | +94% | -75% | 7 min |
| Chile Liga de Primera Game | ✘ | 47 | 0 | 11% | 2% | -100% | -82% | 11 min |
| Serie A Femminile Game | ✘ | 47 | 0 | 2% | 2% | -100% | -96% | 8 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Adriatic ABA Game | ✘ | 46 | 1 | 7% | 4% | +103% | -89% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 46 | 0 | 20% | 11% | -100% | -66% | 5 min |
| Spanish Liga F Game | ✘ | 45 | 0 | 7% | 4% | -100% | -88% | 7 min |
| Scottish Premiership Game | ✘ | 44 | 0 | 11% | 2% | -100% | -80% | 10 min |
| Rugby French 14 Match | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Spain Liga ACB Game | ✘ | 43 | 0 | 7% | 2% | -100% | -88% | 17 min |
| Brazil NBB Basketball Game | ✘ | 43 | 0 | 7% | 5% | -100% | -88% | 18 min |
| LNB Elite Game | ✘ | 42 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Danish Superliga Game | ✘ | 41 | 0 | 10% | 5% | -100% | -83% | 10 min |
| Romanian Liga I Game | ✘ | 41 | 0 | 10% | 2% | -100% | -83% | 9 min |
| Australia NBL Game | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 8 min |
| Czech NBL Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 17 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Italy Serie A Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Croatia HNL Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 8 min |
| Sweden SBL Game | ✘ | 37 | 0 | 5% | 5% | -100% | -91% | 14 min |
| Bundesliga Basketball Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 13 min |
| Latvian Virsliga Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 21 min |
| Slovenian Prva Liga Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Indian Super League Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 8 min |
| Qatar Stars League | ✘ | 36 | 0 | 8% | 3% | -100% | -86% | 7 min |
| Canadian Premier League | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 22 min |
| Swiss Super League Game | ✘ | 35 | 1 | 6% | 3% | +167% | -90% | 12 min |
| Korea KBL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Hungarian NB I Game | ✘ | 34 | 0 | 9% | 9% | -100% | -85% | 6 min |
| Austria BSL Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Turkey BSL Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Australian A League Game | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 6 min |
| Austrian Bundesliga Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 12 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Russia VTB United Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 15 min |
| EFL Trophy Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 47 min |
| FIBA Champions League Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Croatia Premijer Liga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eredivisie Vrouwen Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 8 min |
| Liga Nacional de Basquetbol Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 6 min |
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| England Super League Basketball Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakian Cup Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 18 min |
| Slovakia SBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 18 min |
| French Women's Première Ligue Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| BNXT League Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 11 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| Slovenia 1. SKL Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 13 min |
| LKL Lithuania Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Women's ODI Cricket Match | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 61 min |
| Men's Iceland Basketball Premier League Game | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 9 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| CFL Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 9 min |
| Malaysia Super League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 9 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Philippines PBA Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Colombia LBP Basketball Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 17 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Israel Super League Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 14 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Bundesliga Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| GBL Basketball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 35 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Copa do Brasil Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 15 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Hungary NB I. A Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1031 | 4% | 1% | 0% | -93% |
| 5–15 min | 639 | 16% | 8% | 1% | -72% |
| 15–30 min | 429 | 24% | 13% | 1% | -58% |
| 30–60 min | 322 | 21% | 11% | 1% | -64% |
| Over 60 min | 261 | 19% | 10% | 0% | -67% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 38 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11-06 02:58 | Liga Expansion Game | Cancun FC | ✘ | — | — | In play | — |
| 11-06 02:58 | Women's College Basketball Game | Pepperdine | ✘ | — | — | In play | — |
| 11-06 02:56 | eSoccer Game | Universitario (Frenkie) | ✘ | — | — | In play | — |
| 11-06 02:56 | eSoccer Game | Botafogo (Luis) | ✘ | — | — | In play | — |
| 11-06 02:55 | NHL Game | Utah | ✔ | 4:30 - OT · UTA 4 - MTL 4 | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:54 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-06 02:54 | eSoccer Game | Estudiantes (Hazard) | ✘ | — | — | In play | — |
| 11-06 02:54 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-06 02:53 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-06 02:52 | Women's College Basketball Game | Northwestern | ✘ | — | — | In play | — |
| 11-06 02:52 | NHL Game | Dallas | ✔ | In SO · DAL 1 - CBJ 1 | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:52 | eSoccer Game | Olympique de Marseille (Maddy) | ✘ | — | — | In play | — |
| 11-06 02:52 | eSoccer Game | Paris Saint-Germain (Kate) | ✘ | — | — | In play | — |
| 11-06 02:51 | Women's College Basketball Game | Morehead St. | ✘ | — | — | In play | — |
| 11-06 02:49 | Liga Nacional de Basquetbol Game | Independiente de Oliva | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:48 | Women's College Basketball Game | Wagner | ✘ | — | — | In play | — |
| 11-06 02:47 | Women's College Basketball Game | Sam Houston | ✘ | — | — | In play | — |
| 11-06 02:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:44 | NHL Game | Detroit | ✔ | 0:29 - 3rd · VGK 2 - DET 1 | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:42 | Men's College Basketball Game | Tulane | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:42 | Women's College Volleyball Match | Southern California | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:41 | NHL Game | New York I | ✔ | 0:49 - 3rd · CAR 4 - NYI 3 | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:41 | Men's College Basketball Game | South Alabama | ✘ | — | — | In play | — |
| 11-06 02:41 | Women's College Basketball Game | Grambling St. | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:40 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:39 | eSoccer Game | Manchester City (Drakon) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:39 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:39 | eSoccer Game | Paris Saint-Germain (Kate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:34 | eSoccer Game | Olympique de Marseille (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 02:33 | eBasketball Game | Indiana Pacers (Walt) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
