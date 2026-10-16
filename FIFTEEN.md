# 15-Minute 1¢ Study

*Updated Fri Oct 16, 4:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1663 finished bets | 1% | $81.20 | +44% | +4.88¢ | $35.85 / $45.35 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1529 | $44.40 | +27% |
| Momentum model ≥ 2%, hold to the close | 2598 | -$7.05 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1663 | -$21.30 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21302 | 21295 | 80 (0%) | 1.07% | -$1,474.40 (-57%) | Hold to the close: -$1,474.40 (-57%) |

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
| Volatility model | 13589 | 4.4% | 0.4% (54) | -637% | ❌ Worse |
| Momentum model | 13589 | 4.4% | 0.4% (54) | -659% | ❌ Worse |
| Mean-reversion model | 13589 | 7.4% | 0.4% (54) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13589 | 54 | -50% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3050 | 24 | -9% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1663 | 19 | +44% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 960 | 11 | +64% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2598 | 21 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1529 | 15 | +27% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1019 | 10 | +38% | -72% | -72% | -66% |
| Mean-reversion model ≥ 2% | 5152 | 34 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3553 | 27 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2330 | 16 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13787 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5291 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21295 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,474.40 | -57% | — |
| Sell at 2¢ | 761 | 4% | -$2,298.54 | -89% | 37 sec |
| Sell at 3¢ | 512 | 2% | -$2,296.72 | -89% | 47 sec |
| Sell at 5¢ | 370 | 2% | -$2,255.90 | -87% | 50 sec |
| Sell at 10¢ | 222 | 1% | -$2,177.58 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,009.34 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,796.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 725 | 5 | 10% | 3% | -34% | -82% | -85% |
| 2–5 min | 6900 | 37 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5545 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8121 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1548 | 11 | 5% | 3% | -12% | -89% | -90% |
| HYPE | 1543 | 5 | 4% | 2% | -60% | -90% | -88% |
| ETH | 1537 | 8 | 6% | 3% | -37% | -88% | -87% |
| BNB | 1534 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1533 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1531 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1522 | 7 | 2% | 1% | -43% | -86% | -87% |
| BTC | 1521 | 7 | 5% | 2% | -39% | -88% | -91% |
| NEAR | 1518 | 8 | 6% | 3% | -31% | -77% | -77% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 807 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 663 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10746 | 40 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10549 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2261 | 11 | 2% | 1% | -18% | -79% | -79% |
| 0.05–0.1% | 2355 | 7 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 3479 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4073 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1616 | 6 | 6% | 3% | -62% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5030 | 16 | 3% | 1% | -62% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,430 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 3:59:50 PM | WTI | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:59:50 PM | BTC | UP | 9 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:59:34 PM | ETH | UP | 25 sec | -0.014% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:59:18 PM | SOL | UP | 41 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:59:03 PM | HYPE | UP | 56 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:59:03 PM | XRP | UP | 56 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:31 PM | NEAR | UP | 88 sec | -0.383% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:57:09 PM | BNB | UP | 2.9 min | -0.148% | 7¢ | ❌ Lost | -$0.15 |
| 10/16 3:56:54 PM | DOGE | UP | 3.1 min | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:55:49 PM | ZEC | UP | 4.2 min | -0.596% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:33 PM | SOL | UP | 27 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:33 PM | XRP | UP | 27 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:44:33 PM | NEAR | DOWN | 27 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:44:33 PM | BTC | UP | 27 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:44:00 PM | ZEC | DOWN | 59 sec | +0.240% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:43:28 PM | ETH | UP | 1.5 min | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:43:12 PM | BNB | UP | 1.8 min | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:42:56 PM | DOGE | UP | 2.1 min | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:41:50 PM | HYPE | UP | 3.2 min | -0.163% | 3¢ | ❌ Lost | $0.00 |
| 10/16 3:29:52 PM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:29:52 PM | ZEC | DOWN | 7 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:29:36 PM | BTC | DOWN | 23 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:29:04 PM | SOL | DOWN | 55 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:28:48 PM | ETH | DOWN | 71 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:28:48 PM | NATGAS | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:26:22 PM | NEAR | DOWN | 3.6 min | +0.601% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:26:22 PM | BNB | DOWN | 3.6 min | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:25:50 PM | HYPE | DOWN | 4.2 min | +0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:25:34 PM | XRP | DOWN | 4.4 min | +0.353% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:25:34 PM | DOGE | DOWN | 4.4 min | +0.354% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
