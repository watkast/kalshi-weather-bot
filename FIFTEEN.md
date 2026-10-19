# 15-Minute 1¢ Study

*Updated Mon Oct 19, 4:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2053 finished bets | 1% | $91.75 | +40% | +4.47¢ | $27.95 / $63.80 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1891 | $72.25 | +35% |
| Momentum model ≥ 2%, hold to the close | 3154 | -$5.45 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 2053 | -$25.25 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24211 | 24204 | 90 (0%) | 1.07% | -$1,677.90 (-57%) | Hold to the close: -$1,677.90 (-57%) |

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
| Volatility model | 15924 | 4.6% | 0.4% (64) | -673% | ❌ Worse |
| Momentum model | 15924 | 4.6% | 0.4% (64) | -696% | ❌ Worse |
| Mean-reversion model | 15924 | 7.7% | 0.4% (64) | -808% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15924 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3705 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2053 | 23 | +40% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1202 | 15 | +75% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3154 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1891 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1257 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6194 | 41 | -28% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 4305 | 33 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2849 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16122 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5653 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2429 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24204 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,677.90 | -57% | — |
| Sell at 2¢ | 871 | 4% | -$2,599.44 | -88% | 46 sec |
| Sell at 3¢ | 590 | 2% | -$2,595.80 | -88% | 47 sec |
| Sell at 5¢ | 424 | 2% | -$2,550.30 | -87% | 50 sec |
| Sell at 10¢ | 257 | 1% | -$2,461.23 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,275.19 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,044.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 914 | 5 | 10% | 3% | -48% | -82% | -85% |
| 2–5 min | 7870 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6188 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9228 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1812 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1802 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1800 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1792 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1791 | 9 | 6% | 3% | -40% | -87% | -87% |
| SOL | 1787 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1783 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1778 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1777 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 925 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 898 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 871 | 3 | 3% | 1% | -60% | -94% | -95% |
| COPPER | 780 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 769 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 711 | 5 | 2% | 2% | -34% | -83% | -82% |
| EURUSD | 710 | 3 | 2% | 1% | -61% | -83% | -82% |
| PALLADIUM | 699 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 664 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 615 | 3 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 243 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 197 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12195 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 12009 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2743 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2803 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4056 | 13 | 5% | 2% | -60% | -89% | -89% |
| 0.2–0.5% | 4690 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1827 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5733 | 19 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,818 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 4:44:49 PM | BNB | DOWN | 11 sec | -0.059% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:44:33 PM | PALLADIUM | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:44:02 PM | DOGE | UP | 57 sec | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:44:02 PM | NATGAS | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:44:02 PM | HYPE | UP | 57 sec | -0.156% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 4:44:02 PM | USDCAD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:43:46 PM | NEAR | UP | 74 sec | -0.410% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:43:46 PM | WTI | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:43:30 PM | SOL | UP | 1.5 min | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:43:30 PM | XRP | UP | 1.5 min | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:43:30 PM | BTC | UP | 1.5 min | -0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:43:30 PM | ETH | UP | 1.5 min | -0.112% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:42:24 PM | ZEC | UP | 2.6 min | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:42:24 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:40:17 PM | GOLD | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:39:27 PM | SILVER | UP | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:50 PM | SILVER | UP | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:29:50 PM | BTC | UP | 10 sec | -0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:50 PM | ETH | UP | 10 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:29:34 PM | WTI | UP | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:29:18 PM | SOL | UP | 42 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:18 PM | DOGE | UP | 42 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:18 PM | ZEC | UP | 42 sec | -0.203% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:29:03 PM | XRP | UP | 56 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/19 4:29:03 PM | GBPUSD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:27:59 PM | HYPE | DOWN | 2.0 min | +0.171% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:24:29 PM | BNB | UP | 5.5 min | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:54 PM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:07 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:07 PM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
