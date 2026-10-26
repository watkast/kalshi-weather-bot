# 15-Minute 1¢ Study

*Updated Mon Oct 26, 8:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2747 finished bets | 1% | $80.15 | +26% | +2.92¢ | $31.10 / $49.05 |

*Expect about **97 buys a day** (~$14.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2551 | $53.70 | +19% |
| Volatility model ≥ 2%, hold to the close | 5097 | -$22.30 | -4% |
| Momentum model ≥ 2%, hold to the close | 4242 | -$35.40 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32876 | 32868 | 122 (0%) | 1.07% | -$2,288.00 (-57%) | Hold to the close: -$2,288.00 (-57%) |

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
| Volatility model | 21091 | 4.6% | 0.4% (85) | -663% | ❌ Worse |
| Momentum model | 21091 | 4.5% | 0.4% (85) | -687% | ❌ Worse |
| Mean-reversion model | 21091 | 7.9% | 0.4% (85) | -804% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 21091 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5097 | 43 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2747 | 28 | +26% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1554 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4242 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2551 | 24 | +19% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1661 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8525 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5966 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3971 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21291 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7679 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3898 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32868 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 122 | 0% | -$2,288.00 | -57% | — |
| Sell at 2¢ | 1235 | 4% | -$3,506.90 | -88% | 47 sec |
| Sell at 3¢ | 845 | 3% | -$3,498.45 | -88% | 48 sec |
| Sell at 5¢ | 588 | 2% | -$3,445.80 | -86% | 61 sec |
| Sell at 10¢ | 364 | 1% | -$3,309.16 | -83% | 65 sec |
| Sell at 25¢ | 195 | 1% | -$3,070.55 | -77% | 83 sec |
| Sell at 50¢ | 126 | 0% | -$2,781.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1453 | 8 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 10551 | 56 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8333 | 30 | 3% | 1% | -61% | -92% | -92% |
| Under 1 min | 12527 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2386 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2378 | 8 | 5% | 3% | -58% | -88% | -86% |
| BNB | 2375 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2372 | 6 | 4% | 2% | -69% | -92% | -92% |
| ETH | 2366 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2358 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2355 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2354 | 12 | 5% | 2% | -34% | -82% | -81% |
| BTC | 2347 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1239 | 4 | 4% | 2% | -62% | -81% | -83% |
| SILVER | 1206 | 6 | 4% | 2% | -42% | -82% | -81% |
| WTI | 1181 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1053 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1026 | 4 | 1% | 1% | -64% | -70% | -70% |
| EURUSD | 984 | 3 | 2% | 1% | -72% | -87% | -87% |
| NATGAS | 976 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 941 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 931 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 911 | 5 | 1% | 1% | -49% | -98% | -97% |
| AUDUSD | 473 | 1 | 1% | 1% | -80% | -98% | -97% |
| USDCAD | 435 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 57 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 47 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 42 | 1 | 5% | 0% | +122% | +130% | +128% |
| 30YRRATE | 42 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 33 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16660 | 67 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 16208 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3533 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3649 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5500 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6240 | 28 | 6% | 3% | -51% | -87% | -86% |
| Over 0.5% | 2365 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8317 | 33 | 4% | 2% | -55% | -85% | -85% |
| Morning (6am–12pm) | 7970 | 36 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,778 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 8:14:47 AM | NATGAS | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:14:31 AM | 5YRRATE | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:14:15 AM | COPPER | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:58 AM | PLATINUM | DOWN | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:42 AM | AUDUSD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:42 AM | ZEC | DOWN | 77 sec | +0.419% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:26 AM | 10YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:26 AM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:10 AM | 30YRRATE | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:10 AM | USDCAD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:13:10 AM | SILVER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:46 AM | GBPUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:46 AM | EURUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:46 AM | NEAR | DOWN | 3.2 min | +0.926% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:30 AM | BTC | DOWN | 3.5 min | +0.521% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:14 AM | HYPE | DOWN | 3.8 min | +0.472% | 3¢ | ❌ Lost | -$0.15 |
| 10/26 8:11:00 AM | PALLADIUM | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:42 AM | BNB | DOWN | 4.3 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:42 AM | ETH | DOWN | 4.3 min | +0.599% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:26 AM | DOGE | DOWN | 4.6 min | +0.496% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:10 AM | GOLD | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:10 AM | XRP | DOWN | 4.8 min | +0.780% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:10 AM | SOL | DOWN | 4.8 min | +0.683% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 8:10:10 AM | WTI | UP | 4.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/26 8:09:55 AM | USDJPY | UP | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 7:59:47 AM | USDJPY | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:59:31 AM | 2YRRATE | DOWN | 29 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/26 7:59:07 AM | 5YRRATE | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:51 AM | 10YRRATE | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 7:58:51 AM | COPPER | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
