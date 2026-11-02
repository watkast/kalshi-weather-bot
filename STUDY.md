# 1¢ Study

*Updated Mon Nov 2, 2:44 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 46 finished bets | 2% | $7.10 | +103% | +15.43¢ | $10.55 / -$3.45 |

*Expect about **2 buys a day**, roughly **$0.23/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 5%, sell at 50¢ | 46 | -$0.15 | -2% |
| ESPN win probability ≥ 5%, sell at 25¢ | 46 | -$0.28 | -4% |
| ESPN win probability ≥ 2%, hold to the end | 98 | -$0.70 | -5% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 44939 | 2482 | 9 (0%) | 1.1% | -$246.30 (-66%) | Hold to the end: -$246.30 (-66%) |

*In play right now: 33. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 457 | 3.1% | 0.2% (1) | -90% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 457 | 1 | -80% | -72% | -70% | -71% |
| ESPN win probability ≥ 2% | 98 | 1 | -5% | -61% | -66% | -73% |
| ESPN win probability ≥ 5% | 46 | 1 | +103% | -77% | -77% | -81% |
| ESPN win probability ≥ 10% | 31 | 1 | +201% | -72% | -66% | -72% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2482 | 13% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 42424 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 9 | 0% | -$246.30 | -66% |
| Sell at 2¢ | 332 | 13% | -$285.98 | -77% |
| Sell at 3¢ | 232 | 9% | -$281.82 | -76% |
| Sell at 5¢ | 158 | 6% | -$269.60 | -72% |
| Sell at 10¢ | 71 | 3% | -$279.29 | -75% |
| Sell at 25¢ | 24 | 1% | -$292.86 | -79% |
| Sell at 50¢ | 16 | 1% | -$264.30 | -71% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 20533 | 12 | 1% | 1% | -95% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2509 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 2008 | 3 | 2% | 1% | -86% | -93% | 2 min |
| ITF Women's Match | ✘ | 1443 | 6 | 14% | 6% | -61% | -77% | 4 min |
| ITF Men's Match | ✘ | 1351 | 2 | 13% | 5% | -86% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1342 | 2 | 6% | 3% | -86% | -90% | 12 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 855 | 2 | 11% | 3% | -78% | -82% | 5 min |
| eFootball Game | ✘ | 539 | 2 | 1% | 1% | -65% | -98% | 2 min |
| College Football Game | partly | 410 | 3 | 12% | 6% | -32% | -80% | 24 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Women's College Volleyball Match | ✘ | 308 | 2 | 5% | 3% | -39% | -92% | 67 min |
| Men's T20 Cricket Match | ✘ | 304 | 1 | 15% | 6% | -69% | -74% | 23 min |
| Serie C Game | ✘ | 284 | 2 | 5% | 2% | -34% | -92% | 6 min |
| Dota 2 Game | ✘ | 271 | 1 | 1% | 1% | -66% | -98% | 31 min |
| Challenger WTA | ✘ | 251 | 1 | 14% | 5% | -63% | -77% | 9 min |
| NHL Game | ✔ | 230 | 1 | 14% | 7% | -59% | -76% | 5 min |
| Major League Soccer Game | partly | 187 | 1 | 12% | 6% | -50% | -80% | 8 min |
| WTA Tennis Match | ✘ | 175 | 0 | 11% | 2% | -100% | -80% | 5 min |
| AHL Game | ✘ | 165 | 0 | 4% | 2% | -100% | -93% | 5 min |
| League of Legends Game | ✘ | 156 | 0 | 6% | 2% | -100% | -89% | 11 min |
| NBA Game | ✔ | 153 | 0 | 18% | 5% | -100% | -68% | 9 min |
| Ettan Game | ✘ | 145 | 0 | 3% | 1% | -100% | -94% | 7 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Argentina Primera Division Game | ✘ | 139 | 2 | 15% | 9% | +34% | -74% | 7 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| KHL Game | ✘ | 127 | 0 | 5% | 2% | -100% | -92% | 6 min |
| Brasileiro Serie B Game | ✘ | 123 | 1 | 7% | 4% | -24% | -87% | 8 min |
| ATP Tennis Match | ✘ | 123 | 0 | 15% | 6% | -100% | -75% | 4 min |
| Liga DIMAYOR Game | ✘ | 121 | 1 | 9% | 2% | -23% | -84% | 6 min |
| Japan J2 League Game | ✘ | 120 | 0 | 11% | 4% | -100% | -81% | 6 min |
| College Hockey Game | ✘ | 120 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Overwatch Game | ✘ | 114 | 0 | 2% | 0% | -100% | -97% | 6 min |
| USL Championship Game | partly | 110 | 0 | 12% | 5% | -100% | -80% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| EFL League One Game | ✔ | 106 | 0 | 9% | 3% | -100% | -84% | 10 min |
| Brasileiro Serie A Game | partly | 102 | 1 | 12% | 7% | -8% | -80% | 7 min |
| Japan J League Game | ✘ | 101 | 1 | 15% | 6% | -8% | -74% | 13 min |
| EFL Championship Game | ✔ | 100 | 0 | 7% | 4% | -100% | -88% | 10 min |
| LaLiga 2 Game | partly | 98 | 1 | 17% | 8% | -5% | -70% | 8 min |
| Liiga Game | ✘ | 95 | 0 | 0% | 0% | -100% | -100% | 5 min |
| German 3. Liga Game | ✘ | 95 | 0 | 12% | 5% | -100% | -80% | 7 min |
| Serie B Game | ✘ | 95 | 0 | 13% | 6% | -100% | -78% | 10 min |
| Serie A Game | ✔ | 94 | 0 | 9% | 4% | -100% | -85% | 12 min |
| Liga MX Game | ✔ | 91 | 0 | 15% | 9% | -100% | -73% | 6 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Valorant game winner | ✘ | 88 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Eerste Divisie Game | ✘ | 87 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Chinese Basketball Association Game  | ✘ | 87 | 0 | 7% | 1% | -100% | -88% | 10 min |
| TFF 1. Lig Game | ✘ | 86 | 0 | 14% | 8% | -100% | -76% | 10 min |
| Slovakian 2. Liga Game | ✘ | 82 | 0 | 6% | 5% | -100% | -89% | 78 min |
| Indonesia Super League Game | ✘ | 82 | 0 | 15% | 9% | -100% | -75% | 9 min |
| Liga Leumit Game | ✘ | 80 | 0 | 4% | 4% | -100% | -94% | 19 min |
| Peru Liga 1 Game | ✘ | 80 | 0 | 14% | 6% | -100% | -76% | 11 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Liga Expansion Game | ✘ | 79 | 0 | 6% | 3% | -100% | -89% | 11 min |
| Uruguay Primera Division Game | ✘ | 78 | 0 | 8% | 3% | -100% | -87% | 10 min |
| Euroleague Game | ✘ | 78 | 0 | 21% | 6% | -100% | -64% | 13 min |
| Women's T20 Match | ✘ | 78 | 0 | 15% | 5% | -100% | -73% | 25 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| EuroCup Basketball Game | ✘ | 76 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| La Liga Game | ✔ | 76 | 0 | 18% | 12% | -100% | -68% | 9 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| Japan B League Game | ✘ | 75 | 0 | 7% | 0% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 71 | 1 | 18% | 7% | +31% | -68% | 8 min |
| Mobile Legends Bang Bang Game | ✘ | 71 | 0 | 0% | 0% | -100% | -100% | 4 min |
| English Premier League Game | ✔ | 71 | 0 | 7% | 3% | -100% | -88% | 9 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| NWSL Game | ✔ | 68 | 0 | 7% | 1% | -100% | -87% | 7 min |
| Ligue 2 Game | ✘ | 68 | 0 | 9% | 6% | -100% | -85% | 8 min |
| Polish Ekstraklasa Game | ✘ | 67 | 0 | 13% | 7% | -100% | -77% | 8 min |
| Allsvenskan Game | ✘ | 67 | 1 | 16% | 10% | +39% | -72% | 9 min |
| Men's ODI Cricket Match | ✘ | 66 | 3 | 23% | 8% | +324% | -61% | 48 min |
| Bundesliga 2 Game | ✔ | 65 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Korea K-League 2 Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 7 min |
| Eliteserien Game | ✘ | 64 | 0 | 9% | 5% | -100% | -84% | 10 min |
| Turkish Super Lig Game | ✘ | 64 | 0 | 14% | 3% | -100% | -76% | 13 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Bundesliga Game | ✔ | 63 | 1 | 16% | 10% | +48% | -72% | 7 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Eredivisie Game | ✔ | 62 | 0 | 10% | 8% | -100% | -83% | 5 min |
| Ligue 1 Game | ✔ | 62 | 0 | 16% | 6% | -100% | -72% | 9 min |
| Ecuador Liga Pro Game | ✘ | 60 | 0 | 7% | 2% | -100% | -88% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Czech National Football League Game | ✘ | 59 | 0 | 12% | 7% | -100% | -79% | 8 min |
| Czech First League Game | ✘ | 59 | 0 | 10% | 0% | -100% | -82% | 9 min |
| LNBP Basketball Game | ✘ | 58 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Italy Serie A2 Game | ✘ | 58 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Bolivia Premier Division Game | ✘ | 58 | 0 | 9% | 2% | -100% | -85% | 5 min |
| AFC Champions League Game | ✘ | 58 | 0 | 5% | 0% | -100% | -91% | 8 min |
| LNB Elite 2 Game | ✘ | 57 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Thai League 1 Game | ✘ | 56 | 0 | 18% | 7% | -100% | -69% | 11 min |
| KBO Game | ✘ | 54 | 0 | 11% | 6% | -100% | -81% | 4 min |
| Israeli Premier League Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 8 min |
| APF Division de Honor Game | ✘ | 53 | 0 | 21% | 6% | -100% | -64% | 8 min |
| England Women's Super League Game | ✘ | 52 | 0 | 17% | 8% | -100% | -70% | 23 min |
| Serbian SuperLiga Game | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 12 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Liga Portugal Game | ✘ | 50 | 0 | 4% | 2% | -100% | -93% | 11 min |
| Belgian Pro League Game | ✘ | 50 | 0 | 8% | 0% | -100% | -86% | 12 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Super League Greece Game | ✘ | 49 | 0 | 20% | 4% | -100% | -65% | 12 min |
| Vietnam V-League 1 Game | ✘ | 48 | 1 | 6% | 4% | +94% | -89% | 10 min |
| Korea K League Game | ✘ | 48 | 1 | 15% | 8% | +94% | -75% | 7 min |
| Finland Korisliiga Game | ✘ | 47 | 1 | 9% | 4% | +99% | -85% | 9 min |
| Serie A Femminile Game | ✘ | 47 | 0 | 2% | 2% | -100% | -96% | 8 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| KNVB Cup Game | ✘ | 47 | 0 | 17% | 11% | -100% | -70% | 13 min |
| Adriatic ABA Game | ✘ | 46 | 1 | 7% | 4% | +103% | -89% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 46 | 0 | 20% | 11% | -100% | -66% | 5 min |
| Scottish Premiership Game | ✘ | 44 | 0 | 11% | 2% | -100% | -80% | 10 min |
| Chile Liga de Primera Game | ✘ | 43 | 0 | 12% | 2% | -100% | -80% | 6 min |
| Rugby French 14 Match | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Spain Liga ACB Game | ✘ | 43 | 0 | 7% | 2% | -100% | -88% | 17 min |
| Spanish Liga F Game | ✘ | 43 | 0 | 7% | 5% | -100% | -88% | 7 min |
| LNB Elite Game | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Danish Superliga Game | ✘ | 41 | 0 | 10% | 5% | -100% | -83% | 10 min |
| Romanian Liga I Game | ✘ | 41 | 0 | 10% | 2% | -100% | -83% | 9 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Australia NBL Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 9 min |
| Italy Serie A Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Croatia HNL Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 8 min |
| FIBA Europe Cup Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Czech NBL Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 17 min |
| Latvian Virsliga Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 21 min |
| Slovenian Prva Liga Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Sweden SBL Game | ✘ | 36 | 0 | 6% | 6% | -100% | -90% | 15 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Bundesliga Basketball Game | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 13 min |
| Qatar Stars League | ✘ | 36 | 0 | 8% | 3% | -100% | -86% | 7 min |
| Canadian Premier League | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 22 min |
| Swiss Super League Game | ✘ | 35 | 1 | 6% | 3% | +167% | -90% | 12 min |
| Hungarian NB I Game | ✘ | 34 | 0 | 9% | 9% | -100% | -85% | 6 min |
| Brazil NBB Basketball Game | ✘ | 34 | 0 | 6% | 3% | -100% | -90% | 19 min |
| Korea KBL Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Austria BSL Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Turkey BSL Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Australian A League Game | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 6 min |
| Indian Super League Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 7 min |
| Austrian Bundesliga Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 12 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Russia VTB United Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 14 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Singapore Premier League Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 18 min |
| Croatia Premijer Liga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Eredivisie Vrouwen Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 8 min |
| German Women's Bundesliga Game | ✘ | 28 | 0 | 7% | 4% | -100% | -88% | 18 min |
| England Super League Basketball Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakia SBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 18 min |
| French Women's Première Ligue Game | ✘ | 25 | 0 | 12% | 8% | -100% | -79% | 6 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| LKL Lithuania Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 9 min |
| BNXT League Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 11 min |
| South African Premiership Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Slovenia 1. SKL Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 14 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| FIBA Champions League Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liga Nacional de Basquetbol Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Ligue Magnus Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Polish Hockey Game | ✘ | 21 | 0 | 5% | 5% | -100% | -92% | 5 min |
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
| Israel Super League Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 14 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Bundesliga Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Women's College Basketball Game | partly | 7 | 0 | 14% | 0% | -100% | -75% | 40 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| GBL Basketball Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Portugal LPB Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 35 min |
| State Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 137 min |
| Scottish Cup Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's College Basketball Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 44 min |
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
| Under 5 min | 958 | 4% | 1% | 0% | -93% |
| 5–15 min | 591 | 16% | 7% | 1% | -72% |
| 15–30 min | 401 | 23% | 12% | 1% | -59% |
| 30–60 min | 301 | 20% | 11% | 0% | -65% |
| Over 60 min | 204 | 20% | 11% | 0% | -65% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 37 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11-02 21:42 | eSoccer Game | Sunderland (Ousmane) | ✘ | — | — | In play | — |
| 11-02 21:42 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-02 21:42 | Counter-Strike 2 Game | Pandaric eSports | ✘ | — | — | In play | — |
| 11-02 21:42 | Challenger ATP  | Henrique Rocha | ✘ | — | — | In play | — |
| 11-02 21:41 | ITF Men's Match | Tomas Quesada Perez | ✘ | — | — | In play | — |
| 11-02 21:38 | Liga Portugal Game | Alverca | ✘ | — | — | In play | — |
| 11-02 21:35 | ITF Women's Match | Kennedy Gibbs | ✘ | — | — | In play | — |
| 11-02 21:35 | Men's College Basketball Game | UTEP | ✘ | — | — | In play | — |
| 11-02 21:34 | eSoccer Game | Manchester City (SilentShooter) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:33 | Ligue 2 Game | Tie | ✘ | — | — | In play | — |
| 11-02 21:33 | eSoccer Game | Leverkusen (Haze) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:31 | eSoccer Game | Manchester City (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:31 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:30 | eSoccer Game | France (Annie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:30 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:29 | eSoccer Game | Chelsea (Elastico) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:29 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:29 | Women's College Basketball Game | North Carolina | ✔ | 7:54 - 4th · OU 75 - UNC 60 | — | In play | — |
| 11-02 21:29 | Polish Ekstraklasa Game | Tie | ✘ | — | — | In play | — |
| 11-02 21:28 | eSoccer Game | United States (Mia) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:28 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:28 | Women's College Basketball Game | Wofford | ✘ | — | — | In play | — |
| 11-02 21:28 | Women's College Basketball Game | District of Columbia | ✘ | — | — | In play | — |
| 11-02 21:26 | Ligue 2 Game | Tie | ✘ | — | — | In play | — |
| 11-02 21:26 | Women's College Basketball Game | Saint Anselm | ✘ | — | — | In play | — |
| 11-02 21:26 | Serie C Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:25 | Men's College Basketball Game | UTSA | ✘ | — | — | In play | — |
| 11-02 21:23 | Serie C Game | Casarano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:22 | Italy Serie A Game | Pallacanestro Cantu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-02 21:21 | Serie A Game | Tie | ✔ | 78' · PAR 3 - ATA 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
