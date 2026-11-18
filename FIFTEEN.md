# 15-Minute 1¢ Study

*Updated Wed Nov 18, 1:32 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4500 finished bets | 1% | $216.75 | +44% | +4.82¢ | $81.90 / $134.85 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4238 | $116.80 | +26% |
| Volatility model ≥ 2%, hold to the close | 8393 | $82.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6966 | -$1.35 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60427 | 60393 | 237 (0%) | 1.07% | -$4,032.75 (-55%) | Hold to the close: -$4,032.75 (-55%) |

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
| Volatility model | 36163 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36163 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 36163 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36163 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8393 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4500 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2583 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6966 | 57 | -0% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4238 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2759 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14819 | 108 | -20% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10307 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6847 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36369 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14373 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9651 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60393 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,032.75 | -55% | — |
| Sell at 2¢ | 2437 | 4% | -$6,423.13 | -87% | 47 sec |
| Sell at 3¢ | 1647 | 3% | -$6,414.42 | -87% | 48 sec |
| Sell at 5¢ | 1126 | 2% | -$6,296.85 | -86% | 63 sec |
| Sell at 10¢ | 685 | 1% | -$6,047.40 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,593.29 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$5,038.50 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3058 | 17 | 11% | 4% | -47% | -81% | -82% |
| 2–5 min | 19584 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15144 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22594 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4067 | 19 | 5% | 3% | -39% | -88% | -87% |
| SOL | 4065 | 19 | 4% | 2% | -40% | -86% | -87% |
| HYPE | 4058 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4047 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4046 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4040 | 19 | 7% | 3% | -41% | -82% | -82% |
| NEAR | 4021 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4021 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 4004 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2149 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2130 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2085 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1901 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1854 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1786 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1781 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1751 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1741 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1709 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1294 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1239 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 862 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 438 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 423 | 4 | 4% | 2% | -12% | -49% | -48% |
| 30YRRATE | 406 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 394 | 2 | 4% | 2% | -53% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30777 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29616 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5461 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5921 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9110 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11280 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4588 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14606 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

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
| 11/18 1:29:53 AM | USDJPY | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:53 AM | HYPE | UP | 6 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:53 AM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:37 AM | NEAR | UP | 22 sec | -0.242% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:29:21 AM | BRENT | UP | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:29:05 AM | SOL | DOWN | 55 sec | +0.158% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:50 AM | BNB | DOWN | 69 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:28:02 AM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:30 AM | USDCAD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:30 AM | GBPUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:27:14 AM | 30YRRATE | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:26:58 AM | GOLD | DOWN | 3.0 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/18 1:26:42 AM | SILVER | DOWN | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:39 AM | ETH | DOWN | 4.3 min | +0.246% | 7¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:39 AM | EURUSD | UP | 4.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:07 AM | 2YRRATE | DOWN | 4.9 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/18 1:25:07 AM | BTC | DOWN | 4.9 min | +0.239% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:24:51 AM | DOGE | DOWN | 5.1 min | +0.321% | 7¢ | ❌ Lost | -$0.15 |
| 11/18 1:24:35 AM | 5YRRATE | DOWN | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:24:35 AM | 10YRRATE | DOWN | 5.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:24:19 AM | XRP | DOWN | 5.7 min | +0.671% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:14:36 AM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:32 AM | 30YRRATE | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:32 AM | 2YRRATE | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | AUDUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | 10YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | USDJPY | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:12:41 AM | XRP | UP | 2.3 min | -0.429% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:12:09 AM | DOGE | UP | 2.8 min | -0.278% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
