# 15-Minute 1¢ Study

*Updated Sat Oct 17, 5:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1842 finished bets | 1% | $89.40 | +44% | +4.85¢ | $39.80 / $49.60 |

*Expect about **93 buys a day** (~$14.01/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1687 | $54.40 | +30% |
| Momentum model ≥ 2%, hold to the close | 2825 | -$6.20 | -2% |
| Volatility model ≥ 2%, hold to the close | 3318 | -$23.85 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 22213 | 22206 | 85 (0%) | 1.07% | -$1,506.10 (-56%) | Hold to the close: -$1,506.10 (-56%) |

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
| Volatility model | 14482 | 4.6% | 0.4% (59) | -653% | ❌ Worse |
| Momentum model | 14482 | 4.5% | 0.4% (59) | -676% | ❌ Worse |
| Mean-reversion model | 14482 | 7.6% | 0.4% (59) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 14482 | 59 | -49% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3318 | 27 | -6% | -79% | -79% | -75% |
| Volatility model ≥ 5% | 1842 | 21 | +44% | -75% | -74% | -71% |
| Volatility model ≥ 10% | 1079 | 13 | +71% | -68% | -67% | -64% |
| Momentum model ≥ 2% | 2825 | 23 | -2% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 1687 | 17 | +30% | -78% | -78% | -74% |
| Momentum model ≥ 10% | 1125 | 12 | +49% | -74% | -74% | -69% |
| Mean-reversion model ≥ 2% | 5558 | 38 | -25% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3844 | 30 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2545 | 19 | -14% | -80% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 14680 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5309 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 22206 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 85 | 0% | -$1,506.10 | -56% | — |
| Sell at 2¢ | 804 | 4% | -$2,389.06 | -89% | 39 sec |
| Sell at 3¢ | 542 | 2% | -$2,386.72 | -89% | 47 sec |
| Sell at 5¢ | 391 | 2% | -$2,343.95 | -87% | 50 sec |
| Sell at 10¢ | 238 | 1% | -$2,258.32 | -84% | 63 sec |
| Sell at 25¢ | 134 | 1% | -$2,084.56 | -77% | 79 sec |
| Sell at 50¢ | 88 | 0% | -$1,864.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 783 | 5 | 10% | 3% | -39% | -82% | -84% |
| 2–5 min | 7186 | 38 | 7% | 3% | -48% | -88% | -88% |
| 1–2 min | 5753 | 23 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8480 | 19 | 1% | 0% | -68% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1649 | 11 | 4% | 2% | -17% | -90% | -90% |
| HYPE | 1642 | 6 | 5% | 2% | -55% | -90% | -88% |
| ETH | 1636 | 9 | 6% | 3% | -34% | -87% | -86% |
| BNB | 1636 | 7 | 5% | 2% | -48% | -89% | -89% |
| DOGE | 1633 | 2 | 4% | 2% | -85% | -91% | -90% |
| SOL | 1627 | 2 | 4% | 2% | -85% | -92% | -92% |
| XRP | 1621 | 7 | 3% | 1% | -47% | -86% | -87% |
| NEAR | 1619 | 9 | 6% | 3% | -28% | -78% | -78% |
| BTC | 1617 | 8 | 5% | 2% | -33% | -88% | -91% |
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
| UP (bought YES) | 11188 | 41 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11018 | 44 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2517 | 13 | 2% | 1% | -14% | -81% | -81% |
| 0.05–0.1% | 2549 | 8 | 3% | 2% | -54% | -91% | -91% |
| 0.1–0.2% | 3678 | 13 | 5% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 4256 | 21 | 6% | 3% | -46% | -88% | -88% |
| Over 0.5% | 1677 | 6 | 6% | 3% | -63% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5566 | 22 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5315 | 27 | 4% | 2% | -42% | -87% | -86% |
| Afternoon (12–6pm) | 5302 | 19 | 3% | 1% | -57% | -88% | -89% |
| Evening (6pm–12am) | 6023 | 17 | 3% | 2% | -68% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/17 5:44:33 PM | ETH | DOWN | 27 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:44:17 PM | SOL | DOWN | 43 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:46 PM | ZEC | DOWN | 74 sec | +0.230% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:46 PM | NEAR | DOWN | 74 sec | +0.226% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:29 PM | BTC | DOWN | 1.5 min | +0.111% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:43:29 PM | HYPE | DOWN | 1.5 min | +0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:43:13 PM | DOGE | DOWN | 1.8 min | +0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:42:57 PM | XRP | DOWN | 2.0 min | +0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:42:26 PM | BNB | DOWN | 2.6 min | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:29:46 PM | ETH | DOWN | 14 sec | +0.028% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:29:30 PM | SOL | UP | 30 sec | -0.121% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:28:26 PM | BTC | UP | 1.6 min | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:28:10 PM | DOGE | UP | 1.8 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:27:23 PM | HYPE | UP | 2.6 min | -0.379% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:26:51 PM | XRP | UP | 3.1 min | -0.279% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:26:51 PM | NEAR | UP | 3.1 min | -0.742% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:26:51 PM | BNB | UP | 3.1 min | -0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:14:45 PM | ETH | DOWN | 15 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:14:29 PM | XRP | UP | 31 sec | -0.077% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:14:29 PM | BTC | UP | 31 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:14:29 PM | SOL | DOWN | 31 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:13:57 PM | ZEC | UP | 63 sec | -0.258% | 0¢ | ❌ Lost | $0.00 |
| 10/17 5:13:57 PM | HYPE | UP | 63 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:26 PM | DOGE | DOWN | 1.6 min | +0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 5:13:10 PM | BNB | DOWN | 1.8 min | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 5:12:54 PM | NEAR | UP | 2.1 min | -0.632% | 1¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:48 PM | ETH | UP | 12 sec | -0.111% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:32 PM | XRP | UP | 28 sec | -0.108% | 0¢ | ❌ Lost | -$0.15 |
| 10/17 4:59:32 PM | BTC | UP | 28 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/17 4:59:32 PM | DOGE | DOWN | 28 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
