# 15-Minute 1¢ Study

*Updated Wed Oct 21, 7:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2245 finished bets | 1% | $82.50 | +33% | +3.67¢ | $46.20 / $36.30 |

*Expect about **97 buys a day** (~$14.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2078 | $63.30 | +27% |
| Volatility model ≥ 2%, hold to the close | 4107 | -$27.10 | -5% |
| Momentum model ≥ 2%, hold to the close | 3468 | -$30.75 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26613 | 26606 | 97 (0%) | 1.07% | -$1,883.95 (-58%) | Hold to the close: -$1,883.95 (-58%) |

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
| Volatility model | 17244 | 4.6% | 0.4% (69) | -671% | ❌ Worse |
| Momentum model | 17244 | 4.6% | 0.4% (69) | -693% | ❌ Worse |
| Mean-reversion model | 17244 | 7.8% | 0.4% (69) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17244 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4107 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2245 | 24 | +33% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1292 | 16 | +73% | -61% | -60% | -57% |
| Momentum model ≥ 2% | 3468 | 27 | -8% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2078 | 21 | +27% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 1368 | 14 | +39% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 6807 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4751 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3156 | 25 | -10% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17442 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6345 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2819 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26606 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,883.95 | -58% | — |
| Sell at 2¢ | 964 | 4% | -$2,851.31 | -88% | 46 sec |
| Sell at 3¢ | 654 | 2% | -$2,846.89 | -88% | 48 sec |
| Sell at 5¢ | 463 | 2% | -$2,801.00 | -86% | 56 sec |
| Sell at 10¢ | 282 | 1% | -$2,704.53 | -83% | 64 sec |
| Sell at 25¢ | 154 | 1% | -$2,508.21 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,279.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1072 | 6 | 10% | 4% | -47% | -81% | -84% |
| 2–5 min | 8565 | 43 | 7% | 3% | -51% | -87% | -87% |
| 1–2 min | 6802 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10163 | 23 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1957 | 11 | 5% | 2% | -30% | -89% | -90% |
| BNB | 1949 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1948 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1938 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1937 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1936 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1929 | 7 | 3% | 1% | -56% | -88% | -88% |
| NEAR | 1924 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1924 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1039 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 1001 | 4 | 3% | 1% | -54% | -82% | -82% |
| WTI | 979 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 871 | 0 | 1% | 0% | -100% | -99% | -99% |
| COPPER | 867 | 3 | 1% | 1% | -68% | -76% | -75% |
| NATGAS | 801 | 5 | 2% | 1% | -42% | -85% | -84% |
| EURUSD | 797 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 787 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 747 | 1 | 2% | 1% | -88% | -97% | -97% |
| USDJPY | 706 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 307 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 262 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13380 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13226 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2932 | 15 | 2% | 1% | -15% | -78% | -77% |
| 0.05–0.1% | 3032 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4443 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5072 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1960 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6844 | 28 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6273 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,733 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 6:59:51 AM | BNB | DOWN | 8 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:59:51 AM | SOL | DOWN | 8 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:59:35 AM | USDCAD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:59:35 AM | SILVER | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:59:35 AM | HYPE | DOWN | 24 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:59:35 AM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:59:19 AM | GOLD | DOWN | 40 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:58:31 AM | XRP | DOWN | 88 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:58:15 AM | ETH | UP | 1.7 min | -0.125% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:58:15 AM | DOGE | DOWN | 1.7 min | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:57:59 AM | ZEC | DOWN | 2.0 min | +0.312% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:56:37 AM | WTI | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:55:50 AM | BTC | UP | 4.2 min | -0.180% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:55:50 AM | NEAR | UP | 4.2 min | -0.732% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:50 AM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:34 AM | HYPE | DOWN | 26 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:44:34 AM | BTC | UP | 26 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:44:34 AM | BNB | UP | 26 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:44:01 AM | WTI | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:45 AM | XRP | UP | 74 sec | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:29 AM | GOLD | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:13 AM | ZEC | UP | 1.8 min | -0.385% | 2¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:13 AM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:13 AM | SOL | UP | 1.8 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:43:13 AM | DOGE | UP | 1.8 min | -0.172% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:42:41 AM | NEAR | UP | 2.3 min | -0.586% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 6:41:03 AM | PLATINUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:29:16 AM | SOL | DOWN | 43 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 10/21 6:29:16 AM | DOGE | DOWN | 43 sec | +0.063% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 6:28:44 AM | ETH | DOWN | 75 sec | +0.109% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
