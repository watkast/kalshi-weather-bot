# 1¢ Study

*Updated Mon Oct 26, 9:59 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 38 finished bets | 3% | $8.30 | +146% | +21.84¢ | $11.15 / -$2.85 |

*Expect about **2 buys a day**, roughly **$0.25/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 81 | $1.85 | +15% |
| ESPN win probability ≥ 5%, sell at 50¢ | 38 | $1.05 | +18% |
| ESPN win probability ≥ 5%, sell at 25¢ | 38 | $0.92 | +16% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 33152 | 2037 | 8 (0%) | 1.1% | -$193.55 (-63%) | Hold to the end: -$193.55 (-63%) |

*In play right now: 20. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 365 | 3.1% | 0.3% (1) | -74% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 365 | 1 | -74% | -73% | -73% | -70% |
| ESPN win probability ≥ 2% | 81 | 1 | +15% | -66% | -71% | -73% |
| ESPN win probability ≥ 5% | 38 | 1 | +146% | -77% | -79% | -77% |
| ESPN win probability ≥ 10% | 24 | 1 | +289% | -71% | -68% | -64% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 2037 | 14% | 9% | 7% | 3% | 1% | 1% |
| Unverified | 31095 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 8 | 0% | -$193.55 | -63% |
| Sell at 2¢ | 275 | 14% | -$234.05 | -77% |
| Sell at 3¢ | 193 | 9% | -$230.28 | -75% |
| Sell at 5¢ | 135 | 7% | -$217.80 | -71% |
| Sell at 10¢ | 61 | 3% | -$225.64 | -74% |
| Sell at 25¢ | 19 | 1% | -$242.66 | -79% |
| Sell at 50¢ | 12 | 1% | -$224.55 | -73% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 14415 | 5 | 1% | 0% | -97% | -99% | 2 min |
| Russia Liga Pro Match | ✘ | 1584 | 0 | 0% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1427 | 2 | 1% | 0% | -87% | -91% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 1151 | 3 | 13% | 5% | -76% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 1080 | 2 | 5% | 3% | -83% | -91% | 12 min |
| ITF Men's Match | ✘ | 1042 | 1 | 13% | 6% | -91% | -78% | 5 min |
| Challenger ATP  | ✘ | 697 | 2 | 11% | 4% | -73% | -82% | 5 min |
| College Football Game | partly | 333 | 2 | 11% | 6% | -44% | -80% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Darts Match | ✘ | 278 | 0 | 0% | 0% | -100% | -99% | 8 min |
| eFootball Game | ✘ | 272 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Women's College Volleyball Match | ✘ | 256 | 2 | 5% | 3% | -27% | -91% | 72 min |
| Men's T20 Cricket Match | ✘ | 249 | 1 | 14% | 6% | -63% | -75% | 22 min |
| Serie C Game | ✘ | 230 | 2 | 4% | 2% | -19% | -92% | 6 min |
| Dota 2 Game | ✘ | 217 | 0 | 1% | 1% | -100% | -98% | 30 min |
| NHL Game | ✔ | 183 | 0 | 10% | 5% | -100% | -82% | 5 min |
| Challenger WTA | ✘ | 169 | 0 | 12% | 4% | -100% | -79% | 8 min |
| WTA Tennis Match | ✘ | 148 | 0 | 11% | 2% | -100% | -81% | 5 min |
| League of Legends Game | ✘ | 147 | 0 | 7% | 2% | -100% | -88% | 11 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Major League Soccer Game | partly | 129 | 1 | 13% | 6% | -28% | -77% | 6 min |
| AHL Game | ✘ | 129 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Ettan Game | ✘ | 117 | 0 | 4% | 1% | -100% | -93% | 7 min |
| Argentina Primera Division Game | ✘ | 110 | 1 | 15% | 8% | -15% | -75% | 7 min |
| Argentine Nacional B Game | ✘ | 108 | 0 | 9% | 6% | -100% | -84% | 9 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| NBA Game | ✔ | 107 | 0 | 17% | 6% | -100% | -71% | 7 min |
| KHL Game | ✘ | 102 | 0 | 6% | 3% | -100% | -90% | 6 min |
| Brasileiro Serie B Game | ✘ | 101 | 1 | 8% | 4% | -8% | -86% | 8 min |
| Japan J2 League Game | ✘ | 100 | 0 | 12% | 5% | -100% | -79% | 6 min |
| ATP Tennis Match | ✘ | 98 | 0 | 15% | 6% | -100% | -73% | 4 min |
| USL Championship Game | partly | 96 | 0 | 11% | 4% | -100% | -80% | 4 min |
| Liga DIMAYOR Game | ✘ | 95 | 1 | 9% | 3% | -2% | -84% | 6 min |
| Overwatch Game | ✘ | 95 | 0 | 2% | 0% | -100% | -96% | 6 min |
| LaLiga 2 Game | partly | 87 | 1 | 18% | 9% | +7% | -68% | 9 min |
| Brasileiro Serie A Game | partly | 81 | 1 | 15% | 9% | +15% | -74% | 7 min |
| Japan J League Game | ✘ | 81 | 1 | 19% | 7% | +15% | -68% | 12 min |
| German 3. Liga Game | ✘ | 80 | 0 | 11% | 5% | -100% | -80% | 8 min |
| English National League Game | ✘ | 79 | 0 | 9% | 6% | -100% | -85% | 10 min |
| EFL League One Game | ✔ | 79 | 0 | 11% | 4% | -100% | -80% | 10 min |
| EFL Championship Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 9 min |
| R6 Game | ✘ | 75 | 1 | 9% | 4% | +24% | -84% | 9 min |
| College Hockey Game | ✘ | 75 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liga MX Game | ✔ | 73 | 0 | 15% | 10% | -100% | -74% | 5 min |
| Liiga Game | ✘ | 73 | 0 | 0% | 0% | -100% | -100% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| Eerste Divisie Game | ✘ | 70 | 0 | 10% | 7% | -100% | -83% | 9 min |
| TFF 1. Lig Game | ✘ | 70 | 0 | 17% | 10% | -100% | -70% | 10 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| National League Game | ✘ | 69 | 1 | 1% | 1% | +35% | -97% | 5 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| Chinese Basketball Association Game  | ✘ | 67 | 0 | 6% | 1% | -100% | -90% | 11 min |
| Uruguay Primera Division Game | ✘ | 66 | 0 | 8% | 3% | -100% | -87% | 10 min |
| Valorant game winner | ✘ | 66 | 0 | 5% | 3% | -100% | -92% | 14 min |
| Slovakian 2. Liga Game | ✘ | 66 | 0 | 5% | 5% | -100% | -92% | 85 min |
| Indonesia Super League Game | ✘ | 64 | 0 | 14% | 8% | -100% | -76% | 9 min |
| Liga Expansion Game | ✘ | 63 | 0 | 5% | 3% | -100% | -92% | 11 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| ELH Game | ✘ | 62 | 0 | 2% | 2% | -100% | -97% | 5 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| La Liga Game | ✔ | 58 | 0 | 22% | 16% | -100% | -61% | 7 min |
| Serie A Game | ✔ | 58 | 0 | 7% | 5% | -100% | -88% | 12 min |
| China League 1 Game | ✘ | 57 | 0 | 12% | 7% | -100% | -79% | 10 min |
| DEL Game | ✘ | 57 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NFL Game | ✔ | 57 | 1 | 19% | 9% | +64% | -67% | 4 min |
| SHL Game | ✘ | 56 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Peru Liga 1 Game | ✘ | 56 | 0 | 12% | 7% | -100% | -78% | 12 min |
| Mobile Legends Bang Bang Game | ✘ | 56 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Serie B Game | ✘ | 56 | 0 | 14% | 7% | -100% | -75% | 9 min |
| Saudi Pro League Game | ✘ | 55 | 1 | 18% | 11% | +70% | -68% | 14 min |
| Polish Ekstraklasa Game | ✘ | 55 | 0 | 13% | 7% | -100% | -78% | 8 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| Bundesliga 2 Game | ✔ | 54 | 0 | 11% | 6% | -100% | -81% | 8 min |
| English Premier League Game | ✔ | 54 | 0 | 7% | 4% | -100% | -87% | 10 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| NWSL Game | ✔ | 52 | 0 | 10% | 2% | -100% | -83% | 7 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Eredivisie Game | ✔ | 51 | 0 | 10% | 8% | -100% | -83% | 4 min |
| Japan B League Game | ✘ | 51 | 0 | 8% | 0% | -100% | -86% | 13 min |
| Ligue 2 Game | ✘ | 50 | 0 | 12% | 8% | -100% | -79% | 7 min |
| Ligue 1 Game | ✔ | 50 | 0 | 18% | 8% | -100% | -69% | 8 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Women's T20 Match | ✘ | 49 | 0 | 16% | 8% | -100% | -72% | 25 min |
| Italy Serie A2 Game | ✘ | 49 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Korea K-League 2 Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Thai League 1 Game | ✘ | 48 | 0 | 19% | 6% | -100% | -68% | 10 min |
| Eliteserien Game | ✘ | 48 | 0 | 10% | 4% | -100% | -82% | 12 min |
| LNB Elite 2 Game | ✘ | 47 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Czech National Football League Game | ✘ | 47 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Allsvenskan Game | ✘ | 47 | 1 | 15% | 13% | +99% | -74% | 11 min |
| Turkish Super Lig Game | ✘ | 46 | 0 | 13% | 0% | -100% | -77% | 14 min |
| Ecuador Liga Pro Game | ✘ | 46 | 0 | 9% | 2% | -100% | -85% | 8 min |
| Czech First League Game | ✘ | 45 | 0 | 11% | 0% | -100% | -81% | 8 min |
| Bundesliga Game | ✔ | 45 | 1 | 13% | 9% | +107% | -77% | 6 min |
| Men's ODI Cricket Match | ✘ | 43 | 3 | 19% | 9% | +551% | -68% | 36 min |
| England Women's Super League Game | ✘ | 42 | 0 | 21% | 10% | -100% | -63% | 26 min |
| APF Division de Honor Game | ✘ | 41 | 0 | 20% | 7% | -100% | -66% | 6 min |
| Finland Korisliiga Game | ✘ | 40 | 1 | 8% | 5% | +133% | -87% | 9 min |
| Bolivia Premier Division Game | ✘ | 40 | 0 | 12% | 2% | -100% | -78% | 7 min |
| Serbian SuperLiga Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 12 min |
| Israeli Premier League Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 8 min |
| Super League Greece Game | ✘ | 39 | 0 | 18% | 5% | -100% | -69% | 14 min |
| Adriatic ABA Game | ✘ | 38 | 0 | 5% | 3% | -100% | -91% | 11 min |
| Vietnam V-League 1 Game | ✘ | 37 | 1 | 8% | 5% | +152% | -86% | 10 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Serie A Femminile Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Spain Liga ACB Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 14 min |
| Japan NPB Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Danish Superliga Game | ✘ | 34 | 0 | 12% | 6% | -100% | -80% | 12 min |
| Liga Portugal Game | ✘ | 34 | 0 | 6% | 3% | -100% | -90% | 10 min |
| Belgian Pro League Game | ✘ | 34 | 0 | 9% | 0% | -100% | -85% | 18 min |
| Venezuela Liga FUTVE game | ✘ | 34 | 0 | 21% | 15% | -100% | -64% | 6 min |
| Rugby French 14 Match | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 6 min |
| LNB Elite Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A Game | ✘ | 32 | 0 | 3% | 3% | -100% | -95% | 6 min |
| Spanish Liga F Game | ✘ | 32 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Canadian Premier League | ✘ | 31 | 1 | 16% | 16% | +201% | -72% | 23 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| Australia NBL Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 8 min |
| Chile Liga de Primera Game | ✘ | 30 | 0 | 10% | 0% | -100% | -83% | 6 min |
| Faroe Islands Premier League Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 84 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Latvian Virsliga Game | ✘ | 29 | 0 | 14% | 3% | -100% | -76% | 17 min |
| Scottish Premiership Game | ✘ | 29 | 0 | 10% | 0% | -100% | -82% | 15 min |
| Sweden SBL Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 15 min |
| Czech NBL Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 17 min |
| AFC Champions League Game | ✘ | 28 | 0 | 7% | 0% | -100% | -88% | 9 min |
| Romanian Liga I Game | ✘ | 28 | 0 | 11% | 4% | -100% | -81% | 10 min |
| Turkey BSL Game | ✘ | 27 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bundesliga Basketball Game | ✘ | 26 | 0 | 12% | 4% | -100% | -80% | 12 min |
| German Women's Bundesliga Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 18 min |
| Russia VTB United Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Croatia HNL Game | ✘ | 25 | 0 | 8% | 4% | -100% | -86% | 10 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Singapore Premier League Game | ✘ | 24 | 0 | 12% | 0% | -100% | -78% | 18 min |
| Swiss Super League Game | ✘ | 24 | 0 | 4% | 0% | -100% | -93% | 18 min |
| Qatar Stars League | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 7 min |
| Austrian Bundesliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 11 min |
| Hungarian NB I Game | ✘ | 24 | 0 | 8% | 8% | -100% | -86% | 6 min |
| Austria BSL Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 5 min |
| Croatia Premijer Liga Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Korea KBL Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 4 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Australian A League Game | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 6 min |
| Professional Baseball Game | partly | 21 | 0 | 14% | 10% | -100% | -75% | 2 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Slovakia SBL Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 16 min |
| England Super League Basketball Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LKL Lithuania Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 8 min |
| Indian Super League Game | ✘ | 20 | 0 | 10% | 10% | -100% | -83% | 8 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Women's ODI Cricket Match | ✘ | 18 | 0 | 22% | 11% | -100% | -61% | 56 min |
| Brazil NBB Basketball Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Slovenia 1. SKL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 15 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Women's Pro Basketball Game | ✔ | 16 | 0 | 19% | 6% | -100% | -68% | 6 min |
| CFL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| BNXT League Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| French Women's Première Ligue Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 6 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Liga Nacional de Basquetbol Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Polish Hockey Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 7 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Ligue Magnus Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| United Rugby Championship Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EuroLeague (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Philippines PBA Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Israel Super League Game | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 13 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| GBL Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
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
| Under 5 min | 832 | 5% | 1% | 0% | -92% |
| 5–15 min | 474 | 17% | 8% | 1% | -70% |
| 15–30 min | 311 | 26% | 14% | 1% | -55% |
| 30–60 min | 229 | 19% | 12% | 0% | -67% |
| Over 60 min | 171 | 18% | 9% | 0% | -70% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 42 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-26 15:59 | Challenger WTA | Julia Konishi Camargo Silva | ✘ | — | — | In play | — |
| 10-26 15:58 | eSoccer Game | Paris Saint-Germain (Frost) | ✘ | — | — | In play | — |
| 10-26 15:57 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-26 15:56 | eSoccer Game | Manchester City (Maddy) | ✘ | — | — | In play | — |
| 10-26 15:56 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-26 15:56 | eSoccer Game | Olympique Lyon (Kylian) | ✘ | — | — | In play | — |
| 10-26 15:55 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-26 15:54 | eSoccer Game | Manchester Utd (Adri) | ✘ | — | — | In play | — |
| 10-26 15:54 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-26 15:53 | Indian Super League Game | Tie | ✘ | — | — | In play | — |
| 10-26 15:51 | eFootball Game | Detroit (Cooper) | ✘ | — | — | In play | — |
| 10-26 15:50 | Russia Liga Pro Match | Vorozheikin Aleksandr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:46 | eSoccer Game | FC Bayern (Mantis) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:46 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:44 | Indian Super League Game | Chennaiyin | ✘ | — | — | In play | — |
| 10-26 15:44 | eSoccer Game | Paris Saint-Germain (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:44 | Men's T20 Cricket Match | Emirates Reds | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:43 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:43 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:42 | eSoccer Game | Manchester City (Maddy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:41 | ITF Women's Match | Filippa Eckersten | ✘ | — | — | In play | — |
| 10-26 15:41 | eSoccer Game | Olympique de Marseille (Kevin) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:41 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:41 | AFC Champions League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:40 | eSoccer Game | Chelsea (Kate) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:40 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-26 15:40 | ITF Men's Match | Conor Brady | ✘ | — | 4¢ | ❌ Lost | -$0.15 |
| 10-26 15:38 | ITF Men's Match | Mateja Stanisavljevic | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-26 15:38 | Dota 2 Game | No Hoodwink | ✘ | — | — | In play | — |
| 10-26 15:35 | Russia Liga Pro Match | Drykin Sergei | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
