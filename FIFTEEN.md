# 15-Minute 1¢ Study

*Updated Tue Nov 24, 12:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4829 finished bets | 1% | $214.90 | +41% | +4.45¢ | $76.85 / $138.05 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4574 | $113.45 | +23% |
| Volatility model ≥ 2%, hold to the close | 8990 | $47.65 | +4% |
| Momentum model ≥ 2%, hold to the close | 7490 | -$26.00 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66210 | 66176 | 254 (0%) | 1.07% | -$4,456.70 (-56%) | Hold to the close: -$4,456.70 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39459 | 4.5% | 0.4% (164) | -640% | ❌ Worse |
| Momentum model | 39459 | 4.4% | 0.4% (164) | -663% | ❌ Worse |
| Mean-reversion model | 39459 | 7.9% | 0.4% (164) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39459 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8990 | 80 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4829 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2795 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7490 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4574 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2981 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16052 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11173 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7421 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39665 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15685 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10826 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66176 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,456.70 | -56% | — |
| Sell at 2¢ | 2712 | 4% | -$7,013.58 | -88% | 47 sec |
| Sell at 3¢ | 1827 | 3% | -$7,006.17 | -87% | 48 sec |
| Sell at 5¢ | 1247 | 2% | -$6,880.15 | -86% | 62 sec |
| Sell at 10¢ | 764 | 1% | -$6,605.86 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,095.60 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,495.45 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3422 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21453 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16537 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24751 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4434 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4428 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4426 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4417 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4413 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4408 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4387 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4382 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4370 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2325 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2310 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2267 | 9 | 5% | 2% | -52% | -83% | -83% |
| PLATINUM | 2060 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2022 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1952 | 8 | 2% | 1% | -62% | -96% | -96% |
| COPPER | 1949 | 6 | 2% | 1% | -71% | -78% | -78% |
| USDJPY | 1915 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1912 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1850 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1468 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1386 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 1012 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 520 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 494 | 4 | 4% | 2% | -24% | -56% | -55% |
| 30YRRATE | 479 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 471 | 2 | 3% | 1% | -60% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33835 | 130 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32341 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5794 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6328 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9864 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12474 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5196 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16029 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,136 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 12:29:54 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:54 AM | ZEC | DOWN | 5 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:54 AM | BTC | UP | 5 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:29:38 AM | USDCAD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:38 AM | PLATINUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:38 AM | SILVER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:22 AM | COPPER | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | ETH | UP | 54 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:29:06 AM | DOGE | UP | 54 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | SOL | UP | 54 sec | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:29:06 AM | XRP | UP | 54 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:28:49 AM | GOLD | UP | 70 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:28:33 AM | WTI | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:28:33 AM | BRENT | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:28:17 AM | USDMXN | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:28:01 AM | AUDUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:28:01 AM | NATGAS | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:27:43 AM | HYPE | UP | 2.3 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:27:43 AM | NEAR | UP | 2.3 min | -0.484% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:27:43 AM | USDJPY | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:14:14 AM | NEAR | DOWN | 46 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:14:14 AM | EURUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:14:14 AM | SILVER | UP | 46 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:14:14 AM | USDMXN | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:13:58 AM | COPPER | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 12:13:58 AM | SOL | UP | 62 sec | -0.140% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:13:58 AM | BTC | UP | 62 sec | -0.151% | 0¢ | ❌ Lost | $0.00 |
| 11/24 12:13:26 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:13:10 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 12:12:54 AM | AUDUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
