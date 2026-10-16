# 15-Minute 1¢ Study

*Updated Fri Oct 16, 9:21 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1627 finished bets | 1% | $85.70 | +48% | +5.27¢ | $37.95 / $47.75 |

*Expect about **89 buys a day** (~$13.29/day at risk); max loss per buy **15¢**.*

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
| 20917 | 20910 | 80 (0%) | 1.07% | -$1,426.40 (-56%) | Hold to the close: -$1,426.40 (-56%) |

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
| Volatility model | 13351 | 4.4% | 0.4% (54) | -639% | ❌ Worse |
| Momentum model | 13351 | 4.4% | 0.4% (54) | -662% | ❌ Worse |
| Mean-reversion model | 13351 | 7.4% | 0.4% (54) | -769% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13351 | 54 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 2965 | 24 | -6% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1627 | 19 | +48% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 952 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2545 | 21 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1510 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1006 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 5024 | 34 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3457 | 27 | -14% | -82% | -81% | -77% |
| Mean-reversion model ≥ 10% | 2269 | 16 | -19% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13549 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5199 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2162 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20910 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,426.40 | -56% | — |
| Sell at 2¢ | 744 | 4% | -$2,254.96 | -89% | 42 sec |
| Sell at 3¢ | 501 | 2% | -$2,253.01 | -88% | 47 sec |
| Sell at 5¢ | 363 | 2% | -$2,212.45 | -87% | 50 sec |
| Sell at 10¢ | 219 | 1% | -$2,133.51 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$1,961.34 | -77% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,748.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 695 | 5 | 10% | 3% | -32% | -82% | -86% |
| 2–5 min | 6777 | 37 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5443 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7991 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1521 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1517 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1511 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1507 | 2 | 4% | 2% | -83% | -90% | -90% |
| BNB | 1507 | 6 | 5% | 2% | -51% | -90% | -89% |
| SOL | 1504 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1497 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1494 | 7 | 5% | 2% | -38% | -88% | -91% |
| NEAR | 1491 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 850 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 823 | 4 | 3% | 1% | -44% | -79% | -79% |
| WTI | 792 | 3 | 3% | 1% | -56% | -94% | -96% |
| COPPER | 724 | 2 | 2% | 1% | -74% | -84% | -84% |
| PLATINUM | 708 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 652 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 650 | 5 | 2% | 2% | -28% | -82% | -80% |
| EURUSD | 643 | 3 | 3% | 1% | -56% | -81% | -81% |
| GBPUSD | 605 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 565 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 187 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 162 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10545 | 40 | 4% | 2% | -57% | -89% | -88% |
| DOWN (bought NO) | 10365 | 40 | 4% | 2% | -56% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2240 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2334 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3432 | 11 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 3973 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1567 | 6 | 7% | 3% | -60% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4927 | 27 | 4% | 2% | -37% | -87% | -86% |
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
| 10/16 9:14:57 AM | EURUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:14:41 AM | GBPUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:14:25 AM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:14:25 AM | GOLD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:13:22 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:13:06 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:13:06 AM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:49 AM | PLATINUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:33 AM | USDJPY | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:33 AM | ETH | UP | 2.4 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:01 AM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:12:01 AM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:10:54 AM | COPPER | UP | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 9:10:20 AM | DOGE | UP | 4.7 min | -0.946% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:49 AM | XRP | UP | 5.2 min | -0.881% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:49 AM | BNB | UP | 5.2 min | -0.483% | 7¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:32 AM | NEAR | UP | 5.5 min | -1.640% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:32 AM | HYPE | UP | 5.5 min | -0.847% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:16 AM | ZEC | UP | 5.7 min | -1.464% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 9:09:00 AM | BTC | UP | 6.0 min | -0.490% | 5¢ | ❌ Lost | -$0.15 |
| 10/16 9:07:54 AM | SOL | UP | 7.1 min | -1.002% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:55 AM | USDCAD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:55 AM | NATGAS | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:55 AM | WTI | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 8:59:08 AM | COPPER | DOWN | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:59:08 AM | GOLD | UP | 51 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:52 AM | GBPUSD | UP | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:36 AM | USDJPY | DOWN | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:58:04 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 8:56:26 AM | DOGE | UP | 3.5 min | -0.552% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
