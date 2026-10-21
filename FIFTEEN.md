# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2179 finished bets | 1% | $75.85 | +31% | +3.48¢ | $21.20 / $54.65 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2014 | $56.80 | +25% |
| Momentum model ≥ 2%, hold to the close | 3364 | -$32.30 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2179 | -$41.15 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25838 | 25831 | 94 (0%) | 1.07% | -$1,831.00 (-58%) | Hold to the close: -$1,831.00 (-58%) |

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
| Volatility model | 16818 | 4.6% | 0.4% (66) | -671% | ❌ Worse |
| Momentum model | 16818 | 4.5% | 0.4% (66) | -692% | ❌ Worse |
| Mean-reversion model | 16818 | 7.8% | 0.4% (66) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16818 | 66 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3987 | 31 | -11% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2179 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1250 | 15 | +68% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3364 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2014 | 20 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1326 | 13 | +34% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6612 | 42 | -31% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4605 | 34 | -19% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3048 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17016 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6118 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2697 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25831 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 94 | 0% | -$1,831.00 | -58% | — |
| Sell at 2¢ | 942 | 4% | -$2,762.08 | -88% | 46 sec |
| Sell at 3¢ | 642 | 2% | -$2,756.62 | -88% | 48 sec |
| Sell at 5¢ | 454 | 2% | -$2,711.90 | -86% | 51 sec |
| Sell at 10¢ | 276 | 1% | -$2,617.44 | -83% | 64 sec |
| Sell at 25¢ | 148 | 1% | -$2,433.12 | -77% | 80 sec |
| Sell at 50¢ | 96 | 0% | -$2,205.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1041 | 5 | 10% | 4% | -54% | -81% | -84% |
| 2–5 min | 8348 | 41 | 7% | 3% | -52% | -88% | -87% |
| 1–2 min | 6582 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9856 | 23 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1912 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1902 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1901 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1890 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1890 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1888 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1881 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1877 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1875 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 1006 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 965 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 942 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 837 | 3 | 2% | 1% | -67% | -75% | -75% |
| PLATINUM | 835 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 773 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 767 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 760 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 725 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 677 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 289 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 239 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12985 | 47 | 4% | 2% | -58% | -87% | -86% |
| DOWN (bought NO) | 12846 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2851 | 15 | 2% | 1% | -12% | -77% | -77% |
| 0.05–0.1% | 2951 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4310 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4974 | 24 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 1927 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7011 | 20 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,782 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:44:56 PM | GOLD | UP | 4 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/20 6:44:56 PM | GBPUSD | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:41 PM | SOL | UP | 19 sec | -0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:41 PM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:44:41 PM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:41 PM | PALLADIUM | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:25 PM | ZEC | DOWN | 35 sec | +0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:25 PM | SILVER | UP | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:09 PM | EURUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:44:09 PM | AUDUSD | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:53 PM | XRP | UP | 67 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:53 PM | ETH | UP | 67 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:43:53 PM | HYPE | DOWN | 67 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:43:21 PM | DOGE | DOWN | 1.6 min | +0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:43:21 PM | BTC | UP | 1.6 min | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:43:21 PM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:42:43 PM | NATGAS | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:41:40 PM | BNB | DOWN | 3.3 min | +0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:49 PM | BNB | DOWN | 10 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:29:49 PM | USDCAD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:33 PM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:01 PM | SILVER | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:46 PM | USDJPY | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | PLATINUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | HYPE | DOWN | 1.5 min | +0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | SOL | DOWN | 1.5 min | +0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:14 PM | DOGE | DOWN | 1.8 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:58 PM | XRP | DOWN | 2.0 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:27 PM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:11 PM | WTI | DOWN | 2.8 min | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
