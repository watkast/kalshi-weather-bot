# 15-Minute 1¢ Study

*Updated Thu Nov 19, 8:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4584 finished bets | 1% | $209.70 | +42% | +4.57¢ | $76.95 / $132.75 |

*Expect about **87 buys a day** (~$13.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4325 | $109.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 8559 | $64.80 | +6% |
| Momentum model ≥ 2%, hold to the close | 7105 | -$15.45 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62509 | 62474 | 242 (0%) | 1.07% | -$4,211.00 (-55%) | Hold to the close: -$4,211.00 (-55%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37087 | 4.5% | 0.4% (155) | -637% | ❌ Worse |
| Momentum model | 37087 | 4.4% | 0.4% (155) | -662% | ❌ Worse |
| Mean-reversion model | 37087 | 7.9% | 0.4% (155) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37087 | 155 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8559 | 78 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4584 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2636 | 30 | +66% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7105 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4325 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2822 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15151 | 109 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10540 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7005 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37293 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14970 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10211 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62474 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 242 | 0% | -$4,211.00 | -55% | — |
| Sell at 2¢ | 2534 | 4% | -$6,646.16 | -87% | 47 sec |
| Sell at 3¢ | 1710 | 3% | -$6,638.10 | -87% | 48 sec |
| Sell at 5¢ | 1169 | 2% | -$6,517.15 | -86% | 63 sec |
| Sell at 10¢ | 716 | 1% | -$6,255.04 | -82% | 65 sec |
| Sell at 25¢ | 383 | 1% | -$5,771.27 | -76% | 80 sec |
| Sell at 50¢ | 248 | 0% | -$5,211.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3195 | 17 | 11% | 4% | -50% | -81% | -82% |
| 2–5 min | 20254 | 109 | 7% | 3% | -47% | -86% | -87% |
| 1–2 min | 15631 | 53 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 23381 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4170 | 19 | 5% | 2% | -40% | -88% | -87% |
| SOL | 4167 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4159 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4149 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4148 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4144 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4126 | 22 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 4123 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4107 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2230 | 7 | 5% | 2% | -62% | -82% | -84% |
| WTI | 2210 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2170 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1975 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1937 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1867 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1859 | 6 | 2% | 1% | -70% | -77% | -77% |
| USDJPY | 1820 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1817 | 10 | 2% | 1% | -49% | -76% | -75% |
| PALLADIUM | 1777 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1371 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1311 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 932 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31899 | 124 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30575 | 118 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5555 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6045 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9335 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11604 | 51 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4745 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15444 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17035 | 50 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,006 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 8:39:33 PM | GOLD | DOWN | 5.5 min | — | — | In play | — |
| 11/19 8:29:44 PM | USDCAD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:29:44 PM | EURUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:29:44 PM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:28:25 PM | ZEC | DOWN | 1.6 min | +0.413% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:28:09 PM | BTC | DOWN | 1.9 min | +0.321% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:27:46 PM | SOL | DOWN | 2.2 min | +0.472% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:27:46 PM | DOGE | DOWN | 2.2 min | +0.402% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:27:30 PM | NEAR | DOWN | 2.5 min | +0.612% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:59 PM | SILVER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:41 PM | AUDUSD | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:41 PM | ETH | DOWN | 3.3 min | +0.335% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:25 PM | BNB | DOWN | 3.6 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:09 PM | HYPE | DOWN | 3.9 min | +0.600% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:26:09 PM | XRP | DOWN | 3.9 min | +0.535% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:14:14 PM | USDCAD | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:14:14 PM | NATGAS | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:12:51 PM | USDJPY | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:12:35 PM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:11:46 PM | HYPE | UP | 3.2 min | -0.529% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:11:28 PM | PLATINUM | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 8:11:12 PM | SOL | UP | 3.8 min | -0.722% | 0¢ | ❌ Lost | $0.00 |
| 11/19 8:11:12 PM | BTC | UP | 3.8 min | -0.475% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:11:12 PM | ETH | UP | 3.8 min | -0.640% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:55 PM | BNB | UP | 4.1 min | -0.512% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:55 PM | NEAR | UP | 4.1 min | -1.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:55 PM | ZEC | UP | 4.1 min | -0.977% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:39 PM | WTI | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:23 PM | SILVER | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/19 8:10:23 PM | GOLD | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
