# 15-Minute 1¢ Study

*Updated Tue Sep 29, 12:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 56 finished bets | 4% | $19.60 | +233% | +35.00¢ | $23.80 / -$4.20 |

*Expect about **49 buys a day** (~$7.29/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 195 | $16.50 | +65% |
| 5+ min left, sell at 50¢ | 56 | $5.10 | +61% |
| Mean-reversion model ≥ 2%, hold to the close | 299 | $3.45 | +9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1585 | 1579 | 8 (1%) | 1.07% | -$78.35 (-41%) | Hold to the close: -$78.35 (-41%) |

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
| Volatility model | 801 | 2.7% | 0.5% (4) | -326% | ❌ Worse |
| Momentum model | 801 | 2.9% | 0.5% (4) | -401% | ❌ Worse |
| Mean-reversion model | 801 | 5.7% | 0.5% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 801 | 4 | -36% | -89% | -90% | -85% |
| Volatility model ≥ 2% | 154 | 1 | -25% | -83% | -85% | -79% |
| Volatility model ≥ 5% | 70 | 0 | -100% | -69% | -69% | -58% |
| Volatility model ≥ 10% | 36 | 0 | -100% | -70% | -66% | -43% |
| Momentum model ≥ 2% | 128 | 0 | -100% | -84% | -89% | -87% |
| Momentum model ≥ 5% | 76 | 0 | -100% | -81% | -91% | -85% |
| Momentum model ≥ 10% | 51 | 0 | -100% | -89% | -84% | -74% |
| Mean-reversion model ≥ 2% | 299 | 3 | +9% | -84% | -85% | -78% |
| Mean-reversion model ≥ 5% | 195 | 3 | +65% | -82% | -82% | -72% |
| Mean-reversion model ≥ 10% | 123 | 2 | +81% | -76% | -77% | -66% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 996 | 5% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 490 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 93 | 3% | 3% | 2% | 2% | 2% | 2% |
| **All** | 1579 | 3% | 2% | 2% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$78.35 | -41% | — |
| Sell at 2¢ | 54 | 3% | -$176.31 | -93% | 47 sec |
| Sell at 3¢ | 34 | 2% | -$177.09 | -93% | 47 sec |
| Sell at 5¢ | 25 | 2% | -$174.10 | -91% | 81 sec |
| Sell at 10¢ | 23 | 1% | -$160.22 | -84% | 1.9 min |
| Sell at 25¢ | 13 | 1% | -$147.32 | -77% | 2.1 min |
| Sell at 50¢ | 9 | 1% | -$129.60 | -68% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 56 | 2 | 7% | 4% | +233% | -88% | -86% |
| 2–5 min | 533 | 5 | 7% | 3% | -9% | -88% | -89% |
| 1–2 min | 444 | 1 | 2% | 1% | -76% | -95% | -96% |
| Under 1 min | 546 | 0 | 1% | 0% | -100% | -98% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 114 | 2 | 5% | 4% | +117% | -88% | -85% |
| ZEC | 113 | 1 | 6% | 2% | +9% | -86% | -94% |
| DOGE | 112 | 1 | 4% | 3% | +9% | -90% | -85% |
| NEAR | 111 | 0 | 5% | 2% | -100% | -88% | -93% |
| BTC | 111 | 0 | 8% | 3% | -100% | -79% | -86% |
| XRP | 111 | 2 | 4% | 3% | +130% | -91% | -90% |
| SOL | 110 | 0 | 3% | 2% | -100% | -92% | -89% |
| BNB | 108 | 0 | 3% | 1% | -100% | -94% | -94% |
| HYPE | 106 | 0 | 3% | 2% | -100% | -94% | -94% |
| GOLD | 86 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 78 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 77 | 0 | 1% | 0% | -100% | -97% | -96% |
| COPPER | 68 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 67 | 0 | 3% | 1% | -100% | -95% | -92% |
| PLATINUM | 66 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 48 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 35 | 0 | 3% | 0% | -100% | -95% | -93% |
| EURUSD | 30 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 28 | 2 | 7% | 7% | +567% | -88% | -81% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 841 | 5 | 4% | 2% | -31% | -91% | -91% |
| DOWN (bought NO) | 738 | 3 | 3% | 1% | -53% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 98 | 0 | 3% | 2% | -100% | -88% | -88% |
| 0.05–0.1% | 111 | 0 | 1% | 0% | -100% | -97% | -100% |
| 0.1–0.2% | 225 | 0 | 4% | 1% | -100% | -89% | -89% |
| 0.2–0.5% | 380 | 2 | 5% | 3% | -42% | -90% | -91% |
| Over 0.5% | 182 | 4 | 7% | 4% | +132% | -86% | -85% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 322 | 1 | 4% | 2% | -64% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 589 | 2 | 4% | 2% | -60% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,037 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/29 12:13:17 AM | NEAR | DOWN | 1.7 min | +0.550% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:13:17 AM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:43 AM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:43 AM | COPPER | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:11 AM | SILVER | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:12:11 AM | PLATINUM | DOWN | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:56 AM | HYPE | DOWN | 3.0 min | +0.478% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:11:56 AM | XRP | DOWN | 3.0 min | +0.663% | 0¢ | ❌ Lost | -$0.15 |
| 9/29 12:10:35 AM | DOGE | DOWN | 4.4 min | +0.569% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:10:03 AM | ZEC | DOWN | 4.9 min | +1.009% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:09:46 AM | ETH | DOWN | 5.2 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:09:46 AM | BNB | DOWN | 5.2 min | +0.172% | 2¢ | ❌ Lost | -$0.15 |
| 9/29 12:09:46 AM | SOL | DOWN | 5.2 min | +0.699% | 1¢ | ❌ Lost | -$0.15 |
| 9/29 12:09:12 AM | BTC | DOWN | 5.8 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:49 PM | PLATINUM | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | SILVER | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | NEAR | DOWN | 43 sec | +0.145% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:59:17 PM | ZEC | DOWN | 43 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:59:02 PM | SOL | DOWN | 57 sec | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:58:30 PM | XRP | DOWN | 89 sec | +0.262% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:57:58 PM | BTC | DOWN | 2.0 min | +0.143% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 11:57:26 PM | DOGE | DOWN | 2.5 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | ETH | DOWN | 3.1 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | WTI | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | BNB | DOWN | 3.1 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:54 PM | COPPER | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:56:37 PM | HYPE | DOWN | 3.4 min | +0.445% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:56 PM | XRP | UP | 4 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 11:44:56 PM | GBPUSD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 11:44:56 PM | BTC | UP | 4 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
