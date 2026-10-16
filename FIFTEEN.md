# 15-Minute 1¢ Study

*Updated Fri Oct 16, 4:20 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1606 finished bets | 1% | $73.80 | +41% | +4.60¢ | $39.15 / $34.65 |

*Expect about **88 buys a day** (~$13.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1493 | $48.30 | +30% |
| Momentum model ≥ 2%, hold to the close | 2509 | -$10.85 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1606 | -$21.45 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20583 | 20576 | 79 (0%) | 1.07% | -$1,398.10 (-56%) | Hold to the close: -$1,398.10 (-56%) |

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
| Volatility model | 13176 | 4.4% | 0.4% (53) | -645% | ❌ Worse |
| Momentum model | 13176 | 4.4% | 0.4% (53) | -668% | ❌ Worse |
| Mean-reversion model | 13176 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13176 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2922 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1606 | 18 | +41% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 941 | 11 | +66% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2509 | 20 | -4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1493 | 15 | +30% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 997 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4938 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3394 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2223 | 15 | -23% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13374 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5096 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2106 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20576 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,398.10 | -56% | — |
| Sell at 2¢ | 725 | 4% | -$2,217.60 | -89% | 42 sec |
| Sell at 3¢ | 485 | 2% | -$2,216.95 | -89% | 47 sec |
| Sell at 5¢ | 353 | 2% | -$2,176.65 | -87% | 50 sec |
| Sell at 10¢ | 217 | 1% | -$2,093.83 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,922.35 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,712.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 664 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6668 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5361 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7879 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1501 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1497 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1491 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1487 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1487 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1484 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1479 | 7 | 3% | 1% | -42% | -86% | -87% |
| BTC | 1475 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1473 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 832 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 809 | 4 | 3% | 1% | -43% | -79% | -80% |
| WTI | 775 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 711 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 691 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 641 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 637 | 5 | 2% | 2% | -27% | -81% | -80% |
| EURUSD | 633 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 592 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 555 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 174 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 152 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10372 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10204 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2225 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2316 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3390 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3904 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1536 | 6 | 6% | 2% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5251 | 20 | 4% | 2% | -57% | -88% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,438 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 4:14:13 AM | USDJPY | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:13:26 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:13:26 AM | AUDUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:13:26 AM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:13:10 AM | SILVER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:12:54 AM | PALLADIUM | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:12:54 AM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:12:38 AM | PLATINUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:12:38 AM | GOLD | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:11:16 AM | BTC | UP | 3.7 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:11:16 AM | ETH | UP | 3.7 min | -0.208% | 2¢ | ❌ Lost | -$0.15 |
| 10/16 4:10:45 AM | EURUSD | DOWN | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 4:10:29 AM | BNB | UP | 4.5 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:10:29 AM | ZEC | UP | 4.5 min | -0.500% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:10:29 AM | NEAR | UP | 4.5 min | -0.520% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 4:09:41 AM | XRP | UP | 5.3 min | -0.389% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:09:25 AM | SOL | UP | 5.6 min | -0.413% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:08:21 AM | HYPE | UP | 6.7 min | -0.540% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 4:08:21 AM | DOGE | UP | 6.7 min | -0.410% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:59:31 AM | EURUSD | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:59:15 AM | NATGAS | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:59 AM | GOLD | UP | 61 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:59 AM | DOGE | UP | 61 sec | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:59 AM | ETH | UP | 61 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:58:40 AM | HYPE | UP | 79 sec | -0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:40 AM | BTC | UP | 79 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:58:24 AM | SOL | UP | 1.6 min | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:24 AM | ZEC | UP | 1.6 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:24 AM | USDCAD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:58:24 AM | XRP | UP | 1.6 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
