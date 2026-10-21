# 15-Minute 1¢ Study

*Updated Wed Oct 21, 4:44 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2224 finished bets | 1% | $84.90 | +34% | +3.82¢ | $47.25 / $37.65 |

*Expect about **96 buys a day** (~$14.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2059 | $65.55 | +29% |
| Volatility model ≥ 2%, hold to the close | 4077 | -$23.35 | -5% |
| Momentum model ≥ 2%, hold to the close | 3441 | -$27.45 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26466 | 26443 | 97 (0%) | 1.07% | -$1,863.70 (-58%) | Hold to the close: -$1,863.70 (-58%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 17160 | 4.6% | 0.4% (69) | -665% | ❌ Worse |
| Momentum model | 17160 | 4.5% | 0.4% (69) | -687% | ❌ Worse |
| Mean-reversion model | 17160 | 7.8% | 0.4% (69) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17160 | 69 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4077 | 34 | -5% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2224 | 24 | +34% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1277 | 16 | +75% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 3441 | 27 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2059 | 21 | +29% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1354 | 14 | +41% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6767 | 45 | -28% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4719 | 37 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3129 | 25 | -9% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17358 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6297 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2788 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26443 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 97 | 0% | -$1,863.70 | -58% | — |
| Sell at 2¢ | 958 | 4% | -$2,832.62 | -88% | 46 sec |
| Sell at 3¢ | 652 | 2% | -$2,827.42 | -88% | 48 sec |
| Sell at 5¢ | 461 | 2% | -$2,782.05 | -86% | 56 sec |
| Sell at 10¢ | 280 | 1% | -$2,686.90 | -83% | 64 sec |
| Sell at 25¢ | 152 | 1% | -$2,494.58 | -77% | 80 sec |
| Sell at 50¢ | 99 | 0% | -$2,259.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1062 | 6 | 10% | 4% | -46% | -81% | -84% |
| 2–5 min | 8526 | 43 | 7% | 3% | -50% | -87% | -87% |
| 1–2 min | 6755 | 25 | 3% | 1% | -60% | -93% | -92% |
| Under 1 min | 10096 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1948 | 11 | 5% | 2% | -30% | -90% | -90% |
| BNB | 1940 | 10 | 5% | 2% | -37% | -83% | -82% |
| HYPE | 1938 | 6 | 5% | 3% | -62% | -89% | -87% |
| ETH | 1929 | 10 | 6% | 3% | -38% | -87% | -86% |
| DOGE | 1928 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1927 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1920 | 7 | 3% | 1% | -55% | -88% | -88% |
| NEAR | 1914 | 11 | 6% | 3% | -26% | -79% | -79% |
| BTC | 1914 | 11 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 1031 | 2 | 3% | 1% | -77% | -81% | -83% |
| SILVER | 993 | 4 | 3% | 1% | -53% | -82% | -82% |
| WTI | 972 | 3 | 3% | 1% | -64% | -94% | -95% |
| PLATINUM | 864 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 861 | 3 | 2% | 1% | -67% | -76% | -75% |
| NATGAS | 794 | 5 | 2% | 1% | -41% | -85% | -84% |
| EURUSD | 790 | 3 | 2% | 1% | -65% | -84% | -84% |
| PALLADIUM | 782 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 739 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 699 | 3 | 1% | 1% | -60% | -99% | -98% |
| AUDUSD | 305 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 255 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13302 | 49 | 4% | 2% | -58% | -88% | -87% |
| DOWN (bought NO) | 13141 | 48 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2912 | 15 | 2% | 1% | -14% | -78% | -77% |
| 0.05–0.1% | 3018 | 11 | 3% | 2% | -47% | -92% | -91% |
| 0.1–0.2% | 4414 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5058 | 25 | 6% | 3% | -46% | -88% | -87% |
| Over 0.5% | 1953 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6741 | 28 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,745 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/21 4:44:12 AM | BNB | DOWN | 47 sec | +0.011% | — | In play | — |
| 10/21 4:43:07 AM | WTI | UP | 1.9 min | — | — | In play | — |
| 10/21 4:43:07 AM | BTC | DOWN | 1.9 min | +0.152% | — | In play | — |
| 10/21 4:42:33 AM | XRP | DOWN | 2.5 min | +0.177% | — | In play | — |
| 10/21 4:42:17 AM | ETH | DOWN | 2.7 min | +0.184% | — | In play | — |
| 10/21 4:42:02 AM | COPPER | DOWN | 3.0 min | — | — | In play | — |
| 10/21 4:42:02 AM | DOGE | DOWN | 3.0 min | +0.157% | — | In play | — |
| 10/21 4:41:28 AM | SOL | DOWN | 3.5 min | +0.198% | — | In play | — |
| 10/21 4:41:12 AM | GBPUSD | UP | 3.8 min | — | — | In play | — |
| 10/21 4:40:57 AM | GOLD | DOWN | 4.0 min | — | — | In play | — |
| 10/21 4:40:57 AM | PALLADIUM | DOWN | 4.0 min | — | — | In play | — |
| 10/21 4:39:52 AM | HYPE | DOWN | 5.1 min | +0.286% | — | In play | — |
| 10/21 4:39:52 AM | SILVER | DOWN | 5.1 min | — | — | In play | — |
| 10/21 4:39:19 AM | NEAR | DOWN | 5.7 min | +0.719% | — | In play | — |
| 10/21 4:39:19 AM | PLATINUM | DOWN | 5.7 min | — | — | In play | — |
| 10/21 4:37:23 AM | ZEC | DOWN | 7.6 min | +0.855% | — | In play | — |
| 10/21 4:29:48 AM | XRP | DOWN | 11 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:29:48 AM | BNB | UP | 11 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:48 AM | AUDUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:48 AM | PLATINUM | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:32 AM | DOGE | DOWN | 27 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:29:32 AM | PALLADIUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:16 AM | SOL | DOWN | 43 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:16 AM | BTC | UP | 43 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/21 4:29:00 AM | NEAR | UP | 59 sec | -0.414% | 0¢ | ❌ Lost | $0.00 |
| 10/21 4:28:28 AM | ZEC | DOWN | 1.5 min | +0.235% | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:28 AM | WTI | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:28 AM | USDCAD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:28:12 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/21 4:26:51 AM | SILVER | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
