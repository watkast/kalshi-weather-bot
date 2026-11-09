# 15-Minute 1¢ Study

*Updated Mon Nov 9, 2:03 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4104 finished bets | 1% | $187.55 | +41% | +4.57¢ | $91.90 / $95.65 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3811 | $105.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 7514 | $75.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6211 | $0.45 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51153 | 51135 | 189 (0%) | 1.07% | -$3,578.70 (-57%) | Hold to the close: -$3,578.70 (-57%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31142 | 4.8% | 0.4% (124) | -685% | ❌ Worse |
| Momentum model | 31142 | 4.6% | 0.4% (124) | -710% | ❌ Worse |
| Mean-reversion model | 31142 | 8.1% | 0.4% (124) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31142 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7514 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4104 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2361 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6211 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3811 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2498 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12876 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9028 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6033 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31347 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12080 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7708 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51135 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 189 | 0% | -$3,578.70 | -57% | — |
| Sell at 2¢ | 2023 | 4% | -$5,418.72 | -87% | 47 sec |
| Sell at 3¢ | 1376 | 3% | -$5,408.06 | -87% | 48 sec |
| Sell at 5¢ | 961 | 2% | -$5,292.05 | -85% | 62 sec |
| Sell at 10¢ | 580 | 1% | -$5,072.90 | -81% | 65 sec |
| Sell at 25¢ | 301 | 1% | -$4,724.39 | -76% | 83 sec |
| Sell at 50¢ | 194 | 0% | -$4,313.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2532 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16514 | 88 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12932 | 43 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19145 | 46 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3512 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3506 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3497 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3491 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3488 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3482 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3461 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3460 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3450 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1838 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1808 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1787 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1620 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1551 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1516 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1477 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1472 | 4 | 2% | 1% | -75% | -96% | -96% |
| PALLADIUM | 1456 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1454 | 5 | 2% | 1% | -68% | -97% | -96% |
| AUDUSD | 1013 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 979 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 578 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 328 | 1 | 4% | 2% | -72% | -64% | -62% |
| 2YRRATE | 310 | 3 | 4% | 2% | -10% | -33% | -31% |
| 30YRRATE | 305 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 286 | 1 | 4% | 1% | -67% | -93% | -95% |
| INX | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25916 | 98 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25219 | 91 | 4% | 2% | -59% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5058 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5353 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8063 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9350 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3515 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12237 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,909 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 1:59:35 PM | NATGAS | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:35 PM | PLATINUM | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:35 PM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:35 PM | BRENT | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:21 PM | EURUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:21 PM | SILVER | DOWN | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:59:21 PM | NEAR | UP | 39 sec | -0.260% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:58:48 PM | INX | UP | 71 sec | — | 0¢ | In play | — |
| 11/9 1:58:32 PM | GBPUSD | DOWN | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:58:16 PM | SOL | DOWN | 1.7 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:57:59 PM | BNB | DOWN | 2.0 min | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:57:27 PM | PALLADIUM | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:57:27 PM | GOLD | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:52 PM | HYPE | DOWN | 3.1 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:52 PM | BTC | DOWN | 3.1 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:52 PM | DOGE | DOWN | 3.1 min | +0.192% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:56:20 PM | ETH | DOWN | 3.7 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:54:43 PM | XRP | DOWN | 5.3 min | +0.540% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:52 PM | HYPE | UP | 8 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:44:37 PM | XRP | DOWN | 23 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:37 PM | 5YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:04 PM | 2YRRATE | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:04 PM | NEAR | UP | 55 sec | -0.333% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:48 PM | BTC | UP | 71 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | SILVER | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | DOGE | UP | 71 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | INX | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | SOL | UP | 88 sec | -0.350% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | PALLADIUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
