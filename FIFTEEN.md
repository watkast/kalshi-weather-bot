# 15-Minute 1¢ Study

*Updated Mon Sep 28, 5:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 151 finished bets | 2% | $22.20 | +112% | +14.70¢ | $18.25 / $3.95 |

*Expect **151 buys in the first 17 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 47 | $20.95 | +297% |
| Mean-reversion model ≥ 2%, hold to the close | 233 | $11.70 | +39% |
| 2–5 min left, hold to the close | 422 | $9.40 | +16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1235 | 1229 | 8 (1%) | 1.07% | -$37.10 (-25%) | Hold to the close: -$37.10 (-25%) |

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
| Volatility model | 586 | 3.1% | 0.7% (4) | -312% | ❌ Worse |
| Momentum model | 586 | 3.2% | 0.7% (4) | -389% | ❌ Worse |
| Mean-reversion model | 586 | 6.1% | 0.7% (4) | -346% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 586 | 4 | -13% | -91% | -92% | -89% |
| Volatility model ≥ 2% | 115 | 1 | +0% | -87% | -86% | -81% |
| Volatility model ≥ 5% | 55 | 0 | -100% | -75% | -75% | -69% |
| Volatility model ≥ 10% | 29 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 99 | 0 | -100% | -84% | -90% | -89% |
| Momentum model ≥ 5% | 57 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 38 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 233 | 3 | +39% | -87% | -88% | -85% |
| Mean-reversion model ≥ 5% | 151 | 3 | +112% | -84% | -84% | -77% |
| Mean-reversion model ≥ 10% | 94 | 2 | +136% | -80% | -80% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 781 | 4% | 2% | 2% | 2% | 1% | 1% |
| Commodities | 384 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 64 | 3% | 3% | 3% | 3% | 3% | 3% |
| **All** | 1229 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$37.10 | -25% | — |
| Sell at 2¢ | 39 | 3% | -$138.96 | -93% | 47 sec |
| Sell at 3¢ | 24 | 2% | -$139.74 | -94% | 63 sec |
| Sell at 5¢ | 16 | 1% | -$138.70 | -93% | 81 sec |
| Sell at 10¢ | 15 | 1% | -$129.45 | -87% | 1.6 min |
| Sell at 25¢ | 11 | 1% | -$112.69 | -76% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$95.10 | -64% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 47 | 2 | 6% | 4% | +297% | -89% | -83% |
| 2–5 min | 422 | 5 | 6% | 2% | +16% | -89% | -91% |
| 1–2 min | 365 | 1 | 2% | 1% | -70% | -96% | -97% |
| Under 1 min | 395 | 0 | 1% | 1% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 89 | 2 | 4% | 2% | +179% | -90% | -88% |
| DOGE | 89 | 1 | 4% | 2% | +30% | -90% | -86% |
| ZEC | 88 | 1 | 6% | 1% | +39% | -87% | -96% |
| NEAR | 87 | 0 | 1% | 0% | -100% | -97% | -100% |
| BTC | 87 | 0 | 8% | 2% | -100% | -80% | -87% |
| XRP | 87 | 2 | 5% | 3% | +192% | -89% | -88% |
| SOL | 86 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 86 | 0 | 1% | 0% | -100% | -97% | -96% |
| HYPE | 82 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 69 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 64 | 0 | 2% | 0% | -100% | -97% | -100% |
| SILVER | 62 | 0 | 2% | 0% | -100% | -96% | -95% |
| NATGAS | 53 | 0 | 4% | 2% | -100% | -93% | -90% |
| COPPER | 51 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 37 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 21 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 19 | 2 | 11% | 11% | +882% | -82% | -73% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 659 | 5 | 3% | 1% | -11% | -93% | -93% |
| DOWN (bought NO) | 570 | 3 | 3% | 1% | -41% | -93% | -94% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 74 | 0 | 4% | 3% | -100% | -85% | -85% |
| 0.05–0.1% | 77 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 173 | 0 | 3% | 0% | -100% | -92% | -93% |
| 0.2–0.5% | 314 | 2 | 4% | 2% | -30% | -92% | -93% |
| Over 0.5% | 143 | 4 | 7% | 3% | +204% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 307 | 1 | 3% | 1% | -64% | -95% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,971 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 49 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 5:29:32 PM | PLATINUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:32 PM | WTI | UP | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:29:16 PM | USDJPY | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:29 PM | NATGAS | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:28:13 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:41 PM | GOLD | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:27:10 PM | NEAR | DOWN | 2.8 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:54 PM | XRP | DOWN | 3.1 min | +0.376% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:38 PM | BTC | DOWN | 3.4 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:38 PM | DOGE | DOWN | 3.4 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:38 PM | SOL | DOWN | 3.4 min | +0.294% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:23 PM | ETH | DOWN | 3.6 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:23 PM | HYPE | DOWN | 3.6 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:26:07 PM | SILVER | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:20 PM | BNB | DOWN | 4.7 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:25:04 PM | ZEC | DOWN | 4.9 min | +0.489% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:49 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:49 PM | SOL | UP | 11 sec | -0.021% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:14:34 PM | HYPE | DOWN | 25 sec | +0.062% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:14:34 PM | XRP | UP | 25 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:14:34 PM | PLATINUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:18 PM | DOGE | UP | 41 sec | -0.138% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:18 PM | ZEC | DOWN | 41 sec | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:14:18 PM | ETH | UP | 41 sec | -0.049% | 0¢ | ❌ Lost | $0.00 |
| 9/28 5:13:15 PM | BTC | UP | 1.7 min | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:13:15 PM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:59 PM | NEAR | DOWN | 2.0 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:12:09 PM | BNB | UP | 2.9 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 5:11:53 PM | GOLD | DOWN | 3.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 9/28 4:59:52 PM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
