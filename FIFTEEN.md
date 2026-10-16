# 15-Minute 1¢ Study

*Updated Fri Oct 16, 2:07 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1595 finished bets | 1% | $74.70 | +42% | +4.68¢ | $39.90 / $34.80 |

*Expect about **88 buys a day** (~$13.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1485 | $48.90 | +30% |
| Momentum model ≥ 2%, hold to the close | 2496 | -$9.65 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1595 | -$20.55 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20440 | 20433 | 79 (0%) | 1.07% | -$1,380.10 (-56%) | Hold to the close: -$1,380.10 (-56%) |

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
| Volatility model | 13100 | 4.4% | 0.4% (53) | -641% | ❌ Worse |
| Momentum model | 13100 | 4.4% | 0.4% (53) | -665% | ❌ Worse |
| Mean-reversion model | 13100 | 7.3% | 0.4% (53) | -767% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13100 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2907 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1595 | 18 | +42% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 936 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2496 | 20 | -3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1485 | 15 | +30% | -77% | -77% | -74% |
| Momentum model ≥ 10% | 992 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4915 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3378 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2212 | 15 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13298 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5058 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2077 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20433 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,380.10 | -56% | — |
| Sell at 2¢ | 721 | 4% | -$2,200.64 | -89% | 42 sec |
| Sell at 3¢ | 483 | 2% | -$2,199.73 | -88% | 47 sec |
| Sell at 5¢ | 352 | 2% | -$2,159.30 | -87% | 50 sec |
| Sell at 10¢ | 217 | 1% | -$2,075.83 | -83% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,904.35 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,694.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6626 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5320 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7823 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1492 | 11 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1488 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1482 | 8 | 5% | 3% | -35% | -88% | -87% |
| BNB | 1480 | 5 | 4% | 2% | -58% | -90% | -90% |
| DOGE | 1479 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1475 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1470 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1468 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1464 | 8 | 5% | 3% | -29% | -78% | -79% |
| GOLD | 825 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 803 | 4 | 3% | 1% | -42% | -79% | -80% |
| WTI | 772 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 707 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 685 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 634 | 2 | 1% | 0% | -71% | -83% | -84% |
| NATGAS | 632 | 5 | 2% | 2% | -26% | -81% | -80% |
| EURUSD | 625 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 585 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 550 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 169 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 148 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10291 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10142 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2210 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2299 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3367 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3886 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1533 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5108 | 20 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,454 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 1:59:57 AM | BNB | UP | 3 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:57 AM | WTI | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:59:57 AM | USDCAD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:41 AM | ETH | DOWN | 19 sec | +0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:25 AM | HYPE | UP | 35 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:25 AM | XRP | DOWN | 35 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:09 AM | DOGE | UP | 51 sec | -0.105% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:59:09 AM | SOL | UP | 51 sec | -0.109% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:58:53 AM | GBPUSD | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:58:53 AM | BTC | DOWN | 67 sec | +0.055% | 1¢ | ❌ Lost | $0.00 |
| 10/16 1:58:21 AM | PALLADIUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:58:21 AM | ZEC | DOWN | 1.6 min | +0.275% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:58:21 AM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:57:50 AM | GOLD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:57:18 AM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:56:55 AM | NEAR | UP | 3.1 min | -0.544% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 1:44:35 AM | SOL | DOWN | 24 sec | +0.033% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:44:35 AM | BTC | UP | 24 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/16 1:44:19 AM | ZEC | UP | 40 sec | -0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:44:19 AM | COPPER | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:44:19 AM | GBPUSD | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:44:19 AM | NEAR | DOWN | 40 sec | +0.201% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:47 AM | GOLD | UP | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:31 AM | SILVER | UP | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:15 AM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:15 AM | NATGAS | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:15 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:15 AM | PLATINUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 1:43:15 AM | HYPE | UP | 1.8 min | -0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 1:41:22 AM | XRP | UP | 3.6 min | -0.291% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
