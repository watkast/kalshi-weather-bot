# 15-Minute 1¢ Study

*Updated Mon Oct 12, 1:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1196 finished bets | 1% | $38.25 | +29% | +3.20¢ | $33.35 / $4.90 |

*Expect about **82 buys a day** (~$12.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1147 | $17.15 | +14% |
| 5+ min left, hold to the close | 432 | -$7.90 | -12% |
| Volatility model ≥ 2%, hold to the close | 2111 | -$15.65 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15823 | 15816 | 62 (0%) | 1.07% | -$1,039.55 (-54%) | Hold to the close: -$1,039.55 (-54%) |

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
| Volatility model | 10517 | 4.5% | 0.4% (45) | -672% | ❌ Worse |
| Momentum model | 10517 | 4.5% | 0.4% (45) | -698% | ❌ Worse |
| Mean-reversion model | 10517 | 7.2% | 0.4% (45) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10517 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2111 | 17 | -6% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1196 | 12 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 754 | 8 | +54% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1858 | 14 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1147 | 10 | +14% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 792 | 7 | +26% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3685 | 26 | -23% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2519 | 20 | -12% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1676 | 14 | -3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10715 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3770 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1331 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15816 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,039.55 | -54% | — |
| Sell at 2¢ | 538 | 3% | -$1,725.67 | -90% | 33 sec |
| Sell at 3¢ | 357 | 2% | -$1,726.32 | -90% | 47 sec |
| Sell at 5¢ | 261 | 2% | -$1,695.90 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,613.54 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,488.48 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,335.55 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 428 | 4 | 11% | 3% | -12% | -82% | -86% |
| 2–5 min | 5083 | 32 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 4185 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6116 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1203 | 7 | 4% | 2% | -29% | -90% | -90% |
| HYPE | 1200 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1194 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1192 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1191 | 8 | 5% | 2% | -18% | -90% | -89% |
| SOL | 1191 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1186 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1179 | 7 | 5% | 2% | -22% | -76% | -77% |
| XRP | 1179 | 7 | 2% | 1% | -26% | -85% | -85% |
| GOLD | 620 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 603 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 579 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 541 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 496 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 466 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 465 | 3 | 3% | 2% | -40% | -96% | -94% |
| EURUSD | 445 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 425 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 384 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 38 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7983 | 34 | 3% | 2% | -51% | -90% | -89% |
| DOWN (bought NO) | 7833 | 28 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1922 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1913 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2748 | 9 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 2976 | 18 | 5% | 3% | -34% | -89% | -88% |
| Over 0.5% | 1153 | 5 | 6% | 2% | -55% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3658 | 9 | 3% | 1% | -71% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,526 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 1:29:44 PM | COPPER | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:29:28 PM | GOLD | UP | 32 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:29:12 PM | NATGAS | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:26:12 PM | HYPE | DOWN | 3.8 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:55 PM | DOGE | DOWN | 4.1 min | +0.293% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:55 PM | XRP | DOWN | 4.1 min | +0.391% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:55 PM | ETH | DOWN | 4.1 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:21 PM | ZEC | DOWN | 4.7 min | +0.782% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:21 PM | BNB | DOWN | 4.7 min | +0.203% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:21 PM | SOL | DOWN | 4.7 min | +0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:05 PM | NEAR | DOWN | 4.9 min | +0.546% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:25:05 PM | BTC | DOWN | 4.9 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:14:15 PM | NEAR | UP | 45 sec | -0.325% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:14:15 PM | BNB | UP | 45 sec | -0.063% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:14:15 PM | XRP | UP | 45 sec | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:14:15 PM | SOL | UP | 45 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:13:58 PM | ETH | UP | 61 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 10/12 1:13:58 PM | SILVER | UP | 61 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:42 PM | GOLD | UP | 77 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:42 PM | HYPE | UP | 77 sec | -0.217% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:42 PM | NATGAS | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:42 PM | BTC | UP | 77 sec | -0.068% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:13:26 PM | DOGE | UP | 1.6 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:12:37 PM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 1:11:45 PM | COPPER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 1:10:41 PM | ZEC | UP | 4.3 min | -0.413% | 2¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:54 PM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:59:54 PM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:19 PM | GOLD | UP | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:59:19 PM | HYPE | UP | 40 sec | -0.081% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
