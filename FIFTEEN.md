# 15-Minute 1¢ Study

*Updated Sat Nov 7, 7:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3939 finished bets | 1% | $150.75 | +34% | +3.83¢ | $87.80 / $62.95 |

*Expect about **96 buys a day** (~$14.47/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3661 | $80.30 | +20% |
| Volatility model ≥ 2%, hold to the close | 7235 | $39.85 | +5% |
| Momentum model ≥ 2%, hold to the close | 5974 | -$27.65 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49203 | 49186 | 179 (0%) | 1.07% | -$3,478.40 (-58%) | Hold to the close: -$3,478.40 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 29943 | 4.8% | 0.4% (115) | -705% | ❌ Worse |
| Momentum model | 29943 | 4.7% | 0.4% (115) | -731% | ❌ Worse |
| Mean-reversion model | 29943 | 8.1% | 0.4% (115) | -854% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29943 | 115 | -51% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7235 | 65 | +5% | -76% | -75% | -72% |
| Volatility model ≥ 5% | 3939 | 42 | +34% | -71% | -69% | -66% |
| Volatility model ≥ 10% | 2271 | 27 | +71% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 5974 | 47 | -4% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3661 | 34 | +20% | -73% | -72% | -69% |
| Momentum model ≥ 10% | 2403 | 23 | +35% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12366 | 83 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8671 | 72 | -8% | -79% | -78% | -76% |
| Mean-reversion model ≥ 10% | 5798 | 52 | +2% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30148 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49186 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 179 | 0% | -$3,478.40 | -58% | — |
| Sell at 2¢ | 1923 | 4% | -$5,204.42 | -87% | 47 sec |
| Sell at 3¢ | 1307 | 3% | -$5,194.67 | -87% | 48 sec |
| Sell at 5¢ | 907 | 2% | -$5,086.85 | -85% | 63 sec |
| Sell at 10¢ | 548 | 1% | -$4,874.52 | -81% | 65 sec |
| Sell at 25¢ | 287 | 1% | -$4,530.43 | -76% | 82 sec |
| Sell at 50¢ | 183 | 0% | -$4,147.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2422 | 10 | 11% | 4% | -61% | -81% | -83% |
| 2–5 min | 15813 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12421 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18518 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3380 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3374 | 14 | 4% | 2% | -47% | -87% | -87% |
| HYPE | 3364 | 10 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3359 | 17 | 5% | 2% | -36% | -85% | -85% |
| DOGE | 3351 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3349 | 13 | 7% | 3% | -52% | -81% | -81% |
| NEAR | 3328 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3325 | 16 | 5% | 2% | -34% | -88% | -89% |
| XRP | 3318 | 12 | 3% | 1% | -55% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24939 | 94 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24247 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4900 | 25 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 5163 | 19 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7772 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8944 | 34 | 6% | 3% | -58% | -87% | -87% |
| Over 0.5% | 3361 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11973 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13227 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 7:43:49 PM | BTC | UP | 71 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:43:49 PM | ZEC | UP | 71 sec | -0.286% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:43:49 PM | XRP | UP | 71 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:42:03 PM | HYPE | UP | 3.0 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:42:03 PM | NEAR | UP | 3.0 min | -0.411% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:42:03 PM | ETH | UP | 3.0 min | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:41:46 PM | BNB | UP | 3.2 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:41:14 PM | DOGE | UP | 3.8 min | -0.273% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:41:02 PM | SOL | UP | 4.0 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:29:55 PM | DOGE | DOWN | 5 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:29:55 PM | XRP | UP | 5 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:29:23 PM | ETH | DOWN | 37 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:29:07 PM | HYPE | DOWN | 53 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:28:51 PM | SOL | DOWN | 69 sec | +0.063% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:28:35 PM | BTC | DOWN | 85 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:28:35 PM | ZEC | DOWN | 85 sec | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:27:48 PM | NEAR | DOWN | 2.2 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:27:22 PM | BNB | DOWN | 2.6 min | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:14:21 PM | NEAR | UP | 38 sec | -0.163% | 0¢ | ❌ Lost | $0.00 |
| 11/7 7:13:17 PM | DOGE | UP | 1.7 min | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:13:17 PM | BTC | UP | 1.7 min | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:13:01 PM | SOL | UP | 2.0 min | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 7:12:45 PM | XRP | UP | 2.2 min | -0.130% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:12:45 PM | ETH | UP | 2.2 min | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:12:13 PM | BNB | UP | 2.8 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:11:09 PM | HYPE | UP | 3.8 min | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 7:09:49 PM | ZEC | UP | 5.2 min | -0.586% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 6:59:51 PM | NEAR | DOWN | 8 sec | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 6:59:35 PM | DOGE | DOWN | 24 sec | +0.015% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 6:59:19 PM | XRP | UP | 40 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
