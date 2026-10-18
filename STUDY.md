# 1¢ Study

*Updated Sun Oct 18, 11:03 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 2%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 60 finished bets | 2% | $5.00 | +56% | +8.33¢ | -$4.50 / $9.50 |

*Expect about **3 buys a day**, roughly **$0.48/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, sell at 50¢ | 60 | -$2.25 | -25% |
| ESPN win probability ≥ 2%, sell at 25¢ | 60 | -$5.69 | -63% |
| ESPN win probability ≥ 2%, sell at 2¢ | 60 | -$5.88 | -65% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 19607 | 1404 | 7 (0%) | 1.1% | -$112.60 (-53%) | Hold to the end: -$112.60 (-53%) |

*In play right now: 52. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 268 | 3.3% | 0.4% (1) | -55% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 268 | 1 | -65% | -75% | -76% | -74% |
| ESPN win probability ≥ 2% | 60 | 1 | +56% | -65% | -70% | -78% |
| ESPN win probability ≥ 5% | 29 | 1 | +222% | -82% | -82% | -85% |
| ESPN win probability ≥ 10% | 18 | 1 | +419% | -81% | -71% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1404 | 14% | 10% | 7% | 3% | 1% | 1% |
| Unverified | 18151 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 7 | 0% | -$112.60 | -53% |
| Sell at 2¢ | 199 | 14% | -$158.86 | -75% |
| Sell at 3¢ | 134 | 10% | -$158.34 | -75% |
| Sell at 5¢ | 92 | 7% | -$150.80 | -72% |
| Sell at 10¢ | 48 | 3% | -$147.72 | -70% |
| Sell at 25¢ | 15 | 1% | -$160.95 | -76% |
| Sell at 50¢ | 10 | 1% | -$143.10 | -68% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 7261 | 4 | 1% | 1% | -95% | -99% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 776 | 1 | 12% | 5% | -88% | -79% | 4 min |
| eBasketball Game | ✘ | 741 | 1 | 0% | 0% | -87% | -87% | 2 min |
| Counter-Strike 2 Game | ✘ | 729 | 1 | 5% | 2% | -87% | -92% | 11 min |
| ITF Men's Match | ✘ | 712 | 1 | 12% | 6% | -87% | -79% | 5 min |
| Challenger ATP  | ✘ | 523 | 2 | 10% | 4% | -64% | -82% | 5 min |
| Russia Liga Pro Match | ✘ | 504 | 0 | 0% | 0% | -100% | -100% | 4 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| College Football Game | partly | 262 | 2 | 13% | 7% | -29% | -77% | 24 min |
| Darts Match | ✘ | 226 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Women's College Volleyball Match | ✘ | 190 | 2 | 7% | 3% | -2% | -88% | 80 min |
| Men's T20 Cricket Match | ✘ | 177 | 1 | 12% | 4% | -47% | -78% | 25 min |
| Dota 2 Game | ✘ | 166 | 0 | 1% | 1% | -100% | -98% | 30 min |
| Challenger WTA | ✘ | 159 | 0 | 12% | 4% | -100% | -79% | 8 min |
| Serie C Game | ✘ | 151 | 1 | 5% | 3% | -38% | -92% | 8 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| NHL Game | ✔ | 133 | 0 | 13% | 6% | -100% | -78% | 5 min |
| League of Legends Game | ✘ | 132 | 0 | 8% | 2% | -100% | -87% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Major League Soccer Game | partly | 97 | 1 | 11% | 4% | -4% | -80% | 6 min |
| AHL Game | ✘ | 87 | 0 | 2% | 1% | -100% | -96% | 5 min |
| Ettan Game | ✘ | 85 | 0 | 5% | 1% | -100% | -92% | 6 min |
| Brasileiro Serie B Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 10 min |
| KHL Game | ✘ | 73 | 0 | 4% | 3% | -100% | -93% | 5 min |
| Argentina Primera Division Game | ✘ | 71 | 0 | 14% | 6% | -100% | -76% | 7 min |
| Overwatch Game | ✘ | 70 | 0 | 3% | 0% | -100% | -95% | 5 min |
| WTA Tennis Match | ✘ | 68 | 0 | 12% | 1% | -100% | -80% | 4 min |
| Argentine Nacional B Game | ✘ | 66 | 0 | 9% | 9% | -100% | -84% | 10 min |
| R6 Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 9 min |
| USL Championship Game | partly | 66 | 0 | 14% | 3% | -100% | -76% | 5 min |
| NBA Game | ✔ | 64 | 0 | 12% | 3% | -100% | -78% | 7 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Japan J2 League Game | ✘ | 60 | 0 | 15% | 7% | -100% | -74% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| English National League Game | ✘ | 59 | 0 | 7% | 5% | -100% | -88% | 10 min |
| LaLiga 2 Game | partly | 58 | 0 | 21% | 10% | -100% | -64% | 9 min |
| German 3. Liga Game | ✘ | 58 | 0 | 12% | 5% | -100% | -79% | 7 min |
| ATP Tennis Match | ✘ | 57 | 0 | 12% | 5% | -100% | -79% | 3 min |
| Liga DIMAYOR Game | ✘ | 55 | 1 | 13% | 4% | +70% | -78% | 7 min |
| Brasileiro Serie A Game | partly | 55 | 1 | 18% | 11% | +70% | -68% | 8 min |
| EFL Championship Game | ✔ | 53 | 0 | 8% | 4% | -100% | -87% | 8 min |
| KBO Game | ✘ | 52 | 0 | 10% | 6% | -100% | -83% | 4 min |
| Liiga Game | ✘ | 52 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Liga Leumit Game | ✘ | 50 | 0 | 2% | 2% | -100% | -97% | 64 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Euroleague Game | ✘ | 49 | 0 | 24% | 8% | -100% | -58% | 14 min |
| National League Game | ✘ | 49 | 1 | 2% | 2% | +90% | -96% | 5 min |
| Eerste Divisie Game | ✘ | 49 | 0 | 8% | 6% | -100% | -86% | 11 min |
| Uruguay Primera Division Game | ✘ | 48 | 0 | 6% | 4% | -100% | -89% | 10 min |
| Slovakian 2. Liga Game | ✘ | 48 | 0 | 6% | 6% | -100% | -89% | 100 min |
| Liga Expansion Game | ✘ | 47 | 0 | 6% | 4% | -100% | -89% | 10 min |
| EuroCup Basketball Game | ✘ | 44 | 0 | 5% | 2% | -100% | -92% | 9 min |
| Tweede Divisie Game | ✘ | 44 | 0 | 2% | 0% | -100% | -96% | 4 min |
| Mobile Legends Bang Bang Game | ✘ | 44 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Taca de Portugal Game | ✘ | 44 | 0 | 16% | 5% | -100% | -72% | 11 min |
| College Hockey Game | ✘ | 43 | 0 | 0% | 0% | -100% | -100% | 6 min |
| TFF 1. Lig Game | ✘ | 43 | 0 | 14% | 7% | -100% | -76% | 8 min |
| ELH Game | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 5 min |
| China League 1 Game | ✘ | 41 | 0 | 7% | 5% | -100% | -87% | 9 min |
| SHL Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 5 min |
| DEL Game | ✘ | 41 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LNBP Basketball Game | ✘ | 40 | 0 | 8% | 0% | -100% | -87% | 16 min |
| Japan J League Game | ✘ | 40 | 0 | 15% | 5% | -100% | -74% | 13 min |
| Women's T20 Match | ✘ | 37 | 0 | 19% | 11% | -100% | -67% | 25 min |
| Chinese Basketball Association Game  | ✘ | 37 | 0 | 3% | 0% | -100% | -95% | 10 min |
| UEFA Champions League Game | partly | 37 | 1 | 14% | 5% | +152% | -77% | 12 min |
| Bundesliga 2 Game | ✔ | 36 | 0 | 14% | 6% | -100% | -76% | 8 min |
| UEFA Conference League Game | partly | 36 | 0 | 19% | 8% | -100% | -66% | 10 min |
| Liga MX Game | ✔ | 35 | 0 | 11% | 9% | -100% | -80% | 2 min |
| EFL League One Game | ✔ | 35 | 0 | 11% | 3% | -100% | -80% | 5 min |
| UEFA Europa League Game | partly | 35 | 0 | 20% | 9% | -100% | -65% | 11 min |
| Ligue 2 Game | ✘ | 34 | 0 | 18% | 12% | -100% | -69% | 7 min |
| Japan NPB Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Polish Ekstraklasa Game | ✘ | 33 | 0 | 9% | 3% | -100% | -84% | 8 min |
| Valorant game winner | ✘ | 32 | 0 | 6% | 3% | -100% | -89% | 15 min |
| NFL Game | ✔ | 32 | 1 | 19% | 6% | +192% | -68% | 3 min |
| Korea K-League 2 Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Indonesia Super League Game | ✘ | 32 | 0 | 16% | 6% | -100% | -73% | 8 min |
| Thai League 1 Game | ✘ | 32 | 0 | 22% | 9% | -100% | -62% | 8 min |
| Serie B Game | ✘ | 32 | 0 | 19% | 9% | -100% | -68% | 11 min |
| Eredivisie Game | ✔ | 32 | 0 | 9% | 6% | -100% | -84% | 5 min |
| La Liga Game | ✔ | 32 | 0 | 31% | 22% | -100% | -46% | 6 min |
| Chinese Super League Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 18 min |
| Czech National Football League Game | ✘ | 31 | 0 | 10% | 10% | -100% | -83% | 9 min |
| Serie A Game | ✔ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| NWSL Game | ✔ | 30 | 0 | 10% | 0% | -100% | -83% | 7 min |
| Peru Liga 1 Game | ✘ | 30 | 0 | 17% | 13% | -100% | -71% | 10 min |
| Turkish Super Lig Game | ✘ | 30 | 0 | 17% | 0% | -100% | -71% | 14 min |
| English Premier League Game | ✔ | 30 | 0 | 13% | 7% | -100% | -77% | 12 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Czech First League Game | ✘ | 29 | 0 | 14% | 0% | -100% | -76% | 9 min |
| Allsvenskan Game | ✘ | 29 | 0 | 14% | 14% | -100% | -76% | 12 min |
| Finland Korisliiga Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 28 | 0 | 0% | 0% | -100% | -100% | 7 min |
| England Women's Super League Game | ✘ | 28 | 0 | 21% | 7% | -100% | -63% | 39 min |
| Eliteserien Game | ✘ | 28 | 0 | 14% | 7% | -100% | -75% | 18 min |
| Ligue 1 Game | ✔ | 28 | 0 | 18% | 7% | -100% | -69% | 10 min |
| Adriatic ABA Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Saudi Pro League Game | ✘ | 26 | 0 | 19% | 12% | -100% | -67% | 14 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Italy Serie A2 Game | ✘ | 25 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Korea K League Game | ✘ | 25 | 1 | 24% | 12% | +273% | -58% | 8 min |
| Bundesliga Game | ✔ | 25 | 1 | 12% | 12% | +273% | -79% | 5 min |
| Spain Liga ACB Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 16 min |
| Ecuador Liga Pro Game | ✘ | 24 | 0 | 8% | 0% | -100% | -86% | 6 min |
| Bolivia Premier Division Game | ✘ | 24 | 0 | 12% | 0% | -100% | -78% | 5 min |
| Serbian SuperLiga Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Israeli Premier League Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 10 min |
| APF Division de Honor Game | ✘ | 23 | 0 | 9% | 0% | -100% | -85% | 5 min |
| Australia NBL Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 6 min |
| LNB Elite Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Sweden SBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 26 min |
| Serie A Femminile Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Rugby French 14 Match | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Vietnam V-League 1 Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Super League Greece Game | ✘ | 22 | 0 | 27% | 9% | -100% | -53% | 16 min |
| Czech NBL Game | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 16 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Slovakian Cup Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 2 min |
| Russia VTB United Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 13 min |
| Italy Serie A Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 6 min |
| Danish Superliga Game | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 13 min |
| Venezuela Liga FUTVE game | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Bundesliga Basketball Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 12 min |
| Scottish Premiership Game | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 11 min |
| Belgian Pro League Game | ✘ | 18 | 0 | 6% | 0% | -100% | -90% | 10 min |
| Austria BSL Game | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 5 min |
| Turkey BSL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Croatia HNL Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 13 min |
| Latvian Virsliga Game | ✘ | 17 | 0 | 18% | 6% | -100% | -69% | 18 min |
| Slovenian Prva Liga Game | ✘ | 17 | 0 | 12% | 6% | -100% | -80% | 7 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Chile Liga de Primera Game | ✘ | 16 | 0 | 12% | 0% | -100% | -78% | 12 min |
| Liga Portugal Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Singapore Premier League Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 16 min |
| Croatia Premijer Liga Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 19 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| Women's Pro Basketball Game | ✔ | 14 | 0 | 21% | 7% | -100% | -63% | 6 min |
| Women's ODI Cricket Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 56 min |
| Slovakia SBL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 14 min |
| Egyptian Premier League Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Spanish Liga F Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovenia 1. SKL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 15 min |
| England Super League Basketball Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CFL Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Swiss Super League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 28 min |
| FIBA Europe Cup Game | ✘ | 12 | 0 | 17% | 8% | -100% | -71% | 10 min |
| Japan B League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| UAE Pro League | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 14 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Faroe Islands Premier League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 86 min |
| Korea KBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Australian A League Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 4 min |
| Indian Super League Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 12 min |
| Qatar Stars League | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 8 min |
| Austrian Bundesliga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Hungarian NB I Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 6 min |
| French Women's Première Ligue Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| BNXT League Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Romanian Liga I Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 6 min |
| German Women's Bundesliga Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 15 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| FIBA Champions League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| United Rugby Championship Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| PREM Rugby Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Men's Iceland Basketball Premier League Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga Nacional de Basquetbol Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CONMEBOL Sudamericana Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 13 min |
| CONMEBOL Libertadores Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Brazil NBB Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Colombia LBP Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| National League Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 122 min |
| Mexican Pacific League | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 216 min |
| Philippines PBA Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Women's Bundesliga Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Powerslap Match Winner | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 436 min |
| Portugal LPB Game | ✘ | 1 | 0 | 100% | 100% | -100% | +73% | 49 min |
| GBL Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Israel Super League Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 19 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 582 | 5% | 1% | 0% | -91% |
| 5–15 min | 308 | 17% | 7% | 1% | -71% |
| 15–30 min | 198 | 31% | 17% | 2% | -47% |
| 30–60 min | 166 | 18% | 10% | 0% | -69% |
| Over 60 min | 136 | 19% | 10% | 0% | -67% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 48 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-18 17:03 | eBasketball Game | Dallas Mavericks (Zion) | ✘ | — | — | In play | — |
| 10-18 17:03 | ITF Men's Match | David Quayle | ✘ | — | — | In play | — |
| 10-18 17:02 | Ligue 1 Game | Monaco | ✔ | 88' · MON 0 - LOR 1 | — | In play | — |
| 10-18 17:01 | eBasketball Game | New Orleans Pelicans (Cade) | ✘ | — | — | In play | — |
| 10-18 17:01 | eSoccer Game | Everton (Danny) | ✘ | — | — | In play | — |
| 10-18 17:01 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-18 16:59 | Ligue 1 Game | Tie | ✔ | 86' · AUX 3 - HAC 1 | — | In play | — |
| 10-18 16:59 | Austrian Bundesliga Game | GAK | ✘ | — | — | In play | — |
| 10-18 16:59 | Austrian Bundesliga Game | Tie | ✘ | — | — | In play | — |
| 10-18 16:58 | Russia Liga Pro Match | Kariukhin Aleksandr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:54 | Serie C Game | Ostia | ✘ | — | — | In play | — |
| 10-18 16:53 | Ligue 1 Game | Le Havre | ✔ | 80' · AUX 2 - HAC 1 | — | In play | — |
| 10-18 16:53 | DEL Game | Augsburger Panther | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:52 | Romanian Liga I Game | CFR Cluj | ✘ | — | — | In play | — |
| 10-18 16:50 | Counter-Strike 2 Game | EYEBALLERS | ✘ | — | — | In play | — |
| 10-18 16:50 | Serie C Game | Crema | ✘ | — | — | In play | — |
| 10-18 16:50 | Eliteserien Game | Tie | ✘ | — | — | In play | — |
| 10-18 16:49 | Serie A Game | Atalanta | ✔ | 45'+3' · ATA 0 - MIL 2 | — | In play | — |
| 10-18 16:49 | eSoccer Game | Manchester City (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:49 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:49 | ITF Women's Match | Olivia Gram | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:49 | Italy Serie A Game | APU Udine | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:47 | Eliteserien Game | Tie | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-18 16:46 | Russia Liga Pro Match | Kirichenko Stanislav | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:44 | DEL Game | Fischtown Pinguins | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:44 | ITF Women's Match | Avery Alexander | ✘ | — | — | In play | — |
| 10-18 16:43 | Eliteserien Game | Brann | ✘ | — | — | In play | — |
| 10-18 16:42 | DEL Game | Adler Mannheim | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-18 16:41 | Croatia HNL Game | Slaven Belupo | ✘ | — | — | In play | — |
| 10-18 16:40 | Russia Liga Pro Match | Sevalnev Nikolai | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
