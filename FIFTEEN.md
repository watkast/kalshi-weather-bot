# 15-Minute 1¢ Study

*Updated Fri Oct 16, 12:14 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1586 finished bets | 1% | $75.90 | +43% | +4.79¢ | $26.50 / $49.40 |

*Expect about **88 buys a day** (~$13.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1472 | $50.70 | +32% |
| Momentum model ≥ 2%, hold to the close | 2475 | -$6.80 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1586 | -$19.35 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20325 | 20301 | 79 (0%) | 1.07% | -$1,362.40 (-55%) | Hold to the close: -$1,362.40 (-55%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13030 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 13030 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 13030 | 7.3% | 0.4% (53) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13030 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2888 | 23 | -8% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1586 | 18 | +43% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 932 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2475 | 20 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1472 | 15 | +32% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 985 | 10 | +42% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4891 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3361 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2201 | 15 | -22% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13228 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5021 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2052 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20301 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,362.40 | -55% | — |
| Sell at 2¢ | 716 | 4% | -$2,184.24 | -88% | 42 sec |
| Sell at 3¢ | 479 | 2% | -$2,183.59 | -88% | 47 sec |
| Sell at 5¢ | 349 | 2% | -$2,143.55 | -87% | 50 sec |
| Sell at 10¢ | 215 | 1% | -$2,060.75 | -83% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,886.65 | -76% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,676.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6583 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5279 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7775 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1485 | 11 | 5% | 3% | -8% | -89% | -89% |
| HYPE | 1480 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1474 | 8 | 5% | 3% | -34% | -88% | -86% |
| BNB | 1472 | 5 | 4% | 2% | -58% | -90% | -90% |
| DOGE | 1471 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1467 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1462 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1460 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1457 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 817 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 797 | 4 | 3% | 1% | -42% | -79% | -79% |
| WTI | 769 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 702 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 679 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 629 | 5 | 2% | 2% | -26% | -81% | -80% |
| PALLADIUM | 628 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 620 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 579 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 543 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 165 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 145 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10237 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10064 | 40 | 4% | 2% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2201 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2288 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3340 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3865 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1531 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,465 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 12:14:54 AM | ZEC | DOWN | 5 sec | -0.056% | — | In play | — |
| 10/16 12:14:22 AM | HYPE | UP | 37 sec | -0.055% | — | In play | — |
| 10/16 12:14:06 AM | USDJPY | DOWN | 54 sec | — | — | In play | — |
| 10/16 12:14:06 AM | GOLD | UP | 54 sec | — | — | In play | — |
| 10/16 12:13:50 AM | WTI | DOWN | 70 sec | — | — | In play | — |
| 10/16 12:13:18 AM | NATGAS | UP | 1.7 min | — | — | In play | — |
| 10/16 12:13:01 AM | DOGE | UP | 2.0 min | -0.213% | — | In play | — |
| 10/16 12:13:01 AM | NEAR | UP | 2.0 min | -0.492% | — | In play | — |
| 10/16 12:12:45 AM | COPPER | UP | 2.2 min | — | — | In play | — |
| 10/16 12:12:45 AM | SILVER | UP | 2.2 min | — | — | In play | — |
| 10/16 12:12:13 AM | BNB | UP | 2.8 min | -0.166% | — | In play | — |
| 10/16 12:12:13 AM | SOL | UP | 2.8 min | -0.249% | — | In play | — |
| 10/16 12:12:13 AM | PLATINUM | UP | 2.8 min | — | — | In play | — |
| 10/16 12:11:39 AM | XRP | UP | 3.4 min | -0.224% | — | In play | — |
| 10/16 12:11:07 AM | BTC | UP | 3.9 min | -0.148% | — | In play | — |
| 10/16 12:10:52 AM | ETH | UP | 4.1 min | -0.244% | — | In play | — |
| 10/16 12:10:52 AM | PALLADIUM | UP | 4.1 min | — | — | In play | — |
| 10/15 11:59:59 PM | PALLADIUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:43 PM | GOLD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:43 PM | SILVER | DOWN | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:59:27 PM | NEAR | DOWN | 32 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:59:11 PM | COPPER | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:59:11 PM | WTI | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:58:39 PM | BNB | DOWN | 80 sec | +0.038% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:58:23 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:57:35 PM | NATGAS | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:57:35 PM | ZEC | DOWN | 2.4 min | +0.297% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:57:19 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:57:03 PM | HYPE | DOWN | 2.9 min | +0.270% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:56:48 PM | ETH | DOWN | 3.2 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
