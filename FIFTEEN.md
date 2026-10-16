# 15-Minute 1¢ Study

*Updated Fri Oct 16, 12:45 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1589 finished bets | 1% | $75.45 | +43% | +4.75¢ | $26.35 / $49.10 |

*Expect about **88 buys a day** (~$13.25/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1478 | $49.80 | +31% |
| Momentum model ≥ 2%, hold to the close | 2483 | -$8.00 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1589 | -$19.80 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20361 | 20342 | 79 (0%) | 1.07% | -$1,368.40 (-55%) | Hold to the close: -$1,368.40 (-55%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13054 | 4.4% | 0.4% (53) | -639% | ❌ Worse |
| Momentum model | 13054 | 4.4% | 0.4% (53) | -663% | ❌ Worse |
| Mean-reversion model | 13054 | 7.4% | 0.4% (53) | -764% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13054 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2895 | 23 | -8% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1589 | 18 | +43% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 933 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2483 | 20 | -3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1478 | 15 | +31% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 989 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4901 | 33 | -27% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3367 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2205 | 15 | -22% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13252 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5033 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2057 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20342 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,368.40 | -55% | — |
| Sell at 2¢ | 718 | 4% | -$2,189.72 | -88% | 42 sec |
| Sell at 3¢ | 481 | 2% | -$2,188.81 | -88% | 47 sec |
| Sell at 5¢ | 350 | 2% | -$2,148.90 | -87% | 50 sec |
| Sell at 10¢ | 216 | 1% | -$2,065.44 | -83% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,892.65 | -76% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,682.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6606 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5292 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7780 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1488 | 11 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1483 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1477 | 8 | 5% | 3% | -34% | -88% | -87% |
| DOGE | 1474 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1474 | 5 | 4% | 2% | -58% | -90% | -90% |
| SOL | 1470 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1464 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1463 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1459 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 819 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 799 | 4 | 3% | 1% | -42% | -79% | -79% |
| WTI | 770 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 704 | 2 | 2% | 1% | -73% | -84% | -83% |
| PLATINUM | 681 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 630 | 5 | 2% | 2% | -26% | -81% | -80% |
| PALLADIUM | 630 | 2 | 1% | 0% | -70% | -83% | -84% |
| EURUSD | 621 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 580 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 545 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 166 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 145 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10255 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10087 | 40 | 4% | 2% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2202 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2291 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3347 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3878 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1531 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5017 | 20 | 4% | 2% | -55% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,466 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 12:44:48 AM | USDCAD | UP | 12 sec | — | 0¢ | In play | — |
| 10/16 12:44:48 AM | AUDUSD | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/16 12:44:48 AM | GOLD | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/16 12:44:48 AM | EURUSD | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/16 12:44:48 AM | PALLADIUM | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/16 12:44:32 AM | USDJPY | DOWN | 28 sec | — | 0¢ | In play | — |
| 10/16 12:44:17 AM | COPPER | DOWN | 42 sec | — | 0¢ | In play | — |
| 10/16 12:44:17 AM | PLATINUM | DOWN | 42 sec | — | 0¢ | In play | — |
| 10/16 12:43:13 AM | SILVER | DOWN | 1.8 min | — | 1¢ | In play | — |
| 10/16 12:42:57 AM | DOGE | DOWN | 2.0 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:42:09 AM | HYPE | DOWN | 2.9 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:42:09 AM | ZEC | DOWN | 2.9 min | +0.423% | 0¢ | ❌ Lost | $0.00 |
| 10/16 12:41:52 AM | BTC | DOWN | 3.1 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:41:52 AM | ETH | DOWN | 3.1 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:41:20 AM | XRP | DOWN | 3.6 min | +0.307% | 1¢ | In play | — |
| 10/16 12:41:04 AM | SOL | DOWN | 3.9 min | +0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:40:46 AM | BNB | DOWN | 4.2 min | +0.108% | 1¢ | In play | — |
| 10/16 12:40:14 AM | NEAR | DOWN | 4.8 min | +0.630% | 1¢ | In play | — |
| 10/16 12:29:15 AM | BNB | UP | 44 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:59 AM | SILVER | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:59 AM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:43 AM | ZEC | DOWN | 76 sec | +0.352% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:43 AM | NEAR | UP | 76 sec | -0.408% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:27 AM | USDJPY | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:27 AM | AUDUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:27 AM | PLATINUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:11 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:28:11 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 12:27:55 AM | BTC | DOWN | 2.1 min | +0.096% | 18¢ | ❌ Lost | -$0.15 |
| 10/16 12:27:39 AM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
