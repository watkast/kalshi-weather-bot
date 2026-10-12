# 15-Minute 1¢ Study

*Updated Mon Oct 12, 12:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1196 finished bets | 1% | $38.25 | +29% | +3.20¢ | $33.35 / $4.90 |

*Expect about **82 buys a day** (~$12.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1147 | $17.15 | +14% |
| 5+ min left, hold to the close | 431 | -$7.75 | -12% |
| Volatility model ≥ 2%, hold to the close | 2111 | -$15.65 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 15795 | 15776 | 62 (0%) | 1.07% | -$1,034.30 (-54%) | Hold to the close: -$1,034.30 (-54%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 10490 | 4.5% | 0.4% (45) | -673% | ❌ Worse |
| Momentum model | 10490 | 4.5% | 0.4% (45) | -699% | ❌ Worse |
| Mean-reversion model | 10490 | 7.2% | 0.4% (45) | -778% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10490 | 45 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2111 | 17 | -6% | -77% | -77% | -74% |
| Volatility model ≥ 5% | 1196 | 12 | +29% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 754 | 8 | +54% | -62% | -62% | -58% |
| Momentum model ≥ 2% | 1856 | 14 | -8% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1147 | 10 | +14% | -75% | -76% | -73% |
| Momentum model ≥ 10% | 792 | 7 | +26% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3675 | 26 | -23% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2513 | 20 | -11% | -83% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1673 | 14 | -3% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10688 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3757 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1331 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 15776 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 62 | 0% | -$1,034.30 | -54% | — |
| Sell at 2¢ | 536 | 3% | -$1,720.94 | -90% | 33 sec |
| Sell at 3¢ | 356 | 2% | -$1,721.46 | -90% | 46 sec |
| Sell at 5¢ | 261 | 2% | -$1,690.65 | -89% | 50 sec |
| Sell at 10¢ | 171 | 1% | -$1,608.29 | -85% | 64 sec |
| Sell at 25¢ | 97 | 1% | -$1,483.23 | -78% | 80 sec |
| Sell at 50¢ | 64 | 0% | -$1,330.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 427 | 4 | 11% | 3% | -11% | -81% | -86% |
| 2–5 min | 5068 | 32 | 6% | 3% | -38% | -88% | -88% |
| 1–2 min | 4173 | 16 | 3% | 2% | -58% | -94% | -94% |
| Under 1 min | 6104 | 10 | 1% | 0% | -76% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1200 | 7 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1197 | 4 | 4% | 2% | -59% | -90% | -89% |
| DOGE | 1191 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1189 | 5 | 4% | 2% | -49% | -91% | -92% |
| ETH | 1188 | 8 | 5% | 2% | -18% | -90% | -89% |
| SOL | 1188 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1183 | 5 | 5% | 2% | -44% | -88% | -91% |
| NEAR | 1176 | 7 | 5% | 2% | -22% | -76% | -77% |
| XRP | 1176 | 7 | 2% | 1% | -26% | -85% | -85% |
| GOLD | 617 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 602 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 578 | 3 | 3% | 1% | -41% | -94% | -96% |
| COPPER | 538 | 0 | 1% | 1% | -100% | -98% | -98% |
| PLATINUM | 496 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 464 | 1 | 1% | 0% | -80% | -98% | -98% |
| NATGAS | 462 | 3 | 3% | 2% | -39% | -95% | -94% |
| EURUSD | 445 | 3 | 3% | 2% | -37% | -74% | -73% |
| GBPUSD | 425 | 1 | 2% | 1% | -78% | -96% | -96% |
| USDJPY | 384 | 3 | 1% | 1% | -27% | -98% | -97% |
| USDCAD | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| AUDUSD | 38 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7956 | 34 | 3% | 2% | -50% | -90% | -89% |
| DOWN (bought NO) | 7820 | 28 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1921 | 9 | 2% | 1% | -22% | -77% | -76% |
| 0.05–0.1% | 1907 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2742 | 9 | 4% | 2% | -60% | -91% | -91% |
| 0.2–0.5% | 2965 | 18 | 5% | 3% | -33% | -89% | -88% |
| Over 0.5% | 1150 | 5 | 6% | 2% | -55% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3618 | 9 | 3% | 1% | -70% | -90% | -91% |
| Evening (6pm–12am) | 4359 | 13 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,518 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 12:59:19 PM | GOLD | UP | 40 sec | — | — | In play | — |
| 10/12 12:59:19 PM | HYPE | UP | 40 sec | -0.081% | — | In play | — |
| 10/12 12:59:19 PM | ZEC | UP | 40 sec | -0.073% | — | In play | — |
| 10/12 12:58:46 PM | ETH | UP | 73 sec | -0.059% | — | In play | — |
| 10/12 12:58:46 PM | COPPER | UP | 73 sec | — | — | In play | — |
| 10/12 12:58:46 PM | NATGAS | UP | 73 sec | — | — | In play | — |
| 10/12 12:58:30 PM | DOGE | UP | 89 sec | -0.134% | — | In play | — |
| 10/12 12:58:14 PM | SOL | UP | 1.8 min | -0.117% | — | In play | — |
| 10/12 12:57:41 PM | BTC | UP | 2.3 min | -0.088% | — | In play | — |
| 10/12 12:57:25 PM | XRP | UP | 2.6 min | -0.184% | — | In play | — |
| 10/12 12:55:31 PM | NEAR | UP | 4.5 min | -0.752% | — | In play | — |
| 10/12 12:52:32 PM | BNB | UP | 7.5 min | -0.309% | — | In play | — |
| 10/12 12:44:59 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:44:43 PM | BTC | UP | 17 sec | -0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:44:27 PM | GBPUSD | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:36 PM | EURUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:36 PM | PLATINUM | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:36 PM | SOL | DOWN | 84 sec | +0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:20 PM | ETH | DOWN | 1.7 min | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:20 PM | HYPE | DOWN | 1.7 min | +0.123% | 38¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:20 PM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:43:05 PM | WTI | UP | 1.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:49 PM | ZEC | DOWN | 2.2 min | +0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:49 PM | NEAR | DOWN | 2.2 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:49 PM | BNB | DOWN | 2.2 min | +0.035% | 0¢ | ❌ Lost | $0.00 |
| 10/12 12:42:33 PM | SILVER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:17 PM | DOGE | DOWN | 2.7 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:00 PM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:42:00 PM | XRP | DOWN | 3.0 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 12:41:44 PM | AUDUSD | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
