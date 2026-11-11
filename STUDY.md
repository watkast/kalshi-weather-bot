# 1¢ Study

*Updated Wed Nov 11, 12:58 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 62 finished bets | 2% | $4.70 | +51% | +7.58¢ | $9.35 / -$4.65 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 62 | -$2.55 | -27% |
| ESPN win probability ≥ 5%, sell at 25¢ | 62 | -$2.68 | -29% |
| ESPN win probability ≥ 5%, sell at 10¢ | 62 | -$6.68 | -72% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 57345 | 3130 | 13 (0%) | 1.1% | -$287.50 (-61%) | Hold to the end: -$287.50 (-61%) |

*In play right now: 36. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 714 | 2.7% | 0.1% (1) | -171% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 714 | 1 | -87% | -70% | -71% | -73% |
| ESPN win probability ≥ 2% | 142 | 1 | -34% | -63% | -67% | -73% |
| ESPN win probability ≥ 5% | 62 | 1 | +51% | -83% | -83% | -86% |
| ESPN win probability ≥ 10% | 40 | 1 | +133% | -78% | -74% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 3130 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 54179 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 13 | 0% | -$287.50 | -61% |
| Sell at 2¢ | 440 | 14% | -$355.10 | -76% |
| Sell at 3¢ | 306 | 10% | -$350.16 | -75% |
| Sell at 5¢ | 206 | 7% | -$335.60 | -71% |
| Sell at 10¢ | 89 | 3% | -$352.91 | -75% |
| Sell at 25¢ | 34 | 1% | -$356.96 | -76% |
| Sell at 50¢ | 22 | 1% | -$321.00 | -68% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 27019 | 18 | 1% | 1% | -94% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 3325 | 0 | 1% | 0% | -100% | -98% | 4 min |
| eBasketball Game | ✘ | 2657 | 5 | 3% | 1% | -82% | -92% | 3 min |
| ITF Women's Match | ✘ | 1775 | 8 | 14% | 6% | -58% | -76% | 4 min |
| ITF Men's Match | ✘ | 1704 | 4 | 14% | 6% | -78% | -76% | 5 min |
| Counter-Strike 2 Game | ✘ | 1559 | 3 | 6% | 4% | -82% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 1025 | 5 | 11% | 4% | -54% | -81% | 5 min |
| eFootball Game | ✘ | 625 | 2 | 1% | 1% | -70% | -98% | 2 min |
| College Football Game | partly | 523 | 3 | 11% | 6% | -46% | -81% | 23 min |
| Men's College Basketball Game | partly | 429 | 5 | 20% | 7% | +9% | -66% | 30 min |
| Women's College Basketball Game | partly | 397 | 1 | 12% | 5% | -76% | -79% | 40 min |
| Darts Match | ✘ | 384 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's College Volleyball Match | ✘ | 361 | 2 | 4% | 2% | -48% | -93% | 66 min |
| Dota 2 Game | ✘ | 359 | 1 | 1% | 1% | -74% | -98% | 31 min |
| Men's T20 Cricket Match | ✘ | 339 | 2 | 16% | 7% | -45% | -72% | 22 min |
| Serie C Game | ✘ | 337 | 2 | 4% | 2% | -45% | -92% | 8 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| NHL Game | ✔ | 289 | 2 | 16% | 9% | -35% | -72% | 5 min |
| Challenger WTA | ✘ | 287 | 1 | 13% | 5% | -67% | -78% | 9 min |
| Major League Soccer Game | partly | 217 | 1 | 12% | 6% | -57% | -80% | 8 min |
| NBA Game | ✔ | 217 | 0 | 20% | 6% | -100% | -65% | 10 min |
| AHL Game | ✘ | 211 | 0 | 4% | 2% | -100% | -93% | 5 min |
| WTA Tennis Match | ✘ | 189 | 0 | 13% | 3% | -100% | -78% | 5 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| Argentina Primera Division Game | ✘ | 175 | 2 | 17% | 9% | +7% | -71% | 9 min |
| College Hockey Game | ✘ | 166 | 0 | 1% | 0% | -100% | -99% | 10 min |
| League of Legends Game | ✘ | 163 | 0 | 7% | 2% | -100% | -87% | 11 min |
| Japan J2 League Game | ✘ | 161 | 1 | 10% | 4% | -42% | -83% | 7 min |
| Liga DIMAYOR Game | ✘ | 153 | 1 | 11% | 3% | -39% | -81% | 9 min |
| EFL Championship Game | ✔ | 149 | 1 | 9% | 5% | -37% | -85% | 9 min |
| Brasileiro Serie B Game | ✘ | 147 | 1 | 7% | 3% | -37% | -87% | 10 min |
| ATP Tennis Match | ✘ | 147 | 0 | 16% | 7% | -100% | -73% | 4 min |
| KHL Game | ✘ | 146 | 0 | 4% | 2% | -100% | -93% | 6 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| Overwatch Game | ✘ | 127 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Valorant game winner | ✘ | 120 | 0 | 5% | 3% | -100% | -91% | 11 min |
| Brasileiro Serie A Game | partly | 120 | 1 | 11% | 7% | -22% | -81% | 9 min |
| Japan J League Game | ✘ | 119 | 1 | 16% | 7% | -22% | -72% | 12 min |
| USL Championship Game | partly | 118 | 0 | 11% | 4% | -100% | -81% | 5 min |
| R6 Game | ✘ | 115 | 1 | 10% | 4% | -19% | -83% | 8 min |
| Serie B Game | ✘ | 115 | 0 | 10% | 5% | -100% | -82% | 9 min |
| LaLiga 2 Game | partly | 114 | 1 | 18% | 8% | -18% | -70% | 9 min |
| German 3. Liga Game | ✘ | 113 | 0 | 11% | 4% | -100% | -82% | 10 min |
| EFL League One Game | ✔ | 112 | 0 | 9% | 3% | -100% | -85% | 10 min |
| Serie A Game | ✔ | 112 | 0 | 10% | 5% | -100% | -83% | 12 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Liga MX Game | ✔ | 108 | 0 | 14% | 8% | -100% | -76% | 7 min |
| Peru Liga 1 Game | ✘ | 106 | 0 | 17% | 8% | -100% | -71% | 14 min |
| Eerste Divisie Game | ✘ | 105 | 0 | 9% | 5% | -100% | -85% | 12 min |
| Women's T20 Match | ✘ | 103 | 0 | 17% | 5% | -100% | -70% | 27 min |
| Liiga Game | ✘ | 101 | 0 | 0% | 0% | -100% | -100% | 5 min |
| EuroCup Basketball Game | ✘ | 99 | 0 | 5% | 4% | -100% | -91% | 11 min |
| TFF 1. Lig Game | ✘ | 98 | 0 | 12% | 7% | -100% | -79% | 11 min |
| Slovakian 2. Liga Game | ✘ | 96 | 0 | 5% | 4% | -100% | -91% | 48 min |
| Indonesia Super League Game | ✘ | 96 | 0 | 12% | 7% | -100% | -78% | 12 min |
| Japan B League Game | ✘ | 96 | 0 | 8% | 1% | -100% | -86% | 12 min |
| Liga Expansion Game | ✘ | 95 | 0 | 6% | 3% | -100% | -89% | 13 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| La Liga Game | ✔ | 94 | 0 | 18% | 12% | -100% | -69% | 8 min |
| English Premier League Game | ✔ | 94 | 1 | 9% | 4% | -1% | -85% | 10 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Ligue 2 Game | ✘ | 90 | 0 | 8% | 6% | -100% | -87% | 12 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| NFL Game | ✔ | 87 | 1 | 17% | 7% | +7% | -70% | 8 min |
| Polish Ekstraklasa Game | ✘ | 85 | 0 | 12% | 7% | -100% | -80% | 12 min |
| Euroleague Game | ✘ | 83 | 0 | 22% | 6% | -100% | -62% | 13 min |
| Copa Del Rey Game | ✘ | 81 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Allsvenskan Game | ✘ | 81 | 1 | 14% | 9% | +15% | -76% | 13 min |
| Bundesliga Game | ✔ | 81 | 1 | 17% | 9% | +15% | -70% | 9 min |
| Uruguay Primera Division Game | ✘ | 80 | 0 | 8% | 2% | -100% | -87% | 10 min |
| Tweede Divisie Game | ✘ | 80 | 0 | 1% | 0% | -100% | -98% | 8 min |
| Korea K-League 2 Game | ✘ | 80 | 0 | 11% | 6% | -100% | -80% | 9 min |
| Ligue 1 Game | ✔ | 80 | 0 | 15% | 6% | -100% | -74% | 9 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's ODI Cricket Match | ✘ | 78 | 3 | 19% | 6% | +259% | -67% | 48 min |
| Eliteserien Game | ✘ | 78 | 0 | 10% | 4% | -100% | -82% | 16 min |
| Turkish Super Lig Game | ✘ | 78 | 0 | 18% | 4% | -100% | -69% | 17 min |
| APF Division de Honor Game | ✘ | 77 | 0 | 16% | 4% | -100% | -73% | 13 min |
| NWSL Game | ✔ | 76 | 0 | 7% | 1% | -100% | -89% | 7 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| Eredivisie Game | ✔ | 76 | 0 | 9% | 7% | -100% | -84% | 5 min |
| Ecuador Liga Pro Game | ✘ | 76 | 0 | 7% | 1% | -100% | -89% | 12 min |
| Czech First League Game | ✘ | 75 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Bolivia Premier Division Game | ✘ | 74 | 0 | 8% | 1% | -100% | -86% | 11 min |
| Mobile Legends Bang Bang Game | ✘ | 73 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Bundesliga 2 Game | ✔ | 73 | 0 | 15% | 7% | -100% | -74% | 8 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Italy Serie A2 Game | ✘ | 69 | 0 | 1% | 0% | -100% | -97% | 6 min |
| Thai League 1 Game | ✘ | 68 | 0 | 16% | 7% | -100% | -72% | 15 min |
| Belgian Pro League Game | ✘ | 68 | 0 | 7% | 0% | -100% | -87% | 19 min |
| Israeli Premier League Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 13 min |
| Liga Portugal Game | ✘ | 67 | 0 | 6% | 3% | -100% | -90% | 13 min |
| LNB Elite 2 Game | ✘ | 64 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Czech National Football League Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 9 min |
| LNBP Basketball Game | ✘ | 63 | 0 | 10% | 2% | -100% | -83% | 12 min |
| Chile Liga de Primera Game | ✘ | 63 | 0 | 13% | 2% | -100% | -78% | 14 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Super League Greece Game | ✘ | 63 | 0 | 17% | 3% | -100% | -70% | 14 min |
| England Women's Super League Game | ✘ | 62 | 0 | 15% | 6% | -100% | -75% | 23 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| Serbian SuperLiga Game | ✘ | 62 | 0 | 3% | 2% | -100% | -94% | 15 min |
| FIBA Europe Cup Game | ✘ | 62 | 0 | 8% | 3% | -100% | -86% | 10 min |
| Vietnam V-League 1 Game | ✘ | 60 | 1 | 5% | 3% | +56% | -91% | 11 min |
| Korea K League Game | ✘ | 60 | 1 | 15% | 8% | +56% | -74% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Finland Korisliiga Game | ✘ | 58 | 1 | 7% | 3% | +61% | -88% | 8 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Serie A Femminile Game | ✘ | 57 | 0 | 2% | 2% | -100% | -97% | 13 min |
| Scottish Premiership Game | ✘ | 56 | 0 | 9% | 2% | -100% | -85% | 11 min |
| Romanian Liga I Game | ✘ | 55 | 0 | 11% | 2% | -100% | -81% | 13 min |
| Spanish Liga F Game | ✘ | 55 | 0 | 7% | 5% | -100% | -87% | 12 min |
| Venezuela Liga FUTVE game | ✘ | 54 | 0 | 19% | 11% | -100% | -68% | 8 min |
| Brazil NBB Basketball Game | ✘ | 53 | 0 | 8% | 4% | -100% | -87% | 16 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Adriatic ABA Game | ✘ | 51 | 1 | 6% | 4% | +83% | -90% | 10 min |
| LNB Elite Game | ✘ | 50 | 0 | 2% | 0% | -100% | -97% | 9 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Spain Liga ACB Game | ✘ | 49 | 0 | 6% | 2% | -100% | -89% | 14 min |
| Danish Superliga Game | ✘ | 49 | 0 | 10% | 6% | -100% | -82% | 13 min |
| Czech NBL Game | ✘ | 47 | 0 | 2% | 0% | -100% | -96% | 16 min |
| Croatia HNL Game | ✘ | 47 | 0 | 9% | 4% | -100% | -85% | 11 min |
| Qatar Stars League | ✘ | 47 | 0 | 11% | 4% | -100% | -82% | 10 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Italy Serie A Game | ✘ | 46 | 0 | 4% | 2% | -100% | -92% | 6 min |
| Australia NBL Game | ✘ | 45 | 0 | 4% | 2% | -100% | -92% | 10 min |
| Bundesliga Basketball Game | ✘ | 45 | 0 | 9% | 4% | -100% | -85% | 13 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| Slovenian Prva Liga Game | ✘ | 45 | 0 | 9% | 2% | -100% | -85% | 12 min |
| Swiss Super League Game | ✘ | 45 | 1 | 4% | 2% | +107% | -92% | 7 min |
| Champions League Women's Game | partly | 44 | 1 | 20% | 9% | +112% | -65% | 26 min |
| Hungarian NB I Game | ✘ | 44 | 0 | 7% | 7% | -100% | -88% | 9 min |
| Korea KBL Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Sweden SBL Game | ✘ | 42 | 0 | 5% | 5% | -100% | -92% | 12 min |
| Australian A League Game | ✘ | 42 | 0 | 10% | 2% | -100% | -83% | 11 min |
| Indian Super League Game | ✘ | 42 | 0 | 14% | 7% | -100% | -75% | 9 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Austrian Bundesliga Game | ✘ | 40 | 0 | 8% | 5% | -100% | -87% | 14 min |
| Canadian Premier League | ✘ | 39 | 1 | 15% | 13% | +139% | -73% | 17 min |
| Turkey BSL Game | ✘ | 38 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Nacional de Basquetbol Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 6 min |
| Russia VTB United Game | ✘ | 37 | 0 | 5% | 0% | -100% | -91% | 16 min |
| Austria BSL Game | ✘ | 37 | 0 | 8% | 5% | -100% | -86% | 10 min |
| French Women's Première Ligue Game | ✘ | 37 | 0 | 8% | 5% | -100% | -86% | 13 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EFL Trophy Game | ✘ | 35 | 0 | 9% | 6% | -100% | -85% | 46 min |
| FIBA Champions League Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 10 min |
| German Women's Bundesliga Game | ✘ | 34 | 0 | 6% | 3% | -100% | -90% | 25 min |
| England Super League Basketball Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 7 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| BNXT League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 11 min |
| Slovakia SBL Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 16 min |
| Croatia Premijer Liga Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Slovakian Cup Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| LKL Lithuania Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 8 min |
| Slovenia 1. SKL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 15 min |
| Call of Duty Games | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 38 min |
| UAE Pro League | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 17 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| Ligue Magnus Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 6 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Men's Iceland Basketball Premier League Game | ✘ | 22 | 0 | 18% | 9% | -100% | -68% | 8 min |
| Women's ODI Cricket Match | ✘ | 21 | 0 | 19% | 10% | -100% | -67% | 61 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Colombia LBP Basketball Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Malaysia Super League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 9 min |
| Philippines PBA Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Israel Super League Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 13 min |
| Liga Portugal 2 Game | ✘ | 12 | 0 | 25% | 17% | -100% | -57% | 19 min |
| Slovakia Niké liga Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 21 min |
| Powerslap Match Winner | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 7 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Champions League Hockey | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Copa do Brasil Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 17 min |
| Bare Knuckle Fight Match | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 27 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| GBL Basketball Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ukraine SuperLeague Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| SAFF Championship Game | ✘ | 6 | 0 | 33% | 0% | -100% | -42% | 31 min |
| Portugal LPB Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Bulgaria First League Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 46 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Hungary NB I. A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Ukrainian Premier League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Womens TGL Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 71 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1158 | 4% | 1% | 0% | -93% |
| 5–15 min | 732 | 17% | 8% | 1% | -71% |
| 15–30 min | 496 | 25% | 12% | 1% | -57% |
| 30–60 min | 377 | 21% | 12% | 1% | -64% |
| Over 60 min | 339 | 22% | 9% | 0% | -62% |

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
| 11-11 19:58 | ITF Men's Match | Wilson Leite | ✘ | — | — | In play | — |
| 11-11 19:57 | Counter-Strike 2 Game | BoyBand | ✘ | — | — | In play | — |
| 11-11 19:56 | ITF Men's Match | Hiroki Sakagawa | ✘ | — | — | In play | — |
| 11-11 19:55 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-11 19:55 | eSoccer Game | Juventus (SilentShooter) | ✘ | — | — | In play | — |
| 11-11 19:53 | eSoccer Game | Brighton (Frost) | ✘ | — | — | In play | — |
| 11-11 19:53 | eSoccer Game | Nottingham Forest (Ousmane) | ✘ | — | — | In play | — |
| 11-11 19:52 | EuroCup Basketball Game | Niners Chemnitz | ✘ | — | — | In play | — |
| 11-11 19:52 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-11 19:52 | eSoccer Game | Aston Villa (Elastico) | ✘ | — | — | In play | — |
| 11-11 19:52 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-11 19:51 | Dota 2 Game | angry birds | ✘ | — | — | In play | — |
| 11-11 19:51 | eSoccer Game | France (Demi) | ✘ | — | — | In play | — |
| 11-11 19:51 | FIBA Europe Cup Game | Sporting Cp | ✘ | — | — | In play | — |
| 11-11 19:51 | ITF Women's Match | Anastasia Zolotareva | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:50 | eSoccer Game | Portugal (Adri) | ✘ | — | — | In play | — |
| 11-11 19:50 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-11 19:47 | ITF Men's Match | Tristan McCormick | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:45 | EFL Trophy Game | Tie | ✘ | — | — | In play | — |
| 11-11 19:43 | Counter-Strike 2 Game | SINQU | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:42 | EFL Trophy Game | Oldham | ✘ | — | — | In play | — |
| 11-11 19:41 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:40 | eSoccer Game | Liverpool (Ryft) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:40 | eSoccer Game | Brighton (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:40 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:39 | Russia Liga Pro Match | Khomenko Roman | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:39 | Russia Liga Pro Match | Drykin Sergei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:38 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:37 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-11 19:37 | eSoccer Game | Nottingham Forest (Ousmane) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
