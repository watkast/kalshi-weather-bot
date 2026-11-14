# 15-Minute 1¢ Study

*Updated Fri Nov 13, 9:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4317 finished bets | 1% | $178.60 | +37% | +4.14¢ | $78.55 / $100.05 |

*Expect about **92 buys a day** (~$13.81/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4061 | $105.15 | +24% |
| Volatility model ≥ 2%, hold to the close | 7981 | $32.65 | +3% |
| Momentum model ≥ 2%, hold to the close | 6634 | -$21.05 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56666 | 56644 | 216 (0%) | 1.07% | -$3,887.10 (-56%) | Hold to the close: -$3,887.10 (-56%) |

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
| Volatility model | 33782 | 4.6% | 0.4% (137) | -656% | ❌ Worse |
| Momentum model | 33782 | 4.5% | 0.4% (137) | -682% | ❌ Worse |
| Mean-reversion model | 33782 | 8.0% | 0.4% (137) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33782 | 137 | -48% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7981 | 71 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4317 | 47 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2493 | 29 | +67% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6634 | 53 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4061 | 39 | +24% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2654 | 25 | +32% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 13885 | 96 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9683 | 80 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6451 | 57 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33987 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13647 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56644 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 216 | 0% | -$3,887.10 | -56% | — |
| Sell at 2¢ | 2259 | 4% | -$6,029.76 | -87% | 47 sec |
| Sell at 3¢ | 1528 | 3% | -$6,021.18 | -87% | 48 sec |
| Sell at 5¢ | 1048 | 2% | -$5,907.90 | -85% | 63 sec |
| Sell at 10¢ | 638 | 1% | -$5,669.32 | -82% | 65 sec |
| Sell at 25¢ | 334 | 1% | -$5,273.56 | -76% | 82 sec |
| Sell at 50¢ | 221 | 0% | -$4,775.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2819 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18263 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14276 | 48 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 21273 | 56 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3803 | 17 | 5% | 2% | -42% | -88% | -87% |
| SOL | 3802 | 17 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 3794 | 11 | 5% | 2% | -64% | -89% | -88% |
| DOGE | 3782 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3778 | 19 | 5% | 2% | -37% | -86% | -85% |
| ETH | 3776 | 16 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3756 | 19 | 5% | 2% | -31% | -87% | -88% |
| NEAR | 3754 | 17 | 5% | 2% | -41% | -85% | -86% |
| XRP | 3742 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1672 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 775 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28797 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27847 | 106 | 4% | 2% | -56% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5304 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5710 | 21 | 3% | 2% | -43% | -91% | -91% |
| 0.1–0.2% | 8656 | 33 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 10337 | 42 | 6% | 3% | -55% | -87% | -87% |
| Over 0.5% | 3972 | 18 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13638 | 63 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13785 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15488 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 9:11:16 PM | HYPE | DOWN | 3.7 min | +1.217% | — | In play | — |
| 11/13 8:59:16 PM | BNB | UP | 43 sec | -0.211% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 8:59:16 PM | DOGE | DOWN | 43 sec | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:59:16 PM | XRP | UP | 43 sec | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:59:16 PM | SOL | UP | 43 sec | -0.259% | 0¢ | ❌ Lost | $0.00 |
| 11/13 8:59:01 PM | BRENT | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 8:58:45 PM | BTC | UP | 75 sec | -0.210% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 8:58:45 PM | ETH | UP | 75 sec | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:58:29 PM | HYPE | UP | 1.5 min | -0.609% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:58:12 PM | WTI | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:57:41 PM | NEAR | UP | 2.3 min | -0.556% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:56:20 PM | ZEC | UP | 3.7 min | -1.266% | 0¢ | ❌ Lost | $0.00 |
| 11/13 8:44:54 PM | NATGAS | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 8:44:38 PM | BRENT | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 8:43:34 PM | WTI | UP | 85 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/13 8:42:14 PM | SOL | UP | 2.8 min | -0.733% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:41:58 PM | BTC | UP | 3.0 min | -0.655% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:41:27 PM | XRP | UP | 3.5 min | -0.690% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:41:27 PM | ZEC | UP | 3.5 min | -0.882% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:40:43 PM | ETH | UP | 4.3 min | -0.877% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:40:43 PM | NEAR | UP | 4.3 min | -1.011% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:40:26 PM | DOGE | UP | 4.6 min | -1.003% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:39:24 PM | BNB | UP | 5.6 min | -0.972% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:37:48 PM | HYPE | UP | 7.2 min | -2.576% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:29:47 PM | XRP | UP | 12 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/13 8:29:31 PM | NEAR | UP | 28 sec | -0.276% | 0¢ | ❌ Lost | $0.00 |
| 11/13 8:29:31 PM | DOGE | UP | 28 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/13 8:27:24 PM | ZEC | UP | 2.6 min | -0.500% | 3¢ | ❌ Lost | $0.00 |
| 11/13 8:27:24 PM | ETH | UP | 2.6 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 8:27:08 PM | HYPE | UP | 2.9 min | -0.559% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
