# 15-Minute 1¢ Study

*Updated Sat Nov 7, 10:25 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3947 finished bets | 1% | $149.85 | +34% | +3.80¢ | $87.50 / $62.35 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3666 | $79.70 | +20% |
| Volatility model ≥ 2%, hold to the close | 7247 | $38.50 | +4% |
| Momentum model ≥ 2%, hold to the close | 5985 | -$29.00 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49279 | 49262 | 179 (0%) | 1.07% | -$3,487.40 (-58%) | Hold to the close: -$3,487.40 (-58%) |

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
| Volatility model | 30019 | 4.8% | 0.4% (115) | -706% | ❌ Worse |
| Momentum model | 30019 | 4.7% | 0.4% (115) | -732% | ❌ Worse |
| Mean-reversion model | 30019 | 8.1% | 0.4% (115) | -855% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30019 | 115 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7247 | 65 | +4% | -76% | -75% | -72% |
| Volatility model ≥ 5% | 3947 | 42 | +34% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2278 | 27 | +70% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 5985 | 47 | -4% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3666 | 34 | +20% | -73% | -72% | -69% |
| Momentum model ≥ 10% | 2408 | 23 | +34% | -64% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12396 | 83 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8694 | 72 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5814 | 52 | +2% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30224 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49262 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 179 | 0% | -$3,487.40 | -58% | — |
| Sell at 2¢ | 1924 | 4% | -$5,213.16 | -87% | 47 sec |
| Sell at 3¢ | 1307 | 3% | -$5,203.67 | -87% | 48 sec |
| Sell at 5¢ | 907 | 2% | -$5,095.85 | -85% | 63 sec |
| Sell at 10¢ | 548 | 1% | -$4,883.52 | -81% | 65 sec |
| Sell at 25¢ | 287 | 1% | -$4,539.43 | -76% | 82 sec |
| Sell at 50¢ | 183 | 0% | -$4,156.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2428 | 10 | 11% | 4% | -61% | -81% | -83% |
| 2–5 min | 15844 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12440 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18538 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3389 | 13 | 5% | 2% | -50% | -88% | -88% |
| SOL | 3382 | 14 | 4% | 2% | -47% | -87% | -87% |
| HYPE | 3373 | 10 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3367 | 17 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3360 | 6 | 4% | 2% | -78% | -90% | -90% |
| ETH | 3358 | 13 | 7% | 3% | -52% | -81% | -81% |
| NEAR | 3336 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3333 | 16 | 5% | 2% | -34% | -88% | -89% |
| XRP | 3326 | 12 | 3% | 1% | -55% | -90% | -89% |
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
| UP (bought YES) | 24971 | 94 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24291 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4918 | 25 | 2% | 1% | -11% | -76% | -76% |
| 0.05–0.1% | 5181 | 19 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7793 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 8959 | 34 | 6% | 3% | -58% | -87% | -87% |
| Over 0.5% | 3365 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11973 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13303 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,826 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 10:13:12 PM | HYPE | DOWN | 1.8 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 10:13:12 PM | BTC | DOWN | 1.8 min | +0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/7 10:13:12 PM | BNB | DOWN | 1.8 min | +0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 10:11:17 PM | ETH | DOWN | 3.7 min | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 10:11:17 PM | ZEC | DOWN | 3.7 min | +0.514% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 10:10:13 PM | NEAR | DOWN | 4.8 min | +0.415% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 10:09:56 PM | DOGE | DOWN | 5.0 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 10:09:38 PM | XRP | DOWN | 5.3 min | +0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 10:08:18 PM | SOL | DOWN | 6.7 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:59:06 PM | SOL | UP | 53 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 9:59:06 PM | BNB | UP | 53 sec | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:58:32 PM | BTC | UP | 87 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:58:01 PM | NEAR | UP | 2.0 min | -0.294% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 9:57:29 PM | HYPE | UP | 2.5 min | -0.162% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:57:29 PM | ZEC | UP | 2.5 min | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 11/7 9:56:57 PM | DOGE | UP | 3.0 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:55:52 PM | ETH | UP | 4.1 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:43:01 PM | BTC | UP | 2.0 min | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:42:43 PM | HYPE | UP | 2.3 min | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:42:27 PM | XRP | UP | 2.5 min | -0.121% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:42:27 PM | DOGE | UP | 2.5 min | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 9:42:27 PM | BNB | UP | 2.5 min | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:42:11 PM | ETH | UP | 2.8 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:40:51 PM | NEAR | UP | 4.1 min | -0.501% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:40:35 PM | ZEC | UP | 4.4 min | -0.330% | 2¢ | ❌ Lost | -$0.15 |
| 11/7 9:40:19 PM | SOL | UP | 4.7 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:29:55 PM | SOL | DOWN | 4 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/7 9:29:55 PM | HYPE | UP | 4 sec | -0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/7 9:29:23 PM | DOGE | DOWN | 36 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 9:29:08 PM | ETH | DOWN | 51 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
