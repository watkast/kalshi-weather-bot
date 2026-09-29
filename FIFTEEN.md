# 15-Minute 1¢ Study

*Updated Mon Sep 28, 7:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 165 finished bets | 2% | $20.55 | +96% | +12.45¢ | $17.50 / $3.05 |

*Expect **165 buys in the first 19 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 50 | $20.50 | +273% |
| Mean-reversion model ≥ 2%, hold to the close | 252 | $9.60 | +30% |
| 5+ min left, sell at 50¢ | 50 | $6.00 | +80% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1343 | 1337 | 8 (1%) | 1.07% | -$50.30 (-31%) | Hold to the close: -$50.30 (-31%) |

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
| Volatility model | 651 | 3.0% | 0.6% (4) | -341% | ❌ Worse |
| Momentum model | 651 | 3.1% | 0.6% (4) | -416% | ❌ Worse |
| Mean-reversion model | 651 | 6.0% | 0.6% (4) | -382% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 651 | 4 | -22% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 123 | 1 | -3% | -87% | -86% | -82% |
| Volatility model ≥ 5% | 59 | 0 | -100% | -76% | -76% | -70% |
| Volatility model ≥ 10% | 31 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 105 | 0 | -100% | -85% | -90% | -89% |
| Momentum model ≥ 5% | 61 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 42 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 252 | 3 | +30% | -87% | -88% | -84% |
| Mean-reversion model ≥ 5% | 165 | 3 | +96% | -85% | -85% | -79% |
| Mean-reversion model ≥ 10% | 104 | 2 | +117% | -82% | -82% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 846 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 417 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 74 | 4% | 4% | 3% | 3% | 3% | 3% |
| **All** | 1337 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$50.30 | -31% | — |
| Sell at 2¢ | 44 | 3% | -$150.86 | -93% | 47 sec |
| Sell at 3¢ | 28 | 2% | -$151.38 | -93% | 55 sec |
| Sell at 5¢ | 19 | 1% | -$149.95 | -92% | 81 sec |
| Sell at 10¢ | 17 | 1% | -$140.03 | -86% | 1.9 min |
| Sell at 25¢ | 11 | 1% | -$125.89 | -78% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$108.30 | -67% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 50 | 2 | 6% | 4% | +273% | -90% | -84% |
| 2–5 min | 464 | 5 | 6% | 3% | +5% | -88% | -90% |
| 1–2 min | 384 | 1 | 2% | 1% | -72% | -96% | -96% |
| Under 1 min | 439 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 97 | 2 | 5% | 3% | +156% | -88% | -86% |
| DOGE | 96 | 1 | 4% | 2% | +21% | -91% | -86% |
| ZEC | 96 | 1 | 6% | 2% | +28% | -86% | -93% |
| XRP | 95 | 2 | 4% | 3% | +167% | -90% | -89% |
| NEAR | 94 | 0 | 2% | 1% | -100% | -94% | -96% |
| BTC | 94 | 0 | 9% | 2% | -100% | -79% | -88% |
| SOL | 93 | 0 | 3% | 2% | -100% | -92% | -87% |
| BNB | 92 | 0 | 1% | 0% | -100% | -98% | -97% |
| HYPE | 89 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 73 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 68 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 67 | 0 | 1% | 0% | -100% | -97% | -95% |
| NATGAS | 59 | 0 | 3% | 2% | -100% | -94% | -91% |
| COPPER | 55 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 54 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 41 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 27 | 0 | 4% | 0% | -100% | -94% | -90% |
| EURUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 22 | 2 | 9% | 9% | +748% | -84% | -76% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 725 | 5 | 4% | 2% | -20% | -92% | -92% |
| DOWN (bought NO) | 612 | 3 | 3% | 1% | -44% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 83 | 0 | 4% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 87 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 180 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 337 | 2 | 5% | 3% | -35% | -90% | -91% |
| Over 0.5% | 159 | 4 | 6% | 3% | +171% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 361 | 2 | 4% | 2% | -37% | -92% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,971 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 7:29:23 PM | NATGAS | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:07 PM | SILVER | UP | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:29:07 PM | COPPER | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:51 PM | GOLD | DOWN | 68 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:36 PM | PALLADIUM | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:36 PM | NEAR | UP | 83 sec | -0.769% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:20 PM | XRP | UP | 1.6 min | -0.587% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:20 PM | BTC | UP | 1.6 min | -0.151% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:28:20 PM | WTI | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:48 PM | ETH | UP | 2.2 min | -0.238% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:16 PM | DOGE | UP | 2.7 min | -0.623% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:16 PM | SOL | UP | 2.7 min | -0.550% | 0¢ | ❌ Lost | $0.00 |
| 9/28 7:27:16 PM | USDJPY | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:16 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:16 PM | BNB | UP | 2.7 min | -0.283% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:27:00 PM | HYPE | UP | 3.0 min | -0.446% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:26:12 PM | ZEC | UP | 3.8 min | -1.765% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:35 PM | EURUSD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:35 PM | GOLD | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:19 PM | USDJPY | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:19 PM | PLATINUM | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:19 PM | SILVER | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:14:03 PM | COPPER | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:12:12 PM | XRP | UP | 2.8 min | -0.591% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 7:12:12 PM | HYPE | UP | 2.8 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:12:12 PM | NEAR | UP | 2.8 min | -0.820% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:11:56 PM | DOGE | UP | 3.1 min | -0.613% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:11:56 PM | BTC | UP | 3.1 min | -0.241% | 3¢ | ❌ Lost | -$0.15 |
| 9/28 7:11:40 PM | BNB | UP | 3.3 min | -0.256% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 7:11:40 PM | ZEC | UP | 3.3 min | -1.377% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
