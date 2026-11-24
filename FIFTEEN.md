# 15-Minute 1¢ Study

*Updated Tue Nov 24, 2:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4833 finished bets | 1% | $214.45 | +41% | +4.44¢ | $76.70 / $137.75 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4578 | $113.00 | +23% |
| Volatility model ≥ 2%, hold to the close | 8996 | $46.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 7494 | -$26.45 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66367 | 66313 | 254 (0%) | 1.07% | -$4,474.40 (-56%) | Hold to the close: -$4,474.40 (-56%) |

*In play or awaiting result: 26. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39517 | 4.5% | 0.4% (164) | -641% | ❌ Worse |
| Momentum model | 39517 | 4.4% | 0.4% (164) | -664% | ❌ Worse |
| Mean-reversion model | 39517 | 7.9% | 0.4% (164) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39517 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8996 | 80 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4833 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2799 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7494 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4578 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2985 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16078 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11188 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7434 | 66 | +1% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39723 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15727 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10863 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66313 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,474.40 | -56% | — |
| Sell at 2¢ | 2718 | 4% | -$7,029.72 | -88% | 47 sec |
| Sell at 3¢ | 1829 | 3% | -$7,023.09 | -87% | 48 sec |
| Sell at 5¢ | 1247 | 2% | -$6,897.85 | -86% | 62 sec |
| Sell at 10¢ | 764 | 1% | -$6,623.56 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,113.30 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,513.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3427 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21505 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16572 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 24796 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4440 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4435 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4433 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4423 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4419 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4414 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4394 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4388 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4377 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2330 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2316 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2273 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2065 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2026 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1955 | 6 | 2% | 1% | -71% | -78% | -78% |
| GBPUSD | 1955 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1920 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1916 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1855 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1473 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1391 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1017 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 524 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 495 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 483 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 474 | 2 | 4% | 1% | -61% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33930 | 130 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32383 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5799 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6334 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9872 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12503 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5206 | 23 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16166 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,134 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 2:14:59 AM | SILVER | UP | 1 sec | — | 0¢ | In play | — |
| 11/24 2:14:43 AM | USDMXN | DOWN | 17 sec | — | 0¢ | In play | — |
| 11/24 2:14:43 AM | USDCAD | DOWN | 17 sec | — | 0¢ | In play | — |
| 11/24 2:14:43 AM | GOLD | DOWN | 17 sec | — | 1¢ | In play | — |
| 11/24 2:14:27 AM | USDJPY | UP | 33 sec | — | 0¢ | In play | — |
| 11/24 2:14:27 AM | PALLADIUM | DOWN | 33 sec | — | 0¢ | In play | — |
| 11/24 2:13:41 AM | PLATINUM | DOWN | 78 sec | — | 0¢ | In play | — |
| 11/24 2:13:25 AM | BRENT | UP | 1.6 min | — | 0¢ | In play | — |
| 11/24 2:13:09 AM | NATGAS | DOWN | 1.9 min | — | 0¢ | In play | — |
| 11/24 2:12:36 AM | WTI | UP | 2.4 min | — | 1¢ | In play | — |
| 11/24 2:12:20 AM | 30YRRATE | UP | 2.7 min | — | 0¢ | In play | — |
| 11/24 2:12:20 AM | AUDUSD | UP | 2.7 min | — | 97¢ | In play | — |
| 11/24 2:12:05 AM | COPPER | UP | 2.9 min | — | 0¢ | In play | — |
| 11/24 2:11:33 AM | NEAR | UP | 3.4 min | -0.978% | 1¢ | In play | — |
| 11/24 2:10:27 AM | 10YRRATE | UP | 4.5 min | — | 0¢ | In play | — |
| 11/24 2:10:11 AM | XRP | UP | 4.8 min | -0.672% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:10:11 AM | SOL | UP | 4.8 min | -0.628% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:09:56 AM | BTC | UP | 5.0 min | -0.662% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:09:56 AM | BNB | UP | 5.0 min | -0.560% | 1¢ | In play | — |
| 11/24 2:09:38 AM | HYPE | UP | 5.3 min | -0.968% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 2:09:38 AM | DOGE | UP | 5.3 min | -0.713% | 1¢ | In play | — |
| 11/24 2:09:22 AM | ETH | UP | 5.6 min | -0.690% | 1¢ | In play | — |
| 11/24 2:09:22 AM | ZEC | UP | 5.6 min | -1.253% | 1¢ | In play | — |
| 11/24 2:08:35 AM | 5YRRATE | UP | 6.4 min | — | 0¢ | In play | — |
| 11/24 1:59:43 AM | 30YRRATE | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:43 AM | 10YRRATE | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:43 AM | EURUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:27 AM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:27 AM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:59:11 AM | USDMXN | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
