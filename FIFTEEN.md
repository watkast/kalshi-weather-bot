# 15-Minute 1¢ Study

*Updated Thu Oct 15, 7:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1498 finished bets | 1% | $86.40 | +52% | +5.77¢ | $31.60 / $54.80 |

*Expect about **87 buys a day** (~$13.03/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1403 | $58.20 | +38% |
| Momentum model ≥ 2%, hold to the close | 2339 | $9.40 | +3% |
| Volatility model ≥ 2%, hold to the close | 2706 | -$4.70 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19279 | 19263 | 76 (0%) | 1.07% | -$1,272.40 (-54%) | Hold to the close: -$1,272.40 (-54%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12444 | 4.5% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12444 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12444 | 7.4% | 0.4% (53) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12444 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2706 | 23 | -1% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1498 | 18 | +52% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 889 | 11 | +76% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2339 | 20 | +3% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1403 | 15 | +38% | -76% | -76% | -72% |
| Momentum model ≥ 10% | 942 | 10 | +49% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4614 | 33 | -22% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3161 | 26 | -9% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 2074 | 15 | -17% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12642 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4738 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1883 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19263 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 76 | 0% | -$1,272.40 | -54% | — |
| Sell at 2¢ | 684 | 4% | -$2,102.56 | -90% | 36 sec |
| Sell at 3¢ | 461 | 2% | -$2,100.61 | -90% | 47 sec |
| Sell at 5¢ | 336 | 2% | -$2,062.00 | -88% | 50 sec |
| Sell at 10¢ | 211 | 1% | -$1,975.99 | -85% | 63 sec |
| Sell at 25¢ | 123 | 1% | -$1,803.27 | -77% | 79 sec |
| Sell at 50¢ | 80 | 0% | -$1,600.40 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 613 | 5 | 11% | 3% | -22% | -81% | -86% |
| 2–5 min | 6224 | 36 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 5014 | 19 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7408 | 16 | 1% | 0% | -69% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1419 | 11 | 5% | 3% | -3% | -89% | -89% |
| HYPE | 1413 | 5 | 4% | 2% | -56% | -90% | -89% |
| ETH | 1409 | 8 | 5% | 3% | -31% | -88% | -87% |
| BNB | 1408 | 5 | 5% | 2% | -56% | -90% | -89% |
| DOGE | 1407 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1403 | 2 | 3% | 1% | -82% | -93% | -92% |
| XRP | 1396 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1394 | 7 | 5% | 2% | -33% | -88% | -91% |
| NEAR | 1393 | 8 | 5% | 3% | -25% | -78% | -78% |
| GOLD | 774 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 752 | 4 | 3% | 1% | -38% | -78% | -78% |
| WTI | 723 | 3 | 3% | 1% | -52% | -94% | -96% |
| COPPER | 667 | 1 | 2% | 1% | -86% | -97% | -96% |
| PLATINUM | 639 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 593 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 590 | 4 | 3% | 2% | -37% | -96% | -94% |
| EURUSD | 582 | 3 | 3% | 1% | -52% | -79% | -79% |
| GBPUSD | 545 | 1 | 2% | 1% | -83% | -97% | -97% |
| USDJPY | 502 | 3 | 1% | 1% | -44% | -99% | -98% |
| AUDUSD | 132 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 122 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9759 | 39 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9504 | 37 | 4% | 2% | -55% | -91% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2137 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2194 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3188 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3679 | 21 | 6% | 3% | -37% | -88% | -87% |
| Over 0.5% | 1441 | 6 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4396 | 24 | 4% | 2% | -37% | -91% | -90% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,464 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 7:27:42 AM | ZEC | UP | 2.3 min | -0.619% | — | In play | — |
| 10/15 7:27:26 AM | WTI | DOWN | 2.6 min | — | — | In play | — |
| 10/15 7:27:10 AM | BNB | UP | 2.8 min | -0.216% | — | In play | — |
| 10/15 7:26:54 AM | BTC | UP | 3.1 min | -0.253% | — | In play | — |
| 10/15 7:26:54 AM | SOL | UP | 3.1 min | -0.409% | — | In play | — |
| 10/15 7:26:39 AM | HYPE | UP | 3.4 min | -0.402% | — | In play | — |
| 10/15 7:26:39 AM | XRP | UP | 3.4 min | -0.416% | — | In play | — |
| 10/15 7:26:39 AM | DOGE | UP | 3.4 min | -0.457% | — | In play | — |
| 10/15 7:26:39 AM | ETH | UP | 3.4 min | -0.336% | — | In play | — |
| 10/15 7:14:56 AM | COPPER | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:41 AM | GOLD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:41 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:25 AM | XRP | DOWN | 34 sec | +0.146% | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:14:09 AM | USDJPY | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:09 AM | GBPUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:09 AM | EURUSD | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:14:09 AM | ETH | DOWN | 50 sec | +0.133% | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:13:53 AM | NEAR | DOWN | 67 sec | +0.516% | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:13:53 AM | BNB | DOWN | 67 sec | +0.202% | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:13:53 AM | SILVER | DOWN | 67 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:13:36 AM | SOL | DOWN | 84 sec | +0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:13:20 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 7:12:49 AM | ZEC | DOWN | 2.2 min | +0.505% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 7:12:49 AM | HYPE | UP | 2.2 min | -0.359% | 91¢ | ✅ Won | $14.00 |
| 10/15 7:12:34 AM | DOGE | UP | 2.4 min | -0.467% | 0¢ | ❌ Lost | $0.00 |
| 10/15 7:12:34 AM | BTC | UP | 2.4 min | -0.244% | 4¢ | ❌ Lost | -$0.15 |
| 10/15 7:11:46 AM | WTI | DOWN | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 6:59:56 AM | EURUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:59:41 AM | USDJPY | UP | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 6:59:25 AM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
