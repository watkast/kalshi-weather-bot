# 1¢ Study

*Updated Sat Oct 24, 8:02 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

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
| 28913 | 1742 | 7 (0%) | 1.1% | -$163.30 (-62%) | Hold to the end: -$163.30 (-62%) |

*In play right now: 38. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 1742 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 27133 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$163.30 | -62% |
| Sell at 2¢ | 244 | 14% | -$197.86 | -76% |
| Sell at 3¢ | 167 | 10% | -$196.17 | -75% |
| Sell at 5¢ | 115 | 7% | -$186.55 | -71% |
| Sell at 10¢ | 54 | 3% | -$190.56 | -73% |
| Sell at 25¢ | 16 | 1% | -$208.34 | -80% |
| Sell at 50¢ | 10 | 1% | -$193.80 | -74% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 12459 | 5 | 0% | 0% | -96% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Russia Liga Pro Match | ✘ | 1274 | 0 | 0% | 0% | -100% | -100% | 4 min |
| eBasketball Game | ✘ | 1238 | 1 | 1% | 0% | -92% | -91% | 2 min |
| ITF Women's Match | ✘ | 1077 | 2 | 13% | 5% | -83% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 1009 | 2 | 5% | 3% | -81% | -92% | 11 min |
| ITF Men's Match | ✘ | 983 | 1 | 12% | 5% | -91% | -79% | 5 min |
| Challenger ATP  | ✘ | 644 | 2 | 11% | 4% | -71% | -81% | 5 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 275 | 2 | 13% | 7% | -32% | -77% | 23 min |
| Darts Match | ✘ | 249 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 230 | 2 | 6% | 3% | -19% | -89% | 73 min |
| Men's T20 Cricket Match | ✘ | 226 | 1 | 14% | 4% | -59% | -75% | 25 min |
| Dota 2 Game | ✘ | 204 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Serie C Game | ✘ | 184 | 2 | 5% | 3% | +1% | -92% | 7 min |
| eFootball Game | ✘ | 175 | 0 | 0% | 0% | -100% | -100% | 2 min |
| NHL Game | ✔ | 166 | 0 | 11% | 5% | -100% | -81% | 4 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| League of Legends Game | ✘ | 139 | 0 | 7% | 2% | -100% | -88% | 11 min |
| WTA Tennis Match | ✘ | 132 | 0 | 11% | 2% | -100% | -82% | 5 min |
| AHL Game | ✘ | 111 | 0 | 3% | 2% | -100% | -95% | 5 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 101 | 1 | 11% | 4% | -8% | -81% | 6 min |
| Ettan Game | ✘ | 97 | 0 | 5% | 1% | -100% | -91% | 6 min |
| KHL Game | ✘ | 95 | 0 | 6% | 3% | -100% | -89% | 5 min |
| Argentina Primera Division Game | ✘ | 92 | 1 | 16% | 9% | +1% | -72% | 6 min |
| NBA Game | ✔ | 92 | 0 | 15% | 5% | -100% | -74% | 7 min |
| Brasileiro Serie B Game | ✘ | 90 | 0 | 8% | 3% | -100% | -87% | 9 min |
| ATP Tennis Match | ✘ | 89 | 0 | 13% | 7% | -100% | -77% | 4 min |
| Japan J2 League Game | ✘ | 84 | 0 | 14% | 6% | -100% | -75% | 7 min |
| Liga DIMAYOR Game | ✘ | 83 | 1 | 10% | 4% | +12% | -83% | 6 min |
| Overwatch Game | ✘ | 81 | 0 | 2% | 0% | -100% | -96% | 5 min |
| Argentine Nacional B Game | ✘ | 76 | 0 | 9% | 8% | -100% | -84% | 8 min |
| R6 Game | ✘ | 73 | 0 | 8% | 3% | -100% | -86% | 9 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| USL Championship Game | partly | 72 | 0 | 12% | 3% | -100% | -78% | 5 min |
| Japan J League Game | ✘ | 70 | 0 | 17% | 7% | -100% | -70% | 13 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| LaLiga 2 Game | partly | 68 | 0 | 21% | 9% | -100% | -64% | 8 min |
| Eerste Divisie Game | ✘ | 68 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Brasileiro Serie A Game | partly | 67 | 1 | 15% | 9% | +39% | -74% | 8 min |
| Liiga Game | ✘ | 66 | 0 | 0% | 0% | -100% | -100% | 5 min |
| German 3. Liga Game | ✘ | 66 | 0 | 12% | 5% | -100% | -79% | 7 min |
| English National League Game | ✘ | 63 | 0 | 8% | 5% | -100% | -86% | 11 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| National League Game | ✘ | 62 | 1 | 2% | 2% | +51% | -97% | 5 min |
| EFL Championship Game | ✔ | 62 | 0 | 10% | 5% | -100% | -83% | 9 min |
| Valorant game winner | ✘ | 60 | 0 | 3% | 2% | -100% | -94% | 14 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| EFL League One Game | ✔ | 60 | 0 | 13% | 5% | -100% | -77% | 11 min |
| College Hockey Game | ✘ | 60 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga MX Game | ✔ | 59 | 0 | 15% | 8% | -100% | -74% | 5 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| TFF 1. Lig Game | ✘ | 59 | 0 | 17% | 10% | -100% | -71% | 10 min |
| Chinese Basketball Association Game  | ✘ | 58 | 0 | 7% | 2% | -100% | -88% | 10 min |
| ELH Game | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 5 min |
| Uruguay Primera Division Game | ✘ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| Liga Expansion Game | ✘ | 53 | 0 | 6% | 4% | -100% | -90% | 10 min |
| Mobile Legends Bang Bang Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| China League 1 Game | ✘ | 51 | 0 | 12% | 6% | -100% | -80% | 10 min |
| DEL Game | ✘ | 51 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 100 min |
| Indonesia Super League Game | ✘ | 50 | 0 | 12% | 6% | -100% | -79% | 9 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| SHL Game | ✘ | 49 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Saudi Pro League Game | ✘ | 49 | 1 | 18% | 12% | +90% | -68% | 13 min |
| Ligue 2 Game | ✘ | 48 | 0 | 12% | 8% | -100% | -78% | 7 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Bundesliga 2 Game | ✔ | 46 | 0 | 13% | 7% | -100% | -77% | 7 min |
| NFL Game | ✔ | 45 | 1 | 22% | 9% | +107% | -61% | 4 min |
| LNB Elite 2 Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Women's T20 Match | ✘ | 43 | 0 | 19% | 9% | -100% | -68% | 27 min |
| Polish Ekstraklasa Game | ✘ | 43 | 0 | 14% | 7% | -100% | -76% | 9 min |
| NWSL Game | ✔ | 42 | 0 | 7% | 0% | -100% | -88% | 7 min |
| Peru Liga 1 Game | ✘ | 42 | 0 | 14% | 10% | -100% | -75% | 10 min |
| La Liga Game | ✔ | 42 | 0 | 29% | 21% | -100% | -50% | 8 min |
| Czech National Football League Game | ✘ | 41 | 0 | 12% | 7% | -100% | -79% | 7 min |
| Serie A Game | ✔ | 41 | 0 | 7% | 7% | -100% | -87% | 12 min |
| Japan B League Game | ✘ | 40 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Italy Serie A2 Game | ✘ | 39 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Turkish Super Lig Game | ✘ | 38 | 0 | 16% | 0% | -100% | -73% | 13 min |
| Serie B Game | ✘ | 38 | 0 | 16% | 8% | -100% | -73% | 9 min |
| Eredivisie Game | ✔ | 38 | 0 | 11% | 8% | -100% | -82% | 5 min |
| Ligue 1 Game | ✔ | 38 | 0 | 18% | 8% | -100% | -68% | 9 min |
| English Premier League Game | ✔ | 38 | 0 | 11% | 5% | -100% | -82% | 7 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Finland Korisliiga Game | ✘ | 36 | 1 | 6% | 6% | +159% | -90% | 9 min |
| Korea K-League 2 Game | ✘ | 36 | 0 | 17% | 8% | -100% | -71% | 9 min |
| Thai League 1 Game | ✘ | 36 | 0 | 25% | 8% | -100% | -57% | 10 min |
| Allsvenskan Game | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 11 min |
| Men's ODI Cricket Match | ✘ | 34 | 1 | 15% | 3% | +175% | -75% | 44 min |
| Ecuador Liga Pro Game | ✘ | 34 | 0 | 9% | 3% | -100% | -85% | 5 min |
| Serbian SuperLiga Game | ✘ | 34 | 0 | 3% | 0% | -100% | -95% | 12 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| APF Division de Honor Game | ✘ | 33 | 0 | 12% | 3% | -100% | -79% | 6 min |
| Adriatic ABA Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 10 min |
| Vietnam V-League 1 Game | ✘ | 33 | 1 | 9% | 6% | +183% | -84% | 10 min |
| Eliteserien Game | ✘ | 32 | 0 | 12% | 6% | -100% | -78% | 16 min |
| Czech First League Game | ✘ | 31 | 0 | 16% | 0% | -100% | -72% | 9 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| England Women's Super League Game | ✘ | 30 | 0 | 20% | 7% | -100% | -65% | 38 min |
| Bolivia Premier Division Game | ✘ | 30 | 0 | 17% | 3% | -100% | -71% | 3 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Bundesliga Game | ✔ | 29 | 1 | 17% | 10% | +222% | -70% | 5 min |
| Sweden SBL Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 15 min |
| Australia NBL Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| Israeli Premier League Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Venezuela Liga FUTVE game | ✘ | 28 | 0 | 18% | 14% | -100% | -69% | 6 min |
| Spain Liga ACB Game | ✘ | 27 | 0 | 7% | 4% | -100% | -87% | 17 min |
| Serie A Femminile Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Danish Superliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 11 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| LNB Elite Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Super League Greece Game | ✘ | 25 | 0 | 24% | 8% | -100% | -58% | 13 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Russia VTB United Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Italy Serie A Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Czech NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 18 min |
| Latvian Virsliga Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Spanish Liga F Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Professional Baseball Game | partly | 21 | 0 | 14% | 10% | -100% | -75% | 2 min |
| Turkey BSL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Bundesliga Basketball Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 12 min |
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
| Singapore Premier League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 15 min |
| Korea KBL Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Australian A League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 6 min |
| Romanian Liga I Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 8 min |
| German Women's Bundesliga Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 29 min |
| England Super League Basketball Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Women's ODI Cricket Match | ✘ | 16 | 0 | 19% | 6% | -100% | -68% | 56 min |
| Brazil NBB Basketball Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Women's Pro Basketball Game | ✔ | 15 | 0 | 20% | 7% | -100% | -65% | 6 min |
| Slovenia 1. SKL Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 19 min |
| Slovakia SBL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 21 min |
| LKL Lithuania Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| CFL Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Indian Super League Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 12 min |
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
| United Rugby Championship Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
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
| Under 5 min | 706 | 5% | 1% | 0% | -91% |
| 5–15 min | 397 | 18% | 8% | 1% | -69% |
| 15–30 min | 263 | 28% | 15% | 1% | -52% |
| 30–60 min | 196 | 19% | 11% | 0% | -67% |
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
| 10-24 14:02 | eSoccer Game | AS Monaco (Frenkie) | ✘ | — | — | In play | — |
| 10-24 14:02 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-24 14:00 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-24 13:59 | eSoccer Game | Rennes (Hazard) | ✘ | — | — | In play | — |
| 10-24 13:59 | Russia Liga Pro Match | Shmakov Andrey | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:58 | eSoccer Game | Manchester Utd (Florie) | ✘ | — | — | In play | — |
| 10-24 13:58 | eSoccer Game | Chelsea (Olive) | ✘ | — | — | In play | — |
| 10-24 13:57 | Men's ODI Cricket Match | Qatar | ✘ | — | — | In play | — |
| 10-24 13:57 | Indonesia Super League Game | Malut United | ✘ | — | — | In play | — |
| 10-24 13:57 | Indonesia Super League Game | Persijap Jepara | ✘ | — | — | In play | — |
| 10-24 13:56 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-24 13:54 | German 3. Liga Game | Duisburg | ✘ | — | — | In play | — |
| 10-24 13:53 | Russia Liga Pro Match | KHurudzhi Aleksandr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:53 | Ligue 2 Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:53 | German 3. Liga Game | Dusseldorf | ✘ | — | — | In play | — |
| 10-24 13:53 | German 3. Liga Game | Rostock | ✘ | — | — | In play | — |
| 10-24 13:53 | Russia Liga Pro Match | Sitnikov Roman | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:53 | LaLiga 2 Game | Tie | ✔ | 87' · EIB 0 - COR 2 | — | In play | — |
| 10-24 13:52 | eFootball Game | Buffalo (Charlie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:52 | Ligue 2 Game | Dijon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:52 | Darts Match | Damon Heta | ✘ | — | — | In play | — |
| 10-24 13:51 | GBL Basketball Game | AO Mykonoy | ✘ | — | — | In play | — |
| 10-24 13:50 | eSoccer Game | FC Bayern (Krocs) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:49 | eSoccer Game | Leverkusen (Haze) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:49 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 10-24 13:48 | TFF 1. Lig Game | Istanbulspor | ✘ | — | — | In play | — |
| 10-24 13:48 | eSoccer Game | AS Monaco (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:48 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:47 | ATP Tennis Match | Joel Schwaerzler | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-24 13:47 | United Rugby Championship Match | Ulster Rugby | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
