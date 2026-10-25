# 1¢ Study

*Updated Sun Oct 25, 11:29 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every live game in **ESPN win probability ≥ 5%**.
2. **Buy** when a team or player's YES price hits **1¢**: **14 contracts** with a 1¢ limit order (cost 15¢ including the fee). One buy per outcome.
3. **Hold** every position until the game ends. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN win probability ≥ 5%, hold to the end | 37 finished bets | 3% | $8.45 | +152% | +22.84¢ | $11.30 / -$2.85 |

*Expect about **2 buys a day**, roughly **$0.25/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN win probability ≥ 2%, hold to the end | 79 | $2.15 | +18% |
| ESPN win probability ≥ 5%, sell at 50¢ | 37 | $1.20 | +22% |
| ESPN win probability ≥ 5%, sell at 25¢ | 37 | $1.07 | +19% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 31543 | 1974 | 8 (0%) | 1.1% | -$184.10 (-62%) | Hold to the end: -$184.10 (-62%) |

*In play right now: 45. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 347 | 3.2% | 0.3% (1) | -73% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 347 | 1 | -73% | -72% | -72% | -70% |
| ESPN win probability ≥ 2% | 79 | 1 | +18% | -65% | -70% | -73% |
| ESPN win probability ≥ 5% | 37 | 1 | +152% | -77% | -79% | -77% |
| ESPN win probability ≥ 10% | 23 | 1 | +306% | -70% | -66% | -62% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 1974 | 13% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 29524 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 8 | 0% | -$184.10 | -62% |
| Sell at 2¢ | 266 | 13% | -$226.94 | -77% |
| Sell at 3¢ | 185 | 9% | -$223.95 | -76% |
| Sell at 5¢ | 128 | 6% | -$212.90 | -72% |
| Sell at 10¢ | 58 | 3% | -$220.12 | -74% |
| Sell at 25¢ | 18 | 1% | -$236.52 | -80% |
| Sell at 50¢ | 11 | 1% | -$221.85 | -75% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| eSoccer Game | ✘ | 13539 | 5 | 1% | 0% | -97% | -99% | 2 min |
| Russia Liga Pro Match | ✘ | 1449 | 0 | 0% | 0% | -100% | -99% | 4 min |
| eBasketball Game | ✘ | 1346 | 2 | 1% | 1% | -86% | -91% | 2 min |
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 1111 | 2 | 13% | 5% | -83% | -77% | 4 min |
| Counter-Strike 2 Game | ✘ | 1047 | 2 | 5% | 3% | -82% | -91% | 12 min |
| ITF Men's Match | ✘ | 1023 | 1 | 13% | 6% | -91% | -78% | 5 min |
| Challenger ATP  | ✘ | 671 | 2 | 11% | 4% | -72% | -82% | 5 min |
| College Football Game | partly | 333 | 2 | 11% | 6% | -44% | -80% | 23 min |
| TT Star Series Match | ✘ | 320 | 1 | 2% | 2% | -71% | -97% | 5 min |
| Darts Match | ✘ | 260 | 0 | 0% | 0% | -100% | -99% | 8 min |
| Men's T20 Cricket Match | ✘ | 243 | 1 | 14% | 5% | -62% | -75% | 23 min |
| Women's College Volleyball Match | ✘ | 234 | 2 | 6% | 3% | -20% | -90% | 72 min |
| eFootball Game | ✘ | 231 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Serie C Game | ✘ | 222 | 2 | 5% | 2% | -16% | -92% | 6 min |
| Dota 2 Game | ✘ | 211 | 0 | 1% | 1% | -100% | -98% | 30 min |
| NHL Game | ✔ | 178 | 0 | 10% | 4% | -100% | -82% | 4 min |
| Challenger WTA | ✘ | 164 | 0 | 12% | 4% | -100% | -80% | 8 min |
| League of Legends Game | ✘ | 144 | 0 | 7% | 2% | -100% | -88% | 11 min |
| WTA Tennis Match | ✘ | 141 | 0 | 11% | 2% | -100% | -82% | 5 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| Major League Soccer Game | partly | 127 | 1 | 13% | 6% | -27% | -77% | 7 min |
| AHL Game | ✘ | 126 | 0 | 2% | 2% | -100% | -96% | 5 min |
| Ettan Game | ✘ | 117 | 0 | 4% | 1% | -100% | -93% | 7 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| KHL Game | ✘ | 102 | 0 | 6% | 3% | -100% | -90% | 6 min |
| Brasileiro Serie B Game | ✘ | 101 | 1 | 8% | 4% | -8% | -86% | 8 min |
| Argentina Primera Division Game | ✘ | 100 | 1 | 15% | 8% | -7% | -74% | 7 min |
| Japan J2 League Game | ✘ | 100 | 0 | 12% | 5% | -100% | -79% | 6 min |
| NBA Game | ✔ | 100 | 0 | 18% | 6% | -100% | -69% | 7 min |
| ATP Tennis Match | ✘ | 97 | 0 | 14% | 6% | -100% | -75% | 4 min |
| USL Championship Game | partly | 96 | 0 | 11% | 4% | -100% | -80% | 4 min |
| Overwatch Game | ✘ | 91 | 0 | 2% | 0% | -100% | -96% | 5 min |
| Argentine Nacional B Game | ✘ | 88 | 0 | 10% | 7% | -100% | -82% | 9 min |
| Liga DIMAYOR Game | ✘ | 87 | 1 | 10% | 3% | +7% | -82% | 6 min |
| LaLiga 2 Game | partly | 85 | 1 | 19% | 9% | +10% | -67% | 9 min |
| Brasileiro Serie A Game | partly | 81 | 1 | 15% | 9% | +15% | -74% | 7 min |
| Japan J League Game | ✘ | 81 | 1 | 19% | 7% | +15% | -68% | 12 min |
| English National League Game | ✘ | 79 | 0 | 9% | 6% | -100% | -85% | 10 min |
| EFL League One Game | ✔ | 79 | 0 | 11% | 4% | -100% | -80% | 10 min |
| German 3. Liga Game | ✘ | 78 | 0 | 12% | 5% | -100% | -80% | 7 min |
| EFL Championship Game | ✔ | 78 | 0 | 9% | 5% | -100% | -84% | 9 min |
| College Hockey Game | ✘ | 75 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 74 | 0 | 8% | 3% | -100% | -86% | 9 min |
| Liiga Game | ✘ | 73 | 0 | 0% | 0% | -100% | -100% | 5 min |
| UEFA Champions League Game | partly | 73 | 1 | 10% | 3% | +28% | -83% | 11 min |
| Liga Leumit Game | ✘ | 72 | 0 | 3% | 3% | -100% | -95% | 39 min |
| Eerste Divisie Game | ✘ | 70 | 0 | 10% | 7% | -100% | -83% | 9 min |
| UEFA Conference League Game | partly | 70 | 0 | 16% | 10% | -100% | -73% | 10 min |
| National League Game | ✘ | 69 | 1 | 1% | 1% | +35% | -97% | 5 min |
| UEFA Europa League Game | partly | 69 | 0 | 16% | 7% | -100% | -72% | 13 min |
| TFF 1. Lig Game | ✘ | 68 | 0 | 16% | 10% | -100% | -72% | 10 min |
| Slovakian 2. Liga Game | ✘ | 66 | 0 | 5% | 5% | -100% | -92% | 85 min |
| Liga MX Game | ✔ | 65 | 0 | 14% | 8% | -100% | -76% | 2 min |
| Chinese Basketball Association Game  | ✘ | 65 | 0 | 6% | 2% | -100% | -89% | 11 min |
| Valorant game winner | ✘ | 64 | 0 | 5% | 3% | -100% | -92% | 14 min |
| FIFA Women's Game | ✘ | 63 | 1 | 14% | 8% | +48% | -75% | 47 min |
| Tweede Divisie Game | ✘ | 62 | 0 | 2% | 0% | -100% | -97% | 5 min |
| Liga Expansion Game | ✘ | 61 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Uruguay Primera Division Game | ✘ | 60 | 0 | 7% | 3% | -100% | -88% | 10 min |
| EuroCup Basketball Game | ✘ | 60 | 0 | 5% | 3% | -100% | -91% | 10 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Euroleague Game | ✘ | 59 | 0 | 25% | 8% | -100% | -56% | 14 min |
| ELH Game | ✘ | 58 | 0 | 2% | 2% | -100% | -97% | 5 min |
| Indonesia Super League Game | ✘ | 58 | 0 | 12% | 5% | -100% | -79% | 9 min |
| China League 1 Game | ✘ | 57 | 0 | 12% | 7% | -100% | -79% | 10 min |
| SHL Game | ✘ | 56 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Mobile Legends Bang Bang Game | ✘ | 56 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Saudi Pro League Game | ✘ | 55 | 1 | 18% | 11% | +70% | -68% | 14 min |
| LNBP Basketball Game | ✘ | 54 | 0 | 6% | 0% | -100% | -90% | 12 min |
| Bundesliga 2 Game | ✔ | 54 | 0 | 11% | 6% | -100% | -81% | 8 min |
| Serie B Game | ✘ | 54 | 0 | 15% | 7% | -100% | -74% | 9 min |
| La Liga Game | ✔ | 54 | 0 | 24% | 17% | -100% | -58% | 8 min |
| Serie A Game | ✔ | 54 | 0 | 7% | 6% | -100% | -87% | 12 min |
| KBO Game | ✘ | 53 | 0 | 11% | 6% | -100% | -80% | 5 min |
| DEL Game | ✘ | 53 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Polish Ekstraklasa Game | ✘ | 53 | 0 | 13% | 8% | -100% | -77% | 9 min |
| English Premier League Game | ✔ | 52 | 0 | 8% | 4% | -100% | -87% | 10 min |
| Taca de Portugal Game | ✘ | 52 | 0 | 15% | 4% | -100% | -73% | 14 min |
| Ligue 2 Game | ✘ | 50 | 0 | 12% | 8% | -100% | -79% | 7 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| Peru Liga 1 Game | ✘ | 48 | 0 | 15% | 8% | -100% | -75% | 11 min |
| Korea K-League 2 Game | ✘ | 48 | 0 | 12% | 6% | -100% | -78% | 9 min |
| Thai League 1 Game | ✘ | 48 | 0 | 19% | 6% | -100% | -68% | 10 min |
| LNB Elite 2 Game | ✘ | 47 | 0 | 2% | 0% | -100% | -96% | 7 min |
| Chinese Super League Game | ✘ | 47 | 1 | 11% | 6% | +99% | -82% | 17 min |
| Czech National Football League Game | ✘ | 47 | 0 | 13% | 6% | -100% | -78% | 8 min |
| Allsvenskan Game | ✘ | 47 | 1 | 15% | 13% | +99% | -74% | 11 min |
| Eredivisie Game | ✔ | 47 | 0 | 11% | 9% | -100% | -82% | 4 min |
| NWSL Game | ✔ | 46 | 0 | 7% | 0% | -100% | -89% | 7 min |
| NFL Game | ✔ | 46 | 1 | 22% | 9% | +103% | -62% | 4 min |
| Women's T20 Match | ✘ | 45 | 0 | 18% | 9% | -100% | -69% | 26 min |
| Turkish Super Lig Game | ✘ | 44 | 0 | 14% | 0% | -100% | -76% | 14 min |
| Men's ODI Cricket Match | ✘ | 43 | 3 | 19% | 9% | +551% | -68% | 36 min |
| Czech First League Game | ✘ | 43 | 0 | 12% | 0% | -100% | -80% | 8 min |
| Bundesliga Game | ✔ | 43 | 1 | 12% | 7% | +117% | -80% | 5 min |
| Ligue 1 Game | ✔ | 42 | 0 | 17% | 7% | -100% | -71% | 8 min |
| Japan B League Game | ✘ | 42 | 0 | 10% | 0% | -100% | -83% | 13 min |
| Finland Korisliiga Game | ✘ | 40 | 1 | 8% | 5% | +133% | -87% | 9 min |
| England Women's Super League Game | ✘ | 40 | 0 | 20% | 8% | -100% | -65% | 28 min |
| Italy Serie A2 Game | ✘ | 40 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Ecuador Liga Pro Game | ✘ | 40 | 0 | 10% | 2% | -100% | -83% | 7 min |
| Serbian SuperLiga Game | ✘ | 40 | 0 | 2% | 0% | -100% | -96% | 12 min |
| APF Division de Honor Game | ✘ | 39 | 0 | 18% | 5% | -100% | -69% | 6 min |
| Eliteserien Game | ✘ | 38 | 0 | 11% | 5% | -100% | -82% | 16 min |
| Israeli Premier League Game | ✘ | 38 | 0 | 3% | 0% | -100% | -95% | 8 min |
| Adriatic ABA Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 10 min |
| Vietnam V-League 1 Game | ✘ | 37 | 1 | 8% | 5% | +152% | -86% | 10 min |
| Korea K League Game | ✘ | 37 | 1 | 19% | 11% | +152% | -67% | 8 min |
| Japan NPB Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Serie A Femminile Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Bolivia Premier Division Game | ✘ | 34 | 0 | 15% | 3% | -100% | -75% | 6 min |
| Spain Liga ACB Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 14 min |
| Super League Greece Game | ✘ | 33 | 0 | 18% | 6% | -100% | -68% | 13 min |
| Danish Superliga Game | ✘ | 32 | 0 | 9% | 6% | -100% | -84% | 12 min |
| Rugby French 14 Match | ✘ | 31 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Egyptian Premier League Game | ✘ | 31 | 0 | 6% | 6% | -100% | -89% | 11 min |
| Australia NBL Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 8 min |
| LNB Elite Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Belgian Pro League Game | ✘ | 30 | 0 | 10% | 0% | -100% | -83% | 12 min |
| Faroe Islands Premier League Game | ✘ | 30 | 0 | 3% | 0% | -100% | -94% | 84 min |
| Venezuela Liga FUTVE game | ✘ | 30 | 0 | 17% | 13% | -100% | -71% | 6 min |
| Spanish Liga F Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 7 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Scottish Premiership Game | ✘ | 29 | 0 | 10% | 0% | -100% | -82% | 15 min |
| Sweden SBL Game | ✘ | 28 | 0 | 4% | 4% | -100% | -94% | 15 min |
| Italy Serie A Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Latvian Virsliga Game | ✘ | 27 | 0 | 11% | 4% | -100% | -81% | 17 min |
| Czech NBL Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 17 min |
| Turkey BSL Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga Portugal Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 10 min |
| AFC Champions League Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 10 min |
| Romanian Liga I Game | ✘ | 26 | 0 | 12% | 4% | -100% | -80% | 12 min |
| Russia VTB United Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 14 min |
| Canadian Premier League | ✘ | 25 | 1 | 20% | 20% | +273% | -65% | 29 min |
| Bundesliga Basketball Game | ✘ | 25 | 0 | 12% | 4% | -100% | -79% | 12 min |
| Slovakian Cup Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 19 min |
| Qatar Stars League | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 7 min |
| German Women's Bundesliga Game | ✘ | 24 | 0 | 8% | 4% | -100% | -86% | 23 min |
| Austria BSL Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 5 min |
| Croatia HNL Game | ✘ | 23 | 0 | 9% | 4% | -100% | -85% | 11 min |
| Chile Liga de Primera Game | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 9 min |
| Singapore Premier League Game | ✘ | 22 | 0 | 14% | 0% | -100% | -76% | 17 min |
| FIBA Europe Cup Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 9 min |
| Australian A League Game | ✘ | 22 | 0 | 9% | 0% | -100% | -84% | 6 min |
| Austrian Bundesliga Game | ✘ | 22 | 0 | 9% | 5% | -100% | -84% | 11 min |
| Hungarian NB I Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Professional Baseball Game | partly | 21 | 0 | 14% | 10% | -100% | -75% | 2 min |
| Croatia Premijer Liga Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Finnish Ykkosliiga Game | ✘ | 21 | 1 | 10% | 5% | +344% | -83% | 6 min |
| Korea KBL Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Swiss Super League Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 21 min |
| Indian Super League Game | ✘ | 20 | 0 | 10% | 10% | -100% | -83% | 8 min |
| Slovakia SBL Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| LKL Lithuania Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Slovenian Prva Liga Game | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 6 min |
| Women's ODI Cricket Match | ✘ | 18 | 0 | 22% | 11% | -100% | -61% | 56 min |
| England Super League Basketball Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Brazil NBB Basketball Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Slovenia 1. SKL Game | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 15 min |
| Brasileiro Serie C Game | ✘ | 16 | 0 | 19% | 12% | -100% | -68% | 5 min |
| Women's Pro Basketball Game | ✔ | 16 | 0 | 19% | 6% | -100% | -68% | 6 min |
| CFL Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 10 min |
| Eredivisie Vrouwen Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 10 min |
| BNXT League Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Copa Del Rey Game | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 34 min |
| FIBA Champions League Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 10 min |
| French Women's Première Ligue Game | ✘ | 15 | 0 | 13% | 7% | -100% | -77% | 6 min |
| UAE Pro League | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| Liga Nacional de Basquetbol Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's Iceland Basketball Premier League Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 10 min |
| Malaysia Super League Game | ✘ | 11 | 0 | 18% | 0% | -100% | -68% | 9 min |
| Colombia LBP Basketball Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Polish Hockey Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 9 min |
| United Rugby Championship Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| CONMEBOL Sudamericana Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| South African Premiership Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 2 min |
| EuroLeague (W) Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 7 min |
| PREM Rugby Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Powerslap Match Winner | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 12 min |
| CONMEBOL Libertadores Game | ✘ | 7 | 0 | 29% | 0% | -100% | -50% | 12 min |
| Philippines PBA Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Israel Super League Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 16 min |
| Ukraine SuperLeague Game | ✘ | 6 | 0 | 17% | 0% | -100% | -71% | 9 min |
| Ligue Magnus Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Champions League Hockey | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| GBL Basketball Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's Bundesliga Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 1 min |
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
| Under 5 min | 809 | 5% | 1% | 0% | -92% |
| 5–15 min | 460 | 18% | 8% | 1% | -69% |
| 15–30 min | 302 | 26% | 14% | 1% | -55% |
| 30–60 min | 216 | 19% | 11% | 0% | -68% |
| Over 60 min | 167 | 17% | 9% | 0% | -71% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 43 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-25 17:29 | TFF 1. Lig Game | Keciorengucu | ✘ | — | — | In play | — |
| 10-25 17:28 | Challenger ATP  | Arthur Bouquier | ✘ | — | — | In play | — |
| 10-25 17:27 | LNB Elite Game | Sluc Nancy Basket | ✘ | — | — | In play | — |
| 10-25 17:27 | Counter-Strike 2 Game | Infinite | ✘ | — | — | In play | — |
| 10-25 17:25 | Russia Liga Pro Match | Kovalev Igor | ✘ | — | — | In play | — |
| 10-25 17:25 | Challenger ATP  | Govind Nanda | ✘ | — | — | In play | — |
| 10-25 17:24 | Swiss Super League Game | Basel | ✘ | — | — | In play | — |
| 10-25 17:24 | Swiss Super League Game | Grasshopper | ✘ | — | — | In play | — |
| 10-25 17:23 | Ligue 1 Game | Tie | ✔ | 51' · HAC 0 - OLM 3 | — | In play | — |
| 10-25 17:22 | Super League Greece Game | Volos | ✘ | — | — | In play | — |
| 10-25 17:22 | eSoccer Game | Hoffenheim (Mantis) | ✘ | — | — | In play | — |
| 10-25 17:22 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-25 17:22 | Swiss Super League Game | Tie | ✘ | — | — | In play | — |
| 10-25 17:22 | Uruguay Primera Division Game | Cerro | ✘ | — | — | In play | — |
| 10-25 17:21 | eSoccer Game | Chelsea (Luis) | ✘ | — | — | In play | — |
| 10-25 17:21 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-25 17:21 | Italy Serie A Game | APU Udine | ✘ | — | — | In play | — |
| 10-25 17:21 | Hungarian NB I Game | MTK Budapest | ✘ | — | — | In play | — |
| 10-25 17:21 | German 3. Liga Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-25 17:20 | Chile Liga de Primera Game | Coquimbo | ✘ | — | — | In play | — |
| 10-25 17:20 | eSoccer Game | Olympique de Marseille (Annie) | ✘ | — | — | In play | — |
| 10-25 17:20 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-25 17:20 | eFootball Game | Dallas (Speed) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-25 17:19 | Counter-Strike 2 Game | DENDELE CS | ✘ | — | — | In play | — |
| 10-25 17:19 | eSoccer Game | Crystal Palace (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-25 17:19 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-25 17:19 | ELH Game | HC Skoda Plzen | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-25 17:19 | Latvian Virsliga Game | Tie | ✘ | — | — | In play | — |
| 10-25 17:19 | Turkish Super Lig Game | Corum | ✘ | — | — | In play | — |
| 10-25 17:18 | eSoccer Game | RC Lens (Florie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
