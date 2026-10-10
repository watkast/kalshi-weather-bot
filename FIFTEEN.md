# 15-Minute 1¢ Study

*Updated Sat Oct 10, 12:57 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 925 finished bets | 1% | $39.35 | +39% | +4.25¢ | -$6.90 / $46.25 |

*Expect about **77 buys a day** (~$11.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 903 | $15.25 | +16% |
| 5+ min left, hold to the close | 386 | -$1.00 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 925 | -$5.15 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13543 | 13531 | 54 (0%) | 1.07% | -$884.40 (-54%) | Hold to the close: -$884.40 (-54%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 8686 | 4.1% | 0.4% (37) | -583% | ❌ Worse |
| Momentum model | 8686 | 4.1% | 0.4% (37) | -618% | ❌ Worse |
| Mean-reversion model | 8686 | 6.8% | 0.4% (37) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8686 | 37 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1678 | 14 | -3% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 925 | 10 | +39% | -68% | -67% | -64% |
| Volatility model ≥ 10% | 572 | 8 | +104% | -54% | -54% | -50% |
| Momentum model ≥ 2% | 1486 | 11 | -11% | -77% | -78% | -76% |
| Momentum model ≥ 5% | 903 | 8 | +16% | -71% | -73% | -70% |
| Momentum model ≥ 10% | 617 | 6 | +40% | -62% | -64% | -61% |
| Mean-reversion model ≥ 2% | 3032 | 22 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2043 | 17 | -8% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1344 | 13 | +11% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8884 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13531 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 54 | 0% | -$884.40 | -54% | — |
| Sell at 2¢ | 455 | 3% | -$1,480.10 | -90% | 33 sec |
| Sell at 3¢ | 306 | 2% | -$1,479.06 | -90% | 47 sec |
| Sell at 5¢ | 223 | 2% | -$1,453.45 | -89% | 50 sec |
| Sell at 10¢ | 146 | 1% | -$1,379.14 | -84% | 64 sec |
| Sell at 25¢ | 83 | 1% | -$1,267.67 | -77% | 82 sec |
| Sell at 50¢ | 55 | 0% | -$1,129.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 382 | 4 | 10% | 3% | -1% | -82% | -85% |
| 2–5 min | 4370 | 28 | 6% | 3% | -37% | -88% | -89% |
| 1–2 min | 3540 | 13 | 3% | 2% | -60% | -94% | -94% |
| Under 1 min | 5235 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 994 | 6 | 4% | 3% | -27% | -90% | -90% |
| DOGE | 992 | 2 | 3% | 2% | -74% | -92% | -91% |
| HYPE | 992 | 3 | 4% | 2% | -62% | -90% | -88% |
| BNB | 992 | 5 | 4% | 2% | -39% | -90% | -92% |
| ETH | 986 | 7 | 5% | 2% | -13% | -89% | -89% |
| NEAR | 983 | 5 | 5% | 2% | -33% | -73% | -74% |
| SOL | 983 | 1 | 3% | 1% | -87% | -94% | -93% |
| BTC | 981 | 4 | 5% | 2% | -46% | -88% | -90% |
| XRP | 981 | 6 | 2% | 1% | -24% | -83% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6808 | 28 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6723 | 26 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1462 | 8 | 2% | 1% | -6% | -71% | -70% |
| 0.05–0.1% | 1524 | 5 | 3% | 1% | -52% | -92% | -92% |
| 0.1–0.2% | 2269 | 8 | 4% | 2% | -56% | -92% | -92% |
| 0.2–0.5% | 2568 | 13 | 5% | 3% | -44% | -89% | -88% |
| Over 0.5% | 1058 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3370 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3143 | 9 | 3% | 1% | -66% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,113 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 12:56:13 AM | DOGE | UP | 3.8 min | -0.226% | — | In play | — |
| 10/10 12:55:57 AM | ETH | UP | 4.0 min | -0.114% | — | In play | — |
| 10/10 12:55:41 AM | HYPE | UP | 4.3 min | -0.221% | — | In play | — |
| 10/10 12:55:25 AM | BNB | UP | 4.6 min | -0.204% | — | In play | — |
| 10/10 12:55:25 AM | XRP | UP | 4.6 min | -0.255% | — | In play | — |
| 10/10 12:44:15 AM | ZEC | DOWN | 45 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:44:15 AM | BTC | DOWN | 45 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:43:44 AM | ETH | DOWN | 75 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:43:28 AM | SOL | DOWN | 1.5 min | +0.099% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:43:12 AM | XRP | DOWN | 1.8 min | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:43:12 AM | BNB | DOWN | 1.8 min | +0.028% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:42:42 AM | NEAR | DOWN | 2.3 min | +0.764% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:41:40 AM | DOGE | DOWN | 3.3 min | +0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:41:24 AM | HYPE | DOWN | 3.6 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:29:44 AM | ZEC | DOWN | 15 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:29:44 AM | HYPE | UP | 15 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:29:28 AM | ETH | DOWN | 31 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:29:28 AM | BTC | DOWN | 31 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:29:12 AM | SOL | UP | 47 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:28:56 AM | XRP | DOWN | 64 sec | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:28:56 AM | NEAR | UP | 64 sec | -0.422% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:28:56 AM | DOGE | UP | 64 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:26:57 AM | BNB | UP | 3.0 min | -0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:14:32 AM | NEAR | DOWN | 27 sec | +0.164% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:14:16 AM | ZEC | UP | 43 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:13:30 AM | ETH | UP | 1.5 min | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:12:43 AM | BTC | UP | 2.3 min | -0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:12:13 AM | SOL | UP | 2.8 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:12:13 AM | XRP | UP | 2.8 min | -0.241% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:11:44 AM | DOGE | UP | 3.2 min | -0.265% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
