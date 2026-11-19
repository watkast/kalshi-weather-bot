# 15-Minute 1¢ Study

*Updated Thu Nov 19, 3:58 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4572 finished bets | 1% | $210.75 | +42% | +4.61¢ | $77.40 / $133.35 |

*Expect about **87 buys a day** (~$13.02/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4312 | $110.50 | +24% |
| Volatility model ≥ 2%, hold to the close | 8535 | $66.90 | +7% |
| Momentum model ≥ 2%, hold to the close | 7079 | -$13.05 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 62238 | 62201 | 240 (0%) | 1.07% | -$4,207.50 (-56%) | Hold to the close: -$4,207.50 (-56%) |

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
| Volatility model | 36951 | 4.5% | 0.4% (154) | -638% | ❌ Worse |
| Momentum model | 36951 | 4.4% | 0.4% (154) | -663% | ❌ Worse |
| Mean-reversion model | 36951 | 7.9% | 0.4% (154) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36951 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8535 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4572 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2631 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7079 | 57 | -2% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4312 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2811 | 26 | +32% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 15102 | 108 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10508 | 89 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6986 | 64 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 37157 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14886 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10158 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 62201 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 240 | 0% | -$4,207.50 | -56% | — |
| Sell at 2¢ | 2526 | 4% | -$6,616.74 | -87% | 47 sec |
| Sell at 3¢ | 1705 | 3% | -$6,608.55 | -87% | 48 sec |
| Sell at 5¢ | 1166 | 2% | -$6,487.60 | -86% | 63 sec |
| Sell at 10¢ | 713 | 1% | -$6,227.47 | -82% | 65 sec |
| Sell at 25¢ | 381 | 1% | -$5,746.39 | -76% | 80 sec |
| Sell at 50¢ | 247 | 0% | -$5,200.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3183 | 17 | 11% | 4% | -49% | -81% | -82% |
| 2–5 min | 20161 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15568 | 52 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23276 | 63 | 1% | 0% | -61% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4155 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4152 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4144 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4134 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4133 | 21 | 5% | 2% | -36% | -85% | -85% |
| ETH | 4129 | 19 | 7% | 3% | -43% | -82% | -82% |
| BTC | 4110 | 21 | 5% | 2% | -31% | -86% | -88% |
| NEAR | 4108 | 18 | 5% | 2% | -43% | -85% | -86% |
| XRP | 4092 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2219 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2196 | 7 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 2159 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1967 | 5 | 3% | 1% | -76% | -95% | -95% |
| EURUSD | 1927 | 7 | 3% | 1% | -66% | -91% | -90% |
| GBPUSD | 1856 | 8 | 2% | 1% | -60% | -96% | -95% |
| COPPER | 1849 | 6 | 2% | 1% | -70% | -76% | -76% |
| USDJPY | 1810 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1809 | 10 | 2% | 1% | -48% | -76% | -75% |
| PALLADIUM | 1767 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1360 | 6 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1300 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 920 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 480 | 2 | 3% | 1% | -61% | -75% | -73% |
| 2YRRATE | 456 | 4 | 4% | 2% | -18% | -52% | -51% |
| 30YRRATE | 441 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 431 | 2 | 4% | 2% | -57% | -94% | -95% |
| INX | 97 | 1 | 2% | 1% | -4% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31721 | 123 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 30480 | 117 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5543 | 25 | 2% | 1% | -18% | -78% | -78% |
| 0.05–0.1% | 6030 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9306 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11559 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4710 | 23 | 7% | 3% | -49% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15189 | 47 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14806 | 79 | 5% | 2% | -39% | -85% | -84% |
| Afternoon (12–6pm) | 15279 | 65 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 16927 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,003 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/19 3:58:04 PM | AUDUSD | UP | 1.9 min | — | — | In play | — |
| 11/19 3:57:47 PM | ZEC | DOWN | 2.2 min | +0.412% | — | In play | — |
| 11/19 3:57:15 PM | USDJPY | UP | 2.7 min | — | — | In play | — |
| 11/19 3:44:48 PM | BNB | UP | 12 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:32 PM | DOGE | DOWN | 28 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:32 PM | ZEC | UP | 28 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:32 PM | GBPUSD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:44:17 PM | XRP | UP | 42 sec | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:17 PM | BTC | DOWN | 42 sec | +0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:44:01 PM | HYPE | UP | 58 sec | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:45 PM | SOL | DOWN | 74 sec | +0.168% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:45 PM | ETH | DOWN | 74 sec | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:43:29 PM | NEAR | UP | 1.5 min | -0.334% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:29:42 PM | GBPUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:29:26 PM | NATGAS | DOWN | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:27:35 PM | ZEC | DOWN | 2.4 min | +0.653% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:26:42 PM | BTC | DOWN | 3.3 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:25:24 PM | XRP | DOWN | 4.6 min | +0.398% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:25:24 PM | SOL | DOWN | 4.6 min | +0.405% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:24:52 PM | HYPE | DOWN | 5.1 min | +0.793% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:24:52 PM | BNB | DOWN | 5.1 min | +0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:24:52 PM | NEAR | DOWN | 5.1 min | +0.750% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:24:36 PM | DOGE | DOWN | 5.4 min | +0.536% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:24:36 PM | ETH | DOWN | 5.4 min | +0.501% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:14:58 PM | EURUSD | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:14:58 PM | ZEC | DOWN | 2 sec | -0.027% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:13:53 PM | DOGE | DOWN | 66 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |
| 11/19 3:13:53 PM | NEAR | UP | 66 sec | -0.410% | 0¢ | ❌ Lost | -$0.15 |
| 11/19 3:13:21 PM | XRP | DOWN | 1.6 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/19 3:12:49 PM | HYPE | DOWN | 2.2 min | +0.496% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
