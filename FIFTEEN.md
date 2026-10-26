# 15-Minute 1¢ Study

*Updated Mon Oct 26, 8:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2746 finished bets | 1% | $80.30 | +26% | +2.92¢ | $31.10 / $49.20 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2551 | $53.70 | +19% |
| Volatility model ≥ 2%, hold to the close | 5094 | -$21.85 | -4% |
| Momentum model ≥ 2%, hold to the close | 4241 | -$35.25 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32851 | 32843 | 122 (0%) | 1.07% | -$2,284.25 (-57%) | Hold to the close: -$2,284.25 (-57%) |

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
| Volatility model | 21082 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21082 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21082 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21082 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5094 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2746 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1554 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4241 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2551 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1661 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8518 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5962 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3969 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21282 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7671 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3890 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32843 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,284.25 | -57% | — |
| Sell at 2¢ | 1234 | 4% | -$3,503.41 | -88% | 47 sec |
| Sell at 3¢ | 844 | 3% | -$3,495.09 | -88% | 48 sec |
| Sell at 5¢ | 588 | 2% | -$3,442.05 | -86% | 61 sec |
| Sell at 10¢ | 364 | 1% | -$3,305.41 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,066.80 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,777.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1452 | 8 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 10538 | 56 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8325 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12524 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2385 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2377 | 8 | 5% | 3% | -58% | -88% | -87% |
| BNB | 2374 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2371 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2365 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2357 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2354 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2353 | 12 | 5% | 2% | -34% | -82% | -81% |
| BTC | 2346 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1238 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1205 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1180 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1052 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1025 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 983 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 975 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 940 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 930 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 910 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 472 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 434 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 56 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 46 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 42 | 1 | 5% | 0% | +122% | +130% | +128% |
| 30YRRATE | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16653 | 67 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16190 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3533 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3649 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5500 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6236 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2360 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7945 | 36 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,781 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 7:59:47 AM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:59:31 AM | 2YRRATE | DOWN | 29 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/26 7:59:07 AM | 5YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:51 AM | 10YRRATE | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:51 AM | COPPER | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:19 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:19 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:19 AM | NEAR | UP | 1.7 min | -0.553% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:46 AM | DOGE | UP | 2.2 min | -0.384% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:46 AM | BTC | UP | 2.2 min | -0.306% | 1¢ | ❌ Lost | $0.00 |
| 10/26 7:57:46 AM | BNB | UP | 2.2 min | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:57:46 AM | BRENT | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:46 AM | SOL | UP | 2.2 min | -0.426% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:30 AM | AUDUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:30 AM | ZEC | UP | 2.5 min | -0.647% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:30 AM | XRP | UP | 2.5 min | -0.482% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:14 AM | USDCAD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:14 AM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:57:14 AM | EURUSD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:56:58 AM | ETH | UP | 3.0 min | -0.430% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:56:43 AM | HYPE | UP | 3.3 min | -0.561% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:55:23 AM | SILVER | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:55:07 AM | GOLD | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:54:36 AM | PLATINUM | UP | 5.4 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | 2YRRATE | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | USDJPY | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:58 AM | WTI | UP | 2 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 7:44:42 AM | COPPER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:44:27 AM | 5YRRATE | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
