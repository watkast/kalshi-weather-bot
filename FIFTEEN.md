# 15-Minute 1¢ Study

*Updated Wed Oct 14, 5:43 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1434 finished bets | 1% | $93.45 | +59% | +6.52¢ | $35.05 / $58.40 |

*Expect about **86 buys a day** (~$12.88/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1347 | $64.50 | +44% |
| Momentum model ≥ 2%, hold to the close | 2230 | $21.70 | +8% |
| Volatility model ≥ 2%, hold to the close | 2571 | $11.35 | +4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18516 | 18504 | 74 (0%) | 1.07% | -$1,206.20 (-54%) | Hold to the close: -$1,206.20 (-54%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12043 | 4.5% | 0.4% (52) | -636% | ❌ Worse |
| Momentum model | 12043 | 4.4% | 0.4% (52) | -661% | ❌ Worse |
| Mean-reversion model | 12043 | 7.3% | 0.4% (52) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12043 | 52 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2571 | 23 | +4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1434 | 18 | +59% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 862 | 11 | +82% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2230 | 20 | +8% | -79% | -80% | -77% |
| Momentum model ≥ 5% | 1347 | 15 | +44% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 909 | 10 | +55% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4429 | 32 | -21% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3035 | 25 | -9% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1996 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12241 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4527 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 1736 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18504 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 74 | 0% | -$1,206.20 | -54% | — |
| Sell at 2¢ | 651 | 4% | -$2,016.94 | -90% | 34 sec |
| Sell at 3¢ | 438 | 2% | -$2,015.38 | -90% | 46 sec |
| Sell at 5¢ | 320 | 2% | -$1,978.20 | -88% | 49 sec |
| Sell at 10¢ | 202 | 1% | -$1,893.58 | -84% | 63 sec |
| Sell at 25¢ | 117 | 1% | -$1,728.93 | -77% | 79 sec |
| Sell at 50¢ | 78 | 0% | -$1,519.70 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 579 | 5 | 10% | 3% | -18% | -82% | -87% |
| 2–5 min | 5968 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4834 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7119 | 16 | 1% | 0% | -67% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1373 | 11 | 5% | 3% | -0% | -89% | -89% |
| HYPE | 1367 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1364 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1364 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1363 | 5 | 4% | 2% | -55% | -90% | -90% |
| SOL | 1360 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1351 | 7 | 5% | 2% | -31% | -88% | -91% |
| XRP | 1350 | 7 | 2% | 1% | -36% | -86% | -86% |
| NEAR | 1349 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 735 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 721 | 4 | 3% | 1% | -35% | -78% | -77% |
| WTI | 693 | 3 | 3% | 1% | -50% | -94% | -96% |
| COPPER | 638 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 612 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 565 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 563 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 547 | 3 | 3% | 1% | -49% | -79% | -78% |
| GBPUSD | 514 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 468 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 107 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 100 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9342 | 38 | 3% | 2% | -53% | -89% | -88% |
| DOWN (bought NO) | 9162 | 36 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2103 | 11 | 2% | 1% | -13% | -78% | -78% |
| 0.05–0.1% | 2155 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3107 | 10 | 4% | 2% | -60% | -91% | -90% |
| 0.2–0.5% | 3519 | 20 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1354 | 6 | 6% | 2% | -54% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4454 | 16 | 3% | 1% | -57% | -87% | -88% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,496 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 5:43:17 PM | EURUSD | DOWN | 1.7 min | — | — | In play | — |
| 10/14 5:43:17 PM | HYPE | UP | 1.7 min | -0.131% | — | In play | — |
| 10/14 5:42:45 PM | SOL | UP | 2.2 min | -0.162% | — | In play | — |
| 10/14 5:42:29 PM | NEAR | UP | 2.5 min | -0.562% | — | In play | — |
| 10/14 5:41:52 PM | GBPUSD | DOWN | 3.1 min | — | — | In play | — |
| 10/14 5:29:53 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:29:32 PM | NATGAS | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:29:32 PM | BNB | UP | 28 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:29:32 PM | USDJPY | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:29:16 PM | NEAR | UP | 44 sec | -0.265% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:29:00 PM | GOLD | UP | 60 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:28:45 PM | ETH | UP | 74 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:45 PM | BTC | UP | 74 sec | -0.126% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:28:12 PM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:56 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:56 PM | DOGE | UP | 2.1 min | -0.160% | 8¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:40 PM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:40 PM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:27:03 PM | ZEC | UP | 3.0 min | -0.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:26:47 PM | HYPE | UP | 3.2 min | -0.310% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:26:47 PM | SOL | UP | 3.2 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:26:32 PM | XRP | UP | 3.5 min | -0.262% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:46 PM | BNB | DOWN | 13 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:14:46 PM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:27 PM | SOL | DOWN | 32 sec | +0.094% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:27 PM | ETH | DOWN | 32 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/14 5:14:27 PM | BTC | UP | 32 sec | -0.010% | 77¢ | ✅ Won | $13.85 |
| 10/14 5:14:27 PM | SILVER | UP | 32 sec | — | 20¢ | ✅ Won | $13.85 |
| 10/14 5:14:27 PM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 5:14:11 PM | XRP | DOWN | 48 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
