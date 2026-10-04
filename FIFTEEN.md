# 15-Minute 1¢ Study

*Updated Sat Oct 3, 11:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 496 finished bets | 1% | $3.80 | +7% | +0.77¢ | $0.85 / $2.95 |

*Expect about **83 buys a day** (~$12.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 178 | $1.75 | +7% |
| Volatility model ≥ 5%, hold to the close | 492 | -$10.35 | -20% |
| Momentum model ≥ 5%, sell at 50¢ | 496 | -$10.70 | -20% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7082 | 7075 | 29 (0%) | 1.07% | -$444.05 (-52%) | Hold to the close: -$444.05 (-52%) |

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
| Volatility model | 4539 | 4.2% | 0.4% (17) | -692% | ❌ Worse |
| Momentum model | 4539 | 4.3% | 0.4% (17) | -725% | ❌ Worse |
| Mean-reversion model | 4539 | 7.0% | 0.4% (17) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 4539 | 17 | -52% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 929 | 6 | -25% | -68% | -69% | -64% |
| Volatility model ≥ 5% | 492 | 3 | -20% | -52% | -52% | -50% |
| Volatility model ≥ 10% | 299 | 3 | +52% | -27% | -29% | -26% |
| Momentum model ≥ 2% | 812 | 5 | -25% | -67% | -70% | -68% |
| Momentum model ≥ 5% | 496 | 4 | +7% | -57% | -60% | -57% |
| Momentum model ≥ 10% | 338 | 3 | +30% | -42% | -44% | -41% |
| Mean-reversion model ≥ 2% | 1633 | 8 | -47% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 1103 | 7 | -30% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 725 | 5 | -20% | -78% | -79% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 4736 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7075 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 29 | 0% | -$444.05 | -52% | — |
| Sell at 2¢ | 274 | 4% | -$750.81 | -88% | 34 sec |
| Sell at 3¢ | 174 | 2% | -$754.19 | -89% | 48 sec |
| Sell at 5¢ | 130 | 2% | -$737.55 | -87% | 61 sec |
| Sell at 10¢ | 87 | 1% | -$694.08 | -82% | 78 sec |
| Sell at 25¢ | 48 | 1% | -$635.17 | -75% | 1.6 min |
| Sell at 50¢ | 28 | 0% | -$563.05 | -66% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 175 | 2 | 11% | 3% | +9% | -80% | -89% |
| 2–5 min | 2291 | 14 | 8% | 4% | -40% | -86% | -87% |
| 1–2 min | 1845 | 8 | 3% | 2% | -53% | -94% | -93% |
| Under 1 min | 2761 | 5 | 1% | 0% | -73% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 533 | 2 | 4% | 1% | -51% | -91% | -92% |
| ZEC | 532 | 3 | 5% | 3% | -33% | -89% | -90% |
| HYPE | 531 | 2 | 5% | 3% | -54% | -89% | -86% |
| ETH | 528 | 4 | 6% | 3% | -4% | -86% | -86% |
| BNB | 526 | 1 | 4% | 2% | -77% | -91% | -92% |
| SOL | 524 | 0 | 3% | 1% | -100% | -93% | -92% |
| BTC | 522 | 1 | 6% | 2% | -75% | -87% | -90% |
| XRP | 522 | 4 | 2% | 1% | -1% | -71% | -71% |
| NEAR | 518 | 2 | 6% | 2% | -48% | -59% | -62% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 274 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 225 | 2 | 4% | 2% | -17% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3572 | 17 | 4% | 2% | -44% | -88% | -88% |
| DOWN (bought NO) | 3503 | 12 | 4% | 2% | -60% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 757 | 5 | 2% | 1% | +14% | -49% | -49% |
| 0.05–0.1% | 773 | 0 | 3% | 1% | -100% | -93% | -94% |
| 0.1–0.2% | 1161 | 4 | 4% | 2% | -55% | -90% | -91% |
| 0.2–0.5% | 1421 | 6 | 6% | 3% | -53% | -88% | -88% |
| Over 0.5% | 622 | 4 | 7% | 3% | -34% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1673 | 7 | 4% | 2% | -51% | -84% | -85% |
| Morning (6am–12pm) | 1849 | 13 | 5% | 3% | -20% | -90% | -89% |
| Afternoon (12–6pm) | 1513 | 3 | 3% | 1% | -76% | -85% | -87% |
| Evening (6pm–12am) | 2040 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,838 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/3 11:38:41 PM | ZEC | DOWN | 6.3 min | +0.540% | — | In play | — |
| 10/3 11:29:00 PM | XRP | DOWN | 60 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | ZEC | UP | 76 sec | -0.215% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | ETH | DOWN | 76 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:44 PM | BTC | DOWN | 76 sec | +0.033% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:28 PM | SOL | DOWN | 1.5 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:28:12 PM | DOGE | DOWN | 1.8 min | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 11:27:24 PM | HYPE | DOWN | 2.6 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:27:24 PM | NEAR | DOWN | 2.6 min | +0.536% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:26:34 PM | BNB | DOWN | 3.4 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:14:38 PM | XRP | UP | 22 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:38 PM | NEAR | UP | 22 sec | -0.170% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:38 PM | HYPE | UP | 22 sec | -0.055% | 0¢ | ❌ Lost | $0.00 |
| 10/3 11:14:07 PM | BTC | DOWN | 52 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:14:07 PM | SOL | DOWN | 52 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:13:19 PM | ETH | DOWN | 1.7 min | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:13:03 PM | ZEC | DOWN | 1.9 min | +0.170% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 11:10:05 PM | BNB | DOWN | 4.9 min | +0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:54 PM | ZEC | UP | 5 sec | -0.030% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:54 PM | BTC | UP | 5 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:38 PM | XRP | DOWN | 21 sec | +0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:59:16 PM | ETH | DOWN | 44 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:59:01 PM | BNB | DOWN | 58 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:59:01 PM | DOGE | DOWN | 58 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:58:45 PM | SOL | DOWN | 74 sec | +0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:58:29 PM | HYPE | UP | 1.5 min | -0.310% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:44:53 PM | BTC | UP | 6 sec | -0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/3 10:44:21 PM | XRP | UP | 38 sec | -0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:21 PM | BNB | DOWN | 38 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/3 10:44:05 PM | HYPE | DOWN | 54 sec | +0.053% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
