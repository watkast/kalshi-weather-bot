# 15-Minute 1¢ Study

*Updated Thu Oct 29, 5:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3112 finished bets | 1% | $84.80 | +24% | +2.72¢ | $79.50 / $5.30 |

*Expect about **98 buys a day** (~$14.73/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2882 | $34.25 | +11% |
| Volatility model ≥ 2%, hold to the close | 5758 | $0.40 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3112 | -$69.45 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 38422 | 38400 | 143 (0%) | 1.07% | -$2,686.10 (-57%) | Hold to the close: -$2,686.10 (-57%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 23665 | 4.7% | 0.4% (93) | -678% | ❌ Worse |
| Momentum model | 23665 | 4.6% | 0.4% (93) | -701% | ❌ Worse |
| Mean-reversion model | 23665 | 8.0% | 0.4% (93) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 23665 | 93 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5758 | 50 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3112 | 31 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1757 | 19 | +54% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4759 | 34 | -14% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2882 | 25 | +11% | -78% | -77% | -73% |
| Momentum model ≥ 10% | 1882 | 17 | +25% | -72% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9684 | 64 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6787 | 54 | -12% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4529 | 39 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23866 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9223 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5311 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 38400 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 143 | 0% | -$2,686.10 | -57% | — |
| Sell at 2¢ | 1472 | 4% | -$4,109.38 | -88% | 47 sec |
| Sell at 3¢ | 1015 | 3% | -$4,096.25 | -87% | 49 sec |
| Sell at 5¢ | 708 | 2% | -$4,017.90 | -86% | 63 sec |
| Sell at 10¢ | 428 | 1% | -$3,847.42 | -82% | 65 sec |
| Sell at 25¢ | 226 | 1% | -$3,548.04 | -76% | 83 sec |
| Sell at 50¢ | 146 | 0% | -$3,226.60 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1774 | 8 | 11% | 4% | -57% | -80% | -81% |
| 2–5 min | 12214 | 68 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9724 | 34 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 14679 | 33 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2670 | 12 | 5% | 3% | -42% | -88% | -88% |
| HYPE | 2667 | 8 | 5% | 3% | -63% | -89% | -87% |
| BNB | 2665 | 15 | 5% | 2% | -30% | -85% | -84% |
| SOL | 2658 | 7 | 4% | 2% | -67% | -92% | -91% |
| ETH | 2651 | 11 | 6% | 3% | -50% | -86% | -85% |
| DOGE | 2651 | 6 | 4% | 2% | -72% | -90% | -90% |
| BTC | 2635 | 13 | 5% | 2% | -34% | -88% | -89% |
| XRP | 2635 | 11 | 3% | 1% | -49% | -89% | -89% |
| NEAR | 2634 | 12 | 5% | 2% | -41% | -82% | -82% |
| GOLD | 1448 | 5 | 4% | 2% | -58% | -82% | -83% |
| SILVER | 1417 | 7 | 5% | 2% | -42% | -82% | -81% |
| WTI | 1405 | 4 | 3% | 1% | -66% | -93% | -94% |
| PLATINUM | 1252 | 2 | 2% | 1% | -85% | -97% | -96% |
| COPPER | 1196 | 5 | 1% | 1% | -61% | -74% | -74% |
| EURUSD | 1193 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1158 | 7 | 2% | 1% | -44% | -80% | -79% |
| GBPUSD | 1129 | 2 | 2% | 1% | -83% | -96% | -96% |
| PALLADIUM | 1119 | 2 | 1% | 0% | -83% | -90% | -90% |
| USDJPY | 1109 | 5 | 2% | 1% | -58% | -97% | -96% |
| AUDUSD | 664 | 4 | 1% | 1% | -44% | -84% | -82% |
| USDCAD | 624 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 228 | 0 | 0% | 0% | -100% | -99% | -99% |
| 10YRRATE | 158 | 0 | 4% | 1% | -100% | -92% | -90% |
| 30YRRATE | 152 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 146 | 1 | 5% | 1% | -36% | -28% | -27% |
| 5YRRATE | 136 | 1 | 7% | 3% | -31% | -89% | -90% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 19491 | 78 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 18909 | 65 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3876 | 19 | 2% | 1% | -15% | -81% | -81% |
| 0.05–0.1% | 4089 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6182 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7058 | 30 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2657 | 10 | 7% | 3% | -61% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9458 | 35 | 4% | 2% | -58% | -86% | -86% |
| Morning (6am–12pm) | 9668 | 43 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9112 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10162 | 34 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/29 5:14:01 PM | USDCAD | DOWN | 59 sec | — | — | In play | — |
| 10/29 5:13:29 PM | COPPER | DOWN | 1.5 min | — | — | In play | — |
| 10/29 5:13:13 PM | XRP | UP | 1.8 min | -0.418% | — | In play | — |
| 10/29 5:12:41 PM | ETH | UP | 2.3 min | -0.465% | — | In play | — |
| 10/29 5:12:25 PM | DOGE | UP | 2.6 min | -0.417% | — | In play | — |
| 10/29 5:12:25 PM | SOL | UP | 2.6 min | -0.493% | — | In play | — |
| 10/29 5:11:53 PM | BTC | UP | 3.1 min | -0.307% | — | In play | — |
| 10/29 5:11:22 PM | HYPE | UP | 3.6 min | -0.995% | — | In play | — |
| 10/29 5:11:06 PM | USDJPY | DOWN | 3.9 min | — | — | In play | — |
| 10/29 5:10:02 PM | SILVER | UP | 5.0 min | — | — | In play | — |
| 10/29 5:08:59 PM | ZEC | UP | 6.0 min | -1.657% | — | In play | — |
| 10/29 5:08:43 PM | GOLD | UP | 6.3 min | — | — | In play | — |
| 10/29 4:59:30 PM | PALLADIUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:59:14 PM | BRENT | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:59:14 PM | BTC | UP | 46 sec | -0.003% | 2¢ | ❌ Lost | -$0.15 |
| 10/29 4:59:14 PM | ETH | UP | 46 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:58:42 PM | BNB | DOWN | 78 sec | +0.184% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:58:42 PM | SILVER | DOWN | 78 sec | — | 5¢ | ✅ Won | $13.85 |
| 10/29 4:58:42 PM | NEAR | UP | 78 sec | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:58:42 PM | NATGAS | UP | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:58:10 PM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:58:10 PM | DOGE | UP | 1.8 min | -0.417% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:57:54 PM | HYPE | UP | 2.1 min | -0.570% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:57:38 PM | SOL | UP | 2.4 min | -0.428% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:57:06 PM | XRP | UP | 2.9 min | -0.488% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:56:35 PM | ZEC | UP | 3.4 min | -0.930% | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:56:19 PM | USDJPY | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:55:47 PM | GOLD | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/29 4:55:15 PM | EURUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/29 4:55:15 PM | GBPUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
