# 15-Minute 1¢ Study

*Updated Sat Oct 10, 2:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1003 finished bets | 1% | $30.65 | +28% | +3.06¢ | -$11.10 / $41.75 |

*Expect about **80 buys a day** (~$11.95/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 971 | $7.30 | +7% |
| 5+ min left, hold to the close | 390 | -$1.60 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1003 | -$13.85 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13960 | 13953 | 56 (0%) | 1.07% | -$903.50 (-54%) | Hold to the close: -$903.50 (-54%) |

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
| Volatility model | 9108 | 4.3% | 0.4% (39) | -616% | ❌ Worse |
| Momentum model | 9108 | 4.3% | 0.4% (39) | -645% | ❌ Worse |
| Mean-reversion model | 9108 | 6.9% | 0.4% (39) | -717% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9108 | 39 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1787 | 14 | -9% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1003 | 10 | +28% | -69% | -68% | -65% |
| Volatility model ≥ 10% | 626 | 8 | +85% | -55% | -56% | -51% |
| Momentum model ≥ 2% | 1580 | 11 | -16% | -77% | -79% | -76% |
| Momentum model ≥ 5% | 971 | 8 | +7% | -72% | -73% | -70% |
| Momentum model ≥ 10% | 669 | 6 | +27% | -64% | -65% | -61% |
| Mean-reversion model ≥ 2% | 3184 | 23 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2160 | 17 | -13% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1431 | 13 | +5% | -81% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9306 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13953 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$903.50 | -54% | — |
| Sell at 2¢ | 474 | 3% | -$1,522.26 | -90% | 33 sec |
| Sell at 3¢ | 315 | 2% | -$1,522.65 | -90% | 47 sec |
| Sell at 5¢ | 230 | 2% | -$1,496.00 | -89% | 50 sec |
| Sell at 10¢ | 151 | 1% | -$1,419.69 | -84% | 64 sec |
| Sell at 25¢ | 86 | 1% | -$1,304.84 | -77% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,162.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 386 | 4 | 11% | 3% | -2% | -81% | -86% |
| 2–5 min | 4519 | 28 | 6% | 3% | -39% | -89% | -89% |
| 1–2 min | 3656 | 15 | 3% | 2% | -55% | -94% | -93% |
| Under 1 min | 5388 | 9 | 1% | 0% | -75% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1042 | 6 | 5% | 3% | -30% | -90% | -90% |
| HYPE | 1040 | 3 | 4% | 2% | -64% | -90% | -89% |
| BNB | 1039 | 5 | 4% | 2% | -42% | -91% | -92% |
| DOGE | 1038 | 2 | 4% | 2% | -76% | -92% | -91% |
| ETH | 1033 | 8 | 5% | 3% | -5% | -89% | -88% |
| SOL | 1031 | 1 | 3% | 1% | -88% | -94% | -93% |
| NEAR | 1028 | 6 | 6% | 3% | -24% | -74% | -75% |
| BTC | 1028 | 4 | 5% | 2% | -49% | -88% | -91% |
| XRP | 1027 | 6 | 2% | 1% | -27% | -83% | -83% |
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
| UP (bought YES) | 7019 | 29 | 3% | 2% | -52% | -89% | -89% |
| DOWN (bought NO) | 6934 | 27 | 3% | 1% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1588 | 9 | 2% | 1% | -4% | -72% | -72% |
| 0.05–0.1% | 1633 | 5 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2379 | 8 | 4% | 2% | -58% | -91% | -92% |
| 0.2–0.5% | 2633 | 14 | 5% | 3% | -42% | -89% | -88% |
| Over 0.5% | 1070 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3223 | 9 | 3% | 1% | -67% | -90% | -90% |
| Evening (6pm–12am) | 3780 | 10 | 3% | 1% | -70% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,280 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 2:44:58 PM | BNB | DOWN | 1 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:43:54 PM | BTC | DOWN | 66 sec | +0.026% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:43:38 PM | ETH | DOWN | 82 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:42:17 PM | XRP | DOWN | 2.7 min | +0.135% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:42:17 PM | SOL | DOWN | 2.7 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:42:01 PM | HYPE | DOWN | 3.0 min | +0.282% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 2:41:28 PM | ZEC | DOWN | 3.5 min | +0.219% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:41:28 PM | DOGE | DOWN | 3.5 min | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:40:56 PM | NEAR | DOWN | 4.1 min | +0.590% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:29:56 PM | BNB | DOWN | 4 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:29:40 PM | BTC | UP | 20 sec | -0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:29:09 PM | SOL | UP | 50 sec | -0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:29:09 PM | DOGE | UP | 50 sec | -0.117% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:28:51 PM | XRP | DOWN | 69 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:28:19 PM | HYPE | UP | 1.7 min | -0.130% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 2:27:32 PM | NEAR | DOWN | 2.5 min | +0.347% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:26:11 PM | ZEC | UP | 3.8 min | -0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:25:38 PM | ETH | UP | 4.4 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:14:32 PM | SOL | UP | 27 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:14:32 PM | HYPE | UP | 27 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:14:32 PM | XRP | UP | 27 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:14:12 PM | DOGE | UP | 47 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/10 2:14:12 PM | NEAR | DOWN | 47 sec | +0.124% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 2:13:56 PM | BNB | UP | 63 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 2:13:40 PM | ZEC | UP | 79 sec | -0.069% | 8¢ | ❌ Lost | -$0.15 |
| 10/10 2:13:24 PM | BTC | UP | 1.6 min | -0.046% | 2¢ | ❌ Lost | -$0.15 |
| 10/10 2:12:49 PM | ETH | UP | 2.2 min | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:59:42 PM | BTC | DOWN | 18 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:59:42 PM | BNB | UP | 18 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 1:58:51 PM | SOL | UP | 69 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
