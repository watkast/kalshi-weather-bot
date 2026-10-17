# 15-Minute 1¢ Study

*Updated Sat Oct 17, 1:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1795 finished bets | 1% | $80.65 | +40% | +4.49¢ | $42.20 / $38.45 |

*Expect about **92 buys a day** (~$13.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1649 | $44.60 | +25% |
| Momentum model ≥ 2%, hold to the close | 2771 | -$13.90 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1795 | -$29.10 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22051 | 22044 | 84 (0%) | 1.07% | -$1,502.40 (-56%) | Hold to the close: -$1,502.40 (-56%) |

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
| Volatility model | 14320 | 4.5% | 0.4% (58) | -648% | ❌ Worse |
| Momentum model | 14320 | 4.5% | 0.4% (58) | -669% | ❌ Worse |
| Mean-reversion model | 14320 | 7.5% | 0.4% (58) | -780% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14320 | 58 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3251 | 26 | -8% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1795 | 20 | +40% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1051 | 12 | +62% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2771 | 22 | -4% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1649 | 16 | +25% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1095 | 11 | +40% | -74% | -73% | -68% |
| Mean-reversion model ≥ 2% | 5477 | 37 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3788 | 29 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2503 | 18 | -18% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14518 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22044 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 84 | 0% | -$1,502.40 | -56% | — |
| Sell at 2¢ | 797 | 4% | -$2,373.18 | -89% | 37 sec |
| Sell at 3¢ | 537 | 2% | -$2,370.97 | -89% | 47 sec |
| Sell at 5¢ | 387 | 2% | -$2,328.85 | -87% | 50 sec |
| Sell at 10¢ | 234 | 1% | -$2,245.86 | -84% | 63 sec |
| Sell at 25¢ | 132 | 1% | -$2,073.48 | -77% | 80 sec |
| Sell at 50¢ | 87 | 0% | -$1,853.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 772 | 5 | 10% | 3% | -39% | -82% | -85% |
| 2–5 min | 7141 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5712 | 22 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 8415 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1632 | 11 | 4% | 2% | -16% | -90% | -90% |
| HYPE | 1624 | 6 | 4% | 2% | -55% | -90% | -88% |
| ETH | 1617 | 8 | 6% | 3% | -40% | -87% | -86% |
| BNB | 1617 | 7 | 5% | 2% | -47% | -89% | -89% |
| DOGE | 1615 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1610 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1603 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1601 | 9 | 6% | 3% | -27% | -78% | -78% |
| BTC | 1599 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11124 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10920 | 43 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2474 | 13 | 2% | 1% | -12% | -81% | -81% |
| 0.05–0.1% | 2516 | 7 | 3% | 1% | -60% | -92% | -91% |
| 0.1–0.2% | 3650 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4214 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1661 | 6 | 6% | 3% | -63% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5140 | 18 | 3% | 1% | -58% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,596 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 12:59:39 PM | BNB | UP | 20 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:39 PM | HYPE | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:59:23 PM | SOL | UP | 36 sec | -0.029% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:23 PM | BTC | UP | 36 sec | -0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:59:23 PM | ETH | UP | 36 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:58:51 PM | BNB | DOWN | 68 sec | -0.008% | 99¢ | ✅ Won | $13.85 |
| 10/17 12:58:35 PM | NEAR | DOWN | 84 sec | +0.190% | 91¢ | ✅ Won | $13.85 |
| 10/17 12:58:19 PM | ZEC | DOWN | 1.7 min | +0.352% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:57:41 PM | DOGE | DOWN | 2.3 min | +0.131% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:57:41 PM | XRP | DOWN | 2.3 min | +0.069% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:44:51 PM | BNB | DOWN | 8 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:51 PM | BTC | UP | 8 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:19 PM | ETH | UP | 40 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:45 PM | DOGE | DOWN | 75 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:45 PM | XRP | DOWN | 75 sec | +0.039% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:58 PM | SOL | DOWN | 2.0 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:58 PM | NEAR | DOWN | 2.0 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:25 PM | ZEC | DOWN | 2.6 min | +0.368% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:29:47 PM | BNB | DOWN | 12 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:59 PM | NEAR | DOWN | 61 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:59 PM | BTC | DOWN | 61 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:28:27 PM | XRP | DOWN | 1.6 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | ZEC | DOWN | 3.3 min | +0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | DOGE | DOWN | 3.3 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | SOL | DOWN | 3.3 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | ETH | DOWN | 3.3 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | HYPE | DOWN | 3.3 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:01 PM | HYPE | DOWN | 2.0 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:12 PM | SOL | DOWN | 2.8 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:12 PM | XRP | DOWN | 2.8 min | +0.209% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
