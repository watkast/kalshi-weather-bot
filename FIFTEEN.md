# 15-Minute 1¢ Study

*Updated Tue Nov 10, 5:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4187 finished bets | 1% | $179.00 | +38% | +4.28¢ | $87.40 / $91.60 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3906 | $95.30 | +23% |
| Volatility model ≥ 2%, hold to the close | 7666 | $57.50 | +6% |
| Momentum model ≥ 2%, hold to the close | 6359 | -$16.20 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52732 | 52702 | 201 (0%) | 1.07% | -$3,608.25 (-56%) | Hold to the close: -$3,608.25 (-56%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31848 | 4.8% | 0.4% (128) | -681% | ❌ Worse |
| Momentum model | 31848 | 4.6% | 0.4% (128) | -705% | ❌ Worse |
| Mean-reversion model | 31848 | 8.1% | 0.4% (128) | -825% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31848 | 128 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7666 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4187 | 46 | +38% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2412 | 28 | +67% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6359 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3906 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2563 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13190 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9242 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6178 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32053 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12526 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8123 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52702 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 201 | 0% | -$3,608.25 | -56% | — |
| Sell at 2¢ | 2098 | 4% | -$5,596.77 | -87% | 47 sec |
| Sell at 3¢ | 1426 | 3% | -$5,586.11 | -87% | 48 sec |
| Sell at 5¢ | 992 | 2% | -$5,469.45 | -85% | 63 sec |
| Sell at 10¢ | 599 | 1% | -$5,245.56 | -82% | 65 sec |
| Sell at 25¢ | 317 | 1% | -$4,868.98 | -76% | 83 sec |
| Sell at 50¢ | 208 | 0% | -$4,416.25 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2636 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 17028 | 93 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13293 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19733 | 52 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3588 | 15 | 5% | 2% | -46% | -88% | -88% |
| SOL | 3584 | 16 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 3577 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3570 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3566 | 8 | 4% | 2% | -72% | -90% | -89% |
| ETH | 3559 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3541 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3539 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3529 | 13 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1892 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1875 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1844 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1674 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1612 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1567 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1536 | 8 | 2% | 1% | -51% | -78% | -78% |
| GBPUSD | 1527 | 5 | 2% | 1% | -69% | -96% | -96% |
| USDJPY | 1512 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1505 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1073 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1042 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 633 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26699 | 105 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 26003 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5128 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5463 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8233 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9582 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3639 | 15 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12806 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 5:58:57 PM | NATGAS | UP | 62 sec | — | — | In play | — |
| 11/10 5:58:57 PM | PLATINUM | UP | 62 sec | — | — | In play | — |
| 11/10 5:58:41 PM | SILVER | UP | 78 sec | — | — | In play | — |
| 11/10 5:58:25 PM | DOGE | UP | 1.6 min | -0.143% | — | In play | — |
| 11/10 5:58:09 PM | BNB | UP | 1.9 min | -0.130% | — | In play | — |
| 11/10 5:57:36 PM | NEAR | UP | 2.4 min | -0.503% | — | In play | — |
| 11/10 5:57:36 PM | ETH | UP | 2.4 min | -0.149% | — | In play | — |
| 11/10 5:57:20 PM | SOL | UP | 2.6 min | -0.230% | — | In play | — |
| 11/10 5:57:20 PM | HYPE | UP | 2.6 min | -0.321% | — | In play | — |
| 11/10 5:56:31 PM | ZEC | UP | 3.5 min | -0.635% | — | In play | — |
| 11/10 5:55:58 PM | GOLD | UP | 4.0 min | — | — | In play | — |
| 11/10 5:55:26 PM | XRP | UP | 4.5 min | -0.341% | — | In play | — |
| 11/10 5:55:10 PM | WTI | DOWN | 4.8 min | — | — | In play | — |
| 11/10 5:44:58 PM | PLATINUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:58 PM | BRENT | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:42 PM | WTI | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:42 PM | PALLADIUM | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:44:26 PM | XRP | UP | 34 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:26 PM | SILVER | UP | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:26 PM | SOL | UP | 34 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:11 PM | BNB | UP | 49 sec | -0.110% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:11 PM | HYPE | UP | 49 sec | -0.125% | 0¢ | ❌ Lost | $0.00 |
| 11/10 5:44:11 PM | COPPER | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:53 PM | NATGAS | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:37 PM | USDCAD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:37 PM | BTC | UP | 83 sec | -0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:06 PM | GOLD | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:43:06 PM | ZEC | UP | 1.9 min | -0.445% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 5:42:32 PM | USDJPY | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 5:42:16 PM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
