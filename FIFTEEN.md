# 15-Minute 1¢ Study

*Updated Fri Nov 27, 11:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5006 finished bets | 1% | $199.15 | +37% | +3.98¢ | $94.65 / $104.50 |

*Expect about **83 buys a day** (~$12.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4748 | $99.05 | +20% |
| Volatility model ≥ 2%, hold to the close | 9345 | $24.00 | +2% |
| Momentum model ≥ 2%, hold to the close | 7775 | -$53.30 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69423 | 69387 | 257 (0%) | 1.07% | -$4,802.90 (-57%) | Hold to the close: -$4,802.90 (-57%) |

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
| Volatility model | 40928 | 4.5% | 0.4% (165) | -661% | ❌ Worse |
| Momentum model | 40928 | 4.5% | 0.4% (165) | -684% | ❌ Worse |
| Mean-reversion model | 40928 | 7.9% | 0.4% (165) | -802% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40928 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9345 | 81 | +2% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 5006 | 53 | +37% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2906 | 32 | +64% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 7775 | 59 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4748 | 43 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 3096 | 28 | +32% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16702 | 113 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11633 | 93 | -11% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7716 | 66 | -2% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41134 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16602 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11651 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69387 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 257 | 0% | -$4,802.90 | -57% | — |
| Sell at 2¢ | 2845 | 4% | -$7,353.20 | -88% | 47 sec |
| Sell at 3¢ | 1910 | 3% | -$7,348.00 | -87% | 48 sec |
| Sell at 5¢ | 1291 | 2% | -$7,225.75 | -86% | 62 sec |
| Sell at 10¢ | 790 | 1% | -$6,946.00 | -83% | 65 sec |
| Sell at 25¢ | 426 | 1% | -$6,416.84 | -76% | 80 sec |
| Sell at 50¢ | 271 | 0% | -$5,815.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3607 | 17 | 10% | 4% | -55% | -82% | -83% |
| 2–5 min | 22506 | 116 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17247 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26014 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4602 | 20 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4591 | 16 | 5% | 2% | -55% | -89% | -88% |
| SOL | 4585 | 20 | 4% | 2% | -43% | -86% | -86% |
| BNB | 4579 | 22 | 5% | 2% | -39% | -85% | -85% |
| DOGE | 4576 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4571 | 19 | 7% | 3% | -48% | -82% | -82% |
| BTC | 4549 | 24 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4544 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4537 | 16 | 4% | 2% | -55% | -88% | -88% |
| GOLD | 2452 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2434 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2401 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2169 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2125 | 7 | 2% | 1% | -69% | -91% | -91% |
| GBPUSD | 2072 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2057 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2023 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2011 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1959 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1598 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1501 | 1 | 3% | 1% | -94% | -95% | -95% |
| BRENT | 1119 | 1 | 2% | 1% | -92% | -96% | -97% |
| 10YRRATE | 563 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 525 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 522 | 4 | 4% | 2% | -28% | -58% | -57% |
| 5YRRATE | 513 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 67 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35315 | 133 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34072 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5956 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6521 | 26 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 10187 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12972 | 56 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 5489 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16692 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16484 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 16940 | 73 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19271 | 51 | 4% | 2% | -69% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,067 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/27 10:59:44 AM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:59:28 AM | 30YRRATE | DOWN | 31 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/27 10:59:28 AM | 10YRRATE | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:59:28 AM | 5YRRATE | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:59:10 AM | 2YRRATE | DOWN | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:59:10 AM | WTI | DOWN | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:58:54 AM | EURUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:58:54 AM | AUDUSD | DOWN | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:58:22 AM | USDMXN | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:58:04 AM | NATGAS | UP | 1.9 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/27 10:58:04 AM | COPPER | DOWN | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:57:16 AM | PALLADIUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:57:16 AM | PLATINUM | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:57:16 AM | BTC | DOWN | 2.7 min | +0.267% | 0¢ | ❌ Lost | $0.00 |
| 11/27 10:56:56 AM | DOGE | DOWN | 3.1 min | +0.351% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:56 AM | BNB | DOWN | 3.1 min | +0.193% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:56 AM | SOL | DOWN | 3.1 min | +0.406% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:56 AM | XRP | DOWN | 3.1 min | +0.286% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:40 AM | ETH | DOWN | 3.3 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:24 AM | SILVER | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:09 AM | GOLD | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:56:09 AM | HYPE | DOWN | 3.8 min | +0.735% | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:54:27 AM | ZEC | DOWN | 5.5 min | +1.898% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:54:27 AM | NEAR | DOWN | 5.5 min | +0.888% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:44:30 AM | USDJPY | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:43:06 AM | 30YRRATE | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:42:50 AM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:42:50 AM | BTC | UP | 2.2 min | -0.270% | 1¢ | ❌ Lost | -$0.15 |
| 11/27 10:42:34 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/27 10:42:34 AM | 2YRRATE | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
