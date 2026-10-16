# 15-Minute 1¢ Study

*Updated Fri Oct 16, 9:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1627 finished bets | 1% | $85.70 | +48% | +5.27¢ | $37.95 / $47.75 |

*Expect about **89 buys a day** (~$13.30/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1510 | $46.80 | +29% |
| Momentum model ≥ 2%, hold to the close | 2545 | -$0.75 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1627 | -$16.80 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20905 | 20889 | 80 (0%) | 1.07% | -$1,423.25 (-56%) | Hold to the close: -$1,423.25 (-56%) |

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
| Volatility model | 13342 | 4.4% | 0.4% (54) | -639% | ❌ Worse |
| Momentum model | 13342 | 4.4% | 0.4% (54) | -663% | ❌ Worse |
| Mean-reversion model | 13342 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13342 | 54 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2965 | 24 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1627 | 19 | +48% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 952 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2545 | 21 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1510 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1006 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5017 | 34 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3453 | 27 | -14% | -82% | -81% | -77% |
| Mean-reversion model ≥ 10% | 2268 | 16 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13540 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5192 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2157 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20889 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,423.25 | -56% | — |
| Sell at 2¢ | 742 | 4% | -$2,252.33 | -89% | 42 sec |
| Sell at 3¢ | 499 | 2% | -$2,250.64 | -88% | 47 sec |
| Sell at 5¢ | 361 | 2% | -$2,210.60 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,130.36 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,958.19 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,745.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 688 | 5 | 10% | 3% | -31% | -82% | -86% |
| 2–5 min | 6770 | 37 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5440 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7987 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1520 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1516 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1510 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1506 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1506 | 6 | 5% | 2% | -51% | -90% | -90% |
| SOL | 1503 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1496 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1493 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1490 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 849 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 822 | 4 | 3% | 1% | -44% | -79% | -79% |
| WTI | 791 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 723 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 707 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 651 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 649 | 5 | 2% | 2% | -28% | -82% | -80% |
| EURUSD | 642 | 3 | 3% | 1% | -56% | -81% | -81% |
| GBPUSD | 604 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 564 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 186 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 161 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10526 | 40 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10363 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2240 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2334 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3432 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3970 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1561 | 6 | 7% | 3% | -60% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4906 | 27 | 4% | 2% | -36% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,417 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 9:10:54 AM | COPPER | UP | 4.1 min | — | — | In play | — |
| 10/16 9:10:20 AM | DOGE | UP | 4.7 min | -0.946% | — | In play | — |
| 10/16 9:09:49 AM | XRP | UP | 5.2 min | -0.881% | — | In play | — |
| 10/16 9:09:49 AM | BNB | UP | 5.2 min | -0.483% | — | In play | — |
| 10/16 9:09:32 AM | NEAR | UP | 5.5 min | -1.640% | — | In play | — |
| 10/16 9:09:32 AM | HYPE | UP | 5.5 min | -0.847% | — | In play | — |
| 10/16 9:09:16 AM | ZEC | UP | 5.7 min | -1.464% | — | In play | — |
| 10/16 9:09:00 AM | BTC | UP | 6.0 min | -0.490% | — | In play | — |
| 10/16 9:07:54 AM | SOL | UP | 7.1 min | -1.002% | — | In play | — |
| 10/16 8:59:55 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:55 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:55 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:59:08 AM | COPPER | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:08 AM | GOLD | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:52 AM | GBPUSD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:36 AM | USDJPY | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:04 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:56:26 AM | DOGE | UP | 3.5 min | -0.552% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:55:54 AM | PLATINUM | DOWN | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:55:37 AM | NEAR | UP | 4.4 min | -1.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:55:37 AM | BTC | UP | 4.4 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:55:05 AM | ETH | UP | 4.9 min | -0.501% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:55:05 AM | BNB | UP | 4.9 min | -0.295% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:54:32 AM | XRP | UP | 5.5 min | -0.680% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:54:32 AM | SOL | UP | 5.5 min | -0.652% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:54:32 AM | ZEC | UP | 5.5 min | -1.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:54:32 AM | HYPE | UP | 5.5 min | -0.657% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:44:58 AM | XRP | UP | 1 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:44:58 AM | USDCAD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:44:58 AM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
