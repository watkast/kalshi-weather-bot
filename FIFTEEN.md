# 15-Minute 1¢ Study

*Updated Wed Nov 18, 5:41 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4535 finished bets | 1% | $213.90 | +43% | +4.72¢ | $79.95 / $133.95 |

*Expect about **88 buys a day** (~$13.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4268 | $114.40 | +25% |
| Volatility model ≥ 2%, hold to the close | 8466 | $74.40 | +7% |
| Momentum model ≥ 2%, hold to the close | 7013 | -$6.30 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61222 | 61185 | 237 (0%) | 1.07% | -$4,126.65 (-55%) | Hold to the close: -$4,126.65 (-55%) |

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
| Volatility model | 36498 | 4.5% | 0.4% (154) | -630% | ❌ Worse |
| Momentum model | 36498 | 4.4% | 0.4% (154) | -655% | ❌ Worse |
| Mean-reversion model | 36498 | 7.9% | 0.4% (154) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36498 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8466 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4535 | 51 | +43% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2608 | 30 | +68% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7013 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4268 | 41 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2781 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14950 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10405 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6913 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36704 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14596 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9885 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61185 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,126.65 | -55% | — |
| Sell at 2¢ | 2469 | 4% | -$6,508.71 | -87% | 47 sec |
| Sell at 3¢ | 1666 | 3% | -$6,500.91 | -87% | 48 sec |
| Sell at 5¢ | 1136 | 2% | -$6,384.25 | -86% | 63 sec |
| Sell at 10¢ | 693 | 1% | -$6,130.82 | -82% | 65 sec |
| Sell at 25¢ | 371 | 1% | -$5,670.64 | -76% | 80 sec |
| Sell at 50¢ | 244 | 0% | -$5,125.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3115 | 17 | 10% | 4% | -48% | -82% | -83% |
| 2–5 min | 19828 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15323 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 22906 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4104 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4101 | 19 | 4% | 2% | -41% | -86% | -87% |
| HYPE | 4095 | 12 | 4% | 2% | -63% | -89% | -88% |
| BNB | 4085 | 21 | 5% | 2% | -35% | -85% | -85% |
| DOGE | 4084 | 11 | 4% | 2% | -66% | -90% | -89% |
| ETH | 4078 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4059 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4056 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4042 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2180 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2159 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2117 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1927 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1882 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1814 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1809 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1779 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1768 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1732 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1320 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1261 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 888 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 444 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 426 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31187 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29998 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5503 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5974 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9193 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11395 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4630 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15091 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,027 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 5:41:25 PM | NATGAS | UP | 3.6 min | — | — | In play | — |
| 11/18 5:40:19 PM | NEAR | DOWN | 4.7 min | +0.718% | — | In play | — |
| 11/18 5:40:03 PM | AUDUSD | UP | 5.0 min | — | — | In play | — |
| 11/18 5:29:29 PM | SOL | DOWN | 30 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:29 PM | HYPE | DOWN | 30 sec | +0.172% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:29 PM | BTC | DOWN | 30 sec | +0.137% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:29 PM | DOGE | DOWN | 30 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:29 PM | NEAR | DOWN | 30 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:29:29 PM | USDJPY | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:29 PM | PALLADIUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:29:13 PM | ZEC | DOWN | 47 sec | +0.221% | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:28:08 PM | BNB | DOWN | 1.9 min | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:27:52 PM | PLATINUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:27:36 PM | ETH | DOWN | 2.4 min | +0.230% | 2¢ | ❌ Lost | -$0.15 |
| 11/18 5:26:47 PM | NATGAS | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:26:47 PM | GOLD | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 5:25:59 PM | SILVER | DOWN | 4.0 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/18 5:25:59 PM | AUDUSD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 5:25:27 PM | COPPER | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:44:16 PM | XRP | UP | 43 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:43:58 PM | DOGE | UP | 62 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:43:58 PM | HYPE | DOWN | 62 sec | +0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:43:58 PM | ETH | DOWN | 62 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:43:26 PM | BNB | DOWN | 1.6 min | +0.095% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:43:26 PM | ZEC | UP | 1.6 min | -0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:31 PM | WTI | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:31 PM | GBPUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 3:29:13 PM | DOGE | DOWN | 47 sec | +0.055% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:29:13 PM | ETH | UP | 47 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/18 3:29:13 PM | XRP | DOWN | 47 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
