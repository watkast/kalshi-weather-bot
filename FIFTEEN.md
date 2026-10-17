# 15-Minute 1¢ Study

*Updated Sat Oct 17, 5:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1748 finished bets | 1% | $72.05 | +37% | +4.12¢ | $31.05 / $41.00 |

*Expect about **91 buys a day** (~$13.66/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1614 | $34.80 | +20% |
| Momentum model ≥ 2%, hold to the close | 2717 | -$21.30 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 1748 | -$30.45 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21780 | 21772 | 82 (0%) | 1.07% | -$1,498.90 (-57%) | Hold to the close: -$1,498.90 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 14048 | 4.5% | 0.4% (56) | -658% | ❌ Worse |
| Momentum model | 14048 | 4.5% | 0.4% (56) | -680% | ❌ Worse |
| Mean-reversion model | 14048 | 7.5% | 0.4% (56) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14048 | 56 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3172 | 24 | -13% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1748 | 19 | +37% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1024 | 11 | +53% | -67% | -66% | -64% |
| Momentum model ≥ 2% | 2717 | 21 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1614 | 15 | +20% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1073 | 10 | +31% | -73% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5345 | 35 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3689 | 27 | -19% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2430 | 16 | -25% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14246 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21772 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,498.90 | -57% | — |
| Sell at 2¢ | 780 | 4% | -$2,346.10 | -89% | 37 sec |
| Sell at 3¢ | 523 | 2% | -$2,344.93 | -89% | 47 sec |
| Sell at 5¢ | 377 | 2% | -$2,303.85 | -87% | 50 sec |
| Sell at 10¢ | 228 | 1% | -$2,222.22 | -84% | 63 sec |
| Sell at 25¢ | 128 | 1% | -$2,055.22 | -78% | 78 sec |
| Sell at 50¢ | 85 | 0% | -$1,835.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 744 | 5 | 10% | 3% | -36% | -82% | -85% |
| 2–5 min | 7036 | 38 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5662 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8326 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1601 | 11 | 4% | 2% | -14% | -90% | -90% |
| HYPE | 1596 | 6 | 4% | 2% | -54% | -90% | -88% |
| ETH | 1587 | 8 | 6% | 3% | -39% | -87% | -86% |
| DOGE | 1585 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1585 | 6 | 5% | 2% | -53% | -89% | -89% |
| SOL | 1580 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1574 | 7 | 3% | 1% | -45% | -86% | -87% |
| NEAR | 1570 | 8 | 6% | 3% | -34% | -78% | -78% |
| BTC | 1568 | 8 | 5% | 2% | -32% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10972 | 41 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10800 | 41 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2411 | 12 | 2% | 1% | -17% | -81% | -80% |
| 0.05–0.1% | 2463 | 7 | 3% | 1% | -59% | -92% | -91% |
| 0.1–0.2% | 3587 | 12 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 4145 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1637 | 6 | 6% | 3% | -62% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5541 | 22 | 4% | 2% | -55% | -88% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,522 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 5:22:24 AM | HYPE | UP | 7.6 min | -0.469% | — | In play | — |
| 10/17 5:14:44 AM | DOGE | DOWN | 16 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:14:44 AM | XRP | UP | 16 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:14:44 AM | ETH | DOWN | 16 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:14:44 AM | BTC | DOWN | 16 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:14:10 AM | BNB | DOWN | 49 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:54 AM | NEAR | DOWN | 65 sec | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:38 AM | ZEC | UP | 81 sec | -0.219% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:22 AM | SOL | UP | 1.6 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:22 AM | HYPE | UP | 1.6 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:59 AM | ZEC | DOWN | 0 sec | +0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:43 AM | DOGE | DOWN | 16 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:59:43 AM | BTC | UP | 16 sec | -0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:59:27 AM | SOL | UP | 32 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:58:54 AM | BNB | UP | 66 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:58:38 AM | XRP | DOWN | 82 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:58:22 AM | HYPE | UP | 1.6 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:57:31 AM | ETH | DOWN | 2.5 min | +0.117% | 21¢ | ❌ Lost | -$0.15 |
| 10/17 4:57:00 AM | NEAR | DOWN | 3.0 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:44:49 AM | BTC | DOWN | 10 sec | +0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:44:17 AM | NEAR | UP | 43 sec | -0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:25 AM | HYPE | DOWN | 2.6 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:25 AM | XRP | DOWN | 2.6 min | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:09 AM | BNB | DOWN | 2.9 min | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:09 AM | SOL | DOWN | 2.9 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:41:53 AM | ZEC | DOWN | 3.1 min | +0.336% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:41:53 AM | DOGE | DOWN | 3.1 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:41:17 AM | ETH | DOWN | 3.7 min | +0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:29:29 AM | NEAR | DOWN | 30 sec | -0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:29:13 AM | HYPE | UP | 47 sec | -0.019% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
