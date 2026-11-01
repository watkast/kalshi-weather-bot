# 1¢ Study

*Updated Sun Nov 1, 10:12 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 44 finished bets | 2% | $7.40 | +112% | +16.82¢ | $10.70 / -$3.30 |

*Expect about **2 buys a day**, roughly **$0.23/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 44 | $0.15 | +2% |
| ESPN win probability ≥ 5%, sell at 25¢ | 44 | $0.02 | +0% |
| ESPN win probability ≥ 2%, hold to the end | 94 | -$0.10 | -1% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 43335 | 2395 | 9 (0%) | 1.1% | -$233.25 (-65%) | Hold to the end: -$233.25 (-65%) |

*In play right now: 39. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 437 | 3.0% | 0.2% (1) | -85% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 437 | 1 | -79% | -71% | -70% | -70% |
| ESPN win probability ≥ 2% | 94 | 1 | -1% | -59% | -64% | -72% |
| ESPN win probability ≥ 5% | 44 | 1 | +112% | -76% | -76% | -80% |
| ESPN win probability ≥ 10% | 29 | 1 | +222% | -70% | -64% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2395 | 13% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 40901 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 9 | 0% | -$233.25 | -65% |
| Sell at 2¢ | 323 | 13% | -$275.27 | -77% |
| Sell at 3¢ | 224 | 9% | -$271.89 | -76% |
| Sell at 5¢ | 155 | 6% | -$258.50 | -72% |
| Sell at 10¢ | 71 | 3% | -$266.24 | -74% |
| Sell at 25¢ | 24 | 1% | -$279.81 | -78% |
| Sell at 50¢ | 16 | 1% | -$251.25 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 19664 | 12 | 1% | 1% | -94% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 2380 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1930 | 3 | 2% | 1% | -85% | -92% | 2 min |
| ITF Women's Match | ✘ | 1421 | 6 | 13% | 5% | -61% | -77% | 4 min |
| ITF Men's Match | ✘ | 1342 | 2 | 13% | 5% | -86% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1315 | 2 | 6% | 3% | -86% | -90% | 12 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 822 | 2 | 11% | 4% | -77% | -82% | 5 min |
| eFootball Game | ✘ | 504 | 2 | 1% | 1% | -63% | -98% | 2 min |
| College Football Game | partly | 410 | 3 | 12% | 6% | -32% | -80% | 24 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Men's T20 Cricket Match | ✘ | 295 | 1 | 16% | 6% | -68% | -73% | 23 min |
| Women's College Volleyball Match | ✘ | 288 | 2 | 5% | 3% | -35% | -91% | 70 min |
| Serie C Game | ✘ | 267 | 2 | 4% | 2% | -30% | -92% | 6 min |
| Dota 2 Game | ✘ | 263 | 1 | 1% | 1% | -65% | -98% | 31 min |
| Challenger WTA | ✘ | 239 | 0 | 13% | 5% | -100% | -78% | 9 min |
| NHL Game | ✔ | 225 | 1 | 14% | 7% | -59% | -76% | 5 min |
| Major League Soccer Game | partly | 175 | 1 | 11% | 6% | -47% | -80% | 6 min |
| WTA Tennis Match | ✘ | 175 | 0 | 11% | 2% | -100% | -80% | 5 min |
| League of Legends Game | ✘ | 156 | 0 | 6% | 2% | -100% | -89% | 11 min |
| AHL Game | ✘ | 155 | 0 | 4% | 2% | -100% | -93% | 5 min |
| NBA Game | ✔ | 149 | 0 | 17% | 5% | -100% | -70% | 9 min |
| Ettan Game | ✘ | 143 | 0 | 3% | 1% | -100% | -94% | 7 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Argentine Nacional B Game | ✘ | 138 | 0 | 9% | 6% | -100% | -85% | 8 min |
| Argentina Primera Division Game | ✘ | 131 | 2 | 16% | 10% | +42% | -72% | 7 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| KHL Game | ✘ | 127 | 0 | 5% | 2% | -100% | -92% | 6 min |
| ATP Tennis Match | ✘ | 120 | 0 | 14% | 6% | -100% | -75% | 4 min |
| Japan J2 League Game | ✘ | 120 | 0 | 11% | 4% | -100% | -81% | 6 min |
| College Hockey Game | ✘ | 118 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liga DIMAYOR Game | ✘ | 117 | 1 | 9% | 3% | -20% | -85% | 6 min |
| Brasileiro Serie B Game | ✘ | 115 | 1 | 8% | 4% | -19% | -86% | 8 min |
| Overwatch Game | ✘ | 112 | 0 | 2% | 0% | -100% | -97% | 6 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| EFL League One Game | ✔ | 106 | 0 | 9% | 3% | -100% | -84% | 10 min |
| USL Championship Game | partly | 104 | 0 | 12% | 5% | -100% | -78% | 5 min |
| Brasileiro Serie A Game | partly | 102 | 1 | 12% | 7% | -8% | -80% | 7 min |
| Japan J League Game | ✘ | 101 | 1 | 15% | 6% | -8% | -74% | 13 min |
| EFL Championship Game | ✔ | 100 | 0 | 7% | 4% | -100% | -88% | 10 min |
| Liiga Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LaLiga 2 Game | partly | 94 | 1 | 18% | 9% | -1% | -69% | 8 min |
| German 3. Liga Game | ✘ | 91 | 0 | 11% | 5% | -100% | -81% | 7 min |
| Serie B Game | ✘ | 91 | 0 | 13% | 7% | -100% | -77% | 10 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Valorant game winner | ✘ | 88 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Serie A Game | ✔ | 88 | 0 | 9% | 5% | -100% | -84% | 12 min |
| Liga MX Game | ✔ | 87 | 0 | 15% | 9% | -100% | -74% | 6 min |
| Chinese Basketball Association Game  | ✘ | 85 | 0 | 7% | 1% | -100% | -88% | 10 min |
| TFF 1. Lig Game | ✘ | 84 | 0 | 14% | 8% | -100% | -75% | 10 min |
| Slovakian 2. Liga Game | ✘ | 82 | 0 | 6% | 5% | -100% | -89% | 78 min |
| Indonesia Super League Game | ✘ | 82 | 0 | 15% | 9% | -100% | -75% | 9 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| Eerste Divisie Game | ✘ | 79 | 0 | 10% | 6% | -100% | -82% | 8 min |
| Euroleague Game | ✘ | 78 | 0 | 21% | 6% | -100% | -64% | 13 min |
| Liga Expansion Game | ✘ | 77 | 0 | 6% | 3% | -100% | -89% | 10 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| EuroCup Basketball Game | ✘ | 76 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| Japan B League Game | ✘ | 75 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Peru Liga 1 Game | ✘ | 74 | 0 | 15% | 7% | -100% | -74% | 11 min |
| ELH Game | ✘ | 73 | 0 | 1% | 1% | -100% | -98% | 4 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Uruguay Primera Division Game | ✘ | 72 | 0 | 8% | 3% | -100% | -86% | 10 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| Women's T20 Match | ✘ | 70 | 0 | 14% | 6% | -100% | -75% | 25 min |
| La Liga Game | ✔ | 70 | 0 | 20% | 13% | -100% | -65% | 10 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| Mobile Legends Bang Bang Game | ✘ | 69 | 0 | 0% | 0% | -100% | -100% | 4 min |
| English Premier League Game | ✔ | 69 | 0 | 7% | 3% | -100% | -87% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| DEL Game | ✘ | 68 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Ligue 2 Game | ✘ | 68 | 0 | 9% | 6% | -100% | -85% | 8 min |
| Polish Ekstraklasa Game | ✘ | 67 | 0 | 13% | 7% | -100% | -77% | 8 min |
| Men's ODI Cricket Match | ✘ | 65 | 3 | 23% | 8% | +331% | -60% | 45 min |
| Bundesliga 2 Game | ✔ | 65 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Korea K-League 2 Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Turkish Super Lig Game | ✘ | 62 | 0 | 13% | 2% | -100% | -78% | 13 min |
| Allsvenskan Game | ✘ | 61 | 1 | 16% | 11% | +53% | -72% | 10 min |
| Bundesliga Game | ✔ | 61 | 1 | 15% | 8% | +53% | -74% | 7 min |
| Eredivisie Game | ✔ | 60 | 0 | 10% | 8% | -100% | -83% | 5 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| NFL Game | ✔ | 59 | 1 | 20% | 8% | +58% | -65% | 5 min |
| Czech National Football League Game | ✘ | 59 | 0 | 12% | 7% | -100% | -79% | 8 min |
| LNBP Basketball Game | ✘ | 58 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Ligue 1 Game | ✔ | 58 | 0 | 16% | 7% | -100% | -73% | 9 min |
| LNB Elite 2 Game | ✘ | 57 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Czech First League Game | ✘ | 57 | 0 | 9% | 0% | -100% | -85% | 9 min |
| Eliteserien Game | ✘ | 56 | 0 | 9% | 4% | -100% | -85% | 11 min |
| AFC Champions League Game | ✘ | 56 | 0 | 5% | 0% | -100% | -91% | 8 min |
| KBO Game | ✘ | 54 | 0 | 11% | 6% | -100% | -81% | 4 min |
| Thai League 1 Game | ✘ | 54 | 0 | 19% | 7% | -100% | -68% | 11 min |
| Ecuador Liga Pro Game | ✘ | 54 | 0 | 7% | 2% | -100% | -87% | 9 min |
| NWSL Game | ✔ | 52 | 0 | 10% | 2% | -100% | -83% | 7 min |
| England Women's Super League Game | ✘ | 52 | 0 | 17% | 8% | -100% | -70% | 23 min |
| Italy Serie A2 Game | ✘ | 52 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Bolivia Premier Division Game | ✘ | 52 | 0 | 10% | 2% | -100% | -83% | 5 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| APF Division de Honor Game | ✘ | 51 | 0 | 20% | 6% | -100% | -66% | 8 min |
| Serbian SuperLiga Game | ✘ | 50 | 0 | 4% | 2% | -100% | -93% | 12 min |
| Israeli Premier League Game | ✘ | 50 | 0 | 4% | 0% | -100% | -93% | 8 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Vietnam V-League 1 Game | ✘ | 48 | 1 | 6% | 4% | +94% | -89% | 10 min |
| Korea K League Game | ✘ | 48 | 1 | 15% | 8% | +94% | -75% | 7 min |
| Finland Korisliiga Game | ✘ | 47 | 1 | 9% | 4% | +99% | -85% | 9 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Belgian Pro League Game | ✘ | 46 | 0 | 9% | 0% | -100% | -85% | 12 min |
| Scottish Premiership Game | ✘ | 44 | 0 | 11% | 2% | -100% | -80% | 10 min |
| Venezuela Liga FUTVE game | ✘ | 44 | 0 | 20% | 11% | -100% | -65% | 6 min |
| Serie A Femminile Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Super League Greece Game | ✘ | 43 | 0 | 21% | 5% | -100% | -64% | 14 min |
| Adriatic ABA Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 11 min |
| Liga Portugal Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 10 min |
| Chile Liga de Primera Game | ✘ | 41 | 0 | 10% | 0% | -100% | -83% | 6 min |
| Rugby French 14 Match | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Spanish Liga F Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 7 min |
| Spain Liga ACB Game | ✘ | 40 | 0 | 8% | 2% | -100% | -87% | 16 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| LNB Elite Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Danish Superliga Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 8 min |
| FIBA Europe Cup Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Australia NBL Game | ✘ | 38 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Croatia HNL Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 8 min |
| Latvian Virsliga Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 21 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Sweden SBL Game | ✘ | 36 | 0 | 6% | 6% | -100% | -90% | 15 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Italy Serie A Game | ✘ | 36 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Qatar Stars League | ✘ | 36 | 0 | 8% | 3% | -100% | -86% | 7 min |
| Slovenian Prva Liga Game | ✘ | 35 | 0 | 6% | 3% | -100% | -90% | 6 min |
| Romanian Liga I Game | ✘ | 35 | 0 | 9% | 3% | -100% | -85% | 11 min |
| Czech NBL Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 17 min |
| Bundesliga Basketball Game | ✘ | 34 | 0 | 12% | 6% | -100% | -80% | 13 min |
| Brazil NBB Basketball Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Korea KBL Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Australian A League Game | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 6 min |
| Indian Super League Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 7 min |
| Hungarian NB I Game | ✘ | 32 | 0 | 9% | 9% | -100% | -84% | 6 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Canadian Premier League | ✘ | 31 | 1 | 16% | 16% | +201% | -72% | 23 min |
| Austria BSL Game | ✘ | 31 | 0 | 10% | 6% | -100% | -83% | 10 min |
| Turkey BSL Game | ✘ | 31 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Russia VTB United Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 14 min |
| Swiss Super League Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 15 min |
| Austrian Bundesliga Game | ✘ | 30 | 0 | 10% | 7% | -100% | -83% | 12 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Croatia Premijer Liga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Slovakia SBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 18 min |
| England Super League Basketball Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 7 min |
| French Women's Première Ligue Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| LKL Lithuania Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 9 min |
| BNXT League Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 11 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 14 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| FIBA Champions League Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Eredivisie Vrouwen Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 8 min |
| Liga Nacional de Basquetbol Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's ODI Cricket Match | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 61 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| CFL Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 9 min |
| Men's Iceland Basketball Premier League Game | ✘ | 18 | 0 | 22% | 11% | -100% | -61% | 11 min |
| Malaysia Super League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 9 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EuroLeague (W) Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 18 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Philippines PBA Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 10 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Israel Super League Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 8 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| GBL Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 3 | 0 | 33% | 33% | -100% | -42% | 48 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Denmark Basketligaen Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Hungary NB I. A Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's College Basketball Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 933 | 4% | 1% | 0% | -92% |
| 5–15 min | 566 | 17% | 7% | 1% | -71% |
| 15–30 min | 381 | 23% | 13% | 1% | -60% |
| 30–60 min | 289 | 20% | 11% | 0% | -66% |
| Over 60 min | 199 | 21% | 12% | 0% | -64% |

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
| 11-01 17:10 | Counter-Strike 2 Game | Acend | ✘ | — | — | In play | — |
| 11-01 17:10 | Men's T20 Cricket Match | Mississauga Skyhawks | ✘ | — | — | In play | — |
| 11-01 17:09 | Allsvenskan Game | Brommapojkarna | ✘ | — | — | In play | — |
| 11-01 17:09 | eSoccer Game | Freiburg (Kovboj) | ✘ | — | — | In play | — |
| 11-01 17:09 | eSoccer Game | Frankfurt (Mantis) | ✘ | — | — | In play | — |
| 11-01 17:09 | Challenger ATP  | Arklon Huertas Del Pino Cordova | ✘ | — | — | In play | — |
| 11-01 17:09 | Turkish Super Lig Game | Kasimpasa | ✘ | — | — | In play | — |
| 11-01 17:09 | Counter-Strike 2 Game | Misa Esports | ✘ | — | — | In play | — |
| 11-01 17:09 | Portugal LPB Game | Sporting Cp | ✘ | — | — | In play | — |
| 11-01 17:07 | Challenger WTA | Maria Jose Rico Sanchez | ✘ | — | — | In play | — |
| 11-01 17:07 | Liga Portugal Game | Nacional | ✘ | — | — | In play | — |
| 11-01 17:07 | Turkey BSL Game | Bursaspor | ✘ | — | — | In play | — |
| 11-01 17:06 | eSoccer Game | Sunderland (Ousmane) | ✘ | — | — | In play | — |
| 11-01 17:06 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-01 17:06 | eSoccer Game | Olympique de Marseille (Annie) | ✘ | — | — | In play | — |
| 11-01 17:06 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-01 17:05 | eSoccer Game | Chelsea (Elastico) | ✘ | — | — | In play | — |
| 11-01 17:05 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-01 17:04 | eSoccer Game | RC Lens (Florie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 17:04 | eSoccer Game | Paris Saint-Germain (Olive) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 17:00 | Chile Liga de Primera Game | Deportes La Serena | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 17:00 | LaLiga 2 Game | Tie | ✔ | 85' · RSG 2 - CEU 0 | — | In play | — |
| 11-01 17:00 | Challenger ATP  | Joshua Sheehy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 17:00 | Chile Liga de Primera Game | Huachipato | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 16:58 | Danish Superliga Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 16:57 | Danish Superliga Game | Nordsjaelland | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 16:57 | Men's College Basketball Game | Villanova | ✔ | 0:04 - 2nd · ND 73 - VILL 70 | 0¢ | ❌ Lost | -$0.15 |
| 11-01 16:57 | Ettan Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-01 16:56 | Dota 2 Game | Team Yandex | ✘ | — | — | In play | — |
| 11-01 16:56 | Scottish Cup Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
