# 15-Minute 1¢ Study

*Updated Sat Oct 17, 8:06 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1760 finished bets | 1% | $70.25 | +36% | +3.99¢ | $30.45 / $39.80 |

*Expect about **91 buys a day** (~$13.67/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1624 | $33.30 | +19% |
| Momentum model ≥ 2%, hold to the close | 2732 | -$23.55 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 1760 | -$32.25 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21875 | 21868 | 82 (0%) | 1.07% | -$1,510.45 (-57%) | Hold to the close: -$1,510.45 (-57%) |

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
| Volatility model | 14144 | 4.5% | 0.4% (56) | -658% | ❌ Worse |
| Momentum model | 14144 | 4.5% | 0.4% (56) | -680% | ❌ Worse |
| Mean-reversion model | 14144 | 7.5% | 0.4% (56) | -790% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14144 | 56 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3194 | 24 | -13% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 1760 | 19 | +36% | -74% | -74% | -70% |
| Volatility model ≥ 10% | 1029 | 11 | +52% | -67% | -67% | -64% |
| Momentum model ≥ 2% | 2732 | 21 | -7% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1624 | 15 | +19% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1079 | 10 | +29% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5386 | 35 | -29% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3715 | 27 | -20% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2448 | 16 | -25% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14342 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21868 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,510.45 | -57% | — |
| Sell at 2¢ | 790 | 4% | -$2,355.05 | -89% | 37 sec |
| Sell at 3¢ | 531 | 2% | -$2,353.36 | -89% | 47 sec |
| Sell at 5¢ | 382 | 2% | -$2,312.15 | -87% | 50 sec |
| Sell at 10¢ | 231 | 1% | -$2,229.84 | -84% | 63 sec |
| Sell at 25¢ | 130 | 1% | -$2,060.15 | -77% | 80 sec |
| Sell at 50¢ | 85 | 0% | -$1,846.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 755 | 5 | 10% | 3% | -37% | -82% | -85% |
| 2–5 min | 7070 | 38 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5682 | 20 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 8357 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1612 | 11 | 4% | 2% | -15% | -90% | -90% |
| HYPE | 1607 | 6 | 5% | 2% | -54% | -90% | -88% |
| ETH | 1597 | 8 | 6% | 3% | -40% | -87% | -86% |
| DOGE | 1596 | 2 | 4% | 2% | -84% | -91% | -90% |
| BNB | 1596 | 6 | 5% | 2% | -54% | -89% | -89% |
| SOL | 1590 | 2 | 4% | 2% | -85% | -92% | -91% |
| XRP | 1584 | 7 | 3% | 1% | -45% | -86% | -87% |
| NEAR | 1581 | 8 | 6% | 3% | -34% | -78% | -78% |
| BTC | 1579 | 8 | 5% | 2% | -32% | -88% | -91% |
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
| UP (bought YES) | 11042 | 41 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10826 | 41 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2432 | 12 | 2% | 1% | -18% | -81% | -80% |
| 0.05–0.1% | 2483 | 7 | 3% | 1% | -59% | -91% | -91% |
| 0.1–0.2% | 3611 | 12 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4168 | 21 | 6% | 3% | -44% | -88% | -88% |
| Over 0.5% | 1645 | 6 | 7% | 3% | -62% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5175 | 27 | 4% | 2% | -40% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,544 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 7:59:32 AM | HYPE | DOWN | 28 sec | +0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:59:16 AM | BTC | DOWN | 44 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:57:09 AM | BNB | DOWN | 2.9 min | +0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:56:54 AM | ETH | DOWN | 3.1 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:56:38 AM | NEAR | DOWN | 3.4 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:56:38 AM | DOGE | DOWN | 3.4 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:56:38 AM | XRP | DOWN | 3.4 min | +0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:56:38 AM | SOL | DOWN | 3.4 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:54:02 AM | ZEC | DOWN | 6.0 min | +0.765% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:44:29 AM | ZEC | UP | 31 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/17 7:44:14 AM | NEAR | DOWN | 45 sec | +0.282% | 0¢ | ❌ Lost | $0.00 |
| 10/17 7:43:58 AM | XRP | UP | 62 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:43:26 AM | HYPE | UP | 1.6 min | -0.105% | 10¢ | ❌ Lost | -$0.15 |
| 10/17 7:43:26 AM | BNB | UP | 1.6 min | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:42:53 AM | BTC | UP | 2.1 min | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:42:04 AM | DOGE | UP | 2.9 min | -0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:41:16 AM | SOL | UP | 3.7 min | -0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:40:10 AM | ETH | UP | 4.8 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:28:52 AM | BTC | DOWN | 67 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/17 7:28:36 AM | BNB | DOWN | 83 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:28:06 AM | ZEC | DOWN | 1.9 min | +0.403% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:28:06 AM | NEAR | DOWN | 1.9 min | +0.516% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:27:48 AM | SOL | DOWN | 2.2 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:27:16 AM | ETH | DOWN | 2.7 min | +0.121% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:27:01 AM | XRP | DOWN | 3.0 min | +0.186% | 0¢ | ❌ Lost | $0.00 |
| 10/17 7:27:01 AM | DOGE | DOWN | 3.0 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 7:25:57 AM | HYPE | UP | 4.0 min | -0.295% | 44¢ | ❌ Lost | -$0.15 |
| 10/17 7:14:42 AM | SOL | DOWN | 17 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/17 7:14:42 AM | HYPE | UP | 17 sec | -0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 7:14:10 AM | BNB | DOWN | 50 sec | -0.022% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
