# 15-Minute 1¢ Study

*Updated Fri Nov 13, 11:36 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4285 finished bets | 1% | $168.35 | +35% | +3.93¢ | $80.65 / $87.70 |

*Expect about **92 buys a day** (~$13.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4028 | $95.35 | +22% |
| Volatility model ≥ 2%, hold to the close | 7915 | $27.35 | +3% |
| Momentum model ≥ 2%, hold to the close | 6572 | -$27.25 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56165 | 56144 | 213 (0%) | 1.07% | -$3,869.55 (-56%) | Hold to the close: -$3,869.55 (-56%) |

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
| Volatility model | 33465 | 4.7% | 0.4% (134) | -667% | ❌ Worse |
| Momentum model | 33465 | 4.6% | 0.4% (134) | -694% | ❌ Worse |
| Mean-reversion model | 33465 | 8.0% | 0.4% (134) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33465 | 134 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7915 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4285 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2483 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6572 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4028 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2642 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13775 | 94 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9606 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6402 | 56 | -1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33670 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13545 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8929 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56144 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 213 | 0% | -$3,869.55 | -56% | — |
| Sell at 2¢ | 2237 | 4% | -$5,975.93 | -87% | 47 sec |
| Sell at 3¢ | 1515 | 3% | -$5,966.70 | -87% | 48 sec |
| Sell at 5¢ | 1042 | 2% | -$5,852.25 | -85% | 63 sec |
| Sell at 10¢ | 633 | 1% | -$5,616.32 | -82% | 65 sec |
| Sell at 25¢ | 331 | 1% | -$5,223.94 | -76% | 82 sec |
| Sell at 50¢ | 218 | 0% | -$4,736.05 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2801 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18087 | 98 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14164 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 21079 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3769 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3765 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3759 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3745 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3745 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3740 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3720 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3720 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3707 | 14 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 2036 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2009 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1976 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1802 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1747 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1688 | 6 | 2% | 1% | -67% | -75% | -74% |
| GBPUSD | 1673 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1661 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1636 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1616 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1191 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1156 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 757 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 392 | 2 | 4% | 2% | -52% | -70% | -68% |
| 2YRRATE | 373 | 4 | 4% | 2% | +0% | -43% | -42% |
| 30YRRATE | 371 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 345 | 2 | 4% | 2% | -46% | -93% | -95% |
| INX | 45 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28524 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27620 | 103 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5278 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5675 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8587 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10206 | 42 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3916 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13594 | 63 | 4% | 2% | -47% | -85% | -85% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,810 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 11:29:49 AM | 10YRRATE | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | GBPUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | XRP | UP | 10 sec | -0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:29:49 AM | GOLD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:49 AM | COPPER | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:35 AM | SOL | DOWN | 25 sec | +0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:17 AM | NATGAS | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:29:01 AM | PLATINUM | DOWN | 58 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 11/13 11:28:45 AM | 30YRRATE | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:28:29 AM | WTI | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:28:29 AM | NEAR | DOWN | 1.5 min | +0.253% | 2¢ | ❌ Lost | $0.00 |
| 11/13 11:28:09 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:28:09 AM | BRENT | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:27:53 AM | DOGE | DOWN | 2.1 min | +0.232% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:27:53 AM | HYPE | DOWN | 2.1 min | +0.398% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:27:37 AM | BTC | DOWN | 2.4 min | +0.218% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:27:37 AM | INX | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:27:37 AM | ETH | DOWN | 2.4 min | +0.198% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:26:47 AM | AUDUSD | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:26:31 AM | XRP | DOWN | 3.5 min | +0.332% | 100¢ | ✅ Won | $13.85 |
| 11/13 11:26:16 AM | BNB | DOWN | 3.7 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:14:55 AM | AUDUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:14:55 AM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:14:55 AM | SILVER | UP | 5 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 11:14:55 AM | ETH | DOWN | 5 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:14:39 AM | SOL | DOWN | 21 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:14:39 AM | 10YRRATE | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:14:39 AM | BRENT | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 11:14:24 AM | WTI | DOWN | 36 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
