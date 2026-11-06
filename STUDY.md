# 1¢ Study

*Updated Fri Nov 6, 12:53 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

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
| ESPN win probability ≥ 2%, hold to the end | 115 | -$3.25 | -19% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 49821 | 2726 | 11 (0%) | 1.1% | -$254.90 (-62%) | Hold to the end: -$254.90 (-62%) |

*In play right now: 32. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 557 | 2.8% | 0.2% (1) | -92% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 557 | 1 | -83% | -70% | -70% | -71% |
| ESPN win probability ≥ 2% | 115 | 1 | -19% | -61% | -64% | -70% |
| ESPN win probability ≥ 5% | 49 | 1 | +90% | -79% | -79% | -82% |
| ESPN win probability ≥ 10% | 32 | 1 | +192% | -73% | -68% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2726 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 47063 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 11 | 0% | -$254.90 | -62% |
| Sell at 2¢ | 371 | 14% | -$312.44 | -76% |
| Sell at 3¢ | 261 | 10% | -$307.11 | -75% |
| Sell at 5¢ | 178 | 7% | -$293.20 | -72% |
| Sell at 10¢ | 78 | 3% | -$306.72 | -75% |
| Sell at 25¢ | 29 | 1% | -$312.91 | -77% |
| Sell at 50¢ | 19 | 1% | -$280.65 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 23274 | 12 | 1% | 0% | -95% | -99% | 3 min |
| Russia Liga Pro Match | ✘ | 2739 | 0 | 1% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 2285 | 3 | 2% | 1% | -88% | -93% | 2 min |
| ITF Women's Match | ✘ | 1618 | 6 | 13% | 6% | -65% | -77% | 4 min |
| ITF Men's Match | ✘ | 1530 | 3 | 13% | 6% | -82% | -77% | 5 min |
| Counter-Strike 2 Game | ✘ | 1447 | 2 | 6% | 3% | -87% | -90% | 11 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 927 | 3 | 11% | 4% | -70% | -81% | 5 min |
| eFootball Game | ✘ | 625 | 2 | 1% | 1% | -70% | -98% | 2 min |
| College Football Game | partly | 414 | 3 | 12% | 6% | -32% | -79% | 24 min |
| Darts Match | ✘ | 374 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's T20 Cricket Match | ✘ | 322 | 2 | 16% | 7% | -42% | -73% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Women's College Volleyball Match | ✘ | 316 | 2 | 5% | 3% | -41% | -92% | 67 min |
| Dota 2 Game | ✘ | 300 | 1 | 1% | 1% | -69% | -98% | 31 min |
| Serie C Game | ✘ | 285 | 2 | 5% | 2% | -35% | -92% | 6 min |
| Challenger WTA | ✘ | 278 | 1 | 13% | 4% | -66% | -78% | 9 min |
| NHL Game | ✔ | 260 | 2 | 15% | 8% | -28% | -75% | 5 min |
| Women's College Basketball Game | partly | 211 | 0 | 10% | 5% | -100% | -82% | 45 min |
| Men's College Basketball Game | partly | 201 | 3 | 19% | 8% | +39% | -67% | 46 min |
| Major League Soccer Game | partly | 187 | 1 | 12% | 6% | -50% | -80% | 8 min |
| NBA Game | ✔ | 183 | 0 | 18% | 5% | -100% | -69% | 9 min |
| WTA Tennis Match | ✘ | 180 | 0 | 12% | 2% | -100% | -80% | 5 min |
| AHL Game | ✘ | 172 | 0 | 4% | 2% | -100% | -93% | 5 min |
| League of Legends Game | ✘ | 158 | 0 | 8% | 2% | -100% | -87% | 11 min |
| Argentina Primera Division Game | ✘ | 149 | 2 | 15% | 9% | +25% | -74% | 7 min |
| Ettan Game | ✘ | 145 | 0 | 3% | 1% | -100% | -94% | 7 min |
| Argentine Nacional B Game | ✘ | 142 | 0 | 8% | 6% | -100% | -85% | 8 min |
| Japan J2 League Game | ✘ | 141 | 1 | 11% | 4% | -34% | -82% | 6 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| KHL Game | ✘ | 137 | 0 | 4% | 2% | -100% | -92% | 6 min |
| Liga DIMAYOR Game | ✘ | 133 | 1 | 11% | 3% | -30% | -82% | 7 min |
| Brasileiro Serie B Game | ✘ | 129 | 1 | 8% | 4% | -28% | -87% | 9 min |
| ATP Tennis Match | ✘ | 129 | 0 | 16% | 6% | -100% | -73% | 4 min |
| English National League Game | ✘ | 128 | 1 | 9% | 7% | -27% | -84% | 10 min |
| EFL Championship Game | ✔ | 124 | 0 | 8% | 5% | -100% | -86% | 10 min |
| College Hockey Game | ✘ | 122 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Overwatch Game | ✘ | 118 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Brasileiro Serie A Game | partly | 118 | 1 | 11% | 7% | -21% | -81% | 9 min |
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
| Women's T20 Match | ✘ | 91 | 0 | 16% | 4% | -100% | -71% | 26 min |
| Liga Leumit Game | ✘ | 90 | 0 | 4% | 3% | -100% | -92% | 18 min |
| National League Game | ✘ | 90 | 1 | 1% | 1% | +4% | -98% | 6 min |
| Valorant game winner | ✘ | 89 | 0 | 6% | 3% | -100% | -90% | 13 min |
| Peru Liga 1 Game | ✘ | 88 | 0 | 14% | 7% | -100% | -76% | 12 min |
| UEFA Europa League Game | partly | 88 | 1 | 16% | 8% | +6% | -72% | 11 min |
| UEFA Conference League Game | partly | 88 | 0 | 15% | 9% | -100% | -74% | 13 min |
| Eerste Divisie Game | ✘ | 87 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Liga Expansion Game | ✘ | 87 | 0 | 6% | 2% | -100% | -90% | 12 min |
| R6 Game | ✘ | 86 | 1 | 12% | 6% | +9% | -80% | 10 min |
| TFF 1. Lig Game | ✘ | 86 | 0 | 14% | 8% | -100% | -76% | 10 min |
| Slovakian 2. Liga Game | ✘ | 84 | 0 | 6% | 5% | -100% | -90% | 77 min |
| Indonesia Super League Game | ✘ | 84 | 0 | 14% | 8% | -100% | -75% | 9 min |
| Uruguay Primera Division Game | ✘ | 80 | 0 | 8% | 2% | -100% | -87% | 10 min |
| Euroleague Game | ✘ | 80 | 0 | 21% | 6% | -100% | -63% | 13 min |
| ELH Game | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| La Liga Game | ✔ | 78 | 0 | 18% | 12% | -100% | -69% | 9 min |
| Copa Del Rey Game | ✘ | 77 | 0 | 6% | 5% | -100% | -89% | 40 min |
| Saudi Pro League Game | ✘ | 76 | 2 | 18% | 12% | +146% | -68% | 13 min |
| Japan B League Game | ✘ | 75 | 0 | 7% | 0% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 73 | 0 | 10% | 5% | -100% | -83% | 9 min |
| Men's ODI Cricket Match | ✘ | 73 | 3 | 21% | 7% | +284% | -64% | 51 min |
| NFL Game | ✔ | 73 | 1 | 18% | 7% | +28% | -69% | 8 min |
| English Premier League Game | ✔ | 73 | 0 | 7% | 3% | -100% | -88% | 9 min |
| SHL Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 5 min |
| DEL Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Mobile Legends Bang Bang Game | ✘ | 72 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Ligue 2 Game | ✘ | 72 | 0 | 8% | 6% | -100% | -86% | 8 min |
| AFC Champions League Game | ✘ | 72 | 0 | 6% | 1% | -100% | -90% | 12 min |
| Polish Ekstraklasa Game | ✘ | 69 | 0 | 13% | 7% | -100% | -77% | 9 min |
| Allsvenskan Game | ✘ | 69 | 1 | 16% | 10% | +35% | -72% | 10 min |
| NWSL Game | ✔ | 68 | 0 | 7% | 1% | -100% | -87% | 7 min |
| APF Division de Honor Game | ✘ | 65 | 0 | 17% | 5% | -100% | -71% | 11 min |
| Bundesliga 2 Game | ✔ | 65 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Korea K-League 2 Game | ✘ | 64 | 0 | 11% | 6% | -100% | -81% | 7 min |
| Eliteserien Game | ✘ | 64 | 0 | 9% | 5% | -100% | -84% | 10 min |
| Turkish Super Lig Game | ✘ | 64 | 0 | 14% | 3% | -100% | -76% | 13 min |
| Ecuador Liga Pro Game | ✘ | 64 | 0 | 6% | 2% | -100% | -89% | 10 min |
| LNBP Basketball Game | ✘ | 63 | 0 | 10% | 2% | -100% | -83% | 12 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Bundesliga Game | ✔ | 63 | 1 | 16% | 10% | +48% | -72% | 7 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Eredivisie Game | ✔ | 62 | 0 | 10% | 8% | -100% | -83% | 5 min |
| Ligue 1 Game | ✔ | 62 | 0 | 16% | 6% | -100% | -72% | 9 min |
| Czech First League Game | ✘ | 61 | 0 | 10% | 0% | -100% | -83% | 9 min |
| Italy Serie A2 Game | ✘ | 60 | 0 | 2% | 0% | -100% | -97% | 6 min |
| Czech National Football League Game | ✘ | 60 | 0 | 12% | 7% | -100% | -80% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| LNB Elite 2 Game | ✘ | 58 | 0 | 2% | 0% | -100% | -97% | 7 min |
| Thai League 1 Game | ✘ | 58 | 0 | 17% | 7% | -100% | -70% | 11 min |
| Bolivia Premier Division Game | ✘ | 58 | 0 | 9% | 2% | -100% | -85% | 5 min |
| Israeli Premier League Game | ✘ | 56 | 0 | 7% | 2% | -100% | -88% | 9 min |
| KBO Game | ✘ | 55 | 0 | 11% | 5% | -100% | -81% | 5 min |
| FIBA Europe Cup Game | ✘ | 55 | 0 | 9% | 4% | -100% | -84% | 11 min |
| Liga Portugal Game | ✘ | 54 | 0 | 6% | 2% | -100% | -90% | 11 min |
| Finland Korisliiga Game | ✘ | 53 | 1 | 8% | 4% | +76% | -87% | 8 min |
| England Women's Super League Game | ✘ | 52 | 0 | 17% | 8% | -100% | -70% | 23 min |
| Vietnam V-League 1 Game | ✘ | 52 | 1 | 6% | 4% | +79% | -90% | 10 min |
| Belgian Pro League Game | ✘ | 52 | 0 | 8% | 0% | -100% | -87% | 15 min |
| Serbian SuperLiga Game | ✘ | 52 | 0 | 4% | 2% | -100% | -93% | 12 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Egyptian Premier League Game | ✘ | 50 | 0 | 6% | 6% | -100% | -90% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Super League Greece Game | ✘ | 49 | 0 | 20% | 4% | -100% | -65% | 12 min |
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
| Romanian Liga I Game | ✘ | 43 | 0 | 9% | 2% | -100% | -84% | 11 min |
| Brazil NBB Basketball Game | ✘ | 43 | 0 | 7% | 5% | -100% | -88% | 18 min |
| LNB Elite Game | ✘ | 42 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Czech NBL Game | ✘ | 41 | 0 | 2% | 0% | -100% | -96% | 18 min |
| Danish Superliga Game | ✘ | 41 | 0 | 10% | 5% | -100% | -83% | 10 min |
| Australia NBL Game | ✘ | 40 | 0 | 5% | 2% | -100% | -91% | 8 min |
| Faroe Islands Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 31 min |
| Italy Serie A Game | ✘ | 39 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Croatia HNL Game | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 8 min |
| Qatar Stars League | ✘ | 39 | 0 | 10% | 5% | -100% | -82% | 7 min |
| Sweden SBL Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 14 min |
| Indian Super League Game | ✘ | 38 | 0 | 16% | 8% | -100% | -73% | 8 min |
| Bundesliga Basketball Game | ✘ | 37 | 0 | 11% | 5% | -100% | -81% | 13 min |
| Latvian Virsliga Game | ✘ | 37 | 0 | 16% | 8% | -100% | -72% | 21 min |
| Slovenian Prva Liga Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 6 min |
| Japan NPB Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Champions League Women's Game | partly | 36 | 1 | 19% | 8% | +159% | -66% | 26 min |
| Canadian Premier League | ✘ | 35 | 1 | 14% | 14% | +167% | -75% | 22 min |
| Swiss Super League Game | ✘ | 35 | 1 | 6% | 3% | +167% | -90% | 12 min |
| Korea KBL Game | ✘ | 35 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Hungarian NB I Game | ✘ | 34 | 0 | 9% | 9% | -100% | -85% | 6 min |
| Russia VTB United Game | ✘ | 32 | 0 | 3% | 0% | -100% | -95% | 15 min |
| Austria BSL Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 10 min |
| Turkey BSL Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Australian A League Game | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 6 min |
| Austrian Bundesliga Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 12 min |
| DFB Pokal Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 18 min |
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
| Philippines PBA Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 10 min |
| EFL Cup Game | ✘ | 16 | 0 | 19% | 0% | -100% | -68% | 15 min |
| Coppa Italia Lega Pro Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 9 min |
| Greek Cup Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| Colombia LBP Basketball Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 16 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Powerslap Match Winner | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 7 min |
| Israel Super League Game | ✘ | 11 | 0 | 9% | 9% | -100% | -84% | 13 min |
| United Rugby Championship Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Bundesliga Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
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
| Call of Duty Games | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 1032 | 4% | 1% | 0% | -93% |
| 5–15 min | 639 | 16% | 8% | 1% | -72% |
| 15–30 min | 431 | 24% | 13% | 1% | -58% |
| 30–60 min | 326 | 21% | 11% | 1% | -64% |
| Over 60 min | 270 | 20% | 10% | 0% | -66% |

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
| 11-06 19:52 | eSoccer Game | France (Mei) | ✘ | — | — | In play | — |
| 11-06 19:52 | eSoccer Game | England (Trinity) | ✘ | — | — | In play | — |
| 11-06 19:52 | Women's College Basketball Game | Drexel | ✘ | — | — | In play | — |
| 11-06 19:52 | Call of Duty Games | Stallions | ✘ | — | — | In play | — |
| 11-06 19:52 | Eerste Divisie Game | Roda | ✘ | — | — | In play | — |
| 11-06 19:52 | French Women's Première Ligue Game | Toulouse | ✘ | — | — | In play | — |
| 11-06 19:51 | French Women's Première Ligue Game | Nantes | ✘ | — | — | In play | — |
| 11-06 19:51 | Sweden SBL Game | Sodertalje BBK | ✘ | — | — | In play | — |
| 11-06 19:51 | Danish Superliga Game | Tie | ✘ | — | — | In play | — |
| 11-06 19:50 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 11-06 19:48 | Argentina Primera Division Game | Tie | ✘ | — | — | In play | — |
| 11-06 19:47 | eSoccer Game | Spain (Lotta) | ✘ | — | — | In play | — |
| 11-06 19:45 | Call of Duty Games | FaZe Vegas | ✘ | — | — | In play | — |
| 11-06 19:44 | Call of Duty Games | M80 Boston | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | Sweden SBL Game | Hogsbo Basket | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | Sweden SBL Game | Uppsala Basket | ✘ | — | — | In play | — |
| 11-06 19:44 | Russia Liga Pro Match | Razinkov Dmitrii | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | Danish Superliga Game | Lyngby | ✘ | — | — | In play | — |
| 11-06 19:44 | eSoccer Game | Liverpool (Kovboj) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | Austrian Bundesliga Game | Wolfsberg | ✘ | — | — | In play | — |
| 11-06 19:44 | German 3. Liga Game | Saarbrucken | ✘ | — | — | In play | — |
| 11-06 19:44 | German 3. Liga Game | Tie | ✘ | — | — | In play | — |
| 11-06 19:44 | Argentina Primera Division Game | Racing Avellaneda | ✘ | — | — | In play | — |
| 11-06 19:44 | Dota 2 Game | Level Up Academy | ✘ | — | — | In play | — |
| 11-06 19:44 | French Women's Première Ligue Game | Montpellier | ✘ | — | — | In play | — |
| 11-06 19:44 | French Women's Première Ligue Game | Tie | ✘ | — | — | In play | — |
| 11-06 19:44 | Counter-Strike 2 Game | Thousand | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 19:44 | Counter-Strike 2 Game | QUINTESSENCIA | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 11-06 18:17 | eSoccer Game | Arsenal (Kovboj) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
