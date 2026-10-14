# 15-Minute 1¢ Study

*Updated Wed Oct 14, 2:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1416 finished bets | 1% | $81.85 | +52% | +5.78¢ | $35.95 / $45.90 |

*Expect about **85 buys a day** (~$12.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1331 | $52.60 | +37% |
| Momentum model ≥ 2%, hold to the close | 2201 | $11.60 | +5% |
| Volatility model ≥ 2%, hold to the close | 2537 | $1.85 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18327 | 18314 | 70 (0%) | 1.07% | -$1,239.55 (-56%) | Hold to the close: -$1,239.55 (-56%) |

*In play or awaiting result: 12. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11927 | 4.5% | 0.4% (50) | -647% | ❌ Worse |
| Momentum model | 11927 | 4.4% | 0.4% (50) | -671% | ❌ Worse |
| Mean-reversion model | 11927 | 7.3% | 0.4% (50) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11927 | 50 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2537 | 22 | +1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1416 | 17 | +52% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 853 | 10 | +67% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2201 | 19 | +5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1331 | 14 | +37% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 897 | 9 | +42% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4375 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2995 | 23 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1974 | 14 | -18% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12125 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4484 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1705 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18314 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 70 | 0% | -$1,239.55 | -56% | — |
| Sell at 2¢ | 639 | 3% | -$2,011.41 | -91% | 34 sec |
| Sell at 3¢ | 431 | 2% | -$2,009.46 | -91% | 46 sec |
| Sell at 5¢ | 315 | 2% | -$1,972.80 | -89% | 49 sec |
| Sell at 10¢ | 199 | 1% | -$1,888.86 | -85% | 63 sec |
| Sell at 25¢ | 115 | 1% | -$1,740.90 | -78% | 79 sec |
| Sell at 50¢ | 76 | 0% | -$1,538.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 576 | 4 | 10% | 2% | -34% | -82% | -88% |
| 2–5 min | 5905 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4785 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7044 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1359 | 10 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1355 | 4 | 4% | 2% | -63% | -90% | -89% |
| ETH | 1352 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1351 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1350 | 5 | 5% | 2% | -55% | -90% | -89% |
| SOL | 1347 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1338 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1337 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1336 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 727 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 715 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 682 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 634 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 607 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 563 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 556 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 540 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 508 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 462 | 3 | 1% | 1% | -39% | -98% | -98% |
| AUDUSD | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 91 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9242 | 35 | 3% | 2% | -56% | -90% | -89% |
| DOWN (bought NO) | 9072 | 35 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2090 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2138 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3081 | 10 | 4% | 2% | -60% | -91% | -90% |
| 0.2–0.5% | 3464 | 20 | 6% | 3% | -36% | -88% | -88% |
| Over 0.5% | 1349 | 5 | 6% | 2% | -61% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4264 | 12 | 3% | 1% | -67% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,492 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 2:28:37 PM | NATGAS | DOWN | 83 sec | — | — | In play | — |
| 10/14 2:28:21 PM | ZEC | UP | 1.6 min | -0.376% | — | In play | — |
| 10/14 2:28:06 PM | ETH | UP | 1.9 min | -0.156% | — | In play | — |
| 10/14 2:28:06 PM | XRP | UP | 1.9 min | -0.234% | — | In play | — |
| 10/14 2:28:06 PM | COPPER | DOWN | 1.9 min | — | — | In play | — |
| 10/14 2:27:49 PM | HYPE | UP | 2.2 min | -0.263% | — | In play | — |
| 10/14 2:14:44 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:44 PM | USDJPY | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:28 PM | ETH | DOWN | 32 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:14:28 PM | SILVER | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:28 PM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:28 PM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:28 PM | BNB | DOWN | 32 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:14:13 PM | NEAR | DOWN | 46 sec | +0.350% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:14:13 PM | AUDUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:13 PM | SOL | DOWN | 46 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:14:13 PM | HYPE | UP | 46 sec | -0.160% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:14:13 PM | GBPUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:13:57 PM | USDCAD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:13:57 PM | PALLADIUM | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:12:37 PM | BTC | DOWN | 2.4 min | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:11:30 PM | ZEC | DOWN | 3.5 min | +0.176% | 90¢ | ✅ Won | $14.00 |
| 10/14 2:11:30 PM | XRP | DOWN | 3.5 min | +0.295% | 2¢ | ❌ Lost | -$0.15 |
| 10/14 2:10:11 PM | DOGE | DOWN | 4.8 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:48 PM | BTC | DOWN | 11 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:59:48 PM | SILVER | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:48 PM | GOLD | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:48 PM | PALLADIUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 1:59:16 PM | ETH | UP | 43 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/14 1:59:16 PM | DOGE | UP | 43 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
