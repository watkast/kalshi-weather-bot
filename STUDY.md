# 1¢ Study

*Updated Fri Nov 20, 4:03 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 71 finished bets | 1% | $3.35 | +31% | +4.72¢ | $8.75 / -$5.40 |

*Expect about **1 buys a day**, roughly **$0.22/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 71 | -$3.90 | -37% |
| ESPN win probability ≥ 5%, sell at 25¢ | 71 | -$4.03 | -38% |
| ESPN win probability ≥ 5%, sell at 10¢ | 71 | -$8.03 | -75% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 68847 | 3683 | 14 (0%) | 1.1% | -$356.45 (-65%) | Hold to the end: -$356.45 (-65%) |

*In play right now: 33. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 962 | 2.5% | 0.1% (1) | -213% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 962 | 1 | -90% | -71% | -71% | -71% |
| ESPN win probability ≥ 2% | 179 | 1 | -48% | -59% | -61% | -66% |
| ESPN win probability ≥ 5% | 71 | 1 | +31% | -80% | -85% | -88% |
| ESPN win probability ≥ 10% | 47 | 1 | +99% | -78% | -78% | -82% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 3683 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 65131 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 14 | 0% | -$356.45 | -65% |
| Sell at 2¢ | 527 | 14% | -$415.43 | -75% |
| Sell at 3¢ | 369 | 10% | -$408.54 | -74% |
| Sell at 5¢ | 251 | 7% | -$389.30 | -70% |
| Sell at 10¢ | 103 | 3% | -$417.52 | -76% |
| Sell at 25¢ | 39 | 1% | -$423.36 | -77% |
| Sell at 50¢ | 25 | 1% | -$383.70 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 33102 | 22 | 1% | 1% | -94% | -98% | 3 min |
| Russia Liga Pro Match | ✘ | 4266 | 0 | 2% | 1% | -100% | -97% | 4 min |
| eBasketball Game | ✘ | 3272 | 8 | 3% | 2% | -77% | -91% | 3 min |
| ITF Women's Match | ✘ | 2019 | 8 | 14% | 6% | -63% | -76% | 4 min |
| ITF Men's Match | ✘ | 1976 | 5 | 14% | 6% | -76% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1840 | 3 | 6% | 3% | -85% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 1250 | 5 | 12% | 5% | -63% | -79% | 5 min |
| Men's College Basketball Game | partly | 804 | 5 | 20% | 8% | -42% | -66% | 26 min |
| Women's College Basketball Game | partly | 787 | 2 | 15% | 5% | -76% | -74% | 32 min |
| College Football Game | partly | 636 | 3 | 11% | 5% | -56% | -81% | 23 min |
| eFootball Game | ✘ | 625 | 2 | 1% | 1% | -70% | -98% | 2 min |
| Darts Match | ✘ | 463 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Dota 2 Game | ✘ | 432 | 1 | 1% | 1% | -78% | -98% | 32 min |
| Women's College Volleyball Match | ✘ | 426 | 2 | 4% | 2% | -56% | -93% | 51 min |
| Men's T20 Cricket Match | ✘ | 408 | 2 | 15% | 6% | -54% | -75% | 26 min |
| Serie C Game | ✘ | 393 | 2 | 5% | 3% | -53% | -91% | 8 min |
| NHL Game | ✔ | 353 | 3 | 16% | 9% | -21% | -73% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Challenger WTA | ✘ | 306 | 1 | 12% | 4% | -69% | -78% | 9 min |
| NBA Game | partly | 277 | 0 | 19% | 7% | -100% | -67% | 11 min |
| AHL Game | ✘ | 261 | 0 | 4% | 2% | -100% | -93% | 6 min |
| Major League Soccer Game | partly | 221 | 1 | 11% | 5% | -58% | -80% | 8 min |
| College Hockey Game | ✘ | 219 | 0 | 1% | 0% | -100% | -98% | 13 min |
| UEFA Nations League Game | ✔ | 215 | 0 | 13% | 7% | -100% | -78% | 10 min |
| WTA Tennis Match | ✘ | 198 | 0 | 12% | 3% | -100% | -79% | 5 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| KHL Game | ✘ | 175 | 0 | 3% | 2% | -100% | -94% | 6 min |
| Argentina Primera Division Game | ✘ | 175 | 2 | 17% | 9% | +7% | -71% | 9 min |
| Liga DIMAYOR Game | ✘ | 173 | 1 | 10% | 3% | -46% | -82% | 9 min |
| Japan J2 League Game | ✘ | 173 | 1 | 10% | 4% | -46% | -83% | 7 min |
| League of Legends Game | ✘ | 164 | 0 | 7% | 2% | -100% | -87% | 11 min |
| Brasileiro Serie B Game | ✘ | 162 | 1 | 7% | 3% | -42% | -87% | 10 min |
| Valorant game winner | ✘ | 160 | 0 | 4% | 2% | -100% | -94% | 10 min |
| Argentine Nacional B Game | ✘ | 156 | 0 | 8% | 5% | -100% | -87% | 8 min |
| CONCACAF Nations League Game | partly | 156 | 2 | 20% | 8% | +20% | -66% | 20 min |
| ATP Tennis Match | ✘ | 153 | 0 | 16% | 7% | -100% | -73% | 4 min |
| English National League Game | ✘ | 149 | 1 | 8% | 6% | -37% | -86% | 10 min |
| EFL Championship Game | ✔ | 149 | 1 | 9% | 5% | -37% | -85% | 9 min |
| Women's T20 Match | ✘ | 141 | 0 | 16% | 5% | -100% | -73% | 28 min |
| Brasileiro Serie A Game | partly | 140 | 1 | 12% | 7% | -33% | -79% | 9 min |
| Overwatch Game | ✘ | 132 | 0 | 2% | 0% | -100% | -97% | 6 min |
| LaLiga 2 Game | partly | 131 | 1 | 18% | 8% | -29% | -70% | 9 min |
| Liiga Game | ✘ | 125 | 0 | 0% | 0% | -100% | -100% | 6 min |
| EFL League One Game | ✔ | 122 | 0 | 8% | 2% | -100% | -86% | 10 min |
| R6 Game | ✘ | 121 | 1 | 10% | 4% | -23% | -83% | 8 min |
| Eerste Divisie Game | ✘ | 121 | 0 | 8% | 4% | -100% | -86% | 12 min |
| USL Championship Game | partly | 120 | 0 | 11% | 4% | -100% | -81% | 5 min |
| Japan J League Game | ✘ | 119 | 1 | 16% | 7% | -22% | -72% | 12 min |
| Japan B League Game | ✘ | 119 | 0 | 8% | 1% | -100% | -87% | 13 min |
| German 3. Liga Game | ✘ | 115 | 0 | 11% | 4% | -100% | -80% | 10 min |
| Serie B Game | ✘ | 115 | 0 | 10% | 5% | -100% | -82% | 9 min |
| Peru Liga 1 Game | ✘ | 114 | 0 | 16% | 7% | -100% | -73% | 14 min |
| Serie A Game | ✔ | 112 | 0 | 10% | 5% | -100% | -83% | 12 min |
| Liga MX Game | ✔ | 110 | 0 | 14% | 8% | -100% | -76% | 7 min |
| AFCON Game Winner | ✘ | 109 | 1 | 17% | 6% | -14% | -71% | 20 min |
| EuroCup Basketball Game | ✘ | 109 | 0 | 5% | 4% | -100% | -92% | 11 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| International Friendly Game | partly | 106 | 1 | 16% | 5% | -12% | -72% | 17 min |
| National League Game | ✘ | 102 | 1 | 1% | 1% | -8% | -98% | 6 min |
| NFL Game | ✔ | 101 | 1 | 18% | 7% | -8% | -69% | 9 min |
| Liga Expansion Game | ✘ | 101 | 0 | 6% | 3% | -100% | -90% | 12 min |
| Slovakian 2. Liga Game | ✘ | 100 | 0 | 5% | 4% | -100% | -91% | 44 min |
| Euroleague Game | ✘ | 100 | 0 | 20% | 6% | -100% | -65% | 12 min |
| TFF 1. Lig Game | ✘ | 100 | 0 | 12% | 7% | -100% | -79% | 11 min |
| ELH Game | ✘ | 99 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Indonesia Super League Game | ✘ | 99 | 0 | 12% | 7% | -100% | -79% | 12 min |
| Men's ODI Cricket Match | ✘ | 95 | 3 | 20% | 8% | +195% | -65% | 56 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| Tweede Divisie Game | ✘ | 94 | 0 | 1% | 0% | -100% | -98% | 7 min |
| La Liga Game | ✔ | 94 | 0 | 18% | 12% | -100% | -69% | 8 min |
| English Premier League Game | ✔ | 94 | 1 | 9% | 4% | -1% | -85% | 10 min |
| Uruguay Primera Division Game | ✘ | 93 | 0 | 12% | 5% | -100% | -79% | 10 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| Italy Serie A2 Game | ✘ | 90 | 1 | 2% | 1% | +4% | -96% | 6 min |
| Ligue 2 Game | ✘ | 90 | 0 | 8% | 6% | -100% | -87% | 12 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Polish Ekstraklasa Game | ✘ | 87 | 0 | 11% | 7% | -100% | -80% | 12 min |
| SHL Game | ✘ | 86 | 0 | 3% | 2% | -100% | -94% | 6 min |
| DEL Game | ✘ | 86 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Copa Del Rey Game | ✘ | 85 | 0 | 6% | 5% | -100% | -90% | 40 min |
| Mobile Legends Bang Bang Game | ✘ | 81 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Allsvenskan Game | ✘ | 81 | 1 | 14% | 9% | +15% | -76% | 13 min |
| Bundesliga Game | ✔ | 81 | 1 | 17% | 9% | +15% | -70% | 9 min |
| Korea K-League 2 Game | ✘ | 80 | 0 | 11% | 6% | -100% | -80% | 9 min |
| Ligue 1 Game | ✔ | 80 | 0 | 15% | 6% | -100% | -74% | 9 min |
| NWSL Game | ✔ | 79 | 0 | 6% | 1% | -100% | -89% | 7 min |
| APF Division de Honor Game | ✘ | 79 | 0 | 16% | 4% | -100% | -71% | 13 min |
| Eliteserien Game | ✘ | 79 | 0 | 10% | 4% | -100% | -82% | 17 min |
| Saudi Pro League Game | ✘ | 78 | 2 | 18% | 12% | +139% | -69% | 13 min |
| Turkish Super Lig Game | ✘ | 78 | 0 | 18% | 4% | -100% | -69% | 17 min |
| Ecuador Liga Pro Game | ✘ | 78 | 0 | 6% | 1% | -100% | -89% | 11 min |
| FIBA Europe Cup Game | ✘ | 78 | 0 | 6% | 3% | -100% | -89% | 9 min |
| Bundesliga 2 Game | ✔ | 77 | 0 | 14% | 6% | -100% | -75% | 8 min |
| Eredivisie Game | ✔ | 76 | 0 | 9% | 7% | -100% | -84% | 5 min |
| Czech First League Game | ✘ | 75 | 0 | 8% | 0% | -100% | -86% | 12 min |
| LNB Elite 2 Game | ✘ | 74 | 0 | 1% | 0% | -100% | -98% | 6 min |
| Bolivia Premier Division Game | ✘ | 74 | 0 | 8% | 1% | -100% | -86% | 11 min |
| England Women's Super League Game | ✘ | 73 | 0 | 14% | 5% | -100% | -76% | 22 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Brazil NBB Basketball Game | ✘ | 71 | 0 | 7% | 3% | -100% | -88% | 18 min |
| Czech National Football League Game | ✘ | 70 | 0 | 11% | 6% | -100% | -80% | 10 min |
| Thai League 1 Game | ✘ | 68 | 0 | 16% | 7% | -100% | -72% | 15 min |
| Belgian Pro League Game | ✘ | 68 | 0 | 7% | 0% | -100% | -87% | 19 min |
| Israeli Premier League Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 13 min |
| LNBP Basketball Game | ✘ | 67 | 0 | 10% | 3% | -100% | -82% | 12 min |
| Serie A Femminile Game | ✘ | 67 | 1 | 6% | 4% | +39% | -90% | 13 min |
| Liga Portugal Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Spanish Liga F Game | ✘ | 66 | 0 | 11% | 8% | -100% | -82% | 10 min |
| Finland Korisliiga Game | ✘ | 65 | 1 | 6% | 3% | +44% | -89% | 9 min |
| Chile Liga de Primera Game | ✘ | 63 | 0 | 13% | 2% | -100% | -78% | 14 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Super League Greece Game | ✘ | 63 | 0 | 17% | 3% | -100% | -70% | 14 min |
| Vietnam V-League 1 Game | ✘ | 62 | 1 | 5% | 3% | +51% | -92% | 11 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| Serbian SuperLiga Game | ✘ | 62 | 0 | 3% | 2% | -100% | -94% | 15 min |
| Adriatic ABA Game | ✘ | 61 | 1 | 7% | 3% | +53% | -89% | 9 min |
| Korea K League Game | ✘ | 60 | 1 | 15% | 8% | +56% | -74% | 8 min |
| Spain Liga ACB Game | ✘ | 58 | 0 | 7% | 3% | -100% | -88% | 14 min |
| Romanian Liga I Game | ✘ | 58 | 1 | 14% | 5% | +61% | -76% | 13 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| LNB Elite Game | ✘ | 57 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Czech NBL Game | ✘ | 56 | 0 | 2% | 0% | -100% | -97% | 15 min |
| Scottish Premiership Game | ✘ | 56 | 0 | 9% | 2% | -100% | -85% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 56 | 0 | 18% | 11% | -100% | -69% | 7 min |
| Australia NBL Game | ✘ | 54 | 0 | 7% | 6% | -100% | -87% | 10 min |
| Champions League Women's Game | partly | 54 | 1 | 20% | 9% | +73% | -65% | 26 min |
| Taca de Portugal Game | ✘ | 54 | 0 | 17% | 6% | -100% | -71% | 14 min |
| Italy Serie A Game | ✘ | 53 | 0 | 4% | 2% | -100% | -93% | 7 min |
| Liga Nacional de Basquetbol Game | ✘ | 53 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Qatar Stars League | ✘ | 53 | 0 | 13% | 8% | -100% | -77% | 10 min |
| Bundesliga Basketball Game | ✘ | 52 | 0 | 8% | 4% | -100% | -87% | 13 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Korea KBL Game | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Sweden SBL Game | ✘ | 49 | 0 | 6% | 6% | -100% | -89% | 14 min |
| Danish Superliga Game | ✘ | 49 | 0 | 10% | 6% | -100% | -82% | 13 min |
| French Women's Première Ligue Game | ✘ | 49 | 0 | 10% | 8% | -100% | -82% | 14 min |
| Austria BSL Game | ✘ | 47 | 0 | 6% | 4% | -100% | -89% | 8 min |
| Croatia HNL Game | ✘ | 47 | 0 | 9% | 4% | -100% | -85% | 11 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| Slovenian Prva Liga Game | ✘ | 45 | 0 | 9% | 2% | -100% | -85% | 12 min |
| Swiss Super League Game | ✘ | 45 | 1 | 4% | 2% | +107% | -92% | 7 min |
| Turkey BSL Game | ✘ | 44 | 0 | 2% | 2% | -100% | -96% | 9 min |
| Indian Super League Game | ✘ | 44 | 0 | 14% | 7% | -100% | -76% | 10 min |
| Hungarian NB I Game | ✘ | 44 | 0 | 7% | 7% | -100% | -88% | 9 min |
| Russia VTB United Game | ✘ | 42 | 0 | 5% | 0% | -100% | -92% | 16 min |
| Australian A League Game | ✘ | 42 | 0 | 10% | 2% | -100% | -83% | 11 min |
| German Women's Bundesliga Game | ✘ | 42 | 0 | 5% | 2% | -100% | -92% | 28 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Austrian Bundesliga Game | ✘ | 40 | 0 | 8% | 5% | -100% | -87% | 14 min |
| Canadian Premier League | ✘ | 39 | 1 | 15% | 13% | +139% | -73% | 17 min |
| EFL Trophy Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 46 min |
| FIBA Champions League Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 10 min |
| BNXT League Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 11 min |
| Eredivisie Vrouwen Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 8 min |
| England Super League Basketball Game | ✘ | 37 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Slovakia SBL Game | ✘ | 36 | 0 | 3% | 0% | -100% | -95% | 15 min |
| Croatia Premijer Liga Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Polish Hockey Game | ✘ | 34 | 0 | 3% | 3% | -100% | -95% | 7 min |
| LKL Lithuania Game | ✘ | 33 | 0 | 3% | 0% | -100% | -95% | 9 min |
| UAE Pro League | ✘ | 32 | 0 | 6% | 6% | -100% | -89% | 17 min |
| Ligue Magnus Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 7 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Slovenia 1. SKL Game | ✘ | 31 | 0 | 3% | 3% | -100% | -94% | 15 min |
| EuroBasket (W) Game | ✘ | 31 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Slovakian Cup Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| Women's ODI Cricket Match | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 40 min |
| Men's Iceland Basketball Premier League Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 7 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Colombia LBP Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 15 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Malaysia Super League Game | ✘ | 20 | 0 | 10% | 0% | -100% | -83% | 9 min |
| Liga Portugal 2 Game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 16 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Powerslap Match Winner | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 6 min |
| Philippines PBA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Israel Super League Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 12 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Coupe de France Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 141 min |
| EFL League Two Game | ✔ | 16 | 0 | 12% | 12% | -100% | -78% | 5 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| RAF Match Result | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 2840 min |
| Champions League Hockey | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's Bundesliga Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Slovakia Niké liga Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 21 min |
| Ukraine SuperLeague Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 7 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| SAFF Championship Game | ✘ | 10 | 0 | 30% | 10% | -100% | -48% | 31 min |
| Scottish Women Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| GBL Basketball Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Uruguay LUB Basketball Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 7 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Bare Knuckle Fight Match | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 27 min |
| Liga MX Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Poland PLK Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Australia A League Women Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 5 min |
| Scottish Championship Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 28 min |
| Slovenian Cup Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 23 min |
| Lithuania NKL Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 287 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Portugal LPB Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Bulgaria First League Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 34 min |
| USL Super League Women Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 46 min |
| Japan J League Cup Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NBL Australia (W) Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Romania Division A Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 27 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Ukrainian Premier League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Latvian-Estonian Basketball League Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Paraguay Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serbian Cup Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 12 min |
| T10 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Mexican Pacific League | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Womens TGL Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 51 min |
| Bosnia Division I Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 428 min |
| China CBA (W) Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Puerto Rico BSN (W) Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Hungary NB I. A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| UEFA Women Europa Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Argentina Super Cup Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 16 min |
| Dominican Winter League (LIDOM) | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 47 min |
| Argentina Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 24 min |
| USL League One Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 12 min |
| Peru League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 87 min |
| England Women League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 109 min |
| Padel Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Korea KBL (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Europe Adriatic League 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Israel National League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Women's PPL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Turkey TBL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 22 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1300 | 4% | 1% | 0% | -93% |
| 5–15 min | 834 | 16% | 8% | 1% | -72% |
| 15–30 min | 595 | 25% | 12% | 1% | -57% |
| 30–60 min | 454 | 20% | 12% | 1% | -64% |
| Over 60 min | 471 | 22% | 10% | 0% | -62% |

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
| 11-20 23:03 | Women's College Basketball Game | New Haven | ✘ | — | — | In play | — |
| 11-20 23:03 | Darts Match | Laura Turner | ✘ | — | — | In play | — |
| 11-20 23:03 | eSoccer Game | Real Betis (Strudl) | ✘ | — | — | In play | — |
| 11-20 23:03 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-20 23:02 | Men's College Basketball Game | South Dakota St. | ✘ | — | — | In play | — |
| 11-20 23:02 | Russia Liga Pro Match | Zemit Igor | ✘ | — | — | In play | — |
| 11-20 23:02 | Counter-Strike 2 Game | paiN Academy | ✘ | — | — | In play | — |
| 11-20 23:02 | Counter-Strike 2 Game | BakS eSports | ✘ | — | — | In play | — |
| 11-20 22:59 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-20 22:58 | eSoccer Game | Chelsea (Olive) | ✘ | — | — | In play | — |
| 11-20 22:58 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-20 22:57 | Challenger ATP  | Duncan Chan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:54 | eSoccer Game | Spurs (Mei) | ✘ | — | — | In play | — |
| 11-20 22:51 | Russia Liga Pro Match | Chernov Vyacheslav | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:49 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:48 | Brazil NBB Basketball Game | Fortaleza Basquete Cearense | ✘ | — | — | In play | — |
| 11-20 22:47 | eBasketball Game | Indiana Pacers (Wemby) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:46 | eSoccer Game | RCD Mallorca (Strudl) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:46 | eBasketball Game | Dallas Mavericks (Lonzo) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:45 | eSoccer Game | Spurs (Mei) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:45 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:45 | eSoccer Game | Universitario (Rooney) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:44 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:43 | Chile Liga de Primera Game | Tie | ✘ | — | — | In play | — |
| 11-20 22:43 | Taca de Portugal Game | Reg Time: Porto | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:42 | eSoccer Game | Palmeiras (Endrick) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-20 22:42 | Dota 2 Game | Team Allied | ✘ | — | — | In play | — |
| 11-20 22:41 | Russia Liga Pro Match | CHagaev Aleksei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
