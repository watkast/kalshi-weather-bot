# 15-Minute 1¢ Study

*Updated Fri Oct 9, 9:20 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 914 finished bets | 1% | $40.40 | +41% | +4.42¢ | -$6.45 / $46.85 |

*Expect about **77 buys a day** (~$11.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 892 | $16.30 | +17% |
| 5+ min left, hold to the close | 386 | -$1.00 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 914 | -$4.10 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13475 | 13468 | 54 (0%) | 1.07% | -$877.65 (-54%) | Hold to the close: -$877.65 (-54%) |

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
| Volatility model | 8624 | 4.0% | 0.4% (37) | -573% | ❌ Worse |
| Momentum model | 8624 | 4.1% | 0.4% (37) | -606% | ❌ Worse |
| Mean-reversion model | 8624 | 6.7% | 0.4% (37) | -670% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8624 | 37 | -46% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 1664 | 14 | -3% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 914 | 10 | +41% | -68% | -67% | -64% |
| Volatility model ≥ 10% | 562 | 8 | +107% | -53% | -53% | -49% |
| Momentum model ≥ 2% | 1471 | 11 | -10% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 892 | 8 | +17% | -71% | -72% | -70% |
| Momentum model ≥ 10% | 609 | 6 | +41% | -62% | -63% | -60% |
| Mean-reversion model ≥ 2% | 3008 | 22 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2028 | 17 | -8% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1332 | 13 | +12% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8822 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3443 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13468 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 54 | 0% | -$877.65 | -54% | — |
| Sell at 2¢ | 454 | 3% | -$1,473.61 | -90% | 33 sec |
| Sell at 3¢ | 305 | 2% | -$1,472.70 | -90% | 47 sec |
| Sell at 5¢ | 223 | 2% | -$1,446.70 | -89% | 50 sec |
| Sell at 10¢ | 146 | 1% | -$1,372.39 | -84% | 64 sec |
| Sell at 25¢ | 83 | 1% | -$1,260.92 | -77% | 82 sec |
| Sell at 50¢ | 55 | 0% | -$1,122.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 382 | 4 | 10% | 3% | -1% | -82% | -85% |
| 2–5 min | 4353 | 28 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3517 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5212 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 987 | 6 | 4% | 3% | -26% | -90% | -90% |
| DOGE | 985 | 2 | 3% | 2% | -74% | -92% | -92% |
| HYPE | 985 | 3 | 4% | 2% | -62% | -90% | -88% |
| BNB | 985 | 5 | 4% | 2% | -39% | -90% | -91% |
| ETH | 979 | 7 | 5% | 2% | -12% | -89% | -88% |
| NEAR | 977 | 5 | 6% | 2% | -33% | -73% | -74% |
| SOL | 976 | 1 | 3% | 1% | -87% | -94% | -93% |
| BTC | 974 | 4 | 5% | 2% | -46% | -88% | -90% |
| XRP | 974 | 6 | 2% | 1% | -23% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 430 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6775 | 28 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6693 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1443 | 8 | 2% | 1% | -5% | -70% | -70% |
| 0.05–0.1% | 1508 | 5 | 3% | 1% | -51% | -92% | -92% |
| 0.1–0.2% | 2251 | 8 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2561 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1056 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3744 | 10 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,098 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 9:14:49 PM | WTI | DOWN | 11 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 9:14:00 PM | NEAR | UP | 60 sec | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:14:00 PM | HYPE | UP | 60 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:13:28 PM | BTC | UP | 1.5 min | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:13:11 PM | SOL | UP | 1.8 min | -0.147% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:13:11 PM | ZEC | UP | 1.8 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:12:53 PM | DOGE | UP | 2.1 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 9:12:53 PM | XRP | UP | 2.1 min | -0.206% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 9:11:33 PM | BNB | UP | 3.4 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 8:59:27 PM | WTI | DOWN | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/9 8:58:57 PM | BNB | DOWN | 63 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:58:41 PM | DOGE | DOWN | 79 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:58:41 PM | NEAR | UP | 79 sec | -0.280% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 8:57:18 PM | SOL | UP | 2.7 min | -0.169% | 83¢ | ✅ Won | $13.85 |
| 10/9 8:57:03 PM | XRP | UP | 2.9 min | -0.192% | 8¢ | ❌ Lost | -$0.15 |
| 10/9 8:57:03 PM | ETH | UP | 2.9 min | -0.088% | 9¢ | ❌ Lost | -$0.15 |
| 10/9 8:57:03 PM | HYPE | UP | 2.9 min | -0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:55:58 PM | ZEC | UP | 4.0 min | -0.335% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 8:44:58 PM | HYPE | UP | 2 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:44:42 PM | ETH | DOWN | 18 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/9 8:44:26 PM | BTC | UP | 34 sec | -0.018% | 4¢ | ❌ Lost | -$0.15 |
| 10/9 8:44:11 PM | XRP | DOWN | 48 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/9 8:44:11 PM | BNB | DOWN | 48 sec | -0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:43:39 PM | SOL | DOWN | 81 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/9 8:42:34 PM | DOGE | DOWN | 2.4 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 8:40:23 PM | ZEC | DOWN | 4.6 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 8:39:01 PM | NEAR | DOWN | 6.0 min | +1.005% | 3¢ | ❌ Lost | -$0.15 |
| 10/9 8:29:35 PM | DOGE | DOWN | 24 sec | +0.038% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:29:18 PM | XRP | UP | 42 sec | -0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 8:28:29 PM | BNB | UP | 1.5 min | -0.114% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
