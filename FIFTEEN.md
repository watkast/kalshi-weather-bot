# 15-Minute 1¢ Study

*Updated Mon Oct 12, 9:10 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1237 finished bets | 1% | $46.85 | +35% | +3.79¢ | $31.40 / $15.45 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1176 | $27.25 | +21% |
| 5+ min left, hold to the close | 444 | -$9.70 | -15% |
| Volatility model ≥ 2%, hold to the close | 2183 | -$10.95 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 16195 | 16188 | 63 (0%) | 1.07% | -$1,074.45 (-55%) | Hold to the close: -$1,074.45 (-55%) |

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
| Volatility model | 10710 | 4.5% | 0.4% (46) | -659% | ❌ Worse |
| Momentum model | 10710 | 4.5% | 0.4% (46) | -685% | ❌ Worse |
| Mean-reversion model | 10710 | 7.2% | 0.4% (46) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 10710 | 46 | -46% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2183 | 18 | -4% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 1237 | 13 | +35% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 774 | 9 | +67% | -63% | -62% | -59% |
| Momentum model ≥ 2% | 1914 | 15 | -5% | -79% | -80% | -78% |
| Momentum model ≥ 5% | 1176 | 11 | +21% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 808 | 8 | +40% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 3801 | 27 | -22% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2602 | 20 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 1722 | 14 | -6% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 10908 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3876 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1404 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 16188 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 63 | 0% | -$1,074.45 | -55% | — |
| Sell at 2¢ | 550 | 3% | -$1,771.45 | -91% | 33 sec |
| Sell at 3¢ | 364 | 2% | -$1,772.49 | -91% | 46 sec |
| Sell at 5¢ | 264 | 2% | -$1,742.85 | -89% | 49 sec |
| Sell at 10¢ | 174 | 1% | -$1,658.51 | -85% | 63 sec |
| Sell at 25¢ | 99 | 1% | -$1,530.76 | -78% | 79 sec |
| Sell at 50¢ | 64 | 0% | -$1,370.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 440 | 4 | 11% | 3% | -14% | -81% | -86% |
| 2–5 min | 5237 | 32 | 6% | 3% | -40% | -88% | -89% |
| 1–2 min | 4268 | 16 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 6239 | 11 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1224 | 7 | 4% | 2% | -30% | -90% | -90% |
| HYPE | 1221 | 4 | 4% | 2% | -60% | -90% | -89% |
| DOGE | 1215 | 2 | 4% | 2% | -79% | -91% | -90% |
| BNB | 1214 | 5 | 4% | 1% | -50% | -91% | -91% |
| ETH | 1213 | 8 | 5% | 2% | -19% | -90% | -89% |
| SOL | 1213 | 2 | 3% | 1% | -79% | -93% | -92% |
| BTC | 1206 | 6 | 5% | 2% | -34% | -88% | -90% |
| NEAR | 1201 | 7 | 5% | 2% | -24% | -76% | -77% |
| XRP | 1201 | 7 | 2% | 1% | -28% | -85% | -85% |
| GOLD | 639 | 0 | 3% | 1% | -100% | -93% | -94% |
| SILVER | 620 | 1 | 3% | 1% | -81% | -94% | -94% |
| WTI | 594 | 3 | 3% | 1% | -42% | -94% | -96% |
| COPPER | 555 | 0 | 1% | 1% | -100% | -98% | -97% |
| PLATINUM | 512 | 0 | 0% | 0% | -100% | -100% | -99% |
| PALLADIUM | 479 | 1 | 1% | 0% | -81% | -98% | -98% |
| NATGAS | 477 | 3 | 3% | 2% | -41% | -96% | -94% |
| EURUSD | 462 | 3 | 3% | 2% | -39% | -75% | -74% |
| GBPUSD | 442 | 1 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 398 | 3 | 1% | 1% | -30% | -98% | -97% |
| AUDUSD | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 50 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8164 | 34 | 3% | 2% | -52% | -90% | -89% |
| DOWN (bought NO) | 8024 | 29 | 3% | 2% | -58% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1940 | 10 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 1940 | 6 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 2777 | 9 | 4% | 2% | -60% | -91% | -92% |
| 0.2–0.5% | 3051 | 18 | 5% | 3% | -35% | -89% | -88% |
| Over 0.5% | 1197 | 5 | 6% | 2% | -57% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4019 | 20 | 4% | 2% | -43% | -86% | -86% |
| Morning (6am–12pm) | 3780 | 20 | 4% | 2% | -39% | -91% | -91% |
| Afternoon (12–6pm) | 3818 | 9 | 3% | 1% | -72% | -91% | -91% |
| Evening (6pm–12am) | 4571 | 14 | 3% | 2% | -65% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,522 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/12 8:59:53 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:59:53 PM | USDJPY | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:59:06 PM | PLATINUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:58:19 PM | NEAR | DOWN | 1.7 min | +0.452% | 0¢ | ❌ Lost | $0.00 |
| 10/12 8:58:03 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:58:03 PM | ZEC | DOWN | 1.9 min | +0.424% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | SOL | DOWN | 2.5 min | +0.401% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | HYPE | DOWN | 2.5 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | BNB | DOWN | 2.5 min | +0.147% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | BTC | DOWN | 2.5 min | +0.233% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | GBPUSD | DOWN | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:57:31 PM | ETH | DOWN | 2.5 min | +0.447% | 0¢ | ❌ Lost | $0.00 |
| 10/12 8:56:59 PM | EURUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:56:59 PM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:56:59 PM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:56:59 PM | SILVER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:56:18 PM | DOGE | DOWN | 3.7 min | +0.397% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:56:18 PM | XRP | DOWN | 3.7 min | +0.346% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:51 PM | GOLD | DOWN | 9 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:51 PM | XRP | DOWN | 9 sec | +0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:51 PM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:35 PM | USDCAD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:35 PM | WTI | DOWN | 25 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:19 PM | NEAR | UP | 41 sec | -0.078% | 28¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:19 PM | SOL | DOWN | 41 sec | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:03 PM | ETH | DOWN | 57 sec | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:03 PM | EURUSD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:44:03 PM | ZEC | DOWN | 57 sec | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/12 8:43:30 PM | GBPUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/12 8:42:26 PM | BNB | DOWN | 2.5 min | +0.066% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
