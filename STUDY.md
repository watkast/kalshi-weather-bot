# 1¢ Study

*Updated Wed Oct 28, 6:16 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 40 finished bets | 2% | $8.00 | +133% | +20.00¢ | $11.00 / -$3.00 |

*Expect about **2 buys a day**, roughly **$0.24/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 86 | $1.10 | +9% |
| ESPN win probability ≥ 5%, sell at 50¢ | 40 | $0.75 | +12% |
| ESPN win probability ≥ 5%, sell at 25¢ | 40 | $0.62 | +10% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 37171 | 2111 | 9 (0%) | 1.1% | -$190.65 (-60%) | Hold to the end: -$190.65 (-60%) |

*In play right now: 19. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 383 | 3.1% | 0.3% (1) | -76% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 383 | 1 | -76% | -73% | -73% | -71% |
| ESPN win probability ≥ 2% | 86 | 1 | +9% | -66% | -70% | -70% |
| ESPN win probability ≥ 5% | 40 | 1 | +133% | -78% | -80% | -78% |
| ESPN win probability ≥ 10% | 26 | 1 | +259% | -73% | -70% | -67% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2111 | 13% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 35041 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 9 | 0% | -$190.65 | -60% |
| Sell at 2¢ | 284 | 13% | -$242.81 | -77% |
| Sell at 3¢ | 198 | 9% | -$239.43 | -76% |
| Sell at 5¢ | 139 | 7% | -$226.30 | -71% |
| Sell at 10¢ | 63 | 3% | -$234.12 | -74% |
| Sell at 25¢ | 21 | 1% | -$247.14 | -78% |
| Sell at 50¢ | 14 | 1% | -$222.15 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 16557 | 9 | 1% | 1% | -95% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 1897 | 0 | 0% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1628 | 2 | 2% | 0% | -89% | -91% | 2 min |
| ITF Women's Match | ✘ | 1341 | 6 | 13% | 6% | -58% | -77% | 4 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 1242 | 1 | 13% | 5% | -92% | -78% | 5 min |
| Counter-Strike 2 Game | ✘ | 1177 | 2 | 5% | 3% | -84% | -91% | 11 min |
| Challenger ATP  | ✘ | 757 | 2 | 11% | 4% | -75% | -81% | 5 min |
| eFootball Game | ✘ | 373 | 2 | 1% | 1% | -50% | -99% | 2 min |
| College Football Game | partly | 335 | 2 | 11% | 6% | -44% | -80% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Darts Match | ✘ | 315 | 0 | 0% | 0% | -100% | -99% | 7 min |
| Men's T20 Cricket Match | ✘ | 264 | 1 | 14% | 5% | -65% | -75% | 23 min |
| Women's College Volleyball Match | ✘ | 256 | 2 | 5% | 3% | -27% | -91% | 72 min |
| Serie C Game | ✘ | 238 | 2 | 4% | 2% | -22% | -93% | 6 min |
| Dota 2 Game | ✘ | 235 | 0 | 1% | 1% | -100% | -99% | 30 min |
| Challenger WTA | ✘ | 213 | 0 | 13% | 4% | -100% | -78% | 8 min |
| NHL Game | ✔ | 198 | 1 | 12% | 6% | -53% | -80% | 4 min |
| League of Legends Game | ✘ | 152 | 0 | 7% | 2% | -100% | -89% | 11 min |
| WTA Tennis Match | ✘ | 150 | 0 | 11% | 2% | -100% | -82% | 5 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| AHL Game | ✘ | 130 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Major League Soccer Game | partly | 129 | 1 | 13% | 6% | -28% | -77% | 6 min |
| NBA Game | ✔ | 120 | 0 | 17% | 6% | -100% | -71% | 8 min |
| Ettan Game | ✘ | 117 | 0 | 4% | 1% | -100% | -93% | 7 min |
| Argentina Primera Division Game | ✘ | 116 | 1 | 14% | 8% | -20% | -76% | 7 min |
| KHL Game | ✘ | 113 | 0 | 5% | 3% | -100% | -91% | 5 min |
| Argentine Nacional B Game | ✘ | 112 | 0 | 9% | 6% | -100% | -85% | 8 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Brasileiro Serie B Game | ✘ | 107 | 1 | 7% | 4% | -13% | -87% | 8 min |
| English National League Game | ✘ | 104 | 1 | 10% | 7% | -10% | -83% | 11 min |
| Liga DIMAYOR Game | ✘ | 103 | 1 | 9% | 3% | -9% | -85% | 6 min |
| ATP Tennis Match | ✘ | 102 | 0 | 16% | 7% | -100% | -73% | 4 min |
| Japan J2 League Game | ✘ | 100 | 0 | 12% | 5% | -100% | -79% | 6 min |
| USL Championship Game | partly | 96 | 0 | 11% | 4% | -100% | -80% | 4 min |
| Overwatch Game | ✘ | 95 | 0 | 2% | 0% | -100% | -96% | 6 min |
| LaLiga 2 Game | partly | 89 | 1 | 18% | 9% | +5% | -69% | 9 min |
| EFL League One Game | ✔ | 88 | 0 | 10% | 3% | -100% | -82% | 10 min |
| Brasileiro Serie A Game | partly | 85 | 1 | 14% | 8% | +10% | -76% | 6 min |
| Liiga Game | ✘ | 81 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Japan J League Game | ✘ | 81 | 1 | 19% | 7% | +15% | -68% | 12 min |
| German 3. Liga Game | ✘ | 80 | 0 | 11% | 5% | -100% | -80% | 8 min |
| EFL Championship Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 9 min |
| National League Game | ✘ | 77 | 1 | 1% | 1% | +21% | -98% | 5 min |
| Valorant game winner | ✘ | 76 | 0 | 5% | 3% | -100% | -91% | 14 min |
| EuroCup Basketball Game | ✘ | 76 | 0 | 5% | 4% | -100% | -91% | 11 min |
| Serie B Game | ✘ | 76 | 0 | 14% | 7% | -100% | -75% | 9 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| College Hockey Game | ✘ | 75 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Chinese Basketball Association Game  | ✘ | 75 | 0 | 8% | 1% | -100% | -86% | 10 min |
| Serie A Game | ✔ | 74 | 0 | 8% | 5% | -100% | -86% | 12 min |
| Liga MX Game | ✔ | 73 | 0 | 15% | 10% | -100% | -74% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| TFF 1. Lig Game | ✘ | 72 | 0 | 17% | 10% | -100% | -71% | 10 min |
| Eerste Divisie Game | ✘ | 70 | 0 | 10% | 7% | -100% | -83% | 9 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| Euroleague Game | ✘ | 69 | 0 | 23% | 7% | -100% | -60% | 14 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| ELH Game | ✘ | 68 | 0 | 1% | 1% | -100% | -97% | 4 min |
| Uruguay Primera Division Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 10 min |
| Slovakian 2. Liga Game | ✘ | 66 | 0 | 5% | 5% | -100% | -92% | 85 min |
| Indonesia Super League Game | ✘ | 66 | 0 | 15% | 9% | -100% | -74% | 9 min |
| Peru Liga 1 Game | ✘ | 64 | 0 | 16% | 6% | -100% | -73% | 13 min |
| Liga Expansion Game | ✘ | 63 | 0 | 5% | 3% | -100% | -92% | 11 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| La Liga Game | ✔ | 60 | 0 | 22% | 15% | -100% | -62% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| DEL Game | ✘ | 59 | 0 | 0% | 0% | -100% | -100% | 5 min |
| SHL Game | ✘ | 58 | 0 | 3% | 3% | -100% | -94% | 6 min |
| NFL Game | ✔ | 58 | 1 | 19% | 9% | +61% | -67% | 5 min |
| China League 1 Game | ✘ | 57 | 0 | 12% | 7% | -100% | -79% | 10 min |
| Mobile Legends Bang Bang Game | ✘ | 57 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Saudi Pro League Game | ✘ | 57 | 1 | 18% | 11% | +64% | -70% | 13 min |
| Allsvenskan Game | ✘ | 57 | 1 | 16% | 12% | +64% | -73% | 10 min |
| AFC Champions League Game | ✘ | 56 | 0 | 5% | 0% | -100% | -91% | 8 min |
| Polish Ekstraklasa Game | ✘ | 55 | 0 | 13% | 7% | -100% | -78% | 8 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| Women's T20 Match | ✘ | 54 | 0 | 15% | 7% | -100% | -74% | 24 min |
| Bundesliga 2 Game | ✔ | 54 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Ligue 2 Game | ✘ | 54 | 0 | 11% | 7% | -100% | -81% | 7 min |
| English Premier League Game | ✔ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| NWSL Game | ✔ | 52 | 0 | 10% | 2% | -100% | -83% | 7 min |
| Men's ODI Cricket Match | ✘ | 52 | 3 | 21% | 10% | +438% | -63% | 48 min |
| Turkish Super Lig Game | ✘ | 52 | 0 | 13% | 2% | -100% | -77% | 13 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Eredivisie Game | ✔ | 51 | 0 | 10% | 8% | -100% | -83% | 4 min |
| Japan B League Game | ✘ | 51 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Ligue 1 Game | ✔ | 50 | 0 | 18% | 8% | -100% | -69% | 8 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Italy Serie A2 Game | ✘ | 49 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Korea K-League 2 Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Thai League 1 Game | ✘ | 48 | 0 | 19% | 6% | -100% | -68% | 10 min |
| Eliteserien Game | ✘ | 48 | 0 | 10% | 4% | -100% | -82% | 12 min |
| Ecuador Liga Pro Game | ✘ | 48 | 0 | 8% | 2% | -100% | -86% | 8 min |
| LNB Elite 2 Game | ✘ | 47 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Copa Del Rey Game | ✘ | 47 | 0 | 6% | 6% | -100% | -89% | 41 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Czech National Football League Game | ✘ | 47 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Czech First League Game | ✘ | 45 | 0 | 11% | 0% | -100% | -81% | 8 min |
| Bundesliga Game | ✔ | 45 | 1 | 13% | 9% | +107% | -77% | 6 min |
| Bolivia Premier Division Game | ✘ | 44 | 0 | 11% | 2% | -100% | -80% | 8 min |
| Serbian SuperLiga Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 11 min |
| Finland Korisliiga Game | ✘ | 42 | 1 | 7% | 5% | +122% | -88% | 9 min |
| England Women's Super League Game | ✘ | 42 | 0 | 21% | 10% | -100% | -63% | 26 min |
| Israeli Premier League Game | ✘ | 42 | 0 | 5% | 0% | -100% | -92% | 9 min |
| APF Division de Honor Game | ✘ | 41 | 0 | 20% | 7% | -100% | -66% | 6 min |
| Scottish Premiership Game | ✘ | 41 | 0 | 12% | 2% | -100% | -79% | 10 min |
| Super League Greece Game | ✘ | 39 | 0 | 18% | 5% | -100% | -69% | 14 min |
| FIBA Europe Cup Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 8 min |
| Adriatic ABA Game | ✘ | 38 | 0 | 5% | 3% | -100% | -91% | 11 min |
| Venezuela Liga FUTVE game | ✘ | 38 | 0 | 18% | 13% | -100% | -68% | 6 min |
| Vietnam V-League 1 Game | ✘ | 37 | 1 | 8% | 5% | +152% | -86% | 10 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Serie A Femminile Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Spain Liga ACB Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Danish Superliga Game | ✘ | 36 | 0 | 11% | 6% | -100% | -81% | 11 min |
| Liga Portugal Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 10 min |
| Egyptian Premier League Game | ✘ | 35 | 0 | 6% | 6% | -100% | -90% | 7 min |
| KNVB Cup Game | ✘ | 35 | 0 | 14% | 11% | -100% | -75% | 13 min |
| Belgian Pro League Game | ✘ | 34 | 0 | 9% | 0% | -100% | -85% | 18 min |
| Sweden SBL Game | ✘ | 33 | 0 | 6% | 6% | -100% | -89% | 14 min |
| LNB Elite Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Rugby French 14 Match | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Chile Liga de Primera Game | ✘ | 32 | 0 | 12% | 0% | -100% | -78% | 7 min |
| Italy Serie A Game | ✘ | 32 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Spanish Liga F Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 7 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
| Australia NBL Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 8 min |
| Czech NBL Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 16 min |
| Canadian Premier League | ✘ | 31 | 1 | 16% | 16% | +201% | -72% | 23 min |
| Latvian Virsliga Game | ✘ | 31 | 0 | 13% | 3% | -100% | -78% | 18 min |
| Faroe Islands Premier League Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 84 min |
| Romanian Liga I Game | ✘ | 30 | 0 | 10% | 3% | -100% | -83% | 12 min |
| Champions League Women's Game | partly | 29 | 1 | 17% | 7% | +222% | -70% | 26 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Croatia HNL Game | ✘ | 29 | 0 | 10% | 7% | -100% | -82% | 10 min |
| Russia VTB United Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 15 min |
| Austria BSL Game | ✘ | 27 | 0 | 11% | 7% | -100% | -81% | 8 min |
| Bundesliga Basketball Game | ✘ | 27 | 0 | 15% | 7% | -100% | -74% | 12 min |
| Turkey BSL Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Slovenian Prva Liga Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 6 min |
| German Women's Bundesliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 18 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Singapore Premier League Game | ✘ | 24 | 0 | 12% | 0% | -100% | -78% | 18 min |
| Swiss Super League Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 18 min |
| Korea KBL Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Indian Super League Game | ✘ | 24 | 0 | 12% | 8% | -100% | -78% | 8 min |
| Qatar Stars League | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 7 min |
| Austrian Bundesliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 11 min |
| Hungarian NB I Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 6 min |
| Brazil NBB Basketball Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 16 min |
| Professional Baseball Game | partly | 22 | 0 | 14% | 9% | -100% | -76% | 2 min |
| Croatia Premijer Liga Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 9 min |
| FIBA Champions League Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Australian A League Game | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 6 min |
| Slovakia SBL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| England Super League Basketball Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 8 min |
| Women's ODI Cricket Match | ✘ | 19 | 0 | 21% | 11% | -100% | -64% | 61 min |
| Slovenia 1. SKL Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 15 min |
| Women's Pro Basketball Game | ✔ | 17 | 0 | 18% | 6% | -100% | -69% | 6 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| CFL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| BNXT League Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Ligue Magnus Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Liga Nacional de Basquetbol Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 5 min |
| French Women's Première Ligue Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 6 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| EFL Cup Game | ✘ | 14 | 0 | 14% | 0% | -100% | -75% | 14 min |
| Polish Hockey Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 6 min |
| EuroLeague (W) Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Greek Cup Game | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 12 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Philippines PBA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| United Rugby Championship Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
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
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Portugal LPB Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 49 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| US Open Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 52 min |
| Serbia KLS Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Denmark Basketligaen Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 21 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NBL Australia (W) Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Hungary NB I. A Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 855 | 5% | 1% | 0% | -92% |
| 5–15 min | 491 | 17% | 8% | 1% | -71% |
| 15–30 min | 329 | 25% | 14% | 1% | -56% |
| 30–60 min | 238 | 20% | 12% | 0% | -66% |
| Over 60 min | 178 | 19% | 10% | 0% | -68% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 40 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-29 00:14 | League of Legends Game | LYON | ✘ | — | — | In play | — |
| 10-29 00:12 | eSoccer Game | CA Osasuna (Drakon) | ✘ | — | — | In play | — |
| 10-29 00:12 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-29 00:12 | eBasketball Game | New York Knicks (Larry) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:12 | Brazil NBB Basketball Game | Sao Jose dos Campos | ✘ | — | — | In play | — |
| 10-29 00:11 | Brasileiro Serie A Game | Tie | ✔ | 82' · CHA 0 - BRA 2 | — | In play | — |
| 10-29 00:10 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-29 00:09 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:09 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:09 | eSoccer Game | Universitario (Kevin) | ✘ | — | — | In play | — |
| 10-29 00:08 | eSoccer Game | Boca Juniors (Bradley) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:08 | eSoccer Game | Palmeiras (Kylian) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:08 | eSoccer Game | Chelsea (Kate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:07 | eSoccer Game | Arsenal (Rose) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:05 | Russia Liga Pro Match | Mameka Maksim | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:04 | eBasketball Game | Brooklyn Nets (Kyle) | ✘ | — | — | In play | — |
| 10-29 00:03 | eFootball Game | Detroit (Walter) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:02 | Russia Liga Pro Match | Lebedev Denis | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:00 | eSoccer Game | Girona (Dzen) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-29 00:00 | eSoccer Game | RC Celta (Minjori) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:57 | eSoccer Game | Universitario (Kevin) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:57 | Russia Liga Pro Match | Konobeev Aleksei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:57 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:55 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:54 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:53 | eSoccer Game | Arsenal (Rose) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:53 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:53 | eSoccer Game | Palmeiras (Kylian) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:53 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-28 23:43 | eBasketball Game | New Orleans Pelicans (Tim) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
