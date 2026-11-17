# 15-Minute 1¢ Study

*Updated Tue Nov 17, 8:52 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4469 finished bets | 1% | $220.20 | +45% | +4.93¢ | $83.70 / $136.50 |

*Expect about **89 buys a day** (~$13.31/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4210 | $119.65 | +26% |
| Volatility model ≥ 2%, hold to the close | 8322 | $77.20 | +8% |
| Momentum model ≥ 2%, hold to the close | 6908 | $5.70 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59694 | 59652 | 228 (0%) | 1.07% | -$4,066.95 (-56%) | Hold to the close: -$4,066.95 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35814 | 4.5% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35814 | 4.4% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35814 | 7.9% | 0.4% (148) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35814 | 148 | -47% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8322 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4469 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2570 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6908 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4210 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2742 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14675 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10211 | 85 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6786 | 61 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36020 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14167 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59652 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 228 | 0% | -$4,066.95 | -56% | — |
| Sell at 2¢ | 2405 | 4% | -$6,339.65 | -87% | 47 sec |
| Sell at 3¢ | 1620 | 3% | -$6,333.15 | -87% | 48 sec |
| Sell at 5¢ | 1109 | 2% | -$6,216.10 | -86% | 63 sec |
| Sell at 10¢ | 673 | 1% | -$5,971.32 | -82% | 65 sec |
| Sell at 25¢ | 357 | 1% | -$5,545.28 | -76% | 80 sec |
| Sell at 50¢ | 235 | 0% | -$5,014.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3009 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19326 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14979 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22325 | 60 | 1% | 0% | -62% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4029 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4027 | 18 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 4019 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 4009 | 20 | 5% | 2% | -37% | -85% | -85% |
| DOGE | 4008 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 4000 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3982 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3981 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3965 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2120 | 5 | 5% | 2% | -71% | -83% | -84% |
| WTI | 2100 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2060 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1876 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1828 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1758 | 6 | 2% | 1% | -68% | -76% | -76% |
| GBPUSD | 1753 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1734 | 10 | 2% | 1% | -46% | -75% | -74% |
| USDJPY | 1713 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1687 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1268 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1216 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 832 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 427 | 2 | 4% | 1% | -56% | -72% | -70% |
| 2YRRATE | 413 | 4 | 4% | 2% | -10% | -49% | -47% |
| 30YRRATE | 396 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 383 | 2 | 4% | 2% | -51% | -93% | -95% |
| INX | 68 | 0 | 1% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30351 | 114 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29301 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5439 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5887 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9039 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11135 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4511 | 19 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14507 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14154 | 71 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,076 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 8:52:48 AM | XRP | UP | 7.2 min | -1.283% | — | In play | — |
| 11/17 8:52:32 AM | BTC | UP | 7.5 min | -1.192% | — | In play | — |
| 11/17 8:52:16 AM | ETH | UP | 7.7 min | -1.440% | — | In play | — |
| 11/17 8:52:16 AM | NEAR | UP | 7.7 min | -1.552% | — | In play | — |
| 11/17 8:52:16 AM | SOL | UP | 7.7 min | -1.562% | — | In play | — |
| 11/17 8:51:44 AM | PALLADIUM | UP | 8.2 min | — | — | In play | — |
| 11/17 8:51:44 AM | DOGE | UP | 8.2 min | -1.552% | — | In play | — |
| 11/17 8:51:28 AM | BNB | UP | 8.5 min | -1.015% | — | In play | — |
| 11/17 8:44:01 AM | NATGAS | UP | 59 sec | — | 94¢ | ✅ Won | $13.85 |
| 11/17 8:43:29 AM | GBPUSD | DOWN | 1.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/17 8:42:25 AM | GOLD | DOWN | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:42:09 AM | USDCAD | UP | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:41:54 AM | COPPER | UP | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:41:38 AM | 30YRRATE | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:41:38 AM | EURUSD | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:41:06 AM | BNB | UP | 3.9 min | -0.416% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:50 AM | USDJPY | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:50 AM | ZEC | UP | 4.2 min | -1.259% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:34 AM | BTC | UP | 4.4 min | -0.556% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:34 AM | ETH | UP | 4.4 min | -0.840% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:34 AM | XRP | UP | 4.4 min | -0.732% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:18 AM | HYPE | UP | 4.7 min | -0.820% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:18 AM | DOGE | UP | 4.7 min | -0.571% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:40:02 AM | NEAR | UP | 5.0 min | -1.170% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:39:30 AM | SOL | UP | 5.5 min | -0.838% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 8:38:58 AM | 10YRRATE | UP | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:38:41 AM | INX | UP | 6.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:37:39 AM | 5YRRATE | UP | 7.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:37:39 AM | 2YRRATE | UP | 7.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 8:29:49 AM | USDCAD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
