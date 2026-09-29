# 15-Minute 1¢ Study

*Updated Mon Sep 28, 7:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 161 finished bets | 2% | $21.15 | +101% | +13.14¢ | $17.50 / $3.65 |

*Expect **161 buys in the first 18 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 50 | $20.50 | +273% |
| Mean-reversion model ≥ 2%, hold to the close | 246 | $10.50 | +33% |
| 5+ min left, sell at 50¢ | 50 | $6.00 | +80% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1311 | 1305 | 8 (1%) | 1.07% | -$45.65 (-29%) | Hold to the close: -$45.65 (-29%) |

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
| Volatility model | 633 | 3.1% | 0.6% (4) | -344% | ❌ Worse |
| Momentum model | 633 | 3.2% | 0.6% (4) | -420% | ❌ Worse |
| Mean-reversion model | 633 | 6.1% | 0.6% (4) | -383% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 633 | 4 | -19% | -90% | -91% | -87% |
| Volatility model ≥ 2% | 123 | 1 | -3% | -87% | -86% | -82% |
| Volatility model ≥ 5% | 59 | 0 | -100% | -76% | -76% | -70% |
| Volatility model ≥ 10% | 31 | 0 | -100% | -74% | -74% | -57% |
| Momentum model ≥ 2% | 105 | 0 | -100% | -85% | -90% | -89% |
| Momentum model ≥ 5% | 61 | 0 | -100% | -80% | -88% | -80% |
| Momentum model ≥ 10% | 42 | 0 | -100% | -87% | -80% | -67% |
| Mean-reversion model ≥ 2% | 246 | 3 | +33% | -87% | -88% | -83% |
| Mean-reversion model ≥ 5% | 161 | 3 | +101% | -85% | -85% | -78% |
| Mean-reversion model ≥ 10% | 101 | 2 | +125% | -81% | -81% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 828 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 406 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 71 | 4% | 4% | 3% | 3% | 3% | 3% |
| **All** | 1305 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 8 | 1% | -$45.65 | -29% | — |
| Sell at 2¢ | 43 | 3% | -$146.47 | -93% | 47 sec |
| Sell at 3¢ | 28 | 2% | -$146.73 | -93% | 55 sec |
| Sell at 5¢ | 19 | 1% | -$145.30 | -92% | 81 sec |
| Sell at 10¢ | 17 | 1% | -$135.38 | -86% | 1.9 min |
| Sell at 25¢ | 11 | 1% | -$121.24 | -77% | 2.1 min |
| Sell at 50¢ | 8 | 1% | -$103.65 | -66% | 2.1 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 50 | 2 | 6% | 4% | +273% | -90% | -84% |
| 2–5 min | 447 | 5 | 6% | 3% | +9% | -88% | -90% |
| 1–2 min | 378 | 1 | 2% | 1% | -71% | -96% | -96% |
| Under 1 min | 430 | 0 | 1% | 0% | -100% | -98% | -97% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 95 | 2 | 5% | 3% | +163% | -88% | -85% |
| DOGE | 94 | 1 | 4% | 2% | +24% | -91% | -86% |
| ZEC | 94 | 1 | 6% | 2% | +31% | -85% | -93% |
| XRP | 93 | 2 | 4% | 3% | +175% | -90% | -89% |
| NEAR | 92 | 0 | 2% | 1% | -100% | -94% | -96% |
| BTC | 92 | 0 | 8% | 2% | -100% | -81% | -88% |
| SOL | 91 | 0 | 3% | 2% | -100% | -91% | -87% |
| BNB | 90 | 0 | 1% | 0% | -100% | -98% | -96% |
| HYPE | 87 | 0 | 2% | 1% | -100% | -95% | -96% |
| GOLD | 71 | 0 | 3% | 0% | -100% | -94% | -100% |
| WTI | 67 | 0 | 1% | 0% | -100% | -97% | -100% |
| SILVER | 65 | 0 | 2% | 0% | -100% | -97% | -95% |
| NATGAS | 58 | 0 | 3% | 2% | -100% | -94% | -91% |
| COPPER | 53 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 52 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 27 | 0 | 4% | 0% | -100% | -94% | -90% |
| EURUSD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 20 | 2 | 10% | 10% | +833% | -83% | -74% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 701 | 5 | 4% | 2% | -16% | -92% | -92% |
| DOWN (bought NO) | 604 | 3 | 3% | 1% | -43% | -94% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 83 | 0 | 4% | 2% | -100% | -86% | -86% |
| 0.05–0.1% | 87 | 0 | 1% | 0% | -100% | -96% | -100% |
| 0.1–0.2% | 179 | 0 | 3% | 0% | -100% | -93% | -93% |
| 0.2–0.5% | 329 | 2 | 5% | 3% | -34% | -91% | -91% |
| Over 0.5% | 150 | 4 | 7% | 3% | +187% | -87% | -86% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 330 | 1 | 2% | 1% | -65% | -95% | -96% |
| Evening (6pm–12am) | 329 | 2 | 4% | 2% | -30% | -92% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 24 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,958 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 6:59:23 PM | EURUSD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:57:33 PM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:56:14 PM | DOGE | UP | 3.8 min | -0.698% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:56:14 PM | XRP | UP | 3.8 min | -0.713% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:56:14 PM | SOL | UP | 3.8 min | -0.585% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:58 PM | BTC | UP | 4.0 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:27 PM | BNB | UP | 4.5 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:11 PM | HYPE | UP | 4.8 min | -0.420% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:55:11 PM | ETH | UP | 4.8 min | -0.365% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 6:53:37 PM | NEAR | UP | 6.4 min | -1.179% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:52:03 PM | ZEC | UP | 7.9 min | -1.219% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:35 PM | PALLADIUM | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:03 PM | NATGAS | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:44:03 PM | NEAR | DOWN | 56 sec | +0.124% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:43:46 PM | XRP | DOWN | 73 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:46 PM | SOL | DOWN | 73 sec | +0.197% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:46 PM | ETH | DOWN | 73 sec | +0.085% | 2¢ | ❌ Lost | -$0.15 |
| 9/28 6:43:00 PM | DOGE | DOWN | 2.0 min | +0.213% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:44 PM | ZEC | DOWN | 2.3 min | +0.333% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:42:29 PM | HYPE | DOWN | 2.5 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:40:21 PM | EURUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:40:05 PM | GBPUSD | DOWN | 4.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:50 PM | BTC | DOWN | 10 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:50 PM | XRP | UP | 10 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | PALLADIUM | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | COPPER | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:33 PM | SILVER | DOWN | 27 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:17 PM | PLATINUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 6:29:17 PM | NEAR | DOWN | 43 sec | +0.241% | 0¢ | ❌ Lost | $0.00 |
| 9/28 6:29:01 PM | BNB | DOWN | 59 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
