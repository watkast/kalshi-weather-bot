# 15-Minute 1¢ Study

*Updated Tue Nov 17, 8:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4494 finished bets | 1% | $217.65 | +44% | +4.84¢ | $82.20 / $135.45 |

*Expect about **88 buys a day** (~$13.25/day at risk); max loss per buy **15¢**.*

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
| 60311 | 60277 | 237 (0%) | 1.07% | -$4,017.30 (-55%) | Hold to the close: -$4,017.30 (-55%) |

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
| Volatility model | 36111 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36111 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 36111 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36111 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8383 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4494 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2581 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6953 | 57 | +0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4230 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2753 | 26 | +34% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14798 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10294 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6838 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36317 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14340 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9620 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60277 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,017.30 | -55% | — |
| Sell at 2¢ | 2430 | 4% | -$6,409.50 | -87% | 47 sec |
| Sell at 3¢ | 1642 | 3% | -$6,400.92 | -87% | 48 sec |
| Sell at 5¢ | 1123 | 2% | -$6,283.35 | -86% | 63 sec |
| Sell at 10¢ | 685 | 1% | -$6,031.95 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,577.84 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$5,023.05 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3040 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19537 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15124 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22563 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4062 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4059 | 19 | 4% | 2% | -40% | -86% | -86% |
| HYPE | 4052 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4041 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4040 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4034 | 19 | 6% | 3% | -41% | -82% | -82% |
| NEAR | 4015 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4015 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 3999 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2144 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2126 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2081 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1897 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1850 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1781 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1777 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1748 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1736 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1706 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1291 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1236 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 857 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 435 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 420 | 4 | 4% | 2% | -11% | -49% | -48% |
| 30YRRATE | 403 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 391 | 2 | 4% | 2% | -52% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30714 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29563 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5459 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5914 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9100 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11257 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4578 | 23 | 7% | 3% | -47% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16541 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,078 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 8:29:44 PM | SOL | UP | 15 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:29:12 PM | BTC | UP | 47 sec | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:28:55 PM | NATGAS | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:28:55 PM | HYPE | UP | 65 sec | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:28:39 PM | BNB | UP | 81 sec | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:28:39 PM | DOGE | UP | 81 sec | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:28:23 PM | GOLD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:27:33 PM | ZEC | UP | 2.5 min | -0.489% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:27:17 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:27:17 PM | XRP | UP | 2.7 min | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:27:05 PM | BRENT | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:26:49 PM | WTI | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:26:49 PM | NEAR | UP | 3.2 min | -0.544% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:26:03 PM | ETH | UP | 4.0 min | -0.272% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:26:03 PM | USDCAD | UP | 4.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:26:03 PM | GBPUSD | DOWN | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:25:15 PM | EURUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:23:46 PM | COPPER | UP | 6.2 min | — | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
