# 15-Minute 1¢ Study

*Updated Mon Nov 16, 8:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4450 finished bets | 1% | $222.45 | +45% | +5.00¢ | $84.75 / $137.70 |

*Expect about **89 buys a day** (~$13.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4200 | $120.70 | +27% |
| Volatility model ≥ 2%, hold to the close | 8281 | $82.60 | +8% |
| Momentum model ≥ 2%, hold to the close | 6885 | $8.55 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59156 | 59107 | 227 (0%) | 1.07% | -$4,010.00 (-56%) | Hold to the close: -$4,010.00 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35569 | 4.6% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35569 | 4.5% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35569 | 7.9% | 0.4% (148) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35569 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8281 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4450 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2563 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6885 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4200 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2737 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14562 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10134 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6729 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35775 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14009 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9323 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59107 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,010.00 | -56% | — |
| Sell at 2¢ | 2372 | 4% | -$6,277.28 | -87% | 47 sec |
| Sell at 3¢ | 1600 | 3% | -$6,270.00 | -87% | 48 sec |
| Sell at 5¢ | 1095 | 2% | -$6,154.25 | -86% | 62 sec |
| Sell at 10¢ | 669 | 1% | -$5,905.61 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,480.95 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,950.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2961 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19117 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14870 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22146 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4004 | 19 | 5% | 2% | -38% | -88% | -87% |
| SOL | 3999 | 18 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3991 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3981 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3980 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3972 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3955 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3953 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3940 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2096 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2078 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2036 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1859 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1806 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1738 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1733 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1717 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1692 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1670 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1250 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1194 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 815 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30050 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29057 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5424 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5871 | 24 | 3% | 2% | -37% | -91% | -90% |
| 0.1–0.2% | 8974 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11046 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4451 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16125 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,080 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 8:59:05 PM | PALLADIUM | UP | 54 sec | — | — | In play | — |
| 11/16 8:59:05 PM | BNB | DOWN | 54 sec | +0.049% | — | In play | — |
| 11/16 8:58:49 PM | DOGE | DOWN | 71 sec | +0.123% | — | In play | — |
| 11/16 8:58:34 PM | BRENT | UP | 85 sec | — | — | In play | — |
| 11/16 8:58:18 PM | SILVER | UP | 1.7 min | — | — | In play | — |
| 11/16 8:58:18 PM | ZEC | DOWN | 1.7 min | +0.356% | — | In play | — |
| 11/16 8:58:02 PM | GOLD | UP | 1.9 min | — | — | In play | — |
| 11/16 8:58:02 PM | SOL | DOWN | 1.9 min | +0.275% | — | In play | — |
| 11/16 8:58:02 PM | XRP | DOWN | 1.9 min | +0.197% | — | In play | — |
| 11/16 8:57:46 PM | WTI | UP | 2.2 min | — | — | In play | — |
| 11/16 8:57:46 PM | COPPER | UP | 2.2 min | — | — | In play | — |
| 11/16 8:57:31 PM | NATGAS | UP | 2.5 min | — | — | In play | — |
| 11/16 8:56:43 PM | USDJPY | UP | 3.3 min | — | — | In play | — |
| 11/16 8:55:24 PM | HYPE | DOWN | 4.6 min | +0.589% | — | In play | — |
| 11/16 8:54:05 PM | NEAR | DOWN | 5.9 min | +1.046% | — | In play | — |
| 11/16 8:44:58 PM | BNB | DOWN | 2 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:44:58 PM | SOL | DOWN | 2 sec | -0.050% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:58 PM | ZEC | UP | 2 sec | -0.226% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:44:58 PM | NATGAS | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:42 PM | GBPUSD | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:42 PM | XRP | DOWN | 17 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:44:26 PM | WTI | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:26 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:26 PM | DOGE | UP | 33 sec | -0.094% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:26 PM | NEAR | DOWN | 33 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:44:26 PM | BTC | DOWN | 33 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 11/16 8:44:10 PM | ETH | DOWN | 49 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:44:10 PM | AUDUSD | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:43:39 PM | COPPER | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 8:43:39 PM | SILVER | UP | 81 sec | — | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
