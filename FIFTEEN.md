# 15-Minute 1¢ Study

*Updated Sat Oct 17, 12:57 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1793 finished bets | 1% | $66.95 | +34% | +3.73¢ | $42.35 / $24.60 |

*Expect about **92 buys a day** (~$13.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1648 | $30.75 | +17% |
| Momentum model ≥ 2%, hold to the close | 2769 | -$27.60 | -9% |
| Volatility model ≥ 5%, sell at 50¢ | 1793 | -$35.55 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22043 | 22034 | 82 (0%) | 1.07% | -$1,529.20 (-57%) | Hold to the close: -$1,529.20 (-57%) |

*In play or awaiting result: 8. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 14310 | 4.5% | 0.4% (56) | -664% | ❌ Worse |
| Momentum model | 14310 | 4.5% | 0.4% (56) | -685% | ❌ Worse |
| Mean-reversion model | 14310 | 7.5% | 0.4% (56) | -799% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14310 | 56 | -51% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3248 | 24 | -15% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1793 | 19 | +34% | -75% | -74% | -70% |
| Volatility model ≥ 10% | 1050 | 11 | +49% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2769 | 21 | -9% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1648 | 15 | +17% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1094 | 10 | +28% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5474 | 35 | -30% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3785 | 27 | -21% | -82% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2500 | 16 | -27% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14508 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22034 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 82 | 0% | -$1,529.20 | -57% | — |
| Sell at 2¢ | 795 | 4% | -$2,372.50 | -89% | 37 sec |
| Sell at 3¢ | 535 | 2% | -$2,370.55 | -89% | 47 sec |
| Sell at 5¢ | 385 | 2% | -$2,328.95 | -87% | 50 sec |
| Sell at 10¢ | 232 | 1% | -$2,247.28 | -84% | 63 sec |
| Sell at 25¢ | 130 | 1% | -$2,078.90 | -78% | 80 sec |
| Sell at 50¢ | 85 | 0% | -$1,865.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 772 | 5 | 10% | 3% | -39% | -82% | -85% |
| 2–5 min | 7139 | 38 | 7% | 3% | -48% | -88% | -87% |
| 1–2 min | 5709 | 20 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 8410 | 19 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1631 | 11 | 4% | 2% | -16% | -90% | -90% |
| HYPE | 1623 | 6 | 4% | 2% | -55% | -90% | -88% |
| ETH | 1616 | 8 | 6% | 3% | -40% | -87% | -86% |
| BNB | 1615 | 6 | 5% | 2% | -54% | -89% | -89% |
| DOGE | 1614 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1609 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1602 | 7 | 3% | 1% | -46% | -86% | -87% |
| NEAR | 1600 | 8 | 6% | 3% | -35% | -78% | -78% |
| BTC | 1598 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11119 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 10915 | 41 | 4% | 2% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2470 | 12 | 2% | 1% | -19% | -81% | -81% |
| 0.05–0.1% | 2513 | 7 | 3% | 1% | -60% | -92% | -91% |
| 0.1–0.2% | 3648 | 12 | 5% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4213 | 21 | 6% | 3% | -45% | -88% | -88% |
| Over 0.5% | 1661 | 6 | 6% | 3% | -63% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5130 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,596 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 12:57:41 PM | DOGE | DOWN | 2.3 min | +0.131% | — | In play | — |
| 10/17 12:57:41 PM | XRP | DOWN | 2.3 min | +0.069% | — | In play | — |
| 10/17 12:44:51 PM | BNB | DOWN | 8 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:51 PM | BTC | UP | 8 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:44:19 PM | ETH | UP | 40 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:45 PM | DOGE | DOWN | 75 sec | +0.084% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:43:45 PM | XRP | DOWN | 75 sec | +0.039% | 2¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:58 PM | SOL | DOWN | 2.0 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:58 PM | NEAR | DOWN | 2.0 min | +0.229% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:42:25 PM | ZEC | DOWN | 2.6 min | +0.368% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:29:47 PM | BNB | DOWN | 12 sec | -0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:59 PM | NEAR | DOWN | 61 sec | +0.024% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:28:59 PM | BTC | DOWN | 61 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 10/17 12:28:27 PM | XRP | DOWN | 1.6 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | ZEC | DOWN | 3.3 min | +0.418% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | DOGE | DOWN | 3.3 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | SOL | DOWN | 3.3 min | +0.164% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | ETH | DOWN | 3.3 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:26:41 PM | HYPE | DOWN | 3.3 min | +0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:13:01 PM | HYPE | DOWN | 2.0 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:12 PM | SOL | DOWN | 2.8 min | +0.162% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:12:12 PM | XRP | DOWN | 2.8 min | +0.209% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:11:57 PM | BNB | DOWN | 3.0 min | +0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 12:11:40 PM | ZEC | DOWN | 3.3 min | +0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:10:53 PM | ETH | DOWN | 4.1 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:10:53 PM | BTC | DOWN | 4.1 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:10:37 PM | DOGE | DOWN | 4.4 min | +0.216% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 12:09:01 PM | NEAR | DOWN | 6.0 min | +0.815% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 11:59:12 AM | XRP | DOWN | 47 sec | +0.031% | 1¢ | ❌ Lost | $0.00 |
| 10/17 11:58:40 AM | BNB | DOWN | 79 sec | +0.024% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
