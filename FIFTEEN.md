# 15-Minute 1¢ Study

*Updated Fri Oct 30, 9:23 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3169 finished bets | 1% | $93.55 | +26% | +2.95¢ | $76.05 / $17.50 |

*Expect about **98 buys a day** (~$14.69/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2936 | $43.00 | +13% |
| Volatility model ≥ 2%, hold to the close | 5874 | $1.80 | +0% |
| Volatility model ≥ 5%, sell at 50¢ | 3169 | -$67.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 39576 | 39566 | 145 (0%) | 1.07% | -$2,804.20 (-58%) | Hold to the close: -$2,804.20 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 24214 | 4.6% | 0.4% (94) | -680% | ❌ Worse |
| Momentum model | 24214 | 4.5% | 0.4% (94) | -703% | ❌ Worse |
| Mean-reversion model | 24214 | 8.0% | 0.4% (94) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 24214 | 94 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5874 | 51 | +0% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3169 | 32 | +26% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1788 | 19 | +52% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 4845 | 35 | -13% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 2936 | 26 | +13% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 1910 | 17 | +23% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9940 | 65 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 6958 | 55 | -13% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 4635 | 39 | -4% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 24415 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9573 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5578 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 39566 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 145 | 0% | -$2,804.20 | -58% | — |
| Sell at 2¢ | 1522 | 4% | -$4,242.48 | -88% | 47 sec |
| Sell at 3¢ | 1048 | 3% | -$4,229.48 | -87% | 49 sec |
| Sell at 5¢ | 730 | 2% | -$4,149.70 | -86% | 63 sec |
| Sell at 10¢ | 441 | 1% | -$3,976.49 | -82% | 65 sec |
| Sell at 25¢ | 229 | 1% | -$3,684.21 | -76% | 83 sec |
| Sell at 50¢ | 148 | 0% | -$3,359.20 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 9 | 0 | 33% | 22% | -100% | -42% | -13% |
| 5–10 min | 1844 | 8 | 11% | 4% | -59% | -80% | -81% |
| 2–5 min | 12624 | 69 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 10014 | 35 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 15075 | 33 | 1% | 0% | -69% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2732 | 13 | 5% | 3% | -39% | -88% | -88% |
| HYPE | 2727 | 8 | 5% | 3% | -64% | -89% | -87% |
| BNB | 2724 | 15 | 5% | 2% | -31% | -85% | -83% |
| SOL | 2720 | 7 | 4% | 2% | -68% | -91% | -91% |
| ETH | 2713 | 11 | 6% | 3% | -51% | -86% | -85% |
| DOGE | 2713 | 6 | 4% | 2% | -72% | -90% | -89% |
| BTC | 2696 | 13 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 2695 | 12 | 5% | 2% | -42% | -83% | -83% |
| XRP | 2695 | 11 | 3% | 1% | -50% | -89% | -89% |
| GOLD | 1499 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1465 | 7 | 4% | 2% | -43% | -82% | -81% |
| WTI | 1445 | 4 | 3% | 1% | -67% | -92% | -93% |
| PLATINUM | 1302 | 3 | 2% | 1% | -78% | -96% | -96% |
| COPPER | 1240 | 5 | 1% | 1% | -62% | -75% | -75% |
| EURUSD | 1237 | 3 | 2% | 1% | -77% | -88% | -88% |
| NATGAS | 1195 | 7 | 2% | 1% | -45% | -81% | -80% |
| GBPUSD | 1173 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1165 | 2 | 1% | 0% | -84% | -90% | -90% |
| USDJPY | 1158 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 697 | 4 | 2% | 1% | -46% | -84% | -83% |
| USDCAD | 670 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 262 | 0 | 1% | 0% | -100% | -99% | -98% |
| 10YRRATE | 173 | 0 | 4% | 1% | -100% | -93% | -91% |
| 30YRRATE | 167 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 159 | 1 | 4% | 1% | -41% | -34% | -33% |
| 5YRRATE | 144 | 1 | 6% | 3% | -35% | -89% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20104 | 80 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 19462 | 65 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3903 | 19 | 2% | 1% | -16% | -81% | -81% |
| 0.05–0.1% | 4140 | 14 | 3% | 2% | -49% | -92% | -92% |
| 0.1–0.2% | 6271 | 22 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 7283 | 31 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2814 | 10 | 7% | 3% | -63% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9916 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 9892 | 44 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 9178 | 31 | 4% | 2% | -60% | -88% | -88% |
| Evening (6pm–12am) | 10580 | 34 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,460 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/30 9:14:05 AM | PLATINUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:13:04 AM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | GOLD | UP | 2.2 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/30 9:12:48 AM | ZEC | DOWN | 2.2 min | +0.735% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | NATGAS | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | HYPE | DOWN | 2.2 min | +0.523% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:48 AM | NEAR | DOWN | 2.2 min | +0.736% | 0¢ | ❌ Lost | $0.00 |
| 10/30 9:12:16 AM | SILVER | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:12:16 AM | PALLADIUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:11:26 AM | AUDUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:10:23 AM | GBPUSD | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:10:07 AM | COPPER | UP | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:49 AM | USDCAD | DOWN | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:49 AM | ETH | DOWN | 5.2 min | +0.705% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:49 AM | SOL | DOWN | 5.2 min | +0.833% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:33 AM | DOGE | DOWN | 5.5 min | +0.755% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:17 AM | BTC | DOWN | 5.7 min | +0.499% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:09:02 AM | XRP | DOWN | 6.0 min | +0.797% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 9:07:41 AM | EURUSD | UP | 7.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 9:07:25 AM | BNB | DOWN | 7.6 min | +0.673% | 1¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:47 AM | 2YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:47 AM | 5YRRATE | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:31 AM | XRP | DOWN | 29 sec | +0.065% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:31 AM | ZEC | DOWN | 29 sec | +0.162% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:31 AM | NATGAS | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:31 AM | COPPER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:16 AM | 10YRRATE | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:16 AM | DOGE | DOWN | 44 sec | +0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/30 8:59:16 AM | NEAR | DOWN | 44 sec | +0.187% | 0¢ | ❌ Lost | -$0.15 |
| 10/30 8:59:00 AM | 30YRRATE | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
