# 15-Minute 1¢ Study

*Updated Wed Nov 18, 10:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4547 finished bets | 1% | $212.85 | +42% | +4.68¢ | $79.20 / $133.65 |

*Expect about **88 buys a day** (~$13.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4283 | $112.90 | +24% |
| Volatility model ≥ 2%, hold to the close | 8485 | $72.30 | +7% |
| Momentum model ≥ 2%, hold to the close | 7034 | -$8.40 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 61571 | 61536 | 237 (0%) | 1.07% | -$4,168.95 (-56%) | Hold to the close: -$4,168.95 (-56%) |

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
| Volatility model | 36654 | 4.5% | 0.4% (154) | -632% | ❌ Worse |
| Momentum model | 36654 | 4.4% | 0.4% (154) | -657% | ❌ Worse |
| Mean-reversion model | 36654 | 7.9% | 0.4% (154) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36654 | 154 | -46% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8485 | 78 | +7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4547 | 51 | +42% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2614 | 30 | +67% | -63% | -62% | -58% |
| Momentum model ≥ 2% | 7034 | 57 | -1% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4283 | 41 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2791 | 26 | +33% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14999 | 108 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 10438 | 89 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6936 | 64 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36860 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14714 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9962 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 61536 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,168.95 | -56% | — |
| Sell at 2¢ | 2494 | 4% | -$6,544.51 | -87% | 47 sec |
| Sell at 3¢ | 1683 | 3% | -$6,536.58 | -87% | 48 sec |
| Sell at 5¢ | 1148 | 2% | -$6,418.75 | -86% | 63 sec |
| Sell at 10¢ | 701 | 1% | -$6,162.64 | -82% | 65 sec |
| Sell at 25¢ | 375 | 1% | -$5,699.70 | -76% | 80 sec |
| Sell at 50¢ | 245 | 0% | -$5,161.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3131 | 17 | 10% | 4% | -49% | -82% | -83% |
| 2–5 min | 19963 | 108 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 15401 | 51 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 23028 | 61 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4122 | 19 | 5% | 2% | -39% | -88% | -87% |
| SOL | 4119 | 19 | 4% | 2% | -41% | -86% | -86% |
| HYPE | 4111 | 12 | 4% | 2% | -63% | -89% | -88% |
| DOGE | 4102 | 11 | 4% | 2% | -66% | -89% | -89% |
| BNB | 4102 | 21 | 5% | 2% | -35% | -85% | -85% |
| ETH | 4095 | 19 | 7% | 3% | -42% | -82% | -82% |
| BTC | 4076 | 21 | 5% | 2% | -30% | -86% | -88% |
| NEAR | 4074 | 18 | 5% | 2% | -42% | -85% | -86% |
| XRP | 4059 | 16 | 3% | 2% | -50% | -89% | -88% |
| GOLD | 2196 | 6 | 5% | 2% | -67% | -82% | -84% |
| WTI | 2174 | 7 | 4% | 1% | -61% | -91% | -92% |
| SILVER | 2131 | 9 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1943 | 4 | 3% | 1% | -81% | -95% | -95% |
| EURUSD | 1899 | 7 | 2% | 1% | -66% | -91% | -90% |
| COPPER | 1829 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1825 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1791 | 10 | 2% | 1% | -48% | -76% | -75% |
| USDJPY | 1783 | 6 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1746 | 4 | 1% | 0% | -79% | -93% | -93% |
| AUDUSD | 1334 | 6 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1276 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 904 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 465 | 2 | 3% | 1% | -60% | -74% | -73% |
| 2YRRATE | 444 | 4 | 4% | 2% | -16% | -52% | -50% |
| 30YRRATE | 426 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 418 | 2 | 4% | 1% | -55% | -94% | -96% |
| INX | 92 | 1 | 2% | 1% | +1% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 31355 | 121 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 30181 | 116 | 4% | 2% | -56% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5516 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5991 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9229 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11459 | 50 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4656 | 23 | 7% | 3% | -48% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14961 | 45 | 4% | 2% | -66% | -88% | -88% |
| Morning (6am–12pm) | 14575 | 78 | 4% | 2% | -39% | -85% | -85% |
| Afternoon (12–6pm) | 15130 | 65 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16870 | 49 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,023 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 10:09:46 PM | GOLD | DOWN | 5.2 min | — | — | In play | — |
| 11/18 9:59:50 PM | GOLD | DOWN | 10 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:59:50 PM | PALLADIUM | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:59:32 PM | BNB | DOWN | 28 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:59:32 PM | USDCAD | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:59:17 PM | BTC | DOWN | 42 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:59:17 PM | DOGE | UP | 42 sec | -0.086% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:58:59 PM | USDJPY | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:58:43 PM | SOL | UP | 76 sec | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:57:57 PM | XRP | DOWN | 2.0 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:57:25 PM | HYPE | DOWN | 2.6 min | +0.353% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:57:09 PM | ZEC | DOWN | 2.9 min | +0.549% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:55:00 PM | NEAR | DOWN | 5.0 min | +0.864% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:51 PM | USDCAD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:51 PM | HYPE | UP | 8 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:19 PM | NATGAS | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:19 PM | EURUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:19 PM | ZEC | DOWN | 40 sec | +0.215% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:44:19 PM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:44:03 PM | NEAR | UP | 57 sec | -0.335% | 0¢ | ❌ Lost | $0.00 |
| 11/18 9:44:03 PM | BRENT | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 9:43:30 PM | COPPER | UP | 89 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/18 9:42:58 PM | GOLD | UP | 2.0 min | — | 9¢ | ❌ Lost | -$0.15 |
| 11/18 9:42:10 PM | WTI | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 9:41:22 PM | BTC | DOWN | 3.6 min | +0.298% | 3¢ | ❌ Lost | -$0.15 |
| 11/18 9:41:22 PM | DOGE | DOWN | 3.6 min | +0.251% | 21¢ | ❌ Lost | -$0.15 |
| 11/18 9:41:06 PM | BNB | DOWN | 3.9 min | +0.161% | 2¢ | ❌ Lost | -$0.15 |
| 11/18 9:41:06 PM | ETH | DOWN | 3.9 min | +0.276% | 7¢ | ❌ Lost | -$0.15 |
| 11/18 9:41:06 PM | XRP | DOWN | 3.9 min | +0.319% | 6¢ | ❌ Lost | -$0.15 |
| 11/18 9:40:19 PM | SOL | DOWN | 4.7 min | +0.406% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
