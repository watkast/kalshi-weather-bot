# 15-Minute 1¢ Study

*Updated Tue Nov 17, 8:22 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4494 finished bets | 1% | $217.65 | +44% | +4.84¢ | $82.20 / $135.45 |

*Expect about **88 buys a day** (~$13.26/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4230 | $118.00 | +26% |
| Volatility model ≥ 2%, hold to the close | 8383 | $83.85 | +8% |
| Momentum model ≥ 2%, hold to the close | 6953 | $0.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60293 | 60259 | 237 (0%) | 1.07% | -$4,014.60 (-55%) | Hold to the close: -$4,014.60 (-55%) |

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
| Volatility model | 36102 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36102 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 36102 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36102 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8383 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4494 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2581 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6953 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4230 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2753 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14794 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10290 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6835 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36308 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14335 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9616 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60259 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,014.60 | -55% | — |
| Sell at 2¢ | 2430 | 4% | -$6,406.80 | -87% | 47 sec |
| Sell at 3¢ | 1642 | 3% | -$6,398.22 | -87% | 48 sec |
| Sell at 5¢ | 1123 | 2% | -$6,280.65 | -86% | 63 sec |
| Sell at 10¢ | 685 | 1% | -$6,029.25 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,575.14 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$5,020.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3039 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19527 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15119 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22561 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4061 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4058 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4051 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4040 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4039 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4033 | 19 | 6% | 3% | -41% | -82% | -82% |
| NEAR | 4014 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4014 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3998 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2143 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2125 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2081 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1897 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1849 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1780 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1776 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1747 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1735 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1706 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1291 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1235 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 856 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30698 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29561 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5458 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5913 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9097 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11254 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4577 | 23 | 7% | 3% | -47% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16523 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,075 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 8:14:56 PM | PALLADIUM | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:14:56 PM | EURUSD | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:14:56 PM | SILVER | UP | 3 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 8:14:56 PM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:14:24 PM | PLATINUM | DOWN | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:13:52 PM | COPPER | UP | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:13:36 PM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:56 PM | BRENT | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:36 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:36 PM | ZEC | DOWN | 2.4 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:20 PM | ETH | DOWN | 2.7 min | +0.280% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:20 PM | HYPE | DOWN | 2.7 min | +0.331% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:12:20 PM | BNB | DOWN | 2.7 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:11:34 PM | BTC | DOWN | 3.4 min | +0.259% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:11:34 PM | NEAR | DOWN | 3.4 min | +0.749% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:11:18 PM | DOGE | DOWN | 3.7 min | +0.360% | 0¢ | ❌ Lost | $0.00 |
| 11/17 8:11:18 PM | SOL | DOWN | 3.7 min | +0.427% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:11:02 PM | XRP | DOWN | 4.0 min | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:46 PM | BTC | UP | 14 sec | -0.039% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:46 PM | AUDUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:46 PM | HYPE | UP | 14 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:46 PM | PLATINUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:14 PM | EURUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:59:14 PM | SOL | DOWN | 46 sec | +0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:58:58 PM | USDCAD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:58:58 PM | XRP | DOWN | 62 sec | +0.072% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:58:58 PM | BNB | DOWN | 62 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 11/17 7:58:26 PM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 7:58:10 PM | NEAR | UP | 1.8 min | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 7:57:54 PM | WTI | UP | 2.1 min | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
