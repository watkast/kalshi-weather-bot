# 1¢ Study

*Updated Wed Nov 4, 4:00 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 47 finished bets | 2% | $6.95 | +99% | +14.79¢ | $10.55 / -$3.60 |

*Expect about **1 buys a day**, roughly **$0.22/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 47 | -$0.30 | -4% |
| ESPN win probability ≥ 5%, sell at 25¢ | 47 | -$0.43 | -6% |
| ESPN win probability ≥ 2%, hold to the end | 107 | -$2.05 | -13% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 47058 | 2597 | 10 (0%) | 1.1% | -$249.55 (-64%) | Hold to the end: -$249.55 (-64%) |

*In play right now: 22. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 507 | 2.9% | 0.2% (1) | -86% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 507 | 1 | -82% | -72% | -71% | -71% |
| ESPN win probability ≥ 2% | 107 | 1 | -13% | -61% | -64% | -68% |
| ESPN win probability ≥ 5% | 47 | 1 | +99% | -78% | -78% | -82% |
| ESPN win probability ≥ 10% | 31 | 1 | +201% | -72% | -66% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2597 | 13% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 44439 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 10 | 0% | -$249.55 | -64% |
| Sell at 2¢ | 347 | 13% | -$299.33 | -77% |
| Sell at 3¢ | 241 | 9% | -$295.56 | -76% |
| Sell at 5¢ | 164 | 6% | -$282.95 | -73% |
| Sell at 10¢ | 73 | 3% | -$293.92 | -75% |
| Sell at 25¢ | 25 | 1% | -$306.80 | -79% |
| Sell at 50¢ | 17 | 1% | -$274.80 | -71% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 21713 | 12 | 1% | 0% | -95% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2510 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 2118 | 3 | 2% | 1% | -87% | -93% | 2 min |
| ITF Women's Match | ✘ | 1513 | 6 | 14% | 6% | -63% | -76% | 4 min |
| ITF Men's Match | ✘ | 1457 | 3 | 13% | 6% | -81% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1385 | 2 | 6% | 3% | -87% | -90% | 12 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 893 | 3 | 11% | 4% | -69% | -81% | 5 min |
| eFootball Game | ✘ | 595 | 2 | 1% | 1% | -69% | -98% | 2 min |
| College Football Game | partly | 412 | 3 | 12% | 6% | -32% | -79% | 24 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Men's T20 Cricket Match | ✘ | 311 | 2 | 15% | 6% | -40% | -73% | 23 min |
| Women's College Volleyball Match | ✘ | 308 | 2 | 5% | 3% | -39% | -92% | 67 min |
| Serie C Game | ✘ | 285 | 2 | 5% | 2% | -35% | -92% | 6 min |
| Dota 2 Game | ✘ | 280 | 1 | 1% | 1% | -67% | -98% | 31 min |
| Challenger WTA | ✘ | 263 | 1 | 14% | 5% | -65% | -76% | 9 min |
| NHL Game | ✔ | 245 | 2 | 14% | 7% | -24% | -75% | 5 min |
| Major League Soccer Game | partly | 187 | 1 | 12% | 6% | -50% | -80% | 8 min |
| WTA Tennis Match | ✘ | 177 | 0 | 11% | 2% | -100% | -80% | 5 min |
| NBA Game | ✔ | 167 | 0 | 18% | 5% | -100% | -69% | 9 min |
| AHL Game | ✘ | 165 | 0 | 4% | 2% | -100% | -93% | 5 min |
| League of Legends Game | ✘ | 156 | 0 | 6% | 2% | -100% | -89% | 11 min |
| Argentina Primera Division Game | ✘ | 147 | 2 | 15% | 9% | +27% | -74% | 7 min |
| Men's College Basketball Game | partly | 146 | 1 | 15% | 7% | -36% | -74% | 48 min |
| Ettan Game | ✘ | 145 | 0 | 3% | 1% | -100% | -94% | 7 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| Japan J2 League Game | ✘ | 141 | 1 | 11% | 4% | -34% | -82% | 6 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| KHL Game | ✘ | 130 | 0 | 5% | 2% | -100% | -92% | 6 min |
| Liga DIMAYOR Game | ✘ | 129 | 1 | 9% | 3% | -28% | -84% | 7 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| Brasileiro Serie B Game | ✘ | 127 | 1 | 8% | 4% | -27% | -86% | 8 min |
| ATP Tennis Match | ✘ | 127 | 0 | 16% | 6% | -100% | -73% | 4 min |
| Women's College Basketball Game | partly | 123 | 0 | 11% | 5% | -100% | -82% | 43 min |
| College Hockey Game | ✘ | 120 | 0 | 0% | 0% | -100% | -100% | 7 min |
| EFL Championship Game | ✔ | 118 | 0 | 8% | 4% | -100% | -87% | 10 min |
| Overwatch Game | ✘ | 114 | 0 | 2% | 0% | -100% | -97% | 6 min |
| USL Championship Game | partly | 110 | 0 | 12% | 5% | -100% | -80% | 5 min |
| EFL League One Game | ✔ | 110 | 0 | 9% | 3% | -100% | -84% | 10 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Brasileiro Serie A Game | partly | 107 | 1 | 11% | 7% | -13% | -81% | 7 min |
| Japan J League Game | ✘ | 101 | 1 | 15% | 6% | -8% | -74% | 13 min |
| LaLiga 2 Game | partly | 100 | 1 | 17% | 8% | -7% | -71% | 8 min |
| Liiga Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Chinese Basketball Association Game  | ✘ | 95 | 0 | 8% | 2% | -100% | -85% | 10 min |
| German 3. Liga Game | ✘ | 95 | 0 | 12% | 5% | -100% | -80% | 7 min |
| Serie B Game | ✘ | 95 | 0 | 13% | 6% | -100% | -78% | 10 min |
| Serie A Game | ✔ | 94 | 0 | 9% | 4% | -100% | -85% | 12 min |
| Liga MX Game | ✔ | 91 | 0 | 15% | 9% | -100% | -73% | 6 min |
| UEFA Champions League Game | partly | 91 | 1 | 10% | 2% | +3% | -83% | 12 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Valorant game winner | ✘ | 88 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Eerste Divisie Game | ✘ | 87 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Peru Liga 1 Game | ✘ | 86 | 0 | 13% | 6% | -100% | -78% | 12 min |
| TFF 1. Lig Game | ✘ | 86 | 0 | 14% | 8% | -100% | -76% | 10 min |
| Slovakian 2. Liga Game | ✘ | 82 | 0 | 6% | 5% | -100% | -89% | 78 min |
| Indonesia Super League Game | ✘ | 82 | 0 | 15% | 9% | -100% | -75% | 9 min |
| EuroCup Basketball Game | ✘ | 81 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Women's T20 Match | ✘ | 81 | 0 | 16% | 5% | -100% | -72% | 26 min |
| Uruguay Primera Division Game | ✘ | 80 | 0 | 8% | 2% | -100% | -87% | 10 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Liga Expansion Game | ✘ | 79 | 0 | 6% | 3% | -100% | -89% | 11 min |
| Euroleague Game | ✘ | 78 | 0 | 21% | 6% | -100% | -64% | 13 min |
| La Liga Game | ✔ | 78 | 0 | 18% | 12% | -100% | -69% | 9 min |
| R6 Game | ✘ | 77 | 1 | 10% | 5% | +21% | -82% | 9 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| Japan B League Game | ✘ | 75 | 0 | 7% | 0% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| English Premier League Game | ✔ | 73 | 0 | 7% | 3% | -100% | -88% | 9 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 72 | 1 | 18% | 7% | +30% | -69% | 8 min |
| Ligue 2 Game | ✘ | 72 | 0 | 8% | 6% | -100% | -86% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 71 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Men's ODI Cricket Match | ✘ | 70 | 3 | 21% | 7% | +300% | -63% | 53 min |
| AFC Champions League Game | ✘ | 70 | 0 | 6% | 1% | -100% | -90% | 12 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| Polish Ekstraklasa Game | ✘ | 69 | 0 | 13% | 7% | -100% | -77% | 9 min |
| Allsvenskan Game | ✘ | 69 | 1 | 16% | 10% | +35% | -72% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| NWSL Game | ✔ | 68 | 0 | 7% | 1% | -100% | -87% | 7 min |
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
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Czech National Football League Game | ✘ | 59 | 0 | 12% | 7% | -100% | -79% | 8 min |
| Czech First League Game | ✘ | 59 | 0 | 10% | 0% | -100% | -82% | 9 min |
| LNB Elite 2 Game | ✘ | 58 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Italy Serie A2 Game | ✘ | 58 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Bolivia Premier Division Game | ✘ | 58 | 0 | 9% | 2% | -100% | -85% | 5 min |
| APF Division de Honor Game | ✘ | 57 | 0 | 19% | 5% | -100% | -67% | 10 min |
| Thai League 1 Game | ✘ | 56 | 0 | 18% | 7% | -100% | -69% | 11 min |
| KBO Game | ✘ | 55 | 0 | 11% | 5% | -100% | -81% | 5 min |
| Liga Portugal Game | ✘ | 54 | 0 | 6% | 2% | -100% | -90% | 11 min |
| Israeli Premier League Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 8 min |
| England Women's Super League Game | ✘ | 52 | 0 | 17% | 8% | -100% | -70% | 23 min |
| Serbian SuperLiga Game | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 12 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Belgian Pro League Game | ✘ | 50 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Finland Korisliiga Game | ✘ | 49 | 1 | 8% | 4% | +90% | -86% | 9 min |
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
| FIBA Europe Cup Game | ✘ | 43 | 0 | 9% | 2% | -100% | -84% | 9 min |
| LNB Elite Game | ✘ | 42 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Danish Superliga Game | ✘ | 41 | 0 | 10% | 5% | -100% | -83% | 10 min |
| Romanian Liga I Game | ✘ | 41 | 0 | 10% | 2% | -100% | -83% | 9 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Australia NBL Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 9 min |
| Italy Serie A Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Croatia HNL Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 8 min |
| Czech NBL Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 17 min |
| Sweden SBL Game | ✘ | 37 | 0 | 5% | 5% | -100% | -91% | 14 min |
| Bundesliga Basketball Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 13 min |
| Latvian Virsliga Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 21 min |
| Slovenian Prva Liga Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Brazil NBB Basketball Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 18 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Qatar Stars League | ✘ | 36 | 0 | 8% | 3% | -100% | -86% | 7 min |
| Canadian Premier League | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 22 min |
| Swiss Super League Game | ✘ | 35 | 1 | 6% | 3% | +167% | -90% | 12 min |
| Korea KBL Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Hungarian NB I Game | ✘ | 34 | 0 | 9% | 9% | -100% | -85% | 6 min |
| Austria BSL Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Turkey BSL Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Australian A League Game | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 6 min |
| Indian Super League Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 7 min |
| Austrian Bundesliga Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 12 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Russia VTB United Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 15 min |
| EFL Trophy Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 47 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Croatia Premijer Liga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eredivisie Vrouwen Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 8 min |
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| England Super League Basketball Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 7 min |
| FIBA Champions League Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Slovakia SBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 18 min |
| Liga Nacional de Basquetbol Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 7 min |
| French Women's Première Ligue Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| LKL Lithuania Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 9 min |
| BNXT League Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 11 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 14 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| EuroLeague (W) Game | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 9 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Women's ODI Cricket Match | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 61 min |
| Women's Pro Basketball Game | ✔ | 18 | 0 | 22% | 6% | -100% | -61% | 6 min |
| CFL Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 9 min |
| Men's Iceland Basketball Premier League Game | ✘ | 18 | 0 | 22% | 11% | -100% | -61% | 11 min |
| Malaysia Super League Game | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 9 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Philippines PBA Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
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

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 993 | 4% | 1% | 0% | -93% |
| 5–15 min | 614 | 16% | 7% | 1% | -72% |
| 15–30 min | 411 | 24% | 12% | 1% | -59% |
| 30–60 min | 313 | 20% | 11% | 1% | -65% |
| Over 60 min | 238 | 20% | 11% | 0% | -66% |

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
| 11-04 11:00 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-04 11:00 | eSoccer Game | Crystal Palace (Strudl) | ✘ | — | — | In play | — |
| 11-04 10:59 | Counter-Strike 2 Game | Leo Team | ✘ | — | — | In play | — |
| 11-04 10:58 | eBasketball Game | New York Knicks (Jimmy) | ✘ | — | — | In play | — |
| 11-04 10:58 | ITF Women's Match | Samaira Pahwa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:57 | eBasketball Game | Brooklyn Nets (Tatum) | ✘ | — | — | In play | — |
| 11-04 10:57 | eSoccer Game | England (Trinity) | ✘ | — | — | In play | — |
| 11-04 10:56 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-04 10:55 | eSoccer Game | Spain (Lotta) | ✘ | — | — | In play | — |
| 11-04 10:55 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-04 10:54 | ITF Women's Match | Ilay Yoruk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:49 | WTA Tennis Match | Oksana Selekhmeteva | ✘ | — | — | In play | — |
| 11-04 10:47 | eSoccer Game | Manchester City (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:47 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:46 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:46 | eSoccer Game | Stuttgart (Vini) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:44 | eSoccer Game | Mönchengladbach (Bradley) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:44 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:44 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:44 | eSoccer Game | England (Trinity) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:41 | eSoccer Game | Portugal (Lexi) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:41 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:41 | Dota 2 Game | Royal Bear | ✘ | — | — | In play | — |
| 11-04 10:38 | ITF Women's Match | Elena Korokozidi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:37 | ITF Men's Match | Egor Khotchenkov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:34 | eBasketball Game | Denver Nuggets (Tyler) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:33 | eSoccer Game | Everton (Homie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:33 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:33 | Counter-Strike 2 Game | Bebop | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-04 10:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
