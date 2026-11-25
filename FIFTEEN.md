# 15-Minute 1¢ Study

*Updated Wed Nov 25, 11:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4891 finished bets | 1% | $209.35 | +39% | +4.28¢ | $87.55 / $121.80 |

*Expect about **84 buys a day** (~$12.55/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4632 | $108.65 | +22% |
| Volatility model ≥ 2%, hold to the close | 9116 | $47.85 | +4% |
| Momentum model ≥ 2%, hold to the close | 7580 | -$34.40 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67683 | 67642 | 256 (0%) | 1.07% | -$4,605.55 (-56%) | Hold to the close: -$4,605.55 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40097 | 4.5% | 0.4% (165) | -646% | ❌ Worse |
| Momentum model | 40097 | 4.4% | 0.4% (165) | -669% | ❌ Worse |
| Mean-reversion model | 40097 | 7.9% | 0.4% (165) | -786% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40097 | 165 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9116 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4891 | 53 | +39% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2831 | 32 | +67% | -65% | -63% | -59% |
| Momentum model ≥ 2% | 7580 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4632 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3022 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16324 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11368 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7548 | 66 | +0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40303 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16101 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11238 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67642 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,605.55 | -56% | — |
| Sell at 2¢ | 2771 | 4% | -$7,175.09 | -88% | 47 sec |
| Sell at 3¢ | 1861 | 3% | -$7,169.76 | -88% | 48 sec |
| Sell at 5¢ | 1260 | 2% | -$7,048.55 | -86% | 62 sec |
| Sell at 10¢ | 769 | 1% | -$6,776.16 | -83% | 65 sec |
| Sell at 25¢ | 415 | 1% | -$6,255.90 | -76% | 79 sec |
| Sell at 50¢ | 266 | 0% | -$5,652.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3496 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 21935 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16875 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25323 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4507 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4501 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4494 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4488 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4484 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4478 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4457 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4453 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4441 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2382 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2370 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2323 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2109 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2062 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 2003 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 1999 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1963 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1957 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1895 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1524 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1435 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1066 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 553 | 2 | 3% | 1% | -66% | -77% | -76% |
| 30YRRATE | 514 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 513 | 4 | 4% | 2% | -27% | -57% | -57% |
| 5YRRATE | 503 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 136 | 1 | 2% | 1% | -31% | -96% | -96% |
| USDMXN | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34577 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33065 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5848 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6403 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10000 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12699 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5344 | 24 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16113 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,094 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 11:58:58 AM | BNB | DOWN | 62 sec | +0.102% | — | In play | — |
| 11/25 11:58:42 AM | BTC | DOWN | 78 sec | +0.144% | — | In play | — |
| 11/25 11:58:27 AM | DOGE | DOWN | 1.5 min | +0.200% | — | In play | — |
| 11/25 11:58:09 AM | 5YRRATE | DOWN | 1.8 min | — | — | In play | — |
| 11/25 11:58:09 AM | ZEC | DOWN | 1.8 min | +0.986% | — | In play | — |
| 11/25 11:57:53 AM | XRP | DOWN | 2.1 min | +0.237% | — | In play | — |
| 11/25 11:57:21 AM | SOL | DOWN | 2.6 min | +0.385% | — | In play | — |
| 11/25 11:44:50 AM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:50 AM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:50 AM | SOL | DOWN | 10 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:50 AM | INX | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:35 AM | BRENT | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:35 AM | PALLADIUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:35 AM | BNB | UP | 24 sec | -0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:35 AM | HYPE | DOWN | 24 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:35 AM | BTC | UP | 24 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:17 AM | AUDUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:17 AM | WTI | DOWN | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:17 AM | ETH | UP | 42 sec | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:17 AM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:01 AM | NEAR | DOWN | 58 sec | +0.264% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:01 AM | XRP | DOWN | 58 sec | +0.195% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:44:01 AM | USDMXN | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:44:01 AM | DOGE | DOWN | 58 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:43:29 AM | 30YRRATE | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:43:09 AM | ZEC | DOWN | 1.9 min | +0.642% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:51 AM | 10YRRATE | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:51 AM | XRP | DOWN | 9 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/25 11:29:51 AM | USDCAD | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 11:29:36 AM | BNB | DOWN | 24 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
