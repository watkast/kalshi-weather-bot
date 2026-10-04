# 15-Minute 1¢ Study

*Updated Sun Oct 4, 3:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 188 finished bets | 2% | $14.25 | +51% | +7.58¢ | $14.05 / $0.20 |

*Expect about **28 buys a day** (~$4.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 550 | $10.90 | +18% |
| Volatility model ≥ 2%, hold to the close | 1020 | $3.15 | +3% |
| Mean-reversion model ≥ 5%, hold to the close | 1210 | $1.60 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 7621 | 7614 | 34 (0%) | 1.07% | -$436.75 (-48%) | Hold to the close: -$436.75 (-48%) |

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
| Volatility model | 5078 | 4.3% | 0.4% (22) | -642% | ❌ Worse |
| Momentum model | 5078 | 4.3% | 0.4% (22) | -674% | ❌ Worse |
| Mean-reversion model | 5078 | 7.0% | 0.4% (22) | -743% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5078 | 22 | -45% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1020 | 9 | +3% | -68% | -69% | -63% |
| Volatility model ≥ 5% | 550 | 5 | +18% | -54% | -54% | -49% |
| Volatility model ≥ 10% | 344 | 4 | +72% | -34% | -35% | -29% |
| Momentum model ≥ 2% | 897 | 6 | -19% | -69% | -71% | -68% |
| Momentum model ≥ 5% | 554 | 4 | -5% | -60% | -64% | -60% |
| Momentum model ≥ 10% | 383 | 3 | +13% | -47% | -49% | -45% |
| Mean-reversion model ≥ 2% | 1795 | 12 | -27% | -82% | -84% | -78% |
| Mean-reversion model ≥ 5% | 1210 | 11 | +1% | -78% | -79% | -71% |
| Mean-reversion model ≥ 10% | 798 | 8 | +16% | -77% | -77% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5275 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1784 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 7614 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 34 | 0% | -$436.75 | -48% | — |
| Sell at 2¢ | 310 | 4% | -$804.15 | -88% | 34 sec |
| Sell at 3¢ | 198 | 3% | -$807.53 | -88% | 48 sec |
| Sell at 5¢ | 146 | 2% | -$789.85 | -87% | 62 sec |
| Sell at 10¢ | 100 | 1% | -$739.75 | -81% | 78 sec |
| Sell at 25¢ | 55 | 1% | -$674.70 | -74% | 1.6 min |
| Sell at 50¢ | 33 | 0% | -$592.00 | -65% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 185 | 3 | 12% | 3% | +54% | -78% | -87% |
| 2–5 min | 2451 | 18 | 8% | 4% | -28% | -85% | -86% |
| 1–2 min | 2003 | 8 | 3% | 2% | -56% | -93% | -93% |
| Under 1 min | 2972 | 5 | 1% | 0% | -75% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 595 | 4 | 5% | 3% | -20% | -89% | -89% |
| DOGE | 591 | 2 | 4% | 2% | -56% | -91% | -91% |
| HYPE | 590 | 2 | 5% | 3% | -59% | -88% | -86% |
| ETH | 588 | 5 | 6% | 3% | +7% | -85% | -85% |
| BNB | 585 | 2 | 4% | 2% | -59% | -90% | -92% |
| SOL | 584 | 0 | 3% | 1% | -100% | -92% | -91% |
| BTC | 582 | 3 | 6% | 2% | -33% | -86% | -89% |
| XRP | 582 | 4 | 2% | 1% | -12% | -74% | -74% |
| NEAR | 578 | 2 | 6% | 3% | -54% | -62% | -63% |
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
| UP (bought YES) | 3829 | 19 | 4% | 2% | -42% | -88% | -87% |
| DOWN (bought NO) | 3785 | 15 | 4% | 2% | -54% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 898 | 7 | 2% | 1% | +31% | -56% | -56% |
| 0.05–0.1% | 909 | 2 | 4% | 1% | -68% | -90% | -92% |
| 0.1–0.2% | 1298 | 4 | 4% | 2% | -61% | -90% | -91% |
| 0.2–0.5% | 1520 | 7 | 6% | 3% | -49% | -87% | -87% |
| Over 0.5% | 648 | 4 | 7% | 3% | -37% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1616 | 3 | 3% | 1% | -78% | -85% | -87% |
| Evening (6pm–12am) | 2058 | 6 | 3% | 2% | -66% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,092 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 3:11:26 PM | BNB | DOWN | 3.5 min | +0.240% | — | In play | — |
| 10/4 2:59:40 PM | ZEC | UP | 19 sec | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:30 PM | NEAR | UP | 29 sec | -0.298% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:30 PM | HYPE | DOWN | 29 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:59:28 PM | BTC | DOWN | 31 sec | +0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:58:45 PM | BNB | DOWN | 75 sec | +0.071% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:58:11 PM | XRP | DOWN | 1.8 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:57:31 PM | DOGE | DOWN | 2.5 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:57:14 PM | ETH | DOWN | 2.8 min | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:56:25 PM | SOL | DOWN | 3.6 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:41 PM | NEAR | UP | 19 sec | -0.402% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:44:41 PM | DOGE | UP | 19 sec | -0.083% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:25 PM | ETH | DOWN | 35 sec | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:09 PM | SOL | DOWN | 51 sec | +0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:09 PM | XRP | UP | 51 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:44:09 PM | BNB | DOWN | 51 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:43:21 PM | HYPE | DOWN | 1.6 min | +0.153% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:42:02 PM | BTC | DOWN | 3.0 min | +0.194% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:41:15 PM | ZEC | DOWN | 3.7 min | +0.306% | 2¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:59 PM | HYPE | DOWN | 1 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:43 PM | SOL | DOWN | 16 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:29:27 PM | NEAR | DOWN | 32 sec | +0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:29:27 PM | XRP | UP | 32 sec | -0.060% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:29:11 PM | BTC | DOWN | 48 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:29:11 PM | ETH | DOWN | 48 sec | +0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:28:55 PM | DOGE | DOWN | 64 sec | +0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:28:55 PM | BNB | DOWN | 64 sec | +0.013% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 2:27:21 PM | ZEC | UP | 2.6 min | -0.290% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 2:14:43 PM | DOGE | UP | 16 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/4 2:14:27 PM | BNB | DOWN | 32 sec | -0.010% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
