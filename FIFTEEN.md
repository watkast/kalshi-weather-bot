# 15-Minute 1¢ Study

*Updated Mon Oct 5, 12:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 609 finished bets | 1% | $32.30 | +49% | +5.30¢ | -$5.45 / $37.75 |

*Expect about **81 buys a day** (~$12.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 610 | $18.90 | +29% |
| Volatility model ≥ 2%, hold to the close | 1136 | $16.90 | +12% |
| 5+ min left, hold to the close | 224 | $8.85 | +27% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8752 | 8746 | 37 (0%) | 1.07% | -$535.00 (-51%) | Hold to the close: -$535.00 (-51%) |

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
| Volatility model | 5758 | 4.1% | 0.4% (25) | -603% | ❌ Worse |
| Momentum model | 5758 | 4.2% | 0.4% (25) | -629% | ❌ Worse |
| Mean-reversion model | 5758 | 6.8% | 0.4% (25) | -706% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5758 | 25 | -45% | -85% | -85% | -83% |
| Volatility model ≥ 2% | 1136 | 11 | +12% | -70% | -70% | -65% |
| Volatility model ≥ 5% | 609 | 7 | +49% | -57% | -56% | -52% |
| Volatility model ≥ 10% | 377 | 5 | +96% | -37% | -39% | -33% |
| Momentum model ≥ 2% | 1001 | 8 | -3% | -71% | -73% | -71% |
| Momentum model ≥ 5% | 610 | 6 | +29% | -62% | -64% | -62% |
| Momentum model ≥ 10% | 422 | 5 | +70% | -49% | -50% | -47% |
| Mean-reversion model ≥ 2% | 1998 | 14 | -24% | -83% | -83% | -78% |
| Mean-reversion model ≥ 5% | 1341 | 12 | -1% | -80% | -80% | -73% |
| Mean-reversion model ≥ 10% | 884 | 9 | +18% | -78% | -79% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5955 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 2111 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 680 | 3% | 3% | 2% | 1% | 1% | 0% |
| **All** | 8746 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 37 | 0% | -$535.00 | -51% | — |
| Sell at 2¢ | 335 | 4% | -$937.90 | -89% | 33 sec |
| Sell at 3¢ | 218 | 2% | -$939.98 | -89% | 47 sec |
| Sell at 5¢ | 161 | 2% | -$920.35 | -87% | 61 sec |
| Sell at 10¢ | 107 | 1% | -$870.83 | -83% | 66 sec |
| Sell at 25¢ | 59 | 1% | -$787.71 | -75% | 1.5 min |
| Sell at 50¢ | 36 | 0% | -$698.00 | -66% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 221 | 3 | 11% | 3% | +28% | -81% | -88% |
| 2–5 min | 2844 | 20 | 7% | 3% | -31% | -87% | -87% |
| 1–2 min | 2307 | 9 | 3% | 2% | -58% | -93% | -93% |
| Under 1 min | 3371 | 5 | 1% | 0% | -78% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 673 | 5 | 5% | 3% | -11% | -89% | -89% |
| DOGE | 665 | 2 | 4% | 2% | -61% | -91% | -90% |
| ETH | 664 | 5 | 6% | 3% | -5% | -87% | -87% |
| HYPE | 664 | 3 | 5% | 3% | -45% | -89% | -87% |
| BNB | 660 | 2 | 4% | 2% | -64% | -90% | -92% |
| XRP | 659 | 4 | 2% | 1% | -23% | -77% | -78% |
| SOL | 659 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 657 | 3 | 5% | 2% | -40% | -87% | -89% |
| NEAR | 654 | 3 | 6% | 3% | -40% | -65% | -66% |
| GOLD | 355 | 0 | 4% | 1% | -100% | -91% | -93% |
| SILVER | 340 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 324 | 2 | 3% | 1% | -34% | -94% | -96% |
| COPPER | 300 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 270 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 264 | 2 | 3% | 2% | -29% | -94% | -92% |
| PALLADIUM | 258 | 1 | 2% | 1% | -64% | -97% | -98% |
| EURUSD | 243 | 1 | 5% | 3% | -62% | -92% | -90% |
| GBPUSD | 233 | 1 | 3% | 2% | -60% | -94% | -94% |
| USDJPY | 204 | 3 | 2% | 1% | +37% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4413 | 20 | 4% | 2% | -47% | -89% | -88% |
| DOWN (bought NO) | 4333 | 17 | 4% | 2% | -55% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 981 | 7 | 2% | 1% | +22% | -59% | -58% |
| 0.05–0.1% | 992 | 2 | 3% | 1% | -70% | -91% | -92% |
| 0.1–0.2% | 1490 | 6 | 4% | 2% | -49% | -91% | -91% |
| 0.2–0.5% | 1759 | 8 | 6% | 3% | -50% | -88% | -87% |
| Over 0.5% | 731 | 4 | 7% | 3% | -44% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2228 | 9 | 4% | 2% | -53% | -86% | -87% |
| Morning (6am–12pm) | 2361 | 17 | 5% | 3% | -18% | -90% | -88% |
| Afternoon (12–6pm) | 1763 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,120 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/5 12:14:53 PM | DOGE | DOWN | 7 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:53 PM | BNB | UP | 7 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:53 PM | BTC | DOWN | 7 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:21 PM | ETH | DOWN | 39 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:21 PM | PLATINUM | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:14:21 PM | NEAR | DOWN | 39 sec | +0.177% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:21 PM | XRP | DOWN | 39 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/5 12:14:04 PM | ZEC | DOWN | 55 sec | +0.160% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:48 PM | HYPE | UP | 72 sec | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:48 PM | SOL | UP | 72 sec | -0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:16 PM | SILVER | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 12:13:16 PM | EURUSD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:59:36 AM | DOGE | DOWN | 23 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:59:36 AM | HYPE | DOWN | 23 sec | +0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/5 11:59:04 AM | SILVER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:48 AM | EURUSD | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:32 AM | GBPUSD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:32 AM | BNB | DOWN | 88 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/5 11:58:32 AM | BTC | DOWN | 88 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:32 AM | XRP | DOWN | 88 sec | +0.120% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:16 AM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/5 11:58:16 AM | ZEC | DOWN | 1.7 min | +0.278% | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:00 AM | COPPER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:00 AM | NATGAS | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:00 AM | PALLADIUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:58:00 AM | SOL | DOWN | 2.0 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:57:41 AM | PLATINUM | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/5 11:57:41 AM | USDJPY | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:57:25 AM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/5 11:57:09 AM | ETH | DOWN | 2.9 min | +0.163% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
