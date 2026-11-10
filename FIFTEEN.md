# 15-Minute 1¢ Study

*Updated Tue Nov 10, 7:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4164 finished bets | 1% | $181.25 | +39% | +4.35¢ | $88.75 / $92.50 |

*Expect about **96 buys a day** (~$14.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3880 | $98.00 | +23% |
| Volatility model ≥ 2%, hold to the close | 7614 | $63.65 | +7% |
| Momentum model ≥ 2%, hold to the close | 6311 | -$10.80 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52129 | 52096 | 199 (0%) | 1.07% | -$3,561.10 (-56%) | Hold to the close: -$3,561.10 (-56%) |

*In play or awaiting result: 25. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31585 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31585 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31585 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31585 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7614 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4164 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2400 | 28 | +67% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6311 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3880 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2546 | 25 | +38% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13076 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9166 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6128 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31790 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12365 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7941 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52096 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,561.10 | -56% | — |
| Sell at 2¢ | 2071 | 4% | -$5,528.64 | -87% | 47 sec |
| Sell at 3¢ | 1409 | 3% | -$5,517.59 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,400.80 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,175.65 | -82% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,803.76 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,361.35 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2604 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16836 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13149 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19495 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3560 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3556 | 16 | 4% | 2% | -42% | -87% | -86% |
| HYPE | 3548 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3541 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3536 | 8 | 4% | 2% | -72% | -90% | -89% |
| ETH | 3531 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3510 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3509 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3499 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1873 | 5 | 5% | 2% | -67% | -81% | -83% |
| WTI | 1847 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1825 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1655 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1589 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1552 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1512 | 8 | 2% | 1% | -51% | -78% | -77% |
| GBPUSD | 1508 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1489 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1487 | 6 | 2% | 1% | -62% | -97% | -96% |
| AUDUSD | 1051 | 5 | 2% | 1% | -56% | -87% | -88% |
| USDCAD | 1018 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 612 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 340 | 2 | 4% | 2% | -45% | -65% | -63% |
| 2YRRATE | 322 | 4 | 4% | 2% | +16% | -34% | -33% |
| 30YRRATE | 316 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 299 | 2 | 4% | 2% | -38% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26415 | 104 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25681 | 95 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5429 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8175 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9503 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3569 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12536 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,892 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 7:29:55 AM | WTI | DOWN | 4 sec | — | 0¢ | In play | — |
| 11/10 7:29:39 AM | NATGAS | UP | 20 sec | — | 0¢ | In play | — |
| 11/10 7:29:39 AM | COPPER | DOWN | 20 sec | — | 0¢ | In play | — |
| 11/10 7:29:25 AM | EURUSD | DOWN | 35 sec | — | 0¢ | In play | — |
| 11/10 7:29:06 AM | SILVER | DOWN | 54 sec | — | 0¢ | In play | — |
| 11/10 7:29:06 AM | USDCAD | UP | 54 sec | — | 0¢ | In play | — |
| 11/10 7:29:06 AM | BRENT | DOWN | 54 sec | — | 0¢ | In play | — |
| 11/10 7:29:06 AM | ZEC | UP | 54 sec | -0.234% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:28:34 AM | PLATINUM | UP | 86 sec | — | 0¢ | In play | — |
| 11/10 7:28:34 AM | XRP | UP | 86 sec | -0.358% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:28:34 AM | USDJPY | DOWN | 86 sec | — | 0¢ | In play | — |
| 11/10 7:28:00 AM | AUDUSD | UP | 2.0 min | — | 0¢ | In play | — |
| 11/10 7:27:28 AM | DOGE | UP | 2.5 min | -0.419% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:28 AM | 30YRRATE | DOWN | 2.5 min | — | 0¢ | In play | — |
| 11/10 7:27:28 AM | ETH | UP | 2.5 min | -0.374% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:13 AM | BTC | UP | 2.8 min | -0.348% | 1¢ | In play | — |
| 11/10 7:26:38 AM | NEAR | UP | 3.4 min | -0.945% | 1¢ | In play | — |
| 11/10 7:26:22 AM | 2YRRATE | DOWN | 3.6 min | — | 0¢ | In play | — |
| 11/10 7:26:07 AM | 10YRRATE | DOWN | 3.9 min | — | 0¢ | In play | — |
| 11/10 7:26:07 AM | 5YRRATE | DOWN | 3.9 min | — | 0¢ | In play | — |
| 11/10 7:24:46 AM | BNB | UP | 5.2 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:24:46 AM | SOL | UP | 5.2 min | -0.698% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:24:30 AM | HYPE | UP | 5.5 min | -0.805% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:49 AM | EURUSD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:34 AM | COPPER | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:34 AM | XRP | UP | 26 sec | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 11/10 7:14:15 AM | DOGE | DOWN | 45 sec | +0.090% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:15 AM | HYPE | DOWN | 45 sec | +0.157% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:13:59 AM | 2YRRATE | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:13:59 AM | SOL | DOWN | 61 sec | +0.095% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
