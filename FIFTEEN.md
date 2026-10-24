# 15-Minute 1¢ Study

*Updated Sat Oct 24, 5:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2593 finished bets | 1% | $97.55 | +33% | +3.76¢ | $39.95 / $57.60 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2392 | $70.95 | +27% |
| Volatility model ≥ 2%, hold to the close | 4788 | $14.90 | +3% |
| Momentum model ≥ 2%, hold to the close | 3996 | -$7.80 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31018 | 31010 | 119 (0%) | 1.07% | -$2,108.45 (-56%) | Hold to the close: -$2,108.45 (-56%) |

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
| Volatility model | 19803 | 4.6% | 0.4% (84) | -637% | ❌ Worse |
| Momentum model | 19803 | 4.6% | 0.4% (84) | -663% | ❌ Worse |
| Mean-reversion model | 19803 | 7.9% | 0.4% (84) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19803 | 84 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4788 | 43 | +3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 2593 | 28 | +33% | -74% | -72% | -69% |
| Volatility model ≥ 10% | 1475 | 18 | +71% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 3996 | 33 | -2% | -80% | -79% | -76% |
| Momentum model ≥ 5% | 2392 | 24 | +27% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1564 | 16 | +40% | -70% | -69% | -64% |
| Mean-reversion model ≥ 2% | 7961 | 55 | -25% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5569 | 46 | -9% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3706 | 33 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20003 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31010 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,108.45 | -56% | — |
| Sell at 2¢ | 1156 | 4% | -$3,305.89 | -88% | 47 sec |
| Sell at 3¢ | 793 | 3% | -$3,297.18 | -87% | 48 sec |
| Sell at 5¢ | 555 | 2% | -$3,245.70 | -86% | 61 sec |
| Sell at 10¢ | 342 | 1% | -$3,116.43 | -83% | 64 sec |
| Sell at 25¢ | 188 | 1% | -$2,872.17 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,593.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1334 | 7 | 11% | 4% | -50% | -80% | -82% |
| 2–5 min | 9905 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7873 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11894 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2243 | 12 | 5% | 2% | -33% | -89% | -89% |
| HYPE | 2235 | 8 | 5% | 3% | -56% | -88% | -86% |
| BNB | 2231 | 12 | 5% | 2% | -33% | -83% | -82% |
| SOL | 2227 | 6 | 4% | 2% | -67% | -92% | -91% |
| ETH | 2222 | 11 | 6% | 3% | -41% | -86% | -85% |
| DOGE | 2217 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2214 | 9 | 3% | 1% | -50% | -88% | -88% |
| NEAR | 2211 | 12 | 5% | 3% | -29% | -81% | -81% |
| BTC | 2203 | 12 | 5% | 2% | -27% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15695 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15315 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3334 | 18 | 2% | 1% | -9% | -80% | -79% |
| 0.05–0.1% | 3449 | 11 | 3% | 1% | -53% | -92% | -92% |
| 0.1–0.2% | 5147 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5823 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2246 | 10 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7739 | 32 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 7570 | 34 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7316 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 5:29:39 PM | BNB | DOWN | 21 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:29:39 PM | BTC | DOWN | 21 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:29:23 PM | XRP | DOWN | 37 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:29:23 PM | ETH | DOWN | 37 sec | +0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/24 5:28:33 PM | SOL | DOWN | 87 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:28:33 PM | DOGE | DOWN | 87 sec | +0.091% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:28:17 PM | NEAR | DOWN | 1.7 min | +0.342% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:28:02 PM | HYPE | DOWN | 1.9 min | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:25:21 PM | ZEC | UP | 4.6 min | -0.379% | 27¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:54 PM | ZEC | UP | 5 sec | -0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:54 PM | ETH | UP | 5 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:38 PM | BNB | DOWN | 21 sec | -0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:38 PM | NEAR | DOWN | 21 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:22 PM | BTC | DOWN | 37 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:06 PM | SOL | DOWN | 54 sec | +0.041% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:14:06 PM | HYPE | UP | 54 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 5:13:32 PM | XRP | UP | 88 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 5:13:32 PM | DOGE | UP | 88 sec | -0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/24 10:14:24 AM | ETH | DOWN | 36 sec | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 10:14:24 AM | BTC | DOWN | 36 sec | +0.058% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 10:14:09 AM | BNB | DOWN | 50 sec | +0.096% | 0¢ | ❌ Lost | $0.00 |
| 10/24 10:13:05 AM | HYPE | DOWN | 1.9 min | +0.450% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 10:13:05 AM | DOGE | DOWN | 1.9 min | +0.319% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 10:13:05 AM | NEAR | DOWN | 1.9 min | +1.198% | 0¢ | ❌ Lost | $0.00 |
| 10/24 10:13:05 AM | XRP | DOWN | 1.9 min | +0.363% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 10:13:05 AM | SOL | DOWN | 1.9 min | +0.335% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 10:13:05 AM | ZEC | DOWN | 1.9 min | +0.618% | 0¢ | ❌ Lost | $0.00 |
| 10/24 9:56:59 AM | NEAR | DOWN | 3.0 min | +0.799% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:56:41 AM | HYPE | DOWN | 3.3 min | +0.304% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 9:56:41 AM | BNB | DOWN | 3.3 min | +0.184% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
