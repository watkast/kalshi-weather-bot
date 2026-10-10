# 15-Minute 1¢ Study

*Updated Sat Oct 10, 1:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 998 finished bets | 1% | $30.95 | +28% | +3.10¢ | -$11.10 / $42.05 |

*Expect about **80 buys a day** (~$11.95/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 968 | $7.45 | +7% |
| 5+ min left, hold to the close | 390 | -$1.60 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 998 | -$13.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13923 | 13908 | 56 (0%) | 1.07% | -$898.55 (-53%) | Hold to the close: -$898.55 (-53%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 9063 | 4.2% | 0.4% (39) | -610% | ❌ Worse |
| Momentum model | 9063 | 4.3% | 0.4% (39) | -639% | ❌ Worse |
| Mean-reversion model | 9063 | 6.9% | 0.4% (39) | -710% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9063 | 39 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1778 | 14 | -9% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 998 | 10 | +28% | -69% | -68% | -65% |
| Volatility model ≥ 10% | 623 | 8 | +86% | -55% | -55% | -51% |
| Momentum model ≥ 2% | 1574 | 11 | -16% | -77% | -79% | -76% |
| Momentum model ≥ 5% | 968 | 8 | +7% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 666 | 6 | +28% | -64% | -65% | -61% |
| Mean-reversion model ≥ 2% | 3172 | 23 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2148 | 17 | -13% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1422 | 13 | +5% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9261 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13908 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$898.55 | -53% | — |
| Sell at 2¢ | 471 | 3% | -$1,518.09 | -90% | 33 sec |
| Sell at 3¢ | 314 | 2% | -$1,518.09 | -90% | 47 sec |
| Sell at 5¢ | 229 | 2% | -$1,491.70 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,414.74 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,299.89 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,157.80 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 386 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4500 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3643 | 15 | 3% | 2% | -55% | -94% | -94% |
| Under 1 min | 5375 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1037 | 6 | 4% | 3% | -30% | -90% | -90% |
| HYPE | 1035 | 3 | 4% | 2% | -64% | -90% | -89% |
| BNB | 1034 | 5 | 4% | 2% | -41% | -91% | -92% |
| DOGE | 1033 | 2 | 4% | 2% | -76% | -92% | -91% |
| ETH | 1028 | 8 | 5% | 3% | -4% | -89% | -88% |
| SOL | 1026 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1023 | 6 | 6% | 3% | -23% | -73% | -74% |
| BTC | 1023 | 4 | 5% | 2% | -49% | -88% | -91% |
| XRP | 1022 | 6 | 2% | 1% | -27% | -83% | -83% |
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
| UP (bought YES) | 6997 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6911 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1577 | 9 | 2% | 1% | -4% | -72% | -71% |
| 0.05–0.1% | 1621 | 5 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2365 | 8 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2626 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1069 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3178 | 9 | 3% | 1% | -67% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,267 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 1:43:52 PM | SOL | DOWN | 68 sec | +0.063% | — | In play | — |
| 10/10 1:43:03 PM | ZEC | DOWN | 1.9 min | +0.165% | — | In play | — |
| 10/10 1:42:30 PM | XRP | DOWN | 2.5 min | +0.114% | — | In play | — |
| 10/10 1:41:24 PM | HYPE | DOWN | 3.6 min | +0.169% | — | In play | — |
| 10/10 1:41:24 PM | BNB | DOWN | 3.6 min | +0.063% | — | In play | — |
| 10/10 1:41:08 PM | BTC | DOWN | 3.9 min | +0.060% | — | In play | — |
| 10/10 1:40:53 PM | NEAR | DOWN | 4.1 min | +0.464% | — | In play | — |
| 10/10 1:40:20 PM | ETH | DOWN | 4.7 min | +0.148% | — | In play | — |
| 10/10 1:29:28 PM | XRP | DOWN | 32 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:28:37 PM | ETH | DOWN | 82 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:28:37 PM | DOGE | DOWN | 82 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:28:05 PM | ZEC | DOWN | 1.9 min | +0.176% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:28:05 PM | BTC | DOWN | 1.9 min | +0.021% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:26:43 PM | SOL | DOWN | 3.3 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:25:06 PM | BNB | DOWN | 4.9 min | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:23:46 PM | HYPE | DOWN | 6.2 min | +0.241% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 1:14:51 PM | DOGE | DOWN | 8 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/10 1:14:35 PM | SOL | DOWN | 24 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:14:35 PM | ZEC | UP | 24 sec | -0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/10 1:14:35 PM | XRP | DOWN | 24 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:14:19 PM | BTC | UP | 41 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/10 1:13:30 PM | ETH | DOWN | 89 sec | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 1:12:24 PM | HYPE | UP | 2.6 min | -0.136% | 0¢ | ❌ Lost | $0.00 |
| 10/10 1:11:19 PM | BNB | DOWN | 3.7 min | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/10 1:10:12 PM | NEAR | UP | 4.8 min | -0.573% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:50 PM | SOL | UP | 10 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:50 PM | ZEC | DOWN | 10 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 10/10 12:59:50 PM | BNB | UP | 10 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:50 PM | BTC | DOWN | 10 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 12:59:02 PM | NEAR | DOWN | 57 sec | +0.081% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
