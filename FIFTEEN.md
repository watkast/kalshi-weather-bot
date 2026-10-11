# 15-Minute 1¢ Study

*Updated Sat Oct 10, 11:08 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1047 finished bets | 1% | $25.25 | +22% | +2.41¢ | -$0.25 / $25.50 |

*Expect about **81 buys a day** (~$12.14/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1006 | $2.80 | +3% |
| 5+ min left, hold to the close | 398 | -$2.80 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1047 | -$19.25 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 14244 | 14237 | 56 (0%) | 1.07% | -$938.30 (-54%) | Hold to the close: -$938.30 (-54%) |

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
| Volatility model | 9392 | 4.3% | 0.4% (39) | -636% | ❌ Worse |
| Momentum model | 9392 | 4.3% | 0.4% (39) | -665% | ❌ Worse |
| Mean-reversion model | 9392 | 7.0% | 0.4% (39) | -741% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9392 | 39 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1847 | 14 | -12% | -76% | -76% | -73% |
| Volatility model ≥ 5% | 1047 | 10 | +22% | -70% | -69% | -66% |
| Volatility model ≥ 10% | 654 | 8 | +75% | -57% | -57% | -53% |
| Momentum model ≥ 2% | 1626 | 11 | -19% | -78% | -79% | -77% |
| Momentum model ≥ 5% | 1006 | 8 | +3% | -73% | -74% | -71% |
| Momentum model ≥ 10% | 695 | 6 | +21% | -65% | -66% | -62% |
| Mean-reversion model ≥ 2% | 3272 | 23 | -24% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 2227 | 17 | -16% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1483 | 13 | +1% | -81% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 9590 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3444 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 14237 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 56 | 0% | -$938.30 | -54% | — |
| Sell at 2¢ | 483 | 3% | -$1,554.72 | -90% | 33 sec |
| Sell at 3¢ | 319 | 2% | -$1,555.89 | -90% | 47 sec |
| Sell at 5¢ | 233 | 2% | -$1,528.85 | -89% | 50 sec |
| Sell at 10¢ | 152 | 1% | -$1,453.18 | -84% | 64 sec |
| Sell at 25¢ | 87 | 1% | -$1,336.33 | -78% | 81 sec |
| Sell at 50¢ | 57 | 0% | -$1,197.55 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 394 | 4 | 11% | 3% | -4% | -81% | -86% |
| 2–5 min | 4609 | 28 | 6% | 3% | -40% | -89% | -89% |
| 1–2 min | 3732 | 15 | 3% | 2% | -56% | -94% | -94% |
| Under 1 min | 5498 | 9 | 1% | 0% | -76% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1073 | 6 | 4% | 3% | -32% | -90% | -90% |
| HYPE | 1073 | 3 | 4% | 2% | -66% | -90% | -89% |
| DOGE | 1071 | 2 | 4% | 2% | -76% | -91% | -91% |
| BNB | 1069 | 5 | 4% | 2% | -43% | -91% | -92% |
| ETH | 1064 | 8 | 5% | 3% | -8% | -89% | -88% |
| SOL | 1063 | 1 | 3% | 1% | -88% | -94% | -93% |
| BTC | 1061 | 4 | 5% | 2% | -50% | -88% | -91% |
| NEAR | 1059 | 6 | 5% | 2% | -26% | -75% | -75% |
| XRP | 1057 | 6 | 2% | 1% | -29% | -84% | -84% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 529 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 431 | 3 | 3% | 2% | -35% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 7162 | 29 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 7075 | 27 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1683 | 9 | 2% | 1% | -11% | -74% | -73% |
| 0.05–0.1% | 1699 | 5 | 3% | 1% | -58% | -92% | -92% |
| 0.1–0.2% | 2452 | 8 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 2673 | 14 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1080 | 5 | 6% | 2% | -52% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3525 | 19 | 4% | 2% | -38% | -85% | -86% |
| Morning (6am–12pm) | 3425 | 18 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3332 | 9 | 3% | 1% | -68% | -90% | -90% |
| Evening (6pm–12am) | 3955 | 10 | 3% | 1% | -71% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,391 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/10 10:59:53 PM | SOL | UP | 6 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:59:53 PM | HYPE | UP | 6 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:59:38 PM | ETH | UP | 21 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:59:38 PM | XRP | DOWN | 21 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:59:38 PM | NEAR | DOWN | 21 sec | -0.011% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:58:50 PM | BTC | DOWN | 69 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:58:00 PM | DOGE | DOWN | 2.0 min | +0.102% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:56:08 PM | BNB | DOWN | 3.9 min | +0.072% | 0¢ | ❌ Lost | -$0.15 |
| 10/10 10:43:17 PM | NEAR | DOWN | 1.7 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:56 PM | DOGE | DOWN | 3.1 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:56 PM | HYPE | DOWN | 3.1 min | +0.130% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:56 PM | BTC | DOWN | 3.1 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:41 PM | SOL | DOWN | 3.3 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:41 PM | XRP | DOWN | 3.3 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:10 PM | ETH | DOWN | 3.8 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:41:10 PM | BNB | DOWN | 3.8 min | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:38:31 PM | ZEC | DOWN | 6.5 min | +0.610% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:29:10 PM | ZEC | UP | 49 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:28:54 PM | SOL | DOWN | 65 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:28:54 PM | HYPE | DOWN | 65 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:28:23 PM | XRP | DOWN | 1.6 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:27:51 PM | NEAR | DOWN | 2.1 min | +0.390% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:27:51 PM | BTC | DOWN | 2.1 min | +0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:27:04 PM | BNB | DOWN | 2.9 min | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:26:33 PM | DOGE | DOWN | 3.4 min | +0.154% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:26:17 PM | ETH | DOWN | 3.7 min | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/10 10:14:50 PM | ETH | DOWN | 10 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:14:33 PM | BTC | DOWN | 27 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:14:01 PM | ZEC | DOWN | 59 sec | +0.150% | 0¢ | ❌ Lost | $0.00 |
| 10/10 10:14:01 PM | DOGE | DOWN | 59 sec | +0.060% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
