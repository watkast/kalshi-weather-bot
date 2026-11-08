# 1¢ Study

*Updated Sun Nov 8, 9:48 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 58 finished bets | 2% | $5.30 | +61% | +9.14¢ | $9.65 / -$4.35 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 58 | -$1.95 | -22% |
| ESPN win probability ≥ 5%, sell at 25¢ | 58 | -$2.08 | -24% |
| ESPN win probability ≥ 2%, hold to the end | 133 | -$5.95 | -30% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 53349 | 2992 | 12 (0%) | 1.1% | -$280.80 (-63%) | Hold to the end: -$280.80 (-63%) |

*In play right now: 39. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 644 | 2.8% | 0.2% (1) | -97% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 644 | 1 | -86% | -71% | -71% | -72% |
| ESPN win probability ≥ 2% | 133 | 1 | -30% | -61% | -65% | -71% |
| ESPN win probability ≥ 5% | 58 | 1 | +61% | -82% | -82% | -85% |
| ESPN win probability ≥ 10% | 38 | 1 | +146% | -77% | -73% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2992 | 14% | 10% | 6% | 3% | 1% | 1% |
| Unverified | 50318 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 12 | 0% | -$280.80 | -63% |
| Sell at 2¢ | 411 | 14% | -$341.94 | -76% |
| Sell at 3¢ | 286 | 10% | -$337.26 | -75% |
| Sell at 5¢ | 193 | 6% | -$323.35 | -72% |
| Sell at 10¢ | 85 | 3% | -$337.45 | -75% |
| Sell at 25¢ | 31 | 1% | -$346.19 | -77% |
| Sell at 50¢ | 20 | 1% | -$313.80 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 24814 | 16 | 1% | 0% | -94% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2980 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 2441 | 4 | 2% | 1% | -85% | -93% | 2 min |
| ITF Women's Match | ✘ | 1643 | 6 | 14% | 6% | -66% | -77% | 4 min |
| ITF Men's Match | ✘ | 1554 | 3 | 13% | 6% | -82% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1500 | 2 | 6% | 3% | -88% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 953 | 3 | 11% | 4% | -71% | -81% | 5 min |
| eFootball Game | ✘ | 625 | 2 | 1% | 1% | -70% | -98% | 2 min |
| College Football Game | partly | 520 | 3 | 11% | 6% | -46% | -81% | 23 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's College Volleyball Match | ✘ | 338 | 2 | 4% | 2% | -45% | -92% | 68 min |
| Men's T20 Cricket Match | ✘ | 328 | 2 | 16% | 7% | -43% | -73% | 23 min |
| Dota 2 Game | ✘ | 322 | 1 | 1% | 1% | -71% | -98% | 31 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Serie C Game | ✘ | 319 | 2 | 4% | 2% | -41% | -93% | 8 min |
| Men's College Basketball Game | partly | 310 | 5 | 19% | 7% | +51% | -68% | 36 min |
| Challenger WTA | ✘ | 280 | 1 | 13% | 4% | -67% | -78% | 9 min |
| Women's College Basketball Game | partly | 279 | 1 | 10% | 4% | -67% | -83% | 37 min |
| NHL Game | ✔ | 275 | 2 | 16% | 8% | -32% | -73% | 5 min |
| Major League Soccer Game | partly | 217 | 1 | 12% | 6% | -57% | -80% | 8 min |
| AHL Game | ✘ | 203 | 0 | 4% | 2% | -100% | -93% | 5 min |
| NBA Game | ✔ | 199 | 0 | 19% | 6% | -100% | -68% | 10 min |
| WTA Tennis Match | ✘ | 183 | 0 | 13% | 3% | -100% | -78% | 5 min |
| Ettan Game | ✘ | 177 | 0 | 5% | 1% | -100% | -92% | 10 min |
| Argentina Primera Division Game | ✘ | 173 | 2 | 17% | 9% | +8% | -71% | 9 min |
| College Hockey Game | ✘ | 164 | 0 | 1% | 0% | -100% | -99% | 11 min |
| Japan J2 League Game | ✘ | 161 | 1 | 10% | 4% | -42% | -83% | 7 min |
| League of Legends Game | ✘ | 160 | 0 | 8% | 2% | -100% | -87% | 11 min |
| EFL Championship Game | ✔ | 149 | 1 | 9% | 5% | -37% | -85% | 9 min |
| Liga DIMAYOR Game | ✘ | 143 | 1 | 10% | 3% | -35% | -82% | 8 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| Brasileiro Serie B Game | ✘ | 141 | 1 | 7% | 4% | -34% | -88% | 10 min |
| KHL Game | ✘ | 141 | 0 | 4% | 2% | -100% | -93% | 6 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| ATP Tennis Match | ✘ | 138 | 0 | 15% | 7% | -100% | -74% | 4 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| Overwatch Game | ✘ | 124 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Brasileiro Serie A Game | partly | 120 | 1 | 11% | 7% | -22% | -81% | 9 min |
| Japan J League Game | ✘ | 119 | 1 | 16% | 7% | -22% | -72% | 12 min |
| USL Championship Game | partly | 118 | 0 | 11% | 4% | -100% | -81% | 5 min |
| EFL League One Game | ✔ | 112 | 0 | 9% | 3% | -100% | -85% | 10 min |
| Serie B Game | ✘ | 111 | 0 | 11% | 5% | -100% | -81% | 9 min |
| German 3. Liga Game | ✘ | 109 | 0 | 11% | 5% | -100% | -81% | 10 min |
| UEFA Champions League Game | partly | 109 | 1 | 11% | 5% | -14% | -81% | 10 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| LaLiga 2 Game | partly | 108 | 1 | 18% | 7% | -14% | -70% | 9 min |
| Serie A Game | ✔ | 108 | 0 | 10% | 6% | -100% | -82% | 12 min |
| Liga MX Game | ✔ | 104 | 0 | 13% | 8% | -100% | -77% | 7 min |
| Valorant game winner | ✘ | 103 | 0 | 6% | 4% | -100% | -90% | 14 min |
| R6 Game | ✘ | 103 | 1 | 10% | 5% | -9% | -83% | 8 min |
| Eerste Divisie Game | ✘ | 103 | 0 | 9% | 5% | -100% | -85% | 12 min |
| Women's T20 Match | ✘ | 99 | 0 | 18% | 5% | -100% | -68% | 27 min |
| Peru Liga 1 Game | ✘ | 98 | 0 | 15% | 6% | -100% | -73% | 14 min |
| Slovakian 2. Liga Game | ✘ | 96 | 0 | 5% | 4% | -100% | -91% | 48 min |
| Indonesia Super League Game | ✘ | 96 | 0 | 12% | 7% | -100% | -78% | 12 min |
| TFF 1. Lig Game | ✘ | 96 | 0 | 12% | 7% | -100% | -78% | 11 min |
| Liiga Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| EuroCup Basketball Game | ✘ | 92 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Liga Expansion Game | ✘ | 91 | 0 | 7% | 3% | -100% | -89% | 12 min |
| English Premier League Game | ✔ | 91 | 0 | 5% | 2% | -100% | -90% | 9 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Ligue 2 Game | ✘ | 90 | 0 | 8% | 6% | -100% | -87% | 12 min |
| China League 1 Game | ✘ | 89 | 0 | 9% | 4% | -100% | -84% | 12 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| La Liga Game | ✔ | 87 | 0 | 18% | 11% | -100% | -68% | 9 min |
| Japan B League Game | ✘ | 84 | 0 | 7% | 0% | -100% | -88% | 11 min |
| Euroleague Game | ✘ | 83 | 0 | 22% | 6% | -100% | -62% | 13 min |
| Polish Ekstraklasa Game | ✘ | 81 | 0 | 11% | 6% | -100% | -81% | 11 min |
| Uruguay Primera Division Game | ✘ | 80 | 0 | 8% | 2% | -100% | -87% | 10 min |
| Tweede Divisie Game | ✘ | 80 | 0 | 1% | 0% | -100% | -98% | 8 min |
| Korea K-League 2 Game | ✘ | 80 | 0 | 11% | 6% | -100% | -80% | 9 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Men's ODI Cricket Match | ✘ | 77 | 3 | 19% | 6% | +264% | -66% | 45 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Bundesliga Game | ✔ | 77 | 1 | 17% | 9% | +21% | -71% | 9 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| Allsvenskan Game | ✘ | 75 | 1 | 15% | 9% | +24% | -75% | 12 min |
| Turkish Super Lig Game | ✘ | 74 | 0 | 18% | 4% | -100% | -70% | 15 min |
| NFL Game | ✔ | 73 | 1 | 18% | 7% | +28% | -69% | 8 min |
| Czech First League Game | ✘ | 73 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Bundesliga 2 Game | ✔ | 73 | 0 | 15% | 7% | -100% | -74% | 8 min |
| NWSL Game | ✔ | 72 | 0 | 7% | 1% | -100% | -88% | 7 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Mobile Legends Bang Bang Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 4 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Eredivisie Game | ✔ | 70 | 0 | 9% | 7% | -100% | -85% | 5 min |
| Ligue 1 Game | ✔ | 70 | 0 | 16% | 6% | -100% | -73% | 9 min |
| APF Division de Honor Game | ✘ | 69 | 0 | 17% | 4% | -100% | -70% | 12 min |
| Thai League 1 Game | ✘ | 68 | 0 | 16% | 7% | -100% | -72% | 15 min |
| Eliteserien Game | ✘ | 68 | 0 | 9% | 4% | -100% | -85% | 12 min |
| Ecuador Liga Pro Game | ✘ | 68 | 0 | 6% | 1% | -100% | -90% | 11 min |
| Bolivia Premier Division Game | ✘ | 66 | 0 | 8% | 2% | -100% | -87% | 8 min |
| Israeli Premier League Game | ✘ | 66 | 0 | 6% | 2% | -100% | -89% | 13 min |
| LNB Elite 2 Game | ✘ | 64 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Italy Serie A2 Game | ✘ | 64 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Czech National Football League Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 9 min |
| LNBP Basketball Game | ✘ | 63 | 0 | 10% | 2% | -100% | -83% | 12 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| England Women's Super League Game | ✘ | 62 | 0 | 15% | 6% | -100% | -75% | 23 min |
| Chinese Super League Game | ✘ | 62 | 1 | 11% | 6% | +51% | -80% | 19 min |
| Belgian Pro League Game | ✘ | 62 | 0 | 6% | 0% | -100% | -89% | 18 min |
| Vietnam V-League 1 Game | ✘ | 60 | 1 | 5% | 3% | +56% | -91% | 11 min |
| Korea K League Game | ✘ | 60 | 1 | 15% | 8% | +56% | -74% | 8 min |
| Liga Portugal Game | ✘ | 60 | 0 | 5% | 2% | -100% | -91% | 12 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Serbian SuperLiga Game | ✘ | 58 | 0 | 3% | 2% | -100% | -94% | 15 min |
| KBO Game | ✘ | 57 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Finland Korisliiga Game | ✘ | 57 | 1 | 7% | 4% | +64% | -88% | 8 min |
| Serie A Femminile Game | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 13 min |
| FIBA Europe Cup Game | ✘ | 55 | 0 | 9% | 4% | -100% | -84% | 11 min |
| Super League Greece Game | ✘ | 53 | 0 | 19% | 4% | -100% | -67% | 14 min |
| Romanian Liga I Game | ✘ | 53 | 0 | 11% | 2% | -100% | -80% | 14 min |
| Scottish Premiership Game | ✘ | 52 | 0 | 10% | 2% | -100% | -83% | 10 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Adriatic ABA Game | ✘ | 51 | 1 | 6% | 4% | +83% | -90% | 10 min |
| Chile Liga de Primera Game | ✘ | 51 | 0 | 12% | 2% | -100% | -80% | 13 min |
| Spanish Liga F Game | ✘ | 51 | 0 | 8% | 6% | -100% | -86% | 10 min |
| Rugby French 14 Match | ✘ | 50 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 50 | 0 | 18% | 10% | -100% | -69% | 6 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| LNB Elite Game | ✘ | 48 | 0 | 2% | 0% | -100% | -96% | 8 min |
| Brazil NBB Basketball Game | ✘ | 48 | 0 | 6% | 4% | -100% | -89% | 19 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Spain Liga ACB Game | ✘ | 46 | 0 | 7% | 2% | -100% | -89% | 14 min |
| Czech NBL Game | ✘ | 45 | 0 | 2% | 0% | -100% | -96% | 16 min |
| Croatia HNL Game | ✘ | 45 | 0 | 9% | 4% | -100% | -85% | 10 min |
| Danish Superliga Game | ✘ | 45 | 0 | 11% | 7% | -100% | -81% | 13 min |
| Latvian Virsliga Game | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 22 min |
| Qatar Stars League | ✘ | 45 | 0 | 11% | 4% | -100% | -81% | 10 min |
| Australia NBL Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 10 min |
| Bundesliga Basketball Game | ✘ | 43 | 0 | 9% | 5% | -100% | -84% | 13 min |
| Slovenian Prva Liga Game | ✘ | 43 | 0 | 7% | 2% | -100% | -88% | 7 min |
| Sweden SBL Game | ✘ | 42 | 0 | 5% | 5% | -100% | -92% | 12 min |
| Australian A League Game | ✘ | 42 | 0 | 10% | 2% | -100% | -83% | 11 min |
| Indian Super League Game | ✘ | 42 | 0 | 14% | 7% | -100% | -75% | 9 min |
| Italy Serie A Game | ✘ | 41 | 0 | 5% | 2% | -100% | -92% | 6 min |
| Swiss Super League Game | ✘ | 41 | 1 | 5% | 2% | +128% | -92% | 11 min |
| Korea KBL Game | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Hungarian NB I Game | ✘ | 40 | 0 | 8% | 8% | -100% | -87% | 7 min |
| Canadian Premier League | ✘ | 39 | 1 | 15% | 13% | +139% | -73% | 17 min |
| Austrian Bundesliga Game | ✘ | 38 | 0 | 8% | 5% | -100% | -86% | 14 min |
| Turkey BSL Game | ✘ | 37 | 0 | 0% | 0% | -100% | -100% | 10 min |
| French Women's Première Ligue Game | ✘ | 37 | 0 | 8% | 5% | -100% | -86% | 13 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Austria BSL Game | ✘ | 36 | 0 | 8% | 6% | -100% | -86% | 10 min |
| Russia VTB United Game | ✘ | 35 | 0 | 6% | 0% | -100% | -90% | 15 min |
| German Women's Bundesliga Game | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 23 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| EFL Trophy Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 47 min |
| Liga Nacional de Basquetbol Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 6 min |
| Slovakia SBL Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 16 min |
| England Super League Basketball Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 6 min |
| FIBA Champions League Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| BNXT League Game | ✘ | 29 | 0 | 7% | 3% | -100% | -88% | 11 min |
| Croatia Premijer Liga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eredivisie Vrouwen Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 8 min |
| Slovakian Cup Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 18 min |
| Slovenia 1. SKL Game | ✘ | 26 | 0 | 4% | 4% | -100% | -93% | 14 min |
| LKL Lithuania Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 9 min |
| EuroLeague (W) Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 9 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Call of Duty Games | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's ODI Cricket Match | ✘ | 21 | 0 | 19% | 10% | -100% | -67% | 61 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Men's Iceland Basketball Premier League Game | ✘ | 21 | 0 | 19% | 10% | -100% | -67% | 9 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| CFL Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 8 min |
| UAE Pro League | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 18 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| Malaysia Super League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 9 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Colombia LBP Basketball Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Philippines PBA Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 10 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Israel Super League Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 13 min |
| Powerslap Match Winner | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 7 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Portugal 2 Game | ✘ | 10 | 0 | 20% | 20% | -100% | -65% | 18 min |
| Slovakia Niké liga Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 19 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bare Knuckle Fight Match | ✘ | 8 | 0 | 25% | 0% | -100% | -57% | 27 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| GBL Basketball Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ukraine SuperLeague Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Copa do Brasil Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 15 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 35 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| SAFF Championship Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 31 min |
| Denmark Basketligaen Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 38 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Hungary NB I. A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Premier League Cup Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Bulgaria First League Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 34 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1123 | 4% | 1% | 0% | -94% |
| 5–15 min | 703 | 17% | 8% | 1% | -71% |
| 15–30 min | 475 | 24% | 12% | 1% | -58% |
| 30–60 min | 357 | 20% | 11% | 1% | -66% |
| Over 60 min | 306 | 22% | 10% | 0% | -62% |

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
| 11-08 16:47 | LKL Lithuania Game | BC Juventus Utena | ✘ | — | — | In play | — |
| 11-08 16:46 | eSoccer Game | Sunderland (Danny) | ✘ | — | — | In play | — |
| 11-08 16:43 | ITF Women's Match | Fanny Pire | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:43 | Russia Liga Pro Match | Girevenkov Alik | ✘ | — | — | In play | — |
| 11-08 16:43 | eBasketball Game | Golden State Warriors (Cade) | ✘ | — | — | In play | — |
| 11-08 16:42 | German Women's Bundesliga Game | Mainz 05 | ✘ | — | — | In play | — |
| 11-08 16:42 | German Women's Bundesliga Game | Tie | ✘ | — | — | In play | — |
| 11-08 16:41 | eSoccer Game | Freiburg (SilentShooter) | ✘ | — | — | In play | — |
| 11-08 16:41 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-08 16:41 | Challenger WTA | Maria Camila Torres Murcia | ✘ | — | — | In play | — |
| 11-08 16:40 | eSoccer Game | Manchester City (Rooney) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:40 | Belgian Pro League Game | Kortrijk | ✘ | — | — | In play | — |
| 11-08 16:38 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:38 | eSoccer Game | Montpellier (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:38 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:38 | eBasketball Game | New York Knicks (Jason) | ✘ | — | — | In play | — |
| 11-08 16:37 | eSoccer Game | Everton (Eder) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:37 | Counter-Strike 2 Game | ex-ENCE | ✘ | — | — | In play | — |
| 11-08 16:36 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:36 | eSoccer Game | Sunderland (Niskanen15) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:36 | Super League Greece Game | Levadiakos | ✘ | — | — | In play | — |
| 11-08 16:36 | Italy Serie A Game | Pallacanestro Cantu | ✘ | — | — | In play | — |
| 11-08 16:36 | eSoccer Game | RC Lens (Nicol) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:30 | Hungarian NB I Game | Tie | ✘ | — | — | In play | — |
| 11-08 16:29 | Hungarian NB I Game | Ujpest Budapest | ✘ | — | — | In play | — |
| 11-08 16:28 | ITF Men's Match | Ryan Char | ✘ | — | — | In play | — |
| 11-08 16:27 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:26 | eSoccer Game | FC Bayern (SilentShooter) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:25 | eSoccer Game | Manchester City (Niskanen15) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-08 16:25 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
