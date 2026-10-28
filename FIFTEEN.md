# 15-Minute 1¢ Study

*Updated Wed Oct 28, 5:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3037 finished bets | 1% | $78.60 | +23% | +2.59¢ | $84.00 / -$5.40 |

*Expect about **99 buys a day** (~$14.85/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2820 | $40.85 | +13% |
| Volatility model ≥ 2%, hold to the close | 5617 | $2.30 | +0% |
| Momentum model ≥ 2%, hold to the close | 4648 | -$64.45 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 37134 | 37106 | 138 (0%) | 1.07% | -$2,596.50 (-57%) | Hold to the close: -$2,596.50 (-57%) |

*In play or awaiting result: 27. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23078 | 4.7% | 0.4% (92) | -675% | ❌ Worse |
| Momentum model | 23078 | 4.6% | 0.4% (92) | -700% | ❌ Worse |
| Mean-reversion model | 23078 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23078 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5617 | 49 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3037 | 30 | +23% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1721 | 19 | +56% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4648 | 34 | -12% | -81% | -80% | -78% |
| Momentum model ≥ 5% | 2820 | 25 | +13% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1846 | 17 | +27% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9434 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6616 | 53 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4418 | 38 | -3% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23278 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8859 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4969 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 37106 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,596.50 | -57% | — |
| Sell at 2¢ | 1412 | 4% | -$3,965.38 | -88% | 47 sec |
| Sell at 3¢ | 971 | 3% | -$3,953.81 | -87% | 48 sec |
| Sell at 5¢ | 673 | 2% | -$3,895.05 | -86% | 63 sec |
| Sell at 10¢ | 408 | 1% | -$3,742.02 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,456.92 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,129.25 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1658 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11850 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9407 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14187 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2606 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2600 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2599 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2592 | 7 | 4% | 2% | -66% | -92% | -91% |
| ETH | 2587 | 11 | 6% | 3% | -49% | -85% | -85% |
| DOGE | 2585 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2572 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2569 | 12 | 5% | 2% | -40% | -82% | -82% |
| BTC | 2568 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1397 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1368 | 6 | 4% | 2% | -48% | -82% | -82% |
| WTI | 1350 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1214 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1152 | 4 | 1% | 1% | -68% | -73% | -73% |
| EURUSD | 1137 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1116 | 6 | 2% | 1% | -50% | -80% | -79% |
| GBPUSD | 1079 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1076 | 2 | 1% | 0% | -83% | -89% | -90% |
| USDJPY | 1059 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 614 | 4 | 1% | 1% | -39% | -83% | -81% |
| USDCAD | 581 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 186 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 133 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 125 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 124 | 1 | 4% | 1% | -25% | -18% | -16% |
| 5YRRATE | 117 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18773 | 77 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 18333 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3827 | 19 | 2% | 1% | -15% | -81% | -80% |
| 0.05–0.1% | 4008 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6063 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6851 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2525 | 10 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8832 | 29 | 4% | 2% | -62% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,556 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 5:59:50 PM | DOGE | DOWN | 9 sec | -0.013% | — | In play | — |
| 10/28 5:59:50 PM | PALLADIUM | DOWN | 9 sec | — | — | In play | — |
| 10/28 5:59:50 PM | BTC | DOWN | 9 sec | -0.005% | — | In play | — |
| 10/28 5:59:50 PM | WTI | DOWN | 9 sec | — | — | In play | — |
| 10/28 5:59:50 PM | NEAR | DOWN | 9 sec | -0.021% | — | In play | — |
| 10/28 5:59:50 PM | USDCAD | DOWN | 9 sec | — | — | In play | — |
| 10/28 5:59:34 PM | ZEC | DOWN | 25 sec | +0.081% | — | In play | — |
| 10/28 5:59:18 PM | COPPER | DOWN | 41 sec | — | — | In play | — |
| 10/28 5:59:18 PM | ETH | DOWN | 41 sec | +0.029% | — | In play | — |
| 10/28 5:59:18 PM | SOL | DOWN | 41 sec | +0.031% | — | In play | — |
| 10/28 5:59:02 PM | HYPE | UP | 58 sec | -0.074% | — | In play | — |
| 10/28 5:58:46 PM | NATGAS | DOWN | 74 sec | — | — | In play | — |
| 10/28 5:58:46 PM | GBPUSD | UP | 74 sec | — | — | In play | — |
| 10/28 5:58:46 PM | EURUSD | UP | 74 sec | — | — | In play | — |
| 10/28 5:57:08 PM | BNB | DOWN | 2.9 min | +0.098% | — | In play | — |
| 10/28 5:57:08 PM | PLATINUM | DOWN | 2.9 min | — | — | In play | — |
| 10/28 5:56:35 PM | AUDUSD | DOWN | 3.4 min | — | — | In play | — |
| 10/28 5:56:19 PM | SILVER | DOWN | 3.7 min | — | — | In play | — |
| 10/28 5:55:33 PM | GOLD | DOWN | 4.4 min | — | — | In play | — |
| 10/28 5:55:17 PM | USDJPY | DOWN | 4.7 min | — | — | In play | — |
| 10/28 5:44:56 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:44:24 PM | HYPE | UP | 35 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:24 PM | SOL | UP | 35 sec | -0.096% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:44:08 PM | DOGE | UP | 51 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:44:08 PM | COPPER | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:44:08 PM | BRENT | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:52 PM | XRP | UP | 67 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/28 5:43:52 PM | EURUSD | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:36 PM | SILVER | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/28 5:43:36 PM | ETH | UP | 83 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
