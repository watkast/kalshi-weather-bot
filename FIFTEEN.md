# 15-Minute 1¢ Study

*Updated Tue Oct 20, 4:49 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2107 finished bets | 1% | $85.60 | +36% | +4.06¢ | $24.50 / $61.10 |

*Expect about **95 buys a day** (~$14.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1937 | $67.15 | +32% |
| Momentum model ≥ 2%, hold to the close | 3230 | -$14.75 | -4% |
| Volatility model ≥ 2%, hold to the close | 3817 | -$31.30 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24958 | 24951 | 92 (0%) | 1.07% | -$1,744.10 (-58%) | Hold to the close: -$1,744.10 (-58%) |

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
| Volatility model | 16332 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16332 | 4.6% | 0.4% (65) | -694% | ❌ Worse |
| Mean-reversion model | 16332 | 7.7% | 0.4% (65) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16332 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3817 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2107 | 23 | +36% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1226 | 15 | +72% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3230 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1937 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1283 | 13 | +39% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6370 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4433 | 34 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2932 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16530 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5872 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2549 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24951 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,744.10 | -58% | — |
| Sell at 2¢ | 899 | 4% | -$2,672.36 | -88% | 46 sec |
| Sell at 3¢ | 610 | 2% | -$2,668.20 | -88% | 47 sec |
| Sell at 5¢ | 434 | 2% | -$2,624.00 | -87% | 51 sec |
| Sell at 10¢ | 264 | 1% | -$2,532.26 | -84% | 64 sec |
| Sell at 25¢ | 145 | 1% | -$2,342.15 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,110.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 967 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8094 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6369 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9517 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1858 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1847 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1847 | 9 | 5% | 2% | -40% | -83% | -82% |
| ETH | 1837 | 9 | 6% | 3% | -41% | -87% | -87% |
| DOGE | 1836 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1833 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1827 | 7 | 3% | 1% | -53% | -87% | -87% |
| NEAR | 1823 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1822 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 964 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 931 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 905 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 808 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 798 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 739 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 735 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 727 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 692 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 642 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 266 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 214 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12605 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12346 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2798 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2873 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4178 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4819 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1859 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6368 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,796 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 4:44:50 AM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:44:34 AM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:44:03 AM | ZEC | UP | 57 sec | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:43:31 AM | COPPER | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:43:14 AM | USDCAD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:57 AM | SOL | UP | 2.0 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | HYPE | UP | 2.3 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | DOGE | UP | 2.3 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | BNB | UP | 2.3 min | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:42:41 AM | BTC | UP | 2.3 min | -0.150% | 1¢ | ❌ Lost | $0.00 |
| 10/20 4:41:38 AM | XRP | UP | 3.4 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:41:22 AM | NEAR | UP | 3.6 min | -0.623% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:41:22 AM | ETH | UP | 3.6 min | -0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:29:44 AM | SILVER | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 4:29:29 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:29:29 AM | NEAR | UP | 31 sec | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:29:29 AM | BNB | DOWN | 31 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:29:29 AM | GBPUSD | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:28:58 AM | ETH | UP | 61 sec | -0.091% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:28:42 AM | ZEC | DOWN | 77 sec | +0.153% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:28:26 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:28:10 AM | GOLD | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:27:53 AM | EURUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:26:31 AM | XRP | UP | 3.5 min | -0.263% | 10¢ | ❌ Lost | -$0.15 |
| 10/20 4:26:15 AM | HYPE | UP | 3.8 min | -0.280% | 6¢ | ❌ Lost | -$0.15 |
| 10/20 4:26:15 AM | DOGE | UP | 3.8 min | -0.161% | 53¢ | ❌ Lost | -$0.15 |
| 10/20 4:25:28 AM | SOL | UP | 4.5 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 4:14:47 AM | USDJPY | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:14:47 AM | COPPER | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 4:14:47 AM | PLATINUM | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
