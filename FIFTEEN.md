# 15-Minute 1¢ Study

*Updated Fri Oct 16, 7:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1616 finished bets | 1% | $72.60 | +40% | +4.49¢ | $38.55 / $34.05 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1501 | $47.40 | +29% |
| Momentum model ≥ 2%, hold to the close | 2531 | -$13.40 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1616 | -$22.65 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20756 | 20749 | 79 (0%) | 1.07% | -$1,420.90 (-56%) | Hold to the close: -$1,420.90 (-56%) |

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
| Volatility model | 13271 | 4.4% | 0.4% (53) | -644% | ❌ Worse |
| Momentum model | 13271 | 4.4% | 0.4% (53) | -667% | ❌ Worse |
| Mean-reversion model | 13271 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13271 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2951 | 23 | -10% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1616 | 18 | +40% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 947 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2531 | 20 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1501 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1001 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4991 | 33 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3432 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2253 | 15 | -24% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13469 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5150 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2130 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20749 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,420.90 | -56% | — |
| Sell at 2¢ | 734 | 4% | -$2,238.06 | -89% | 42 sec |
| Sell at 3¢ | 492 | 2% | -$2,237.02 | -89% | 47 sec |
| Sell at 5¢ | 357 | 2% | -$2,196.85 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,115.32 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,945.15 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,735.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 680 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6734 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5408 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7923 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1512 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1508 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1502 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1498 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1498 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1495 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1489 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1485 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1482 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 842 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 817 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 784 | 3 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 717 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 700 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 646 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 644 | 5 | 2% | 2% | -28% | -81% | -80% |
| EURUSD | 638 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 597 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 559 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 180 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 156 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10461 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10288 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2227 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2327 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3412 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3953 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1547 | 6 | 6% | 3% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4766 | 26 | 4% | 2% | -37% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,429 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
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
| 10/16 6:53:16 AM | ETH | UP | 6.7 min | -0.375% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:53:16 AM | NEAR | UP | 6.7 min | -1.095% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 6:53:16 AM | DOGE | UP | 6.7 min | -0.543% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:55 AM | AUDUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:55 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:23 AM | NEAR | UP | 37 sec | -0.168% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:23 AM | ZEC | UP | 37 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:07 AM | DOGE | UP | 53 sec | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:50 AM | BTC | UP | 69 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:43:50 AM | XRP | UP | 69 sec | -0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:50 AM | BNB | UP | 69 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:43:34 AM | ETH | UP | 85 sec | -0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:18 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:18 AM | GBPUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:42:46 AM | SOL | UP | 2.2 min | -0.222% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
