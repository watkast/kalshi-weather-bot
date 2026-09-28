# 15-Minute 1¢ Study

*Updated Mon Sep 28, 9:02 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade small.** Profitable in both halves of the data; sample still modest.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 69 finished bets | 3% | $19.00 | +211% | +27.54¢ | $9.65 / $9.35 |

*Expect **69 buys in the first 8 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Mean-reversion model ≥ 2%, hold to the close | 115 | $12.70 | +83% |
| Volatility model ≥ 2%, hold to the close | 45 | $8.45 | +152% |
| Mean-reversion model ≥ 5%, sell at 50¢ | 69 | $4.50 | +50% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 769 | 763 | 4 (1%) | 1.07% | -$35.65 (-39%) | Hold to the close: -$35.65 (-39%) |

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
| Volatility model | 301 | 3.3% | 0.7% (2) | -365% | ❌ Worse |
| Momentum model | 301 | 3.7% | 0.7% (2) | -481% | ❌ Worse |
| Mean-reversion model | 301 | 6.0% | 0.7% (2) | -364% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 301 | 2 | -14% | -88% | -90% | -88% |
| Volatility model ≥ 2% | 45 | 1 | +152% | -81% | -79% | -77% |
| Volatility model ≥ 5% | 25 | 0 | -100% | -73% | -73% | -77% |
| Volatility model ≥ 10% | 13 | 0 | -100% | -81% | -71% | -52% |
| Momentum model ≥ 2% | 50 | 0 | -100% | -83% | -87% | -89% |
| Momentum model ≥ 5% | 32 | 0 | -100% | -78% | -89% | -82% |
| Momentum model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Mean-reversion model ≥ 2% | 115 | 2 | +83% | -83% | -85% | -83% |
| Mean-reversion model ≥ 5% | 69 | 2 | +211% | -80% | -78% | -71% |
| Mean-reversion model ≥ 10% | 46 | 2 | +367% | -74% | -74% | -68% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 496 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 235 | 2% | 1% | 0% | 0% | 0% | 0% |
| Financials | 32 | 0% | 0% | 0% | 0% | 0% | 0% |
| **All** | 763 | 4% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 4 | 1% | -$35.65 | -39% | — |
| Sell at 2¢ | 27 | 4% | -$84.63 | -92% | 62 sec |
| Sell at 3¢ | 16 | 2% | -$85.41 | -93% | 72 sec |
| Sell at 5¢ | 9 | 1% | -$85.80 | -94% | 2.2 min |
| Sell at 10¢ | 8 | 1% | -$81.17 | -89% | 2.7 min |
| Sell at 25¢ | 5 | 1% | -$75.10 | -82% | 3.2 min |
| Sell at 50¢ | 4 | 1% | -$64.65 | -71% | 4.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 25 | 2 | 12% | 8% | +647% | -79% | -69% |
| 2–5 min | 260 | 2 | 7% | 2% | -24% | -87% | -90% |
| 1–2 min | 237 | 0 | 2% | 0% | -100% | -96% | -96% |
| Under 1 min | 241 | 0 | 0% | 0% | -100% | -99% | -98% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 57 | 2 | 5% | 4% | +355% | -87% | -81% |
| XRP | 57 | 2 | 5% | 4% | +315% | -88% | -88% |
| ZEC | 57 | 0 | 5% | 0% | -100% | -88% | -100% |
| DOGE | 56 | 0 | 5% | 2% | -100% | -89% | -83% |
| NEAR | 55 | 0 | 2% | 0% | -100% | -96% | -100% |
| BTC | 55 | 0 | 11% | 4% | -100% | -71% | -78% |
| SOL | 55 | 0 | 4% | 2% | -100% | -91% | -86% |
| BNB | 54 | 0 | 2% | 0% | -100% | -96% | -94% |
| HYPE | 50 | 0 | 2% | 0% | -100% | -95% | -100% |
| GOLD | 43 | 0 | 2% | 0% | -100% | -95% | -100% |
| WTI | 39 | 0 | 3% | 0% | -100% | -95% | -100% |
| SILVER | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 33 | 0 | 6% | 3% | -100% | -89% | -84% |
| PLATINUM | 31 | 0 | 0% | 0% | -100% | -100% | -100% |
| COPPER | 29 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 24 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 14 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 12 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 6 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 412 | 3 | 4% | 1% | -12% | -92% | -92% |
| DOWN (bought NO) | 351 | 1 | 3% | 1% | -68% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 42 | 0 | 2% | 2% | -100% | -90% | -86% |
| 0.05–0.1% | 50 | 0 | 2% | 0% | -100% | -94% | -100% |
| 0.1–0.2% | 117 | 0 | 3% | 0% | -100% | -91% | -89% |
| 0.2–0.5% | 210 | 2 | 5% | 2% | +3% | -90% | -91% |
| Over 0.5% | 77 | 2 | 8% | 3% | +187% | -84% | -84% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 179 | 1 | 3% | 1% | -37% | -93% | -96% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,902 |
| Time from buy to best bounce (bounced bets) | 47 sec |
| Price snapshots per bet | 46 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 8:59:39 AM | XRP | UP | 20 sec | -0.094% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:39 AM | BTC | DOWN | 20 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:39 AM | SOL | UP | 20 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:59:23 AM | BNB | UP | 36 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:59:23 AM | HYPE | DOWN | 36 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:58:33 AM | NATGAS | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:33 AM | EURUSD | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:33 AM | ETH | DOWN | 87 sec | +0.145% | 4¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:02 AM | DOGE | DOWN | 1.9 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:58:02 AM | PLATINUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:57:46 AM | NEAR | DOWN | 2.2 min | +0.956% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:57:30 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:55:03 AM | WTI | DOWN | 5.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:53:26 AM | ZEC | UP | 6.6 min | -2.161% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:37 AM | ZEC | UP | 23 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:21 AM | BNB | UP | 39 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:06 AM | XRP | UP | 54 sec | -0.729% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:06 AM | SOL | UP | 54 sec | -0.432% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:06 AM | HYPE | UP | 54 sec | -0.314% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:44:06 AM | DOGE | UP | 54 sec | -0.628% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:44:06 AM | ETH | UP | 54 sec | -0.327% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:43:48 AM | BTC | UP | 72 sec | -0.262% | 0¢ | ❌ Lost | $0.00 |
| 9/28 8:43:32 AM | GBPUSD | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:43:01 AM | COPPER | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:43:01 AM | NEAR | UP | 2.0 min | -1.168% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:42:29 AM | WTI | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:41:23 AM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:41:07 AM | PLATINUM | UP | 3.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 8:40:20 AM | GOLD | UP | 4.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 8:40:04 AM | ETH | DOWN | 4.9 min | +0.412% | 100¢ | ✅ Won | $13.85 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
