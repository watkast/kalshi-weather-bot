# 15-Minute 1¢ Study

*Updated Mon Oct 12, 12:28 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1194 finished bets | 1% | $38.40 | +30% | +3.22¢ | $33.50 / $4.90 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1144 | $17.45 | +14% |
| 5+ min left, hold to the close | 430 | -$7.60 | -12% |
| Volatility model ≥ 2%, hold to the close | 2105 | -$14.90 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15762 | 15747 | 62 (0%) | 1.07% | -$1,030.70 (-54%) | Hold to the close: -$1,030.70 (-54%) |

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
| Volatility model | 10473 | 4.5% | 0.4% (45) | -673% | ❌ Worse |
| Momentum model | 10473 | 4.5% | 0.4% (45) | -699% | ❌ Worse |
| Mean-reversion model | 10473 | 7.2% | 0.4% (45) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10473 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2105 | 17 | -6% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1194 | 12 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 753 | 8 | +54% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1849 | 14 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1144 | 10 | +14% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 790 | 7 | +26% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3669 | 26 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2509 | 20 | -11% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1672 | 14 | -3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10671 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3748 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1328 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15747 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,030.70 | -54% | — |
| Sell at 2¢ | 535 | 3% | -$1,717.60 | -90% | 33 sec |
| Sell at 3¢ | 355 | 2% | -$1,718.25 | -90% | 47 sec |
| Sell at 5¢ | 260 | 2% | -$1,687.70 | -89% | 50 sec |
| Sell at 10¢ | 170 | 1% | -$1,606.00 | -85% | 64 sec |
| Sell at 25¢ | 96 | 1% | -$1,482.94 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,326.70 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 426 | 4 | 11% | 3% | -11% | -81% | -86% |
| 2–5 min | 5056 | 32 | 6% | 3% | -38% | -88% | -88% |
| 1–2 min | 4163 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6098 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1198 | 7 | 4% | 3% | -28% | -90% | -90% |
| HYPE | 1195 | 4 | 4% | 2% | -58% | -90% | -89% |
| DOGE | 1189 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1187 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1186 | 8 | 5% | 2% | -18% | -89% | -89% |
| SOL | 1186 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1181 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1175 | 7 | 5% | 2% | -22% | -76% | -77% |
| XRP | 1174 | 7 | 2% | 1% | -26% | -84% | -85% |
| GOLD | 615 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 601 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 576 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 538 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 495 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 463 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 460 | 3 | 3% | 2% | -39% | -95% | -94% |
| EURUSD | 444 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 424 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 384 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 37 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7938 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7809 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1918 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1904 | 6 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 2738 | 9 | 4% | 2% | -59% | -91% | -92% |
| 0.2–0.5% | 2958 | 18 | 6% | 3% | -33% | -89% | -88% |
| Over 0.5% | 1150 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3589 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,512 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 12:28:53 PM | ETH | UP | 67 sec | -0.059% | — | In play | — |
| 10/12 12:28:53 PM | WTI | UP | 67 sec | — | — | In play | — |
| 10/12 12:28:37 PM | HYPE | UP | 83 sec | -0.112% | — | In play | — |
| 10/12 12:27:33 PM | DOGE | UP | 2.4 min | -0.217% | — | In play | — |
| 10/12 12:27:17 PM | SOL | UP | 2.7 min | -0.216% | — | In play | — |
| 10/12 12:26:28 PM | XRP | UP | 3.5 min | -0.353% | — | In play | — |
| 10/12 12:26:12 PM | ZEC | UP | 3.8 min | -0.485% | — | In play | — |
| 10/12 12:24:19 PM | NATGAS | DOWN | 5.7 min | — | — | In play | — |
| 10/12 12:14:46 PM | GOLD | DOWN | 13 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:14:46 PM | XRP | UP | 13 sec | -0.147% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:14:46 PM | BTC | UP | 13 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:14:30 PM | BNB | DOWN | 29 sec | +0.031% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:14:30 PM | GBPUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:14:30 PM | ZEC | DOWN | 29 sec | +0.034% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:14:30 PM | DOGE | UP | 29 sec | -0.072% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:14:14 PM | SOL | DOWN | 45 sec | +0.048% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:14:14 PM | NATGAS | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:14:14 PM | WTI | DOWN | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:13:57 PM | HYPE | UP | 62 sec | -0.109% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:13:41 PM | ETH | DOWN | 78 sec | +0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:12:52 PM | COPPER | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:11:31 PM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 11:59:53 AM | GOLD | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/12 11:59:53 AM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 11:59:37 AM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 11:59:22 AM | USDJPY | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 11:59:04 AM | SILVER | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 11:59:04 AM | ZEC | UP | 56 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/12 11:58:32 AM | COPPER | UP | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 11:58:16 AM | NEAR | UP | 1.7 min | -0.547% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
