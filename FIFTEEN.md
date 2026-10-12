# 15-Minute 1¢ Study

*Updated Mon Oct 12, 4:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1184 finished bets | 1% | $39.60 | +31% | +3.34¢ | $34.25 / $5.35 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1133 | $18.95 | +16% |
| 5+ min left, hold to the close | 423 | -$6.55 | -10% |
| Volatility model ≥ 2%, hold to the close | 2084 | -$12.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15554 | 15539 | 62 (0%) | 1.07% | -$1,006.70 (-54%) | Hold to the close: -$1,006.70 (-54%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 10353 | 4.5% | 0.4% (45) | -665% | ❌ Worse |
| Momentum model | 10353 | 4.5% | 0.4% (45) | -692% | ❌ Worse |
| Mean-reversion model | 10353 | 7.2% | 0.4% (45) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10353 | 45 | -45% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2084 | 17 | -5% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1184 | 12 | +31% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 747 | 8 | +56% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1830 | 14 | -7% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1133 | 10 | +16% | -75% | -76% | -72% |
| Momentum model ≥ 10% | 784 | 7 | +28% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3625 | 26 | -21% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2478 | 20 | -10% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1657 | 14 | -2% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10551 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3684 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1304 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15539 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,006.70 | -54% | — |
| Sell at 2¢ | 532 | 3% | -$1,694.38 | -90% | 33 sec |
| Sell at 3¢ | 354 | 2% | -$1,694.64 | -90% | 46 sec |
| Sell at 5¢ | 259 | 2% | -$1,664.35 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,582.00 | -84% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,458.94 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,302.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 419 | 4 | 11% | 3% | -10% | -82% | -86% |
| 2–5 min | 5002 | 32 | 6% | 3% | -37% | -88% | -88% |
| 1–2 min | 4105 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6009 | 10 | 1% | 0% | -75% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1184 | 7 | 4% | 3% | -27% | -90% | -90% |
| HYPE | 1183 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1175 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1173 | 5 | 4% | 2% | -48% | -91% | -92% |
| ETH | 1172 | 8 | 5% | 2% | -17% | -89% | -89% |
| SOL | 1172 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1168 | 5 | 5% | 2% | -43% | -88% | -90% |
| NEAR | 1162 | 7 | 5% | 2% | -21% | -76% | -76% |
| XRP | 1162 | 7 | 2% | 1% | -25% | -84% | -84% |
| GOLD | 603 | 0 | 3% | 1% | -100% | -92% | -94% |
| SILVER | 591 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 567 | 3 | 3% | 1% | -40% | -94% | -96% |
| COPPER | 528 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 488 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 454 | 1 | 1% | 0% | -79% | -98% | -98% |
| NATGAS | 453 | 3 | 3% | 2% | -38% | -95% | -94% |
| EURUSD | 438 | 3 | 3% | 2% | -36% | -74% | -73% |
| GBPUSD | 420 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 379 | 3 | 1% | 1% | -26% | -98% | -97% |
| USDCAD | 35 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7805 | 34 | 3% | 2% | -49% | -90% | -89% |
| DOWN (bought NO) | 7734 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1901 | 9 | 2% | 1% | -21% | -76% | -76% |
| 0.05–0.1% | 1882 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2710 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2915 | 18 | 6% | 3% | -32% | -89% | -88% |
| Over 0.5% | 1140 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3990 | 20 | 4% | 2% | -42% | -86% | -86% |
| Morning (6am–12pm) | 3615 | 20 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 3575 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,513 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 4:59:16 AM | GOLD | UP | 44 sec | — | — | In play | — |
| 10/12 4:59:16 AM | SOL | UP | 44 sec | -0.048% | — | In play | — |
| 10/12 4:59:16 AM | NATGAS | UP | 44 sec | — | — | In play | — |
| 10/12 4:59:16 AM | ETH | UP | 44 sec | -0.061% | — | In play | — |
| 10/12 4:59:00 AM | DOGE | UP | 60 sec | -0.136% | — | In play | — |
| 10/12 4:58:13 AM | NEAR | UP | 1.8 min | -0.406% | — | In play | — |
| 10/12 4:57:42 AM | ZEC | DOWN | 2.3 min | +0.264% | — | In play | — |
| 10/12 4:57:27 AM | HYPE | UP | 2.5 min | -0.199% | — | In play | — |
| 10/12 4:44:45 AM | EURUSD | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:44:29 AM | BTC | DOWN | 31 sec | +0.024% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:44:29 AM | PALLADIUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:43:57 AM | GBPUSD | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:43:42 AM | SOL | DOWN | 78 sec | +0.156% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:43:42 AM | ETH | DOWN | 78 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:43:26 AM | XRP | DOWN | 1.6 min | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:43:10 AM | HYPE | UP | 1.8 min | -0.149% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:42:45 AM | ZEC | DOWN | 2.2 min | +0.276% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:42:09 AM | BNB | DOWN | 2.9 min | +0.089% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:41:40 AM | NEAR | DOWN | 3.3 min | +0.447% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:40:06 AM | DOGE | DOWN | 4.9 min | +0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:55 AM | PLATINUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:55 AM | SILVER | DOWN | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:55 AM | DOGE | DOWN | 5 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:40 AM | WTI | UP | 20 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:24 AM | BTC | UP | 36 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:08 AM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | BNB | UP | 52 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/12 4:29:08 AM | COPPER | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | HYPE | UP | 52 sec | -0.075% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 4:29:08 AM | ETH | UP | 52 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
