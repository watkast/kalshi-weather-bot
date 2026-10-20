# 15-Minute 1¢ Study

*Updated Mon Oct 19, 9:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2074 finished bets | 1% | $89.35 | +38% | +4.31¢ | $26.60 / $62.75 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1911 | $70.15 | +33% |
| Momentum model ≥ 2%, hold to the close | 3189 | -$9.80 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 2074 | -$27.65 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24519 | 24511 | 90 (0%) | 1.07% | -$1,716.75 (-58%) | Hold to the close: -$1,716.75 (-58%) |

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
| Volatility model | 16090 | 4.6% | 0.4% (64) | -672% | ❌ Worse |
| Momentum model | 16090 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 16090 | 7.7% | 0.4% (64) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16090 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3756 | 30 | -8% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2074 | 23 | +38% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 1210 | 15 | +74% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3189 | 26 | -3% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1911 | 20 | +33% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 1269 | 13 | +41% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6273 | 41 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4360 | 33 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2883 | 22 | -13% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16288 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5743 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2480 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24511 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,716.75 | -58% | — |
| Sell at 2¢ | 886 | 4% | -$2,634.39 | -88% | 45 sec |
| Sell at 3¢ | 598 | 2% | -$2,631.53 | -88% | 47 sec |
| Sell at 5¢ | 427 | 2% | -$2,587.20 | -87% | 50 sec |
| Sell at 10¢ | 260 | 1% | -$2,496.15 | -84% | 64 sec |
| Sell at 25¢ | 143 | 1% | -$2,307.42 | -78% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,083.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 943 | 5 | 10% | 3% | -49% | -82% | -84% |
| 2–5 min | 7948 | 40 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6259 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9357 | 21 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1831 | 11 | 4% | 2% | -25% | -90% | -90% |
| HYPE | 1820 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1819 | 9 | 5% | 2% | -39% | -82% | -81% |
| ETH | 1810 | 9 | 6% | 3% | -40% | -87% | -86% |
| DOGE | 1810 | 3 | 4% | 2% | -79% | -91% | -90% |
| SOL | 1806 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1799 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1797 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1796 | 10 | 5% | 2% | -25% | -88% | -90% |
| GOLD | 941 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 913 | 4 | 3% | 1% | -49% | -81% | -81% |
| WTI | 883 | 3 | 3% | 1% | -60% | -94% | -96% |
| COPPER | 790 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 780 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 724 | 5 | 2% | 2% | -36% | -84% | -82% |
| EURUSD | 720 | 3 | 2% | 1% | -61% | -83% | -83% |
| PALLADIUM | 712 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 676 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 627 | 3 | 1% | 1% | -55% | -99% | -98% |
| AUDUSD | 256 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 201 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12341 | 43 | 4% | 2% | -60% | -89% | -88% |
| DOWN (bought NO) | 12170 | 47 | 3% | 1% | -55% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2768 | 15 | 2% | 1% | -10% | -76% | -76% |
| 0.05–0.1% | 2830 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4086 | 13 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 4755 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1846 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6826 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 9:53:15 PM | HYPE | DOWN | 6.7 min | +0.241% | — | In play | — |
| 10/19 9:44:57 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | PALLADIUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | USDJPY | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:42 PM | AUDUSD | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:44:05 PM | EURUSD | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:43:34 PM | GBPUSD | DOWN | 86 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:43:02 PM | PLATINUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:42:46 PM | WTI | UP | 2.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/19 9:42:30 PM | SILVER | DOWN | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:41:58 PM | GOLD | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:41:25 PM | COPPER | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:41:25 PM | BNB | DOWN | 3.6 min | +0.084% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 9:40:38 PM | HYPE | DOWN | 4.3 min | +0.277% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:39:50 PM | SOL | DOWN | 5.2 min | +0.327% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 9:39:50 PM | BTC | DOWN | 5.2 min | +0.241% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 9:39:50 PM | ZEC | DOWN | 5.2 min | +0.757% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:39:04 PM | XRP | DOWN | 5.9 min | +0.292% | 2¢ | ❌ Lost | -$0.15 |
| 10/19 9:38:48 PM | ETH | DOWN | 6.2 min | +0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:38:17 PM | NEAR | DOWN | 6.7 min | +0.829% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:38:17 PM | DOGE | DOWN | 6.7 min | +0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:48 PM | AUDUSD | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:33 PM | XRP | UP | 27 sec | -0.061% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:17 PM | ETH | UP | 43 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 10/19 9:29:17 PM | BTC | UP | 43 sec | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:17 PM | NEAR | UP | 43 sec | -0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:17 PM | BNB | UP | 43 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:17 PM | GOLD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:29:01 PM | DOGE | UP | 59 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 9:28:45 PM | PLATINUM | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
