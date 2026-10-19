# 15-Minute 1¢ Study

*Updated Mon Oct 19, 3:05 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2045 finished bets | 1% | $92.50 | +40% | +4.52¢ | $28.55 / $63.95 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1884 | $72.85 | +35% |
| Momentum model ≥ 2%, hold to the close | 3140 | -$3.80 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 2045 | -$24.50 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24129 | 24122 | 90 (0%) | 1.07% | -$1,668.00 (-57%) | Hold to the close: -$1,668.00 (-57%) |

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
| Volatility model | 15863 | 4.6% | 0.4% (64) | -667% | ❌ Worse |
| Momentum model | 15863 | 4.6% | 0.4% (64) | -691% | ❌ Worse |
| Mean-reversion model | 15863 | 7.7% | 0.4% (64) | -801% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15863 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3695 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2045 | 23 | +40% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1198 | 15 | +75% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3140 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1884 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1253 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6170 | 41 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4289 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2839 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16061 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5641 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2420 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24122 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,668.00 | -57% | — |
| Sell at 2¢ | 866 | 4% | -$2,590.84 | -88% | 46 sec |
| Sell at 3¢ | 586 | 2% | -$2,587.46 | -88% | 47 sec |
| Sell at 5¢ | 420 | 2% | -$2,543.00 | -87% | 50 sec |
| Sell at 10¢ | 255 | 1% | -$2,453.95 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,265.29 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,034.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 904 | 5 | 10% | 3% | -47% | -82% | -85% |
| 2–5 min | 7848 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6176 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9190 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1805 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1795 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1793 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1786 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1784 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1780 | 2 | 3% | 2% | -86% | -93% | -92% |
| XRP | 1776 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1772 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1770 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 924 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 896 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 867 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 780 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 768 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 708 | 5 | 2% | 2% | -34% | -83% | -82% |
| EURUSD | 708 | 3 | 2% | 1% | -60% | -83% | -82% |
| PALLADIUM | 698 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 659 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 614 | 3 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 243 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 196 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12151 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11971 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2735 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2788 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4037 | 13 | 5% | 2% | -60% | -90% | -89% |
| 0.2–0.5% | 4677 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1821 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5651 | 19 | 3% | 1% | -60% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 2:59:52 PM | BNB | DOWN | 8 sec | -0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:52 PM | EURUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:52 PM | DOGE | UP | 8 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:59:52 PM | PLATINUM | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:52 PM | NEAR | DOWN | 8 sec | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:52 PM | BTC | UP | 8 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:59:52 PM | HYPE | DOWN | 8 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:59:36 PM | COPPER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:20 PM | SOL | UP | 40 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:59:05 PM | ETH | UP | 54 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:58:33 PM | WTI | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:58:33 PM | XRP | UP | 86 sec | -0.092% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 2:58:01 PM | GOLD | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:58:01 PM | SILVER | DOWN | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:52:35 PM | ZEC | UP | 7.4 min | -0.788% | 3¢ | ❌ Lost | -$0.15 |
| 10/19 2:44:39 PM | SOL | DOWN | 21 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:43:52 PM | ETH | DOWN | 67 sec | +0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:43:52 PM | HYPE | DOWN | 67 sec | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:43:52 PM | BNB | UP | 67 sec | -0.056% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:43:52 PM | DOGE | UP | 67 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:43:36 PM | ZEC | UP | 83 sec | -0.257% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:43:36 PM | XRP | UP | 83 sec | -0.123% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:40:41 PM | NEAR | UP | 4.3 min | -0.592% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:55 PM | ZEC | DOWN | 5 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:29:55 PM | XRP | UP | 5 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:29:55 PM | SOL | DOWN | 5 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:29:39 PM | NEAR | DOWN | 21 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:39 PM | ETH | DOWN | 21 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/19 2:29:39 PM | GOLD | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 2:29:39 PM | BTC | DOWN | 21 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
