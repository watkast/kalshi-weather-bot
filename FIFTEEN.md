# 15-Minute 1¢ Study

*Updated Mon Oct 26, 4:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2734 finished bets | 1% | $81.50 | +26% | +2.98¢ | $32.00 / $49.50 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2539 | $55.05 | +20% |
| Volatility model ≥ 2%, hold to the close | 5071 | -$19.30 | -3% |
| Momentum model ≥ 2%, hold to the close | 4223 | -$33.15 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32546 | 32538 | 121 (0%) | 1.07% | -$2,258.50 (-57%) | Hold to the close: -$2,258.50 (-57%) |

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
| Volatility model | 20939 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20939 | 4.5% | 0.4% (85) | -686% | ❌ Worse |
| Mean-reversion model | 20939 | 7.9% | 0.4% (85) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20939 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5071 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2734 | 28 | +26% | -74% | -73% | -70% |
| Volatility model ≥ 10% | 1548 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4223 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2539 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1657 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8456 | 56 | -28% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5924 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3944 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21139 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7579 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3820 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32538 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,258.50 | -57% | — |
| Sell at 2¢ | 1217 | 4% | -$3,468.08 | -88% | 47 sec |
| Sell at 3¢ | 835 | 3% | -$3,458.85 | -88% | 48 sec |
| Sell at 5¢ | 581 | 2% | -$3,406.85 | -86% | 61 sec |
| Sell at 10¢ | 361 | 1% | -$3,269.59 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,030.36 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,744.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1439 | 7 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 10421 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8240 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12434 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2369 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2361 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2358 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2355 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2349 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2341 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2338 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2338 | 9 | 3% | 1% | -53% | -89% | -89% |
| BTC | 2330 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1225 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1191 | 6 | 4% | 2% | -41% | -82% | -81% |
| WTI | 1169 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1038 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1015 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 971 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 964 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 927 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 917 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 898 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 461 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 421 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16471 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16067 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3523 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3630 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5465 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6174 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2343 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8176 | 33 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,803 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 3:59:52 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:59:52 AM | BRENT | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:59:52 AM | BTC | UP | 8 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:59:36 AM | NATGAS | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:59:21 AM | WTI | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:59:21 AM | GBPUSD | UP | 38 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/26 3:59:21 AM | SILVER | UP | 38 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:59:03 AM | NEAR | DOWN | 57 sec | +0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:59:03 AM | AUDUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:58:47 AM | BNB | DOWN | 73 sec | +0.061% | 3¢ | ❌ Lost | -$0.15 |
| 10/26 3:58:47 AM | HYPE | DOWN | 73 sec | +0.122% | 3¢ | ❌ Lost | $0.00 |
| 10/26 3:58:16 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:58:16 AM | ETH | DOWN | 1.7 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:57:59 AM | USDCAD | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:57:43 AM | SOL | DOWN | 2.3 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:57:11 AM | PLATINUM | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:57:11 AM | XRP | DOWN | 2.8 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:56:20 AM | ZEC | DOWN | 3.7 min | +0.968% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:55:49 AM | EURUSD | UP | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:53 AM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:53 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | ZEC | DOWN | 22 sec | +0.054% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | BRENT | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:37 AM | ETH | DOWN | 22 sec | +0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | SOL | DOWN | 22 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | BTC | DOWN | 22 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:37 AM | DOGE | UP | 22 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/26 3:44:21 AM | NATGAS | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 3:44:21 AM | BNB | UP | 38 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
