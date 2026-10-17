# 15-Minute 1¢ Study

*Updated Sat Oct 17, 5:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1836 finished bets | 1% | $90.30 | +44% | +4.92¢ | $39.95 / $50.35 |

*Expect about **93 buys a day** (~$13.99/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1683 | $55.00 | +30% |
| Momentum model ≥ 2%, hold to the close | 2820 | -$5.45 | -2% |
| Volatility model ≥ 2%, hold to the close | 3310 | -$22.65 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22187 | 22180 | 85 (0%) | 1.07% | -$1,503.25 (-56%) | Hold to the close: -$1,503.25 (-56%) |

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
| Volatility model | 14456 | 4.6% | 0.4% (59) | -654% | ❌ Worse |
| Momentum model | 14456 | 4.5% | 0.4% (59) | -676% | ❌ Worse |
| Mean-reversion model | 14456 | 7.6% | 0.4% (59) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14456 | 59 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3310 | 27 | -6% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1836 | 21 | +44% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1075 | 13 | +72% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2820 | 23 | -2% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1683 | 17 | +30% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1122 | 12 | +50% | -74% | -74% | -68% |
| Mean-reversion model ≥ 2% | 5545 | 38 | -25% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3832 | 30 | -13% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2538 | 19 | -14% | -80% | -80% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14654 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22180 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 85 | 0% | -$1,503.25 | -56% | — |
| Sell at 2¢ | 804 | 4% | -$2,386.21 | -89% | 39 sec |
| Sell at 3¢ | 542 | 2% | -$2,383.87 | -89% | 47 sec |
| Sell at 5¢ | 391 | 2% | -$2,341.10 | -87% | 50 sec |
| Sell at 10¢ | 238 | 1% | -$2,255.47 | -84% | 63 sec |
| Sell at 25¢ | 134 | 1% | -$2,081.71 | -77% | 79 sec |
| Sell at 50¢ | 88 | 0% | -$1,861.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 783 | 5 | 10% | 3% | -39% | -82% | -84% |
| 2–5 min | 7179 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5742 | 23 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8472 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1647 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1639 | 6 | 5% | 3% | -55% | -90% | -88% |
| ETH | 1633 | 9 | 6% | 3% | -33% | -87% | -86% |
| BNB | 1633 | 7 | 5% | 2% | -47% | -89% | -88% |
| DOGE | 1630 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1624 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1618 | 7 | 3% | 1% | -47% | -86% | -87% |
| NEAR | 1616 | 9 | 6% | 3% | -27% | -78% | -78% |
| BTC | 1614 | 8 | 5% | 2% | -33% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 821 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 667 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11176 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11004 | 44 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2512 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2542 | 8 | 3% | 2% | -54% | -91% | -91% |
| 0.1–0.2% | 3672 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4250 | 21 | 6% | 3% | -46% | -88% | -88% |
| Over 0.5% | 1675 | 6 | 7% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5276 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,638 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 4:59:48 PM | ETH | UP | 12 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:32 PM | XRP | UP | 28 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:32 PM | BTC | UP | 28 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:59:32 PM | DOGE | DOWN | 28 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:16 PM | HYPE | DOWN | 44 sec | +0.080% | 33¢ | ❌ Lost | -$0.15 |
| 10/17 4:58:45 PM | NEAR | UP | 75 sec | -0.368% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:58:29 PM | SOL | DOWN | 1.5 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:58:29 PM | BNB | DOWN | 1.5 min | +0.038% | 1¢ | ❌ Lost | $0.00 |
| 10/17 4:58:13 PM | ETH | DOWN | 1.8 min | +0.056% | 99¢ | ✅ Won | $13.85 |
| 10/17 4:44:00 PM | HYPE | UP | 59 sec | -0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:44:00 PM | SOL | DOWN | 59 sec | +0.145% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:43:13 PM | ZEC | DOWN | 1.8 min | +0.442% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:57 PM | NEAR | DOWN | 2.0 min | +0.543% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:10 PM | BTC | DOWN | 2.8 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:10 PM | DOGE | DOWN | 2.8 min | +0.406% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:10 PM | XRP | DOWN | 2.8 min | +0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:10 PM | BNB | DOWN | 2.8 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:42:10 PM | ETH | DOWN | 2.8 min | +0.232% | 2¢ | ❌ Lost | $0.00 |
| 10/17 4:29:55 PM | SOL | DOWN | 5 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:29:40 PM | DOGE | UP | 19 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:29:24 PM | XRP | UP | 35 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:29:24 PM | BNB | UP | 35 sec | -0.043% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:28:52 PM | HYPE | DOWN | 68 sec | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:27:48 PM | BTC | UP | 2.2 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:27:16 PM | ZEC | UP | 2.7 min | -0.448% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:27:16 PM | NEAR | UP | 2.7 min | -0.713% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:14:25 PM | HYPE | DOWN | 34 sec | +0.243% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:14:25 PM | ZEC | DOWN | 34 sec | +0.310% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:13:22 PM | NEAR | DOWN | 1.6 min | +0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:13:06 PM | XRP | DOWN | 1.9 min | +0.350% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
