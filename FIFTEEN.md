# 15-Minute 1¢ Study

*Updated Tue Oct 6, 1:51 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 670 finished bets | 1% | $26.45 | +37% | +3.95¢ | -$8.45 / $34.90 |

*Expect about **78 buys a day** (~$11.76/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 250 | $18.95 | +51% |
| Momentum model ≥ 5%, hold to the close | 668 | $13.35 | +19% |
| Mean-reversion model ≥ 5%, hold to the close | 1476 | $10.60 | +6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 9794 | 9788 | 45 (0%) | 1.07% | -$549.60 (-47%) | Hold to the close: -$549.60 (-47%) |

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
| Volatility model | 6380 | 4.1% | 0.5% (32) | -545% | ❌ Worse |
| Momentum model | 6380 | 4.1% | 0.5% (32) | -574% | ❌ Worse |
| Mean-reversion model | 6380 | 6.7% | 0.5% (32) | -629% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 6380 | 32 | -37% | -86% | -86% | -83% |
| Volatility model ≥ 2% | 1240 | 11 | +3% | -72% | -72% | -68% |
| Volatility model ≥ 5% | 670 | 7 | +37% | -60% | -59% | -56% |
| Volatility model ≥ 10% | 412 | 5 | +83% | -42% | -43% | -38% |
| Momentum model ≥ 2% | 1102 | 9 | -1% | -73% | -75% | -73% |
| Momentum model ≥ 5% | 668 | 6 | +19% | -65% | -67% | -65% |
| Momentum model ≥ 10% | 462 | 5 | +57% | -53% | -54% | -51% |
| Mean-reversion model ≥ 2% | 2188 | 18 | -10% | -83% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1476 | 14 | +6% | -80% | -80% | -74% |
| Mean-reversion model ≥ 10% | 971 | 10 | +20% | -79% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 6577 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 2427 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 784 | 3% | 2% | 2% | 1% | 1% | 0% |
| **All** | 9788 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 45 | 0% | -$549.60 | -47% | — |
| Sell at 2¢ | 356 | 4% | -$1,059.04 | -90% | 33 sec |
| Sell at 3¢ | 235 | 2% | -$1,059.95 | -90% | 47 sec |
| Sell at 5¢ | 175 | 2% | -$1,037.85 | -88% | 50 sec |
| Sell at 10¢ | 119 | 1% | -$981.71 | -83% | 65 sec |
| Sell at 25¢ | 68 | 1% | -$884.52 | -75% | 82 sec |
| Sell at 50¢ | 44 | 0% | -$770.60 | -65% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 247 | 4 | 11% | 4% | +53% | -82% | -87% |
| 2–5 min | 3156 | 24 | 7% | 3% | -26% | -87% | -87% |
| 1–2 min | 2588 | 11 | 3% | 2% | -54% | -94% | -93% |
| Under 1 min | 3794 | 6 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 745 | 6 | 5% | 3% | -3% | -90% | -89% |
| HYPE | 735 | 3 | 5% | 3% | -50% | -89% | -87% |
| DOGE | 734 | 2 | 4% | 1% | -65% | -92% | -91% |
| ETH | 732 | 7 | 5% | 3% | +20% | -87% | -87% |
| BNB | 729 | 3 | 4% | 2% | -50% | -91% | -92% |
| SOL | 727 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 726 | 4 | 5% | 3% | -28% | -87% | -89% |
| NEAR | 725 | 4 | 6% | 3% | -27% | -67% | -68% |
| XRP | 724 | 5 | 2% | 1% | -13% | -79% | -79% |
| GOLD | 408 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 392 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 371 | 2 | 2% | 1% | -41% | -95% | -97% |
| COPPER | 350 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 310 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 298 | 3 | 3% | 2% | -6% | -94% | -92% |
| PALLADIUM | 298 | 1 | 2% | 1% | -69% | -97% | -98% |
| EURUSD | 283 | 1 | 4% | 2% | -67% | -93% | -92% |
| GBPUSD | 272 | 1 | 3% | 2% | -66% | -94% | -94% |
| USDJPY | 229 | 3 | 2% | 1% | +22% | -97% | -95% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4934 | 23 | 4% | 2% | -45% | -89% | -89% |
| DOWN (bought NO) | 4854 | 22 | 3% | 2% | -48% | -90% | -91% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1079 | 7 | 2% | 1% | +12% | -62% | -62% |
| 0.05–0.1% | 1128 | 4 | 3% | 1% | -47% | -91% | -92% |
| 0.1–0.2% | 1659 | 6 | 4% | 2% | -54% | -91% | -92% |
| 0.2–0.5% | 1933 | 12 | 6% | 3% | -32% | -88% | -87% |
| Over 0.5% | 776 | 5 | 7% | 3% | -34% | -87% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 2570 | 15 | 4% | 2% | -32% | -87% | -88% |
| Morning (6am–12pm) | 2536 | 17 | 5% | 3% | -24% | -90% | -89% |
| Afternoon (12–6pm) | 2046 | 6 | 3% | 1% | -65% | -87% | -88% |
| Evening (6pm–12am) | 2636 | 7 | 3% | 1% | -69% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,042 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/6 1:44:52 PM | HYPE | UP | 7 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:44:52 PM | WTI | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:44:36 PM | SOL | DOWN | 23 sec | -0.006% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:44:04 PM | DOGE | UP | 55 sec | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:04 PM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:04 PM | GBPUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:44:04 PM | PALLADIUM | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:48 PM | BNB | DOWN | 71 sec | +0.021% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | COPPER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | XRP | DOWN | 1.7 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | ETH | DOWN | 1.7 min | +0.070% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | GOLD | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | ZEC | DOWN | 1.7 min | +0.237% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:43:16 PM | SILVER | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:41:56 PM | NEAR | UP | 3.1 min | -0.490% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:53 PM | ETH | UP | 7 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:29:37 PM | XRP | UP | 23 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:37 PM | BTC | DOWN | 23 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:29:37 PM | ZEC | UP | 23 sec | -0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:29:19 PM | NEAR | DOWN | 41 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/6 1:29:03 PM | WTI | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:28:30 PM | HYPE | DOWN | 89 sec | +0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:28:30 PM | PLATINUM | UP | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:27:58 PM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:27:58 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:27:40 PM | PALLADIUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/6 1:26:53 PM | SOL | UP | 3.1 min | -0.234% | 2¢ | ❌ Lost | -$0.15 |
| 10/6 1:26:21 PM | DOGE | UP | 3.6 min | -0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:26:05 PM | SILVER | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/6 1:24:12 PM | BNB | UP | 5.8 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
