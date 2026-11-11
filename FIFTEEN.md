# 15-Minute 1¢ Study

*Updated Wed Nov 11, 11:05 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4211 finished bets | 1% | $176.45 | +38% | +4.19¢ | $85.90 / $90.55 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3934 | $92.00 | +22% |
| Volatility model ≥ 2%, hold to the close | 7726 | $50.15 | +5% |
| Momentum model ≥ 2%, hold to the close | 6415 | -$23.10 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53681 | 53660 | 205 (0%) | 1.07% | -$3,674.95 (-56%) | Hold to the close: -$3,674.95 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32295 | 4.7% | 0.4% (131) | -672% | ❌ Worse |
| Momentum model | 32295 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32295 | 8.1% | 0.4% (131) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32295 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7726 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4211 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2433 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6415 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3934 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2581 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13355 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9341 | 78 | -7% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6243 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32500 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12838 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8322 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53660 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 205 | 0% | -$3,674.95 | -56% | — |
| Sell at 2¢ | 2138 | 4% | -$5,709.07 | -87% | 47 sec |
| Sell at 3¢ | 1456 | 3% | -$5,697.11 | -87% | 48 sec |
| Sell at 5¢ | 1012 | 2% | -$5,579.15 | -85% | 63 sec |
| Sell at 10¢ | 611 | 1% | -$5,352.54 | -82% | 65 sec |
| Sell at 25¢ | 325 | 1% | -$4,965.20 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,497.95 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2686 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17372 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13543 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20047 | 53 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3638 | 17 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3634 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3627 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3619 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3615 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3609 | 15 | 7% | 3% | -49% | -82% | -81% |
| NEAR | 3590 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3590 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3578 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1935 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1916 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1886 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1715 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1651 | 5 | 2% | 1% | -72% | -90% | -89% |
| COPPER | 1602 | 6 | 2% | 1% | -65% | -74% | -73% |
| GBPUSD | 1572 | 6 | 2% | 1% | -64% | -96% | -96% |
| NATGAS | 1570 | 8 | 2% | 1% | -52% | -79% | -78% |
| USDJPY | 1555 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1542 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1109 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1078 | 0 | 3% | 1% | -100% | -96% | -96% |
| BRENT | 672 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27191 | 108 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26469 | 97 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5169 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5520 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8351 | 30 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 9750 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3702 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13014 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 10:59:48 AM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:59:32 AM | PLATINUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:58 AM | GBPUSD | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:42 AM | USDCAD | DOWN | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:42 AM | EURUSD | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:42 AM | BNB | UP | 78 sec | -0.096% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:27 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:27 AM | ZEC | UP | 1.6 min | -0.548% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:27 AM | BTC | UP | 1.6 min | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:09 AM | XRP | UP | 1.9 min | -0.280% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:09 AM | ETH | UP | 1.9 min | -0.197% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:58:09 AM | HYPE | UP | 1.9 min | -0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:57:53 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:57:53 AM | BRENT | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:57:53 AM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:57:37 AM | NATGAS | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:56:48 AM | DOGE | UP | 3.2 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:56:48 AM | SOL | UP | 3.2 min | -0.393% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 10:56:32 AM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 10:56:17 AM | NEAR | UP | 3.7 min | -0.741% | 0¢ | ❌ Lost | $0.00 |
| 11/11 10:55:13 AM | WTI | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:41:39 AM | PLATINUM | UP | 3.4 min | — | — | ❌ Lost | -$0.15 |
| 11/11 7:40:04 AM | HYPE | DOWN | 4.9 min | +0.935% | — | ❌ Lost | -$0.15 |
| 11/11 7:40:04 AM | PALLADIUM | UP | 4.9 min | — | — | ❌ Lost | -$0.15 |
| 11/11 7:37:38 AM | GOLD | UP | 7.3 min | — | — | ❌ Lost | -$0.15 |
| 11/11 7:29:49 AM | NEAR | UP | 10 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:29:49 AM | SILVER | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:29:49 AM | GOLD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:29:33 AM | WTI | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:29:33 AM | AUDUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
