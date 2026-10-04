# 15-Minute 1¢ Study

*Updated Sun Oct 4, 12:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 187 finished bets | 2% | $14.40 | +52% | +7.70¢ | $14.20 / $0.20 |

*Expect about **28 buys a day** (~$4.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 537 | $11.80 | +20% |
| Volatility model ≥ 2%, hold to the close | 1005 | $4.20 | +3% |
| Mean-reversion model ≥ 5%, hold to the close | 1193 | $3.10 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7525 | 7519 | 34 (0%) | 1.07% | -$427.00 (-47%) | Hold to the close: -$427.00 (-47%) |

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
| Volatility model | 4983 | 4.2% | 0.4% (22) | -627% | ❌ Worse |
| Momentum model | 4983 | 4.3% | 0.4% (22) | -660% | ❌ Worse |
| Mean-reversion model | 4983 | 7.0% | 0.4% (22) | -727% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4983 | 22 | -44% | -84% | -84% | -82% |
| Volatility model ≥ 2% | 1005 | 9 | +3% | -68% | -68% | -63% |
| Volatility model ≥ 5% | 537 | 5 | +20% | -54% | -53% | -48% |
| Volatility model ≥ 10% | 334 | 4 | +75% | -33% | -34% | -28% |
| Momentum model ≥ 2% | 884 | 6 | -18% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 543 | 4 | -4% | -60% | -63% | -59% |
| Momentum model ≥ 10% | 373 | 3 | +14% | -46% | -48% | -44% |
| Mean-reversion model ≥ 2% | 1771 | 12 | -26% | -82% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1193 | 11 | +2% | -78% | -79% | -71% |
| Mean-reversion model ≥ 10% | 784 | 8 | +18% | -76% | -77% | -69% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5180 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7519 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 34 | 0% | -$427.00 | -47% | — |
| Sell at 2¢ | 306 | 4% | -$795.44 | -88% | 34 sec |
| Sell at 3¢ | 197 | 3% | -$798.17 | -88% | 48 sec |
| Sell at 5¢ | 145 | 2% | -$780.75 | -86% | 61 sec |
| Sell at 10¢ | 99 | 1% | -$731.31 | -81% | 78 sec |
| Sell at 25¢ | 55 | 1% | -$664.95 | -74% | 1.6 min |
| Sell at 50¢ | 33 | 0% | -$582.25 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 184 | 3 | 12% | 3% | +55% | -78% | -87% |
| 2–5 min | 2435 | 18 | 8% | 4% | -28% | -85% | -86% |
| 1–2 min | 1977 | 8 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2920 | 5 | 1% | 0% | -74% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 584 | 4 | 5% | 3% | -19% | -88% | -89% |
| DOGE | 580 | 2 | 4% | 2% | -56% | -91% | -91% |
| HYPE | 579 | 2 | 5% | 3% | -58% | -89% | -86% |
| ETH | 578 | 5 | 6% | 3% | +9% | -85% | -85% |
| BNB | 574 | 2 | 5% | 2% | -58% | -90% | -92% |
| SOL | 573 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 572 | 3 | 6% | 2% | -32% | -86% | -89% |
| XRP | 571 | 4 | 2% | 1% | -10% | -73% | -74% |
| NEAR | 569 | 2 | 6% | 3% | -53% | -62% | -63% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3788 | 19 | 4% | 2% | -41% | -88% | -87% |
| DOWN (bought NO) | 3731 | 15 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 863 | 7 | 2% | 1% | +36% | -55% | -54% |
| 0.05–0.1% | 888 | 2 | 3% | 1% | -67% | -91% | -93% |
| 0.1–0.2% | 1276 | 4 | 4% | 2% | -60% | -90% | -91% |
| 0.2–0.5% | 1505 | 7 | 6% | 4% | -49% | -87% | -86% |
| Over 0.5% | 646 | 4 | 7% | 3% | -36% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1521 | 3 | 3% | 1% | -77% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,042 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 12:14:12 PM | HYPE | DOWN | 48 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:14:12 PM | ZEC | UP | 48 sec | -0.226% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 12:13:56 PM | ETH | UP | 64 sec | -0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:13:56 PM | XRP | UP | 64 sec | -0.080% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:13:40 PM | BNB | DOWN | 79 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/4 12:12:53 PM | DOGE | UP | 2.1 min | -0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:12:53 PM | NEAR | DOWN | 2.1 min | +0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 12:12:37 PM | SOL | UP | 2.4 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:59:34 AM | XRP | UP | 25 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:59:34 AM | NEAR | UP | 25 sec | -0.185% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:47 AM | ETH | UP | 73 sec | -0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:31 AM | BTC | UP | 89 sec | -0.089% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:15 AM | BNB | UP | 1.8 min | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:15 AM | ZEC | UP | 1.8 min | -0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:27 AM | SOL | UP | 2.5 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:11 AM | DOGE | UP | 2.8 min | -0.507% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:11 AM | HYPE | DOWN | 2.8 min | +0.254% | 1¢ | ❌ Lost | $0.00 |
| 10/4 11:44:48 AM | BTC | DOWN | 11 sec | +0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:32 AM | HYPE | DOWN | 27 sec | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:16 AM | XRP | DOWN | 43 sec | +0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:43:45 AM | ZEC | DOWN | 75 sec | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:43:29 AM | NEAR | DOWN | 1.5 min | +0.369% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:43:13 AM | DOGE | DOWN | 1.8 min | +0.612% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:57 AM | ETH | UP | 2.0 min | -0.036% | 98¢ | ✅ Won | $13.85 |
| 10/4 11:42:42 AM | BNB | UP | 2.3 min | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:42 AM | BTC | UP | 2.3 min | -0.049% | 99¢ | ✅ Won | $13.85 |
| 10/4 11:42:10 AM | SOL | UP | 2.8 min | -0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:44 AM | HYPE | DOWN | 15 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:12 AM | NEAR | DOWN | 47 sec | +0.184% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:28:56 AM | DOGE | DOWN | 63 sec | +0.198% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
