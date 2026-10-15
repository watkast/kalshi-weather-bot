# 15-Minute 1¢ Study

*Updated Thu Oct 15, 12:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1472 finished bets | 1% | $89.10 | +55% | +6.05¢ | $33.10 / $56.00 |

*Expect about **87 buys a day** (~$13.00/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1378 | $60.75 | +41% |
| Momentum model ≥ 2%, hold to the close | 2292 | $14.50 | +5% |
| Volatility model ≥ 2%, hold to the close | 2640 | $3.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18961 | 18944 | 75 (0%) | 1.07% | -$1,246.35 (-54%) | Hold to the close: -$1,246.35 (-54%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12275 | 4.5% | 0.4% (52) | -637% | ❌ Worse |
| Momentum model | 12275 | 4.4% | 0.4% (52) | -662% | ❌ Worse |
| Mean-reversion model | 12275 | 7.3% | 0.4% (52) | -757% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12275 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2640 | 23 | +1% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1472 | 18 | +55% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 879 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2292 | 20 | +5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1378 | 15 | +41% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 926 | 10 | +52% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4532 | 32 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3099 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2035 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12473 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4651 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1820 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18944 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,246.35 | -54% | — |
| Sell at 2¢ | 662 | 3% | -$2,068.23 | -90% | 34 sec |
| Sell at 3¢ | 445 | 2% | -$2,066.80 | -90% | 46 sec |
| Sell at 5¢ | 325 | 2% | -$2,029.10 | -88% | 49 sec |
| Sell at 10¢ | 205 | 1% | -$1,943.80 | -85% | 63 sec |
| Sell at 25¢ | 119 | 1% | -$1,776.46 | -77% | 79 sec |
| Sell at 50¢ | 79 | 0% | -$1,567.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 598 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6119 | 35 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 4936 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7287 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1399 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1393 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1390 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1390 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1388 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1385 | 2 | 3% | 1% | -82% | -94% | -93% |
| BTC | 1377 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1376 | 7 | 2% | 1% | -37% | -85% | -86% |
| NEAR | 1375 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 758 | 1 | 4% | 1% | -85% | -92% | -94% |
| SILVER | 739 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 712 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 656 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 629 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 579 | 1 | 1% | 0% | -84% | -98% | -98% |
| NATGAS | 578 | 4 | 2% | 2% | -35% | -96% | -95% |
| EURUSD | 567 | 3 | 2% | 1% | -51% | -79% | -78% |
| GBPUSD | 532 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 487 | 3 | 1% | 1% | -43% | -99% | -98% |
| AUDUSD | 122 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 112 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9592 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9352 | 37 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2120 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2176 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3149 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3607 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1418 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4724 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,515 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 12:14:52 AM | ETH | DOWN | 7 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:14:36 AM | SILVER | DOWN | 23 sec | — | 0¢ | In play | — |
| 10/15 12:14:20 AM | DOGE | DOWN | 39 sec | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:14:04 AM | HYPE | UP | 56 sec | -0.173% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:14:04 AM | NEAR | UP | 56 sec | -0.440% | 0¢ | ❌ Lost | $0.00 |
| 10/15 12:13:45 AM | AUDUSD | UP | 74 sec | — | 0¢ | In play | — |
| 10/15 12:13:29 AM | BTC | DOWN | 1.5 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 12:13:29 AM | USDCAD | DOWN | 1.5 min | — | 0¢ | In play | — |
| 10/15 12:13:13 AM | PALLADIUM | UP | 1.8 min | — | 1¢ | In play | — |
| 10/15 12:13:13 AM | EURUSD | UP | 1.8 min | — | 0¢ | In play | — |
| 10/15 12:12:59 AM | PLATINUM | UP | 2.0 min | — | 0¢ | In play | — |
| 10/15 12:12:59 AM | ZEC | UP | 2.0 min | -0.680% | 1¢ | In play | — |
| 10/15 12:12:09 AM | GOLD | UP | 2.9 min | — | 1¢ | In play | — |
| 10/15 12:11:54 AM | USDJPY | DOWN | 3.1 min | — | 0¢ | In play | — |
| 10/15 12:10:50 AM | BNB | DOWN | 4.2 min | +0.281% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 12:10:40 AM | XRP | DOWN | 4.3 min | +0.487% | 3¢ | In play | — |
| 10/15 12:09:52 AM | SOL | DOWN | 5.1 min | +0.528% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:59:56 PM | SILVER | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:59:56 PM | GOLD | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:59:40 PM | PLATINUM | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:59:24 PM | GBPUSD | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:59:24 PM | PALLADIUM | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:59:08 PM | COPPER | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:58:19 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:57:47 PM | HYPE | UP | 2.2 min | -0.241% | 15¢ | ❌ Lost | -$0.15 |
| 10/14 11:57:47 PM | WTI | UP | 2.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:57:31 PM | USDJPY | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:56:59 PM | ZEC | UP | 3.0 min | -1.205% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:56:43 PM | NEAR | UP | 3.3 min | -0.826% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:55:16 PM | ETH | UP | 4.7 min | -0.526% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
