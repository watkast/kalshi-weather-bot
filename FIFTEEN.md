# 15-Minute 1¢ Study

*Updated Fri Oct 16, 7:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1618 finished bets | 1% | $72.45 | +40% | +4.48¢ | $38.55 / $33.90 |

*Expect about **89 buys a day** (~$13.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1502 | $47.40 | +29% |
| Momentum model ≥ 2%, hold to the close | 2533 | -$13.55 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1618 | -$22.80 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20771 | 20764 | 79 (0%) | 1.07% | -$1,422.55 (-56%) | Hold to the close: -$1,422.55 (-56%) |

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
| Volatility model | 13280 | 4.4% | 0.4% (53) | -643% | ❌ Worse |
| Momentum model | 13280 | 4.4% | 0.4% (53) | -667% | ❌ Worse |
| Mean-reversion model | 13280 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13280 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2953 | 23 | -10% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1618 | 18 | +40% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 948 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2533 | 20 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1502 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1002 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4995 | 33 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3435 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2255 | 15 | -24% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13478 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5154 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2132 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20764 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,422.55 | -56% | — |
| Sell at 2¢ | 736 | 4% | -$2,239.19 | -89% | 42 sec |
| Sell at 3¢ | 494 | 2% | -$2,237.89 | -89% | 47 sec |
| Sell at 5¢ | 358 | 2% | -$2,197.85 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,116.97 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,946.80 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,737.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 680 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6738 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5410 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7932 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1513 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1509 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1503 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1499 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1499 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1496 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1490 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1486 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1483 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 842 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 818 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 785 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 717 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 701 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 646 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 645 | 5 | 2% | 2% | -28% | -81% | -80% |
| EURUSD | 638 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 598 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 559 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 181 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 156 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10469 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10295 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2231 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2328 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3414 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3954 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1548 | 6 | 6% | 3% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4781 | 26 | 4% | 2% | -37% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,426 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 7:14:58 AM | BTC | UP | 2 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:58 AM | GBPUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:58 AM | SOL | DOWN | 2 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:42 AM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:42 AM | NEAR | UP | 18 sec | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:11 AM | ETH | DOWN | 49 sec | +0.045% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:11 AM | SILVER | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:14:11 AM | BNB | UP | 49 sec | -0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:14:11 AM | DOGE | DOWN | 49 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:13:38 AM | XRP | UP | 81 sec | -0.142% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:13:22 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:12:50 AM | WTI | DOWN | 2.2 min | — | 4¢ | ❌ Lost | -$0.15 |
| 10/16 7:12:34 AM | AUDUSD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:10:57 AM | HYPE | UP | 4.0 min | -0.305% | 6¢ | ❌ Lost | -$0.15 |
| 10/16 7:10:38 AM | ZEC | UP | 4.4 min | -0.597% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:48 AM | EURUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:48 AM | NATGAS | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:48 AM | WTI | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:32 AM | COPPER | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:59:16 AM | USDCAD | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:52 AM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:52 AM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:36 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:57:04 AM | HYPE | UP | 2.9 min | -0.271% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 6:56:31 AM | XRP | UP | 3.5 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:56:15 AM | BTC | UP | 3.7 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:55:59 AM | GOLD | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:55:08 AM | SOL | UP | 4.8 min | -0.459% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:54:21 AM | ZEC | UP | 5.6 min | -0.598% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:53:49 AM | BNB | UP | 6.2 min | -0.296% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
