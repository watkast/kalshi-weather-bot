# 15-Minute 1¢ Study

*Updated Wed Nov 4, 11:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3682 finished bets | 1% | $135.90 | +33% | +3.69¢ | $89.55 / $46.35 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3420 | $63.35 | +17% |
| Volatility model ≥ 2%, hold to the close | 6819 | $45.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 5629 | -$32.15 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46241 | 46230 | 170 (0%) | 1.07% | -$3,257.30 (-58%) | Hold to the close: -$3,257.30 (-58%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28144 | 4.7% | 0.4% (110) | -678% | ❌ Worse |
| Momentum model | 28144 | 4.6% | 0.4% (110) | -705% | ❌ Worse |
| Mean-reversion model | 28144 | 8.1% | 0.4% (110) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28144 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6819 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3682 | 39 | +33% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2097 | 24 | +64% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5629 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3420 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2232 | 20 | +26% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11651 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8174 | 69 | -6% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5475 | 49 | +2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28349 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11043 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6838 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46230 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,257.30 | -58% | — |
| Sell at 2¢ | 1817 | 4% | -$4,912.88 | -87% | 47 sec |
| Sell at 3¢ | 1241 | 3% | -$4,901.31 | -87% | 48 sec |
| Sell at 5¢ | 858 | 2% | -$4,799.60 | -85% | 63 sec |
| Sell at 10¢ | 519 | 1% | -$4,593.41 | -81% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,270.91 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,895.55 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2290 | 10 | 10% | 4% | -58% | -81% | -83% |
| 2–5 min | 14904 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11620 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17405 | 42 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3175 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3171 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3164 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3164 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3151 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3145 | 12 | 7% | 3% | -53% | -85% | -85% |
| NEAR | 3129 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3129 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3121 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1707 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1661 | 8 | 5% | 2% | -43% | -82% | -82% |
| WTI | 1659 | 5 | 4% | 1% | -64% | -92% | -93% |
| PLATINUM | 1487 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1429 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1404 | 6 | 2% | 1% | -60% | -71% | -70% |
| GBPUSD | 1356 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1344 | 8 | 2% | 1% | -44% | -76% | -75% |
| USDJPY | 1336 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1334 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 885 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 860 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 447 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23458 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22772 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4554 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4819 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7308 | 26 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 8460 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3200 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12572 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,686 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 10:59:49 PM | AUDUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:59:49 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:59:49 PM | NATGAS | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:59:33 PM | COPPER | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:59:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:59:17 PM | BTC | UP | 43 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 11/4 10:58:59 PM | HYPE | UP | 61 sec | -0.180% | 0¢ | ❌ Lost | $0.00 |
| 11/4 10:58:59 PM | GOLD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:58:59 PM | DOGE | UP | 61 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:58:43 PM | USDCAD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:58:27 PM | BNB | UP | 1.6 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:57:38 PM | GBPUSD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:57:07 PM | ETH | UP | 2.9 min | -0.164% | 3¢ | ❌ Lost | -$0.15 |
| 11/4 10:57:07 PM | XRP | UP | 2.9 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:56:45 PM | SOL | UP | 3.2 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:56:45 PM | ZEC | UP | 3.2 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:56:13 PM | NEAR | UP | 3.8 min | -0.635% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:44 PM | COPPER | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:44 PM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:44 PM | XRP | UP | 16 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/4 10:44:28 PM | HYPE | UP | 32 sec | -0.127% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:28 PM | SOL | DOWN | 32 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:28 PM | SILVER | UP | 32 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:28 PM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 10:44:28 PM | BNB | UP | 32 sec | -0.135% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:13 PM | AUDUSD | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:44:13 PM | ETH | UP | 46 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:43:23 PM | BRENT | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:43:08 PM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 10:42:35 PM | WTI | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
