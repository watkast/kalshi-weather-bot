# 15-Minute 1¢ Study

*Updated Fri Nov 13, 2:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4291 finished bets | 1% | $167.75 | +35% | +3.91¢ | $80.35 / $87.40 |

*Expect about **92 buys a day** (~$13.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4035 | $94.60 | +22% |
| Volatility model ≥ 2%, hold to the close | 7934 | $24.80 | +3% |
| Momentum model ≥ 2%, hold to the close | 6588 | -$29.35 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56405 | 56384 | 214 (0%) | 1.07% | -$3,885.25 (-56%) | Hold to the close: -$3,885.25 (-56%) |

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
| Volatility model | 33570 | 4.6% | 0.4% (135) | -663% | ❌ Worse |
| Momentum model | 33570 | 4.5% | 0.4% (135) | -689% | ❌ Worse |
| Mean-reversion model | 33570 | 8.0% | 0.4% (135) | -805% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33570 | 135 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7934 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4291 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2485 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6588 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4035 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2645 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13808 | 94 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9628 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6419 | 56 | -1% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33775 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13610 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8999 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56384 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 214 | 0% | -$3,885.25 | -56% | — |
| Sell at 2¢ | 2248 | 4% | -$6,002.77 | -87% | 47 sec |
| Sell at 3¢ | 1519 | 3% | -$5,994.84 | -87% | 48 sec |
| Sell at 5¢ | 1045 | 2% | -$5,880.00 | -85% | 63 sec |
| Sell at 10¢ | 635 | 1% | -$5,643.40 | -82% | 65 sec |
| Sell at 25¢ | 332 | 1% | -$5,250.33 | -76% | 82 sec |
| Sell at 50¢ | 219 | 0% | -$4,759.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2811 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18150 | 98 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14217 | 47 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 21193 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3780 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3778 | 17 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 3771 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3757 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3756 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3752 | 16 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3732 | 18 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3731 | 17 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3718 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2045 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2018 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1986 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1808 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1752 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1697 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1678 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1665 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1644 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1625 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1161 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 766 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 400 | 2 | 4% | 2% | -53% | -70% | -68% |
| 2YRRATE | 382 | 4 | 4% | 2% | -2% | -44% | -43% |
| 30YRRATE | 375 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 354 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28650 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27734 | 104 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5292 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5690 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8614 | 32 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 10246 | 42 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3925 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13649 | 60 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 2:29:54 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:38 PM | DOGE | UP | 22 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 11/13 2:29:38 PM | GBPUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:38 PM | 10YRRATE | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:38 PM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:23 PM | HYPE | DOWN | 36 sec | +0.087% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:23 PM | USDJPY | UP | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:23 PM | BRENT | DOWN | 36 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:04 PM | AUDUSD | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:04 PM | NEAR | UP | 56 sec | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:29:04 PM | 2YRRATE | UP | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:28:48 PM | ZEC | UP | 72 sec | -0.350% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:28:32 PM | 5YRRATE | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:27:58 PM | BTC | UP | 2.0 min | -0.252% | 0¢ | ❌ Lost | $0.00 |
| 11/13 2:27:58 PM | XRP | UP | 2.0 min | -0.306% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:27:26 PM | ETH | UP | 2.6 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:26:36 PM | BNB | UP | 3.4 min | -0.266% | 2¢ | ❌ Lost | -$0.15 |
| 11/13 2:26:05 PM | SILVER | DOWN | 3.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/13 2:25:30 PM | GOLD | DOWN | 4.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:25:14 PM | PLATINUM | DOWN | 4.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:24:24 PM | SOL | UP | 5.6 min | -0.683% | 2¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:48 PM | AUDUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:48 PM | GBPUSD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:48 PM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:32 PM | WTI | DOWN | 28 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:32 PM | BRENT | DOWN | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:14:00 PM | 10YRRATE | UP | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:13:44 PM | 5YRRATE | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:13:28 PM | HYPE | UP | 1.5 min | -0.424% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 2:13:28 PM | NEAR | UP | 1.5 min | -0.485% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
