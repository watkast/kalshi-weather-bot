# 15-Minute 1¢ Study

*Updated Sat Oct 3, 5:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **32 buys a day** (~$4.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 430 | -$3.30 | -7% |
| Momentum model ≥ 5%, sell at 50¢ | 430 | -$10.55 | -23% |
| 5+ min left, sell at 50¢ | 171 | -$11.70 | -46% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6473 | 6467 | 25 (0%) | 1.07% | -$430.30 (-55%) | Hold to the close: -$430.30 (-55%) |

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
| Volatility model | 3931 | 4.1% | 0.3% (13) | -712% | ❌ Worse |
| Momentum model | 3931 | 4.2% | 0.3% (13) | -750% | ❌ Worse |
| Mean-reversion model | 3931 | 7.1% | 0.3% (13) | -858% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3931 | 13 | -58% | -82% | -83% | -80% |
| Volatility model ≥ 2% | 830 | 5 | -30% | -66% | -67% | -62% |
| Volatility model ≥ 5% | 431 | 2 | -39% | -48% | -49% | -46% |
| Volatility model ≥ 10% | 258 | 2 | +17% | -18% | -23% | -17% |
| Momentum model ≥ 2% | 726 | 4 | -33% | -66% | -69% | -66% |
| Momentum model ≥ 5% | 430 | 3 | -7% | -52% | -57% | -52% |
| Momentum model ≥ 10% | 293 | 2 | -0% | -35% | -39% | -34% |
| Mean-reversion model ≥ 2% | 1470 | 7 | -48% | -83% | -85% | -80% |
| Mean-reversion model ≥ 5% | 992 | 6 | -33% | -79% | -81% | -74% |
| Mean-reversion model ≥ 10% | 647 | 4 | -29% | -77% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4128 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6467 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 25 | 0% | -$430.30 | -55% | — |
| Sell at 2¢ | 259 | 4% | -$684.96 | -88% | 34 sec |
| Sell at 3¢ | 164 | 3% | -$688.34 | -88% | 48 sec |
| Sell at 5¢ | 122 | 2% | -$673.00 | -86% | 62 sec |
| Sell at 10¢ | 81 | 1% | -$632.19 | -81% | 81 sec |
| Sell at 25¢ | 43 | 1% | -$581.97 | -75% | 1.6 min |
| Sell at 50¢ | 23 | 0% | -$527.05 | -68% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 2112 | 13 | 8% | 4% | -40% | -86% | -86% |
| 1–2 min | 1678 | 6 | 3% | 2% | -61% | -94% | -93% |
| Under 1 min | 2506 | 4 | 1% | 0% | -76% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 465 | 2 | 4% | 2% | -43% | -90% | -90% |
| ZEC | 463 | 2 | 5% | 3% | -48% | -89% | -91% |
| ETH | 462 | 2 | 6% | 3% | -45% | -86% | -85% |
| HYPE | 462 | 2 | 5% | 4% | -47% | -88% | -84% |
| BNB | 458 | 1 | 4% | 2% | -74% | -90% | -92% |
| SOL | 456 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 455 | 1 | 6% | 3% | -71% | -85% | -88% |
| XRP | 454 | 3 | 2% | 1% | -15% | -67% | -68% |
| NEAR | 453 | 2 | 6% | 3% | -41% | -54% | -56% |
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
| UP (bought YES) | 3277 | 16 | 4% | 2% | -43% | -88% | -87% |
| DOWN (bought NO) | 3190 | 9 | 4% | 2% | -67% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 570 | 3 | 1% | 1% | -3% | -30% | -31% |
| 0.05–0.1% | 630 | 0 | 3% | 1% | -100% | -91% | -93% |
| 0.1–0.2% | 1006 | 3 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 1327 | 5 | 6% | 3% | -58% | -88% | -87% |
| Over 0.5% | 593 | 4 | 7% | 3% | -30% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1664 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1858 | 6 | 3% | 2% | -62% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,363 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 5:44:14 AM | BTC | DOWN | 45 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:43:58 AM | ZEC | DOWN | 62 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:43:58 AM | SOL | DOWN | 62 sec | +0.020% | 3¢ | ❌ Lost | -$0.15 |
| 10/3 5:43:26 AM | BNB | DOWN | 1.6 min | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:42:54 AM | ETH | DOWN | 2.1 min | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:41:19 AM | XRP | DOWN | 3.7 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:40:31 AM | HYPE | DOWN | 4.5 min | +0.141% | 65¢ | ❌ Lost | -$0.15 |
| 10/3 5:40:15 AM | NEAR | DOWN | 4.8 min | +0.439% | 24¢ | ❌ Lost | -$0.15 |
| 10/3 5:40:15 AM | DOGE | DOWN | 4.8 min | +0.172% | 6¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:58 AM | NEAR | UP | 1 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:58 AM | DOGE | UP | 1 sec | -0.039% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:27 AM | XRP | DOWN | 32 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:27 AM | BTC | DOWN | 32 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:27 AM | SOL | DOWN | 32 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:27 AM | HYPE | DOWN | 32 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:29:11 AM | ZEC | DOWN | 48 sec | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:29:11 AM | ETH | DOWN | 48 sec | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:28:55 AM | BNB | UP | 65 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:14:13 AM | HYPE | UP | 47 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:58 AM | XRP | UP | 61 sec | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:27 AM | NEAR | UP | 1.6 min | -0.377% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:27 AM | ZEC | UP | 1.6 min | -0.157% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:13:27 AM | ETH | UP | 1.6 min | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/3 5:12:55 AM | DOGE | UP | 2.1 min | -0.062% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:11:51 AM | SOL | UP | 3.1 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 5:10:14 AM | BNB | DOWN | 4.8 min | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 4:59:57 AM | DOGE | DOWN | 3 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:59:57 AM | XRP | DOWN | 3 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/3 4:59:25 AM | NEAR | UP | 34 sec | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 4:59:09 AM | ZEC | DOWN | 50 sec | +0.130% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
