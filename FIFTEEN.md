# 15-Minute 1¢ Study

*Updated Wed Oct 14, 11:35 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1472 finished bets | 1% | $89.10 | +55% | +6.05¢ | $33.10 / $56.00 |

*Expect about **87 buys a day** (~$13.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1378 | $60.75 | +41% |
| Momentum model ≥ 2%, hold to the close | 2291 | $14.50 | +5% |
| Volatility model ≥ 2%, hold to the close | 2640 | $3.10 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18909 | 18902 | 75 (0%) | 1.07% | -$1,242.00 (-54%) | Hold to the close: -$1,242.00 (-54%) |

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
| Volatility model | 12250 | 4.5% | 0.4% (52) | -637% | ❌ Worse |
| Momentum model | 12250 | 4.4% | 0.4% (52) | -663% | ❌ Worse |
| Mean-reversion model | 12250 | 7.3% | 0.4% (52) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12250 | 52 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2640 | 23 | +1% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1472 | 18 | +55% | -73% | -71% | -67% |
| Volatility model ≥ 10% | 879 | 11 | +78% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2291 | 20 | +5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1378 | 15 | +41% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 926 | 10 | +52% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4527 | 32 | -23% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3096 | 25 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2034 | 14 | -21% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12448 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4638 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1816 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18902 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 75 | 0% | -$1,242.00 | -54% | — |
| Sell at 2¢ | 661 | 3% | -$2,064.14 | -90% | 34 sec |
| Sell at 3¢ | 444 | 2% | -$2,062.84 | -90% | 46 sec |
| Sell at 5¢ | 324 | 2% | -$2,025.40 | -88% | 49 sec |
| Sell at 10¢ | 204 | 1% | -$1,940.76 | -85% | 63 sec |
| Sell at 25¢ | 119 | 1% | -$1,772.11 | -77% | 79 sec |
| Sell at 50¢ | 79 | 0% | -$1,562.75 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 595 | 5 | 10% | 3% | -20% | -82% | -87% |
| 2–5 min | 6107 | 35 | 7% | 3% | -43% | -88% | -88% |
| 1–2 min | 4928 | 19 | 3% | 2% | -58% | -94% | -93% |
| Under 1 min | 7268 | 16 | 1% | 0% | -68% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1397 | 11 | 5% | 3% | -2% | -89% | -89% |
| HYPE | 1390 | 4 | 4% | 2% | -65% | -90% | -89% |
| ETH | 1387 | 8 | 5% | 3% | -30% | -88% | -87% |
| BNB | 1387 | 5 | 4% | 2% | -56% | -90% | -89% |
| DOGE | 1385 | 2 | 4% | 2% | -82% | -91% | -90% |
| SOL | 1382 | 2 | 3% | 1% | -82% | -94% | -93% |
| BTC | 1374 | 7 | 5% | 2% | -32% | -88% | -91% |
| XRP | 1374 | 7 | 2% | 1% | -37% | -85% | -86% |
| NEAR | 1372 | 8 | 5% | 2% | -24% | -78% | -78% |
| GOLD | 756 | 1 | 4% | 1% | -84% | -92% | -94% |
| SILVER | 737 | 4 | 3% | 1% | -37% | -78% | -78% |
| WTI | 710 | 3 | 3% | 1% | -51% | -94% | -96% |
| COPPER | 654 | 1 | 2% | 2% | -86% | -97% | -96% |
| PLATINUM | 627 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 577 | 4 | 2% | 2% | -35% | -96% | -95% |
| PALLADIUM | 577 | 1 | 1% | 0% | -84% | -98% | -98% |
| EURUSD | 566 | 3 | 2% | 1% | -51% | -79% | -78% |
| GBPUSD | 530 | 1 | 2% | 1% | -82% | -97% | -97% |
| USDJPY | 486 | 3 | 1% | 1% | -42% | -99% | -98% |
| AUDUSD | 122 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 112 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9563 | 38 | 3% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9339 | 37 | 4% | 2% | -54% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2120 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2173 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3144 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3599 | 20 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1409 | 6 | 6% | 2% | -56% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5374 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,519 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 11:29:55 PM | WTI | DOWN | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:29:55 PM | ZEC | UP | 4 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:29:55 PM | NATGAS | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:55 PM | PALLADIUM | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:39 PM | EURUSD | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:39 PM | USDCAD | DOWN | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:29:23 PM | USDJPY | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:28:35 PM | GBPUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:28:19 PM | BTC | UP | 1.7 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:28:03 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:47 PM | GOLD | UP | 2.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:47 PM | DOGE | UP | 2.2 min | -0.353% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:31 PM | ETH | UP | 2.5 min | -0.210% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:27:31 PM | HYPE | DOWN | 2.5 min | +0.302% | 2¢ | ❌ Lost | $0.00 |
| 10/14 11:27:15 PM | BNB | UP | 2.8 min | -0.150% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:26:59 PM | PLATINUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:26:59 PM | NEAR | UP | 3.0 min | -0.734% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:26:59 PM | XRP | UP | 3.0 min | -0.412% | 0¢ | ❌ Lost | $0.00 |
| 10/14 11:26:42 PM | SOL | UP | 3.3 min | -0.522% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:26:10 PM | SILVER | UP | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:55 PM | EURUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:14:55 PM | USDJPY | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:12:13 PM | PALLADIUM | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:12:13 PM | NEAR | UP | 2.8 min | -0.817% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:36 PM | HYPE | UP | 4.4 min | -0.533% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:36 PM | BTC | UP | 4.4 min | -0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:04 PM | DOGE | UP | 4.9 min | -0.667% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:04 PM | BNB | UP | 4.9 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:04 PM | ETH | UP | 4.9 min | -0.605% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 11:10:04 PM | XRP | UP | 4.9 min | -0.923% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
