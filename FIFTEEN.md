# 15-Minute 1¢ Study

*Updated Sun Oct 25, 11:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2714 finished bets | 1% | $84.05 | +27% | +3.10¢ | $33.05 / $51.00 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2521 | $57.30 | +21% |
| Volatility model ≥ 2%, hold to the close | 5029 | -$13.90 | -2% |
| Momentum model ≥ 2%, hold to the close | 4196 | -$29.85 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32235 | 32227 | 120 (0%) | 1.07% | -$2,234.70 (-57%) | Hold to the close: -$2,234.70 (-57%) |

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
| Volatility model | 20783 | 4.6% | 0.4% (85) | -657% | ❌ Worse |
| Momentum model | 20783 | 4.5% | 0.4% (85) | -682% | ❌ Worse |
| Mean-reversion model | 20783 | 7.9% | 0.4% (85) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20783 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5029 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2714 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1536 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4196 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2521 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1643 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8375 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5867 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3906 | 33 | -5% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20983 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7487 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3757 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32227 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,234.70 | -57% | — |
| Sell at 2¢ | 1199 | 4% | -$3,434.96 | -88% | 47 sec |
| Sell at 3¢ | 822 | 3% | -$3,426.12 | -88% | 48 sec |
| Sell at 5¢ | 572 | 2% | -$3,374.90 | -86% | 61 sec |
| Sell at 10¢ | 354 | 1% | -$3,240.96 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$3,002.49 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,727.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1408 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10327 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8154 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12334 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2351 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2344 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2341 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2337 | 6 | 3% | 1% | -68% | -92% | -92% |
| ETH | 2332 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2324 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2321 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2321 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2312 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1213 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1178 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1157 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1026 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1003 | 4 | 1% | 1% | -63% | -70% | -69% |
| EURUSD | 958 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 953 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 914 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 904 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 888 | 5 | 1% | 1% | -47% | -98% | -97% |
| AUDUSD | 447 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 408 | 0 | 1% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16319 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15908 | 54 | 4% | 1% | -61% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3504 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3609 | 11 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 5421 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6120 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2325 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8935 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,821 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 11:29:45 PM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:29:45 PM | SOL | UP | 15 sec | -0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:29:29 PM | PLATINUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:29 PM | BNB | UP | 31 sec | -0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:14 PM | AUDUSD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:14 PM | NEAR | DOWN | 45 sec | +0.129% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:14 PM | XRP | DOWN | 45 sec | +0.062% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:29:14 PM | BTC | DOWN | 45 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:28:41 PM | BRENT | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:28:41 PM | GBPUSD | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:28:25 PM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:28:09 PM | ZEC | DOWN | 1.9 min | +0.356% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:28:09 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:14:44 PM | GBPUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:14:29 PM | SILVER | DOWN | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:14:29 PM | BTC | DOWN | 30 sec | +0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:14:29 PM | GOLD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:14:12 PM | ZEC | DOWN | 47 sec | +0.176% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:14:12 PM | BNB | DOWN | 47 sec | +0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:13:56 PM | WTI | DOWN | 63 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:13:40 PM | NATGAS | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:13:24 PM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:13:24 PM | NEAR | DOWN | 1.6 min | +0.266% | 2¢ | ❌ Lost | -$0.15 |
| 10/25 11:13:06 PM | XRP | DOWN | 1.9 min | +0.233% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:13:06 PM | ETH | DOWN | 1.9 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:12:50 PM | SOL | DOWN | 2.2 min | +0.202% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:12:50 PM | DOGE | DOWN | 2.2 min | +0.258% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:11:45 PM | COPPER | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:10:39 PM | HYPE | DOWN | 4.3 min | +0.320% | 1¢ | ❌ Lost | $0.00 |
| 10/25 10:59:59 PM | EURUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
