# 15-Minute 1¢ Study

*Updated Wed Oct 14, 12:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1342 finished bets | 1% | $35.30 | +24% | +2.63¢ | $26.30 / $9.00 |

*Expect about **84 buys a day** (~$12.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1267 | $18.10 | +13% |
| 5+ min left, hold to the close | 524 | -$21.10 | -27% |
| Volatility model ≥ 5%, sell at 50¢ | 1342 | -$23.70 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17434 | 17427 | 65 (0%) | 1.07% | -$1,198.10 (-57%) | Hold to the close: -$1,198.10 (-57%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11455 | 4.5% | 0.4% (46) | -673% | ❌ Worse |
| Momentum model | 11455 | 4.4% | 0.4% (46) | -699% | ❌ Worse |
| Mean-reversion model | 11455 | 7.3% | 0.4% (46) | -794% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11455 | 46 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2378 | 18 | -12% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1342 | 13 | +24% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 821 | 9 | +58% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 2090 | 15 | -13% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1267 | 11 | +13% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 862 | 8 | +32% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4137 | 27 | -28% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2824 | 20 | -21% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1859 | 14 | -13% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11653 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4224 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1550 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17427 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,198.10 | -57% | — |
| Sell at 2¢ | 600 | 3% | -$1,910.10 | -91% | 33 sec |
| Sell at 3¢ | 402 | 2% | -$1,909.32 | -91% | 46 sec |
| Sell at 5¢ | 292 | 2% | -$1,876.30 | -89% | 48 sec |
| Sell at 10¢ | 186 | 1% | -$1,794.44 | -85% | 63 sec |
| Sell at 25¢ | 103 | 1% | -$1,669.17 | -79% | 67 sec |
| Sell at 50¢ | 66 | 0% | -$1,494.60 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 520 | 4 | 10% | 2% | -27% | -82% | -87% |
| 2–5 min | 5616 | 32 | 6% | 3% | -44% | -88% | -88% |
| 1–2 min | 4580 | 17 | 3% | 2% | -60% | -94% | -93% |
| Under 1 min | 6707 | 12 | 1% | 0% | -74% | -92% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1307 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1303 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1299 | 8 | 5% | 3% | -25% | -89% | -88% |
| BNB | 1299 | 5 | 4% | 2% | -53% | -90% | -91% |
| DOGE | 1297 | 2 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1294 | 2 | 3% | 1% | -81% | -93% | -92% |
| BTC | 1287 | 6 | 5% | 2% | -38% | -88% | -91% |
| XRP | 1284 | 7 | 2% | 1% | -32% | -85% | -86% |
| NEAR | 1283 | 7 | 5% | 2% | -29% | -77% | -78% |
| GOLD | 691 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 679 | 2 | 3% | 1% | -66% | -94% | -93% |
| WTI | 644 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 596 | 0 | 2% | 1% | -100% | -97% | -97% |
| PLATINUM | 568 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 525 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 521 | 3 | 2% | 2% | -46% | -96% | -95% |
| EURUSD | 503 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 474 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 432 | 3 | 1% | 1% | -35% | -98% | -98% |
| AUDUSD | 76 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 65 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8763 | 35 | 3% | 2% | -54% | -90% | -90% |
| DOWN (bought NO) | 8664 | 30 | 3% | 2% | -60% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2036 | 10 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 2073 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2979 | 9 | 4% | 2% | -63% | -91% | -91% |
| 0.2–0.5% | 3291 | 18 | 5% | 3% | -40% | -89% | -88% |
| Over 0.5% | 1271 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4387 | 20 | 4% | 2% | -48% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 12:44:15 AM | HYPE | DOWN | 45 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:43:58 AM | SOL | DOWN | 61 sec | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:58 AM | DOGE | DOWN | 61 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:43:58 AM | XRP | DOWN | 61 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:58 AM | ZEC | DOWN | 61 sec | +0.263% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:58 AM | ETH | DOWN | 61 sec | +0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:58 AM | BNB | DOWN | 61 sec | +0.007% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:42 AM | GBPUSD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:43:10 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:42:05 AM | NEAR | UP | 2.9 min | -0.685% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:52 AM | PALLADIUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:52 AM | ZEC | DOWN | 7 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:29:52 AM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:52 AM | COPPER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:29:20 AM | HYPE | DOWN | 40 sec | +0.097% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:29:20 AM | NATGAS | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:28:31 AM | SOL | UP | 88 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/14 12:28:31 AM | BTC | UP | 88 sec | -0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:58 AM | DOGE | UP | 2.0 min | -0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:58 AM | XRP | UP | 2.0 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:58 AM | ETH | UP | 2.0 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:27:58 AM | BNB | UP | 2.0 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:26:51 AM | NEAR | DOWN | 3.1 min | +0.456% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:26:04 AM | SILVER | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:26:04 AM | PLATINUM | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:25:25 AM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 12:14:40 AM | NATGAS | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:14:40 AM | AUDUSD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:13:49 AM | DOGE | DOWN | 71 sec | +0.079% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 12:13:49 AM | BTC | DOWN | 71 sec | +0.135% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
