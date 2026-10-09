# 15-Minute 1¢ Study

*Updated Thu Oct 8, 11:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 836 finished bets | 1% | $35.25 | +39% | +4.22¢ | -$16.70 / $51.95 |

*Expect about **76 buys a day** (~$11.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 819 | $23.95 | +27% |
| 5+ min left, hold to the close | 358 | $3.20 | +6% |
| Volatility model ≥ 5%, sell at 50¢ | 836 | -$2.00 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 12545 | 12538 | 51 (0%) | 1.07% | -$809.85 (-53%) | Hold to the close: -$809.85 (-53%) |

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
| Volatility model | 8004 | 4.0% | 0.4% (35) | -567% | ❌ Worse |
| Momentum model | 8004 | 4.0% | 0.4% (35) | -599% | ❌ Worse |
| Mean-reversion model | 8004 | 6.7% | 0.4% (35) | -665% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8004 | 35 | -45% | -87% | -88% | -85% |
| Volatility model ≥ 2% | 1532 | 13 | -2% | -74% | -75% | -71% |
| Volatility model ≥ 5% | 836 | 9 | +39% | -66% | -64% | -61% |
| Volatility model ≥ 10% | 512 | 7 | +101% | -49% | -50% | -45% |
| Momentum model ≥ 2% | 1356 | 11 | -2% | -75% | -77% | -74% |
| Momentum model ≥ 5% | 819 | 8 | +27% | -69% | -70% | -67% |
| Momentum model ≥ 10% | 557 | 6 | +55% | -59% | -60% | -56% |
| Mean-reversion model ≥ 2% | 2781 | 20 | -22% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1877 | 16 | -6% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1238 | 12 | +11% | -81% | -80% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8201 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3206 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1131 | 2% | 2% | 2% | 1% | 1% | 0% |
| **All** | 12538 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 51 | 0% | -$809.85 | -53% | — |
| Sell at 2¢ | 427 | 3% | -$1,370.83 | -90% | 33 sec |
| Sell at 3¢ | 282 | 2% | -$1,371.87 | -90% | 47 sec |
| Sell at 5¢ | 207 | 2% | -$1,347.30 | -88% | 51 sec |
| Sell at 10¢ | 136 | 1% | -$1,289.69 | -85% | 64 sec |
| Sell at 25¢ | 78 | 1% | -$1,181.67 | -78% | 82 sec |
| Sell at 50¢ | 51 | 0% | -$1,053.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 354 | 4 | 11% | 3% | +7% | -81% | -85% |
| 2–5 min | 4076 | 26 | 6% | 3% | -38% | -88% | -89% |
| 1–2 min | 3292 | 13 | 3% | 2% | -57% | -94% | -94% |
| Under 1 min | 4812 | 8 | 1% | 0% | -76% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 918 | 6 | 4% | 3% | -21% | -90% | -90% |
| HYPE | 917 | 3 | 5% | 3% | -60% | -89% | -88% |
| DOGE | 914 | 2 | 3% | 2% | -72% | -92% | -91% |
| BNB | 914 | 4 | 4% | 2% | -47% | -91% | -92% |
| ETH | 912 | 7 | 5% | 3% | -6% | -89% | -88% |
| NEAR | 908 | 5 | 6% | 2% | -28% | -72% | -74% |
| SOL | 907 | 0 | 3% | 1% | -100% | -94% | -93% |
| BTC | 906 | 4 | 5% | 2% | -42% | -87% | -90% |
| XRP | 905 | 6 | 2% | 1% | -17% | -82% | -82% |
| GOLD | 537 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 521 | 0 | 3% | 1% | -100% | -94% | -94% |
| WTI | 495 | 3 | 3% | 1% | -32% | -95% | -96% |
| COPPER | 458 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 415 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 395 | 3 | 3% | 2% | -29% | -95% | -93% |
| EURUSD | 389 | 3 | 3% | 2% | -28% | -71% | -69% |
| PALLADIUM | 385 | 1 | 1% | 1% | -76% | -98% | -99% |
| GBPUSD | 368 | 1 | 3% | 2% | -75% | -95% | -95% |
| USDJPY | 329 | 3 | 1% | 1% | -15% | -98% | -97% |
| AUDUSD | 23 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 22 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6335 | 27 | 3% | 2% | -51% | -89% | -88% |
| DOWN (bought NO) | 6203 | 24 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1318 | 8 | 2% | 1% | +5% | -68% | -67% |
| 0.05–0.1% | 1376 | 4 | 3% | 1% | -57% | -92% | -92% |
| 0.1–0.2% | 2093 | 7 | 4% | 2% | -58% | -92% | -92% |
| 0.2–0.5% | 2403 | 13 | 5% | 3% | -41% | -89% | -88% |
| Over 0.5% | 1009 | 5 | 6% | 2% | -49% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3090 | 17 | 4% | 2% | -37% | -85% | -85% |
| Morning (6am–12pm) | 3025 | 17 | 4% | 2% | -36% | -91% | -90% |
| Afternoon (12–6pm) | 2853 | 8 | 3% | 1% | -67% | -89% | -90% |
| Evening (6pm–12am) | 3570 | 9 | 3% | 1% | -71% | -95% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,098 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/8 11:14:36 PM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:20 PM | COPPER | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:14:04 PM | ZEC | DOWN | 56 sec | +0.137% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:48 PM | WTI | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:48 PM | PLATINUM | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:13:15 PM | GOLD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:12:13 PM | XRP | DOWN | 2.8 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:41 PM | BTC | DOWN | 3.3 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:41 PM | ETH | DOWN | 3.3 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:26 PM | SOL | DOWN | 3.6 min | +0.412% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:26 PM | DOGE | DOWN | 3.6 min | +0.237% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:10 PM | BNB | DOWN | 3.8 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 11:11:10 PM | HYPE | DOWN | 3.8 min | +0.335% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 11:10:05 PM | NEAR | DOWN | 4.9 min | +0.799% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:59:49 PM | NEAR | UP | 10 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:59:18 PM | ZEC | UP | 41 sec | -0.126% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:59:18 PM | DOGE | DOWN | 41 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:58:46 PM | XRP | UP | 73 sec | -0.079% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:31 PM | SOL | UP | 88 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:31 PM | HYPE | DOWN | 88 sec | +0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:15 PM | BNB | UP | 1.7 min | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/8 10:58:15 PM | GBPUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:58:15 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:57:59 PM | BTC | UP | 2.0 min | -0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/8 10:57:43 PM | ETH | UP | 2.3 min | -0.139% | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:44:47 PM | NATGAS | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:43:59 PM | EURUSD | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:43:43 PM | ZEC | UP | 76 sec | -0.235% | 4¢ | ❌ Lost | -$0.15 |
| 10/8 10:43:27 PM | COPPER | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/8 10:43:11 PM | BNB | UP | 1.8 min | -0.159% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
