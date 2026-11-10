# 15-Minute 1¢ Study

*Updated Mon Nov 9, 10:29 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4135 finished bets | 1% | $184.25 | +40% | +4.46¢ | $90.10 / $94.15 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3842 | $102.05 | +25% |
| Volatility model ≥ 2%, hold to the close | 7563 | $69.65 | +8% |
| Momentum model ≥ 2%, hold to the close | 6260 | -$4.95 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51645 | 51610 | 199 (0%) | 1.07% | -$3,498.70 (-56%) | Hold to the close: -$3,498.70 (-56%) |

*In play or awaiting result: 27. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31369 | 4.8% | 0.4% (128) | -676% | ❌ Worse |
| Momentum model | 31369 | 4.6% | 0.4% (128) | -701% | ❌ Worse |
| Mean-reversion model | 31369 | 8.1% | 0.4% (128) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31369 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7563 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4135 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2382 | 28 | +68% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6260 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3842 | 37 | +25% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2522 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12977 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9102 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6084 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31574 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 12222 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7814 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51610 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,498.70 | -56% | — |
| Sell at 2¢ | 2056 | 4% | -$5,470.14 | -87% | 47 sec |
| Sell at 3¢ | 1401 | 3% | -$5,458.31 | -87% | 48 sec |
| Sell at 5¢ | 980 | 2% | -$5,339.70 | -85% | 63 sec |
| Sell at 10¢ | 594 | 1% | -$5,114.56 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,741.36 | -75% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,298.95 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2563 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16665 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13051 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19319 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3536 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3532 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3523 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3516 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3512 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3507 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3487 | 17 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3486 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3475 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1856 | 5 | 5% | 2% | -67% | -81% | -83% |
| WTI | 1827 | 6 | 4% | 2% | -60% | -91% | -92% |
| SILVER | 1806 | 8 | 5% | 2% | -48% | -82% | -82% |
| PLATINUM | 1636 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1570 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1534 | 6 | 2% | 1% | -63% | -73% | -72% |
| NATGAS | 1496 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1491 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1472 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1468 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1030 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 999 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 595 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26157 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25453 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5082 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5398 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8117 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9435 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3534 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 13979 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,915 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 10:29:08 PM | USDCAD | UP | 51 sec | — | — | In play | — |
| 11/9 10:28:37 PM | AUDUSD | DOWN | 83 sec | — | — | In play | — |
| 11/9 10:28:21 PM | BTC | UP | 1.6 min | -0.084% | — | In play | — |
| 11/9 10:28:05 PM | HYPE | UP | 1.9 min | -0.316% | — | In play | — |
| 11/9 10:27:49 PM | DOGE | UP | 2.2 min | -0.192% | — | In play | — |
| 11/9 10:27:49 PM | PLATINUM | DOWN | 2.2 min | — | — | In play | — |
| 11/9 10:27:33 PM | XRP | UP | 2.4 min | -0.219% | — | In play | — |
| 11/9 10:27:33 PM | ETH | UP | 2.4 min | -0.139% | — | In play | — |
| 11/9 10:27:17 PM | COPPER | DOWN | 2.7 min | — | — | In play | — |
| 11/9 10:27:01 PM | GOLD | DOWN | 3.0 min | — | — | In play | — |
| 11/9 10:27:01 PM | EURUSD | DOWN | 3.0 min | — | — | In play | — |
| 11/9 10:26:13 PM | ZEC | UP | 3.8 min | -0.525% | — | In play | — |
| 11/9 10:26:13 PM | SOL | UP | 3.8 min | -0.269% | — | In play | — |
| 11/9 10:25:42 PM | GBPUSD | DOWN | 4.3 min | — | — | In play | — |
| 11/9 10:25:26 PM | NATGAS | DOWN | 4.6 min | — | — | In play | — |
| 11/9 10:25:26 PM | NEAR | UP | 4.6 min | -0.882% | — | In play | — |
| 11/9 10:25:10 PM | SILVER | DOWN | 4.8 min | — | — | In play | — |
| 11/9 10:24:38 PM | USDJPY | UP | 5.3 min | — | — | In play | — |
| 11/9 10:14:58 PM | COPPER | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:14:58 PM | SILVER | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:14:42 PM | PALLADIUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:14:26 PM | GBPUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:54 PM | USDJPY | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:54 PM | EURUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:37 PM | NATGAS | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:37 PM | BNB | DOWN | 83 sec | +0.004% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:21 PM | BTC | DOWN | 1.6 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 10:13:21 PM | NEAR | DOWN | 1.6 min | +0.238% | 0¢ | ❌ Lost | $0.00 |
| 11/9 10:12:33 PM | USDCAD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 10:12:33 PM | HYPE | DOWN | 2.5 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
