# 15-Minute 1¢ Study

*Updated Mon Oct 26, 4:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2739 finished bets | 1% | $80.90 | +26% | +2.95¢ | $31.70 / $49.20 |

*Expect about **97 buys a day** (~$14.59/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2544 | $54.45 | +19% |
| Volatility model ≥ 2%, hold to the close | 5078 | -$20.05 | -3% |
| Momentum model ≥ 2%, hold to the close | 4229 | -$33.75 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32591 | 32575 | 121 (0%) | 1.07% | -$2,263.00 (-57%) | Hold to the close: -$2,263.00 (-57%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20956 | 4.6% | 0.4% (85) | -661% | ❌ Worse |
| Momentum model | 20956 | 4.5% | 0.4% (85) | -685% | ❌ Worse |
| Mean-reversion model | 20956 | 7.9% | 0.4% (85) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20956 | 85 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 5078 | 43 | -3% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2739 | 28 | +26% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1550 | 18 | +62% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4229 | 33 | -7% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2544 | 24 | +19% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 1657 | 16 | +32% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8465 | 56 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5930 | 47 | -13% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3947 | 33 | -6% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21156 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7591 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3828 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32575 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 121 | 0% | -$2,263.00 | -57% | — |
| Sell at 2¢ | 1220 | 4% | -$3,471.80 | -88% | 47 sec |
| Sell at 3¢ | 837 | 3% | -$3,462.57 | -88% | 48 sec |
| Sell at 5¢ | 582 | 2% | -$3,410.70 | -86% | 61 sec |
| Sell at 10¢ | 362 | 1% | -$3,272.78 | -83% | 65 sec |
| Sell at 25¢ | 194 | 1% | -$3,034.86 | -77% | 82 sec |
| Sell at 50¢ | 125 | 0% | -$2,749.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1439 | 7 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 10432 | 56 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8251 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12449 | 28 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2371 | 12 | 5% | 2% | -36% | -89% | -89% |
| HYPE | 2363 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2360 | 13 | 5% | 3% | -32% | -84% | -83% |
| SOL | 2357 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2351 | 11 | 6% | 3% | -44% | -86% | -85% |
| DOGE | 2343 | 4 | 4% | 2% | -79% | -91% | -90% |
| XRP | 2340 | 9 | 3% | 1% | -53% | -89% | -89% |
| NEAR | 2339 | 12 | 5% | 2% | -33% | -82% | -81% |
| BTC | 2332 | 12 | 5% | 2% | -31% | -88% | -89% |
| GOLD | 1226 | 4 | 4% | 2% | -61% | -81% | -83% |
| SILVER | 1193 | 6 | 4% | 2% | -41% | -82% | -81% |
| WTI | 1170 | 3 | 3% | 1% | -70% | -94% | -95% |
| PLATINUM | 1040 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 1017 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 972 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 966 | 5 | 2% | 1% | -52% | -87% | -86% |
| PALLADIUM | 929 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 919 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 900 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 463 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 422 | 0 | 1% | 0% | -100% | -98% | -99% |
| BRENT | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16502 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 16073 | 55 | 4% | 2% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3525 | 18 | 2% | 1% | -14% | -80% | -80% |
| 0.05–0.1% | 3633 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5474 | 20 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 6177 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2343 | 10 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 8213 | 33 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,796 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 4:43:52 AM | EURUSD | UP | 68 sec | — | — | In play | — |
| 10/26 4:43:52 AM | NEAR | DOWN | 68 sec | +0.196% | — | In play | — |
| 10/26 4:43:36 AM | PLATINUM | UP | 84 sec | — | — | In play | — |
| 10/26 4:41:26 AM | SOL | DOWN | 3.6 min | +0.201% | — | In play | — |
| 10/26 4:41:26 AM | BNB | DOWN | 3.6 min | +0.128% | — | In play | — |
| 10/26 4:41:26 AM | HYPE | DOWN | 3.6 min | +0.230% | — | In play | — |
| 10/26 4:40:23 AM | ZEC | DOWN | 4.6 min | +0.395% | — | In play | — |
| 10/26 4:39:51 AM | USDJPY | DOWN | 5.2 min | — | — | In play | — |
| 10/26 4:29:44 AM | SOL | UP | 15 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:29:44 AM | NATGAS | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:29:44 AM | HYPE | DOWN | 15 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:29:44 AM | USDCAD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:29:12 AM | ZEC | UP | 47 sec | -0.209% | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:29:12 AM | BTC | UP | 47 sec | -0.078% | 0¢ | ❌ Lost | $0.00 |
| 10/26 4:29:12 AM | GBPUSD | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:28:56 AM | DOGE | DOWN | 64 sec | +0.068% | 1¢ | ❌ Lost | $0.00 |
| 10/26 4:28:40 AM | GOLD | UP | 80 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/26 4:28:24 AM | PLATINUM | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:28:24 AM | XRP | DOWN | 1.6 min | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:28:24 AM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:28:24 AM | SILVER | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:27:51 AM | PALLADIUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:27:51 AM | AUDUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:27:35 AM | ETH | UP | 2.4 min | -0.126% | 10¢ | ❌ Lost | -$0.15 |
| 10/26 4:27:03 AM | COPPER | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:26:15 AM | BNB | UP | 3.7 min | -0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 4:14:57 AM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:14:57 AM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:14:57 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 4:14:57 AM | SILVER | UP | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
