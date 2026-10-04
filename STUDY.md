# 1¢ Study

*Updated Sun Oct 4, 3:13 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 411 finished bets | 0% | -$47.65 | -77% | -11.59¢ | -$16.75 / -$30.90 |

*Expect about **59 buys a day**, roughly **$8.90/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 411 | -$47.87 | -78% |
| ESPN-verified leagues only, sell at 50¢ | 411 | -$48.15 | -78% |
| ESPN-verified leagues only, sell at 5¢ | 411 | -$48.65 | -79% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4216 | 411 | 1 (0%) | 1.1% | -$47.65 (-77%) | Hold to the end: -$47.65 (-77%) |

*In play right now: 8. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 85 | 2.8% | 0.0% (0) | -244% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 85 | 0 | -100% | -71% | -72% | -80% |
| ESPN win probability ≥ 2% | 17 | 0 | -100% | -59% | -54% | -100% |
| ESPN win probability ≥ 5% | 7 | 0 | -100% | -75% | -63% | -100% |
| ESPN win probability ≥ 10% | 4 | 0 | -100% | -57% | -35% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 411 | 13% | 8% | 5% | 2% | 1% | 0% |
| Unverified | 3797 | 5% | 3% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$47.65 | -77% |
| Sell at 2¢ | 53 | 13% | -$47.87 | -78% |
| Sell at 3¢ | 32 | 8% | -$49.17 | -80% |
| Sell at 5¢ | 20 | 5% | -$48.65 | -79% |
| Sell at 10¢ | 9 | 2% | -$49.86 | -81% |
| Sell at 25¢ | 3 | 1% | -$51.72 | -84% |
| Sell at 50¢ | 2 | 0% | -$48.15 | -78% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 268 | 1 | 4% | 3% | -65% | -94% | 9 min |
| ITF Men's Match | ✘ | 258 | 0 | 9% | 4% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 248 | 0 | 11% | 5% | -100% | -80% | 4 min |
| Challenger ATP  | ✘ | 203 | 1 | 8% | 2% | -54% | -85% | 5 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 104 | 0 | 9% | 4% | -100% | -85% | 8 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| League of Legends Game | ✘ | 90 | 0 | 7% | 2% | -100% | -88% | 12 min |
| Women's College Volleyball Match | ✘ | 81 | 1 | 6% | 2% | +15% | -89% | 63 min |
| CONCACAF Nations League Game | partly | 69 | 1 | 20% | 9% | +35% | -65% | 26 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Men's T20 Cricket Match | ✘ | 45 | 0 | 16% | 7% | -100% | -73% | 17 min |
| Dota 2 Game | ✘ | 43 | 0 | 2% | 2% | -100% | -96% | 30 min |
| International Friendly Game | partly | 41 | 0 | 12% | 2% | -100% | -79% | 17 min |
| Challenger WTA | ✘ | 37 | 0 | 22% | 14% | -100% | -63% | 10 min |
| NHL Game | ✔ | 35 | 0 | 11% | 6% | -100% | -80% | 4 min |
| R6 Game | ✘ | 33 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| USL Championship Game | partly | 28 | 0 | 14% | 4% | -100% | -75% | 8 min |
| KHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 5 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| KBO Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 5 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga DIMAYOR Game | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 7 min |
| WTA Tennis Match | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 3 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| LaLiga 2 Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 9 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| AHL Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 7 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| ATP Tennis Match | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 3 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Uruguay Primera Division Game | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 14 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| NWSL Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 10 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| Slovakian 2. Liga Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 111 min |
| Overwatch Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| Argentine Nacional B Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 13 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Argentina Primera Division Game | ✘ | 13 | 0 | 15% | 15% | -100% | -73% | 12 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| NFL Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 2 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Women's Pro Basketball Game | ✔ | 9 | 0 | 33% | 11% | -100% | -42% | 12 min |
| Professional Baseball Game | partly | 9 | 0 | 22% | 11% | -100% | -61% | 5 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Bundesliga Basketball Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 13 min |
| Italy Serie A2 Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Adriatic ABA Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Canadian Premier League | ✘ | 7 | 1 | 57% | 57% | +1233% | -1% | 29 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Italy Serie A Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 6 min |
| College Hockey Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 24 min |
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
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NBA Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 157 | 6% | 1% | 0% | -90% |
| 5–15 min | 69 | 12% | 3% | 0% | -80% |
| 15–30 min | 75 | 29% | 12% | 1% | -49% |
| 30–60 min | 56 | 12% | 5% | 0% | -78% |
| Over 60 min | 53 | 13% | 9% | 0% | -77% |

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
| 10-04 21:12 | CONCACAF Nations League Game | Bahamas | ✘ | — | — | In play | — |
| 10-04 21:04 | Women's College Volleyball Match | Central Florida | ✘ | — | — | In play | — |
| 10-04 21:02 | USL Cup Game | Reg Time: Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 21:01 | USL Cup Game | Reg Time: Hartford Athletic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 21:01 | Rugby French 14 Match | RC Toulon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 21:01 | Rugby French 14 Match | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:57 | Liga DIMAYOR Game | Fortaleza | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 20:56 | Liga DIMAYOR Game | Pasto | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-04 20:55 | Darts Match | Gerwyn Price | ✘ | — | — | In play | — |
| 10-04 20:50 | LaLiga 2 Game | Girona | ✔ | 90'+2' · MLL 0 - GIR 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:50 | LaLiga 2 Game | Mallorca | ✔ | 90'+2' · MLL 0 - GIR 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:49 | R6 Game | LOUD | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:44 | Uruguay Primera Division Game | Tie | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 20:42 | UEFA Nations League Game | Tie | ✔ | 90'+5' · NOR 1 - POR 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:38 | UEFA Nations League Game | Germany | ✔ | 90'+3' · GER 0 - GRE 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:37 | UEFA Nations League Game | Greece | ✔ | 90'+3' · GER 0 - GRE 0 | 2¢ | ❌ Lost | -$0.15 |
| 10-04 20:37 | UEFA Nations League Game | Tie | ✔ | 90'+6' · SRB 1 - NED 2 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:37 | UEFA Nations League Game | Tie | ✔ | 90'+5' · DEN 1 - WAL 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:37 | UEFA Nations League Game | Ireland | ✔ | 90'+4' · ISR 1 - IRL 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:37 | UEFA Nations League Game | Israel | ✔ | 90'+4' · ISR 1 - IRL 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:29 | Serie C Game | Alcione Milano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:29 | Serie C Game | Trento | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:29 | Women's College Volleyball Match | Auburn | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:28 | UEFA Nations League Game | Norway | ✔ | 80' · NOR 1 - POR 2 | 1¢ | ❌ Lost | -$0.15 |
| 10-04 20:28 | UEFA Nations League Game | Wales | ✔ | 85' · DEN 1 - WAL 0 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:27 | Serie C Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:27 | Women's College Volleyball Match | Ole Miss | ✘ | — | — | In play | — |
| 10-04 20:26 | Uruguay Primera Division Game | Cerro | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-04 20:26 | Serie C Game | Latina | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 20:26 | Serie C Game | Ostia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
