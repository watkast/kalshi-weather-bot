# 1¢ Study

*Updated Mon Oct 5, 1:03 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 440 finished bets | 0% | -$38.00 | -58% | -8.64¢ | -$19.00 / -$19.00 |

*Expect about **60 buys a day**, roughly **$8.99/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 440 | -$45.75 | -69% |
| ESPN-verified leagues only, sell at 2¢ | 440 | -$50.40 | -76% |
| ESPN-verified leagues only, sell at 10¢ | 440 | -$51.59 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4304 | 440 | 2 (0%) | 1.1% | -$38.00 (-58%) | Hold to the end: -$38.00 (-58%) |

*In play right now: 4. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 91 | 2.7% | 0.0% (0) | -225% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 91 | 0 | -100% | -71% | -71% | -76% |
| ESPN win probability ≥ 2% | 17 | 0 | -100% | -59% | -54% | -100% |
| ESPN win probability ≥ 5% | 7 | 0 | -100% | -75% | -63% | -100% |
| ESPN win probability ≥ 10% | 4 | 0 | -100% | -57% | -35% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 440 | 14% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 3860 | 5% | 4% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 2 | 0% | -$38.00 | -58% |
| Sell at 2¢ | 60 | 14% | -$50.40 | -76% |
| Sell at 3¢ | 36 | 8% | -$51.96 | -79% |
| Sell at 5¢ | 22 | 5% | -$51.70 | -78% |
| Sell at 10¢ | 11 | 2% | -$51.59 | -78% |
| Sell at 25¢ | 4 | 1% | -$52.76 | -80% |
| Sell at 50¢ | 3 | 1% | -$45.75 | -69% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 268 | 1 | 4% | 3% | -65% | -94% | 9 min |
| ITF Men's Match | ✘ | 258 | 0 | 9% | 4% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 248 | 0 | 11% | 5% | -100% | -80% | 4 min |
| Challenger ATP  | ✘ | 210 | 1 | 9% | 2% | -56% | -85% | 5 min |
| TT Star Series Match | ✘ | 112 | 1 | 3% | 3% | -17% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 104 | 0 | 9% | 4% | -100% | -85% | 8 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| League of Legends Game | ✘ | 91 | 0 | 7% | 2% | -100% | -89% | 12 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| CONCACAF Nations League Game | partly | 84 | 2 | 21% | 10% | +122% | -63% | 22 min |
| Darts Match | ✘ | 57 | 0 | 2% | 2% | -100% | -97% | 11 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Men's T20 Cricket Match | ✘ | 48 | 0 | 17% | 6% | -100% | -71% | 16 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Challenger WTA | ✘ | 44 | 0 | 20% | 11% | -100% | -65% | 10 min |
| Dota 2 Game | ✘ | 43 | 0 | 2% | 2% | -100% | -96% | 30 min |
| International Friendly Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 17 min |
| NHL Game | ✔ | 39 | 0 | 13% | 5% | -100% | -78% | 4 min |
| R6 Game | ✘ | 34 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| KHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 5 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Liga DIMAYOR Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 9 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ATP Tennis Match | ✘ | 24 | 0 | 12% | 4% | -100% | -78% | 3 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| KBO Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 5 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Uruguay Primera Division Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 12 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| WTA Tennis Match | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 3 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| LaLiga 2 Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 9 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Argentina Primera Division Game | ✘ | 17 | 0 | 18% | 12% | -100% | -69% | 12 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| Slovakian 2. Liga Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 111 min |
| Overwatch Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| NFL Game | ✔ | 15 | 0 | 27% | 7% | -100% | -54% | 3 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's Pro Basketball Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 9 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 9 | 0 | 22% | 11% | -100% | -61% | 5 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 9 | 1 | 44% | 44% | +937% | -23% | 32 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Bundesliga Basketball Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 13 min |
| Italy Serie A2 Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Adriatic ABA Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Italy Serie A Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| NBA Game | ✔ | 3 | 0 | 33% | 0% | -100% | -42% | 15 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 171 | 6% | 1% | 0% | -89% |
| 5–15 min | 77 | 14% | 4% | 1% | -75% |
| 15–30 min | 79 | 29% | 11% | 1% | -50% |
| 30–60 min | 57 | 12% | 5% | 0% | -79% |
| Over 60 min | 55 | 15% | 11% | 0% | -75% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 41 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-05 06:54 | TT Star Series Match | Lovo Axel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:49 | Challenger ATP  | Sergey Fomin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:45 | ATP Tennis Match | Lorenzo Sonego | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:41 | ATP Tennis Match | Chun Hsin Tseng | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:40 | Challenger ATP  | Beibit Zhukayev | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:36 | Challenger WTA | Sofia Costoulas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:33 | Challenger WTA | Elsa Jacquemot | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:23 | TT Star Series Match | Roșca Mihai | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 06:13 | ATP Tennis Match | Linang Xiao | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 05:33 | Challenger WTA | Sijia Wei | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-05 05:14 | ATP Tennis Match | Alexis Galarneau | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 05:11 | Challenger WTA | Alevtina Ibragimova | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 10-05 05:00 | Challenger ATP  | Maxim Zhukov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 04:55 | ATP Tennis Match | Andre Ilagan | ✘ | — | 77¢ | ❌ Lost | -$0.15 |
| 10-05 04:29 | Challenger WTA | Jia-Jing Lu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 04:21 | Challenger ATP  | Yusuke Takahashi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 04:18 | Men's T20 Cricket Match | Thailand | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-05 04:16 | Challenger WTA | Yidi Yang | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 04:09 | Men's T20 Cricket Match | Myanmar | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:47 | CONCACAF Nations League Game | Tie | ✔ | 90'+3' · DOM 2 - NCA 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:40 | Men's T20 Cricket Match | Indonesia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:39 | CONCACAF Nations League Game | Nicaragua | ✔ | 84' · DOM 2 - NCA 1 | 2¢ | ❌ Lost | -$0.15 |
| 10-05 03:38 | NFL Game | Detroit | ✔ | 1:29 - 4th · DET 26 - CAR 32 | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:36 | NHL Game | Vancouver | ✔ | 0:17 - 3rd · VGK 3 - VAN 2 | 3¢ | ❌ Lost | -$0.15 |
| 10-05 03:31 | Challenger WTA | Katarina Zavatska | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-05 03:23 | Challenger ATP  | Kristjan Tamm | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 10-05 03:13 | Liga DIMAYOR Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:09 | Women's College Volleyball Match | Kentucky | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 03:08 | Liga DIMAYOR Game | Llaneros | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 02:59 | Challenger ATP  | Grigoriy Lomakin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
