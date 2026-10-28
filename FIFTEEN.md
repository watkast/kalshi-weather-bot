# 15-Minute 1¢ Study

*Updated Wed Oct 28, 2:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3020 finished bets | 1% | $80.55 | +24% | +2.67¢ | $84.75 / -$4.20 |

*Expect about **99 buys a day** (~$14.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2805 | $42.35 | +14% |
| Volatility model ≥ 2%, hold to the close | 5590 | $5.45 | +1% |
| Momentum model ≥ 2%, hold to the close | 4623 | -$61.60 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 36950 | 36930 | 138 (0%) | 1.07% | -$2,574.75 (-57%) | Hold to the close: -$2,574.75 (-57%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 22977 | 4.7% | 0.4% (92) | -676% | ❌ Worse |
| Momentum model | 22977 | 4.6% | 0.4% (92) | -701% | ❌ Worse |
| Mean-reversion model | 22977 | 8.1% | 0.4% (92) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 22977 | 92 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5590 | 49 | +1% | -79% | -77% | -74% |
| Volatility model ≥ 5% | 3020 | 30 | +24% | -76% | -74% | -71% |
| Volatility model ≥ 10% | 1711 | 19 | +58% | -68% | -66% | -63% |
| Momentum model ≥ 2% | 4623 | 34 | -11% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 2805 | 25 | +14% | -78% | -77% | -74% |
| Momentum model ≥ 10% | 1839 | 17 | +28% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 9394 | 63 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 6586 | 53 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4400 | 38 | -2% | -79% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 23177 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 8817 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 4936 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 36930 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 138 | 0% | -$2,574.75 | -57% | — |
| Sell at 2¢ | 1409 | 4% | -$3,944.41 | -88% | 47 sec |
| Sell at 3¢ | 968 | 3% | -$3,933.23 | -87% | 48 sec |
| Sell at 5¢ | 670 | 2% | -$3,875.25 | -86% | 62 sec |
| Sell at 10¢ | 408 | 1% | -$3,720.27 | -83% | 65 sec |
| Sell at 25¢ | 218 | 1% | -$3,435.17 | -76% | 83 sec |
| Sell at 50¢ | 143 | 0% | -$3,107.50 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1649 | 8 | 11% | 4% | -54% | -80% | -81% |
| 2–5 min | 11792 | 66 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 9369 | 32 | 3% | 1% | -63% | -92% | -92% |
| Under 1 min | 14116 | 32 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2595 | 12 | 5% | 2% | -41% | -88% | -88% |
| HYPE | 2589 | 8 | 5% | 3% | -62% | -89% | -87% |
| BNB | 2587 | 15 | 5% | 2% | -28% | -85% | -84% |
| SOL | 2581 | 7 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2575 | 11 | 7% | 3% | -48% | -85% | -85% |
| DOGE | 2573 | 5 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2562 | 11 | 3% | 1% | -47% | -89% | -89% |
| NEAR | 2558 | 12 | 5% | 2% | -39% | -82% | -82% |
| BTC | 2557 | 13 | 5% | 2% | -32% | -88% | -89% |
| GOLD | 1392 | 5 | 4% | 2% | -57% | -82% | -83% |
| SILVER | 1363 | 6 | 4% | 2% | -48% | -82% | -81% |
| WTI | 1342 | 4 | 3% | 1% | -65% | -93% | -94% |
| PLATINUM | 1210 | 1 | 2% | 1% | -92% | -97% | -96% |
| COPPER | 1150 | 4 | 1% | 1% | -68% | -73% | -73% |
| EURUSD | 1131 | 3 | 2% | 1% | -75% | -88% | -88% |
| NATGAS | 1108 | 6 | 2% | 1% | -49% | -80% | -79% |
| PALLADIUM | 1072 | 2 | 1% | 0% | -83% | -89% | -90% |
| GBPUSD | 1072 | 2 | 2% | 1% | -83% | -96% | -96% |
| USDJPY | 1052 | 5 | 2% | 1% | -56% | -97% | -96% |
| AUDUSD | 610 | 4 | 1% | 1% | -39% | -82% | -81% |
| USDCAD | 576 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 180 | 0 | 1% | 1% | -100% | -99% | -99% |
| 10YRRATE | 132 | 0 | 5% | 1% | -100% | -92% | -90% |
| 30YRRATE | 124 | 0 | 1% | 0% | -100% | -99% | -98% |
| 2YRRATE | 123 | 1 | 4% | 1% | -24% | -17% | -16% |
| 5YRRATE | 116 | 1 | 6% | 3% | -20% | -90% | -91% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 18684 | 77 | 4% | 2% | -53% | -87% | -86% |
| DOWN (bought NO) | 18246 | 61 | 4% | 2% | -62% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3813 | 19 | 2% | 1% | -14% | -81% | -80% |
| 0.05–0.1% | 3986 | 14 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6039 | 22 | 4% | 2% | -55% | -90% | -89% |
| 0.2–0.5% | 6816 | 29 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2519 | 10 | 7% | 3% | -59% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 9229 | 35 | 4% | 2% | -57% | -86% | -86% |
| Morning (6am–12pm) | 9232 | 42 | 4% | 2% | -48% | -86% | -85% |
| Afternoon (12–6pm) | 8656 | 29 | 4% | 2% | -61% | -88% | -88% |
| Evening (6pm–12am) | 9813 | 32 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,550 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/28 2:57:15 PM | DOGE | DOWN | 2.7 min | +0.319% | — | In play | — |
| 10/28 2:56:58 PM | SOL | DOWN | 3.0 min | +0.221% | — | In play | — |
| 10/28 2:56:58 PM | BTC | DOWN | 3.0 min | +0.218% | — | In play | — |
| 10/28 2:56:58 PM | ETH | DOWN | 3.0 min | +0.311% | — | In play | — |
| 10/28 2:56:40 PM | HYPE | DOWN | 3.3 min | +0.374% | — | In play | — |
| 10/28 2:56:40 PM | BNB | DOWN | 3.3 min | +0.118% | — | In play | — |
| 10/28 2:56:40 PM | 2YRRATE | DOWN | 3.3 min | — | — | In play | — |
| 10/28 2:55:53 PM | ZEC | DOWN | 4.1 min | +0.470% | — | In play | — |
| 10/28 2:55:37 PM | NEAR | DOWN | 4.4 min | +0.791% | — | In play | — |
| 10/28 2:54:49 PM | 30YRRATE | DOWN | 5.2 min | — | — | In play | — |
| 10/28 2:54:16 PM | 10YRRATE | DOWN | 5.7 min | — | — | In play | — |
| 10/28 2:54:16 PM | 5YRRATE | DOWN | 5.7 min | — | — | In play | — |
| 10/28 2:44:54 PM | ETH | DOWN | 5 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:38 PM | PALLADIUM | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:22 PM | COPPER | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:22 PM | USDCAD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:22 PM | ZEC | DOWN | 38 sec | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:44:04 PM | PLATINUM | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:48 PM | BNB | DOWN | 72 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:32 PM | EURUSD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:32 PM | WTI | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:32 PM | HYPE | UP | 88 sec | -0.261% | 0¢ | ❌ Lost | $0.00 |
| 10/28 2:43:32 PM | XRP | DOWN | 88 sec | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:32 PM | BRENT | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:17 PM | 10YRRATE | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:17 PM | SOL | DOWN | 1.7 min | +0.214% | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:17 PM | NEAR | DOWN | 1.7 min | +0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:00 PM | DOGE | DOWN | 2.0 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/28 2:43:00 PM | USDJPY | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/28 2:42:28 PM | NATGAS | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
