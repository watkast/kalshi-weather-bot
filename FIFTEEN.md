# 15-Minute 1¢ Study

*Updated Tue Oct 20, 1:25 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2093 finished bets | 1% | $87.40 | +37% | +4.18¢ | $25.25 / $62.15 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1931 | $67.90 | +32% |
| Momentum model ≥ 2%, hold to the close | 3215 | -$12.95 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2093 | -$29.60 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24738 | 24730 | 90 (0%) | 1.07% | -$1,744.80 (-58%) | Hold to the close: -$1,744.80 (-58%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16210 | 4.6% | 0.4% (64) | -678% | ❌ Worse |
| Momentum model | 16210 | 4.6% | 0.4% (64) | -701% | ❌ Worse |
| Mean-reversion model | 16210 | 7.8% | 0.4% (64) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16210 | 64 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3790 | 30 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2093 | 23 | +37% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1220 | 15 | +73% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3215 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1931 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1280 | 13 | +40% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6322 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4400 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2910 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16408 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5806 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2516 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24730 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,744.80 | -58% | — |
| Sell at 2¢ | 891 | 4% | -$2,661.14 | -89% | 45 sec |
| Sell at 3¢ | 602 | 2% | -$2,658.02 | -88% | 47 sec |
| Sell at 5¢ | 428 | 2% | -$2,614.60 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,524.20 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,335.47 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,111.05 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 956 | 5 | 10% | 3% | -50% | -81% | -84% |
| 2–5 min | 8027 | 40 | 7% | 3% | -51% | -88% | -88% |
| 1–2 min | 6311 | 24 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 9432 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1845 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1834 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1833 | 9 | 5% | 2% | -40% | -82% | -82% |
| ETH | 1823 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1823 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1819 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1813 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1809 | 9 | 6% | 3% | -36% | -79% | -79% |
| BTC | 1809 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 952 | 1 | 3% | 1% | -88% | -93% | -94% |
| SILVER | 921 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 896 | 3 | 3% | 1% | -61% | -94% | -96% |
| COPPER | 798 | 2 | 2% | 1% | -77% | -85% | -85% |
| PLATINUM | 788 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 732 | 5 | 2% | 2% | -36% | -84% | -83% |
| EURUSD | 727 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 719 | 2 | 1% | 0% | -74% | -85% | -86% |
| GBPUSD | 683 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 636 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 262 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 208 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12470 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12260 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2784 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2857 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4129 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4779 | 22 | 6% | 3% | -50% | -88% | -88% |
| Over 0.5% | 1856 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6147 | 24 | 4% | 2% | -56% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,814 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 1:25:05 AM | HYPE | UP | 4.9 min | -0.336% | — | In play | — |
| 10/20 1:14:47 AM | ZEC | UP | 13 sec | -0.155% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:14:47 AM | XRP | DOWN | 13 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:14:47 AM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:14:47 AM | ETH | UP | 13 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:14:31 AM | COPPER | UP | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:14:31 AM | HYPE | UP | 29 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:14:31 AM | SOL | UP | 29 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:14:15 AM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:14:15 AM | BTC | UP | 45 sec | -0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:13:59 AM | DOGE | DOWN | 61 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:13:42 AM | SILVER | UP | 77 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 1:13:10 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:13:10 AM | GOLD | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:12:38 AM | PLATINUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:11:16 AM | BNB | DOWN | 3.7 min | +0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 1:11:16 AM | PALLADIUM | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 1:10:10 AM | WTI | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:59:53 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:59:38 AM | NEAR | UP | 21 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:59:22 AM | NATGAS | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:59:22 AM | HYPE | UP | 37 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:58:50 AM | GOLD | DOWN | 69 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:58:50 AM | PALLADIUM | DOWN | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:58:34 AM | GBPUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:58:34 AM | BTC | UP | 85 sec | -0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:58:18 AM | ZEC | UP | 1.7 min | -0.295% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:58:02 AM | BNB | UP | 1.9 min | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:57:31 AM | SOL | UP | 2.5 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:56:59 AM | SILVER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
