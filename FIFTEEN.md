# 15-Minute 1¢ Study

*Updated Mon Sep 28, 10:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 88 finished bets | 2% | $16.90 | +152% | +19.20¢ | $8.45 / $8.45 |

*Expect **88 buys in the first 9 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 137 | $10.60 | +61% |
| Volatility model ≥ 2%, hold to the close | 66 | $6.20 | +79% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 88 | $2.40 | +22% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 827 | 821 | 4 (0%) | 1.07% | -$41.65 (-43%) | Hold to the close: -$41.65 (-43%) |

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
| Volatility model | 336 | 3.8% | 0.6% (2) | -506% | ❌ Worse |
| Momentum model | 336 | 4.0% | 0.6% (2) | -615% | ❌ Worse |
| Mean-reversion model | 336 | 6.7% | 0.6% (2) | -520% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 336 | 2 | -21% | -88% | -90% | -87% |
| Volatility model ≥ 2% | 66 | 1 | +79% | -83% | -80% | -75% |
| Volatility model ≥ 5% | 33 | 0 | -100% | -72% | -69% | -65% |
| Volatility model ≥ 10% | 18 | 0 | -100% | -86% | -78% | -64% |
| Momentum model ≥ 2% | 60 | 0 | -100% | -85% | -89% | -91% |
| Momentum model ≥ 5% | 36 | 0 | -100% | -80% | -90% | -83% |
| Momentum model ≥ 10% | 24 | 0 | -100% | -89% | -84% | -73% |
| Mean-reversion model ≥ 2% | 137 | 2 | +61% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 88 | 2 | +152% | -81% | -79% | -71% |
| Mean-reversion model ≥ 10% | 58 | 2 | +289% | -75% | -73% | -64% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 531 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 255 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 35 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 821 | 3% | 2% | 1% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 0% | -$41.65 | -43% | — |
| Sell at 2¢ | 28 | 3% | -$90.37 | -93% | 62 sec |
| Sell at 3¢ | 17 | 2% | -$91.02 | -93% | 67 sec |
| Sell at 5¢ | 10 | 1% | -$91.15 | -93% | 1.9 min |
| Sell at 10¢ | 9 | 1% | -$85.86 | -88% | 2.4 min |
| Sell at 25¢ | 6 | 1% | -$77.79 | -80% | 2.8 min |
| Sell at 50¢ | 4 | 0% | -$70.65 | -72% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 25 | 2 | 12% | 8% | +647% | -79% | -69% |
| 2–5 min | 275 | 2 | 7% | 2% | -28% | -87% | -90% |
| 1–2 min | 256 | 0 | 2% | 0% | -100% | -96% | -96% |
| Under 1 min | 265 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 61 | 2 | 5% | 3% | +334% | -88% | -82% |
| XRP | 61 | 2 | 5% | 3% | +297% | -89% | -89% |
| DOGE | 60 | 0 | 5% | 2% | -100% | -89% | -84% |
| ZEC | 60 | 0 | 5% | 0% | -100% | -88% | -100% |
| NEAR | 59 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 59 | 0 | 10% | 3% | -100% | -72% | -79% |
| SOL | 59 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 58 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 54 | 0 | 4% | 2% | -100% | -92% | -94% |
| GOLD | 47 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 42 | 0 | 2% | 0% | -100% | -95% | -100% |
| SILVER | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 35 | 0 | 6% | 3% | -100% | -90% | -85% |
| PLATINUM | 33 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 27 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 15 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 13 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 428 | 3 | 4% | 1% | -14% | -92% | -92% |
| DOWN (bought NO) | 393 | 1 | 3% | 1% | -71% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 45 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 51 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 126 | 0 | 3% | 0% | -100% | -91% | -90% |
| 0.2–0.5% | 226 | 2 | 5% | 2% | -3% | -90% | -92% |
| Over 0.5% | 83 | 2 | 8% | 4% | +171% | -82% | -81% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 237 | 1 | 3% | 1% | -50% | -94% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,808 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 45 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 9:59:34 AM | COPPER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:34 AM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:18 AM | NEAR | DOWN | 42 sec | +0.151% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:59:18 AM | PALLADIUM | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:59:18 AM | GOLD | DOWN | 42 sec | — | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:59:18 AM | SILVER | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:45 AM | ZEC | DOWN | 74 sec | +0.368% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:45 AM | ETH | DOWN | 74 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:58:29 AM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:29 AM | XRP | DOWN | 1.5 min | +0.215% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:58:13 AM | DOGE | DOWN | 1.8 min | +0.320% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:55 AM | BNB | DOWN | 2.1 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:39 AM | BTC | DOWN | 2.4 min | +0.205% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:57:39 AM | SOL | DOWN | 2.4 min | +0.347% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:08 AM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:57:08 AM | HYPE | DOWN | 2.9 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:44:51 AM | WTI | DOWN | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:44:51 AM | XRP | UP | 9 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:44:51 AM | SOL | DOWN | 9 sec | -0.025% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:44:35 AM | USDJPY | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:44:19 AM | NEAR | UP | 41 sec | -0.540% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:44:04 AM | HYPE | UP | 55 sec | -0.293% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:44:04 AM | SILVER | UP | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:43:48 AM | GOLD | UP | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:43:48 AM | ZEC | UP | 71 sec | -0.484% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:43:48 AM | DOGE | DOWN | 71 sec | +0.254% | 0¢ | ❌ Lost | $0.00 |
| 9/28 9:43:32 AM | PALLADIUM | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 9:42:44 AM | BTC | DOWN | 2.2 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:42:12 AM | ETH | DOWN | 2.8 min | +0.362% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 9:42:12 AM | BNB | DOWN | 2.8 min | +0.268% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
