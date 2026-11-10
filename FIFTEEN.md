# 15-Minute 1¢ Study

*Updated Mon Nov 9, 11:52 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4143 finished bets | 1% | $183.65 | +40% | +4.43¢ | $89.65 / $94.00 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3849 | $101.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 7575 | $68.45 | +8% |
| Momentum model ≥ 2%, hold to the close | 6268 | -$5.55 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51746 | 51729 | 199 (0%) | 1.07% | -$3,514.75 (-56%) | Hold to the close: -$3,514.75 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31422 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31422 | 4.6% | 0.4% (128) | -702% | ❌ Worse |
| Mean-reversion model | 31422 | 8.1% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31422 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7575 | 70 | +8% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4143 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2387 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6268 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3849 | 37 | +24% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2526 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13006 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9122 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6098 | 56 | +5% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31627 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12262 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7840 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51729 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,514.75 | -56% | — |
| Sell at 2¢ | 2063 | 4% | -$5,484.37 | -87% | 47 sec |
| Sell at 3¢ | 1405 | 3% | -$5,472.80 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,354.45 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,129.30 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,757.41 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,315.00 | -68% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2574 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16714 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13074 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19355 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3542 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3538 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3529 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3522 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3518 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3513 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3492 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3492 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3481 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1860 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1833 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1811 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1641 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1576 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1539 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1502 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1495 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1477 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1474 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1035 | 5 | 2% | 1% | -55% | -87% | -87% |
| USDCAD | 1004 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 599 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26219 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25510 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5087 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5407 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8132 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9452 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3541 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14098 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,909 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 11:44:57 PM | GOLD | DOWN | 2 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:57 PM | PLATINUM | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:57 PM | SOL | DOWN | 2 sec | -0.004% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:44:41 PM | SILVER | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | USDCAD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | HYPE | DOWN | 34 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:25 PM | DOGE | DOWN | 34 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:44:25 PM | AUDUSD | UP | 34 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | ZEC | DOWN | 50 sec | +0.116% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | XRP | DOWN | 50 sec | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:44:09 PM | EURUSD | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:43:53 PM | PALLADIUM | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:43:53 PM | NEAR | DOWN | 66 sec | +0.188% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:43:38 PM | BNB | UP | 82 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:43:22 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:43:06 PM | ETH | UP | 1.9 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:42:50 PM | BRENT | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:42:18 PM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:39:13 PM | USDJPY | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:29:54 PM | HYPE | UP | 6 sec | -0.082% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:29:38 PM | PALLADIUM | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:29:38 PM | SILVER | UP | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/9 11:29:22 PM | ETH | DOWN | 38 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/9 11:29:22 PM | COPPER | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:29:06 PM | ZEC | DOWN | 54 sec | +0.161% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:28:50 PM | BNB | UP | 69 sec | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:28:50 PM | PLATINUM | UP | 69 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:28:34 PM | WTI | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:28:18 PM | USDJPY | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 11:28:18 PM | BRENT | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
