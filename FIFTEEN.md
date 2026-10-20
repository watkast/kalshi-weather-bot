# 15-Minute 1¢ Study

*Updated Mon Oct 19, 11:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2085 finished bets | 1% | $88.45 | +38% | +4.24¢ | $25.85 / $62.60 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1918 | $69.55 | +33% |
| Momentum model ≥ 2%, hold to the close | 3198 | -$10.70 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2085 | -$28.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24620 | 24613 | 90 (0%) | 1.07% | -$1,729.35 (-58%) | Hold to the close: -$1,729.35 (-58%) |

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
| Volatility model | 16149 | 4.6% | 0.4% (64) | -678% | ❌ Worse |
| Momentum model | 16149 | 4.6% | 0.4% (64) | -701% | ❌ Worse |
| Mean-reversion model | 16149 | 7.7% | 0.4% (64) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16149 | 64 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3770 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2085 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1217 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3198 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1918 | 20 | +33% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1274 | 13 | +40% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6294 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4380 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2897 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16347 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5770 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2496 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24613 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,729.35 | -58% | — |
| Sell at 2¢ | 887 | 4% | -$2,646.73 | -89% | 45 sec |
| Sell at 3¢ | 599 | 2% | -$2,643.74 | -88% | 47 sec |
| Sell at 5¢ | 428 | 2% | -$2,599.15 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,508.75 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,320.02 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,095.60 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 946 | 5 | 10% | 3% | -50% | -82% | -84% |
| 2–5 min | 7982 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6283 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9398 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1838 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1827 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1826 | 9 | 5% | 2% | -39% | -82% | -81% |
| ETH | 1816 | 9 | 6% | 3% | -40% | -87% | -87% |
| DOGE | 1816 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1812 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1806 | 7 | 3% | 1% | -52% | -87% | -88% |
| NEAR | 1804 | 9 | 6% | 3% | -36% | -79% | -80% |
| BTC | 1802 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 947 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 916 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 889 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 793 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 783 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 728 | 5 | 2% | 2% | -36% | -84% | -83% |
| EURUSD | 723 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 714 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 678 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 631 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 259 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 205 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12404 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12209 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2779 | 15 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 2844 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4106 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4762 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1853 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6928 | 18 | 3% | 2% | -70% | -92% | -92% |

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
| 10/19 11:29:44 PM | USDJPY | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:29:44 PM | USDCAD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:29:12 PM | EURUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:56 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:56 PM | WTI | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | BTC | UP | 78 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | XRP | UP | 78 sec | -0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | BNB | UP | 78 sec | -0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:41 PM | GBPUSD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:28:25 PM | ETH | UP | 1.6 min | -0.092% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:38 PM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | HYPE | UP | 2.6 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | PLATINUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | DOGE | UP | 2.6 min | -0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:22 PM | ZEC | UP | 2.6 min | -0.589% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:27:06 PM | SOL | UP | 2.9 min | -0.223% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:26:50 PM | NEAR | UP | 3.2 min | -0.552% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:26:50 PM | GOLD | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:26:50 PM | COPPER | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:51 PM | PALLADIUM | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:51 PM | XRP | UP | 8 sec | -0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:14:51 PM | AUDUSD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:51 PM | BNB | UP | 8 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:51 PM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:20 PM | HYPE | UP | 39 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:14:20 PM | BTC | UP | 39 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/19 11:14:20 PM | WTI | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:20 PM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:14:04 PM | SOL | UP | 55 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 11:13:48 PM | ZEC | DOWN | 72 sec | +0.224% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
